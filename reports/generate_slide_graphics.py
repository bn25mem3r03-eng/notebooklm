#!/usr/bin/env python3
"""Three portrait 4cm x 10cm (2:5) slide graphics for the AR/VR deck."""
import os
from PIL import Image, ImageDraw, ImageFont

OUTDIR = "/home/user/notebooklm/reports/slide_images"
os.makedirs(OUTDIR, exist_ok=True)

W, H = 720, 1800  # 2:5 ratio == 4cm x 10cm
FD = "/usr/share/fonts/truetype/dejavu/"
def F(sz, bold=False):
    return ImageFont.truetype(FD + ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"), sz)

NAVY = (20, 43, 69)
RED = (193, 18, 31)
TEAL = (14, 124, 134)
GREY = (97, 111, 125)
LIGHT = (243, 245, 248)
WHITE = (255, 255, 255)


def center(d, cx, y, text, font, fill):
    b = d.textbbox((0, 0), text, font=font)
    d.text((cx - (b[2]-b[0])/2, y), text, font=font, fill=fill)


def wrap(d, text, font, maxw):
    words = text.split(); lines = []; cur = ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textbbox((0, 0), t, font=font)[2] <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ============== 1. MARKET FUNNEL ==============
img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
center(d, W/2, 44, "MARKET SIZE", F(46, True), NAVY)
d.rounded_rectangle([W/2-70, 108, W/2+70, 118], radius=5, fill=RED)
cx = 360
ys = [250, 640, 1030, 1420]
widths = [670, 470, 285, 120]
segs = [
    (NAVY, "TAM", "₹1,000 Cr/yr", "Total opportunity"),
    (TEAL, "SAM", "₹100–150 Cr/yr", "Serviceable · 4 clusters"),
    (RED, "SOM", "₹1.5–2.5 Cr/yr", "Year-3 obtainable"),
]
for i, (col, tag, big, sub) in enumerate(segs):
    yt, yb = ys[i], ys[i+1]
    wt, wb = widths[i], widths[i+1]
    d.polygon([(cx-wt/2, yt), (cx+wt/2, yt), (cx+wb/2, yb-14), (cx-wb/2, yb-14)], fill=col)
    midy = (yt + yb) / 2
    center(d, cx, midy-66, tag, F(30, True), (255, 255, 255, 200))
    center(d, cx, midy-30, big, F(44 if i < 2 else 40, True), WHITE)
    center(d, cx, midy+26, sub, F(24, False), (235, 240, 245))
# penetration pill
d.rounded_rectangle([90, 1470, 630, 1540], radius=35, fill=LIGHT, outline=NAVY, width=3)
center(d, W/2, 1487, "Penetration ≈ 1–2% of SAM", F(30, True), NAVY)
center(d, W/2, 1600, "Illustrative — all figures are assumptions", F(23, False), GREY)
img.save(OUTDIR + "/market_analysis.png")

# ============== 2. REVENUE STREAMS ==============
img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
center(d, W/2, 44, "REVENUE STREAMS", F(44, True), NAVY)
d.rounded_rectangle([W/2-70, 108, W/2+70, 118], radius=5, fill=RED)
cards = [
    (RED, "Station Subscription", "₹20,000 / station / mo", "Core recurring revenue (RaaS)"),
    (TEAL, "VR Training Licence", "₹30,000 / headset / yr", "New & contract-worker onboarding"),
    (NAVY, "Hardware + Onboarding", "~₹1.6L kit + ~₹3L setup", "Near-cost kit + MES/ERP integration"),
    (GREY, "Cobot Bridge (future)", "₹5,000 / station / mo", "Robot hand-over — after FTO"),
]
top = 210; ch = 350; gap = 35
for i, (col, title, price, note) in enumerate(cards):
    y = top + i*(ch+gap)
    d.rounded_rectangle([40, y, 680, y+ch], radius=24, fill=LIGHT, outline=(223,227,232), width=2)
    d.rounded_rectangle([40, y, 70, y+ch], radius=12, fill=col)
    d.rectangle([58, y, 72, y+ch], fill=col)
    d.text((100, y+46), title, font=F(34, True), fill=NAVY)
    psz = 46
    while d.textbbox((0,0), price, font=F(psz, True))[2] > 560 and psz > 30:
        psz -= 2
    d.text((100, y+120), price, font=F(psz, True), fill=col)
    for j, ln in enumerate(wrap(d, note, F(26), 540)):
        d.text((100, y+210+j*36), ln, font=F(26), fill=GREY)
img.save(OUTDIR + "/business_model.png")

# ============== 3. ROADMAP TIMELINE ==============
img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
center(d, W/2, 44, "36-MONTH ROADMAP", F(42, True), NAVY)
d.rounded_rectangle([W/2-70, 108, W/2+70, 118], radius=5, fill=RED)
lx = 120
d.line([(lx, 250), (lx, 1560)], fill=(200, 208, 216), width=8)
nodes = [
    (NAVY, "P1", "0–6 mo", "Prototype: 1 station, ≥95% checks, VR trainer, seed funding"),
    (TEAL, "P2", "6–12 mo", "Paid pilot at 1 plant; KPIs vs baseline; convert to contract"),
    (RED, "P3", "12–24 mo", "v1.0: Recipe Studio, dashboard, MES, multilingual; 2–3 customers"),
    (NAVY, "P4", "24–36 mo", "Cobot Bridge (post-FTO); break-even; patents; SE Asia"),
]
nys = [330, 660, 990, 1320]
r = 52
for i, (col, p, mo, txt) in enumerate(nodes):
    y = nys[i]
    d.ellipse([lx-r, y-r, lx+r, y+r], fill=col, outline=WHITE, width=5)
    center(d, lx, y-26, p, F(38, True), WHITE)
    d.text((lx+80, y-r+4), mo, font=F(32, True), fill=col)
    for j, ln in enumerate(wrap(d, txt, F(26), 470)):
        d.text((lx+80, y-6+j*34), ln, font=F(26), fill=(55, 65, 80))
# conclusion strip
d.rounded_rectangle([40, 1620, 680, 1770], radius=20, fill=NAVY)
concl = "Guides, checks & trains from one recipe — headset-free, at an Indian price."
for j, ln in enumerate(wrap(d, concl, F(27, True), 600)):
    center(d, W/2, 1648+j*40, ln, F(27, True), WHITE)
img.save(OUTDIR + "/roadmap.png")

print("saved 3 images to", OUTDIR)
for f in ("market_analysis", "business_model", "roadmap"):
    im = Image.open(f"{OUTDIR}/{f}.png"); print(f, im.size)
