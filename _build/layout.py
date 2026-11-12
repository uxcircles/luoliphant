import os

from opencc import OpenCC

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OFFICIAL = "https://www.luoliphant.com/"
FIRM = "Lu Oliphant Solicitors LLP"
EMAIL = "info@luoliphant.com"
TEL = "020 8952 8448"
TEL_INTL = "+44 (0)20 8952 8448"
TEL_HREF = "tel:+442089528448"
ADDRESS_1 = "210 Euston Road"
ADDRESS_2 = "London NW1 2DA"
MAPS = "https://maps.app.goo.gl/iTiofpZ1e9enMx7b6"
LINKEDIN = "https://www.linkedin.com/company/lu-oliphant-solicitors-llp/"
TWITTER = "https://twitter.com/LuOliphant"

LANGS = {
    "en": {"prefix": "", "html": "en-GB", "label": "EN", "name": "English"},
    "zh": {"prefix": "zh/", "html": "zh-Hant", "label": "繁", "name": "繁體中文"},
    "sc": {"prefix": "sc/", "html": "zh-Hans", "label": "简", "name": "简体中文"},
}

_cur = ["en"]
_s2t = OpenCC("s2t")
_t2s = OpenCC("t2s")


def cur():
    return _cur[0]


def set_lang(lang):
    _cur[0] = lang


def zh_text(s):
    """Chinese copy is written once (mostly Traditional; client quotes are often Simplified)
    and converted for each Chinese build so the two scripts never drift apart."""
    return _s2t.convert(s) if cur() == "zh" else _t2s.convert(s)


def L(en, zh):
    return en if cur() == "en" else zh_text(zh)


def is_zh():
    return cur() != "en"


def root():
    return "../" if LANGS[cur()]["prefix"] else ""


ICONS = {
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "ext": '<path d="M7 17 17 7M9 7h8v8"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "menu": '<path d="M4 8h16M4 16h16"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "quote": '<path d="M9 7H5v6h4v4H5M19 7h-4v6h4v4h-4" stroke-width="1.8"/>',
    "globe": '<circle cx="12" cy="12" r="9.5"/><path d="M2.5 12h19M12 2.5c2.6 2.8 3.9 6 3.9 9.5s-1.3 6.7-3.9 9.5c-2.6-2.8-3.9-6-3.9-9.5s1.3-6.7 3.9-9.5z"/>',
    "linkedin": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M8 10.5V17M8 7.2v.1M12 17v-3.8c0-1.6 1-2.7 2.4-2.7s2.1 1 2.1 2.7V17M12 10.5V17"/>',
}


def icon(name, cls="ic"):
    return (f'<svg class="{cls} ic-{name}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


# A square seal with the firm's initials: the one brand element that carries across all three languages.
SEAL = ('<svg class="seal" viewBox="0 0 40 40" aria-hidden="true">'
        '<rect x="1.5" y="1.5" width="37" height="37" rx="3" fill="currentColor"/>'
        '<rect x="5" y="5" width="30" height="30" rx="1.5" fill="none" stroke="var(--seal-ink)" stroke-width="1"/>'
        '<text x="20" y="26.4" text-anchor="middle" fill="var(--seal-ink)" font-family="Newsreader, Georgia, serif" '
        'font-size="17" font-weight="500" letter-spacing="-.5">LO</text></svg>')


def brand(href):
    return f'''<a class="brand" href="{href}" aria-label="Lu Oliphant Solicitors LLP — {L("home", "首頁")}">
      {SEAL}
      <span class="brand-text"><span class="brand-name">Lu Oliphant</span><span class="brand-sub">Solicitors LLP</span></span>
    </a>'''


def nav_items():
    return [
        ("services", "services.html", L("Services", "服務領域")),
        ("fees", "fees.html", L("Fees", "收費")),
        ("team", "team.html", L("Our firm", "律所與團隊")),
        ("testimonials", "testimonials.html", L("Client words", "客戶反饋")),
        ("insights", "insights.html", L("Insights", "法律資訊")),
    ]


def lang_switch(rel):
    out = []
    for code, meta in LANGS.items():
        href = root() + meta["prefix"] + rel
        cls = ' aria-current="true"' if code == cur() else ""
        out.append(f'<a href="{href}" hreflang="{meta["html"]}" lang="{meta["html"]}" title="{meta["name"]}"{cls}>{meta["label"]}</a>')
    return '<nav class="lang" aria-label="Language / 語言">' + "".join(out) + "</nav>"


def concept_bar():
    return f'''<div class="concept-bar" role="note">
  <div class="wrap concept-inner">
    <p><span class="concept-tag">Concept</span><span class="concept-long">{L(
        f'Concept redesign. Not the <a href="{OFFICIAL}" target="_blank" rel="noopener">official Lu Oliphant website</a>.',
        f'改版概念設計，並非 <a href="{OFFICIAL}" target="_blank" rel="noopener">Lu Oliphant 官方網站</a>。')}</span></p>
    <a href="https://ux-circles.com/professionals" target="_blank" rel="noopener"><span class="concept-by">{L("Designed by ", "設計：")}</span><strong>UX CIRCLES</strong> {icon("ext", "ic ic-sm")}</a>
  </div>
</div>'''


def header(rel, key):
    r = root()
    here = ' aria-current="page"'
    links = "".join(
        f'<a href="{href}"{here if k == key else ""}>{label}</a>' for k, href, label in nav_items())
    return f'''<header class="site-header">
  <div class="wrap header-inner">
    {brand("index.html")}
    <nav class="main-nav" id="main-nav" aria-label="{L("Main", "主選單")}">
      {links}
      <a class="nav-contact" href="contact.html"{' aria-current="page"' if key == "contact" else ""}>{L("Contact", "聯繫我們")}</a>
    </nav>
    <div class="header-tools">
      {lang_switch(rel)}
      <a class="btn btn-ink btn-sm header-cta" href="contact.html">{L("Make an enquiry", "提交諮詢")}</a>
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="main-nav" aria-label="{L("Menu", "選單")}">{icon("menu")}{icon("close")}</button>
    </div>
  </div>
</header>'''


def footer():
    y = "2026"
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        {brand("index.html")}
        <p>{L("A boutique firm of London solicitors advising clients in the UK, China and around the world since 1999.",
              "自 1999 年起，為英國、中國及世界各地客戶提供法律服務的倫敦精品律師事務所。")}</p>
        <p class="footer-langs">{L("We work in English, Mandarin and Cantonese.", "我們以英語、普通話及廣東話提供服務。")}</p>
      </div>
      <div class="footer-col">
        <h2>{L("Visit", "地址")}</h2>
        <p><a href="{MAPS}" target="_blank" rel="noopener">{ADDRESS_1}<br>{ADDRESS_2}</a></p>
        <p class="muted">{L("A short walk from Euston Square, Euston and Warren Street stations.", "步行可達 Euston Square、Euston 及 Warren Street 站。")}</p>
      </div>
      <div class="footer-col">
        <h2>{L("Talk to us", "聯繫")}</h2>
        <p><a href="{TEL_HREF}">{TEL_INTL}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p class="footer-social"><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a> · <a href="{TWITTER}" target="_blank" rel="noopener">X / Twitter</a></p>
      </div>
      <div class="footer-col">
        <h2>{L("Firm", "律所")}</h2>
        <ul>
          <li><a href="fees.html">{L("Price transparency", "收費透明")}</a></li>
          <li><a href="complaints.html">{L("Complaints procedure", "投訴程序")}</a></li>
          <li><a href="careers.html">{L("Careers", "招聘")}</a></li>
          <li><a href="{OFFICIAL}user-privacy" target="_blank" rel="noopener">{L("Privacy", "隱私政策")}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-base">
      <p>© {y} {FIRM}. {L("Authorised and regulated by the Solicitors Regulation Authority.", "受英國律師監管局（SRA）授權及監管。")}</p>
      <p class="concept-note">{L("Unofficial redesign concept by", "非官方改版概念，設計：")} <a href="https://ux-circles.com/professionals" target="_blank" rel="noopener">UX CIRCLES</a></p>
    </div>
  </div>
</footer>
<div class="mobile-bar" aria-label="{L("Quick contact", "快速聯繫")}">
  <a href="{TEL_HREF}">{icon("phone")}<span>{L("Call", "致電")}</span></a>
  <a href="mailto:{EMAIL}">{icon("mail")}<span>{L("Email", "電郵")}</span></a>
  <a class="primary" href="contact.html">{icon("arrow")}<span>{L("Enquire", "諮詢")}</span></a>
</div>'''


FONTS = ("https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300..600;1,6..72,300..500"
         "&family=Manrope:wght@400;500;600;700&display=swap")
FONTS_ZH = {
    "zh": "https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400;500;600&display=swap",
    "sc": "https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;600&display=swap",
}


def page(rel, *, key, title, description, body):
    lang = cur()
    out_path = os.path.join(OUT, LANGS[lang]["prefix"] + rel)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    r = root()
    full_title = f"{title} · Lu Oliphant Solicitors" if key != "home" else title
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{m["html"]}" href="{r}{m["prefix"]}{rel}">' for m in LANGS.values())
    zh_font = f'\n<link rel="stylesheet" href="{FONTS_ZH[lang]}">' if lang in FONTS_ZH else ""
    html = f'''<!doctype html>
<html lang="{LANGS[lang]["html"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{full_title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#11202e">
{alternates}
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">{zh_font}
<link rel="stylesheet" href="{r}assets/css/style.css">
</head>
<body class="page-{key} lang-{lang}">
<a class="skip" href="#main">{L("Skip to content", "跳至內容")}</a>
{concept_bar()}
{header(rel, key)}
<main id="main">
{body}
</main>
{footer()}
<script src="{r}assets/js/main.js" defer></script>
</body>
</html>
'''
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
