"""The rest of the illustration set, same paper-cut kit as the home hero.
    python3 _build/illo/set.py  -> assets/illo/*.svg (sources; the site uses WebP exports)"""
import math
from paper import Canvas, c, wy_mark, backdrop


def tax_return():
    cv = Canvas(600, 450, .26)
    backdrop(cv, 40, 46, 520, 360)
    # tear-off calendar: 31 January
    cv.rect("bldg", 66, 64, 128, 150, "cream", 10)
    cv.rect("bldg", 66, 64, 128, 40, "orange", 10)
    cv.rect("bldg", 66, 88, 128, 16, "orange")
    cv.text("bldg", 130, 92, "JAN", 22, "cream")
    cv.text("bldg", 130, 180, "31", 66, "purple")
    for x in (96, 164):
        cv.circle("top", x, 64, 7, "deep")
    # the return, tilted
    cv.path("mid", "M178 84 L452 64 L482 396 L208 416 Z", "cream")
    cv.group("mid", "rotate(-4.2 330 240)", f'<rect x="200" y="96" width="120" height="34" rx="4" fill="{c["purple"]}"/>'
             f'<text x="260" y="120" font-family="Red Hat Mono, monospace" font-weight="700" font-size="20" fill="{c["cream"]}" text-anchor="middle">SA100</text>')
    for i in range(6):
        y0 = 160 + i * 38
        cv.line(f"M{214 + i * 2.2} {y0 + 18} L{354 + i * 2.2} {y0 + 8}", 1.6, .55)
        cv.group("mid", f"rotate(-4.2 400 {y0})", f'<rect x="372" y="{y0 - 6}" width="66" height="22" rx="3" fill="{c["pale"]}"/>')
        cv.line(f"M{372 + i * 2} {y0 + 10} l66 -5 l1.6 22 l-66 5 z", 1.2, .5)
    # W·Y stamp impression
    cv.add("ink", f'<g opacity=".92"><path d="M232 340 l84 -6 l6 76 l-84 6 z" fill="none" stroke="{c["orange"]}" stroke-width="5"/>{wy_mark(244, 352, .62)}</g>')
    # pen
    cv.group("top", "rotate(32 470 250)", f'<rect x="452" y="120" width="34" height="230" rx="14" fill="{c["yellow"]}"/>'
             f'<rect x="452" y="120" width="34" height="70" rx="14" fill="{c["purple"]}"/>'
             f'<path d="M452 336 h34 l-17 44 z" fill="{c["cream"]}"/><path d="M464 366 h10 l-5 14 z" fill="{c["deep"]}"/>')
    cv.line("M541 155 l-26 -16", 2, .6)
    cv.save("tax-return")


def company():
    cv = Canvas(600, 450, .26)
    backdrop(cv, 30, 54, 540, 350, 2)
    # shopfront
    cv.rect("bldg", 96, 112, 320, 300, "lilac")
    cv.rect("mid", 84, 104, 344, 60, "purple", 4)
    cv.text("mid", 256, 146, "&amp; CO LTD", 30, "yellow")
    scallop = "M84 164 H428 V196 " + "".join("q-17 22 -34.4 0 " for _ in range(10)) + "Z"
    cv.path("top", scallop, "orange")
    for i in range(5):
        cv.rect("top", 84 + 34.4 * (2 * i + 1), 164, 34.4, 32, "cream")
    cv.line(scallop, 1.4, .55)
    cv.rect("mid", 112, 232, 170, 150, "pale", 3)                 # window
    cv.line("M112 232 h170 v150 h-170 z M197 232 v150", 1.8, .8)
    cv.group("top", "rotate(-4 197 272)", f'<rect x="150" y="256" width="94" height="38" rx="4" fill="{c["yellow"]}"/>'
             f'<text x="197" y="283" font-family="Red Hat Mono, monospace" font-weight="700" font-size="20" fill="{c["purple"]}" text-anchor="middle">OPEN</text>')
    cv.line("M170 232 L174 257 M224 232 L222 254", 1.4, .8)
    cv.rect("mid", 312, 222, 82, 172, "purple", 3)                 # door
    cv.circle("top", 380, 312, 6, "yellow")
    cv.rect("mid", 322, 236, 62, 52, "slate", 2)
    cv.rect("front", 80, 404, 352, 14, "deep", 2)
    cv.rect("front", 410, 362, 38, 42, "orange", 5)               # plant
    cv.path("front", "M429 362 q-30 -26 -8 -58 q6 30 8 58 q0 -40 26 -52 q2 32 -26 52z", "green")
    # certificate with seal
    cv.group("top", "translate(-26 6) rotate(8 500 140)", f'<rect x="440" y="64" width="124" height="160" rx="6" fill="{c["cream"]}"/>'
             f'<rect x="458" y="86" width="88" height="10" rx="5" fill="{c["purple"]}"/>'
             + "".join(f'<rect x="458" y="{108 + i * 16}" width="{88 - (i % 2) * 26}" height="6" rx="3" fill="{c["lilac"]}"/>' for i in range(4))
             + f'<path d="M520 196 l-10 34 l14 -8 l8 14 l4 -36 z" fill="{c["orange"]}"/>'
             f'<circle cx="524" cy="190" r="20" fill="{c["yellow"]}"/><circle cx="524" cy="190" r="11" fill="none" stroke="{c["orange"]}" stroke-width="3"/>')
    cv.save("company")


def payroll():
    cv = Canvas(600, 450, .26)
    backdrop(cv, 36, 50, 528, 356, -2)
    # pay-day calendar
    cv.rect("bldg", 420, 58, 120, 136, "cream", 10)
    cv.rect("bldg", 420, 58, 120, 36, "purple", 10)
    cv.rect("bldg", 420, 80, 120, 14, "purple")
    cv.text("bldg", 480, 84, "PAY DAY", 16, "yellow")
    cv.text("bldg", 480, 168, "25", 60, "purple")
    for x in (448, 512):
        cv.circle("top", x, 58, 6, "deep")
    # payslip sliding out of its envelope
    cv.group("mid", "rotate(-5 260 170)", f'<rect x="150" y="70" width="226" height="210" rx="6" fill="{c["cream"]}"/>'
             f'<rect x="168" y="88" width="120" height="26" rx="4" fill="{c["purple"]}"/>'
             f'<text x="228" y="107" font-family="Red Hat Mono, monospace" font-weight="700" font-size="16" fill="{c["cream"]}" text-anchor="middle">PAYSLIP</text>'
             + "".join(f'<rect x="168" y="{130 + i * 18}" width="{120 - (i % 2) * 30}" height="7" rx="3" fill="{c["lilac"]}"/><rect x="316" y="{130 + i * 18}" width="42" height="7" rx="3" fill="{c["lilac"]}"/>' for i in range(4))
             + f'<rect x="168" y="208" width="190" height="30" rx="4" fill="{c["yellow"]}"/>'
             f'<text x="178" y="229" font-family="Red Hat Mono, monospace" font-weight="700" font-size="15" fill="{c["purple"]}">NET PAY</text>'
             f'<text x="350" y="229" font-family="Red Hat Mono, monospace" font-weight="700" font-size="15" fill="{c["purple"]}" text-anchor="end">£</text>')
    cv.rect("bldg", 110, 200, 300, 186, "lilac", 8)               # envelope back
    cv.path("front", "M110 230 L260 312 L410 230 V386 H110 Z", "cream")
    cv.line("M110 230 L260 312 L410 230 M110 386 L220 300 M410 386 L300 300", 1.6, .55)
    cv.rect("front", 300, 340, 86, 30, "pale", 3)
    # coins
    for i in range(5):
        y = 392 - i * 20
        cv.path("top", f"M452 {y} a52 15 0 0 0 104 0 v-18 a52 15 0 0 0 -104 0 z", "yellow" if i % 2 else "orange")
        cv.line(f"M452 {y - 18} a52 15 0 0 0 104 0", 1.2, .5)
    cv.path("top", "M452 292 a52 15 0 0 0 104 0 a52 15 0 0 0 -104 0 z", "yellow")
    cv.text("top", 504, 298, "£", 18, "orange")
    cv.save("payroll")


def landlord():
    cv = Canvas(600, 450, .26)
    backdrop(cv, 40, 50, 520, 360, -2)
    # sky: plane on its way back to Hong Kong
    cv.line("M520 92 C 460 40, 360 46, 300 76", 2.6, .6, 'stroke-dasharray="2 10"')
    cv.path("top", "M300 70 l-40 12 l38 14 l-6 -12 z", "cream")
    cv.line("M300 70 l-40 12 l38 14 l-6 -12 z", 1.3, .7)
    # terraced house
    cv.path("bldg", "M128 160 L176 108 H380 L428 160 Z", "slate")
    for x in (196, 340):
        cv.rect("bldg", x, 78, 30, 40, "brick2")
        cv.rect("bldg", x + 4, 66, 9, 16, "orange", 2)
        cv.rect("bldg", x + 17, 66, 9, 16, "orange", 2)
    cv.rect("bldg", 140, 160, 276, 244, "brick")
    for r in range(10):
        cv.line(f"M144 {176 + r * 22} h268", 1, .16)
    cv.path("mid", "M160 250 h110 v134 h-110 z", "cream")         # bay window
    cv.path("mid", "M150 244 h130 v12 h-130 z", "pale")
    for x in (170, 206, 242):
        cv.rect("mid", x, 266, 24, 104, "water", 2)
    cv.line("M160 250 h110 v134 h-110 z", 1.6, .7)
    cv.rect("mid", 166, 176, 92, 52, "cream", 3)
    cv.rect("mid", 174, 184, 34, 36, "water", 2)
    cv.rect("mid", 216, 184, 34, 36, "water", 2)
    cv.path("mid", "M306 404 V262 A40 40 0 0 1 386 262 V404 Z", "purple")   # door
    cv.path("top", "M310 260 A36 36 0 0 1 382 260 Z", "yellow")
    cv.line("M346 226 V260 M318 246 L346 260 L374 246", 1.4, .7)
    cv.circle("top", 372, 334, 5, "yellow")
    cv.rect("mid", 300, 176, 92, 52, "cream", 3)
    cv.rect("mid", 308, 184, 34, 36, "water", 2)
    cv.rect("mid", 350, 184, 34, 36, "water", 2)
    cv.rect("front", 128, 404, 300, 14, "deep", 2)
    # TO LET board
    cv.rect("front", 470, 236, 10, 182, "deep", 2)
    cv.group("top", "rotate(-3 475 220)", f'<rect x="410" y="186" width="130" height="66" rx="6" fill="{c["yellow"]}"/>'
             f'<text x="475" y="230" font-family="Red Hat Mono, monospace" font-weight="700" font-size="26" fill="{c["purple"]}" text-anchor="middle">TO LET</text>')
    # key on a tag
    cv.group("top", "translate(26 10) rotate(-24 96 150)", f'<circle cx="96" cy="120" r="24" fill="{c["yellow"]}"/><circle cx="96" cy="120" r="9" fill="{c["pale"]}"/>'
             f'<rect x="90" y="140" width="12" height="74" rx="4" fill="{c["yellow"]}"/><rect x="102" y="186" width="16" height="9" fill="{c["yellow"]}"/><rect x="102" y="200" width="12" height="9" fill="{c["yellow"]}"/>'
             f'<rect x="58" y="76" width="44" height="26" rx="4" fill="{c["cream"]}"/>')
    cv.line("M112 108 L122 118", 1.4, .7)
    cv.save("landlord")


def stamp_duty():
    cv = Canvas(1000, 540, .34)
    cv.circle("sky", 330, 220, 150, "slate")
    # house front, right
    cv.path("bldg", "M600 128 L640 84 H960 V128 Z", "slate")
    cv.rect("bldg", 600, 128, 360, 340, "brick")
    for r in range(15):
        cv.line(f"M604 {146 + r * 22} h352", 1, .16)
    cv.path("mid", "M760 468 V250 A62 62 0 0 1 884 250 V468 Z", "purple")
    cv.path("top", "M766 248 A56 56 0 0 1 878 248 Z", "yellow")
    cv.line("M822 192 V248 M780 220 L822 248 L864 220", 1.6, .7)
    cv.rect("top", 806, 300, 32, 22, "cream", 3)
    cv.text("top", 822, 317, "24", 16, "purple")
    cv.circle("top", 862, 380, 7, "yellow")
    cv.rect("mid", 630, 196, 100, 150, "cream", 3)
    cv.rect("mid", 640, 206, 36, 130, "water", 2)
    cv.rect("mid", 684, 206, 36, 130, "water", 2)
    cv.rect("front", 740, 468, 164, 14, "cream", 2)
    cv.rect("front", 728, 482, 188, 14, "pale", 2)
    cv.rect("front", 580, 496, 400, 14, "deep", 2)
    # the SDLT receipt, curling
    zig = "".join("l-12 14 l-12 -14 " for _ in range(8))
    cv.group("mid", "rotate(-7 340 280)", f'<path d="M244 70 H436 V452 {zig} Z" fill="{c["cream"]}"/>'
             f'<text x="340" y="122" font-family="Red Hat Mono, monospace" font-weight="700" font-size="34" fill="{c["purple"]}" text-anchor="middle">SDLT</text>'
             f'<rect x="268" y="140" width="144" height="4" rx="2" fill="{c["lilac"]}"/>'
             + "".join(f'<rect x="268" y="{168 + i * 30}" width="{70 + (i % 3) * 14}" height="8" rx="4" fill="{c["lilac"]}"/><rect x="372" y="{168 + i * 30}" width="40" height="8" rx="4" fill="{c["lilac"]}"/>' for i in range(5))
             + f'<rect x="268" y="330" width="144" height="46" rx="5" fill="{c["purple"]}"/>'
             f'<text x="282" y="362" font-family="Red Hat Mono, monospace" font-weight="700" font-size="22" fill="{c["yellow"]}">£</text>'
             f'<rect x="306" y="347" width="92" height="12" rx="6" fill="{c["yellow"]}"/>')
    # big key in the foreground, with a W·Y fob
    key = (f'<path fill-rule="evenodd" d="M100 400 a66 66 0 1 0 132 0 a66 66 0 1 0 -132 0 z M140 400 a26 26 0 1 0 52 0 a26 26 0 1 0 -52 0 z" fill="{c["yellow"]}"/>'
           f'<rect x="226" y="386" width="330" height="28" rx="8" fill="{c["yellow"]}"/>'
           f'<path d="M480 414 h20 v30 h-20 z M516 414 h22 v44 h-22 z" fill="{c["yellow"]}"/>')
    cv.group("top", "rotate(-8 300 420)", key)
    cv.group("top", "rotate(14 120 470)", f'<rect x="70" y="440" width="96" height="58" rx="10" fill="{c["orange"]}"/>' + wy_mark(88, 450, .7, c["purple"], 0))
    cv.line("M120 446 L136 420", 2, .8)
    cv.save("stamp-duty")


def lost():
    cv = Canvas(600, 450, .24)
    backdrop(cv, 50, 60, 500, 330, 3)
    cv.path("sky", "M110 128 q14 -26 46 -14 q12 -24 44 -10 q32 0 30 26 q20 4 16 24 h-150 q-6 -20 14 -26z", "cream")
    cv.path("sky", "M380 300 q12 -22 38 -12 q10 -20 36 -8 q28 0 26 22 q16 4 14 20 h-126 q-4 -16 12 -22z", "lilac")
    cv.line("M120 330 C 160 200, 300 190, 330 250 S 260 360, 230 300 S 330 150, 450 150", 3, .7, 'stroke-dasharray="2 11"')
    cv.path("top", "M450 136 l58 20 l-56 22 l10 -18 z", "cream")
    cv.line("M450 136 l58 20 l-56 22 l10 -18 z M462 160 l46 -4", 1.4, .8)
    # torn boarding pass
    cv.group("top", "rotate(-10 200 330)", f'<path d="M140 300 h70 l-6 10 l8 10 l-6 10 l6 10 l-6 10 l6 8 h-72 z" fill="{c["cream"]}"/>'
             f'<rect x="140" y="300" width="18" height="58" rx="3" fill="{c["orange"]}"/>'
             f'<text x="184" y="336" font-family="Red Hat Mono, monospace" font-weight="700" font-size="16" fill="{c["purple"]}" text-anchor="middle">MAN</text>')
    cv.group("top", "rotate(12 270 350)", f'<path d="M240 330 l-6 10 l8 10 l-6 10 l6 10 l-6 10 l6 8 h64 v-58 z" fill="{c["cream"]}"/>'
             f'<text x="276" y="366" font-family="Red Hat Mono, monospace" font-weight="700" font-size="18" fill="{c["purple"]}" text-anchor="middle">404</text>')
    cv.save("lost")


if __name__ == "__main__":
    for f in (tax_return, company, payroll, landlord, stamp_duty, lost):
        f()
    print("ok")
