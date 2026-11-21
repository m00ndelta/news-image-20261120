"""Generate entry.png (1024x1024) — a newspaper front page summing up 20 Nov 2026 world news.
Deterministic: same input -> same bytes (no timestamps, no randomness)."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
NAVY = (15, 42, 67)
RED = (178, 34, 34)
GOLD = (176, 141, 60)
INK = (24, 24, 24)
RULE = (200, 200, 198)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
M = 48

# ---- Masthead ----
d.rectangle([0, 0, W, 104], fill=NAVY)
d.text((M, 22), "THE WORLD", font=font(SERIF_B, 58), fill="white")
d.text((M, 82), "FRIDAY  ·  20 NOVEMBER 2026", font=font(SANS_B, 17), fill=(200, 210, 220))
d.rectangle([0, 104, W, 110], fill=RED)

y = 130
# ---- Lead story ----
d.text((M, y), "TOP STORY  ·  POLAND", font=font(SANS_B, 18), fill=RED)
y += 30
lead_top = y
d.rectangle([M, y, M + 118, y + 118], fill=NAVY)
d.text((M + 8, y + 30), "NATO", font=font(SERIF_B, 46), fill="white")
d.rectangle([M, y + 118, M + 118, y + 124], fill=GOLD)
tx = M + 140
head = "Russian missiles hit Poland in grave NATO airspace violation"
hl = wrap(d, head, font(SERIF_B, 40), W - M - tx)
y2 = draw_lines(d, hl, tx, y - 6, font(SERIF_B, 40), INK, 48)
summary = ("Two missiles and a suspected drone came down in Poland, which called "
           "it a deliberate provocation; NATO called it a grave violation of "
           "its airspace.")
sl = wrap(d, summary, font(SANS, 21), W - M - tx)
y3 = draw_lines(d, sl, tx, y2 + 8, font(SANS, 21), (60, 60, 60), 28)
y = max(lead_top + 140, y3 + 14)
d.line([(M, y), (W - M, y)], fill=RULE, width=2)

# ---- 2x2 grid ----
stories = [
    ("MARKETS",
     "Wall Street slumps as AI sell-off deepens",
     "The S&P 500 falls 3.7% into correction territory; Japan's Nikkei drops 5.06%."),
    ("BRITAIN & EU",
     "UK and EU sign food, carbon and youth deals",
     "Agreements cover food trade, carbon markets and youth mobility after years of talks."),
    ("PERU",
     "Magnitude 6.7 earthquake hits central Peru",
     "The quake strikes near Cerro de Pasco; buildings and roads damaged, one person injured."),
    ("CLIMATE  ·  COP31",
     "COP31 draft omits fossil fuels as talks overrun",
     "Activists protest in Antalya as the UN climate summit runs past its deadline."),
]
gy = y + 20
col_w = (W - 2 * M - 28) // 2
row_h = 172
for i, (kick, head, summ) in enumerate(stories):
    cx = M + (i % 2) * (col_w + 28)
    cy = gy + (i // 2) * row_h
    d.text((cx, cy), kick, font=font(SANS_B, 15), fill=RED)
    hl = wrap(d, head, font(SANS_B, 23), col_w)
    yy = draw_lines(d, hl, cx, cy + 24, font(SANS_B, 23), INK, 28)
    sl = wrap(d, summ, font(SANS, 17), col_w)
    draw_lines(d, sl, cx, yy + 4, font(SANS, 17), (70, 70, 70), 22)
    if i % 2 == 0:
        d.line([(cx + col_w + 14, cy), (cx + col_w + 14, cy + row_h - 16)], fill=RULE, width=1)

y = gy + 2 * row_h + 4
d.line([(M, y), (W - M, y)], fill=RULE, width=2)
y += 16
# ---- Also today ----
d.text((M, y), "ALSO TODAY", font=font(SANS_B, 16), fill=RED)
y += 28
also = [
    ("JUSTICE", "Jury convicts the man who started the Palisades Fire."),
    ("SPACE", "BepiColombo reaches Mercury after eight years in flight."),
    ("HEALTH", "United States loses its measles elimination status."),
]
for kick, txt in also:
    d.text((M, y), kick, font=font(SANS_B, 16), fill=NAVY)
    d.text((M + 96, y), txt, font=font(SANS, 17), fill=INK)
    y += 30

# ---- Footer ----
d.rectangle([0, H - 44, W, H], fill=NAVY)
d.text((M, H - 33), "20 NOVEMBER 2026  ·  THE WORLD IN ONE IMAGE", font=font(SANS_B, 14), fill=(200, 210, 220))
d.text((W - M - 300, H - 33), "Sources: NATO · S&P · EU · USGS", font=font(SANS, 14), fill=(170, 180, 190))

img.save("/home/hatch/workspace/news-image-20261120/entry.png", optimize=True)
print("saved entry.png")
