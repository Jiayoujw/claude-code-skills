# LAYOUT_THESIS — 论文式布局（配对 SCHOLAR）

**核心原则：** 像读一篇严谨的论文，先建立信任再展示方案。视觉上强调"克制的高级感"——留白多、颜色克制、字号偏大。

## 签名视觉时刻（Hero Moment）

**「研究焦点块」**：在封面图下方，用一个深底白字的大号数字卡展示最关键数据（不是 Star 数，而是项目独特指标——如"本地处理 100% 数据""支持 47 种语言"），制造"这篇论文的核心发现"的第一印象。

## 段落顺序

```
h1 标题
├─ p 开篇钩子（2 段，制造认知冲突）
├─ p 封面图（在引子完成、读者产生好奇后出现——约第 3 段位置）
├─ table 「研究焦点块」（深底卡片，大号数字+说明，单行单列）
├─ h2 "为什么它值得你关注？"
├─ p 项目介绍（直接以段落叙述，融入数据；不使用独立数据卡片）
├─ table 「权威引用卡」（1 行 2 列：左列小字标签+右列加粗引用来源）
├─ h2 "核心技术深度拆解"
├─ blockquote 功能 1 标题块 → p 论据展开
├─ blockquote 功能 2 标题块 → p 论据展开
├─ blockquote 功能 3 标题块 → p 论据展开
├─ h2 "谁在用？效果如何？"
├─ p 适用场景叙述（不用 table 清单，用流畅段落）
├─ h2 "一分钟上手"
├─ p 安装说明 + 体验链接（如有在线 Demo 优先推荐）
├─ hr 分割线
├─ table 转发金句模块
├─ table CTA：开放式提问（无 ABC 选项，用段落式提问）
└─ p 点赞引导
```

## 格式规范

- **数据卡格式（研究焦点块）**：深底白字，单行单列，超大数字 + 说明文字
- **数据卡格式（权威引用卡）**：浅底 2 列，左列标签（⭐ Stars / 📝 协议 / 🔗 标准），右列加粗数值
- **功能展示**：blockquote 做子标题，p 展开论据
- **封面位置**：第 3 段位置（引子完成、问题充分铺垫后）
- **间距密/疏**：疏朗 —— h2 margin 30px/18px，段间距 18px，行高 1.9
- **分割线**：极细浅灰线 `border-top:1px solid #d1d5db; margin:32px 0`
- **h2 装饰**：无 border-left，纯文字 `font-weight:700`，字号 18px（比别的风格小 1px，体现学术克制）
- **炫酷元素**：「研究焦点块」深底白字大数字

---

## 完整 HTML 模板

```html
<h1 style="font-size:24px;color:#1a1a1a;text-align:center;margin:0 0 24px;line-height:1.5;">{{文章标题}}</h1>
<p style="font-size:16px;color:#333;line-height:1.9;margin:0 0 18px;">{{开篇钩子第一段……制造认知冲突}}</p>
<p style="font-size:16px;color:#333;line-height:1.9;margin:0 0 18px;">{{开篇钩子第二段……引出项目}}</p>
<p style="text-align:center;margin:20px 0;"><img src="{{BASE64_COVER}}" alt="" style="max-width:100%;"></p>

<!-- 【研究焦点块】— 签名视觉：深底 + 大号数字 -->
<table width="100%" cellpadding="24" cellspacing="0" border="0" style="background:#1e3a5f;margin:24px 0;text-align:center;">
  <tr><td>
    <p style="font-size:42px;font-weight:800;color:#ffffff;margin:0;line-height:1.2;">{{核心数据，如"100% 本地处理"}}</p>
    <p style="font-size:14px;color:rgba(255,255,255,0.7);margin:10px 0 0;">{{一句话解释这个数字意味着什么}}</p>
  </td></tr>
</table>

<h2 style="font-size:18px;color:#1a1a1a;font-weight:700;margin:30px 0 18px;">为什么它值得你关注？</h2>
<p style="font-size:15px;color:#333;line-height:1.9;margin:0 0 18px;">{{项目介绍段落，融入 Star 数和许可证等关键数据……截至 {{YEAR}} 年 {{MONTH}} 月，Star 数 {{STARS}}……}}</p>

<!-- 【权威引用卡】— 结构化数据但保持学术克制 -->
<table width="100%" cellpadding="12" cellspacing="0" border="0" style="background:#f0f4ff;margin:20px 0;">
  <tr><td style="font-size:14px;color:#666;padding:8px 14px;width:80px;">⭐ Stars</td><td style="font-size:15px;color:#2563eb;font-weight:700;padding:8px 14px;">{{STARS}}（截至 {{YEAR}}.{{MONTH}}）</td></tr>
  <tr><td style="font-size:14px;color:#666;padding:8px 14px;">📝 协议</td><td style="font-size:15px;color:#059669;font-weight:600;padding:8px 14px;">{{LICENSE}}</td></tr>
  <tr><td style="font-size:14px;color:#666;padding:8px 14px;">🔗 语言</td><td style="font-size:15px;color:#333;font-weight:600;padding:8px 14px;">{{LANGUAGE}}</td></tr>
</table>

<h2 style="font-size:18px;color:#1a1a1a;font-weight:700;margin:30px 0 18px;">核心技术深度拆解</h2>

<blockquote style="border-left:3px solid #2563eb;background:#f8fafc;margin:20px 0 8px;padding:10px 16px;">
  <p style="font-size:14px;color:#2563eb;font-weight:700;margin:0;">🔬 {{功能 1 标题}}</p>
</blockquote>
<p style="font-size:15px;color:#333;line-height:1.9;margin:0 0 18px;">{{功能 1 论据展开，论点-论据式}}</p>

<blockquote style="border-left:3px solid #2563eb;background:#f8fafc;margin:20px 0 8px;padding:10px 16px;">
  <p style="font-size:14px;color:#2563eb;font-weight:700;margin:0;">🔬 {{功能 2 标题}}</p>
</blockquote>
<p style="font-size:15px;color:#333;line-height:1.9;margin:0 0 18px;">{{功能 2 论据展开}}</p>

<blockquote style="border-left:3px solid #2563eb;background:#f8fafc;margin:20px 0 8px;padding:10px 16px;">
  <p style="font-size:14px;color:#2563eb;font-weight:700;margin:0;">🔬 {{功能 3 标题}}</p>
</blockquote>
<p style="font-size:15px;color:#333;line-height:1.9;margin:0 0 18px;">{{功能 3 论据展开}}</p>

<h2 style="font-size:18px;color:#1a1a1a;font-weight:700;margin:30px 0 18px;">谁在用？效果如何？</h2>
<p style="font-size:15px;color:#333;line-height:1.9;margin:0 0 18px;">{{适用场景叙述（段落形式，不用表格清单）}}……如果你属于以上任何一类，这个项目值得你花 10 分钟了解。</p>
<p style="font-size:14px;color:#999;line-height:1.8;margin:0 0 18px;">⚠️ {{使用限制说明（至少 1 条）}}</p>

<h2 style="font-size:18px;color:#1a1a1a;font-weight:700;margin:30px 0 18px;">一分钟上手</h2>
<p style="font-size:15px;color:#333;line-height:1.9;margin:0 0 18px;">{{最快的试用方式……推荐在线体验链接，其次为安装命令说明（用段落文字描述而非代码块）}}</p>

<hr style="border:0;border-top:1px solid #d1d5db;margin:32px 0;">

<!-- 转发金句模块 -->
<table width="100%" cellpadding="16" cellspacing="0" border="0" style="background:#f0f4ff;margin:20px 0;text-align:center;">
  <tr><td>
    <p style="font-size:16px;color:#2563eb;font-weight:700;line-height:1.8;margin:0;">"{{转发金句，30 字以内，独立观点}}"</p>
    <p style="font-size:12px;color:#999;margin:8px 0 0;">—— 长按选中复制，转发给用得上的朋友</p>
  </td></tr>
</table>

<!-- CTA 开放式提问（无 ABC 选项） -->
<table width="100%" cellpadding="14" cellspacing="0" border="0" style="background:#f8fafc;margin:20px 0;text-align:center;">
  <tr><td>
    <p style="font-size:15px;color:#2563eb;font-weight:600;margin:0 0 8px;">{{CTA 开放式提问}}</p>
    <p style="font-size:13px;color:#999;margin:0;">{{引导语，如"评论区聊聊你的使用体验～"}}</p>
  </td></tr>
</table>

<p style="font-size:13px;color:#999;text-align:center;margin:20px 0 0;">🧡 欢迎<strong style="color:#2563eb;">点赞、收藏、转发</strong>给需要的朋友～</p>
<p style="font-size:13px;color:#999;text-align:center;margin:8px 0 0;">关注「{{公众号名称}}」，深度拆解更多值得关注的开源工具。</p>
```
