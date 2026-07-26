#!/usr/bin/env python3
"""
banner 生成器 — 在原图底部叠加半透明信息条 + 文字

用法:
  python3 generate_banner.py <原图> <项目名> <副标题> <技术栈> <输出路径>

示例:
  # 三行（项目名 + 副标题 + 技术栈）
  python3 generate_banner.py big.png "NekoC2" "Modular C2 Framework" "Java · C · Electron" banner.png

  # 两行（项目名 + 副标题，无技术栈）
  python3 generate_banner.py big.png "NekoPT" "Agent Framework" "" banner.png

依赖:
  pip install Pillow

效果:
  原图底部 1/4 区域叠加半透明深色条
  技术栈为空 → 两行（项目名 + 副标题）
  技术栈非空 → 三行（项目名 + 副标题 + 技术栈）
  不修改原图
"""
import sys
from PIL import Image, ImageDraw, ImageFont


def load_font(size):
    candidates = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNS.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/mnt/c/Windows/Fonts/arial.ttf",
        "/mnt/c/Windows/Fonts/segoeui.ttf",
    ]
    for p in candidates:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()


def generate_banner(src, title, subtitle, tech, out):
    img = Image.open(src).convert("RGBA")
    W, H = img.size
    BAR = H // 4

    overlay = Image.new("RGBA", (W, BAR), (17, 17, 27, 180))
    img.paste(overlay, (0, H - BAR), overlay)

    draw = ImageDraw.Draw(img)

    f_big   = load_font(W // 16)
    f_med   = load_font(W // 38)
    f_small = load_font(W // 50)

    def center(text, y, font, fill):
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        draw.text(((W - tw) // 2, y), text, fill=fill, font=font)

    base = H - BAR

    if tech:
        # 三行（不变）
        center(title, base + int(BAR * 0.15), f_big, (205, 214, 244))
        center(subtitle, base + int(BAR * 0.50), f_med, (137, 180, 250))
        center(tech, base + int(BAR * 0.78), f_small, (166, 173, 200))
    else:
        # 两行：固定比例，标题 0.18 / 副标题 0.65
        center(title, base + int(BAR * 0.18), f_big, (205, 214, 244))
        center(subtitle, base + int(BAR * 0.65), f_med, (137, 180, 250))

    img.convert("RGB").save(out)
    print(f"OK: {out} ({W}x{H})")


if __name__ == "__main__":
    if len(sys.argv) < 6:
        print(__doc__)
        sys.exit(1)
    generate_banner(*sys.argv[1:6])
