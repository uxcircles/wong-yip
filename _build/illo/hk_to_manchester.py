"""Theme 1, 'Hong Kong to Manchester', paper-cut with fine ink lines.
    python3 _build/illo/hk_to_manchester.py  -> assets/illo/hk-to-manchester.svg (source)
The site uses a 2x WebP exported from this SVG (see export.js), so phones don't run the SVG filters.
"""
import os

W, H = 1000, 540
INK = "#22003f"
c = {"purple": "#360064", "deep": "#22003f", "yellow": "#ffe900", "orange": "#ff9b00", "cream": "#fbf6ec",
     "lilac": "#d9c9ea", "pale": "#ece4f4", "brick": "#e0662a", "brick2": "#c9531f", "water": "#b9c8ee", "mint": "#bfe3cf"}

layers = {}  # name -> list of svg strings; each layer is one sheet of paper with its own shadow


def add(layer, s):
    layers.setdefault(layer, []).append(s)


def rect(layer, x, y, w, h, fill, rx=0, extra=""):
    add(layer, f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" {extra}/>')


def path(layer, d, fill, extra=""):
    add(layer, f'<path d="{d}" fill="{fill}" {extra}/>')


def line(d, w=2, op=.85, dash=""):
    add("ink", f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" opacity="{op}" {dash}/>')


# ---- sky
add("sky", f'<circle cx="640" cy="200" r="132" fill="{c["yellow"]}"/>')
path("sky", "M720 92 q20 -34 58 -20 q14 -30 50 -16 q36 -6 38 30 q26 4 22 30 h-188 q-6 -22 20 -24z", c["cream"])
path("sky", "M372 150 q14 -24 42 -14 q12 -22 40 -10 q30 0 28 24 q18 4 14 22 h-136 q-4 -18 12 -22z", c["pale"])

# ---- Hong Kong tong lau (left)
TX, TY, TW = 70, 70, 250
rect("bldg", TX, TY, TW, 420, c["lilac"])
rect("bldg", TX - 8, TY - 14, TW + 16, 22, c["cream"], 3)          # parapet
for row in range(6):
    y = TY + 36 + row * 62
    for col in range(3):
        x = TX + 22 + col * 76
        rect("bldg", x, y, 54, 36, c["purple"], 2)
        line(f"M{x} {y} h54 v36 h-54 z", 1.6, .9)
        line(f"M{x+27} {y} v36 M{x} {y+12} h54", 1.4, .6)
        if (row * 3 + col) % 4 == 1:
            rect("bldg", x + 6, y + 15, 18, 19, c["yellow"], 1)        # a lit window
    rect("front", TX - 6, y + 40, TW + 12, 9, c["cream"], 2)          # balcony slab
    line(" ".join(f"M{TX - 2 + i * 14} {y+40} v-12" for i in range(19)) + f" M{TX-4} {y+28} h{TW+8}", 1.4, .7)
    if row in (1, 3, 4):                                             # aircon box
        ax = TX + TW - 6
        rect("front", ax, y + 4, 40, 28, c["cream"], 3)
        line(f"M{ax+6} {y+10} h28 M{ax+6} {y+16} h28 M{ax+6} {y+22} h28 M{ax} {y+32} l-6 8", 1.3, .75)
    if row in (0, 2, 5):                                             # laundry pole with clothes
        px = TX + TW
        line(f"M{px-30} {y+30} L{px+74} {y+12}", 2.2, .9)
        for k, col_ in enumerate(("yellow", "orange", "pale")):
            cx = px - 4 + k * 26
            cy = y + 26 - k * 4.6
            path("front", f"M{cx} {cy} h16 l3 22 h-22 z", c[col_])
            line(f"M{cx} {cy} h16", 1.2, .7)
# plants on the roof
for i, x in enumerate((TX + 20, TX + 52, TX + 200)):
    rect("front", x, TY - 30, 20, 18, c["orange"], 3)
    path("front", f"M{x+10} {TY-30} q-16 -18 -4 -34 q4 16 4 34 q2 -24 16 -30 q0 18 -16 30z", "#7fbf8e")
# vertical neon sign
rect("front", TX - 52, 150, 44, 186, c["orange"], 5)
line(f"M{TX-8} 170 h10 M{TX-8} 316 h10", 2.4, .9)
add("front", f'<text x="{TX-30}" y="206" fill="{c["cream"]}" font-family="Chiron Hei HK, Noto Sans TC, sans-serif" font-weight="800" font-size="36" text-anchor="middle">黃</text>')
add("front", f'<text x="{TX-30}" y="252" fill="{c["cream"]}" font-family="Chiron Hei HK, Noto Sans TC, sans-serif" font-weight="800" font-size="36" text-anchor="middle">葉</text>')
add("front", f'<circle cx="{TX-30}" cy="290" r="10" fill="{c["yellow"]}"/>')
add("front", f'<circle cx="{TX-30}" cy="318" r="6" fill="{c["cream"]}"/>')

# ---- Ancoats cotton mill (right)
MX, MY, MW = 560, 250, 400
rect("bldg", 860, 88, 46, 180, c["brick2"])                          # chimney
rect("bldg", 852, 78, 62, 18, c["cream"], 2)
rect("bldg", 860, 120, 46, 10, c["orange"])
path("bldg", f"M{MX} {MY} " + " ".join(f"L{MX+25+i*50} {MY-46} L{MX+50+i*50} {MY}" for i in range(8)) + " Z", c["orange"])
rect("bldg", MX, MY, MW, 200, c["brick"])
for i in range(8):
    line(f"M{MX+25+i*50} {MY-46} L{MX+25+i*50} {MY-6}", 1.3, .5)
for row in range(2):
    for col in range(7):
        x, y = MX + 22 + col * 54, MY + 26 + row * 82
        fill = c["yellow"] if (row, col) in ((0, 2), (1, 5), (0, 6)) else c["cream"]
        path("front", f"M{x} {y+52} V{y+18} A18 16 0 0 1 {x+36} {y+18} V{y+52} Z", fill)
        line(f"M{x} {y+52} V{y+18} A18 16 0 0 1 {x+36} {y+18} V{y+52} Z M{x+18} {y+3} V{y+52} M{x} {y+30} h36", 1.4, .75)
for row in range(9):                                                 # brick coursing
    yy = MY + 12 + row * 22
    line(f"M{MX+4} {yy} h{MW-8}", 1, .18)
rect("front", MX - 6, MY + 192, MW + 12, 12, c["brick2"], 2)          # plinth

# ---- Rochdale Canal, bridge and a narrowboat
path("water", "M0 470 H1000 V512 " + "".join("q-25 %d -50 0 " % (12 if i % 2 else 16) for i in range(20)) + "Z", c["water"])
line("M60 498 q20 -8 40 0 t40 0 M300 500 q20 -8 40 0 t40 0 M620 500 q20 -8 40 0 t40 0 M840 500 q20 -8 40 0 t40 0", 1.6, .45)
path("ground", "M0 452 H424 V470 H0 Z", c["deep"])                   # Hong Kong pavement
path("ground", f"M606 452 H{W} V470 H606 Z", c["deep"])               # towpath
path("boat", "M404 456 Q515 392 626 456 V522 H598 Q515 452 432 522 H404 Z", c["brick2"])   # humpback canal bridge
path("boat", "M404 456 Q515 392 626 456 L626 466 Q515 402 404 466 Z", c["cream"])           # coping stones
line("M432 522 Q515 452 598 522", 1.6, .8)

line(" ".join(f"M{x} {500 - 0} " for x in ()) + "M470 470 h20 M540 470 h20 M505 486 h20 M450 500 h18 M565 500 h18", 1.1, .35)
path("boat", "M660 488 h220 l-16 26 h-196 z", c["purple"])
rect("boat", 700, 466, 140, 24, c["orange"], 4)
for i in range(4):
    rect("boat", 712 + i * 32, 472, 18, 12, c["cream"], 2)
line("M660 488 h220 M706 466 h128", 1.4, .7)

# ---- flight path and the paper plane
line("M200 52 C 330 -10, 520 10, 610 60", 3, .8, 'stroke-dasharray="2 11"')
path("plane", "M612 46 l46 18 l-44 16 l8 -14 z", c["cream"])
line("M612 46 l46 18 l-44 16 l8 -14 z M622 66 l36 -2", 1.4, .8)
# boarding pass drifting along the route
add("plane", '<g transform="rotate(-10 430 64)">'
             f'<rect x="392" y="40" width="96" height="48" rx="5" fill="{c["cream"]}"/>'
             f'<rect x="392" y="40" width="22" height="48" rx="5" fill="{c["orange"]}"/>'
             f'<text x="452" y="62" font-family="Red Hat Mono, monospace" font-weight="700" font-size="15" fill="{c["purple"]}" text-anchor="middle">HKG</text>'
             f'<text x="452" y="80" font-family="Red Hat Mono, monospace" font-weight="700" font-size="15" fill="{c["purple"]}" text-anchor="middle">MAN</text></g>')

FILTER = '''<filter id="paper" x="-6%" y="-6%" width="112%" height="118%" color-interpolation-filters="sRGB">
  <feTurbulence type="fractalNoise" baseFrequency="1.15" numOctaves="2" seed="5" result="t"/>
  <feDiffuseLighting in="t" lighting-color="#ffffff" surfaceScale=".7" result="lit"><feDistantLight azimuth="235" elevation="68"/></feDiffuseLighting>
  <feComposite in="lit" in2="SourceAlpha" operator="in" result="tex"/>
  <feBlend in="SourceGraphic" in2="tex" mode="multiply" result="papered"/>
  <feComposite in="papered" in2="SourceAlpha" operator="in" result="cut"/>
  <feDropShadow in="cut" dx="3" dy="6" stdDeviation="4" flood-color="#22003f" flood-opacity=".32"/>
</filter>'''

order = ["sky", "bldg", "front", "water", "ground", "boat", "plane", "ink"]
body = ""
for name in order:
    inner = "".join(layers.get(name, []))
    body += f'<g>{inner}</g>' if name == "ink" else f'<g filter="url(#paper)">{inner}</g>'
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
       f'<defs>{FILTER}</defs>{body}</svg>')
out = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "assets", "illo", "hk-to-manchester.svg")
open(out, "w").write(svg)
print(out)
