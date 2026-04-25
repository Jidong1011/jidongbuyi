#!/bin/bash
# Dream Cycle - 夜间维护脚本
# 每天凌晨3点运行
# 功能：
# 1. 扫描今日对话
# 2. 识别新实体
# 3. 更新实体文件
# 4. 修复断裂链接
# 5. 导入新记忆到向量库

echo "=== Dream Cycle Started: $(date) ==="

# 1. 导入今日新记忆
echo "[1/4] Importing today's memories..."
python3 /workspace/projects/workspace/scripts/gbrain_core.py init

# 2. 扫描memory/daily-raw/下的新素材
echo "[2/4] Processing daily raw materials..."
TODAY=$(date +%Y-%m-%d)
RAW_FILE="/workspace/projects/workspace/memory/daily-raw/${TODAY}.md"

if [ -f "$RAW_FILE" ]; then
    echo "Found raw materials for today"
    # 提取关键信息（简化版）
    grep -E "^\[|^- |^## " "$RAW_FILE" | head -20 >> /workspace/projects/workspace/memory/daily/${TODAY}.md
fi

# 3. 检查是否有新实体需要创建
echo "[3/4] Checking for new entities..."
python3 << 'PYEOF'
import os
import re
from datetime import datetime

memory_dir = "/workspace/projects/workspace/memory/daily"
entities_dir = "/workspace/projects/workspace/entities"

# 扫描最近3天的记忆
new_entities = []
for i in range(3):
    date_str = (datetime.now() - __import__('datetime').timedelta(days=i)).strftime('%Y-%m-%d')
    file_path = os.path.join(memory_dir, f"{date_str}.md")
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        
        # 简单的人名检测（中文2-4字，或英文首字母大写）
        chinese_names = re.findall(r'[^\w\s][\u4e00-\u9fa5]{2,4}(?=[，。、\s])', content)
        for name in chinese_names:
            name = name.strip('，。、\s')
            if name and len(name) >= 2:
                new_entities.append((name, 'people'))

# 去重
new_entities = list(set(new_entities))

# 创建实体文件模板
for name, etype in new_entities[:5]:  # 最多处理5个新实体
    entity_file = os.path.join(entities_dir, etype, f"{name}.md")
    if not os.path.exists(entity_file) and name not in ['东东', '今天', '明天']:
        with open(entity_file, 'w') as f:
            f.write(f"# {name}\n\n")
            f.write("> 类型：{etype}\n")
            f.write(f"> 自动创建：{datetime.now().strftime('%Y-%m-%d')}\n\n")
            f.write("---\n\n## 已整理事实\n\n")
            f.write("（待补充）\n\n")
            f.write("---\n\n## 时间线\n\n")
        print(f"Created entity: {name}")

PYEOF

# 4. 健康检查
echo "[4/4] Health check..."
VECTOR_COUNT=$(python3 -c "
import chromadb
client = chromadb.PersistentClient('/workspace/projects/workspace/memory/vector_db')
coll = client.get_collection('openclaw_memory')
print(coll.count())
" 2>/dev/null || echo "0")

echo "Total vectors in brain: $VECTOR_COUNT"

echo "=== Dream Cycle Completed: $(date) ==="
