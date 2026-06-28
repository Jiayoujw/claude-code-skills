# LAYOUT_BLUEPRINT — 蓝图式布局（配对 ARCHITECT）

**核心原则：** 像读一份建筑设计图，结构清晰、层级分明、每一个模块都有明确位置。冷峻、专业、标准定义。

## 签名视觉时刻（Hero Moment）

**「规格说明书卡」**：封面图下方用一个深灰底 `#0f172a` 的规格表，3 行 label:value 格式（Stars / 协议 / 标准），白字 + 亮蓝色强调数字。像翻阅一份技术标准文档的第一页。

**「分层架构卡」**：功能展示用 3 层菱形标记 `🔷` 的 table，每层一个 table cell（深底标题行 + 浅底说明行），模拟系统架构图的层次感——基础层 → 中间层 → 接口层，从下到上的视觉递进。

## 段落顺序

```
h1 标题
├─ p 开篇钩子（问题场景——理性观察，不用戏剧化）
├─ p 问题收束——"这件事之前没有统一方案，直到 [项目名]"
├─ p 封面图（问题陈述后——"这就是它的架构全貌"）
├─ table 「规格说明书卡」（深灰底，3 行 label:value）
├─ h2 "它解决的问题是什么？"
├─ p 问题详细说明
├─ h2 "架构拆解：关键设计"
├─ table 基础层：🔷 标题行 + 说明行
├─ table 中间层：🔷 标题行 + 说明行
├─ table 接口层：🔷 标题行 + 说明行
├─ h2 "谁在用它？生态如何？"
├─ table 决策矩阵（3 列：角色 / 需求 / 匹配度）
├─ p 生态说明
├─ h2 "怎么接入？"
├─ pre 安装命令（深色代码块 `#0f172a`）
├─ hr 灰色分割线
├─ table 转发金句模块
├─ table CTA：技术栈偏好投票
└─ p 点赞引导
```

## 格式规范

- **数据卡格式（规格说明书卡）**：深灰底 `#0f172a`，3 行左 label + 右 value，白字 + 亮蓝 `#0284c7` 强调
- **功能展示（分层架构卡）**：每层独立 table，深底 `🔷` 标题行 + 浅底说明行
- **适合谁用（决策矩阵）**：3 列 table（角色/需求/匹配度⭐⭐⭐⭐⭐）
- **封面位置**：问题陈述之后
- **间距密/疏**：精准一致 —— h2 margin 24px/14px，段间距 14px，行高 1.75
- **分割线**：灰色 1px `border-top:1px solid #cbd5e1; margin:28px 0`
- **h2 装饰**：`border-left:4px solid #0f172a; padding-left:14px`
- **代码块**：最深底色 `#0f172a`，体现底层基础设施感
- **炫酷元素**：深灰底规格卡 + 分层架构卡 + 决策矩阵⭐⭐⭐⭐⭐

---

## 完整 HTML 模板

```html
<h1 style="font-size:24px;color:#1a1a1a;text-align:center;margin:0 0 24px;line-height:1.5;">{{文章标题}}</h1>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;">{{问题场景钩子——理性观察，不用戏剧化}}</p>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;">{{问题收束——"之前没有统一方案，直到 {{项目名}}"}}</p>
<p style="text-align:center;margin:18px 0;"><img src="{{BASE64_COVER}}" alt="" style="max-width:100%;"></p>

<!-- 【规格说明书卡】— 签名视觉：深灰底 + label:value -->
<table width="100%" cellpadding="12" cellspacing="0" border="0" style="background:#0f172a;margin:20px 0;">
  <tr>
    <td style="font-size:13px;color:rgba(255,255,255,0.6);padding:8px 14px;width:80px;">⭐ Stars</td>
    <td style="font-size:15px;color:#ffffff;font-weight:700;padding:8px 14px;">{{STARS}}（截至 {{YEAR}}.{{MONTH}}）</td>
  </tr>
  <tr>
    <td style="font-size:13px;color:rgba(255,255,255,0.6);padding:8px 14px;">📝 协议</td>
    <td style="font-size:15px;color:#0284c7;font-weight:600;padding:8px 14px;">{{LICENSE}}</td>
  </tr>
  <tr>
    <td style="font-size:13px;color:rgba(255,255,255,0.6);padding:8px 14px;">🔗 标准</td>
    <td style="font-size:15px;color:#06b6d4;font-weight:600;padding:8px 14px;">{{支持的协议/标准名称}}</td>
  </tr>
</table>

<h2 style="font-size:19px;color:#1a1a1a;margin:24px 0 14px;border-left:4px solid #0f172a;padding-left:14px;">它解决的问题是什么？</h2>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;">{{问题详细说明……}}</p>
<p style="font-size:14px;color:#999;line-height:1.75;margin:0 0 14px;">⚠️ {{当前局限性或适用范围说明}}</p>

<h2 style="font-size:19px;color:#1a1a1a;margin:24px 0 14px;border-left:4px solid #0f172a;padding-left:14px;">架构拆解：关键设计</h2>

<!-- 【分层架构卡】— 签名视觉：从基础层到接口层 -->
<table width="100%" cellpadding="10" cellspacing="0" border="0" style="margin:12px 0;">
  <tr><td style="font-size:15px;color:#ffffff;font-weight:700;background:#0f172a;padding:10px 14px;">🔷 基础层：{{基础层名称}}</td></tr>
  <tr><td style="font-size:14px;color:#555;background:#f1f5f9;padding:10px 14px;">{{详细说明……}}</td></tr>
</table>

<table width="100%" cellpadding="10" cellspacing="0" border="0" style="margin:12px 0;">
  <tr><td style="font-size:15px;color:#ffffff;font-weight:700;background:#1e293b;padding:10px 14px;">🔷 中间层：{{中间层名称}}</td></tr>
  <tr><td style="font-size:14px;color:#555;background:#f8fafc;padding:10px 14px;">{{详细说明……}}</td></tr>
</table>

<table width="100%" cellpadding="10" cellspacing="0" border="0" style="margin:12px 0;">
  <tr><td style="font-size:15px;color:#ffffff;font-weight:700;background:#334155;padding:10px 14px;">🔷 接口层：{{接口层名称}}</td></tr>
  <tr><td style="font-size:14px;color:#555;background:#f1f5f9;padding:10px 14px;">{{详细说明……}}</td></tr>
</table>

<h2 style="font-size:19px;color:#1a1a1a;margin:24px 0 14px;border-left:4px solid #0f172a;padding-left:14px;">谁在用它？生态如何？</h2>

<!-- 【决策矩阵】— 签字视觉：⭐⭐⭐⭐⭐ 匹配度 -->
<table width="100%" cellpadding="10" cellspacing="0" border="0" style="background:#f1f5f9;margin:14px 0;">
  <tr style="border-bottom:1px solid #cbd5e1;">
    <td style="font-size:14px;color:#666;font-weight:600;padding:8px 12px;">角色</td>
    <td style="font-size:14px;color:#666;font-weight:600;padding:8px 12px;">需求</td>
    <td style="font-size:14px;color:#0f172a;font-weight:600;padding:8px 12px;text-align:center;">匹配度</td>
  </tr>
  <tr>
    <td style="font-size:14px;color:#333;padding:8px 12px;">{{角色 1}}</td>
    <td style="font-size:14px;color:#555;padding:8px 12px;">{{需求 1}}</td>
    <td style="font-size:14px;color:#0f172a;font-weight:700;padding:8px 12px;text-align:center;">⭐⭐⭐⭐⭐</td>
  </tr>
  <tr>
    <td style="font-size:14px;color:#333;padding:8px 12px;">{{角色 2}}</td>
    <td style="font-size:14px;color:#555;padding:8px 12px;">{{需求 2}}</td>
    <td style="font-size:14px;color:#0f172a;font-weight:700;padding:8px 12px;text-align:center;">⭐⭐⭐⭐</td>
  </tr>
  <tr>
    <td style="font-size:14px;color:#333;padding:8px 12px;">{{角色 3}}</td>
    <td style="font-size:14px;color:#555;padding:8px 12px;">{{需求 3}}</td>
    <td style="font-size:14px;color:#999;padding:8px 12px;text-align:center;">⭐⭐⭐</td>
  </tr>
</table>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;">{{生态说明：哪些大厂/项目在采用……}}</p>

<h2 style="font-size:19px;color:#1a1a1a;margin:24px 0 14px;border-left:4px solid #0f172a;padding-left:14px;">怎么接入？</h2>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 10px;">{{接入说明……}}</p>

<pre style="background:#0f172a;color:#cbd5e1;padding:14px;font-size:14px;line-height:1.7;"><code>{{安装命令，1-3 行}}</code></pre>

<hr style="border:0;border-top:1px solid #cbd5e1;margin:28px 0;">

<!-- 转发金句模块 -->
<table width="100%" cellpadding="16" cellspacing="0" border="0" style="background:#f1f5f9;margin:20px 0;text-align:center;">
  <tr><td>
    <p style="font-size:16px;color:#0f172a;font-weight:700;line-height:1.8;margin:0;">"{{转发金句，30 字以内}}"</p>
    <p style="font-size:12px;color:#999;margin:8px 0 0;">—— 长按选中复制，转发给同样在搭架构的伙伴</p>
  </td></tr>
</table>

<!-- CTA 技术栈偏好投票 -->
<table width="100%" cellpadding="14" cellspacing="0" border="0" style="background:#f8fafc;text-align:center;">
  <tr><td>
    <p style="font-size:16px;font-weight:600;color:#0f172a;margin:0 0 12px;">{{CTA 投票问题}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">A. {{选项 A}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">B. {{选项 B}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">C. {{选项 C}}</p>
  </td></tr>
</table>

<p style="font-size:13px;color:#999;text-align:center;margin:20px 0 0;">🧡 欢迎<strong style="color:#0f172a;">点赞、收藏、转发</strong>给同样在搭架构的伙伴～</p>
<p style="font-size:13px;color:#999;text-align:center;margin:8px 0 0;">关注「{{公众号名称}}」，拆解更多 GitHub 上的技术基础设施。</p>
```
