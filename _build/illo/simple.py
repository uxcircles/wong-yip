"""Wong & Yip illustrations: plain paper cut, few large shapes, no ink lines.
    python3 _build/illo/simple.py  -> assets/illo/*.svg (sources; the site uses WebP exports)"""
from paper import Canvas, c, backdrop


def arch(x, y, w, h):
    r = w / 2
    return f"M{x} {y+h} V{y+r} A{r} {r} 0 0 1 {x+w} {y+r} V{y+h} Z"


def hk_to_manchester():
    cv = Canvas(1000, 540)
    cv.circle("sky", 620, 210, 130, "yellow")
    cv.path("sky", "M700 118 q20 -34 58 -20 q14 -30 50 -16 q36 -6 38 30 q26 4 22 30 h-188 q-6 -22 20 -24z", "cream")
    # Hong Kong tenement: one block, a grid of windows, the vertical sign
    cv.rect("bldg", 90, 90, 240, 380, "lilac")
    cv.rect("bldg", 80, 76, 260, 24, "cream", 4)
    for r in range(5):
        for k in range(3):
            cv.rect("mid", 116 + k * 72, 124 + r * 66, 44, 40, "yellow" if (r, k) in ((1, 2), (3, 0)) else "purple", 3)
    cv.rect("front", 40, 150, 40, 170, "orange", 6)
    # Ancoats mill: sawtooth roof, chimney, two rows of arched windows
    cv.rect("bldg", 850, 96, 44, 170, "brick2")
    cv.path("bldg", "M560 260 " + " ".join(f"L{585 + i * 50} 214 L{610 + i * 50} 260" for i in range(8)) + " Z", "orange")
    cv.rect("bldg", 560, 260, 400, 210, "brick")
    for r in range(2):
        for k in range(5):
            cv.path("mid", arch(592 + k * 74, 292 + r * 86, 40, 58), "yellow" if (r, k) == (0, 3) else "cream")
    # canal with a wavy torn edge, and a plain humpback bridge
    cv.rect("front", 0, 452, 420, 18, "deep")
    cv.rect("front", 610, 452, 390, 18, "deep")
    cv.path("front", "M0 470 H1000 V512 " + "".join("q-25 %d -50 0 " % (12 if i % 2 else 16) for i in range(20)) + "Z", "water")
    cv.path("top", "M404 470 Q515 400 626 470 V522 H596 Q515 456 434 522 H404 Z", "brick2")
    # a single paper plane between the two cities
    cv.path("top", "M400 92 l76 26 l-72 26 l12 -24 z", "cream")
    cv.save("hk-to-manchester")


def stamp_duty():
    cv = Canvas(1000, 540, .34)
    cv.circle("sky", 560, 250, 190, "slate")
    zig = "".join("l-14 16 l-14 -16 " for _ in range(8))
    cv.group("mid", "rotate(-7 520 280)", f'<path d="M408 70 H632 V448 {zig} Z" fill="{c["cream"]}"/>'
             f'<text x="520" y="132" font-family="Red Hat Mono, monospace" font-weight="700" font-size="40" fill="{c["purple"]}" text-anchor="middle">SDLT</text>'
             + "".join(f'<rect x="436" y="{170 + i * 40}" width="{168 - (i % 2) * 52}" height="12" rx="6" fill="{c["lilac"]}"/>' for i in range(4))
             + f'<rect x="436" y="340" width="168" height="48" rx="6" fill="{c["yellow"]}"/>')
    key = (f'<path fill-rule="evenodd" d="M250 410 a70 70 0 1 0 140 0 a70 70 0 1 0 -140 0 z M292 410 a28 28 0 1 0 56 0 a28 28 0 1 0 -56 0 z" fill="{c["orange"]}"/>'
           f'<rect x="384" y="394" width="350" height="32" rx="10" fill="{c["orange"]}"/>'
           f'<path d="M650 426 h24 v34 h-24 z M694 426 h26 v50 h-26 z" fill="{c["orange"]}"/>')
    cv.group("top", "rotate(-8 500 420)", key)
    cv.save("stamp-duty")


def tax_return():
    cv = Canvas(600, 450, .24)
    backdrop(cv, 40, 46, 520, 360)
    cv.group("mid", "rotate(-4 330 240)", f'<rect x="196" y="78" width="270" height="320" rx="8" fill="{c["cream"]}"/>'
             f'<rect x="222" y="104" width="120" height="30" rx="5" fill="{c["purple"]}"/>'
             + "".join(f'<rect x="222" y="{160 + i * 44}" width="{150 - (i % 2) * 40}" height="10" rx="5" fill="{c["lilac"]}"/><rect x="394" y="{154 + i * 44}" width="48" height="22" rx="4" fill="{c["pale"]}"/>' for i in range(5)))
    cv.rect("top", 80, 88, 140, 158, "cream", 12)
    cv.rect("top", 80, 88, 140, 44, "orange", 12)
    cv.rect("top", 80, 114, 140, 18, "orange")
    cv.text("top", 150, 120, "JAN", 24, "cream")
    cv.text("top", 150, 214, "31", 70, "purple")
    cv.save("tax-return")


def company():
    cv = Canvas(600, 450, .24)
    backdrop(cv, 40, 54, 520, 350, 2)
    cv.rect("bldg", 130, 130, 340, 270, "lilac")
    cv.rect("mid", 116, 112, 368, 56, "purple", 6)
    awning = "M116 168 H484 V200 " + "".join("q-23 26 -46 0 " for _ in range(8)) + "Z"
    cv.path("top", awning, "orange")
    cv.rect("mid", 160, 240, 170, 160, "pale", 4)
    cv.rect("mid", 360, 232, 84, 168, "purple", 4)
    cv.circle("top", 428, 318, 7, "yellow")
    cv.save("company")


def payroll():
    cv = Canvas(600, 450, .24)
    backdrop(cv, 40, 50, 520, 356, -2)
    cv.group("mid", "rotate(-5 280 180)", f'<rect x="170" y="78" width="230" height="200" rx="8" fill="{c["cream"]}"/>'
             + "".join(f'<rect x="196" y="{108 + i * 26}" width="{150 - (i % 2) * 44}" height="10" rx="5" fill="{c["lilac"]}"/>' for i in range(3))
             + f'<rect x="196" y="196" width="178" height="34" rx="6" fill="{c["yellow"]}"/>')
    cv.rect("bldg", 120, 196, 320, 190, "lilac", 10)
    cv.path("front", "M120 232 L280 316 L440 232 V386 H120 Z", "cream")
    for i in range(3):
        y = 386 - i * 24
        cv.path("top", f"M462 {y} a48 14 0 0 0 96 0 v-20 a48 14 0 0 0 -96 0 z", "orange" if i % 2 else "yellow")
    cv.path("top", "M462 318 a48 14 0 0 0 96 0 a48 14 0 0 0 -96 0 z", "yellow")
    cv.save("payroll")


def landlord():
    cv = Canvas(600, 450, .24)
    backdrop(cv, 40, 50, 520, 360, -2)
    cv.path("bldg", "M120 180 L270 80 L420 180 Z", "slate")
    cv.rect("bldg", 140, 180, 260, 224, "brick")
    cv.rect("mid", 166, 214, 80, 70, "cream", 4)
    cv.rect("mid", 294, 214, 80, 70, "cream", 4)
    cv.path("mid", arch(232, 300, 76, 104), "purple")
    cv.rect("front", 470, 250, 12, 160, "deep", 3)
    cv.group("top", "rotate(-4 476 230)", f'<rect x="412" y="196" width="128" height="62" rx="8" fill="{c["yellow"]}"/>'
             f'<text x="476" y="238" font-family="Red Hat Mono, monospace" font-weight="700" font-size="26" fill="{c["purple"]}" text-anchor="middle">TO LET</text>')
    cv.save("landlord")


def lost():
    cv = Canvas(600, 450, .22)
    backdrop(cv, 50, 60, 500, 330, 3)
    cv.path("sky", "M130 150 q14 -26 46 -14 q12 -24 44 -10 q32 0 30 26 q20 4 16 24 h-150 q-6 -20 14 -26z", "cream")
    cv.path("top", "M360 150 l96 32 l-92 34 l16 -30 z", "cream", 'transform="rotate(18 410 180)"')
    cv.group("top", "rotate(-8 270 320)", f'<rect x="200" y="280" width="150" height="76" rx="8" fill="{c["cream"]}"/>'
             f'<rect x="200" y="280" width="26" height="76" rx="8" fill="{c["orange"]}"/>'
             f'<text x="290" y="333" font-family="Red Hat Mono, monospace" font-weight="700" font-size="34" fill="{c["purple"]}" text-anchor="middle">404</text>')
    cv.save("lost")


if __name__ == "__main__":
    for f in (hk_to_manchester, stamp_duty, tax_return, company, payroll, landlord, lost):
        f()
    print("ok")
