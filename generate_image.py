#!/usr/bin/env python3
"""Draw the 24 November 2026 news-image entry: a newspaper front page.

Writes entry.png (1024x1024, < 1 MiB) next to this script. Pure PIL,
no network, fully deterministic.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W = H = 1024
PAPER = (247, 243, 232)
INK = (26, 26, 26)
NAVY = (31, 56, 100)
RED = (178, 34, 34)
CARD = (255, 255, 255)
MUTED = (90, 90, 90)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_I = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns list of lines that fit in width px."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_icon(d, kind, cx, cy, s):
    """Small geometric icon, centred at (cx, cy), size ~s."""
    if kind == "chess":
        # crown
        pts = [(cx - s, cy + s * 0.6), (cx - s, cy - s * 0.2),
               (cx - s * 0.5, cy + s * 0.15), (cx, cy - s * 0.6),
               (cx + s * 0.5, cy + s * 0.15), (cx + s, cy - s * 0.2),
               (cx + s, cy + s * 0.6)]
        d.polygon(pts, fill=NAVY)
        d.rectangle([cx - s, cy + s * 0.6, cx + s, cy + s * 0.85], fill=RED)
    elif kind == "jet":
        d.polygon([(cx - s * 1.3, cy + s * 0.25), (cx + s * 0.9, cy - s * 0.5),
                   (cx + s * 1.4, cy), (cx + s * 0.9, cy + s * 0.5)],
                  fill=NAVY)
        d.polygon([(cx - s * 0.2, cy), (cx + s * 0.5, cy - s * 0.9),
                   (cx + s * 0.7, cy - s * 0.7)], fill=RED)
        d.polygon([(cx - s * 0.2, cy), (cx + s * 0.5, cy + s * 0.9),
                   (cx + s * 0.7, cy + s * 0.7)], fill=RED)
    elif kind == "ship":
        d.polygon([(cx - s * 1.2, cy + s * 0.3), (cx + s * 1.2, cy + s * 0.3),
                   (cx + s * 0.9, cy + s * 0.9), (cx - s * 0.9, cy + s * 0.9)],
                  fill=NAVY)
        d.rectangle([cx - s * 0.08, cy - s * 0.9, cx + s * 0.08, cy + s * 0.3],
                    fill=INK)
        d.polygon([(cx + s * 0.08, cy - s * 0.9), (cx + s * 0.08, cy - s * 0.3),
                   (cx + s * 0.9, cy - s * 0.3)], fill=RED)
    elif kind == "flag":
        d.rectangle([cx - s * 0.9, cy - s, cx - s * 0.75, cy + s], fill=INK)
        d.polygon([(cx - s * 0.75, cy - s), (cx + s * 0.9, cy - s * 0.55),
                   (cx - s * 0.75, cy - s * 0.1)], fill=RED)
        d.rectangle([cx - s * 0.9, cy + s * 0.55, cx + s * 0.9, cy + s * 0.75],
                    fill=NAVY)
    elif kind == "chip":
        d.rectangle([cx - s * 0.7, cy - s * 0.7, cx + s * 0.7, cy + s * 0.7],
                    fill=NAVY)
        d.rectangle([cx - s * 0.35, cy - s * 0.35, cx + s * 0.35, cy + s * 0.35],
                    fill=PAPER)
        for dx in (-0.45, 0, 0.45):
            d.rectangle([cx + dx * s - 3, cy - s, cx + dx * s + 3, cy - s * 0.7],
                        fill=INK)
            d.rectangle([cx + dx * s - 3, cy + s * 0.7, cx + dx * s + 3, cy + s],
                        fill=INK)
            d.rectangle([cx - s, cy + dx * s - 3, cx - s * 0.7, cy + dx * s + 3],
                        fill=INK)
            d.rectangle([cx + s * 0.7, cy + dx * s - 3, cx + s, cy + dx * s + 3],
                        fill=INK)
    elif kind == "blast":
        import math
        pts = []
        for i in range(16):
            ang = math.pi * i / 8
            r = s * (1.0 if i % 2 == 0 else 0.45)
            pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
        d.polygon(pts, fill=RED)
        d.ellipse([cx - s * 0.3, cy - s * 0.3, cx + s * 0.3, cy + s * 0.3],
                  fill=(255, 210, 60))


STORIES = [
    ("GENEVA", "chess", "Chess crown on the line",
     "Game 1 in Geneva: champion Gukesh Dommaraju faces challenger "
     "Sindarov over 14 games for the $2.5m title."),
    ("SEOUL", "jet", "Russian jets spark island alert",
     "Russian jets enter South Korea's air zone near Ulleung; jets "
     "scramble, residents shelter, envoy summoned."),
    ("KUALA LUMPUR", "ship", "6,803 more migrants to go home",
     "Malaysia will send 6,803 Myanmar nationals home in December: "
     "1,500 by navy ships, 5,303 by air, Anwar says."),
    ("PYONGYANG", "flag", "North Korea threatens Swiss office",
     "Kim Yo Jong says Pyongyang may shut the Swiss office after Bern "
     "sanctioned a camp over Ukrainian children."),
    ("CANBERRA", "chip", "Singapore vows: no chip back door",
     "PM Wong says Singapore is working with the US to stop firms "
     "rerouting American AI chips through the city-state."),
    ("VILLAVICENCIO", "blast", "Car bomb hits governor's office",
     "A blast outside Meta's government building wounds at least five; "
     "the president blames \u201cnarcoterrorism\u201d."),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 36  # side margin

    # Masthead
    f_mast = font(SERIF_B, 56)
    d.text((W // 2, 62), "THE WORLD IN ONE DAY", font=f_mast, fill=INK,
           anchor="mm")
    d.line([(mx, 100), (W - mx, 100)], fill=INK, width=3)
    d.line([(mx, 106), (W - mx, 106)], fill=INK, width=1)

    # Date band
    d.rectangle([mx, 116, W - mx, 160], fill=NAVY)
    f_date = font(SANS_B, 27)
    d.text((W // 2, 138), "TUESDAY  \u2022  24 NOVEMBER 2026", font=f_date,
           fill=(255, 255, 255), anchor="mm")

    # Subhead
    f_sub = font(SERIF_I, 21)
    d.text((W // 2, 184), "Six stories from around the world \u2014 one day in one image.",
           font=f_sub, fill=MUTED, anchor="mm")

    # Story cards: 3 columns x 2 rows
    gap = 16
    cw = (W - 2 * mx - 2 * gap) // 3
    ch = 372
    top = 208
    f_city = font(SANS_B, 16)
    f_head = font(SANS_B, 21)
    f_body = font(SANS, 17)

    for i, (city, icon, head, body) in enumerate(STORIES):
        col, row = i % 3, i // 3
        x0 = mx + col * (cw + gap)
        y0 = top + row * (ch + gap)
        x1, y1 = x0 + cw, y0 + ch
        d.rectangle([x0, y0, x1, y1], fill=CARD, outline=INK, width=2)
        # icon
        draw_icon(d, icon, x0 + cw // 2, y0 + 52, 30)
        # city label
        d.text((x0 + cw // 2, y0 + 108), city, font=f_city, fill=RED,
               anchor="mm")
        d.line([(x0 + cw // 2 - 24, y0 + 126), (x0 + cw // 2 + 24, y0 + 126)],
               fill=RED, width=2)
        # headline, up to 3 lines
        y = y0 + 140
        for line in wrap(d, head, f_head, cw - 28)[:3]:
            d.text((x0 + 14, y), line, font=f_head, fill=INK)
            y += 26
        # body, up to 4 lines
        y += 6
        for line in wrap(d, body, f_body, cw - 28)[:4]:
            d.text((x0 + 14, y), line, font=f_body, fill=(40, 40, 40))
            y += 22

    # Footer
    f_foot = font(SANS, 15)
    d.text((W // 2, 992),
           "All six stories above happened or were first reported on 24 November 2026.",
           font=f_foot, fill=MUTED, anchor="mm")

    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
