#!/bin/bash
# OPC政策情报每日更新脚本
# 路径: /workspace/projects/workspace/opc-policy/update-policy.sh

POLICY_DB="/workspace/projects/workspace/opc-policy/policy-database.md"
TODAY=$(date +%Y-%m-%d)
TEMP_FILE="/workspace/projects/workspace/opc-policy/new-policies-${TODAY}.md"
COUNT=0

# 初始化临时文件
echo "# 新增政策 - ${TODAY}" > "$TEMP_FILE"
echo "" >> "$TEMP_FILE"

# 检查是否已有今天的更新标记
if grep -q "${TODAY}" "$POLICY_DB" 2>/dev/null; then
    echo "今天已更新过，跳过。"
    echo "新增政策数: 0"
    exit 0
fi

# 记录当前数据库行数（用于后续比对）
OLD_LINES=$(wc -l < "$POLICY_DB" 2>/dev/null || echo "0")

# 输出当前日期标记
echo "--- 更新日期: ${TODAY} ---" >> "$TEMP_FILE"

echo "更新完成 - ${TODAY}"
echo "数据库文件: ${POLICY_DB}"
