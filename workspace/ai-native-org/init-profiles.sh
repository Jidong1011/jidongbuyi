#!/bin/bash
# AI原生组织知识库 - Profile初始化脚本
# 用法：./init-profiles.sh <用户列表CSV>
# CSV格式：name,wecom_app_id（第一行为表头）

set -e

# 配置
BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
SHARED_DIR="$BASE_DIR/shared-skills"
PROFILES_DIR="$BASE_DIR/profiles"

echo "=========================================="
echo "AI原生组织知识库 - Profile初始化"
echo "=========================================="
echo "基础目录: $BASE_DIR"
echo ""

# 检查参数
if [ $# -lt 1 ]; then
    echo "用法: $0 <用户列表CSV>"
    echo "CSV格式: name,wecom_app_id"
    echo ""
    echo "示例:"
    echo "name,wecom_app_id"
    echo "dongdong,zhangsan001"
    echo "zhangsan,lisi002"
    echo "lisi,wangwu003"
    exit 1
fi

USER_CSV="$1"

if [ ! -f "$USER_CSV" ]; then
    echo "错误: 找不到文件 $USER_CSV"
    exit 1
fi

# 创建共享知识库目录（如果不存在）
mkdir -p "$SHARED_DIR"/{knowledge-base/{facts,patterns,decisions,feedback},templates}

# 读取CSV并创建profile
echo "开始创建用户profile..."
echo ""

while IFS=',' read -r name wecom_app_id; do
    # 跳过表头
    if [ "$name" = "name" ]; then
        continue
    fi
    
    # 去除空格和换行
    name=$(echo "$name" | tr -d '[:space:]')
    wecom_app_id=$(echo "$wecom_app_id" | tr -d '[:space:]')
    
    if [ -z "$name" ]; then
        continue
    fi
    
    echo "创建 profile: $name (WeCom App ID: $wecom_app_id)"
    
    # 创建profile目录结构
    PROFILE_DIR="$PROFILES_DIR/$name"
    mkdir -p "$PROFILE_DIR"/{private,workspace}
    
    # 创建symlink到共享知识库
    if [ ! -L "$PROFILE_DIR/shared-skills" ]; then
        ln -s "$SHARED_DIR" "$PROFILE_DIR/shared-skills"
        echo "  ✓ 创建 symlink: shared-skills -> $SHARED_DIR"
    else
        echo "  ✓ symlink已存在"
    fi
    
    # 创建用户偏好文件
    if [ ! -f "$PROFILE_DIR/private/preferences.md" ]; then
        cat > "$PROFILE_DIR/private/preferences.md" << EOF
---
user: $name
wecom_app_id: $wecom_app_id
created: $(date +%Y-%m-%d)
---

# $name 的个人偏好

## 信息偏好
<!-- 记录用户的信息偏好，如喜欢的格式、关注的领域等 -->

## 常用指令
<!-- 记录用户的常用指令模式 -->

## 个性化设置
<!-- 其他个性化配置 -->
EOF
        echo "  ✓ 创建 preferences.md"
    fi
    
    # 创建工作记忆文件
    if [ ! -f "$PROFILE_DIR/workspace/current-task.md" ]; then
        cat > "$PROFILE_DIR/workspace/current-task.md" << EOF
---
user: $name
status: idle
updated: $(date +%Y-%m-%d)
---

# 当前任务

## 状态
空闲

## 进行中的任务
<!-- 无 -->

## 待处理
<!-- 无 -->
EOF
        echo "  ✓ 创建 current-task.md"
    fi
    
    echo ""
done < "$USER_CSV"

echo "=========================================="
echo "初始化完成！"
echo "=========================================="
echo ""
echo "目录结构："
echo "$BASE_DIR/"
echo "├── shared-skills/          # 全局知识库（共享）"
echo "│   ├── knowledge-base/     # 四类知识"
echo "│   ├── methodologies/      # 方法论Skill"
echo "│   └── templates/          # 知识模板"
echo "└── profiles/               # 用户profiles"
for name in $(tail -n +2 "$USER_CSV" | cut -d',' -f1 | tr -d '[:space:]'); do
    if [ -n "$name" ]; then
        echo "    └── $name/"
        echo "        ├── shared-skills -> ../shared-skills (symlink)"
        echo "        ├── private/       # 私有知识"
        echo "        └── workspace/     # 工作记忆"
    fi
done
echo ""
echo "下一步："
echo "1. 在企业微信后台为每个用户创建应用"
echo "2. 将 WeCom App ID 填入 preferences.md"
echo "3. 配置 long-palace 路由映射"
