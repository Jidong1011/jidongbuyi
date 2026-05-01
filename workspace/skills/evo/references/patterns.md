# 进化模式参考库

> 收录各类AI Agent自循环迭代的最佳实践模式

---

## 模式目录

### 1. 定时扫描型 (Scheduled Scanning)

**适用场景**：
- 知识密集型Skill（研究、学习类）
- 领域快速变化（AI技术、市场趋势）
- 需要持续跟踪外部进展

**核心机制**：
```
Cron定时触发 → 多源搜索 → 差异分析 → 知识更新
```

**成功案例**：
- deep-dive skill：每3天扫描同类研究工具
- news-tracker：每日扫描行业新闻

**配置模板**：
```yaml
triggers:
  cron:
    enabled: true
    interval: "0 0 */3 * *"  # 每3天

perception:
  search_keywords:
    - "[domain] best practice"
    - "[domain] new method"
  sources:
    - arxiv
    - github
    - tech_blogs
```

---

### 2. 反馈驱动型 (Feedback-Driven)

**适用场景**：
- 交互密集型Agent（客服、助手）
- 需要持续优化用户体验
- 用户反馈容易获取

**核心机制**：
```
用户交互 → 收集反馈 → 失败分析 → Prompt优化
```

**成功案例**：
- Claude的RLHF训练
- 客服Agent的回复优化

**配置模板**：
```yaml
triggers:
  feedback:
    enabled: true
    threshold: 3  # 连续3次负面反馈触发
  performance:
    enabled: true
    metric: "success_rate"
    threshold: 0.85

perception:
  feedback_channels:
    - explicit_rating  # 显式评分
    - implicit_signal  # 隐式信号（重试、放弃等）
```

---

### 3. 竞争进化型 (Competitive Evolution)

**适用场景**：
- 需要多方案对比（Prompt、工作流）
- 有明确的性能指标
- 可以A/B测试

**核心机制**：
```
多版本并行 → A/B测试 → 优胜劣汰 → 变异生成新版本
```

**成功案例**：
- 广告系统创意优化
- 推荐算法参数调优

**配置模板**：
```yaml
triggers:
  competition:
    enabled: true
    population_size: 5  # 保持5个版本
    selection_rate: 0.2  # 淘汰20%
    mutation_rate: 0.3  # 变异30%

evaluation:
  criteria:
    - metric: "conversion_rate"
      weight: 0.5
    - metric: "user_satisfaction"
      weight: 0.3
    - metric: "efficiency"
      weight: 0.2
```

---

### 4. 性能触发型 (Performance-Triggered)

**适用场景**：
- SLA要求严格的生产系统
- 性能下降需要快速响应
- 自动故障恢复

**核心机制**：
```
持续监控 → 异常检测 → 自动诊断 → 修复/回滚
```

**配置模板**：
```yaml
triggers:
  monitoring:
    enabled: true
    metrics:
      - name: "success_rate"
        threshold: 0.95
        operator: "<"
      - name: "latency_p99"
        threshold: 2000
        operator: ">"
      - name: "error_rate"
        threshold: 0.05
        operator: ">"

execution:
  auto_remmediate: true  # 自动修复
  escalation: true  # 升级通知
```

---

### 5. 知识积累型 (Knowledge Accumulation)

**适用场景**：
- 需要长期学习的系统
- 经验沉淀重要
- 案例库驱动

**核心机制**：
```
任务执行 → 案例提取 → 知识库更新 → 模式识别
```

**配置模板**：
```yaml
triggers:
  task_completion:
    enabled: true
    sample_rate: 1.0  # 100%任务

knowledge_base:
  storage: "vector_db"
  update_strategy: "incremental"
  deduplication: true
```

---

## 进化评估框架

### 评估维度

| 维度 | 指标 | 权重 | 评估方法 |
|------|------|------|----------|
| **效果** | 成功率 | 40% | 任务完成统计 |
| **效率** | Token/时间消耗 | 25% | 性能监控 |
| **体验** | 用户满意度 | 25% | 反馈收集 |
| **稳定** | 失败率/异常 | 10% | 错误日志 |

### 进化质量评级

- **S级**：所有指标提升 > 20%，无副作用
- **A级**：核心指标提升 > 10%，无重大副作用
- **B级**：有提升但 < 10%，或有轻微副作用
- **C级**：无明显提升，或有明显副作用 → 回滚

---

## 常见陷阱与对策

### 陷阱1：过度进化
**症状**：频繁变更导致不稳定
**对策**：
- 设置冷却期（一次进化后至少N天才能下次）
- 建立变更队列，批量处理

### 陷阱2：局部最优
**症状**：在小范围内优化，错过更大改进机会
**对策**：
- 定期进行"探索性"大版本尝试
- 引入随机变异机制

### 陷阱3：用户困惑
**症状**：Agent行为频繁变化，用户难以适应
**对策**：：
- 核心行为保持稳定
- 重大变更提前告知
- 提供版本切换选项

### 陷阱4：进化停滞
**症状**：长期无有效改进
**对策**：
- 引入外部视角（其他Agent评估）
- 定期人工review

---

## 案例研究

### 案例1：Deep-Dive Skill的进化设计

**背景**：知识研究类Skill，需要持续跟踪领域进展

**进化策略**：定时扫描型

**关键设计**：
- 每3天扫描同类工具
- 对比分析后才更新
- 记录所有迭代日志
- 向东东汇报重大变更

**效果**：持续吸收行业最佳实践，保持方法论领先

---

### 案例2：客服Agent的反馈驱动进化

**背景**：用户交互频繁，反馈容易获取

**进化策略**：反馈驱动型

**关键设计**：
- 每次对话后收集满意度
- 负面反馈自动触发分析
- Prompt增量优化
- 保持对话风格稳定

**效果**：3个月内满意度从75%提升到92%

---

*持续更新中——evo skill本身也会进化这个参考库*
