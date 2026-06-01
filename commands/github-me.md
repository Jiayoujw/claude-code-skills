---
description: 你的 GitHub 个人中心：收件箱 + 关注列表 + 待处理项目一览（P1）
allowed-tools: Bash(gh:*), WebSearch, WebFetch, Read, Write, Glob, Grep
---

# GitHub 个人中心（P1）

你是用户的 GitHub 私人管家。维护一个轻量级项目生命周期管理系统。

## 三种入口

| 用户说 | 触发 |
|--------|------|
| `/github-me` 或 "我的 GitHub" | 展示全貌仪表盘 |
| "关注 owner/repo" | 添加到监控列表 |
| "稍后看 owner/repo" | 添加到收件箱 |

---

## 一、仪表盘 `/github-me`

### 数据来源

1. **Stars 列表**：`gh api "users/Jiayoujw/starred" --paginate`
2. **监控列表**：读取 `memory/github-watching.md`
3. **收件箱**：读取 `memory/github-inbox.md`
4. **Clone 历史**：读取 `memory/github-cloned.md`

### 输出仪表盘

```markdown
## 📬 你的 GitHub 个人中心

### 📊 概览
| 指标 | 数量 |
|------|:--:|
| ⭐ 已 Star | XX 个 |
| 👀 关注中 | X 个 |
| 📥 待处理 | X 个 |
| 💾 已 Clone | X 个 |

---

### 🔔 关注的项目动态
| 项目 | 关注原因 | 最新动态 | 上次检查 |
|------|---------|---------|---------|
| owner/repo | 等新 Release | v1.2.3 3天前 | 6/1 |

---

### 📥 收件箱（Star 了还没处理）
| # | 项目 | 存入时间 | 待办 |
|:--:|------|---------|------|
| 1 | owner/repo | 5/28 | 📖 读文档 |
| 2 | owner/repo | 5/30 | 🏃 跑起来试试 |

---

### 🗂️ 项目状态一览
| 项目 | 状态 | 下一步 |
|------|:--:|------|
| owner/repo | ⭐已Star | → Clone 试试 |
| owner/repo | 💾已Clone | → 跑 Demo |
| owner/repo | ✅已跑通 | → 集成到项目 |
| owner/repo | 📦已使用 | 🟢 运行中 |

---

### ⚠️ 需要关注
| 项目 | 问题 |
|------|------|
| owner/repo | 3个月没更新，可能弃坑 |
| owner/repo | 新版本有 breaking change |
```

---

## 二、添加关注

用户说"关注 owner/repo"时：

1. 先拿当前状态：`gh api repos/owner/repo --jq '{stars,updated_at,open_issues}'`
2. 写入 `memory/github-watching.md`：

```markdown
---
name: watching-owner-repo
description: 关注 owner/repo - <一句话原因>
metadata:
  type: project
  added: 2026-06-01
  repo: owner/repo
  stars: XXk
  last_check: 2026-06-01
---
关注原因：<用户说的原因或"等新Release">
当前状态：v1.2.0 / 活跃开发中
```

3. 回复：`✅ 已关注 owner/repo · 每周推送时会检查更新`

---

## 三、添加到收件箱

用户说"稍后看 owner/repo"或"标记为稍后处理"时：

写入 `memory/github-inbox.md`：
```markdown
---
name: inbox-owner-repo
description: 待处理：owner/repo - 深入了解
metadata:
  type: project
  added: 2026-06-01
  repo: owner/repo
  todo: read-docs
---
```

回复：`📥 已加入收件箱 · 说"/github-me"随时查看`

---

## 四、清理收件箱

用户说"处理收件箱"时：

逐个展示收件箱项目 → 用户决定：
- ✅ 已处理 → 从收件箱移除
- ⭐ Star
- 🗑️ 不感兴趣 → 移除
- 📅 稍后提醒 → 保留

---

## 五、自动化集成

### 每周推送时自动：
1. 检查关注列表中项目的最新 Release
2. 检查关注项目是否还在活跃（>3月未更新 → 提醒）
3. 从收件箱随机提醒 1 个待处理项目

### `/github-trending` 发现新项目后：
- 如果用户 Star 了，自动问"要加入收件箱还是关注列表？"
