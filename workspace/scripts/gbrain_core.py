#!/usr/bin/env python3
"""
GBrain Core - 混合搜索系统
结合向量搜索（语义）+ 关键词搜索（精确）
"""

import os
import json
import chromadb
from chromadb.config import Settings
from datetime import datetime
import re

# 初始化ChromaDB
chroma_client = chromadb.PersistentClient(
    path="/workspace/projects/workspace/memory/vector_db",
    settings=Settings(anonymized_telemetry=False)
)

# 获取或创建集合
collection = chroma_client.get_or_create_collection(
    name="openclaw_memory",
    metadata={"hnsw:space": "cosine"}
)

def ingest_memory(content, metadata):
    """摄入新记忆到向量数据库"""
    doc_id = f"{metadata['type']}_{metadata['date']}_{hash(content) & 0xFFFFFFFF}"
    
    collection.add(
        documents=[content],
        metadatas=[metadata],
        ids=[doc_id]
    )
    return doc_id

def hybrid_search(query, n_results=5):
    """混合搜索：向量搜索 + 关键词过滤"""
    # 向量搜索（语义相似度）
    vector_results = collection.query(
        query_texts=[query],
        n_results=n_results * 2  # 多取一些用于后续过滤
    )
    
    results = []
    if vector_results['documents'] and vector_results['documents'][0]:
        for i, doc in enumerate(vector_results['documents'][0]):
            metadata = vector_results['metadatas'][0][i]
            distance = vector_results['distances'][0][i]
            
            # 关键词匹配加分
            keyword_score = keyword_match_score(query, doc)
            
            # 综合得分：向量距离 + 关键词匹配
            results.append({
                'content': doc,
                'metadata': metadata,
                'vector_score': 1 - distance,  # 转换为相似度
                'keyword_score': keyword_score,
                'combined_score': (1 - distance) * 0.7 + keyword_score * 0.3
            })
    
    # 按综合得分排序
    results.sort(key=lambda x: x['combined_score'], reverse=True)
    return results[:n_results]

def keyword_match_score(query, document):
    """计算关键词匹配得分"""
    query_words = set(re.findall(r'\w+', query.lower()))
    doc_words = set(re.findall(r'\w+', document.lower()))
    
    if not query_words:
        return 0
    
    matches = query_words & doc_words
    return len(matches) / len(query_words)

def search_recent(days=7, query=None):
    """搜索近期记忆"""
    from datetime import datetime, timedelta
    cutoff = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    
    # 从向量库搜索
    if query:
        results = hybrid_search(query, n_results=10)
        return [r for r in results if r['metadata'].get('date', '') >= cutoff]
    else:
        # 获取所有近期记录
        all_results = collection.get()
        recent = []
        if all_results['metadatas']:
            for i, meta in enumerate(all_results['metadatas']):
                if meta.get('date', '') >= cutoff:
                    recent.append({
                        'content': all_results['documents'][i],
                        'metadata': meta
                    })
        return recent[:10]

def ingest_from_daily_file(file_path):
    """从daily文件摄入记忆"""
    if not os.path.exists(file_path):
        return 0
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 解析日期
    date_str = os.path.basename(file_path).replace('.md', '')
    
    # 简单分块（按事件/洞察/决策等）
    sections = re.split(r'\n## ', content)
    
    count = 0
    for section in sections:
        if not section.strip():
            continue
        
        # 判断类型
        section_type = 'event'
        if '[INSIGHT]' in section:
            section_type = 'insight'
        elif '[DECISION]' in section:
            section_type = 'decision'
        elif '[INTERACTION]' in section:
            section_type = 'interaction'
        
        ingest_memory(section, {
            'date': date_str,
            'type': section_type,
            'source': file_path
        })
        count += 1
    
    return count

def init_from_existing_memory():
    """初始化：导入所有现有记忆文件"""
    memory_dir = "/workspace/projects/workspace/memory/daily"
    
    if not os.path.exists(memory_dir):
        print(f"Memory directory not found: {memory_dir}")
        return 0
    
    total = 0
    for filename in os.listdir(memory_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(memory_dir, filename)
            count = ingest_from_daily_file(file_path)
            total += count
            print(f"Imported {count} entries from {filename}")
    
    return total

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "init":
            print("Initializing GBrain from existing memory files...")
            count = init_from_existing_memory()
            print(f"Total imported: {count} entries")
        
        elif sys.argv[1] == "search" and len(sys.argv) > 2:
            query = sys.argv[2]
            results = hybrid_search(query)
            print(f"\nSearch results for: '{query}'\n")
            for i, r in enumerate(results, 1):
                print(f"{i}. [{r['metadata']['type']}] {r['metadata']['date']}")
                print(f"   Score: {r['combined_score']:.3f}")
                print(f"   {r['content'][:150]}...\n")
        
        elif sys.argv[1] == "recent":
            days = int(sys.argv[2]) if len(sys.argv) > 2 else 7
            results = search_recent(days)
            print(f"\nRecent {days} days memory:\n")
            for i, r in enumerate(results, 1):
                print(f"{i}. [{r['metadata']['type']}] {r['metadata']['date']}")
                print(f"   {r['content'][:150]}...\n")
    else:
        print("Usage:")
        print("  python gbrain_core.py init")
        print("  python gbrain_core.py search 'your query'")
        print("  python gbrain_core.py recent [days]")
