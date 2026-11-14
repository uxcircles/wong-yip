"""Self-hosted web fonts. Run after editing Chinese text (no dependencies):

    python3 _build/pages.py && python3 _build/fonts.py

- Red Hat Display (400-900), Red Hat Text (400-700), Red Hat Mono (400-700): Google's Latin subset
- Chiron Hei HK 400 and 800: only the Chinese characters used on the site (Google Fonts `text=`)
"""
import glob, html, os, re, urllib.parse, urllib.request

BUILD = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BUILD)
OUT = os.path.join(ROOT, "assets", "fonts")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
API = "https://fonts.googleapis.com/css2?"


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA})).read()


def latin_src(css):
    for comment, block in re.findall(r"/\* ([\w-]+) \*/\s*@font-face \{(.*?)\}", css, re.S):
        if comment == "latin":
            return re.search(r"url\((.*?)\)", block).group(1)
    raise SystemExit("latin block not found")


def save(name, data):
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, name + ".woff2"), "wb").write(data)
    print(f"{name}.woff2  {len(data) // 1024} KB")


def site_cjk():
    chars = set()
    files = glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True) + [os.path.join(ROOT, "assets", "site.js")]
    for f in files:
        chars.update(ch for ch in html.unescape(open(f, encoding="utf-8").read()) if ord(ch) > 0x2E7F)
    chars.update("，。：；！？（）「」、·…０１２３４５６７８９")
    return "".join(sorted(chars))


if __name__ == "__main__":
    save("redhat-display", get(latin_src(get(API + "family=Red+Hat+Display:wght@400..900&display=swap").decode())))
    save("redhat-text", get(latin_src(get(API + "family=Red+Hat+Text:wght@400..700&display=swap").decode())))
    save("redhat-mono", get(latin_src(get(API + "family=Red+Hat+Mono:wght@400..700&display=swap").decode())))
    text = site_cjk()
    for w in (400, 800):
        css = get(API + f"family=Chiron+Hei+HK:wght@{w}&display=swap&text=" + urllib.parse.quote(text)).decode()
        save(f"chiron-hei-hk-{w}", get(re.search(r"url\((.*?)\)", css).group(1)))
    print(len(text), "Chinese characters")
