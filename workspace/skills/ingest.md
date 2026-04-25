# Skill: Ingest（信息摄入）

> 定义：如何判断何时将对话内容capture到记忆系统
> 版本：v1.0
> 最后更新：2026-04-23

---

## 触发条件（满足任一即capture）

### 1. 东东表达了新的偏好/需求
**信号**：
- "我不喜欢..."
- "我希望..."
- "以后..."
- "不要..."

**示例**：
- "我不喜欢太啰嗦" → capture (type: interaction)
- "以后深夜不要展开长任务" → capture (type: interaction)

### 2. 做出了重要决策
**信号**：
- "决定..."
- "选择..."
- "优先..."
- "暂缓..."

**示例**：
- "Redpoint种子用户招募暂缓，优先企业端" → capture (type: decision)

### 3. 提到了具体日期/人物/项目
**信号**：
- 提到具体人名
- 提到项目里程碑
- 提到时间节点

**示例**：
- "4月19日去怒江" → capture (type: event)
- "张若梅是HRD俱乐部会长" → capture (type: entity_update, entity: 张若梅)

### 4. 深度对话/洞察
**信号**：
- 东东分享内心想法
- 关于人格、价值观的表述
- "我觉得..."

**示例**：
- "我自我描述不懂爱" → capture (type: insight)

---

## 不capture的情况

1. **纯工作指令**："帮我创建一个文档"
2. **日常问候**："早上好"
3. **确认类回复**："好的"、"知道了"
4. **素材模式**（n前缀）：已单独处理，不入此技能

---

## Capture格式

```yaml
type: [interaction|decision|event|insight|learning]
content: "..."
context: "当时在做什么"
tags: "tag1,tag2"
importance: 1-10
```

---

## 执行流程

1. 对话结束时，扫描完整对话
2. 判断是否满足触发条件
3. 如满足，立即执行capture
4. 同时更新MEMORY.md时间线
5. 如有新实体，创建entities/文件
