"""Shared paper-cut drawing kit for the Wong & Yip illustrations.
Each Canvas has named layers; every layer except 'ink' is one sheet of paper (texture + drop shadow)."""
import os

INK = "#22003f"
c = {"purple": "#360064", "deep": "#22003f", "yellow": "#ffe900", "orange": "#ff9b00", "cream": "#fbf6ec",
     "lilac": "#d9c9ea", "pale": "#ece4f4", "brick": "#e0662a", "brick2": "#c9531f", "water": "#b9c8ee",
     "green": "#7fbf8e", "slate": "#5b3f80"}
ORDER = ["back", "sky", "bldg", "mid", "front", "top", "ink"]
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "assets", "illo")


def filt(shadow=.32):
    return f'''<filter id="paper" x="-8%" y="-8%" width="116%" height="122%" color-interpolation-filters="sRGB">
  <feTurbulence type="fractalNoise" baseFrequency="1.15" numOctaves="2" seed="5" result="t"/>
  <feDiffuseLighting in="t" lighting-color="#ffffff" surfaceScale=".7" result="lit"><feDistantLight azimuth="235" elevation="68"/></feDiffuseLighting>
  <feComposite in="lit" in2="SourceAlpha" operator="in" result="tex"/>
  <feBlend in="SourceGraphic" in2="tex" mode="multiply" result="papered"/>
  <feComposite in="papered" in2="SourceAlpha" operator="in" result="cut"/>
  <feDropShadow in="cut" dx="3" dy="6" stdDeviation="4" flood-color="#22003f" flood-opacity="{shadow}"/>
</filter>'''


class Canvas:
    def __init__(self, w, h, shadow=.32):
        self.w, self.h, self.shadow, self.L = w, h, shadow, {}

    def add(self, layer, s):
        self.L.setdefault(layer, []).append(s)

    def rect(self, layer, x, y, w, h, fill, rx=0, extra=""):
        self.add(layer, f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{c.get(fill, fill)}" {extra}/>')

    def path(self, layer, d, fill, extra=""):
        self.add(layer, f'<path d="{d}" fill="{c.get(fill, fill)}" {extra}/>')

    def circle(self, layer, cx, cy, r, fill, extra=""):
        self.add(layer, f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c.get(fill, fill)}" {extra}/>')

    def text(self, layer, x, y, s, size, fill, font="mono", weight=700, anchor="middle", extra=""):
        fam = {"mono": "Red Hat Mono, monospace", "zh": "Chiron Hei HK, Noto Sans TC, sans-serif", "display": "Red Hat Display, sans-serif"}[font]
        self.add(layer, f'<text x="{x}" y="{y}" font-family="{fam}" font-weight="{weight}" font-size="{size}" fill="{c.get(fill, fill)}" text-anchor="{anchor}" {extra}>{s}</text>')

    def line(self, d, w=2, op=.85, extra=""):
        self.add("ink", f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" opacity="{op}" {extra}/>')

    def group(self, layer, transform, inner):
        self.add(layer, f'<g transform="{transform}">{inner}</g>')

    def svg(self):
        body = ""
        for name in ORDER:
            inner = "".join(self.L.get(name, []))
            if inner:
                body += f"<g>{inner}</g>" if name == "ink" else f'<g filter="url(#paper)">{inner}</g>'
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}">'
                f"<defs>{filt(self.shadow)}</defs>{body}</svg>")

    def save(self, name):
        os.makedirs(OUT, exist_ok=True)
        open(os.path.join(OUT, name + ".svg"), "w").write(self.svg())


def wy_mark(x, y, s, col="#ff9b00", rot=-6):
    """The W·Y chevron as a stamp impression."""
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" fill="{col}">'
            '<path d="M0 0h16l15 28 -8 14z"/><path d="M16 0h15l24 42v14h-15v-14z"/><path d="M31 28l16-28 8 14-24 42z" opacity=".85"/>'
            '<path d="M64 0h16l-24 42v-14z"/><path d="M80 0h16l-32 56-8-14z"/></g>')


def backdrop(cv, x, y, w, h, rot=-3, fill="pale"):
    cv.add("back", f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="56" fill="{c[fill]}" transform="rotate({rot} {x + w / 2} {y + h / 2})"/>')
