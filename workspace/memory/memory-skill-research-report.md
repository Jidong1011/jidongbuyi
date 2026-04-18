# 记忆系统 Skill 深度研究报告

> 生成时间：2026-04-14
> 研究周期：3天（2026-04-14 ~ 2026-04-17）

---

## 一、三个 Skill 逐一深度分析

### 1.1 memory-pipeline

#### 核心架构

memory-pipeline 是一个**认知架构型**记忆系统，灵感来源于人类记忆工作方式。它包含三个串行阶段和一套可选的性能钩子。

**三阶段流水线：**

| 阶段 | 脚本 | 输入 | 输出 | 功能 |
|------|------|------|------|------|
| Extract | `scripts/memory-extract.py` | `memory/YYYY-MM-DD.md` + 会话 transcript | `memory/extracted.jsonl` | 用 LLM 从原始笔记中提取结构化事实 |
| Link | `scripts/memory-link.py` | `memory/extracted.jsonl` | `memory/knowledge-graph.json` + `memory/knowledge-summary.md` | 构建知识图谱，生成 embedding，建立双向链接，检测矛盾 |
| Briefing | `scripts/memory-briefing.py` | SOUL.md + USER.md + 知识图谱 + todos | `BRIEFING.md`（< 2000 chars） | 生成每日简报 |

**数据结构：**

`extracted.jsonl` 每行为一个 JSON 对象：
```json
{"type": "decision", "content": "Use Rust for the backend", "subject": "Project Architecture", "confidence": 0.9, "date": "2025-01-15", "source": "daily-note"}
```
支持的 type：`decision`、`preference`、`learning`、`commitment`

`knowledge-graph.json` 结构：
```json
{
  "nodes": [
    {
      "id": 0, "type": "decision", "content": "...", "subject": "...",
      "date": "2025-01-15", "confidence": 0.9,
      "keywords": ["keyword1", "keyword2"], "tags": ["decision", "project-name"],
      "embedding": [0.123, -0.456, ...], "links": [1, 5, 12]
    }
  ],
  "links": [{"source": 0, "target": 1, "strength": 0.85, "type": "related"}],
  "metadata": {"created": "...", "total_facts": 42, "has_embeddings": true}
}
```

**四阶段性能钩子（Performance Hooks）：**
```
before_agent_start  → 注入简报 + 记忆文件
before_tool_call    → 工具黑名单检查
tool_result_persist → 60% head + 30% tail 压缩
agent_end           → After-action review 写入记忆
```

**外部知识摄入：** `scripts/ingest-chatgpt.py` 支持 ChatGPT 导出包的解析和导入，输出到 `memory/knowledge/chatgpt/*.md`。

**LLM 依赖：** 需要至少一个 LLM API Key（OpenAI / Anthropic / Gemini），embedding 需要 OpenAI Key。

#### 优势

1. **认知架构设计成熟** — 不只是"存日志"，而是 Extract → Link → Brief 的完整认知流水线，有清晰的信息提炼和压缩机制
2. **知识图谱有实际链接** — 双向关系、矛盾检测、自动标签，不是花架子
3. **简报机制实用** — 每次会话启动时自动加载 < 2000 chars 的上下文包，解决冷启动问题
4. **外部知识可导入** — ChatGPT 历史对话可以迁移过来，降低切换成本
5. **压缩前刷新** — 上下文压缩前先提醒 agent 保存重要信息，防止信息丢失

#### 不足

1. **Python 脚本依赖** — 需要 Python 3 + LLM API Key，不是纯 bash 方案，部署门槛比 memory-system-v2 高
2. **LLM 成本** — 每次 extract/link/briefing 都需要调用 LLM，长期运行有持续 API 成本
3. **没有语义搜索** — 知识图谱本身有 embedding，但没有提供独立的搜索接口给 agent 在会话中查询
4. **设计文档中 workspace 路径用 `~/.clawdbot/`** — 与当前 OpenClaw 的 `/workspace/projects/workspace/` 不一致，需要适配
5. **脚本没有经过实际测试验证** — 没有 test 结果，工程质量不如 memory-system-v2（36/36 通过）

#### 适用场景

- 需要从大量历史对话中提炼结构化知识的场景
- 每日会话量多、需要知识图谱关联发现的场景
- 需要迁移外部知识源（如 ChatGPT 导出）的场景
- 对冷启动质量要求高、希望每次会话有完整上下文简报的场景

#### 与当前系统的兼容性

- ✅ 输出格式（Markdown daily notes）与现有 `memory/YYYY-MM-DD.md` 兼容
- ✅ `BRIEFING.md` 可以被 OpenClaw 的 context loading 机制读取
- ⚠️ 脚本中的 workspace 检测逻辑需要修改为 `/workspace/projects/workspace/`
- ⚠️ 需要 Python 3 + LLM API Key（OpenAI 推荐）
- ❌ 没有与 OpenClaw 的 memory_search 工具集成，搜索能力独立于主系统

---

### 1.2 memory-system-v2

#### 核心架构

memory-system-v2 是一个**纯 bash + jq** 的轻量级记忆系统，追求速度和简单性。

**文件结构：**
```
memory/
├── memory-cli.sh              # 主 CLI 工具（纯 bash + jq）
├── index/
│   └── memory-index.json      # JSON 索引
├── daily/
│   └── YYYY-MM-DD.md          # 每日记忆日志
└── consolidated/
    └── YYYY-WW.md             # 周报摘要
```

**核心操作（5 个命令）：**

| 命令 | 功能 | 性能 |
|------|------|------|
| `capture --type --importance --content --tags --context` | 捕获记忆 | <50ms |
| `search "keywords" [--min-importance N]` | 多词搜索 + 重要性加权 | <20ms |
| `recent <type\|all> <days> <min-importance>` | 按时间/类型/重要性检索 | <15ms |
| `stats` | 记忆统计（按类型/重要性分布） | <10ms |
| `consolidate [--week YYYY-WW]` | 自动周报整合 | <500ms |

**JSON 索引结构（`memory-index.json`）：**
```json
{
  "version": 1,
  "lastUpdate": 1738368000000,
  "memories": [
    {
      "id": "mem_20260131_12345",
      "type": "learning",           // learning|decision|insight|event|interaction
      "importance": 9,              // 1-10 重要性评分
      "timestamp": 1738368000000,
      "date": "2026-01-31",
      "content": "Memory content here",
      "tags": ["tag1", "tag2"],
      "context": "What I was doing",
      "file": "memory/daily/2026-01-31.md",
      "line": 42
    }
  ]
}
```

**设计文档中的扩展架构（docs/memory-system-v2-design.md）还有更完整的 schema v2.0：**
- 额外的 `entities` 字段（people, projects, skills）
- `outcome` 和 `relatedTo` 字段
- `tags.json`、`people.json`、`projects.json`、`decisions.json` 独立索引
- 月度整合（`consolidated/YYYY-MM.md`）
- 归档机制（`archive/`）

**注意：** 设计文档中的 v2.0 schema 比实际 SKILL.md 中描述的 v1 schema 更完整，说明设计愿景超越了当前实现。

**5 种记忆类型：**

| 类型 | 重要性范围 | 用途 |
|------|-----------|------|
| learning | 7-9 | 新技能、工具、模式 |
| decision | 6-9 | 选择、策略、方案 |
| insight | 8-10 | 突破、顿悟、aha moment |
| event | 5-8 | 里程碑、完成、发布 |
| interaction | 5-7 | 关键对话、反馈、请求 |

#### 优势

1. **零外部依赖** — 纯 bash + jq，不需要 Python、不需要 LLM API Key、不需要数据库
2. **经过完整测试** — 36/36 测试通过，搜索 < 20ms、捕获 < 50ms，数据完整性 100%
3. **CLI 设计优秀** — 5 个命令覆盖所有操作，接口简单清晰
4. **重要性评分** — 1-10 评分系统比简单分类更精细，支持 `--min-importance` 过滤
5. **自动整合** — `consolidate` 命令自动生成周报，减少人工整理

#### 不足

1. **纯文本搜索** — 没有语义 embedding，搜索依赖关键词匹配，无法处理同义词/近义词
2. **单用户设计** — 文件锁没有处理，不适合多 agent 并发写入
3. **扩展性有限** — 官方称 ~10K 记忆后会变慢（纯 JSON 文件遍历）
4. **设计-实现差距** — `docs/memory-system-v2-design.md` 的 v2.0 schema 包含 entities、outcome、relatedTo 等字段，但 `SKILL.md` 描述的实际实现还是 v1，许多设计没有落地
5. **没有学习循环** — 只能"存"和"取"，没有自动从对话中提取记忆的机制，需要 agent 手动调用 `capture`

#### 适用场景

- 需要快速部署、零依赖的记忆系统
- 记忆量在数千条以内的个人 agent
- 需要确定性执行（无 LLM 调用波动）的场景
- 作为基础记忆层，与其他更高级的记忆系统组合使用

#### 与当前系统的兼容性

- ✅ 纯 bash + jq，当前环境完全支持
- ✅ daily notes 格式与现有 `memory/YYYY-MM-DD.md` 兼容
- ✅ CLI 可以被 agent 在会话中直接调用（通过 exec 工具）
- ⚠️ 索引文件 `memory/index/memory-index.json` 与现有目录结构不同，需要整合
- ❌ 没有与 OpenClaw 的 memory_search 集成，是独立的搜索路径

---

### 1.3 self-improving

#### 核心架构

self-improving 是一个**自我反思与纠错学习**系统，专注于从错误中学习并持续改进执行质量。它与前两个记忆系统的根本区别是：它不是"记住发生了什么"，而是"记住怎么做得更好"。

**三层存储（Tiered Storage）：**

| 层级 | 位置 | 大小限制 | 加载策略 | 行为 |
|------|------|---------|---------|------|
| HOT | `~/self-improving/memory.md` | ≤100 行 | 每次会话自动加载 | 最常用模式 |
| WARM | `~/self-improving/projects/*.md` + `domains/*.md` | ≤200 行/文件 | 按上下文匹配加载 | 项目/领域级模式 |
| COLD | `~/self-improving/archive/` | 无限 | 仅在明确查询时加载 | 已归档模式 |

**核心文件清单（14 个 .md 文件）：**

| 文件 | 用途 |
|------|------|
| `SKILL.md` | 主入口，触发条件 + 核心规则 + 常见陷阱 |
| `learning.md` | 学习信号分类 + 确认流程 + 模式进化阶段 |
| `memory.md` | HOT 记忆模板 |
| `memory-template.md` | 初始化模板 |
| `corrections.md` | 纠正日志模板（最后 50 条） |
| `operations.md` | 用户命令 + 自动操作流程 + 文件格式规范 |
| `scaling.md` | 扩展规则 + compaction 策略 + 多项目继承 |
| `boundaries.md` | 安全边界 + 隐私红线 + Kill Switch |
| `reflections.md` | 自我反思日志格式 |
| `setup.md` | 安装设置流程（7 步） |
| `heartbeat-rules.md` | Heartbeat 维护规则 |
| `heartbeat-state.md` | Heartbeat 状态模板 |
| `HEARTBEAT.md` | OpenClaw heartbeat 片段 |
| `openclaw-heartbeat.md` | OpenClaw 专用 heartbeat 配置 |

**学习信号触发机制（`learning.md`）：**

高置信度信号（立即记录）：
- "No, that's not right..." / "Actually, it should be..."
- "I told you before..."
- "Always/Never do X"

中置信度信号（观察性记录）：
- 用户编辑 agent 输出（tentative pattern）

确认流程（3 次规则）：
```
1x correction → Tentative（观察）
2x correction → Emerging（可能模式）
3x correction → Pending（请求确认）
User confirms → Confirmed（永久，除非逆转）
```

**模式进化阶段（5 个）：**
```
Tentative → Emerging → Pending → Confirmed → Archived
  (1x)        (2x)       (3x)     (用户确认)   (90天未用)
```

**命名空间隔离与继承：**
```
global (memory.md)
  └── domain (domains/code.md, domains/writing.md)
       └── project (projects/app.md)
```
冲突解决规则：最具体优先 > 最新优先 > 不明确时问用户

**自动晋升/降级机制：**
- 7 天内使用 3x → 晋升到 HOT
- 30 天未使用 → 降级到 WARM
- 90 天未使用 → 归档到 COLD
- 永远不删除（除非用户明确要求）

**安全边界（`boundaries.md`）：**
- 永不存储：凭据、财务、医疗、生物特征、第三方信息
- Kill Switch："forget everything" → 导出当前记忆 → 全部清除 → 确认

**Heartbeat 维护（`heartbeat-rules.md`）：**
- 每次心跳只做保守整理（刷新 index、compact 超大文件、移动错位笔记）
- 大部分心跳应该什么都不做
- 永远不删除数据、不重写不确定的内容

#### 优势

1. **学习机制最完善** — 有明确的信号分类、确认流程、模式进化阶段，不是简单的"记下来"
2. **三层存储设计精妙** — HOT/WARM/COLD 分层 + 按需加载，context 效率高
3. **安全边界清晰** — 明确的"永不存储"列表 + Kill Switch + 审计追踪
4. **命名空间隔离** — global/domain/project 三层继承，不同上下文不串扰
5. **零外部依赖** — 不需要 Python、不需要 LLM API、不需要 jq，纯 Markdown 文件操作
6. **文档极其完整** — 14 个 .md 文件覆盖了安装、使用、安全、扩展、心跳维护的所有方面
7. **与 OpenClaw 深度集成** — 有专门的 `openclaw-heartbeat.md` 和 `HEARTBEAT.md`

#### 不足

1. **没有搜索能力** — 没有任何搜索接口，只能按文件层级浏览，跨文件查找靠 agent 自己读文件
2. **没有知识图谱** — 记忆之间没有显式关联，不知道"A 偏好"和"B 决策"之间的关系
3. **没有外部知识导入** — 不支持 ChatGPT 导出等外部数据源的迁移
4. **路径在 `~/self-improving/`** — 与 workspace 内的 `memory/` 目录分离，两套记忆系统并行维护
5. **compaction 完全靠 agent 自觉** — 没有自动化的 compaction 脚本，只在 heartbeat 中提示整理
6. **没有量化评估** — 没有像 memory-system-v2 那样的性能测试，效果依赖主观感受

#### 适用场景

- 需要从错误中学习、持续改进执行质量的场景
- 重视安全边界和隐私保护的场景
- 多项目并行、需要命名空间隔离的场景
- 作为"执行质量改进层"，与其他记忆系统互补使用

#### 与当前系统的兼容性

- ✅ 零外部依赖，完全兼容当前环境
- ✅ 有 OpenClaw 专用的 heartbeat 集成
- ✅ 可以与现有 AGENTS.md / SOUL.md 无缝融合（setup.md 有详细步骤）
- ⚠️ 存储路径在 `~/self-improving/`，与 workspace 内的 `memory/` 是两套独立系统
- ⚠️ setup.md 要求修改 AGENTS.md 和 SOUL.md，需要谨慎操作避免覆盖现有配置

---

## 二、Hermes Agent 记忆架构研究

> 信息来源：Nous Research 官方仓库、掘金/头条/极客公园等中文技术分析文章

### 2.1 记忆分层设计

Hermes Agent 采用**四层记忆架构**，每层有特定职责、特定磁盘位置、特定读取时机：

| 层级 | 存储 | 读取方式 | 内容类型 | 大小限制 |
|------|------|---------|---------|---------|
| **提示记忆** | `~/.hermes/memories/MEMORY.md` + `USER.md` | 每次会话自动注入 system prompt | 长期偏好、决策、重要事实 | **3,575 字符**（强制） |
| **会话搜索** | SQLite + FTS5 索引 | Agent 主动搜索时按需加载 | 历史对话全文 | 无限制 |
| **技能记忆** | `~/.hermes/skills/*.md` | 渐进式披露：默认只加载名称+摘要 | 程序性记忆（怎么做） | 无限制（按需加载） |
| **Honcho 建模** | 外部 Honcho 服务 | 后台被动构建，注入 system prompt | 用户画像（12 个身份层） | 可选层 |

**关键设计决策：**

1. **提示记忆的字符限制（3,575 chars）** — 这是 Hermes 最独特的设计。不是"能写多少写多少"，而是强制精选，确保每次加载的都是最高价值的信息。

2. **情景记忆与程序性记忆分离** — 会话搜索回答"发生了什么"（情景记忆），技能记忆回答"怎么做某事"（程序性记忆）。两者刻意分开存储。

3. **渐进式披露（Progressive Disclosure）** — 技能默认只加载名称和摘要，完整内容在 Agent 判断与当前任务相关时才加载。200 个技能和 40 个技能的 token 成本几乎相同。

4. **8 个外部记忆 Provider（互斥选一）：**

| Provider | 核心能力 | 特点 |
|----------|---------|------|
| **Honcho** | 辩证式用户建模 + 跨会话观察 | 最复杂，12 个身份层 |
| **OpenViking** | 分层加载 L0/L1/L2 | 字节跳动出品，按需取 token |
| **Mem0** | 全自动提取+去重+语义搜索 | 最省心，但数据在云端 |
| **Hindsight** | 知识图谱 + 跨记忆反思 | 唯一支持综合反思的 |
| **Holographic** | SQLite + FTS5 + 信任评分 + HRR | 最简约，矛盾检测 |
| **RetainDB** | 7 种记忆类型 + 混合搜索 | 唯一收费（$20/月） |
| **ByteRover** | CLI-first + 层级知识树 | 压缩前自动提取 |
| **Supermemory** | 语义图谱 + 防递归污染 | 会话级摄取 + 上下文隔离 |

**生命周期钩子（6 个关键节点）：**
```
initialize → prefetch → sync_turn → on_session_end → on_pre_compress → on_memory_write → shutdown
```

### 2.2 自进化机制

Hermes 的核心竞争力不是记忆，而是**学习循环（Learning Loop）** —— 一个在每个会话下运行的闭环反馈系统。

#### 2.2.1 KEPA 提示反向传播

**KEPA（Knowledge-Enhanced Prompt Adjustment，知识增强提示调整）** 是 Hermes 最独特的设计，被业界戏称为"提示反向传播"。

工作原理（类比神经网络反向传播）：
```
传统深度学习：
  前向：输入 → 模型 → 输出
  反向：根据损失函数，更新模型权重

Hermes 的 KEPA：
  前向：用户意图 → Agent（LLM + 工具）→ 执行序列
  反向：周期性回顾近期执行 → 检测失败点 → 分析失败原因 → 更新提示模板/技能
```

具体步骤：
1. 任务执行失败或用户否定输出时，标记该次提示-响应对为负样本
2. 提取关键变量：指令粒度、上下文长度、工具调用顺序
3. 用 GRPO 算法评估各变量对失败的影响权重
4. 在下次同类任务中，自动增强高权重变量的约束强度
5. 优化后的提示模板持久化到 `config/prompt_templates/` 供复用

**关键差异：** 不修改模型权重，而是动态调整"如何使用模型"的策略。

#### 2.2.2 自动技能创建与改进

**触发条件（任一满足即触发）：**
- 5 次或更多工具调用
- 从错误中恢复
- 用户纠正
- 奏效的非明显工作流

**技能存储格式（遵循 agentskills.io 开放标准）：**
```yaml
---
name: my-skill
description: Brief description
version: 1.0.0
platforms: [macos, linux]
metadata:
  hermes:
    tags: [python, automation]
    category: devops
---
```

**技能操作（6 种）：** `create`、`patch`、`edit`、`delete`、`write_file`、`remove_file`
- 默认使用 `patch`（只传入旧字符串和替换字符串），避免完整重写破坏已有内容
- patch 既是正确性也是效率的决策

**双环学习循环：**

```
内环（单次任务）：
  执行 → 观察 → 微调技能（patch）→ 继续执行

外环（跨会话）：
  会话结束 → 反思 → 创建新技能 / 更新现有技能 → 下次会话复用
```

#### 2.2.3 Honcho 辩证式用户建模

Honcho 使用**辩证建模方法（Dialectical Modeling）**，在 12 个身份层中同时建模用户和 Agent 之间的关系。

辩证进化的结构：
```
正题（Thesis）→ 当前对用户的理解
  ↓
反题（Antithesis）→ 新的观察与当前理解矛盾
  ↓
合题（Synthesis）→ 更新后的用户画像
```

这意味着用户画像不是"最后一次覆盖前一次"，而是新信息与旧信息进行辩证整合，保留有价值的历史理解。

**`dialecticReasoningLevel`** 配置项控制辩证推理的深度。

### 2.3 与 OpenClaw 的对比

| 维度 | Hermes Agent | OpenClaw | 评价 |
|------|-------------|----------|------|
| **架构哲学** | 策展式（精选写入，有字符限制） | 索引式（随意写入，搜索时精准） | 无绝对优劣，场景不同 |
| **记忆搜索** | 内置无搜索；靠外部 Provider | 内置 BM25 + 向量 + 混合 + 中文分词 + 时间衰减 + MMR | OpenClaw 大幅领先 |
| **记忆巩固** | 压缩前刷新 + 会话结束提取 | Dreaming 三阶段系统（Light/Deep/REM + 6 信号加权） | OpenClaw 的 Dreaming 更系统化 |
| **自进化** | KEPA 提示反向传播 + 自动技能创建 + 技能 patch | 无内置等价机制，依赖 skill 系统 | Hermes 大幅领先 |
| **技能系统** | 自动创建 + 自我改进 + 渐进式披露 | 手动安装 + 手动更新 | Hermes 的自动化程度更高 |
| **上下文压缩** | 50% 预压缩 / 85% 强制压缩 / 保留最后 20 条 | 压缩前 memory flush 回合 + Evergreen 不降权 | 基本相当 |
| **外部 Provider** | 8 个互斥选一 | 3 个可切换 + Honcho 插件 | OpenClaw 更灵活（不互斥） |
| **多 Agent** | Honcho profile 独立观察 + 共享 workspace | Honcho 插件 + subagent | 基本相当 |
| **部署** | 6 种后端（Local/Docker/SSH/Daytona/Modal/Singularity） | 1 种后端（Gateway daemon） | Hermes 更灵活 |
| **平台覆盖** | 15+ 平台（含飞书/企业微信） | 通过 channel 插件 | 基本相当 |
| **安全** | 只读根文件系统 + 零遥测 | Plugin Poisoning Defense + Anti-Leak | 各有侧重 |

**核心洞察：** Hermes 在**自进化**（KEPA + 自动技能 + 辩证建模）上远超 OpenClaw，但 OpenClaw 在**记忆搜索**（内置混合检索 + Dreaming）上远超 Hermes。两者最理想的状态是互相借鉴对方的强项。

---

## 三、综合评估与推荐

### 3.1 三个 Skill 的互补性分析

| 维度 | memory-pipeline | memory-system-v2 | self-improving |
|------|----------------|-----------------|----------------|
| **核心定位** | 知识提炼 + 关联发现 | 快速存取 + 分类管理 | 错误学习 + 质量改进 |
| **记忆类型** | 事实性（决策/偏好/学习） | 多类型（5 种 + 重要性评分） | 规则性（纠正/偏好/模式） |
| **存储格式** | JSONL + JSON 图 + Markdown | JSON 索引 + Markdown | 纯 Markdown |
| **搜索能力** | 知识图谱遍历（需要代码） | 关键词搜索（< 20ms） | 无搜索 |
| **外部依赖** | Python + LLM API | bash + jq | 无 |
| **自动提取** | ✅ LLM 驱动 | ❌ 需手动 capture | ❌ 靠 agent 触发 |
| **知识图谱** | ✅ 完整图结构 | ❌ | ❌ |
| **学习循环** | ❌ | ❌ | ✅ 5 阶段进化 |
| **安全边界** | 未提及 | 未提及 | ✅ 详细安全规范 |
| **Heartbeat** | 可通过 HEARTBEAT.md 配置 | 无 | ✅ 专用 heartbeat 规则 |
| **测试状态** | 未测试 | 36/36 通过 | 未测试 |

**互补矩阵：**

```
                    memory-pipeline    memory-system-v2    self-improving
知识提炼                ★★★★★              ★★☆☆☆              ★★☆☆☆
快速检索                ★★☆☆☆              ★★★★★              ★☆☆☆☆
错误学习                ★☆☆☆☆              ★★☆☆☆              ★★★★★
知识图谱                ★★★★★              ★☆☆☆☆              ★☆☆☆☆
部署简易                ★★☆☆☆              ★★★★★              ★★★★★
安全隐私                ★★☆☆☆              ★★☆☆☆              ★★★★★
自动提取                ★★★★☆              ★☆☆☆☆              ★★☆☆☆
长期维护                ★★★☆☆              ★★★☆☆              ★★★★☆
```

**关键互补关系：**
- `memory-system-v2` 提供快速存取的**基础记忆层**
- `memory-pipeline` 提供知识提炼和关联发现的**知识层**
- `self-improving` 提供错误学习和质量改进的**元学习层**

### 3.2 最佳组合方案

**推荐组合：memory-system-v2（基础层）+ self-improving（元学习层）**

理由：
1. **memory-system-v2 作为日常记忆工具** — 它已经过完整测试（36/36），零外部依赖，< 20ms 搜索，满足 90% 的日常记忆需求（记住决策、学习、偏好、事件、交互）
2. **self-improving 作为执行质量改进工具** — 它的学习循环、三层存储、安全边界在另外两个 skill 中没有等价物
3. **暂不部署 memory-pipeline** — 原因：Python + LLM API 依赖增加复杂度，知识图谱功能在记忆量还小的时候价值不大，且没有测试验证

**合并建议：**
- 将 `memory-system-v2` 的 CLI 和索引整合到 workspace 的 `memory/` 目录
- 将 `self-improving` 的 HOT 记忆内容（经确认的偏好和模式）同步到 `MEMORY.md`
- 用 OpenClaw 内置的 `memory_search` 替代 memory-system-v2 的搜索（当 embedding provider 可用时）

### 3.3 与 Hermes 理念的融合建议

Hermes 的三个核心创新理念值得借鉴，但不需要迁移到 Hermes 框架：

#### 3.3.1 KEPA 提示反向传播 → 可用 self-improving 模拟

Hermes 的 KEPA 本质上是"从失败中学习并更新行为策略"。self-improving 已经有类似机制：

| KEPA 步骤 | self-improving 等价操作 |
|-----------|----------------------|
| 检测失败点 | corrections.md 记录用户纠正 |
| 提取关键变量 | corrections.md 的 Type + Context 字段 |
| 评估影响权重 | 3x 确认流程（Tentative → Confirmed） |
| 更新提示模板 | 晋升到 HOT memory.md |
| 持久化到配置 | memory.md + SOUL.md 中的行为规则 |

**增强建议：** 在 `corrections.md` 中增加"失败上下文"字段（工具调用序列、模型参数），使其更接近 KEPA 的分析粒度。

#### 3.3.2 自动技能创建 → 与 OpenClaw skill 系统对接

Hermes 的自动技能创建（5+ 工具调用/错误恢复/用户纠正 → 生成 .md 技能文件）可以直接映射到 OpenClaw 的 skill 系统：

```
Hermes 触发条件 → Agent 判断 → 写入 workspace/skills/xxx/SKILL.md → 下次会话可用
```

**增强建议：** 在 `reflections.md` 的格式中增加"技能候选"字段。当反思结果包含 3+ 步可复用流程时，标记为技能候选，经用户确认后写入 skill 文件。

#### 3.3.3 辩证式用户建模 → 增强用户画像更新机制

Hermes 的"正题→反题→合题"用户画像更新可以用以下方式在 OpenClaw 中实现：

1. 在 `USER.md` 中增加 `## 决策风格`、`## 沟通偏好`、`## 领域知识` 等结构化章节
2. 更新时采用"保留历史 + 标记变更"而非直接覆盖：
   ```markdown
   ## 沟通偏好
   - 直接简洁（2026-01 确认）
   - 喜欢代码示例（2026-03 新增，与"偏好文字解释"矛盾 → 经确认后者已过时）
   ```
3. 在 `~/self-improving/corrections.md` 中追踪偏好变更历史

#### 3.3.4 渐进式披露 → 优化记忆加载策略

Hermes 的渐进式披露（只加载名称和摘要，完整内容按需加载）可以应用到 OpenClaw 的记忆加载：

- 会话开始时只加载 `BRIEFING.md`（< 2000 chars）
- 按需读取 `memory/` 下具体文件
- 使用 memory_search 按语义相关性检索，而非全量加载

### 3.4 落地实施路线图

#### 第一阶段（1-2 天）：基础记忆层

**目标：** 建立日常记忆的快速存取能力

1. 部署 `memory-system-v2` CLI 到 workspace
   ```bash
   # 将 memory-cli.sh 复制到 memory/ 目录
   # 初始化 index/、daily/、consolidated/ 目录结构
   ```
2. 整合到现有 `memory/` 目录（不破坏已有文件）
3. 在 AGENTS.md 中添加记忆规则：
   - 每次做出重要决策 → `memory-cli.sh capture --type decision`
   - 每次学到新东西 → `memory-cli.sh capture --type learning`
   - 每次需要回忆 → `memory-cli.sh search`
4. 在 HEARTBEAT.md 中添加每日 consolidate 任务

#### 第二阶段（2-3 天）：元学习层

**目标：** 建立错误学习和执行质量改进能力

1. 运行 `self-improving` 的 setup 流程（7 步）
   ```bash
   mkdir -p ~/self-improving/{projects,domains,archive}
   ```
2. 按需修改 AGENTS.md 和 SOUL.md（非破坏性，只追加）
3. 在 HEARTBEAT.md 中添加 self-improving 检查
4. 建立 `~/self-improving/memory.md` 与 `workspace/memory/MEMORY.md` 的同步机制：
   - 确认的偏好双向写入
   - AGENTS.md 引导读取路径

#### 第三阶段（3-5 天）：OpenClaw 原生集成

**目标：** 让记忆系统成为 agent 的自然行为

1. 利用 OpenClaw 的 `memory_search` 作为主搜索入口（替代 memory-system-v2 的 CLI 搜索）
2. 建立 `BRIEFING.md` 自动生成机制（简化版 memory-pipeline 的 briefing 阶段）：
   - 不依赖 Python + LLM
   - 用 agent 自身在 heartbeat 中总结生成
3. 增加技能候选识别机制（借鉴 Hermes 的自动技能创建）

#### 第四阶段（持续优化）：Hermes 理念融合

**目标：** 逐步引入 Hermes 的先进理念

1. 在 corrections.md 中增加失败上下文记录（接近 KEPA）
2. 建立 USER.md 的辩证更新机制（正题→反题→合题）
3. 探索 memory-system-v2 的 v2.0 schema（entities、outcome、relatedTo）
4. 考虑是否需要 memory-pipeline 的知识图谱能力（取决于记忆量增长速度）

---

## 四、结论

### 核心发现

1. **三个 Skill 各有所长，互补性极强** — memory-system-v2 解决"怎么快速存取"，self-improving 解决"怎么持续改进"，memory-pipeline 解决"怎么提炼知识"。三者组合可以覆盖记忆系统的所有核心需求。

2. **当前最务实的选择是 memory-system-v2 + self-improving** — 两个都是零外部依赖、经过验证、与 OpenClaw 兼容的方案。memory-pipeline 的知识图谱和 LLM 驱动提取虽然强大，但引入了 Python + LLM API 的复杂度，在记忆量还小的阶段 ROI 不高。

3. **Hermes 的核心理念（KEPA、自动技能、辩证建模）可以在 OpenClaw 中实现，无需迁移框架** — OpenClaw 的 skill 系统、heartbeat 机制、memory_search 能力已经提供了足够的基础设施。关键是在现有基础上增加"学习循环"和"技能沉淀"的行为规则。

4. **OpenClaw 相比 Hermes 的最大差距在"自进化"能力** — OpenClaw 有更好的搜索和记忆巩固（Dreaming），但缺少 KEPA 式的提示优化和自动技能创建。这是通过 self-improving + 规则设计可以弥补的。

### 可执行的下一步

1. **今天** — 部署 memory-system-v2 CLI，跑一遍 36 个测试确认可用
2. **明天** — 运行 self-improving setup，建立两层记忆架构
3. **本周内** — 在 AGENTS.md / HEARTBEAT.md 中集成记忆规则，开始积累
4. **下周** — 评估记忆量增长，决定是否引入 memory-pipeline

### 一句话总结

> 不要追求完美的记忆系统，追求一个能持续进化的记忆系统。从 memory-system-v2 开始，用 self-improving 让它变聪明，用 Hermes 的理念让它变强大。
