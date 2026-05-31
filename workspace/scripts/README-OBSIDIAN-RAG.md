# Obsidian RAG 使用说明

## 📦 已安装组件

| 组件 | 说明 | 状态 |
|------|------|------|
| chromadb | 向量数据库 | ✅ 已安装 |
| sentence-transformers | Embedding模型 | 🔄 安装中 |
| ollama | 本地LLM（可选） | ⏳ 需手动安装 |

---

## 🚀 快速开始

### 1. 首次索引

```bash
cd /workspace/projects/workspace
python3 scripts/obsidian-rag.py index
```

### 2. 语义搜索

```bash
python3 scripts/obsidian-rag.py search "OPC创业"
```

### 3. RAG问答（需要Ollama）

```bash
# 先安装Ollama
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull qwen2.5:7b

# 然后提问
python3 scripts/obsidian-rag.py ask "我之前对AI经济危机有什么思考？"
```

### 4. 查看统计

```bash
python3 scripts/obsidian-rag.py stats
```

---

## ⚙️ 配置

环境变量：
```bash
export OBSIDIAN_PATH="/path/to/your/obsidian/vault"
export VECTOR_DB_PATH="/path/to/vector/db"
```

---

## 📁 文件结构

```
scripts/
├── obsidian-rag.py      # 主脚本
└── README-OBSIDIAN-RAG.md  # 本文档

memory/
└── vector_db/           # 向量数据库
    └── chroma.sqlite3
```

---

## 🔧 常见问题

### Q: 如何重新索引？
A: 使用 `--force` 参数：
```bash
python3 scripts/obsidian-rag.py index --force
```

### Q: 如何调整返回结果数量？
A: 使用 `--top-k` 参数：
```bash
python3 scripts/obsidian-rag.py search "问题" --top-k 10
```

### Q: 支持哪些文件类型？
A: 目前仅支持 `.md` 和 `.MD` 文件。
