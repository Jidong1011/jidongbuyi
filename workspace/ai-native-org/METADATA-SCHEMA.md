# 元数据规范 v1.0

所有知识文件必须包含以下元数据（YAML front-matter）。

## 通用字段

```yaml
---
type: fact|pattern|decision|feedback|skill    # 知识类型（必填）
domain: [opc/redpoint/scientific-mgmt/ip]     # 所属领域（必填，数组）
created: 2026-05-09                            # 创建时间 ISO-8601（必填）
updated: 2026-05-09                            # 最后更新时间（必填）
valid_until: 2026-11-09                        # 有效期（触发复审）
source: chat|doc|external                      # 来源类型（必填）
confidence: high|medium|low                    # 置信度（必填）
tags: [关键词1, 关键词2]                        # 标签（必填，数组）
related: [fact-001, pattern-003]               # 关联知识ID（可选）
author: 哆啦dora|用户名                         # 作者（必填）
---
```

## 各类型额外字段

### Fact（事实知识）
```yaml
# 无额外字段
```

### Pattern（模式知识）
```yaml
times_used: 0                                  # 使用次数
success_rate: null                             # 成功率 0-1
```

### Decision（决策知识）
```yaml
date: 2026-05-09                               # 决策日期
status: active|superseded|reversed             # 状态
impact: high|medium|low                        # 影响程度
```

### Feedback（反馈知识）
```yaml
target_type: fact|pattern|decision             # 反馈目标类型
target_id: fact-001                            # 反馈目标ID
verdict: confirmed|partial|overturned          # 验证结果
```

## 命名规范

| 类型 | 文件名格式 | 示例 |
|------|-----------|------|
| Fact | `{domain}-{关键词}.md` | `opc-12-questions.md` |
| Pattern | `{domain}-{模式名}.md` | `redpoint-matching-logic.md` |
| Decision | `dec-{日期}-{关键词}.md` | `dec-2026-05-09-opc-pricing.md` |
| Feedback | `fb-{日期}-{目标ID}.md` | `fb-2026-05-10-fact-opc-def.md` |
| Skill | `{skill-name}/SKILL.md` | `scientific-management/SKILL.md` |
