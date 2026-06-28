# LAYOUT_MAP — 地图式布局（配对 EXPLORER）

**核心原则：** 像探险家展开一张地图，每次往下翻都有新发现。节奏跳跃、信息点密集、色彩丰富。

## 签名视觉时刻（Hero Moment）

**「探险标签云」**：封面图后紧跟一个 3 列 emoji 标签云 table，每个 cell 用大号 emoji + 彩色标题 + 一行描述，像地图上的兴趣点标记。这组标签云让读者 1 秒感知"这个工具能覆盖多少领域"。

## 段落顺序

```
h1 标题
├─ p 封面图（文章最前面——视觉冲击优先）
├─ p 开篇钩子（1 段短段落，制造好奇）
├─ table 「探险标签云」（3 列 emoji 兴趣点标记）
├─ h2 "它能搜什么？"
├─ p 一句话总结搜索范围
├─ h2 "发现了什么？拆开看这 N 个维度"
├─ blockquote "🔍 维度 1" → p 发现内容
├─ blockquote "🔍 维度 2" → p 发现内容
├─ blockquote "🔍 维度 3" → p 发现内容
├─ hr 虚线分割
├─ h2 "搜索背后的秘密"
├─ p 技术亮点
├─ pre 安装命令（画风像探索工具的命令行入口）
├─ hr 虚线分割
├─ table 转发金句模块
├─ table CTA：平台偏好投票
└─ p 点赞引导
```

## 格式规范

- **数据卡格式（探险标签云）**：3 列紧凑 table，每列：emoji（24px）+ 彩色标题（14px）+ 一行说明（12px）
- **功能展示**：blockquote 标记 "🔍 搜索维度" 作为探索日志条目，后面跟 p 展开
- **封面位置**：文章最前面（第 1 个视觉元素）
- **间距密/疏**：紧凑跳跃 —— h2 margin 20px/12px，段间距 12px，行高 1.7
- **分割线**：青色虚线 `border-top:1px dashed #0891b2; margin:24px 0`
- **h2 装饰**：`border-left:4px solid #0891b2; padding-left:12px`
- **炫酷元素**：「探险标签云」emoji 兴趣点标记 + 虚线分割模拟地图路线

---

## 完整 HTML 模板

```html
<h1 style="font-size:24px;color:#1a1a1a;text-align:center;margin:0 0 20px;line-height:1.5;">{{文章标题}}</h1>
<p style="text-align:center;margin:0 0 16px;"><img src="{{BASE64_COVER}}" alt="" style="max-width:100%;"></p>
<p style="font-size:15px;color:#333;line-height:1.7;margin:0 0 14px;">{{开篇钩子段落……制造好奇心}}</p>

<!-- 【探险标签云】— 签名视觉：emoji + 彩色兴趣点 -->
<table width="100%" cellpadding="12" cellspacing="0" border="0" style="background:#ecfeff;margin:16px 0;text-align:center;">
  <tr>
    <td style="padding:12px 8px;">
      <p style="font-size:26px;margin:0;">📱</p>
      <p style="font-size:14px;color:#0891b2;font-weight:700;margin:6px 0 2px;">{{平台 1 名}}</p>
      <p style="font-size:12px;color:#666;margin:0;">{{一句话说明}}</p>
    </td>
    <td style="padding:12px 8px;">
      <p style="font-size:26px;margin:0;">💬</p>
      <p style="font-size:14px;color:#0891b2;font-weight:700;margin:6px 0 2px;">{{平台 2 名}}</p>
      <p style="font-size:12px;color:#666;margin:0;">{{一句话说明}}</p>
    </td>
    <td style="padding:12px 8px;">
      <p style="font-size:26px;margin:0;">📰</p>
      <p style="font-size:14px;color:#0891b2;font-weight:700;margin:6px 0 2px;">{{平台 3 名}}</p>
      <p style="font-size:12px;color:#666;margin:0;">{{一句话说明}}</p>
    </td>
  </tr>
</table>

<h2 style="font-size:19px;color:#1a1a1a;margin:20px 0 12px;border-left:4px solid #0891b2;padding-left:12px;">它能搜什么？</h2>
<p style="font-size:15px;color:#333;line-height:1.7;margin:0 0 12px;">{{一句话总结搜索范围……截至 {{YEAR}} 年 {{MONTH}}，Star 数 {{STARS}}，{{LICENSE}} 协议。}}</p>

<h2 style="font-size:19px;color:#1a1a1a;margin:20px 0 12px;border-left:4px solid #0891b2;padding-left:12px;">发现了什么？拆开看这 {{N}} 个维度</h2>

<blockquote style="border-left:3px solid #f59e0b;background:#f0fdfa;margin:12px 0 6px;padding:8px 14px;">
  <p style="font-size:14px;color:#0e7490;font-weight:700;margin:0;">🔍 维度 1：{{维度标题}}</p>
</blockquote>
<p style="font-size:15px;color:#333;line-height:1.7;margin:0 0 14px;">{{发现描述……}}</p>

<blockquote style="border-left:3px solid #f59e0b;background:#f0fdfa;margin:12px 0 6px;padding:8px 14px;">
  <p style="font-size:14px;color:#0e7490;font-weight:700;margin:0;">🔍 维度 2：{{维度标题}}</p>
</blockquote>
<p style="font-size:15px;color:#333;line-height:1.7;margin:0 0 14px;">{{发现描述……}}</p>

<blockquote style="border-left:3px solid #f59e0b;background:#f0fdfa;margin:12px 0 6px;padding:8px 14px;">
  <p style="font-size:14px;color:#0e7490;font-weight:700;margin:0;">🔍 维度 3：{{维度标题}}</p>
</blockquote>
<p style="font-size:15px;color:#333;line-height:1.7;margin:0 0 14px;">{{发现描述……}}</p>

<hr style="border:0;border-top:1px dashed #0891b2;margin:24px 0;">

<h2 style="font-size:19px;color:#1a1a1a;margin:20px 0 12px;border-left:4px solid #0891b2;padding-left:12px;">搜索背后的秘密</h2>
<p style="font-size:15px;color:#333;line-height:1.7;margin:0 0 14px;">{{技术亮点说明……比传统方案好在哪}}</p>
<p style="font-size:13px;color:#999;line-height:1.7;margin:0 0 10px;">⚠️ {{使用限制}}</p>

<pre style="background:#f5f5f5;color:#333;border-left:3px solid #0891b2;padding:12px;font-size:14px;line-height:1.6;"><code>{{安装命令，不超过 3 行}}</code></pre>

<hr style="border:0;border-top:1px dashed #0891b2;margin:24px 0;">

<!-- 转发金句模块 -->
<table width="100%" cellpadding="16" cellspacing="0" border="0" style="background:#ecfeff;margin:20px 0;text-align:center;">
  <tr><td>
    <p style="font-size:16px;color:#0891b2;font-weight:700;line-height:1.8;margin:0;">"{{转发金句，30 字以内}}"</p>
    <p style="font-size:12px;color:#999;margin:8px 0 0;">—— 长按选中复制，转发给用得上的朋友</p>
  </td></tr>
</table>

<!-- CTA 平台偏好投票 -->
<table width="100%" cellpadding="14" cellspacing="0" border="0" style="background:#f0fdfa;text-align:center;">
  <tr><td>
    <p style="font-size:16px;font-weight:600;color:#0e7490;margin:0 0 12px;">{{CTA 投票问题}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">A. {{选项 A}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">B. {{选项 B}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">C. {{选项 C}}</p>
  </td></tr>
</table>

<p style="font-size:13px;color:#999;text-align:center;margin:16px 0 0;">🧡 欢迎<strong style="color:#0891b2;">点赞、收藏、转发</strong>给同样爱探索的朋友～</p>
<p style="font-size:13px;color:#999;text-align:center;margin:8px 0 0;">关注「{{公众号名称}}」，每周发现 GitHub 上最有趣的开源项目。</p>
```
