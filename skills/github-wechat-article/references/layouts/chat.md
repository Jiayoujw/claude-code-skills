# LAYOUT_CHAT — 聊天式布局（配对 COMPANION）

**核心原则：** 像跟朋友微信聊天安利一个小工具。轻松、有趣、个人化。emoji 当视觉锚点，段落节奏像聊天记录一样跳跃。

## 签名视觉时刻（Hero Moment）

**「第一印象反应卡」**：封面图下方，用一个 emoji 大图 + 个人化评价 blockquote 打开。像一个朋友甩来一张截图然后说"你看这个！"。不同于正式数据卡，这里用 3 列 emoji（28px）+ 轻量标签的方式展示关键信息。

**「emoji 功能子弹」**：功能展示不用正式卡片，用 p 段落 + emoji 前缀 + `<strong>` 高亮，就像聊天记录里朋友一条一条地列"这玩意儿最牛的是……"

## 段落顺序

```
h1 标题
├─ p 开篇钩子（个人小故事——"我有一个困扰了很久的问题……"）
├─ p 封面图（故事结束后，自然出现——"直到我发现了它"）
├─ blockquote 「第一印象块」（个人口吻评价）
├─ table 「第一印象反应卡」（3 列 emoji + 轻量标签）
├─ h2 "它是个什么东西？简单说"
├─ p 一句话介绍
├─ h2 "亮点一览：最实用的 N 个功能"
├─ p ✨ 功能 1（段落 + strong，不用卡片）
├─ p ✨ 功能 2
├─ p ✨ 功能 3
├─ h2 "装好后是什么体验？"
├─ p 个人使用感受（"自从装上之后，我每天的流程变成了这样……"）
├─ pre 安装命令（简单的一行命令）
├─ hr 分割线
├─ table 转发金句模块
├─ table CTA：趣味安利投票
└─ p 点赞引导
```

## 格式规范

- **数据卡格式（第一印象反应卡）**：3 列 emoji（28px）+ 轻量标签（13px），绿色底 `#ecfdf5`
- **功能展示**：p 段落 + emoji + `<strong>`，不用 table 卡片
- **封面位置**：个人故事之后
- **间距密/疏**：轻快跳跃 —— 段落间距 12-18px 不等，行高 1.75
- **分割线**：极简 `border-top:1px solid #d1d5db; margin:24px 0`
- **h2 装饰**：`border-left:3px solid #059669; padding-left:10px`（3px 细线，轻量）
- **炫酷元素**：「第一印象反应卡」emoji 大图 + 像聊天记录的功能子弹列表

---

## 完整 HTML 模板

```html
<h1 style="font-size:24px;color:#1a1a1a;text-align:center;margin:0 0 20px;line-height:1.5;">{{文章标题}}</h1>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;">{{我有一个困扰了很久的问题……（个人小故事开头）}}</p>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;">{{直到我发现了 {{项目名}}……}}</p>
<p style="text-align:center;margin:16px 0;"><img src="{{BASE64_COVER}}" alt="" style="max-width:100%;"></p>

<!-- 【第一印象块】— 签名视觉：emoji 大图 + 个人评价 -->
<blockquote style="border-left:3px solid #059669;background:#ecfdf5;margin:18px 0;padding:12px 16px;">
  <p style="font-size:15px;color:#059669;font-weight:700;margin:0 0 6px;">我的第一印象 👇</p>
  <p style="font-size:14px;color:#333;line-height:1.8;margin:0;">"{{个人化评价，像跟朋友说的一样……}}"</p>
</blockquote>

<!-- 【第一印象反应卡】— 签名视觉：大号 emoji + 轻量标签 -->
<table width="100%" cellpadding="10" cellspacing="0" border="0" style="background:#ecfdf5;margin:16px 0;text-align:center;">
  <tr>
    <td style="padding:10px 8px;">
      <p style="font-size:28px;margin:0;">😍</p>
      <p style="font-size:13px;color:#666;margin:6px 0 0;">{{STARS}} Stars</p>
    </td>
    <td style="padding:10px 8px;">
      <p style="font-size:28px;margin:0;">⭐</p>
      <p style="font-size:13px;color:#666;margin:6px 0 0;">{{LICENSE}} 开源</p>
    </td>
    <td style="padding:10px 8px;">
      <p style="font-size:28px;margin:0;">🎯</p>
      <p style="font-size:13px;color:#666;margin:6px 0 0;">{{LANGUAGE}} / {{平台}}</p>
    </td>
  </tr>
</table>

<h2 style="font-size:19px;color:#1a1a1a;margin:22px 0 14px;border-left:3px solid #059669;padding-left:10px;">它是个什么东西？简单说</h2>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;">{{一句话轻松介绍……截至 {{YEAR}}.{{MONTH}}，Star {{STARS}}}}</p>

<h2 style="font-size:19px;color:#1a1a1a;margin:22px 0 14px;border-left:3px solid #059669;padding-left:10px;">亮点一览：最实用的 {{N}} 个功能</h2>

<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;"><strong style="color:#059669;">✨ {{功能 1 名}}：</strong>{{简短说明。用了之后你会发现……}}</p>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;"><strong style="color:#059669;">✨ {{功能 2 名}}：</strong>{{简短说明。特别适合……}}</p>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;"><strong style="color:#059669;">✨ {{功能 3 名}}：</strong>{{简短说明。最让我惊喜的是……}}</p>

<h2 style="font-size:19px;color:#1a1a1a;margin:22px 0 14px;border-left:3px solid #059669;padding-left:10px;">装好后是什么体验？</h2>
<p style="font-size:15px;color:#333;line-height:1.75;margin:0 0 14px;">{{个人使用感受，像聊天一样说……"自从装上之后，我每天的流程变成了这样"}}</p>
<p style="font-size:13px;color:#999;line-height:1.75;margin:0 0 10px;">⚠️ {{使用限制或小吐槽}}</p>

<pre style="background:#f5f5f5;color:#333;border-left:3px solid #059669;padding:12px;font-size:14px;line-height:1.6;"><code>{{安装命令，尽量 1 行}}</code></pre>

<hr style="border:0;border-top:1px solid #d1d5db;margin:24px 0;">

<!-- 转发金句模块 -->
<table width="100%" cellpadding="16" cellspacing="0" border="0" style="background:#ecfdf5;margin:20px 0;text-align:center;">
  <tr><td>
    <p style="font-size:16px;color:#059669;font-weight:700;line-height:1.8;margin:0;">"{{转发金句，30 字以内}}"</p>
    <p style="font-size:12px;color:#999;margin:8px 0 0;">—— 长按选中复制，转发给用得上的朋友</p>
  </td></tr>
</table>

<!-- CTA 趣味安利投票 -->
<table width="100%" cellpadding="14" cellspacing="0" border="0" style="background:#f0fdf4;text-align:center;">
  <tr><td>
    <p style="font-size:16px;font-weight:600;color:#059669;margin:0 0 12px;">{{CTA 投票问题}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">A. {{选项 A}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">B. {{选项 B}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">C. {{选项 C}}</p>
  </td></tr>
</table>

<p style="font-size:13px;color:#999;text-align:center;margin:16px 0 0;">🧡 欢迎<strong style="color:#059669;">点赞、收藏、转发</strong>给同样爱折腾的朋友～</p>
<p style="font-size:13px;color:#999;text-align:center;margin:8px 0 0;">关注「{{公众号名称}}」，发现更多让生活变好的小工具。</p>
```
