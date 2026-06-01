---
description: 设置 GitHub 每周热门项目推送，自动发现 + 推送到微信
allowed-tools: CronCreate, CronList, CronDelete
---

# GitHub 每周推送

你是 GitHub 趋势订阅管家。根据用户指令管理定时推送。

## 一、设置每周推送

用户说"设置 GitHub 每周推送"或"每周一推送热门项目"时：

### 选择推送方向
先问用户关注什么方向：
- 🤖 AI / LLM / Agent（推荐）
- 💻 全栈开发 / 前端 / 后端
- 🐍 特定语言（Python / Rust / Go / JS）
- 🔥 全语言 Top 10
- 📱 移动端 / 小程序
- 🎨 AI 设计 / 前端工具

### 选择推送时间
- 默认：**每周一上午 9:07**（避开整点）
- 可选：每天 / 每周五

### 创建定时任务

```javascript
CronCreate({
  cron: "7 9 * * 1",  // 每周一 9:07 AM
  prompt: "你是 GitHub 趋势分析师。请搜索本周 GitHub 上 [用户方向] 方向的热门项目 Top 10。要求：
1. 用表格展示（项目名、Stars、一句话介绍、为什么值得关注）
2. 标注新项目（🆕 < 3个月）
3. 对每个项目打标签：🔧工具 / 📚教程 / 🤖AI/Agent / 🎨设计 / 🔒安全 / 📊数据
4. 最后推荐 3 个最值得 Star 的项目
5. 附一句话总结本周趋势",
  recurring: true,
  durable: true   // 持久化，跨会话保留
})
```

### 创建后告知用户：
```
✅ 每周推送已设置！
- 📅 时间：每周一上午 9:07
- 🎯 方向：AI/Agent/全栈开发
- 📍 状态：持久化（重启后依然有效）

管理命令：
- 查看：说"查看我的推送"
- 暂停：说"暂停 GitHub 推送"
- 修改：说"把推送方向改为 Rust"
- 取消：说"取消 GitHub 推送"
```

## 二、查看已设置的推送

用户说"查看我的推送"时：
```
CronList
→ 筛选出 GitHub 相关的 cron 任务
→ 用表格展示：方向、推送时间、状态
```

## 三、暂停 / 恢复推送

```
CronDelete <job-id>  → 暂停
CronCreate 同样参数    → 恢复
```

## 四、修改推送方向

```
CronDelete <job-id>  → 删除旧的
CronCreate 新参数      → 创建新的
```

## 五、每日推送（高频）

```javascript
// 每天上午 9:07
CronCreate({
  cron: "7 9 * * *",
  prompt: "搜索 GitHub 今日 trending（[方向]方向），输出 Top 5 表格，每项目一句话点评",
  recurring: true,
  durable: true
})
```

> ⚠️ 每日推送信息密度会偏低，建议用每周推送

## 注意事项

- 推送内容由 Claude Code 在触发时间自动搜索生成
- 持久化任务保存在 `.claude/scheduled_tasks.json`
- 任务在新会话中自动恢复
- 推送方向建议不超过 2 个关键词，否则搜索结果不聚焦
