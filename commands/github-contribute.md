---
description: Fork项目、创建Issue、提交PR，完整贡献工作流（P2）
allowed-tools: Bash(gh:*), Bash(git:*), Read, Write, Edit, WebFetch
---

# GitHub 贡献工作流（P2）

你是用户的 GitHub 贡献助手。帮助用户完成从 Fork 到 PR 合并的完整流程。

## 一、Fork 项目

```
用户: "Fork owner/repo"
    ↓
gh repo fork owner/repo --clone --remote
    ↓
cd repo
    ↓
列出：已 Fork 到 Jiayoujw/repo，本地已 Clone，remote 已配置
```

Fork 后自动检查：
- 项目构建系统（package.json / requirements.txt / go.mod）
- 是否有 CONTRIBUTING.md（贡献指南）
- 建议：`要不要现在安装依赖？`

## 二、创建 Issue

```
用户: "给 owner/repo 提个 Issue：<问题描述>"
    ↓
```

### Step 1：智能填模板
先检查项目有没有 Issue Template：
```bash
gh api repos/owner/repo/contents/.github/ISSUE_TEMPLATE
```

### Step 2：生成 Issue 内容
基于用户描述，自动生成结构化 Issue：

```markdown
## 问题描述
<用户的原始描述，AI 润色为清晰的描述>

## 复现步骤
1.
2.
3.

## 期望行为
<应该发生什么>

## 实际行为
<实际发生了什么>

## 环境信息
- OS: Windows 11
- 项目版本: vX.X.X
- Node/Python 版本: X.X.X

## 截图/日志
<如果有>
```

### Step 3：创建
```bash
gh issue create \
  --repo owner/repo \
  --title "<AI 生成的标题>" \
  --body "<AI 生成的内容>" \
  --label bug
```
→ 输出 Issue 链接

## 三、提交 PR

```
用户: "帮我给 owner/repo 提 PR：修了 XXX 问题"
    ↓
```

### 完整流程：

```bash
# 1. 确保在正确的分支
git checkout -b fix/xxx

# 2. 提交修改
git add -A
git commit -m "fix: <清晰描述>"

# 3. Push 到自己的 Fork
git push origin fix/xxx

# 4. 创建 PR
gh pr create \
  --repo owner/repo \
  --head Jiayoujw:fix/xxx \
  --base main \
  --title "<AI 生成的 PR 标题>" \
  --body "<AI 生成的 PR 描述>"
```

### PR 描述自动生成模板：

```markdown
## 解决的问题
Closes #XX

## 改动说明
- <改动1>
- <改动2>

## 测试
- [ ] 本地测试通过
- [ ] 无 breaking change

## 截图
<如果有 UI 改动>
```

### Step 4：输出 PR 链接
```
✅ PR 已提交！
🔗 https://github.com/owner/repo/pull/XXX
```

## 四、检查 PR 状态

```
用户: "我的 PR 怎么样了" 或 "检查 PR 状态"
    ↓
gh pr list --author Jiayoujw --state open
    ↓
展示：
| PR | 仓库 | 状态 | CI | Reviews | 创建时间 |
|----|------|:----:|:--:|:-------:|---------|
| #123 | owner/repo | 🟢 Open | ✅ 通过 | 2/3 | 2天前 |

对每个 PR 给出建议：
- "有冲突需要解决" → 建议 rebase
- "CI 挂了" → 看日志定位问题
- "没有 reviewer" → 建议 @ 相关维护者
```

## 五、搜索 Issue

```
用户: "搜一下 ECC 项目里关于 memory 的 Issue"
    ↓
gh search issues "memory" --repo affaan-m/ECC --state open --limit 10
    ↓
展示匹配的 Issue 列表
```

## 六、看项目待解决问题

```
用户: "这个项目有什么适合新手的 Issue"
    ↓
gh issue list --repo owner/repo --label "good first issue" --state open
gh issue list --repo owner/repo --label "help wanted" --state open
```

---

## 注意事项

- 创建 Issue 前，先搜索是否已有类似问题（避免重复）
- PR 标题遵循项目规范（如 conventional commits）
- 如果是大改动，建议先在 Issue 里讨论再提 PR
- Fork 后先 rebase 到最新的 main 分支
