#!/usr/bin/env python3
"""Convert an image to ASCII art for README embedding."""

import sys
from PIL import Image, ImageOps

SHORT = " .:-=+*#%@"
LONG = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
PORTRAIT = " .,:;i1tfLCG08@"
BLOCK = " ░▒▓█"


def img_to_ascii(path: str, width: int = 70, charset: str = LONG, invert: bool = False) -> str:
    img = Image.open(path).convert("L")
    img = ImageOps.autocontrast(img, cutoff=2)
    w, h = img.size
    new_h = max(1, int((h / w) * width * 0.5))
    img = img.resize((width, new_h), Image.LANCZOS)
    pixels = list(img.getdata())
    if invert:
        pixels = [255 - p for p in pixels]
    chars = charset
    n = len(chars) - 1
    rows = []
    for i in range(new_h):
        row = pixels[i * width : (i + 1) * width]
        rows.append("".join(chars[p * n // 255] for p in row))
    return "\n".join(rows)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: img2ascii.py <path> [width] [short|long] [--invert]", file=sys.stderr)
        sys.exit(1)
    path = sys.argv[1]
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 70
    set_name = sys.argv[3] if len(sys.argv) > 3 else "long"
    invert = "--invert" in sys.argv
    charset = {"short": SHORT, "long": LONG, "portrait": PORTRAIT, "block": BLOCK}.get(set_name, LONG)
    print(img_to_ascii(path, width, charset, invert))
