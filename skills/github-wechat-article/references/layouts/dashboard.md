# LAYOUT_DASHBOARD — 仪表盘式布局（配对 PRAGMATIC）

**核心原则：** 像打开一个监控仪表盘，一眼看到关键数字。紧凑、高效率、零废话。红色主题制造紧迫感和行动号召。

## 签名视觉时刻（Hero Moment）

**「2×2 巨型数据网格」**：封面图后紧跟一个 2×2 数据网格，每个 cell 超大数字 + 标签，字号 26-30px。四组数字并排冲击，读者 1 秒判断"这个项目牛不牛"。

**「前后对比撕裂卡」**：功能展示用双色对比表——上半 grey 底色 "❌ 没有它时"，下半彩色底色 "✅ 有了 [项目名]"。色彩撕裂缝营造戏剧化反差。

## 段落顺序

```
h1 标题
├─ p 开篇钩子（痛点场景，1-2 段）
├─ p 封面图（痛点铺垫后、方案揭晓前）
├─ table 2×2 巨型数据网格（Star / 协议 / 语言 / 关键指标）
├─ p 一句话总结（1 段，不超过 50 字）
├─ h2 "硬核拆解：为什么它这么强？"
├─ table 功能 1：前后对比撕裂卡
├─ table 功能 2：前后对比撕裂卡
├─ table 功能 3：前后对比撕裂卡
├─ h2 "上手门槛？实测给你看"
├─ blockquote 实测数据引用块
├─ pre 安装命令（深色终端风，必须有）
├─ h2 "这个工具适合你吗？"
├─ table ✅/⚠ 二分清单
├─ hr 红色分割线
├─ table 转发金句模块
├─ table CTA：工具对比投票
└─ p 点赞引导
```

## 格式规范

- **数据卡格式**：2×2 网格，每个 cell 大数字（26-30px）+ 小标签（12px），红色底色 `#fef2f2`
- **功能展示**：前后对比撕裂卡——上半 grey 底 ❌ + 下半彩色底 ✅，深色字对比
- **适合谁用**：二分清单 table，✅ 绿色 check + ⚠ 灰色 warning
- **封面位置**：痛点铺垫后、方案揭晓前
- **间距密/疏**：极紧凑 —— h2 margin 20px/10px，段间距 10px，行高 1.6
- **分割线**：红色细线 `border-top:1px solid #fecaca; margin:24px 0`
- **h2 装饰**：`border-left:4px solid #dc2626; padding-left:12px`（粗红线，有力）
- **炫酷元素**：2×2 巨型数据网格 + 前后对比撕裂卡

---

## 完整 HTML 模板

```html
<h1 style="font-size:24px;color:#1a1a1a;text-align:center;margin:0 0 20px;line-height:1.5;">{{文章标题}}</h1>
<p style="font-size:15px;color:#333;line-height:1.6;margin:0 0 10px;">{{痛点钩子第一段……}}</p>
<p style="font-size:15px;color:#333;line-height:1.6;margin:0 0 10px;">{{痛点钩子第二段，引出项目……}}</p>
<p style="text-align:center;margin:14px 0;"><img src="{{BASE64_COVER}}" alt="" style="max-width:100%;"></p>

<!-- 【2×2 巨型数据网格】— 签名视觉：大数字冲击 -->
<table width="100%" cellpadding="14" cellspacing="0" border="0" style="background:#fef2f2;margin:16px 0;">
  <tr style="text-align:center;">
    <td style="padding:16px 8px;">
      <p style="font-size:28px;font-weight:800;color:#dc2626;margin:0;">{{STARS}}</p>
      <p style="font-size:12px;color:#999;margin:6px 0 0;">⭐ GitHub Stars</p>
    </td>
    <td style="padding:16px 8px;">
      <p style="font-size:28px;font-weight:800;color:#059669;margin:0;">{{LICENSE}}</p>
      <p style="font-size:12px;color:#999;margin:6px 0 0;">📝 开源协议</p>
    </td>
  </tr>
  <tr style="text-align:center;">
    <td style="padding:16px 8px;">
      <p style="font-size:28px;font-weight:800;color:#333;margin:0;">{{LANGUAGE}}</p>
      <p style="font-size:12px;color:#999;margin:6px 0 0;">🔧 开发语言</p>
    </td>
    <td style="padding:16px 8px;">
      <p style="font-size:28px;font-weight:800;color:#ea580c;margin:0;">{{关键指标}}</p>
      <p style="font-size:12px;color:#999;margin:6px 0 0;">⚡ 核心性能</p>
    </td>
  </tr>
</table>

<p style="font-size:15px;color:#333;line-height:1.6;margin:0 0 12px;"><strong style="color:#dc2626;">一句话：</strong>{{项目一句话总结，不超过 50 字}}</p>

<h2 style="font-size:19px;color:#1a1a1a;margin:20px 0 10px;border-left:4px solid #dc2626;padding-left:12px;">硬核拆解：为什么它这么强？</h2>

<!-- 【前后对比撕裂卡】— 签名视觉：色彩撕裂制造反差 -->
<table width="100%" cellpadding="10" cellspacing="0" border="0" style="margin:12px 0;">
  <tr><td style="font-size:13px;color:#999;background:#f5f5f5;padding:8px 12px;">❌ 没有它时</td></tr>
  <tr><td style="font-size:14px;color:#555;background:#f5f5f5;padding:8px 12px;">{{旧方案的痛点描述……}}</td></tr>
  <tr><td style="font-size:13px;color:#dc2626;font-weight:700;background:#fef2f2;padding:8px 12px;">✅ 有了 {{项目名}}</td></tr>
  <tr><td style="font-size:14px;color:#333;background:#fef2f2;padding:8px 12px;">{{新方案的改善描述……}}</td></tr>
</table>

<table width="100%" cellpadding="10" cellspacing="0" border="0" style="margin:12px 0;">
  <tr><td style="font-size:13px;color:#999;background:#f5f5f5;padding:8px 12px;">❌ 没有它时</td></tr>
  <tr><td style="font-size:14px;color:#555;background:#f5f5f5;padding:8px 12px;">{{功能 2 旧痛点……}}</td></tr>
  <tr><td style="font-size:13px;color:#dc2626;font-weight:700;background:#fef2f2;padding:8px 12px;">✅ 有了 {{项目名}}</td></tr>
  <tr><td style="font-size:14px;color:#333;background:#fef2f2;padding:8px 12px;">{{功能 2 新改善……}}</td></tr>
</table>

<table width="100%" cellpadding="10" cellspacing="0" border="0" style="margin:12px 0;">
  <tr><td style="font-size:13px;color:#999;background:#f5f5f5;padding:8px 12px;">❌ 没有它时</td></tr>
  <tr><td style="font-size:14px;color:#555;background:#f5f5f5;padding:8px 12px;">{{功能 3 旧痛点……}}</td></tr>
  <tr><td style="font-size:13px;color:#dc2626;font-weight:700;background:#fef2f2;padding:8px 12px;">✅ 有了 {{项目名}}</td></tr>
  <tr><td style="font-size:14px;color:#333;background:#fef2f2;padding:8px 12px;">{{功能 3 新改善……}}</td></tr>
</table>

<h2 style="font-size:19px;color:#1a1a1a;margin:20px 0 10px;border-left:4px solid #dc2626;padding-left:12px;">上手门槛？实测给你看</h2>

<blockquote style="border-left:4px solid #dc2626;background:#fff7ed;margin:12px 0;padding:12px 16px;">
  <p style="font-size:15px;color:#ea580c;font-weight:700;margin:0 0 6px;">⚡ 实测结论</p>
  <p style="font-size:14px;color:#333;line-height:1.7;margin:0;">{{实测数据或真实用户反馈……}}</p>
</blockquote>

<pre style="background:#1e1b4b;color:#e2e8f0;padding:14px;font-size:14px;line-height:1.7;"><code>{{安装命令，1-3 行}}</code></pre>
<p style="font-size:13px;color:#999;margin:4px 0 10px;">⚠️ {{使用限制说明}}</p>

<h2 style="font-size:19px;color:#1a1a1a;margin:20px 0 10px;border-left:4px solid #dc2626;padding-left:12px;">这个工具适合你吗？</h2>

<table width="100%" cellpadding="10" cellspacing="0" border="0" style="background:#fef2f2;margin:12px 0;">
  <tr><td style="font-size:14px;color:#333;padding:8px 12px;">✅ 适合 {{场景 A}} 的 {{角色}}</td></tr>
  <tr><td style="font-size:14px;color:#333;padding:8px 12px;">✅ 想要 {{效果}} 但不想 {{麻烦}} 的人</td></tr>
  <tr><td style="font-size:14px;color:#999;padding:8px 12px;">⚠ {{不适用场景}}，这个工具不太合适</td></tr>
</table>

<hr style="border:0;border-top:1px solid #fecaca;margin:24px 0;">

<!-- 转发金句模块 -->
<table width="100%" cellpadding="16" cellspacing="0" border="0" style="background:#fef2f2;margin:20px 0;text-align:center;">
  <tr><td>
    <p style="font-size:16px;color:#dc2626;font-weight:700;line-height:1.8;margin:0;">"{{转发金句，30 字以内}}"</p>
    <p style="font-size:12px;color:#999;margin:8px 0 0;">—— 长按选中复制，转发给用得上的朋友</p>
  </td></tr>
</table>

<!-- CTA 工具对比投票 -->
<table width="100%" cellpadding="14" cellspacing="0" border="0" style="background:#fff7ed;text-align:center;">
  <tr><td>
    <p style="font-size:16px;font-weight:600;color:#dc2626;margin:0 0 12px;">{{CTA 投票问题}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">A. {{选项 A}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">B. {{选项 B}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">C. {{选项 C}}</p>
  </td></tr>
</table>

<p style="font-size:13px;color:#999;text-align:center;margin:16px 0 0;">🧡 欢迎<strong style="color:#dc2626;">点赞、收藏、转发</strong>给同样在折腾的同行～</p>
<p style="font-size:13px;color:#999;text-align:center;margin:8px 0 0;">关注「{{公众号名称}}」，只推真正好用的开发工具。</p>
```
