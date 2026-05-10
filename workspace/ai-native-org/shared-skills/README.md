# 全局知识库 (shared-skills)

> 所有profile通过symlink共享的知识库

## 结构

```
shared-skills/
├── knowledge-base/          # 四类知识
│   ├── facts/              # 事实知识（What）
│   ├── patterns/           # 模式知识（How）
│   ├── decisions/          # 决策知识（Why）
│   └── feedback/           # 反馈知识（Result）
│
├── methodologies/          # 方法论Skill
│   ├── scientific-management/
│   ├── opc-framework/
│   └── redpoint/
│
└── templates/              # 知识模板
```

## 使用

用户profile通过symlink访问本目录：

```
profiles/{user}/shared-skills -> ../shared-skills
```

## 更新

- 修改本目录下的文件，所有profile立即生效
- 新增文件需遵循 METADATA-SCHEMA.md 规范
- 删除/归档需记录到 decisions/
