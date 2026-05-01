# Evo 进化系统总目录

> 东东设计的所有AI Agent自循环迭代进化系统
> 更新规则：每次设计新进化系统后自动追加

---

## 进化系统清单

### 1. Deep-Dive Skill 进化系统
- **目标Skill**：deep-dive
- **进化策略**：定时扫描型
- **执行周期**：每3天
- **Cron Job ID**：`deep-dive-skill-evolution`
- **设计日期**：2026-04-30
- **状态**：✅ 运行中
- **迭代日志**：`/skills/deep-dive/references/evolution-log.md`

**进化机制**：
- 扫描同类深度研究/费曼学习工具
- 分析方法论差异
- 更新SKILL.md和最佳实践

---

### 2. Evo Skill 自进化系统
- **目标Skill**：evo（元级别自指）
- **进化策略**：定时扫描型
- **执行周期**：每7天
- **Cron Job ID**：`evo-skill-evolution`
- **设计日期**：2026-04-30
- **状态**：✅ 运行中
- **迭代日志**：`/skills/evo/references/evolution-log.md`

**进化机制**：
- 扫描AI Agent自循环迭代最新研究
- 更新进化模式库
- 优化评估框架

---

## Evo Skill 设计方案

- **文档链接**：[https://www.feishu.cn/docx/Dts3dwdEnoK1UXxUE89crzRvnmb](https://www.feishu.cn/docx/Dts3dwdEnoK1UXxUE89crzRvnmb)
- **一句话本质**：让AI从"被维护的工具"进化为"会自我学习的生命体"
- **核心出处**：March (1991) 探索-利用权衡; Maturana & Varela 自指系统; DeepMind RL
- **应用场景**：任何需要持续改进的AI Agent/Skill/System
- **设计日期**：2026-04-30

---

## 统计

- **总进化系统数**：2
- **运行中**：2
- **暂停**：0
- **最后更新**：2026-04-30

---

## 设计模板

新增进化系统时，使用以下模板记录：

```markdown
### N. [Skill名] 进化系统
- **目标Skill**：[skill-name]
- **进化策略**：[定时扫描/反馈驱动/竞争进化/性能触发/知识积累]
- **执行周期**：[周期]
- **Cron Job ID**：`[job-id]`
- **设计日期**：[日期]
- **状态**：[运行中/暂停/设计中]
- **迭代日志**：[路径]

**进化机制**：
- [机制1]
- [机制2]
```
