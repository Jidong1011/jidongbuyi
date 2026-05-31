#!/usr/bin/env python3
"""
Obsidian RAG - 本地知识库智能检索系统
=====================================
将Obsidian笔记向量化，支持语义搜索和RAG问答。

使用方法：
1. 配置OBSIDIAN_PATH指向你的Obsidian库
2. 运行 python3 obsidian-rag.py index  # 首次索引
3. 运行 python3 obsidian-rag.py search "你的问题"  # 语义搜索
4. 运行 python3 obsidian-rag.py ask "你的问题"  # RAG问答（需要Ollama）
"""

import os
import sys
import json
import glob
import hashlib
from pathlib import Path
from datetime import datetime

# ============ 配置 ============
# Obsidian库路径（修改为你的路径）
OBSIDIAN_PATH = os.environ.get("OBSIDIAN_PATH", "/workspace/projects/workspace")

# 向量数据库路径
VECTOR_DB_PATH = os.environ.get("VECTOR_DB_PATH", "/workspace/projects/workspace/memory/vector_db")

# Embedding模型（本地模型，无需API）
EMBEDDING_MODEL = "all-MiniLM-L6-v2"  # 轻量快速

# 文档分块大小（字符数）
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# ============ 导入库 ============
try:
    import chromadb
    from chromadb.config import Settings
except ImportError:
    print("❌ 请先安装chromadb: pip install chromadb")
    sys.exit(1)

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("❌ 请先安装sentence-transformers: pip install sentence-transformers")
    sys.exit(1)


class ObsidianRAG:
    def __init__(self):
        """初始化RAG系统"""
        self.obsidian_path = Path(OBSIDIAN_PATH)
        self.vector_db_path = Path(VECTOR_DB_PATH)
        self.vector_db_path.mkdir(parents=True, exist_ok=True)
        
        # 初始化Chroma
        self.chroma_client = chromadb.PersistentClient(path=str(self.vector_db_path))
        
        # 初始化Embedding模型
        print(f"📦 加载Embedding模型: {EMBEDDING_MODEL}")
        self.embedding_model = SentenceTransformer(EMBEDDING_MODEL)
        
        # 获取或创建集合
        self.collection = self.chroma_client.get_or_create_collection(
            name="obsidian_notes",
            metadata={"hnsw:space": "cosine"}
        )
    
    def get_md_files(self):
        """获取所有Markdown文件"""
        md_files = []
        for pattern in ["**/*.md", "**/*.MD"]:
            md_files.extend(self.obsidian_path.glob(pattern))
        # 过滤隐藏目录和node_modules
        md_files = [
            f for f in md_files 
            if not any(part.startswith('.') for part in f.parts)
            and 'node_modules' not in str(f)
            and '.git' not in str(f)
        ]
        return md_files
    
    def read_file(self, filepath):
        """读取文件内容"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"⚠️ 读取失败: {filepath} - {e}")
            return None
    
    def chunk_text(self, text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
        """将文本分块"""
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            if chunk.strip():
                chunks.append(chunk)
            start += chunk_size - overlap
        return chunks
    
    def index(self, force=False):
        """索引所有笔记"""
        md_files = self.get_md_files()
        print(f"📚 找到 {len(md_files)} 个Markdown文件")
        
        if not force and self.collection.count() > 0:
            print(f"✅ 已有 {self.collection.count()} 条记录，使用 --force 重新索引")
            return
        
        # 清空现有数据
        if force:
            self.chroma_client.delete_collection("obsidian_notes")
            self.collection = self.chroma_client.get_or_create_collection(
                name="obsidian_notes",
                metadata={"hnsw:space": "cosine"}
            )
        
        # 批量处理
        batch_ids = []
        batch_texts = []
        batch_metadatas = []
        total_chunks = 0
        
        for i, md_file in enumerate(md_files):
            rel_path = md_file.relative_to(self.obsidian_path)
            content = self.read_file(md_file)
            if not content:
                continue
            
            chunks = self.chunk_text(content)
            for j, chunk in enumerate(chunks):
                chunk_id = f"{rel_path}_{j}_{hashlib.md5(chunk.encode()).hexdigest()[:8]}"
                batch_ids.append(chunk_id)
                batch_texts.append(chunk)
                batch_metadatas.append({
                    "source": str(rel_path),
                    "chunk_index": j,
                    "total_chunks": len(chunks)
                })
            
            total_chunks += len(chunks)
            
            # 每100个文件批量写入
            if len(batch_ids) >= 100:
                embeddings = self.embedding_model.encode(batch_texts).tolist()
                self.collection.add(
                    ids=batch_ids,
                    embeddings=embeddings,
                    documents=batch_texts,
                    metadatas=batch_metadatas
                )
                print(f"  📥 已处理 {i+1}/{len(md_files)} 文件, {total_chunks} 个片段")
                batch_ids, batch_texts, batch_metadatas = [], [], []
        
        # 处理剩余
        if batch_ids:
            embeddings = self.embedding_model.encode(batch_texts).tolist()
            self.collection.add(
                ids=batch_ids,
                embeddings=embeddings,
                documents=batch_texts,
                metadatas=batch_metadatas
            )
        
        print(f"✅ 索引完成！共 {total_chunks} 个片段")
    
    def search(self, query, top_k=5):
        """语义搜索"""
        if self.collection.count() == 0:
            print("❌ 索引为空，请先运行: python3 obsidian-rag.py index")
            return []
        
        query_embedding = self.embedding_model.encode([query]).tolist()
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=top_k
        )
        
        matches = []
        for i in range(len(results['ids'][0])):
            matches.append({
                'source': results['metadatas'][0][i]['source'],
                'chunk_index': results['metadatas'][0][i]['chunk_index'],
                'text': results['documents'][0][i],
                'distance': results['distances'][0][i]
            })
        return matches
    
    def ask(self, question, top_k=5):
        """RAG问答（需要Ollama）"""
        try:
            import ollama
        except ImportError:
            print("❌ 请先安装ollama: pip install ollama")
            print("   并运行: ollama pull qwen2.5:7b")
            return None
        
        # 检索相关片段
        matches = self.search(question, top_k)
        if not matches:
            return "没有找到相关内容"
        
        # 构建上下文
        context = "\n\n".join([
            f"[来源: {m['source']}]\n{m['text']}"
            for m in matches
        ])
        
        # RAG Prompt
        prompt = f"""你是一个基于个人知识库的AI助手。
以下是从知识库中检索到的相关笔记：

{context}

请基于以上笔记内容回答问题。如果有明确答案就引用来源，如果没有就说没有找到相关信息，不要编造。

问题：{question}"""
        
        try:
            response = ollama.chat(
                model='qwen2.5:7b',
                messages=[{'role': 'user', 'content': prompt}]
            )
            return response['message']['content']
        except Exception as e:
            return f"❌ Ollama调用失败: {e}\n请确保已运行: ollama pull qwen2.5:7b"
    
    def stats(self):
        """显示统计信息"""
        count = self.collection.count()
        md_files = self.get_md_files()
        print(f"📊 Obsidian RAG 统计")
        print(f"   笔记目录: {self.obsidian_path}")
        print(f"   向量数据库: {self.vector_db_path}")
        print(f"   Markdown文件数: {len(md_files)}")
        print(f"   索引片段数: {count}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Obsidian RAG - 本地知识库智能检索")
    parser.add_argument("action", choices=["index", "search", "ask", "stats"], help="操作类型")
    parser.add_argument("query", nargs="?", help="搜索或提问的内容")
    parser.add_argument("--force", action="store_true", help="强制重新索引")
    parser.add_argument("--top-k", type=int, default=5, help="返回结果数量")
    
    args = parser.parse_args()
    
    rag = ObsidianRAG()
    
    if args.action == "index":
        rag.index(force=args.force)
    elif args.action == "stats":
        rag.stats()
    elif args.action == "search":
        if not args.query:
            print("❌ 请提供搜索内容")
            return
        results = rag.search(args.query, args.top_k)
        print(f"\n🔍 搜索结果: {args.query}\n")
        for i, r in enumerate(results, 1):
            print(f"{'='*60}")
            print(f"#{i} | 相关度: {1-r['distance']:.2%} | 来源: {r['source']}")
            print(f"{'='*60}")
            print(r['text'][:300] + "..." if len(r['text']) > 300 else r['text'])
            print()
    elif args.action == "ask":
        if not args.query:
            print("❌ 请提供问题")
            return
        print(f"\n🤖 问答: {args.query}\n")
        answer = rag.ask(args.query, args.top_k)
        print(answer)


if __name__ == "__main__":
    main()
