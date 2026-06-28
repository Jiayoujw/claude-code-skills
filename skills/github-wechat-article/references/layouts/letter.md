# LAYOUT_LETTER — 书信式布局（配对 MENTOR）

**核心原则：** 像收到一封前辈的来信，娓娓道来一个真实的故事。温暖、真诚、故事驱动。

## 签名视觉时刻（Hero Moment）

**「故事时间线卡」**：封面图下方，用一个 3 行渐变色 table 展示作者的故事里程碑——"起点 → 转折 → 成果"。每行左边 emoji + 时间标签，右边事件描述。读者像看电影预告片一样快速了解故事背景。

## 段落顺序

```
h1 标题
├─ p 开篇钩子（作者故事第一段——"X 年前，他是……"）
├─ p 故事第二段——转折
├─ p 故事第三段——结局
├─ p 封面图（故事讲完后——"这就是他留下的宝藏"）
├─ table 「故事时间线卡」（3 行：起点 → 转折 → 成果）
├─ h2 "它的来历？一个真实的故事"
├─ p 补充作者背景 + 项目由来
├─ table 简约数据卡（3 行：Stars / 协议 / 语言，柔和紫色底）
├─ h2 "里面有什么？帮你省半年的精华"
├─ blockquote "📖 第一部分：[名称]" → p 内容描述
├─ blockquote "📖 第二部分：[名称]" → p 内容描述
├─ blockquote "📖 第三部分：[名称]" → p 内容描述
├─ hr 柔和虚线分割
├─ h2 "适合谁？不适合谁？"
├─ p 叙事体适用场景（"如果你也……" 不用表格）
├─ h2 "怎么开始？"
├─ p 最简单的入手方式
├─ pre 安装命令（如果有）
├─ hr 柔和虚线分割
├─ table 转发金句模块
├─ table CTA：阶段式投票
└─ p 点赞引导
```

## 格式规范

- **数据卡格式（故事时间线卡）**：3 行渐变色 table，每行左 emoji + 时间标签 + 右事件描述
- **数据卡格式（简约数据卡）**：3 行 label:value，柔和紫色底 `#f5f0ff`
- **功能展示**：blockquote 标记 "📖 第X部分"，像一本书的目录
- **封面位置**：故事讲完后（"这就是他留下的宝藏"）
- **间距密/疏**：温暖舒适 —— h2 margin 26px/16px，段间距 16px，行高 1.85
- **分割线**：柔和紫色虚线 `border-top:1px dashed #d8b4fe; margin:28px 0`
- **h2 装饰**：`border-left:3px solid #7c3aed; padding-left:14px`（3px 细线，比 PRAGMATIC 的 4px 柔和）
- **炫酷元素**：「故事时间线卡」渐变色行 + 书籍目录式 blockquote

---

## 完整 HTML 模板

```html
<h1 style="font-size:24px;color:#1a1a1a;text-align:center;margin:0 0 24px;line-height:1.5;">{{文章标题}}</h1>
<p style="font-size:15px;color:#333;line-height:1.85;margin:0 0 16px;">{{故事第一段……"X 年前，他只是……"}}</p>
<p style="font-size:15px;color:#333;line-height:1.85;margin:0 0 16px;">{{故事第二段——转折……}}</p>
<p style="font-size:15px;color:#333;line-height:1.85;margin:0 0 16px;">{{故事第三段——结局，引出项目……}}</p>
<p style="text-align:center;margin:20px 0;"><img src="{{BASE64_COVER}}" alt="" style="max-width:100%;"></p>

<!-- 【故事时间线卡】— 签名视觉：渐变色里程碑 -->
<table width="100%" cellpadding="14" cellspacing="0" border="0" style="margin:20px 0;">
  <tr>
    <td style="background:#f5f0ff;padding:12px 14px;font-size:15px;color:#7c3aed;font-weight:700;">
      🚀 起点
    </td>
    <td style="background:#f5f0ff;padding:12px 14px;font-size:14px;color:#555;">
      {{作者最初的状态/动机}}
    </td>
  </tr>
  <tr>
    <td style="background:#ede9fe;padding:12px 14px;font-size:15px;color:#7c3aed;font-weight:700;">
      💡 转折
    </td>
    <td style="background:#ede9fe;padding:12px 14px;font-size:14px;color:#555;">
      {{关键转折事件}}
    </td>
  </tr>
  <tr>
    <td style="background:#e4d4f6;padding:12px 14px;font-size:15px;color:#6d28d9;font-weight:700;">
      🏆 成果
    </td>
    <td style="background:#e4d4f6;padding:12px 14px;font-size:14px;color:#333;">
      <strong style="color:#7c3aed;">{{STARS}} Stars</strong> · {{最终成果描述}}
    </td>
  </tr>
</table>

<h2 style="font-size:19px;color:#1a1a1a;margin:26px 0 16px;border-left:3px solid #7c3aed;padding-left:14px;">它的来历？一个真实的故事</h2>
<p style="font-size:15px;color:#333;line-height:1.85;margin:0 0 16px;">{{补充作者背景和项目由来……截至 {{YEAR}}.{{MONTH}}}}</p>

<!-- 简约数据卡 -->
<table width="100%" cellpadding="10" cellspacing="0" border="0" style="background:#f5f0ff;margin:16px 0;">
  <tr><td style="font-size:14px;color:#999;padding:6px 12px;width:80px;">⭐ Stars</td><td style="font-size:15px;color:#7c3aed;font-weight:700;padding:6px 12px;">{{STARS}}（截至 {{YEAR}}.{{MONTH}}）</td></tr>
  <tr><td style="font-size:14px;color:#999;padding:6px 12px;">📝 协议</td><td style="font-size:15px;color:#059669;font-weight:600;padding:6px 12px;">{{LICENSE}}</td></tr>
  <tr><td style="font-size:14px;color:#999;padding:6px 12px;">🔧 语言</td><td style="font-size:15px;color:#333;font-weight:600;padding:6px 12px;">{{LANGUAGE}}</td></tr>
</table>

<h2 style="font-size:19px;color:#1a1a1a;margin:26px 0 16px;border-left:3px solid #7c3aed;padding-left:14px;">里面有什么？帮你省半年的精华</h2>

<blockquote style="border-left:3px solid #f59e0b;background:#faf5ff;margin:14px 0 6px;padding:10px 16px;">
  <p style="font-size:15px;color:#7c3aed;font-weight:700;margin:0;">📖 第一部分：{{第一部分标题}}</p>
</blockquote>
<p style="font-size:15px;color:#333;line-height:1.85;margin:0 0 16px;">{{内容描述……}}</p>

<blockquote style="border-left:3px solid #f59e0b;background:#faf5ff;margin:14px 0 6px;padding:10px 16px;">
  <p style="font-size:15px;color:#7c3aed;font-weight:700;margin:0;">📖 第二部分：{{第二部分标题}}</p>
</blockquote>
<p style="font-size:15px;color:#333;line-height:1.85;margin:0 0 16px;">{{内容描述……}}</p>

<blockquote style="border-left:3px solid #f59e0b;background:#faf5ff;margin:14px 0 6px;padding:10px 16px;">
  <p style="font-size:15px;color:#7c3aed;font-weight:700;margin:0;">📖 第三部分：{{第三部分标题}}</p>
</blockquote>
<p style="font-size:15px;color:#333;line-height:1.85;margin:0 0 16px;">{{内容描述……}}</p>

<hr style="border:0;border-top:1px dashed #d8b4fe;margin:28px 0;">

<h2 style="font-size:19px;color:#1a1a1a;margin:26px 0 16px;border-left:3px solid #7c3aed;padding-left:14px;">适合谁？不适合谁？</h2>
<p style="font-size:15px;color:#333;line-height:1.85;margin:0 0 16px;">如果你也像 {{作者/人群}} 一样，{{具体描述}}，那这份 {{资料/工具}} 可能就是为你准备的……（叙事体段落，不用列表）</p>
<p style="font-size:13px;color:#999;line-height:1.8;margin:0 0 16px;">⚠️ {{不适用场景或限制说明}}</p>

<h2 style="font-size:19px;color:#1a1a1a;margin:26px 0 16px;border-left:3px solid #7c3aed;padding-left:14px;">怎么开始？</h2>
<p style="font-size:15px;color:#333;line-height:1.85;margin:0 0 14px;">{{最简单的入手方式……链接/安装说明}}</p>

<pre style="background:#f5f5f5;color:#333;border-left:3px solid #7c3aed;padding:12px;font-size:14px;line-height:1.6;"><code>{{安装命令，如果有}}</code></pre>

<hr style="border:0;border-top:1px dashed #d8b4fe;margin:28px 0;">

<!-- 转发金句模块 -->
<table width="100%" cellpadding="16" cellspacing="0" border="0" style="background:#f5f0ff;margin:20px 0;text-align:center;">
  <tr><td>
    <p style="font-size:16px;color:#7c3aed;font-weight:700;line-height:1.8;margin:0;">"{{转发金句，30 字以内}}"</p>
    <p style="font-size:12px;color:#999;margin:8px 0 0;">—— 长按选中复制，转发给同样在路上的朋友</p>
  </td></tr>
</table>

<!-- CTA 阶段式投票 -->
<table width="100%" cellpadding="14" cellspacing="0" border="0" style="background:#faf5ff;text-align:center;">
  <tr><td>
    <p style="font-size:16px;font-weight:600;color:#7c3aed;margin:0 0 12px;">{{CTA 投票问题}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">A. {{选项 A}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">B. {{选项 B}}</p>
    <p style="font-size:14px;color:#666;margin:0 0 6px;">C. {{选项 C}}</p>
  </td></tr>
</table>

<p style="font-size:13px;color:#999;text-align:center;margin:20px 0 0;">🧡 欢迎<strong style="color:#7c3aed;">点赞、收藏、转发</strong>给同样在路上的朋友～</p>
<p style="font-size:13px;color:#999;text-align:center;margin:8px 0 0;">关注「{{公众号名称}}」，每周发现 GitHub 上最暖心的开源项目。</p>
```
