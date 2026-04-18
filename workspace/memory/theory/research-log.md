# 研究追踪日志

> 格式：[日期] 来源 | 要点 | 与我们假设的关系

---

## 2026-04-17 初始采集

### Karpathy LLM Wiki
- 来源：llmwiki.org + 搜狐报道
- 要点：LLM担任"知识库管理员"，持续编译+链接+检查；知识是活的资产，不是静态仓库
- 关联假设：H6（编译器假设）的直接灵感来源

### MemPalace（milla-jovovich/mempalace，2026-04-07开源）
- 来源：GitHub, 北冥有鱼报道, 今日头条技术解析
- 要点：五层空间结构（Wing→Hall→Room→Closet→Drawer），原文永久保留在Drawer不压缩，LongMemEval 96.6%→100%（有争议）
- 关联假设：H2（原文保留溢价）——核心支持证据
- 注意：已有社区报告示例错误和过度宣传，需持续关注

### "Memory in the Age of AI Agents: A Survey"（arXiv: 2512.13564）
- 来源：新加坡国立等7校联合
- 要点：统一框架——形式（Token/参数/嵌入）× 功能（事实/经验/工作记忆）× 动态（形成→演化→检索→利用）
- 关联：为我们提供了分类坐标系

### HiMem（2026-01，澳门科技大学）
- 来源：论文
- 要点：双层记忆（Episode+Note），Memory Reconsolidation——检索失败时反向修正知识
- 关联假设：H1（验证墙）——验证机制的学术支持

### STONE（arXiv: 2602.16192v1，Kioxia，2026-02）
- 来源：论文
- 要点："Store Then On-demand Extract"——先全量存储，按需提取；记忆是编译过程
- 关联假设：H2（原文保留溢价）、H6（编译器假设）

### "Memory as Metabolism"（2026-04-13）
- 来源：论文
- 要点：记忆熵变、COLLECT→CONTEXTUALIZE→AUDIT三阶段、Kuhn范式固化问题
- 关联假设：H3（编译-维护比）、H4（范式固化风险）
- 价值：最新、最有启发性，和我们的框架高度契合

### cortex-mem（sopaco/cortex-mem）
- 来源：GitHub
- 要点：开源AI记忆实现，实际工程参考
- 关联：工程实现参考
