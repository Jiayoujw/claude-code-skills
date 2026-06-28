# LAYOUT_MANIFESTO — 宣言式布局（配对 FUTURIST）

**核心原则：** 像一份未来宣言，用视觉冲击制造震撼。大图、大字、大数字。深蓝底色 + 戏剧化排版节奏。

## 签名视觉时刻（Hero Moment）

**「巨型宣言数字」**：封面图后紧跟一个全宽深蓝底卡片，居中展示一个 56px 的超大数字（Star 数或项目的关键指标），下方一行白字描述。像电影海报的标题，读者滑到这里会猛然停住。

**「认知颠覆对比卡」**：功能展示用双色双栏对比表——左列灰色 "以前我们以为……"，右列深蓝底白字 "[项目名] 告诉我们……"。每张对比卡都是一次世界观冲击。

## 段落顺序

```
h1 标题
├─ p 封面图（文章最前面——"先看这张图"）
├─ p 开篇钩子（直接制造认知冲击）
├─ table 「巨型宣言数字」（深蓝底，56px 大数字）
├─ h2 "它是什么？不是工具，是世界观"
├─ p 项目本质描述
├─ h2 "拆解：重新定义 [领域] 的 N 个维度"
├─ table 维度 1：认知颠覆对比卡
├─ table 维度 2：认知颠覆对比卡
├─ table 维度 3：认知颠覆对比卡
├─ hr 粗实线分割
├─ h2 "这意味着什么？"
├─ blockquote 引用行业大牛或媒体评论
├─ p 展望未来（像一段迷你科幻）
├─ hr 粗实线分割
├─ table 转发金句模块
├─ table CTA：预测式投票
└─ p 点赞引导
```

## 格式规范

- **数据卡格式（巨型宣言数字）**：深蓝底全宽，居中 56px 白字 + 14px 灰白说明
- **功能展示（认知颠覆对比卡）**：左灰右蓝 2 列，左 "以前我们以为" + 右 "[项目名] 告诉我们"
- **封面位置**：文章最前面
- **间距密/疏**：戏剧化反差 —— 段落间 14-28px 不等，行高 1.7
- **分割线**：粗实线 2px `border-top:2px solid #1e1b4b; margin:32px 0`
- **h2 装饰**：全宽浅蓝背景条 + 居中文字 `background:#e0e7ff; text-align:center; padding:8px 0`，字号 18px，`font-weight:700`
- **炫酷元素**：56px 巨型数字 + 深蓝底卡片 + 认知颠覆对比卡

---

## 完整 HTML 模板

```html
<h1 style="font-size:24px;color:#1a1a1a;text-align:center;margin:0 0 20px;line-height:1.5;">{{文章标题}}</h1>
<p style="text-align:center;margin:0 0 16px;"><img src="{{BASE64_COVER}}" alt="" style="max-width:100%;"></p>
<p style="font-size:15px;color:#333;line-height:1.7;margin:0 0 14px;">{{开篇钩子——制造认知冲击……}}</p>
<p style="font-size:15px;color:#333;line-height:1.7;margin:0 0 14px;">{{钩子收束句——引出项目……}}</p>

<!-- 【巨型宣言数字】— 签名视觉：56px 大数字 + 深蓝底 -->
<table width="100%" cellpadding="28" cellspacing="0" border="0" style="background:#1e1b4b;margin:24px 0;text-align:center;">
  <tr><td>
    <p style="font-size:56px;font-weight:900;color:#ffffff;margin:0;line-height:1;">{{STARS}}</p>
    <p style="font-size:15px;color:rgba(255,255,255,0.75);margin:12px 0 0;">GitHub Stars · {{项目领域}}的变革正在发生</p>
  </td></tr>
</table>

<h2 style="font-size:18px;color:#1e1b4b;text-align:center;margin:28px 0 16px;padding:8px 0;background:#e0e7ff;font-weight:700;">它是什么？不是工具，是世界观</h2>
<p style="font-size:15px;color:#333;line-height:1.7;margin:0 0 16px;">{{项目本质描述……截至 {{YEAR}} 年 {{MONTH}}，Star 数 {{STARS}}，{{LICENSE}} 协议。}}</p>

<h2 style="font-size:18px;color:#1e1b4b;text-align:center;margin:28px 0 16px;padding:8px 0;background:#e0e7ff;font-weight:700;">拆解：重新定义 {{领域}} 的 {{N}} 个维度</h2>

<!-- 【认知颠覆对比卡】— 签名视觉：左灰右蓝 -->
<table width="100%" cellpadding="10" cellspacing="0" border="0" style="margin:14px 0;">
  <tr>
    <td style="font-size:13px;color:#999;background:#f5f5f5;padding:10px 12px;">以前我们以为</td>
    <td style="font-size:13px;color:#e0e7ff;font-weight:700;background:#1e1b4b;padding:10px 12px;">{{项目名}} 告诉我们</td>
  </tr>
  <tr>
    <td style="font-size:14px;color:#555;background:#f5f5f5;padding:10px 12px;">{{传统认知……}}</td>
    <td style="font-size:14px;color:#cbd5e1;background:#1e1b4b;padding:10px 12px;">{{项目的突破……}}</td>
  </tr>
</table>

<table width="100%" cellpadding="10" cellspacing="0" border="0" style="margin:14px 0;">
  <tr>
    <td style="font-size:13px;color:#999;background:#f5f5f5;padding:10px 12px;">以前我们以为</td>
    <td style="font-size:13px;color:#e0e7ff;font-weight:700;background:#1e1b4b;padding:10px 12px;">{{项目名}} 告诉我们</td>
  </tr>
  <tr>
    <td style="font-size:14px;color:#555;background:#f5f5f5;padding:10px 12px;">{{传统认知……}}</td>
    <td style="font-size:14px;color:#cbd5e1;background:#1e1b4b;padding:10px 12px;">{{项目的突破……}}</td>
  </tr>
</table>

<table width="100%" cellpadding="10" cellspacing="0" border="0" style="margin:14px 0;">
  <tr>
    <td style="font-size:13px;color:#999;background:#f5f5f5;padding:10px 12px;">以前我们以为</td>
    <td style="font-size:13px;color:#e0e7ff;font-weight:700;background:#1e1b4b;padding:10px 12px;">{{项目名}} 告诉我们</td>
  </tr>
  <tr>
    <td style="font-size:14px;color:#555;background:#f5f5f5;padding:10px 12px;">{{传统认知……}}</td>
    <td style="font-size:14px;color:#cbd5e1;background:#1e1b4b;padding:10px 12px;">{{项目的突破……}}</td>
  </tr>
</table>

<hr style="border:0;border-top:2px solid #1e1b4b;margin:32px 0;">

<h2 style="font-size:18px;color:#1e1b4b;text-align:center;margin:28px 0 16px;padding:8px 0;background:#e0e7ff;font-weight:700;">这意味着什么？</h2>

<blockquote style="border-left:4px solid #4338ca;background:#eef2ff;margin:14px 0;padding:14px 18px;">
  <p style="font-size:14px;color:#4338ca;line-height:1.8;margin:0;">「{{引用行业大牛或媒体的评论}}」</p>
</blockquote>
<p style="font-size:15px;color:#333;line-height:1.7;margin:0 0 14px;">{{展望未来的描述，像一段迷你科幻……}}</p>
<p style="font-size:13px;color:#999;line-height:1.7;margin:0 0 14px;">⚠️ {{成熟度说明或使用限制}}</p>

<hr style="border:0;border-top:2px solid #1e1b4b;margin:32px 0;">

<!-- 转发金句模块 -->
<table width="100%" cellpadding="16" cellspacing="0" border="0" style="background:#e0e7ff;margin:20px 0;text-align:center;">
  <tr><td>
    <p style="font-size:16px;color:#1e1b4b;font-weight:700;line-height:1.8;margin:0;">"{{转发金句，30 字以内}}"</p>
    <p style="font-size:12px;color:#999;margin:8px 0 0;">—— 长按选中复制，转发给对未来好奇的朋友</p>
  </td></tr>
</table>

<!-- CTA 预测式投票 -->
<table width="100%" cellpadding="14" cellspacing="0" border="0" style="background:#eef2ff;text-align:center;">
  <tr><td>
    <p style="font-size:16px;font-weight:600;color:#1e1b4b;margin:0 0 12px;">{{CTA 投票问题}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">A. {{选项 A}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">B. {{选项 B}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">C. {{选项 C}}</p>
  </td></tr>
</table>

<p style="font-size:13px;color:#999;text-align:center;margin:20px 0 0;">🧡 欢迎<strong style="color:#4338ca;">点赞、收藏、转发</strong>给对未来好奇的朋友～</p>
<p style="font-size:13px;color:#999;text-align:center;margin:8px 0 0;">关注「{{公众号名称}}」，一起见证技术如何改变世界。</p>
```
