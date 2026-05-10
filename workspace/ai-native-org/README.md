# AI原生组织知识库

> MVP版本 · 2026-05-09
> 面向3-4人项目组，企业微信部署

---

## 快速开始

### 1. 配置项目组成员

编辑 `project-team.csv`：

```csv
name,wecom_app_id
dongdong,
zhangsan,ww1234567890abcdef
lisi,ww2345678901abcdef
wangwu,ww3456789012abcdef
```

### 2. 执行初始化

```bash
./init-profiles.sh project-team.csv
```

这会为每个用户创建：
- `profiles/{name}/` 目录
- `private/` 私有知识
- `workspace/` 工作记忆
- `shared-skills` symlink（指向全局知识库）

### 3. 在企业微信配置

每个用户的 WeCom App ID 需要在企业微信后台创建应用后获取。

---

## 目录结构

```
ai-native-org/
├── README.md                          # 本文件
├── METADATA-SCHEMA.md                 # 元数据规范
├── init-profiles.sh                   # 初始化脚本
├── project-team.csv                   # 项目组成员列表
│
├── shared-skills/                     # 全局知识库（所有profile共享）
│   ├── knowledge-base/                # 四类知识
│   │   ├── facts/                     # 事实知识
│   │   │   ├── scientific-management-core.md
│   │   │   └── opc-definition.md
│   │   ├── patterns/                  # 模式知识
│   │   │   ├── opc-12-questions.md
│   │   │   └── redpoint-matching-logic.md
│   │   ├── decisions/                 # 决策知识（待填充）
│   │   └── feedback/                  # 反馈知识（待填充）
│   │
│   ├── methodologies/                 # 方法论Skill
│   │   ├── scientific-management/
│   │   │   └── SKILL.md              # 泰勒+德鲁克+麦格雷戈
│   │   ├── opc-framework/
│   │   │   └── SKILL.md              # OPC创业方法论
│   │   └── redpoint/
│   │       └── SKILL.md              # Redpoint业务知识
│   │
│   └── templates/                     # 知识模板
│       ├── fact-template.md
│       ├── pattern-template.md
│       ├── decision-template.md
│       ├── feedback-template.md
│       └── skill-template/
│           └── SKILL.md
│
└── profiles/                          # 用户profiles（初始化后生成）
    ├── dongdong/
    │   ├── shared-skills -> ../shared-skills
    │   ├── private/
    │   │   └── preferences.md
    │   └── workspace/
    │       └── current-task.md
    ├── zhangsan/
    │   └── ...
    └── ...
```

---

## 知识库内容

### 已有内容

| 类型 | 内容 | 状态 |
|------|------|------|
| Skill | 科学管理理论体系 | ✅ 完整 |
| Skill | OPC创业方法论 | ✅ 完整 |
| Skill | Redpoint业务知识 | ✅ 完整 |
| Fact | 科学管理核心遗产 | ✅ 完成 |
| Fact | OPC定义 | ✅ 完成 |
| Pattern | OPC 12问框架 | ✅ 完成 |
| Pattern | Redpoint匹配逻辑 | ✅ 完成 |
| Decision | — | ⏳ 待填充 |
| Feedback | — | ⏳ 待填充 |

### 元数据规范

所有知识文件必须包含YAML front-matter，详见 `METADATA-SCHEMA.md`。

---

## 与 long-palace 对接

### long-palace 需实现的接口

| 接口 | 用途 | 参数 |
|------|------|------|
| `create_profile` | 创建用户profile | name, wecom_app_id |
| `sync_knowledge` | 同步知识库 | skill_name, content |
| `list_profiles` | 列出所有profile | — |
| `get_knowledge` | AI调用知识检索 | category, filters |
| `archive_knowledge` | 归档过期知识 | id, reason |

### WeCom机器人路由

```
企业微信消息 → long-palace路由 → profile/{user}/
                                      ↓
                              读取 shared-skills（全局）
                              读取 private/（个人）
                              读取 workspace/（当前任务）
```

---

## 日常使用

### 创建新知识

1. 选择对应模板（fact/pattern/decision/feedback）
2. 复制到 `shared-skills/knowledge-base/{type}/`
3. 填写元数据和内容
4. 使用时通过 `@import` 或 AI检索调用

### 每日维护

| 时间 | 操作 |
|------|------|
| 对话中 | 发现有价值信息 → 创建fact/pattern |
| 每周五 | 检查过期知识，补充feedback |
| 每月1日 | 审查低使用率知识，执行系统放弃 |

---

## 参考文档

- [飞书MVP方案](https://www.feishu.cn/docx/Y880d3Hwio5h1nxZXFxcYcnpnLe)
- [泰勒1912年证词解读](见今日对话)
- [OpenAI内部智能体架构](https://openai.com/index/inside-our-in-house-data-agent/)
- [Anthropic Claude Code Memory](https://docs.anthropic.com/docs/claude-code/memory)
