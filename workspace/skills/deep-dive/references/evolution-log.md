# Deep-Dive Skill 迭代日志

> 记录每次自循环迭代的学习成果和Skill更新

---

## 2026-06-02 迭代（当前）

### 触发条件
Cron Job: deep-dive-skill-evolution (f6bb3107-a5da-47d4-b825-3de7069e5aa1)

### 搜索关键词
- "feynman technique AI agent workflow"
- "deep research skill OpenClaw Claude"
- "knowledge management AI best practice"
- "research automation framework"
- "费曼技巧 AI 智能体 工作流"
- "深度研究 自动化 最佳实践"

### 关键发现

**1. Feynman AI研究代理 - 证据驱动的研究框架**
- 10大研究工作流：/deepresearch、/lit、/review、/audit、/draft、/autoresearch等
- 四大子代理职责分离：Researcher(搜集)/Writer(写作)/Verifier(验证)/Reviewer(评审)
- **六步流水线**：Plan → Gather → Draft → Cite → Review → Deliver
- **强制确认点**：Plan后暂停等用户确认，防止方向跑偏
- **溯源副件(.provenance.md)**：每个产出附带来源统计和验证状态
- **证据状态标记**：VERIFIED/UNVERIFIED/BLOCKED/INFERRED分级标注
- **核心信条**：Evidence over fluency（证据优先于流畅性）
- **当前Skill状态**: 🔴 重大改进机会 - 上述机制均可借鉴

**2. 费曼学习法的AI实现（feiman-coach）**
- 5位虚拟专家协作：概念拆解大师、简易化转化器、类比创造者、耐心提问者、精准评估器
- 四大评估标准：简洁性、完整性、易懂性、准确性
- 用户主动解释+AI引导发现盲区的互动模式
- **当前Skill状态**: 🟢 持平 - 已有类似机制，但可强化互动模式

**3. 知识管理AI最佳实践**
- 三阶六步知识治理模型：筑基→激活→进化
- 知识资产化→应用场景化→决策智能化的三级进化
- AI知识库全生命周期安全管理
- **当前Skill状态**: 🟡 可借鉴 - 知识资产化概念与Keep阶段整合

**4. 研究自动化框架趋势**
- DeerFlow、Agent Laboratory、EvoMaster等框架的模块化设计
- 从"人力整理"到"智能协同"的PKM演进
- **当前Skill状态**: 🟢 领先 - 六步流水线已对齐行业最佳实践

### 本次更新

**v1.5.0 → v1.6.0**

**采纳的改进（基于Feynman AI代理）**：

1. **六步流水线重构** (v1.6.0)
   - 将五阶段工作流升级为六步流水线：Plan → Gather → Draft → Cite → Review → Deliver
   - 明确各阶段职责边界，减少重叠
   - 更新位置: SKILL.md "六阶段工作流"章节

2. **强制确认点机制** (v1.6.0)
   - Step 1 (Plan) 完成后暂停，展示研究计划等东东确认
   - 展示内容：子目标清单、搜索策略、预期产出、Known Unknowns
   - 可跳过条件：东东明确要求快速研究/紧急任务
   - 好处：防止方向跑偏，让东东参与规划
   - 更新位置: SKILL.md "强制确认点机制"章节

3. **溯源副件(.provenance.md)** (v1.6.0)
   - 为每个Deep-Dive生成独立的溯源文件
   - 包含：来源统计表、证据状态分布、关键声明溯源、局限性声明、置信度评估
   - 自动存档到 `memory/deep-dive/<主题>-provenance.md`
   - 更新位置: SKILL.md "溯源副件(.provenance.md)"章节

4. **证据状态分级标记** (v1.6.0)
   - 引入四级标记：VERIFIED/UNVERIFIED/BLOCKED/INFERRED
   - 每个关键声明必须标注状态
   - 宁标勿藏原则：不确定就标，不假装确定
   - 更新位置: SKILL.md "证据状态分级标记"章节

5. **诚实性戒律强化** (v1.6.0)
   - 新增第6条：溯源副件必生成
   - 强调"不审美清洗"原则
   - 更新位置: SKILL.md "诚实性戒律"章节

**不予采纳的改进**：

| 改进建议 | 不采纳原因 |
|----------|-----------|
| 完全采用Feynman的四子代理模式 | 当前五专家协作模式更适合东东需求，四子代理过于学术化 |
| 引入Docker/实验复现能力 | 东东需求偏向实用知识管理，非学术研究 |
| 增加/watch定期监控功能 | 可用现有cron机制替代，无需重复 |
| 完全自动化无需确认 | 强制确认点是核心设计，确保方向正确 |

### 版本更新

**v1.5.0 → v1.6.0**

新增内容:
- 六步流水线（Plan-Gather-Draft-Cite-Review-Deliver）
- 强制确认点机制
- 溯源副件(.provenance.md)标准格式
- 证据状态四级标记（VERIFIED/UNVERIFIED/BLOCKED/INFERRED）
- 诚实性戒律第6条

优化内容:
- 重构"研究溯源与诚实性标记"章节
- 更新质量检查清单（新增3项检查）
- 明确各阶段职责边界

### 下次迭代方向

1. 验证强制确认点机制在实际Deep-Dive中的使用体验
2. 收集溯源副件的使用反馈，优化格式设计
3. 关注费曼主动交互模式（用户解释+AI引导）的实施效果
4. 监控证据状态标记对研究质量的实际影响

---

*迭代执行: 哆啦dora*
*迭代日期: 2026-06-02*

---

## 2026-05-30 迭代

### 触发条件
Cron Job: deep-dive-skill-evolution (f6bb3107-a5da-47d4-b825-3de7069e5aa1)

### 搜索关键词
- "feynman technique AI agent workflow"
- "deep research skill OpenClaw Claude"
- "knowledge management AI best practice"
- "research automation framework"
- "费曼技巧 AI 智能体 工作流"
- "深度研究 自动化 最佳实践"

### 关键发现

**1. 多智能体协作架构已成行业标准**
- 研知(YanZhi)、AgenticResearchWiki、SciEx均采用Researcher/Writer/Verifier/Reviewer四角色分离
- **当前Skill状态**: 🟢 领先 - v1.4.0已实现四智能体分离模式

**2. 反思与自我改进机制**
- WebResearcher采用"迭代深度研究范式"，将研究视为马尔可夫决策过程
- Prismer.AI的"费曼技巧评估"使用64个主题模板引导用户解释概念
- **当前Skill状态**: 🟢 持平 - 已有对抗验证四问和自我反思三维度

**3. 费曼技巧的AI化应用**
- 东南大学"费曼学习法助手": "用户解释-AI反馈-反思重构"循环
- Prismer.AI: 64个主题模板引导简单语言解释，AI识别知识缺口
- AI+BEST高能经验萃取: 基于"鱼"模型的四步萃取法
- **当前Skill状态**: 🟡 可优化 - 可增加模板化引导

**4. Known Unknowns追踪**
- WebResearcher、SciEx等系统都强调明确标记未知边界
- scholar-deep-research的"饱和停止机制"和"自我批判阶段"
- **当前Skill状态**: 🟡 可优化 - 已有章节但缺乏系统化追踪

### 本次更新

**采纳的改进**

1. **Known Unknowns追踪机制增强** (v1.5.0)
   - 新增 `memory/known-unknowns-registry.md` 全局注册表
   - 定义问题分类标准（数据缺口/观点冲突/边界模糊/因果未明/时序未知）
   - 建立解决触发条件（主动/定时/质量）
   - 更新位置: SKILL.md "待深究的问题"章节

2. **费曼技巧模板化** (v1.5.0)
   - 新增"费曼引导模板库"概念
   - 针对不同主题类型提供结构化引导框架
   - 增加"AI追问模式"作为可选费曼验证路径
   - 更新位置: SKILL.md "费曼输出多智能体协作模式"章节

**不予采纳的改进**

| 改进建议 | 不采纳原因 |
|----------|-----------|
| 完全改用SPARK模型 | 当前五阶段工作流更贴合深度研究场景，已覆盖SPARK核心要素 |
| 增加64个具体主题模板 | 过于具体，维护成本高；采用更灵活的分类引导模板 |
| 集成LaTeX/学术写作 | 东东需求偏向实用知识管理，非学术发表 |

### 版本更新

**v1.4.1 → v1.5.0**

新增内容:
- Known Unknowns全局追踪机制
- 费曼技巧模板化框架
- AI追问模式（费曼验证变体）

优化内容:
- 明确Known Unknowns分类标准和触发机制
- 增强费曼阶段的结构化引导

### 下次迭代方向

1. 验证Known Unknowns追踪机制在实际Deep-Dive中的使用效果
2. 根据使用反馈优化费曼模板库的分类体系
3. 关注多模态研究工具的进展（图片/视频输入处理）

---

*迭代执行: 哆啦dora*
*迭代日期: 2026-05-30*
