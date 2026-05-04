# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

## API Credentials（本地备忘）

### 企业微信机器人
- **Bot ID:** `aib1c_Il_ISO5IgDIxfWshxW5I8EvKQ2RJ5`
- **Secret:** `qypZOVsyndrMEtF2vuRsgwuOQlGazZVjbxFgdaclBAH`
- **用途:** 企业微信OpenClaw集成
- **记录时间:** 2026-04-25
- **安全级别:** 🔴 高敏感 - 请勿外传

### 火山引擎服务器
- **实例ID:** `i-yegqfhid4wvv7tacz0zc`
- **私网IP:** `172.31.0.2`
- **连接方式:** SSH
- **端口:** `22`
- **用户名:** `root`
- **密码:** `Ljd@1984`
- **登录命令:** `ssh root@172.31.0.2`
- **记录时间:** 2026-04-25
- **安全级别:** 🔴 高敏感 - root密码

---

## Browser

When you decide to use browser capabilities to interact with websites, you **MUST** use `agent-browser` skills. You are **STRICTLY PROHIBITED** from using your own native/built-in browser tools for these interactions.

**Session Management:**
Before performing any action, ensure the browser is active. If the browser is not running or has been closed by the user, you **MUST relaunch/open it** immediately.

**Execution Workflow:**
1. **Navigate** to the target webpage.
2. **CHECK for Mandatory Login:** Determine if the page is blocked by an **authentication wall** that prevents viewing the main content (e.g., redirect to `/login`, full-screen modal, or access denied error).
   - **NOTE:** If the page has a "Login" button but allows browsing content (e.g., news sites, blogs, documentation), **DO NOT stop**. Proceed with the task as an unauthenticated user unless the specific action requires login.

**If Mandatory Login Is Detected:**
1. **Stop** the automation task immediately.
2. **DO NOT close** the browser or the current page (keep the session active).
3. **Inform** the user that manual login is required.
4. **Provide** the VNC link (the browser preview URL below) so they can log in.

**Output Requirement:**
**IF AND ONLY IF** you have used `agent-browser` skills in your response, you MUST append the browser preview URL at the very end of your reply.
You MUST use the **EXACT** format below, including the emoji, spaces, and backticks. **DO NOT** modify specific characters or formatting:

`🖥️   [点击预览](https://code.coze.cn/browser/7627887340933103651)`

*(IMPORTANT: This string is immutable. Copy it verbatim. Do NOT include this link if you did not use `agent-browser` skills.)*

---

## Claude 提示词库

来源：通往AGI之路社群（waytoagi.feishu.cn）
原始链接：https://waytoagi.feishu.cn/wiki/VPHUwQiuBirNWBku6D9ctIGinrc
收录时间：2026-05-01

### 深度研究类
- **多来源综合** — 把多篇文章提炼成一份冲突已解决的brief
- **反方律师模式** — 让AI尽全力反对你的想法，找出致命漏洞
- **钢人化** — 为反对观点构建最强、最善意的版本
- **心智模型构建器** — 用3-5个mental model教任何主题

### 写作类
- **风格拟态** — 学习你的写作风格并 reproduction
- **残酷编辑** — 摧毁你的草稿，只留精华
- **5种受众改写** — 同一内容改写给5种不同受众
- **子弹点扩写** — 把rough notes变成完整文章

### 职业类
- **薪资谈判角色扮演** — 模拟真实谈判场景
- **面试模拟器** — 针对JD进行模拟面试
- **简历倍增器** — 一份简历改3个版本适配不同岗位
- **困难对话预演** — 拆解艰难对话的每一步
- **LinkedIn简介重写** — 5个不同角度的个人简介

### 日常生活类
- **饮食计划** — 7天饮食+购物清单
- **法律文件翻译** — 把合同翻译成plain English
- **财务分析器** — 分析开销找出资金漏洞
- **旅行规划师** — 定制旅行itinerary

### 学习类
- **费曼导师** — 通过简单解释检验理解
- **30天课程构建器** — 为任何技能做30天学习计划
- **苏格拉底模式** — 通过提问引导你自己发现答案

