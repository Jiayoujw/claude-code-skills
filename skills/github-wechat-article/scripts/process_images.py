#!/usr/bin/env python3
"""
process_images.py - GitHub 项目图片处理脚本
用于 github-wechat-article skill

功能：
1. 从 GitHub README 提取图片链接并下载
2. 裁剪 GitHub OpenGraph 图为微信公众号封面尺寸 (900x383)
3. 压缩 GIF（隔帧取样 + 缩放 + 调色板降色）
4. 将图片 Base64 编码，生成 <img> 标签供 HTML 嵌入

用法：
  python process_images.py --project-url https://github.com/owner/repo --output-dir xxx-images
"""

import argparse
import base64
import io
import os
import re
import sys
import urllib.request
import urllib.parse
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("错误：需要安装 Pillow。运行：pip install Pillow")
    sys.exit(1)


def download_image(url: str, timeout: int = 15) -> bytes:
    """下载图片并返回二进制数据"""
    headers = {"User-Agent": "Mozilla/5.0"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def save_image(data: bytes, path: Path) -> None:
    """保存二进制数据为文件"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)


def get_opengraph_image(owner: str, repo: str) -> str:
    """获取 GitHub OpenGraph 图片 URL"""
    return f"https://opengraph.githubassets.com/1/{owner}/{repo}"


def extract_readme_images(readme_html: str) -> list[str]:
    """从 README HTML 中提取图片 URL"""
    # 匹配 <img src="..."> 和 ![alt](url)
    img_urls = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', readme_html)
    md_urls = re.findall(r'!\[.*?\]\((https?://[^\)]+)\)', readme_html)
    return list(set(img_urls + md_urls))


def crop_cover(image_data: bytes, output_path: Path) -> None:
    """裁剪图片为微信公众号封面尺寸 900x383 (2.35:1)"""
    img = Image.open(io.BytesIO(image_data))
    img = img.convert("RGB")
    
    target_w, target_h = 900, 383
    src_w, src_h = img.size
    
    # 计算裁剪区域（居中裁剪）
    src_ratio = src_w / src_h
    target_ratio = target_w / target_h
    
    if src_ratio > target_ratio:
        # 原图更宽，按高度裁剪
        new_w = int(src_h * target_ratio)
        left = (src_w - new_w) // 2
        crop_box = (left, 0, left + new_w, src_h)
    else:
        # 原图更高，按宽度裁剪
        new_h = int(src_w / target_ratio)
        top = (src_h - new_h) // 2
        crop_box = (0, top, src_w, top + new_h)
    
    img_cropped = img.crop(crop_box)
    img_resized = img_cropped.resize((target_w, target_h), Image.LANCZOS)
    img_resized.save(output_path, "PNG", optimize=True)
    print(f"封面图已保存：{output_path}")


def compress_gif(input_data: bytes, output_path: Path, 
                 max_colors: int = 192, max_size_mb: int = 5) -> None:
    """
    压缩 GIF：隔帧取样 + 缩放 + 调色板降色
    注意：使用 disposal=0 + optimize=False 避免透明通道 bug
    """
    input_path = output_path.with_suffix(".tmp.gif")
    with open(input_path, "wb") as f:
        f.write(input_data)
    
    try:
        img = Image.open(input_path)
        
        # 隔帧取样
        frames = []
        try:
            while True:
                frames.append(img.copy())
                img.seek(img.tell() + 2)  # 每隔一帧取一帧
        except EOFError:
            pass
        
        if not frames:
            print(f"警告：GIF 无有效帧，跳过压缩：{output_path.name}")
            return
        
        # 缩放（如果原图太大）
        max_dim = 800
        first_frame = frames[0]
        if first_frame.width > max_dim or first_frame.height > max_dim:
            ratio = min(max_dim / first_frame.width, max_dim / first_frame.height)
            new_size = (int(first_frame.width * ratio), int(first_frame.height * ratio))
            frames = [f.resize(new_size, Image.LANCZOS) for f in frames]
        
        # 调色板降色（先转 RGB，再 quantize）
        rgb_frames = [f.convert("RGB") for f in frames]
        quantized = [f.quantize(colors=max_colors) for f in rgb_frames]
        
        # 保存（先输出到新路径，避免源文件损坏）
        output_path_tmp = output_path.with_suffix(".compressed.gif")
        quantized[0].save(
            output_path_tmp,
            save_all=True,
            append_images=quantized[1:],
            loop=0,
            disposal=0,
            optimize=False
        )
        
        # 检查文件大小
        size_mb = output_path_tmp.stat().st_size / (1024 * 1024)
        if size_mb > max_size_mb:
            print(f"警告：压缩后文件仍大于 {max_size_mb}MB ({size_mb:.1f}MB)：{output_path.name}")
        
        # 替换原文件
        if output_path.exists():
            output_path.unlink()
        output_path_tmp.rename(output_path)
        print(f"GIF 压缩完成：{output_path.name} ({size_mb:.1f}MB)")
        
    finally:
        if input_path.exists():
            input_path.unlink()


def image_to_base64(image_path: Path) -> str:
    """将图片文件转换为 Base64 Data URI"""
    suffix = image_path.suffix.lower()
    mime_map = {".png": "image/png", ".jpg": "image/jpeg", 
                 ".jpeg": "image/jpeg", ".gif": "image/gif",
                 ".webp": "image/webp"}
    mime = mime_map.get(suffix, "image/png")
    
    with open(image_path, "rb") as f:
        data = f.read()
    
    b64 = base64.b64encode(data).decode("utf-8")
    return f"data:{mime};base64,{b64}"


def generate_img_tag(base64_uri: str, alt: str = "", caption: str = "") -> str:
    """生成微信兼容的 <img> 标签"""
    tag = f'<p style="text-align:center;margin:18px 0;"><img src="{base64_uri}" alt="{alt}" style="max-width:100%;display:block;margin:0 auto;" loading="lazy"></p>'
    if caption:
        tag += f'<span style="font-size:12px;color:#999;display:block;margin-top:4px;">▲ {caption}</span>'
    return tag


def main():
    parser = argparse.ArgumentParser(description="GitHub 项目图片处理脚本")
    parser.add_argument("--project-url", required=True, help="GitHub 项目 URL")
    parser.add_argument("--output-dir", required=True, help="图片输出目录")
    parser.add_argument("--no-cover", action="store_true", help="跳过封面图生成")
    args = parser.parse_args()
    
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 解析项目 URL
    url = args.project_url.rstrip("/")
    match = re.match(r"https?://github.com/([^/]+)/([^/]+)", url)
    if not match:
        print(f"错误：无法解析 GitHub URL：{url}")
        sys.exit(1)
    
    owner, repo = match.group(1), match.group(2)
    print(f"处理项目：{owner}/{repo}")
    
    # 1. 下载 GitHub OpenGraph 封面图
    if not args.no_cover:
        try:
            og_url = get_opengraph_image(owner, repo)
            print(f"下载封面图：{og_url}")
            og_data = download_image(og_url)
            cover_path = output_dir / "cover-github-banner.png"
            crop_cover(og_data, cover_path)
        except Exception as e:
            print(f"警告：封面图下载失败：{e}")
    
    # 2. 获取 README 图片
    try:
        readme_url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/README.md"
        readme_data = download_image(readme_url)
        readme_text = readme_data.decode("utf-8", errors="ignore")
        img_urls = extract_readme_images(readme_text)
        print(f"从 README 中发现 {len(img_urls)} 张图片")
        
        for i, img_url in enumerate(img_urls[:10]):  # 最多下载 10 张
            try:
                if not img_url.startswith("http"):
                    # 相对路径，拼接 base URL
                    if img_url.startswith("/"):
                        img_url = f"https://github.com{img_url}"
                    else:
                        img_url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{img_url}"
                
                print(f"下载图片 {i+1}/{len(img_urls)}：{img_url[:80]}...")
                img_data = download_image(img_url)
                
                # 判断格式并保存
                ext = ".png"
                if img_url.lower().endswith(".gif"):
                    ext = ".gif"
                elif img_url.lower().endswith((".jpg", ".jpeg")):
                    ext = ".jpg"
                
                img_path = output_dir / f"screenshot-{i+1}{ext}"
                
                if ext == ".gif":
                    # 先保存原文件，再压缩
                    tmp_path = img_path.with_suffix(".orig.gif")
                    save_image(img_data, tmp_path)
                    compress_gif(tmp_path.read_bytes(), img_path)
                    tmp_path.unlink(missing_ok=True)
                else:
                    save_image(img_data, img_path)
                
                # 生成 Base64 版本
                b64 = image_to_base64(img_path)
                tag = generate_img_tag(b64, alt=f"截图 {i+1}")
                print(f"  Base64 URI 长度：{len(b64)} 字符")
                print(f"  HTML 标签：{tag[:100]}...")
                
            except Exception as e:
                print(f"  警告：下载失败：{e}")
                continue
                
    except Exception as e:
        print(f"警告：README 处理失败：{e}")
    
    print(f"\n处理完成！图片保存在：{output_dir}")


if __name__ == "__main__":
    main()
