# Deep-Dive 母文档目录

> 东东深度研究学习成果总目录  
> 更新规则：每次deep-dive完成后自动追加  
> 分类：AI与智能体 | 组织与管理 | 商业与产品 | 技术与工具 | 其他

---

## 📋 Deep-Dive Skill 迭代日志

| 日期 | 版本 | 核心改进 |
|------|------|----------|
| 2026-05-06 | v2026.05-1 | 引入Planner-Executor-Checker三段式架构；增加可复现性保障（中间产物存档）；强化知识图谱构建 |
| 2026-05-03 | v2026.05 | 多智能体费曼协作；Deep Research四大模块；知识图谱构建 |
| 2026-04-30 | v1.0 | 初始版本建立 |

**当前版本特性**：
- ✅ 六阶段工作流（Planning → Research → Learning → Feynman → Verification → Application）
- ✅ 质量自控：Checker校验清单 + 降级策略
- ✅ 可复现性：中间产物存档规范
- ✅ 深度保障：RAG+知识图谱双引擎
- ✅ 费曼输出：多智能体协作 + 对抗性验证

---

---

## AI与智能体

### Anthropic Managed Agents 架构
- **文档链接**：[https://www.feishu.cn/docx/F7umdhQZcoD2DaxoSWUcnktqnAb](https://www.feishu.cn/docx/F7umdhQZcoD2DaxoSWUcnktqnAb)
- **一句话本质**：Managed Agents是Anthropic把"从原型到生产"的Agent基础设施打包成云服务——你只定义Agent的脑子（提示词+工具），沙箱、状态、凭证、错误恢复全部托管
- **核心出处**：Anthropic Engineering博客《Scaling Managed Agents: Decoupling the brain from the hands》（2026-04-08）；官方API文档；三层解耦架构（Brain/Hands/Session）
- **应用场景**：Agent架构设计参考、技术选型决策（Managed Agents vs OpenClaw vs OpenAI Assistants）、成本估算、多Agent协作模式
- **整理日期**：2026-05-15
- **关键洞察**：Session≠Context Window（事件日志比无限上下文更适合长程任务）；Harness假设随模型升级过时，解耦是必然；与OpenClaw是互补而非替代关系

### 延展心智与系统极限
- **文档链接**：[https://www.feishu.cn/docx/BabTdRtEcoqt5ixxhF5codWZnwy](https://www.feishu.cn/docx/BabTdRtEcoqt5ixxhF5codWZnwy)
- **一句话本质**：所谓"人类极限"其实是"当前技术系统下的极限"——当工具被真正内化成为认知的一部分，人+工具的组合将超越任何单一元素，这正是AI时代个人竞争力的核心来源
- **核心出处**：Clark & Chalmers (1998) "The Extended Mind"; 鲨鱼皮泳衣禁令(2010); 半人马棋Kasparov(1998); 记忆宫殿神经科学
- **应用场景**：理解AI时代个人核心竞争力、OPC能力建设、人机协作策略、认知增强方法
- **整理日期**：2026-05-08
- **关键洞察**：人+AI > AI alone，关键变量是"人与AI的接口效率"

### Epiplexity（认知复杂度）
- **文档链接**：[https://www.feishu.cn/docx/DbkcdkUhzow8KFxiFXRck14nnPd](https://www.feishu.cn/docx/DbkcdkUhzow8KFxiFXRck14nnPd)
- **一句话本质**：在有限算力约束下，观察者能从数据中提取的、可复用、可泛化的结构性信息总量——从"神的视角"到"人的视角"的信息论革命
- **核心出处**：Finzi et al. (2026) arXiv:2601.03220; CMU & NYU联合团队
- **应用场景**：预训练数据筛选、课程学习设计、合成数据评估、Redpoint数据价值评估
- **整理日期**：2026-05-05

### AI原生组织
- **文档链接**：[https://www.feishu.cn/docx/DFxMdvDxQoq0vMxhhAVceB1cnpc](https://www.feishu.cn/docx/DFxMdvDxQoq0vMxhhAVceB1cnpc)
- **一句话本质**：AI原生组织不是"用AI的工具"，而是"为AI重生的组织"——从组织结构、决策流程到价值创造方式，全部围绕人机协同智能重新设计。
- **核心出处**：Wolfe et al. (2025) 2×2 AI转型框架; OrgAgent三层治理模型(港中文, 2026); 传神CAIO实践
- **应用场景**：Redpoint项目组织设计、纪东不已IP运营架构、OPC模式升级
- **整理日期**：2026-04-30

---

## 产业与趋势

### 生物制造产业
- **文档链接**：[https://www.feishu.cn/docx/SseWdp37poRi8exBYuucRrjLn0b](https://www.feishu.cn/docx/SseWdp37poRi8exBYuucRrjLn0b)
- **一句话本质**：生物制造是用"生命编程"替代"化石能源+化学合成"的新生产方式，让细胞成为微型工厂，用二氧化碳、秸秆等可再生原料制造人类所需的一切
- **核心出处**：2025生物制造大会/工信部；中科院天津工业生物所《Science》；赛迪研究院
- **应用场景**：医药投资、产业政策研究、技术趋势判断、创业方向选择
- **整理日期**：2026-05-07

### CodeBanana AI原生协作平台
- **文档链接**：[https://www.feishu.cn/docx/GOxtdVi6UoF0Mxx8vkJcJlR6nVc](https://www.feishu.cn/docx/GOxtdVi6UoF0Mxx8vkJcJlR6nVc)
- **一句话本质**：CodeBanana不是"带AI功能的协作工具"，而是"以智能体为组织细胞的操作系统"——让每个项目成为人+Agent共生的活体，让沟通与执行同步发生
- **核心出处**：《超级组织》李志飞/高佳；出门问问官方发布；世界经济论坛WEF报告
- **应用场景**：软件开发团队协作、AI原生组织建设、工具选型决策、人机协同流程设计
- **整理日期**：2026-05-07

### 《卓越的基因》核心方法论
- **文档链接**：[https://www.feishu.cn/docx/EwXxdOTMRoPsBvx2fLfcKJHpnIf](https://www.feishu.cn/docx/EwXxdOTMRoPsBvx2fLfcKJHpnIf)
- **一句话本质**：卓越不是追求的结果，而是"慷慨冲动×放手一搏×信任赌注×关系优先×价值观驱动×享受过程"这套认知范式自然涌现的副产品
- **核心出处**：《卓越的基因》吉姆·柯林斯/比尔·拉齐尔；皮格马利翁效应研究；胖东来管理实践
- **应用场景**：个人职业发展、团队管理、创业决策、组织文化建设
- **整理日期**：2026-05-07

### 工业大模型：从流程驱动到模型驱动
- **文档链接**：[https://www.feishu.cn/docx/Qa7OdWvoZoezoDxhAl8cdDUrnKf](https://www.feishu.cn/docx/Qa7OdWvoZoezoDxhAl8cdDUrnKf)
- **一句话本质**：工业大模型不是"通用AI套工业壳"，而是用"数据+机理双驱动"重构工业生产范式，让机器从"执行指令"进化到"理解场景、自主决策"
- **核心出处**：亿欧智库《2026中国工业大模型发展洞察报告》；国家电网光明电力大模型；海康威视观澜大模型
- **应用场景**：工业投资决策、智能制造项目评估、技术选型、产业趋势判断
- **整理日期**：2026-05-07

### 生活美容行业：颜值经济升级与科技赋能
- **文档链接**：[https://www.feishu.cn/docx/SscZdrUm0omRoAxv38LcPhbWnzc](https://www.feishu.cn/docx/SscZdrUm0omRoAxv38LcPhbWnzc)
- **一句话本质**：生活美容行业正从"表面修饰"向"生命管理"跃迁，从"经验驱动"转向"数据驱动"，科技赋能与消费分层共同重塑万亿级美业生态
- **核心出处**：中研普华《2024-2029年中国生活美容行业市场深度分析与发展趋势报告》；艾媒咨询《中国美业白皮书》；英敏特《2026年全球美容与个人护理趋势预测》
- **应用场景**：美业投资、品牌定位、产品设计、技术选型、下沉市场策略
- **整理日期**：2026-05-07

### 云南HRD俱乐部AI专委会建设方案（重构版）
- **文档链接**：[https://www.feishu.cn/docx/L5IXd4kMIoiMGZxhgPVcNGLdnRg](https://www.feishu.cn/docx/L5IXd4kMIoiMGZxhgPVcNGLdnRg)
- **一句话本质**：云南HRD俱乐部AI专委会不是学习型组织，而是面向AI时代的人力资源变革实验室——以HR真实场景为入口，以AI Agent协作为引擎，让云南HRD成为AI时代组织变革的推动者
- **核心出处**：Gartner《2026年CHRO优先事项》；智联招聘×北大国发院《2026人力资源管理趋势报告》；华为/阿里/腾讯AI组织架构案例；混沌学园运营模式
- **应用场景**：云南HRD俱乐部AI专委会筹建启动、对外宣讲、企业试点招募、纪东不已IP方法论沉淀
- **整理日期**：2026-05-08（基于东东反馈重构）
- **关键优化**：五阶段可执行路径+AI双三角方法模型+三层AI原生架构+情绪钩子开场

### 云南HRD俱乐部AI专委会：AI组织化变革与纪东不已IP融合方案（初版）
- **文档链接**：[https://www.feishu.cn/docx/FIfgdb305oVRSXxvMIocGhevnCb](https://www.feishu.cn/docx/FIfgdb305oVRSXxvMIocGhevnCb)
- **一句话本质**：以"AI双三角"方法论为内核，打造云南首个HRD驱动的AI组织变革实践平台——通过"认知升级×交互共创×联盟生态"三位一体模式，让AI从工具变成组织进化的基因
- **核心出处**：Gartner《2026年CHRO优先事项》；智联招聘×北大国发院《2026人力资源管理趋势报告》；华为/阿里/腾讯AI组织架构案例；混沌学园运营模式
- **应用场景**：云南HRD俱乐部AI专委会筹建、纪东不已IP运营、一堂AI双三角本地化落地、HR组织变革咨询
- **整理日期**：2026-05-07
- **备注**：已基于东东反馈重构为新版本

### AIhot：2026年AI热点全景与爆款应用深度解析
- **文档链接**：[https://www.feishu.cn/docx/SEWLdePEsof1mJxGZU5cKSQrn7d](https://www.feishu.cn/docx/SEWLdePEsof1mJxGZU5cKSQrn7d)
- **一句话本质**：2026年AI正从"技术炫技"转向"价值落地"——从比拼参数到比拼场景，从预测下一个词到预测世界状态，从单点工具到系统生产力，真正的AI应用开始重构工作与生活
- **核心出处**：智源研究院《2026十大AI技术趋势》；周鸿祎《2026年20个AI预言》；Gartner/IDC AI应用数据；GitHub/OpenAI Agent编程实践
- **应用场景**：内容创作选题、投资/创业机会识别、HR人才需求预测、纪东不已IP趋势解读
- **整理日期**：2026-05-08
- **十大方向**：智能体平台、多模态AI、AI编程、AI搜索、AI内容创作、AI硬件、科学智能（AI4S）、具身智能、端侧小模型、AI安全治理

### 米哈游LPM 1.0：角色表演生成的革命
- **文档链接**：[https://www.feishu.cn/docx/VgsKdn2Mhoz9VyxqCkWcuv2NnCe](https://www.feishu.cn/docx/VgsKdn2Mhoz9VyxqCkWcuv2NnCe)
- **一句话本质**：LPM 1.0是米哈游用170亿参数打造的「虚拟演员」——它不生成风景，只生成角色的喜怒哀乐；不追求画面精美，只追求表演真实；不满足于生成一段视频，而是要让角色像真人一样「会说、会听、会反应」，持续陪你聊天几个小时都不会「走样」
- **核心出处**：arXiv:2604.07823论文；曾爱玲通讯作者；Anuttacon公司；170亿参数DiT架构
- **应用场景**：游戏NPC深度对话、虚拟陪伴与虚拟主播、游戏过场动画实时生成、教育培训角色扮演、纪东不已IP虚拟角色化
- **整理日期**：2026-05-12
- **关键洞察**：「特化路线」可能比「通用路线」更适合游戏；全双工实时交互是下一代游戏的关键差异点；无限时长生成打破了游戏叙事的时间限制

### AI编程Agent方法论：多Agent协作与Missions系统
- **文档链接**：[https://www.feishu.cn/docx/ZkYtdmbweoX94WxjArecO7SQnIe](https://www.feishu.cn/docx/ZkYtdmbweoX94WxjArecO7SQnIe)
- **一句话本质**：AI工程化的核心瓶颈已从"模型智能"转向"人类注意力带宽"，解决方案是构建可审计、可恢复的多Agent协作系统，而非追求单点智能突破
- **核心出处**：Galorey Bokan（阿里工程师）方法论；Factory AI Missions系统（40天连续运行）；Anthropic多Agent协作指南（2026-04）；Google Research Agent扩展科学论文
- **应用场景**：企业级代码库迁移、AI工程化流程设计、多Agent系统架构、团队AI编程规范制定
- **整理日期**：2026-05-13
- **关键洞察**：验证契约提前拦截37%潜在问题；创作者-验证者上下文隔离是核心；串行优先原则（仅允许只读操作并行）

### Agent效率革命：多Agent并行工作流与Agentfile
- **文档链接**：[https://www.feishu.cn/docx/FMiqd48tMozb5PxdHOwcrqJtn0e](https://www.feishu.cn/docx/FMiqd48tMozb5PxdHOwcrqJtn0e)
- **一句话本质**：当AI Agent从"单兵作战"进化到"多人军团"，核心挑战从"怎么让Agent干活"变成"怎么管理同时跑的十几个Agent"——文件管理、任务收口、结果预览成为新的效率瓶颈
- **核心出处**：Boris Cherny（Claude Code创始人）并行工作流（5个Claude同时跑）；Thariq Shihipar《The Unreasonable Effectiveness of HTML》；Agentfile开源项目（基于Wave改造）
- **应用场景**：多项目并行开发、Agent产出Review与收口、HTML交付物生成、CLAUDE.md团队记忆配置
- **整理日期**：2026-05-13
- **关键洞察**：收口比生产更重要；开发者从"写代码的人"变成"看结果做决策的人"；HTML是AI输出的新格式标准

### Hermes Kanban 多Agent协作
- **文档链接**：[https://www.feishu.cn/docx/Abt8dSw7ooYM2Pxs5MqcSgvwnhg](https://www.feishu.cn/docx/Abt8dSw7ooYM2Pxs5MqcSgvwnhg)
- **一句话本质**：Hermes Kanban是"给AI打工仔们排班的共享任务看板"——通过持久化SQLite任务队列、原子事务认领、六列状态流转和Dispatcher调度器，让多个独立Agent像真实团队一样并行工作、自动流转、失败重试
- **核心出处**：Hermes Agent官方文档v0.12.0+；Nous Research GitHub仓库；Kanban Tutorial官方教程；社区对比分析文章
- **应用场景**：多Agent自动化流程设计、任务状态管理、失败重试机制、与OpenClaw互补使用
- **整理日期**：2026-05-14
- **关键洞察**：六列状态流转对应真实开发流程；原子事务解决Agent竞争问题；与OpenClaw是互补而非替代关系

### AI PPT生成的Skill革命：从提示词到技能工程
- **文档链接**：[https://www.feishu.cn/docx/BGh6d1pj5oHo3ixrQWzcWNpVnSg](https://www.feishu.cn/docx/BGh6d1pj5oHo3ixrQWzcWNpVnSg)
- **一句话本质**：AI做PPT的瓶颈已经从"能不能做"变成"能不能保持设计一致性"——guizang-ppt-skill用SKILL.md把10年设计经验编码成AI可执行的7条设计纪律，证明了"Skill是AI时代的设计系统"
- **核心出处**：歸藏guizang-ppt-skill（GitHub 6000+ Star）；GPT-Image 2.0配图集成；瑞士国际主义设计传统（Vignelli/Müller-Brockmann）；Agent Skills范式（从Prompt到Skill）
- **应用场景**：PPT自动生成、多平台封面适配、设计一致性保障、Skill驱动内容生产
- **整理日期**：2026-05-13
- **关键洞察**：7条设计纪律是10年经验的规则化；AI只能做70分，剩下30分需要人工微调；跨工具视觉漂移是最大隐形成本；Skill=设计系统的AI可执行版本

### 信息源治理：伯乐Skill与AI时代的信息饮食管理
- **文档链接**：[https://www.feishu.cn/docx/MpA0dtgUNoU4Baxu7OLcIPi4nYe](https://www.feishu.cn/docx/MpA0dtgUNoU4Baxu7OLcIPi4nYe)
- **一句话本质**：在AI让信息获取成本趋近于零的时代，真正稀缺的不是信息量，而是判断力——伯乐Skill的本质是一个"信息源的质检员"，它不帮你消费更多内容，而是帮你筛选值得消费的内容
- **核心出处**：卡尔（AI沃茨）伯乐Skill（GitHub LearnPrompt/ai-news-radar）；150+信息源实践经验；赫拉利《智人之上》"信息饮食"理论；西蒙注意力经济学
- **应用场景**：个人信息源评估与管理、AI日报自动化、信源分层架构（一手源/聚合源）、信息焦虑治理
- **整理日期**：2026-05-13
- **关键洞察**：伯乐三绝招（找最佳入口/分层管理/学养马技术）；7天观察期+65%差异度阈值；原始来源是信息的身份证；判断力比获取能力更稀缺

### 周鸿祎「五虾模型」：AI辅助CEO决策的五角色Agent体系
- **文档链接**：[https://www.feishu.cn/docx/SEWpdvUNzoKUHsxnZR6cAyZxncg](https://www.feishu.cn/docx/SEWpdvUNzoKUHsxnZR6cAyZxncg)
- **一句话本质**：周鸿祎提出"AI的未来不是大模型，而是一群能干活的智能体"——五虾模型是CEO级落地框架：5个专业Agent（情报调研/需求洞察/组织诊断/科学决策/CEO助理）围绕CEO组成"虚拟高管团队"
- **核心出处**：周鸿祎2026年5月直播/抖音（五角色全景图）+ 2026节点增长大会"一九五"框架 + ISC.AI 2025 L1-L5分级
- **应用场景**：CEO决策支持、企业AI转型、OPC创业者个人能力增强、Redpoint项目架构参考
- **整理日期**：2026-05-13
- **关键洞察**：五虾模型=L4多Agent协作的CEO场景落地；哆啦dora正在自然演化为东东的CEO助理Agent；每个Agent有具体工具箱和交付物

### 本周AI论文精选深度解读（2026.5.4-5.10）：10篇前沿论文分类研究
- **文档链接**：[https://www.feishu.cn/docx/SZOfd3BYno6ApWxIxj0celoDnNf](https://www.feishu.cn/docx/SZOfd3BYno6ApWxIxj0celoDnNf)
- **一句话本质**：本周论文的核心主题是"Agent系统工程化"——从协调架构、训练方法、评估基准到安全验证，AI正在从单点智能走向可工程化的多Agent协作系统
- **核心出处**：DAIR.AI 本周AI论文精选；HeavySkill（arXiv:2605.02396）；Conductor/Sakana AI（ICLR 2026）；Coordination as Architecture（arXiv:2605.03310）；Self-Improving Pretraining/Meta FAIR；Horizon Generalization/Microsoft Research
- **应用场景**：Agent系统架构设计、Agent训练方法选择、Agent评估基准理解、Agent安全治理
- **整理日期**：2026-05-13
- **关键洞察**：三大趋势（协调成为一等公民/长horizon是共同挑战/Agent系统正在工程化）；5个分类（架构/训练/评估/记忆/安全）

### AI Agent的正确形态：深度研究与费曼学习笔记
- **文档链接**：[https://www.feishu.cn/docx/P3wMdWbego9XEdx7BC1cHp2LnQg](https://www.feishu.cn/docx/P3wMdWbego9XEdx7BC1cHp2LnQg)
- **一句话本质**：AI Agent的正确形态不是独立App中的万能助手，而是嵌入常用聊天软件、由多个专业agent协同工作、拥有统一记忆系统的"AI团队"
- **核心出处**：郎瀚威Will《龙虾实际产品形态预测》（2026-02-25）；OpenClaw多agent架构技术文章；AgentMemory技术方案；企业级部署报告
- **应用场景**：AI产品形态设计、多agent系统架构、记忆系统选型、企业级agent部署、创业方向识别
- **整理日期**：2026-05-16
- **关键洞察**：交互频率决定论（嵌入式vs独立App）；多agent分工比单agent全能更高效；记忆系统是当前最大短板；5大创业方向（Telegram原生管理层/大总管调配层/统一记忆系统/维护面板/企业合规封装）

---

## 组织与管理

### AI时代工程团队管理：Anthropic Claude Code团队实践
- **文档链接**：[https://www.feishu.cn/docx/E7LOdYmk7oe7XHxydoCcrlYlnMe](https://www.feishu.cn/docx/E7LOdYmk7oe7XHxydoCcrlYlnMe)
- **一句话本质**：当AI让写代码变得几乎免费，工程管理的核心矛盾从"如何让工程师写得更快"转向"如何让人+AI的协作系统产出更高质量的决策"——代码不再是稀缺资源，人类判断力才是。
- **核心出处**：Fiona Fung (Anthropic) Code with Claude 2026演讲；Anthropic Harness Engineering论文；Claude Code创始人Cyril Kirsanov访谈
- **应用场景**：OPC/一人公司工程管理、小团队组织设计、AI辅助决策、产品管理JIT Planning
- **整理日期**：2026-05-13

---

## 商业与产品

### 大圣AI超级个体咨询模式
- **文档链接**：[https://www.feishu.cn/docx/QEwRd21q8obJBTx1y0scVNydnye](https://www.feishu.cn/docx/QEwRd21q8obJBTx1y0scVNydnye)
- **一句话本质**：在AI生产力重构时代，将"碳基智慧（人）+硅基执行（AI）"的分工优势极致化，从一对多培训转向高价值一对一咨询，本质是**时间价值的重新定义与商业模式的结构性跃迁**
- **核心出处**：大圣AI个人主页; 《2025年中国数字经济创业白皮书》; CSDN知识变现研究; CSTD调研报告
- **应用场景**：培训从业者转型咨询、技术专家商业化、Redpoint服务产品设计、OPC商业模式升级
- **整理日期**：2026-05-02

---

## 技术与工具

### AiToEarn平台
- **文档链接**：[待创建，参考之前的研究输出]
- **一句话本质**：面向OPC的AI内容营销智能体平台，实现"创作→发布→互动→变现"全链路自动化
- **核心出处**：GitHub yikart/AiToEarn (10.5k stars); 掘金完全指南
- **应用场景**：纪东不已IP内容矩阵、Redpoint内容运营
- **整理日期**：2026-04-30

---

## 方法论

### Evo：AI Agent自循环迭代进化系统
- **文档链接**：[https://www.feishu.cn/docx/Dts3dwdEnoK1UXxUE89crzRvnmb](https://www.feishu.cn/docx/Dts3dwdEnoK1UXxUE89crzRvnmb)
- **一句话本质**：让AI从"被维护的工具"进化为"会自我学习的生命体"——通过持续感知环境、评估表现、改进自身，实现无需人工干预的自主进化
- **核心出处**：March (1991) 探索-利用权衡; Maturana & Varela 自指系统; DeepMind强化学习
- **应用场景**：Deep-Dive Skill自进化、任何AI Agent持续改进
- **整理日期**：2026-04-30

## 技术与工具

### Warp Terminal
- **文档链接**：[https://www.feishu.cn/docx/XD59d83FVotyRlxB6gMc2QGEnsc](https://www.feishu.cn/docx/XD59d83FVotyRlxB6gMc2QGEnsc)
- **一句话本质**：不是"带AI功能的终端"，而是"以终端为界面的AI Agent"——把命令行从"记忆语法的人机交互"变成"自然语言意图驱动"
- **核心出处**：Warp官方博客(Terminal-Bench 52% SOTA); Jason Warner(前GitHub CTO)
- **应用场景**：日常开发、运维操作、团队协作、命令行学习
- **整理日期**：2026-04-30

### Obsidian+AI知识工作系统
- **文档链接**：[https://www.feishu.cn/docx/XIecd3uQiobGntxWAw9cFM9Pn8e](https://www.feishu.cn/docx/XIecd3uQiobGntxWAw9cFM9Pn8e)
- **一句话本质**：Obsidian+AI不是"带AI功能的笔记软件"，而是"以本地Markdown为数据基座、以双向链接为知识结构、以AI为认知增强引擎"的自主可控知识操作系统——让知识从"死的仓库"变成"活的大脑"
- **核心出处**：Obsidian官方文档；Copilot for Obsidian插件；Tiago Forte《Building a Second Brain》；Sönke Ahrens《How to Take Smart Notes》；Ollama本地LLM部署
- **应用场景**：个人知识管理、内容创作工作流、纪东不已IP内容管理系统、研究资料整理
- **整理日期**：2026-05-07

---

## 摄影与内容创作

### 天文通APP与Pocket 3星空延时摄影
- **文档链接**：[https://www.feishu.cn/docx/WKjadow8iodl5Hx349dcg80vnmf](https://www.feishu.cn/docx/WKjadow8iodl5Hx349dcg80vnmf)
- **一句话本质**：用天文通预判拍摄条件，用Pocket 3记录恒星视运动，用后期堆栈合成星轨——将「不可控的星空」变成「可规划的内容资产」
- **核心出处**：天文通官方文档; DJI大疆社区实测参数; StarStaX软件原理
- **应用场景**：纪东不已IP内容创作、一堂云南学习中心活动记录、个人技能展示
- **整理日期**：2026-05-03

---

## 健康与医疗

### 血糖仪：核心原理与数值差异
- **文档链接**：[https://www.feishu.cn/docx/DNXHdNyzgoiXO8xgze3cl84UnLc](https://www.feishu.cn/docx/DNXHdNyzgoiXO8xgze3cl84UnLc)
- **一句话本质**：血糖仪是通过酶促反应将葡萄糖浓度转化为电信号的微型生化分析仪，不同设备数值差异源于酶种类、血样类型、红细胞压积和校准标准的系统性差异
- **核心出处**：ISO 15197:2013国际标准；GOD/GDH/HK三种酶促反应原理；CGM三代传感器技术；持续葡萄糖监测临床专家共识2024
- **应用场景**：血糖仪选购、数值差异解释、糖尿病日常监测、CGM选择决策
- **整理日期**：2026-05-14
- **关键洞察**：血糖仪测全血而生化仪测血浆，两者本就测的不是同一样本；CGM测组织间液有5-15分钟延迟；ISO允许±15%误差是临床可接受范围

---

## 统计

- **总研究主题数**：26（含1个重构版）
- **最后更新**：2026-05-16
