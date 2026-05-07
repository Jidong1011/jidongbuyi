#!/bin/bash
# 保存笔记图片到指定目录

# 获取当前时间戳
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

# 目标目录
TARGET_DIR="/workspace/projects/workspace/media/notes"

# 创建目录（如果不存在）
mkdir -p "$TARGET_DIR"

# 输出目标路径
echo "$TARGET_DIR/$TIMESTAMP.jpg"