"""Build the Wong & Yip concept site (no dependencies).

    python3 _build/pages.py && python3 _build/fonts.py

Traditional Chinese at /, English at /en/. Every string is written as L(english, chinese).
"""
import json
import os

BUILD = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BUILD)
V = "14"  # cache-bust: bump on every CSS/JS change

LANG = "zh"


def L(en, zh):
    return en if LANG == "en" else zh


# ------------------------------------------------------------------ facts
PHONE = "+44 7599 614875"
TEL = "+447599614875"
WA = "447599614875"
EMAIL = "info@wongyipaccountants.co.uk"
ADDR_EN = "Jactin House, 24 Hood Street, Ancoats, Manchester M4 6WX"
ADDR_ZH = "Jactin House, 24 Hood Street, Ancoats, Manchester M4 6WX"
OFFICIAL = "https://www.wongyipaccountants.co.uk/"
UXC = "https://ux-circles.com/professionals"
LAT, LNG = 53.4843944, -2.2279647
BASE = "https://uxcircles.github.io/wong-yip/"

ROUTES = json.load(open(os.path.join(BUILD, "routes.json")))
STATIONS = [
    ("Piccadilly Gardens", "Piccadilly Gardens", "畢架利花園電車站", "tram"),
    ("New Islington", "New Islington", "New Islington 電車站", "tram"),
    ("Piccadilly", "Manchester Piccadilly", "曼徹斯特 Piccadilly 火車站", "rail"),
]


# ------------------------------------------------------------------ shared pieces
def p(prefix, path):
    return prefix + path


PFX = ""


def chevron(cls=""):
    """The firm's own W·Y mark (yellow W, orange Y), used as the site's recurring device."""
    return f'<img class="chev {cls}" src="{PFX}assets/img/mark.png" width="400" height="238" alt="" aria-hidden="true">'


ALT = {
    "tax-return": ("Paper-cut illustration: a tax return form and a calendar showing 31 January", "剪紙插圖：一份報稅表和顯示 1 月 31 日的月曆"),
    "company": ("Paper-cut illustration: a small shopfront with an awning", "剪紙插圖：一間有簷篷的小店"),
    "payroll": ("Paper-cut illustration: a payslip coming out of an envelope and a stack of coins", "剪紙插圖：從信封抽出的糧單和一疊硬幣"),
    "landlord": ("Paper-cut illustration: a red-brick house with a TO LET board", "剪紙插圖：一間掛著 TO LET 牌的紅磚屋"),
    "lost": ("Paper-cut illustration: a paper plane, a cloud and a ticket reading 404", "剪紙插圖：一架紙飛機、一朵雲和寫著 404 的票"),
}


def spot(name, cls="spot"):
    """One of the paper-cut spot illustrations (4:3 WebP, 480 and 800 wide)."""
    en, zh = ALT[name]
    return (f'<img class="{cls}" src="{PFX}assets/img/{name}-480.webp" srcset="{PFX}assets/img/{name}-480.webp 480w, {PFX}assets/img/{name}-800.webp 800w" '
            f'sizes="(min-width: 761px) 340px, 90vw" width="480" height="360" loading="lazy" alt="{L(en, zh)}">')


def head(prefix, slug, title, desc):
    other = "en/" if LANG == "zh" else ""
    here_zh = BASE + slug
    here_en = BASE + "en/" + slug
    return f'''<!doctype html>
<html lang="{L('en-GB', 'zh-Hant-HK')}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="alternate" hreflang="zh-Hant" href="{here_zh}">
<link rel="alternate" hreflang="en" href="{here_en}">
<link rel="icon" type="image/png" href="{prefix}assets/img/favicon.png">
<link rel="apple-touch-icon" href="{prefix}assets/img/apple-touch-icon.png">
<meta name="theme-color" content="#360064">
<link rel="preload" href="{prefix}assets/fonts/redhat-display.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{prefix}assets/fonts/redhat-text.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{prefix}assets/site.css?v={V}">
<script defer src="{prefix}assets/site.js?v={V}"></script>
</head>
'''


def nav_items(prefix):
    return [
        ("services.html", L("Services", "服務")),
        ("stamp-duty.html", L("Stamp Duty", "印花稅")),
        ("about.html", L("About", "關於我們")),
        ("index.html#contact", L("Contact", "聯絡")),
    ]


def header(prefix, slug):
    sw_href = ("../" if LANG == "en" else "en/") + slug.replace("index.html", "")
    if slug == "404.html":
        sw_href = prefix + "en/"
    sw_label = L("中文", "English")
    sw_lang = L("zh-Hant", "en")
    links = "".join(
        f'<a href="{prefix}{h}"{" aria-current=page" if h == slug else ""}>{t}</a>' for h, t in nav_items(prefix)
    )
    return f'''<body>
<a class="skip" href="#main">{L("Skip to content", "跳至內容")}</a>
<div class="concept" role="note">
  <div class="wrap concept-in">
    <p><span class="concept-tag">{L("Concept", "概念")}</span><span class="concept-long">{L('Redesign concept. Not the official <a href="' + OFFICIAL + '">Wong &amp; Yip Accountants</a> website.', '重新設計概念，並非 <a href="' + OFFICIAL + '">曼城黃葉會計師樓</a> 官方網站。')}</span></p>
    <a class="concept-by" href="{UXC}"><span class="concept-by-txt">Designed by </span>UX CIRCLES ↗</a>
  </div>
</div>
<header class="site-head" id="top">
  <div class="wrap head-in">
    <a class="brand" href="{prefix}index.html" aria-label="{L('Wong &amp; Yip Accountants, home', '曼城黃葉會計師樓 首頁')}">
      <img src="{prefix}assets/img/logo.png" width="1000" height="205" alt="Wong &amp; Yip Accountants Limited">
      <span class="brand-zh" lang="zh-Hant">曼城黃葉（香港）會計師樓</span>
    </a>
    <nav class="nav" aria-label="{L('Main', '主選單')}">{links}</nav>
    <a class="lang" href="{sw_href}" lang="{sw_lang}" hreflang="{sw_lang}">{sw_label}</a>
    <a class="head-call" href="tel:{TEL}">{PHONE}</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu">{L('Menu', '選單')}</button>
  </div>
  <div class="menu" id="menu" hidden>
    <nav class="wrap" aria-label="{L('Menu', '選單')}">
      {links}
      <a href="{sw_href}" lang="{sw_lang}">{sw_label}</a>
      <a href="tel:{TEL}">{L('Call', '致電')} {PHONE}</a>
      <a href="https://wa.me/{WA}">WhatsApp</a>
    </nav>
  </div>
</header>
'''


def footer(prefix, slug):
    sw_href = ("../" if LANG == "en" else "en/") + slug.replace("index.html", "")
    if slug == "404.html":
        sw_href = prefix + "en/"
    return f'''<footer class="foot">
  <div class="wrap foot-grid">
    <div>
      {chevron("foot-chev")}
      <p class="foot-name">Wong &amp; Yip Accountants Ltd<br><span lang="zh-Hant">曼城黃葉（香港）會計師樓</span></p>
      <p>{ADDR_EN}</p>
    </div>
    <div>
      <p><a href="tel:{TEL}">{PHONE}</a> · {L('phone and WhatsApp', '電話及 WhatsApp')}</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p><a href="https://www.facebook.com/wongyipaccountants">Facebook</a></p>
    </div>
    <div>
      <p><a href="{prefix}services.html">{L('Services', '服務')}</a> · <a href="{prefix}stamp-duty.html">{L('Stamp Duty', '印花稅')}</a> · <a href="{prefix}about.html">{L('About', '關於我們')}</a></p>
      <p><a href="{prefix}privacy.html">{L('Privacy and accessibility', '私隱及無障礙')}</a> · <a href="{sw_href}" lang="{L('zh-Hant', 'en')}">{L('中文', 'English')}</a></p>
      <p class="foot-small">{L('Tools on this site give estimates, not tax advice. Rates for England and Northern Ireland, checked against GOV.UK in November 2026.', '本網站的計算工具只提供估算，並非稅務意見。稅率適用於英格蘭及北愛爾蘭，已於 2026 年 11 月按 GOV.UK 核對。')}</p>
      <p class="foot-small">Unofficial redesign concept by <a href="{UXC}">UX CIRCLES</a></p>
    </div>
  </div>
</footer>
<nav class="mbar" aria-label="{L('Quick actions', '快捷操作')}">
  <a href="tel:{TEL}">{L('Call', '致電')}</a>
  <a href="https://wa.me/{WA}">WhatsApp</a>
  <a href="mailto:{EMAIL}">{L('Email', '電郵')}</a>
</nav>
</body>
</html>
'''


def page(prefix, slug, title, desc, body):
    global PFX
    PFX = prefix
    return head(prefix, slug, title, desc) + header(prefix, slug) + f'<main id="main">{body}</main>\n' + footer(prefix, slug)


# ------------------------------------------------------------------ the stamp duty tool
def sdlt_tool(full=False):
    hid = "sdlt-full" if full else "sdlt"
    return f'''<form class="tool" id="{hid}" data-sdlt novalidate>
  <div class="tool-in">
    <label class="price">
      <span class="lbl">{L('Purchase price', '樓價')}</span>
      <span class="price-box"><span aria-hidden="true">£</span><input name="price" inputmode="numeric" autocomplete="off" value="300,000" aria-describedby="{hid}-scope"></span>
    </label>
    <fieldset class="seg">
      <legend class="lbl">{L('After buying, you will own', '買入後，你名下')}</legend>
      <label><input type="radio" name="type" value="ftb"><span>{L('My first home ever', '首次置業<small>從未在任何地方擁有物業</small>')}</span></label>
      <label><input type="radio" name="type" value="home" checked><span>{L('Only this home', '只有這一個物業<small>例如已賣出香港的樓</small>')}</span></label>
      <label><input type="radio" name="type" value="add"><span>{L('More than one home', '多於一個物業<small>例如保留香港的樓</small>')}</span></label>
    </fieldset>
    <label class="check"><input type="checkbox" name="nonres"><span>{L('I have spent fewer than 183 days in the UK in the 12 months before buying (non-UK resident, +2%)', '購買前 12 個月內在英國少於 183 日（非英國居民，+2%）')}</span></label>
  </div>
  <output class="receipt" aria-live="polite" for="{hid}">
    <span class="r-total"><span>{L('Stamp Duty to pay', '應繳印花稅')}</span><b data-total>£0</b></span>
    <span class="r-eff" data-eff></span>
    <table><caption class="vh">{L('Tax by band', '各級稅款')}</caption><tbody data-rows></tbody></table>
    <span class="r-notes" data-notes></span>
  </output>
  <p class="tool-scope" id="{hid}-scope">{L('Residential rates from 1 April 2025, England and Northern Ireland. An estimate, not advice.', '2025 年 4 月 1 日起英格蘭及北愛爾蘭住宅稅率。只供估算，並非稅務意見。')}</p>
</form>'''


# ------------------------------------------------------------------ content
def SERVICES_():
    return [
    ("personal", L("For you", "個人"), [
        ("tax", L("Personal tax management", "個人稅務管理"),
         L("The UK taxes residents on worldwide income, so rent from a flat in Hong Kong belongs on your UK return. We look after your HMRC personal tax account, tax codes and refunds, and file for you if you live overseas and cannot use HMRC online services.",
           "英國按全球收入向稅務居民徵稅，香港物業的租金收入也要在英國申報。我們替你處理 HMRC 個人稅務帳戶、稅碼及退稅；如你身在海外、無法使用 HMRC 網上服務，我們可代你報稅。")),
        ("sa", L("Self Assessment", "自我評估報稅"),
         L("Self-employed, landlords, partners, company directors and anyone with income HMRC has not already taxed. We prepare and file your SA100, work out what is due by 31 January, and check whether Making Tax Digital applies to you.",
           "自僱人士、業主、合夥人、公司董事，以及有未經扣稅收入的人士都要報稅。我們為你準備及遞交 SA100，計算 1 月 31 日前要繳的稅款，並檢查你是否需要遵守 Making Tax Digital。")),
        ("cross", L("Cross-border tax, UK and Hong Kong", "英港跨境稅務"),
         L("Residence under the Statutory Residence Test, double tax relief between the UK and Hong Kong, and accounting around a move to the UK.",
           "按法定居住測試（SRT）判斷稅務居民身份、英港雙重課稅寬免，以及移居英國前後的會計及財富安排。")),
    ]),
    ("business", L("For your business", "公司"), [
        ("setup", L("UK business set-up", "英國業務設立"),
         L("Choosing between sole trader, limited company and LLP; registering with Companies House; company secretarial work, registered office and confirmation statements.",
           "比較個體經營、有限公司及 LLP，向公司註冊處註冊；公司秘書、註冊辦公室地址及年度確認聲明。")),
        ("books", L("Bookkeeping and accounts", "簿記與會計"),
         L("Bookkeeping, management accounts and year-end financial statements under UK GAAP or IFRS.",
           "簿記、管理賬目，以及符合 UK GAAP 或 IFRS 的年度財務報表。")),
        ("ct", L("Corporation Tax", "公司所得稅"),
         L("CT600 returns and the reliefs that reduce the bill: capital allowances, the Annual Investment Allowance, losses, R&D and creative sector reliefs. Main rate 25%, small profits rate 19% up to £50,000.",
           "遞交 CT600，並申請可減稅的寬免：資本免稅額、年度投資免稅額（AIA）、虧損抵銷、研發及創意產業寬免。主要稅率 25%，利潤 £50,000 或以下為 19%。")),
        ("payroll", L("Payroll and PAYE", "計糧及 PAYE"),
         L("Registering as an employer, running payroll, RTI submissions, payslips, P60s and workplace pensions, so tax reaches HMRC by the 22nd.",
           "登記成為僱主、計算工資、RTI 申報、糧單、P60 及職場退休金，確保每月 22 日前把稅款交到 HMRC。")),
        ("vat", L("VAT", "增值稅 VAT"),
         L("Registration once taxable turnover passes £90,000, quarterly returns under Making Tax Digital, VAT planning and HMRC enquiries.",
           "應課稅營業額超過 £90,000 時登記，按 Making Tax Digital 遞交季度申報，增值稅規劃及應對 HMRC 查詢。")),
        ("outsourced", L("Outsourced accounting", "外判會計"),
         L("Your finance team without the hiring: billed by the hour, monthly or per service, or a mix.",
           "不必自組會計團隊：可按小時、月費或服務項目收費，亦可混合配搭。")),
        ("ecom", L("E-commerce accounting", "跨境電商會計"),
         L("Amazon, eBay, Shopify and TikTok Shop sellers: marketplace VAT, multi-currency payouts and stock.",
           "Amazon、eBay、Shopify 及 TikTok Shop 賣家：平台增值稅、多種貨幣收款及存貨。")),
    ]),
    ("property", L("For your property", "物業"), [
        ("sdlt", L("Stamp Duty analysis and refunds", "印花稅分析及退稅"),
         L("What you will pay before you offer, whether first-time buyer relief applies to you, and claims to get the 2% non-resident surcharge or the 5% higher rates back.",
           "出價前計清楚要交多少，判斷你是否符合首次置業寬減，以及申請退回 2% 非居民附加費或 5% 額外物業附加部分。")),
        ("nrl", L("Overseas landlords", "海外業主稅"),
         L("Registering for the Non-Resident Landlord Scheme, rental accounts, allowable expenses and losses, and your annual return to HMRC from abroad.",
           "登記非居民業主計劃（NRLS）、租金記賬、可扣除開支及虧損結轉，並代你每年向 HMRC 申報。")),
    ]),
    ]


def INDUSTRIES_():
    return [
    L("Takeaways and restaurants", "外賣店及餐廳"),
    L("Chinese medicine practitioners", "中醫診所"),
    L("Sourcing and trading agents", "採購及貿易代理"),
    L("Amazon, eBay and Shopify sellers", "Amazon、eBay、Shopify 賣家"),
    L("Law firms", "律師行"),
    L("Telecoms and education agents", "電訊及升學代理"),
    L("Construction and engineering", "建築及工程"),
    L("Printing and IT", "印刷及資訊科技"),
    L("Landlords", "業主"),
    L("Taxi drivers", "的士司機"),
    L("Investors", "投資者"),
    L("Translators", "翻譯"),
    ]

QUOTES = [
    ("Was being a while, I learnt Wong & Yip from my friend, they are very helpful, know my real concern, and give me solutions with some bright ideas. I highly recommend WY to everyone.",
     "有一段時間，我從我的朋友那裡了解到Wong & Yip，他們非常樂於助人，知道我真正關心的問題，並給我一些好的解決方案。我向大家強烈推薦WY。", "Eric Ng"),
    ("For nearly 30 years, we have benefited from first-class, bespoke payroll and business advisory services from Wong & Yip Accountants. Their combination of skill, efficiency, and professionalism, while remaining approachable, makes them an integral part of our team.", None, "Alex, UKTesla"),
    ("Wong & Yip Accountants is the most trustworthy firm. They are highly competent and always put my business interests first.", None, "Sam Leung, Nougart"),
    ("Since moving our business to Wong & Yip Accountants, I’ve been impressed by their professionalism, friendly attitude, efficiency, and the consistently high standard of advice and service.", None, "Chris, Wakuwaku Japan"),
    ("Wong & Yip Accountants took the time to truly understand our business from the inside. Their recommendations proved invaluable, transforming the way we work.", None, "Kurl, Interpropset"),
    ("Wong & Yip Accountants are proactive and supportive in every new business venture, enabling me to make informed commercial decisions with confidence.", None, "Tracy, Woodland International"),
]


def contact_section(prefix):
    stations = "".join(
        f'<li><b>{ROUTES[k]["min"]} {L("min", "分鐘")}</b> {L(en, zh)}</li>' for k, en, zh, _ in STATIONS
    )
    mapdata = {
        "home": [LNG, LAT],
        "routes": [
            {"name": L(en, zh), "min": ROUTES[k]["min"], "kind": kind, "start": ROUTES[k]["start"], "coords": ROUTES[k]["coords"]}
            for k, en, zh, kind in STATIONS
        ],
        "label": L("Wong & Yip", "曼城黃葉"),
        "mark": prefix + "assets/img/mark.png",
    }
    opts = "".join(f"<option>{t}</option>" for _, _, items in SERVICES_() for _, t, _ in items)
    return f'''<section class="contact" id="contact" aria-labelledby="contact-h">
  <div class="wrap contact-grid">
    <div class="contact-text">
      <h2 id="contact-h">{L('Hood Street, Ancoats', '安科茨 Hood Street')}</h2>
      <p class="addr">{ADDR_EN}</p>
      <ul class="walks">{stations}</ul>
      <p class="walk-note">{L('Walking times from OpenStreetMap routes.', '步行時間按 OpenStreetMap 路線計算。')}</p>
      <p class="big-links"><a href="tel:{TEL}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div class="map" data-map data-src="{prefix}assets/vendor/maplibre/maplibre-gl.js" data-css="{prefix}assets/vendor/maplibre/maplibre-gl.css" data-mapjs="{prefix}assets/map.js?v={V}">
      <div class="map-fallback" aria-hidden="true">{chevron("pin-chev")}<span>Jactin House</span></div>
      <script type="application/json" id="map-data">{json.dumps(mapdata, ensure_ascii=False)}</script>
    </div>
  </div>
  <div class="wrap">
    <form class="ask" data-ask novalidate>
      <h3>{L('Send us your question', '留下你的問題')}</h3>
      <div class="ask-grid">
        <label>{L('Your name', '你的名字')}<input name="name" autocomplete="name" required></label>
        <label>{L('Phone or email', '電話或電郵')}<input name="reach" autocomplete="tel" required></label>
        <label>{L('About', '查詢服務')}<select name="topic">{opts}</select></label>
        <label class="wide">{L('Your question', '你的問題')}<textarea name="msg" rows="3" required>{L('Hello, I have a tax question and would like you to contact me.', '你好，我有稅務問題想查詢，請聯絡我。')}</textarea></label>
      </div>
      <p class="ask-err" data-err hidden>{L('Please fill in your name, how to reach you and your question.', '請填寫名字、聯絡方法及問題。')}</p>
      <div class="ask-btns">
        <button type="submit" name="via" value="wa">{L('Send on WhatsApp', '用 WhatsApp 發送')}</button>
        <button type="submit" name="via" value="mail" class="ghost">{L('Send by email', '用電郵發送')}</button>
      </div>
      <p class="ask-note">{L('This opens WhatsApp or your email app with your message filled in. Nothing is stored on this website.', '按下後會開啟 WhatsApp 或電郵程式，並已填好你的訊息。本網站不會儲存任何資料。')}</p>
    </form>
  </div>
</section>'''


def home(prefix):
    groups = ""
    for gid, gname, items in SERVICES_():
        lis = "".join(f'<li><a href="{prefix}services.html#{sid}">{t}</a></li>' for sid, t, _ in items)
        art = {"personal": "tax-return", "business": "company", "property": "landlord"}[gid]
        groups += f'<div class="svc-col">{spot(art)}<h3>{gname}</h3><ul>{lis}</ul></div>'
    inds = "".join(f"<li>{i}</li>" for i in INDUSTRIES_())
    q0 = QUOTES[0]
    quotes = f'<figure class="q q-main"><blockquote lang="{L("en", "zh-Hant")}">{L(q0[0], q0[1])}</blockquote><figcaption>{q0[2]}</figcaption></figure>'
    quotes += "".join(f'<figure class="q"><blockquote lang="en">{a}</blockquote><figcaption>{c}</figcaption></figure>' for a, _, c in QUOTES[1:])
    body = f'''
<section class="hero hero-home" aria-labelledby="hero-h">
  <div class="wrap hero-in">
    <h1 id="hero-h">{L('Know your stamp duty before you make an offer', '買樓之前，先計清楚印花稅')}</h1>
    <figure class="hero-illo">
      <img src="{prefix}assets/img/hk-to-manchester-1000.webp" srcset="{prefix}assets/img/hk-to-manchester-640.webp 640w, {prefix}assets/img/hk-to-manchester-1000.webp 1000w, {prefix}assets/img/hk-to-manchester-1600.webp 1600w" sizes="(min-width: 1021px) 560px, 100vw" width="1000" height="540" alt="{L('Paper-cut illustration: a Hong Kong tenement block, a paper plane, and a red-brick Ancoats cotton mill beside the Rochdale Canal.', '剪紙插圖：香港唐樓、一架紙飛機，以及 Rochdale 運河旁的 Ancoats 紅磚紡織廠。')}" fetchpriority="low">
    </figure>
    {sdlt_tool()}
    <p class="hero-foot">{L('Wong &amp; Yip Accountants, Manchester. ACCA and HKICPA accountants who speak English, Cantonese and Mandarin.', '曼城黃葉會計師樓：ACCA 及 HKICPA 會計師，以英語、廣東話及普通話服務。')} <a href="{prefix}stamp-duty.html">{L('How it is worked out', '計算方法及退稅')}</a></p>
  </div>
</section>

<section class="dates" aria-labelledby="dates-h">
  <div class="wrap">
    <h2 id="dates-h">{L('Next HMRC dates', '接下來的 HMRC 日子')}</h2>
    <ol class="date-stack" data-deadlines aria-live="polite"></ol>
    <p class="dates-note">{L('Counted from today’s date in London. Making Tax Digital quarterly updates apply from April 2026 to sole traders and landlords with qualifying income over £50,000, and over £30,000 from April 2027.', '按倫敦今天的日期計算。Making Tax Digital 季度申報：2026 年 4 月起適用於合資格收入超過 £50,000 的自僱人士及業主，2027 年 4 月起門檻降至 £30,000。')}</p>
  </div>
</section>

<section class="svc" aria-labelledby="svc-h">
  <div class="wrap">
    <h2 id="svc-h">{L('What we do', '我們的服務')}</h2>
    <div class="svc-grid">{groups}</div>
    <p><a class="more" href="{prefix}services.html">{L('All services in detail', '詳細服務內容')}</a></p>
  </div>
</section>

<section class="inds" aria-labelledby="inds-h">
  <div class="wrap">
    <h2 id="inds-h">{L('Clients with turnover from £20,000 to £5 million', '客戶營業額由 £20,000 至 £500 萬')}</h2>
    <ul class="ind-list">{inds}</ul>
    <p class="inds-note">{L('We also work alongside law firms, immigration advisers and asset managers.', '我們亦與律師行、移民顧問及資產管理公司緊密合作。')}</p>
  </div>
</section>

<section class="who" aria-labelledby="who-h">
  <div class="wrap who-grid">
    <div>
      <h2 id="who-h">Henry Yip <span class="creds">BA, FCCA, HKICPA</span></h2>
      <p>{L('Henry leads the firm. He is known for non-UK domicile taxation and has helped hundreds of clients with their UK and international business.', 'Henry 帶領本所，專長於非英國居籍（non-dom）稅務，曾協助數以百計客戶在英國及海外發展業務。')}</p>
      <p>{L('The team is made up of ACCA chartered certified accountants practising in the UK and HKICPA certified public accountants from Hong Kong, with more than 30 years of practice between them.', '團隊由英國執業的 ACCA 特許公認會計師及香港 HKICPA 註冊會計師組成，累積超過 30 年執業經驗。')}</p>
      <p><a class="more" href="{prefix}about.html">{L('About the firm', '關於本所')}</a></p>
    </div>
    <dl class="facts">
      <div><dt>{L('Languages', '語言')}</dt><dd>English · <span lang="yue-Hant">廣東話</span> · <span lang="zh-Hant">普通話</span></dd></div>
      <div><dt>{L('Qualified in', '執業資格')}</dt><dd>{L('UK and Hong Kong', '英國及香港')}</dd></div>
      <div><dt>{L('Membership', '會籍')}</dt><dd>{L('Member and Fellow of ACCA', 'ACCA 會員及資深會員')}</dd></div>
      <div><dt>{L('Recognition', '肯定')}</dt><dd>{L('Nominated for the E-commerce Agent Awards', '獲提名 E-commerce Agent Awards')}</dd></div>
    </dl>
  </div>
</section>

<section class="quotes" aria-labelledby="q-h">
  <div class="wrap">
    <h2 id="q-h">{L('What clients say', '客戶怎樣說')}</h2>
    <div class="q-row">{quotes}</div>
  </div>
</section>
{contact_section(prefix)}
'''
    return page(prefix, "index.html",
                L("Wong & Yip Accountants, Manchester · Stamp Duty, tax and accounts", "曼城黃葉（香港）會計師樓 · 印花稅、報稅及會計"),
                L("ACCA and HKICPA accountants in Ancoats, Manchester. Work out your Stamp Duty, see the next HMRC dates, and talk to us in English, Cantonese or Mandarin.",
                  "位於曼徹斯特 Ancoats 的 ACCA 及 HKICPA 會計師。計算印花稅、查看 HMRC 日子，以英語、廣東話或普通話與我們傾談。"),
                body)


def services(prefix):
    out = ""
    for gid, gname, items in SERVICES_():
        cards = "".join(
            f'<article class="svc-item" id="{sid}"><h3>{t}</h3><p>{d}</p></article>' for sid, t, d in items
        )
        arts = {"personal": ["tax-return"], "business": ["company", "payroll"], "property": ["landlord"]}[gid]
        out += f'<section class="svc-group" aria-labelledby="g-{gid}"><div class="svc-side"><h2 id="g-{gid}">{gname}</h2>{"".join(spot(a) for a in arts)}</div><div class="svc-items">{cards}</div></section>'
    body = f'''
<section class="page-head">
  {chevron("hero-chev")}
  <div class="wrap"><h1>{L('Services', '服務')}</h1>
  <p class="lede">{L('Ten services in three groups, the same way our clients arrive: with a personal tax question, a business to run, or a property to buy or let.', '十項服務分為三類，正如客戶來找我們的原因：個人稅務問題、要打理的生意，或者要買入或出租的物業。')}</p></div>
</section>
<div class="wrap svc-page">{out}
<p class="fees">{L('Fees depend on the type and size of your business, turnover and what you need. Ask us for a quote: hourly, monthly or per service.', '收費視乎公司類型及規模、營業額及所需服務而定，可按小時、月費或服務項目計算。歡迎查詢報價。')} <a href="#contact">{L('Ask for a quote', '索取報價')}</a></p>
</div>
{contact_section(prefix)}
'''
    return page(prefix, "services.html", L("Services · Wong & Yip Accountants", "服務 · 曼城黃葉會計師樓"),
                L("Personal tax, Self Assessment, company accounts, payroll, VAT, Stamp Duty and overseas landlord tax in Manchester.",
                  "個人稅務、自我評估、公司賬目、計糧、增值稅、印花稅及海外業主稅。"), body)


def rate_table(rows, cap):
    trs = "".join(f"<tr><th scope=row>{a}</th><td>{b}</td></tr>" for a, b in rows)
    return f'<table class="rates"><caption>{cap}</caption><thead><tr><th scope=col>{L("Portion of the price", "樓價部分")}</th><th scope=col>{L("Rate", "稅率")}</th></tr></thead><tbody>{trs}</tbody></table>'


def stamp(prefix):
    std = [("£0 – £125,000", "0%"), ("£125,001 – £250,000", "2%"), ("£250,001 – £925,000", "5%"), ("£925,001 – £1.5m", "10%"), (L("Over £1.5m", "£1.5m 以上"), "12%")]
    ftb = [("£0 – £300,000", "0%"), ("£300,001 – £500,000", "5%"), (L("Price over £500,000", "樓價超過 £500,000"), L("No relief: standard rates", "不設寬減，按一般稅率"))]
    body = f'''
<section class="hero hero-sub hero-home" aria-labelledby="hero-h">
  <div class="wrap hero-in">
    <h1 id="hero-h">{L('Stamp Duty for people moving from Hong Kong', '由香港來英買樓的印花稅')}</h1>
    <figure class="hero-illo">
      <img src="{prefix}assets/img/stamp-duty-1000.webp" srcset="{prefix}assets/img/stamp-duty-640.webp 640w, {prefix}assets/img/stamp-duty-1000.webp 1000w, {prefix}assets/img/stamp-duty-1600.webp 1600w" sizes="(min-width: 1021px) 560px, 100vw" width="1000" height="540" alt="{L('Paper-cut illustration: a Stamp Duty (SDLT) receipt and a large key', '剪紙插圖：一張印花稅（SDLT）收據和一條大鎖匙')}">
    </figure>
    {sdlt_tool(full=True)}
  </div>
</section>
<div class="wrap prose">
  <section aria-labelledby="s1">
    <h2 id="s1">{L('What changed on 1 April 2025', '2025 年 4 月 1 日的改變')}</h2>
    <p>{L('The temporary thresholds from September 2022 ended. Stamp Duty now starts at £125,000 instead of £250,000, and first-time buyers pay nothing only up to £300,000 instead of £425,000. A £300,000 home that cost £2,500 in Stamp Duty under the old rates now costs £5,000.', '2022 年 9 月起的臨時門檻已經結束。印花稅起徵點由 £250,000 回落至 £125,000；首次置業免稅上限由 £425,000 降至 £300,000。以 £300,000 物業為例，舊稅率下印花稅為 £2,500，現在是 £5,000。')}</p>
    <div class="tables">{rate_table(std, L('Standard residential rates', '一般住宅稅率'))}{rate_table(ftb, L('First-time buyer relief', '首次置業寬減'))}</div>
    <p>{L('Add 5% to every band if you will own more than one home, and 2% if you are not UK resident for Stamp Duty purposes. Purchases under £40,000 do not pay the higher rates.', '如買入後擁有多於一個住宅，每一級加 5%；如你在印花稅方面屬非英國居民，再加 2%。樓價低於 £40,000 不須付額外物業附加。')}</p>
  </section>
  <section aria-labelledby="s2">
    <h2 id="s2">{L('Questions we are asked most', '最常被問的問題')}</h2>
    <details><summary>{L('I sold my flat in Hong Kong before moving. Am I a first-time buyer?', '移英前已賣出香港的樓，算是首次置業嗎？')}</summary><p>{L('No. First-time buyer relief is only for people who have never owned a home anywhere in the world. You pay the standard rates, but not the 5% higher rates, because this will be your only home.', '不算。首次置業寬減只適用於從未在世界任何地方擁有住宅的人。你要按一般稅率繳付，但因為這將是你唯一的物業，所以不用付 5% 額外物業附加。')}</p></details>
    <details><summary>{L('I kept my flat in Hong Kong. Does that matter?', '我保留了香港的樓，有影響嗎？')}</summary><p>{L('Yes. Homes you own outside the UK count, so buying in the UK means you own more than one and usually pay the 5% higher rates on top.', '有。在英國以外擁有的住宅也會計算在內，所以在英國再買樓，一般要額外付 5%。')}</p></details>
    <details><summary>{L('Can I get the 2% non-resident surcharge back?', '2% 非居民附加費可以退回嗎？')}</summary><p>{L('Often, yes. If you spend at least 183 days in the UK in a continuous 365-day period that falls in the year before or after your purchase, you can claim it back from HMRC. Claims have time limits, so talk to us when you buy.', '很多時可以。如你在購買前後的一段 365 日期間內在英國逗留滿 183 日，便可向 HMRC 申請退回。申請有時限，建議買樓時便與我們商量。')}</p></details>
    <details><summary>{L('I paid the 5% higher rates because my old home had not sold yet. Can I claim it back?', '舊居未賣出，付了 5% 附加，可以退回嗎？')}</summary><p>{L('Yes, if the new home replaces your main residence and you sell the old one within 36 months of buying the new one.', '可以，條件是新物業取代你的主要住所，並在購入新物業後 36 個月內賣出舊居。')}</p></details>
    <details><summary>{L('Who pays it, and when?', '誰繳交？何時繳交？')}</summary><p>{L('The return and payment are due within 14 days of completion. Your solicitor or conveyancer usually files it and adds the tax to their bill.', '須在成交後 14 日內遞交申報表及繳稅，一般由你的律師或產權轉讓師代辦，稅款會加在他們的收費上。')}</p></details>
  </section>
  <section aria-labelledby="s3" id="landlords">
    <h2 id="s3">{L('Letting it out from abroad', '身在海外出租物業')}</h2>
    <p>{L('If you live outside the UK and let out a UK property, the rent is still taxable here. Without approval from HMRC, your letting agent or tenant must take basic-rate tax off the rent. We register you for the Non-Resident Landlord Scheme so you can receive rent in full, keep the rental accounts, claim allowable expenses and losses, and file your return each year.', '即使你住在英國以外，英國物業的租金仍須在英國課稅。未經 HMRC 批准，代理或租客須先從租金中預扣基本稅率的稅款。我們為你登記非居民業主計劃（NRLS），讓你收取全額租金，並處理租金記賬、可扣除開支及虧損，每年代你申報。')}</p>
    <p><a class="more" href="#contact">{L('Ask about your property', '查詢你的物業')}</a></p>
  </section>
  <p class="src">{L('Sources: GOV.UK, Stamp Duty Land Tax residential property rates; non-UK resident surcharge; higher rates for additional dwellings. Scotland and Wales have their own taxes.', '資料來源：GOV.UK 印花稅住宅稅率、非英國居民附加費及額外住宅稅率。蘇格蘭及威爾斯另有不同稅項。')}</p>
</div>
{contact_section(prefix)}
'''
    return page(prefix, "stamp-duty.html", L("Stamp Duty calculator · Wong & Yip Accountants", "印花稅計算 · 曼城黃葉會計師樓"),
                L("Stamp Duty from 1 April 2025 for first-time buyers, people who kept a home in Hong Kong and non-UK residents, with refunds explained.",
                  "2025 年 4 月 1 日起的印花稅：首次置業、保留香港物業及非英國居民，並解釋如何退稅。"), body)


def about(prefix):
    why = [
        (L("Three languages", "三種語言"), L("English, and accountants whose first language is Cantonese or Mandarin, all ACCA qualified.", "英語，以及以廣東話或普通話為母語的 ACCA 會計師。")),
        (L("Two systems", "兩地制度"), L("UK and Hong Kong practice under one roof, which matters most for people with income, property or a company in both.", "英國及香港的執業經驗集於一身，對在兩地都有收入、物業或公司的客戶尤其重要。")),
        (L("Clients first", "客戶至上"), L("That is the firm’s own phrase. Every arrangement is set up around the client’s business.", "這是本所的理念，每項安排都按客戶的業務度身訂造。")),
        (L("One place for everything", "一站式"), L("From UK tax compliance to cross-border e-commerce, with law firms, immigration advisers and asset managers we work with.", "由英國稅務合規到跨境電商，並與律師行、移民顧問及資產管理公司合作。")),
    ]
    whys = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in why)
    body = f'''
<section class="page-head">
  {chevron("hero-chev")}
  <div class="wrap"><h1>{L('About Wong &amp; Yip', '關於曼城黃葉')}</h1>
  <p class="lede">{L('A Manchester firm of chartered certified accountants with more than 30 years of practice, whose team qualified in both the UK and Hong Kong.', '曼徹斯特的特許公認會計師事務所，超過 30 年執業經驗，團隊同時具備英國及香港的專業資格。')}</p></div>
</section>
<div class="wrap prose">
  <section aria-labelledby="a1">
    <h2 id="a1">{L('Who we work for', '我們服務的對象')}</h2>
    <p>{L('Hong Kong people, families and businesses who have moved to the UK; UK residents with business abroad; and companies from start-ups to multi-million-pound turnover. Our mission is to be the most professional, reliable and trusted accounting practice for them.', '移居英國的香港人士、家庭及企業；在海外有業務的英國居民；以及由初創到營業額數百萬英鎊的公司。我們的使命，是成為他們最專業、最可靠、最值得信賴的會計師事務所。')}</p>
  </section>
  <dl class="why">{whys}</dl>
  <section aria-labelledby="a2">
    <h2 id="a2">Henry Yip <span class="creds">BA, FCCA, HKICPA</span></h2>
    <p>{L('Henry Yip is recognised as one of the UK’s leading experts in non-UK domicile taxation. With an entrepreneurial and commercial mindset, he has helped hundreds of clients succeed in their UK and international business ventures.', 'Henry Yip 被視為英國非居籍（non-dom）稅務方面的專家之一。他具創業及商業觸覺，曾協助數以百計客戶在英國及海外發展業務。')}</p>
  </section>
  <section aria-labelledby="a3">
    <h2 id="a3">{L('Core work', '核心工作')}</h2>
    <ul class="ticks">
      <li>{L('Accounting and bookkeeping under UK GAAP and IFRS', '會計及簿記（UK GAAP、IFRS）')}</li>
      <li>{L('UK tax returns: SA100, SA800 partnership, CT600, VAT, PAYE and SDLT', '英國稅務申報：個人 SA100、合夥 SA800、公司 CT600、VAT、PAYE 及印花稅 SDLT')}</li>
      <li>{L('Company formation in the UK and Hong Kong', '英國及香港公司註冊及商業顧問')}</li>
      <li>{L('Cross-border tax and double tax relief between the UK and Hong Kong', '英港跨境稅務及雙重課稅寬免')}</li>
      <li>{L('Accounting and wealth structuring around immigration', '與移民相關的會計及財富架構規劃')}</li>
      <li>{L('E-commerce accounting for Amazon, eBay, Shopify and TikTok Shop', '電子商務會計（Amazon、eBay、Shopify、TikTok Shop）')}</li>
    </ul>
  </section>
</div>
{contact_section(prefix)}
'''
    return page(prefix, "about.html", L("About · Wong & Yip Accountants", "關於我們 · 曼城黃葉會計師樓"),
                L("ACCA and HKICPA accountants in Manchester with more than 30 years of practice.", "曼徹斯特 ACCA 及 HKICPA 會計師，超過 30 年執業經驗。"), body)


def privacy(prefix):
    body = f'''
<section class="page-head">
  <div class="wrap"><h1>{L('Privacy and accessibility', '私隱及無障礙')}</h1>
  <p class="lede">{L('Draft wording for Wong &amp; Yip to review before use.', '草擬文字，須由曼城黃葉審閱後方可使用。')}</p></div>
</section>
<div class="wrap prose">
  <h2>{L('What this website collects', '本網站收集甚麼資料')}</h2>
  <p>{L('Nothing. The forms on this site do not send anything to a server: they open WhatsApp or your email app with your message filled in, and you choose whether to send it. The calculators run in your browser. There are no analytics or advertising cookies. The map loads tiles from OpenFreeMap when you scroll to it.', '沒有。本網站的表格不會把資料傳送到伺服器，只會開啟 WhatsApp 或電郵程式並填好訊息，由你決定是否發送。計算工具在你的瀏覽器內運作。本網站不設分析或廣告 Cookie。地圖在你捲動到該處時才從 OpenFreeMap 載入。')}</p>
  <h2>{L('When you contact us', '當你聯絡我們')}</h2>
  <p>{L('We use what you send us to answer you and, if you become a client, to provide our services and meet our legal duties, including anti-money laundering checks and keeping records for HMRC. We keep client records for at least six years. You can ask to see, correct or delete your information by emailing', '我們會用你提供的資料回覆你；如你成為客戶，亦會用於提供服務及履行法律責任，包括反洗錢核查及為 HMRC 保存紀錄。客戶紀錄最少保存六年。如要查閱、更正或刪除你的資料，請電郵至')} <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  <h2>{L('Accessibility', '無障礙')}</h2>
  <p>{L('This site aims to meet WCAG 2.2 AA: text contrast, keyboard use, visible focus, reduced motion and screen reader labels. If something does not work for you, call or email us and we will help.', '本網站以 WCAG 2.2 AA 為目標：文字對比、鍵盤操作、清晰焦點、減少動畫及螢幕閱讀器標籤。如有任何地方不便使用，請致電或電郵，我們樂意協助。')}</p>
</div>
'''
    return page(prefix, "privacy.html", L("Privacy and accessibility · Wong & Yip", "私隱及無障礙 · 曼城黃葉"), L("Privacy notice and accessibility statement.", "私隱聲明及無障礙聲明。"), body)


def notfound(prefix):
    body = f'''
<section class="nf">
  {spot("lost", "nf-art")}
  <div class="wrap">
    <h1>找不到這一頁 <span lang="en">Page not found</span></h1>
    <p>{L('Try the Stamp Duty calculator, our services, or call us on', '可以試試印花稅計算、我們的服務，或致電')} <a href="tel:{TEL}">{PHONE}</a>.</p>
    <p><a class="more" href="{prefix}index.html">返回首頁</a> <a class="more" href="{prefix}stamp-duty.html">印花稅</a> <a class="more" lang="en" href="{prefix}en/">English</a></p>
  </div>
</section>'''
    return page(prefix, "404.html", L("Page not found · Wong & Yip", "找不到頁面 · 曼城黃葉"), "", body)


PAGES = [("index.html", home), ("services.html", services), ("stamp-duty.html", stamp), ("about.html", about), ("privacy.html", privacy)]

if __name__ == "__main__":
    for lang, sub, prefix in (("zh", "", ""), ("en", "en", "../")):
        LANG = lang
        os.makedirs(os.path.join(ROOT, sub), exist_ok=True)
        PFX = prefix
        for name, fn in PAGES:
            with open(os.path.join(ROOT, sub, name), "w", encoding="utf-8") as f:
                f.write(fn(prefix))
    LANG, PFX = "zh", "/wong-yip/"  # GitHub Pages serves the root 404.html for every missing path: absolute links
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as f:
        f.write(notfound("/wong-yip/"))
    print("built", len(PAGES) * 2 + 1, "pages")
