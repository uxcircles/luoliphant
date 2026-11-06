"""Build every page in English, Traditional Chinese (zh/) and Simplified Chinese (sc/).

    python3 _build/pages.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from layout import (L, page, set_lang, icon, is_zh, cur, LANGS, EMAIL, TEL, TEL_INTL, TEL_HREF,
                    ADDRESS_1, ADDRESS_2, MAPS, OFFICIAL)
from data import SERVICES, TEAM, TESTIMONIALS, INSIGHTS
import fees as F


def T(pair):
    return L(*pair) if isinstance(pair, tuple) else pair


def arrow_link(href, text, cls="link-arrow", ext=False):
    attrs = ' target="_blank" rel="noopener"' if ext else ""
    return f'<a class="{cls}" href="{href}"{attrs}>{text} {icon("ext" if ext else "arrow", "ic ic-sm")}</a>'


def money(n):
    return f"£{n:,}"


def page_head(eyebrow, title, lede, extra=""):
    return f'''<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{title}</h1>
    <p class="lede">{lede}</p>
    {extra}
  </div>
</section>'''


def contact_band():
    return f'''<section class="contact-band">
  <div class="wrap contact-band-inner">
    <div>
      <p class="eyebrow eyebrow-light">{L("We speak your language", "我們說您的語言")}</p>
      <h2>{L("Tell us where things stand, and where you want to get to.", "告訴我們目前的情況，以及您想達成的目標。")}</h2>
      <p>{L("We discuss every matter in English, Mandarin or Cantonese, and you deal directly with the solicitor handling it.",
            "我們以英語、普通話或廣東話與您溝通，並由負責您案件的律師直接跟進。")}</p>
    </div>
    <div class="contact-band-actions">
      <a class="btn btn-light" href="contact.html">{L("Make an enquiry", "提交諮詢")} {icon("arrow", "ic ic-sm")}</a>
      <a class="contact-line" href="{TEL_HREF}">{icon("phone")} {TEL}</a>
      <a class="contact-line" href="mailto:{EMAIL}">{icon("mail")} {EMAIL}</a>
    </div>
  </div>
</section>'''


def quote_card(t, cls=""):
    en, zh, d_en, d_zh, matter = t
    return f'''<figure class="quote {cls}" data-matter="{matter[0]}">
  {icon("quote", "ic quote-mark")}
  <blockquote>{L(en, zh)}</blockquote>
  <figcaption><span>{T(matter)}</span><span>{L(d_en, d_zh)}</span></figcaption>
</figure>'''


# ---------------------------------------------------------------- home
def home():
    facts = [
        ("1999", L("Advising clients from London since", "自此年起在倫敦執業")),
        ("85", L("Years of combined partner experience", "合夥人累計執業年數")),
        ("3", L("Working languages: English, Mandarin, Cantonese", "工作語言：英語、普通話、廣東話")),
        ("CQS", L("Law Society Conveyancing Quality Scheme", "英國律師公會物業轉讓質量認證")),
    ]
    fact_html = "".join(f'<div class="fact"><strong>{n}</strong><span>{t}</span></div>' for n, t in facts)

    svc = "".join(
        f'''<li><a href="services.html#{s["id"]}"><span class="svc-n">{i:02d}</span>
          <span class="svc-t">{T(s["title"])}</span><span class="svc-d">{T(s["short"])}</span>{icon("arrow", "ic svc-ic")}</a></li>'''
        for i, s in enumerate(SERVICES, 1))

    steps = [
        (L("Describe the situation", "說明現況"),
         L("Tell us what has happened so far, then what you want to achieve. A few lines is enough to start.",
           "先告訴我們目前的情況，再說明您想達成的目標。幾句話已足夠開始。")),
        (L("Clear advice and a fee estimate", "清晰建議及收費預算"),
         L("We explain your options and the risks in your own language, and tell you what it is likely to cost before any work begins.",
           "我們以您熟悉的語言解釋可行方案及風險，並在開始工作前告訴您預計費用。")),
        (L("One solicitor, start to finish", "同一位律師跟進到底"),
         L("You deal directly with the lawyer handling your matter, who anticipates problems before they become costly.",
           "由負責您案件的律師直接跟進，在問題變得棘手之前預先處理。")),
    ]
    step_html = "".join(f'<li><span class="step-n">{i}</span><h3>{h}</h3><p>{p}</p></li>' for i, (h, p) in enumerate(steps, 1))

    fee_eg = [
        (L("Residential purchase", "住宅物業購買"), L("from £2,500", "£2,500 起"), "fees.html#conveyancing"),
        (L("British naturalisation", "入籍英國"), "£1,800 – £2,200", "fees.html#immigration"),
        (L("Grant of probate & estate", "遺產認證及管理"), "£2,800 – £4,800", "fees.html#probate"),
    ]
    fee_html = "".join(
        f'<a class="fee-eg" href="{h}"><span>{a}</span><strong>{b}</strong><em>+ VAT</em></a>' for a, b, h in fee_eg)

    people = "".join(
        f'''<a class="person-chip" href="team.html#{p["initials"].lower()}"><span class="mono">{p["initials"]}</span>
          <span><strong>{T(p["name"])}</strong><em>{T(p["role"])}</em></span></a>''' for p in TEAM)

    quotes = "".join(quote_card(TESTIMONIALS[i]) for i in (0, 3, 6))

    insights = "".join(insight_card(x) for x in INSIGHTS)

    body = f'''<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="eyebrow eyebrow-light">{L("Solicitors · Euston Road, London · Since 1999", "律師事務所 · 倫敦 Euston Road · 始於 1999")}</p>
      <h1>{L("Small world.<br><em>Limitless vision.</em>", "世界有限，<br><em>視野無邊。</em>")}</h1>
      <p class="hero-lede">{L("A boutique London firm helping clients in the UK, China and across the world buy property, build businesses, settle here and look after their families.",
                               "倫敦精品律師事務所，協助英國、中國及世界各地的客戶在英國置業、經營業務、定居，並照顧家人。")}</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="contact.html">{L("Make an enquiry", "提交諮詢")} {icon("arrow", "ic ic-sm")}</a>
        <a class="btn btn-ghost" href="fees.html">{L("See our fees", "查看收費")}</a>
      </div>
    </div>
    <aside class="clock-card" aria-label="{L("Local times", "當地時間")}">
      <p class="clock-title">{icon("globe", "ic ic-sm")} {L("Two cities, one team", "兩地時區，同一團隊")}</p>
      <div class="clock" data-tz="Europe/London"><span class="clock-city">{L("London", "倫敦")}</span><span class="clock-time">--:--</span><span class="clock-day"></span></div>
      <div class="clock" data-tz="Asia/Shanghai"><span class="clock-city">{L("Beijing · Hong Kong", "北京 · 香港")}</span><span class="clock-time">--:--</span><span class="clock-day"></span></div>
      <p class="clock-note">{L("Wherever you are, you deal directly with your solicitor, in English, Mandarin or Cantonese.",
                              "無論您身在何地，都由您的律師直接跟進，以英語、普通話或廣東話溝通。")}</p>
      <div class="clock-links"><a href="{TEL_HREF}">{icon("phone", "ic ic-sm")} {TEL_INTL}</a><a href="mailto:{EMAIL}">{icon("mail", "ic ic-sm")} {EMAIL}</a></div>
    </aside>
  </div>
  <div class="wrap facts">{fact_html}</div>
</section>

<section class="intro section">
  <div class="wrap intro-grid">
    <h2 class="display">{L("Wherever our clients need UK legal expertise, Lu Oliphant delivers.", "無論客戶身在何方，需要英國法律服務，Lu Oliphant 都能勝任。")}</h2>
    <div class="intro-copy">
      <p>{L("From our office on Euston Road we have helped thousands of overseas investors, families and companies do business and build lives in the UK. Every client's situation is different, so we take the time to look at all of it: the implications for you now, and the risks further down the line.",
            "我們在 Euston Road 的辦公室，已協助數以千計的海外投資者、家庭及企業在英國發展事業和生活。每位客戶的情況都不同，所以我們會花時間了解全局：對您現在的影響，以及日後可能出現的風險。")}</p>
      {arrow_link("team.html", L("About the firm", "關於我們"))}
    </div>
  </div>
</section>

<section class="section section-tint" id="services">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">{L("Services", "服務領域")}</p>
      <h2>{L("Ten practice areas. One small team that knows your file.", "十個業務範疇，一個熟悉您案件的團隊。")}</h2>
    </div>
    <ol class="svc-list">{svc}</ol>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">{L("How we work", "工作方式")}</p>
      <h2>{L("Personal by design.", "由始至終，個人化服務。")}</h2>
    </div>
    <ol class="steps">{step_html}</ol>
  </div>
</section>

<section class="section section-ink">
  <div class="wrap fees-teaser">
    <div>
      <p class="eyebrow eyebrow-light">{L("Price transparency", "收費透明")}</p>
      <h2>{L("Know what it costs before you instruct us.", "委託之前，先清楚費用。")}</h2>
      <p>{L("Our fee scales for property, immigration, probate, employment tribunals and debt recovery are published in full, with a calculator for conveyancing.",
            "物業、移民、遺產認證、勞動審裁及追討債務的收費全部公開，物業轉讓更設有費用計算器。")}</p>
      {arrow_link("fees.html", L("All fees", "全部收費"), "link-arrow link-light")}
    </div>
    <div class="fee-egs">{fee_html}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head section-head-row">
      <div><p class="eyebrow">{L("Client words", "客戶反饋")}</p>
      <h2>{L("Thank-you letters, in our clients' own words.", "客戶的感謝信，原文照錄。")}</h2></div>
      {arrow_link("testimonials.html", L("Read more", "閱讀更多"))}
    </div>
    <div class="quotes">{quotes}</div>
  </div>
</section>

<section class="section section-tint">
  <div class="wrap team-teaser">
    <div>
      <p class="eyebrow">{L("The team", "團隊")}</p>
      <h2>{L("You deal directly with the people who matter.", "直接與負責的律師溝通。")}</h2>
      <p>{L("Partners with 85 years of combined practice, and lawyers qualified in England & Wales, New York and Australia.",
            "合夥人累計執業 85 年，團隊律師分別具英格蘭及威爾斯、紐約及澳洲執業資格。")}</p>
      {arrow_link("team.html#people", L("Meet the team", "認識團隊"))}
    </div>
    <div class="person-chips">{people}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head section-head-row">
      <div><p class="eyebrow">{L("Insights", "法律資訊")}</p>
      <h2>{L("Recent thinking from the team.", "團隊近期文章。")}</h2></div>
      {arrow_link("insights.html", L("All insights", "全部文章"))}
    </div>
    <div class="insights">{insights}</div>
  </div>
</section>

<section class="community">
  <div class="wrap community-inner">
    <p class="eyebrow">{L("In the community", "社區參與")}</p>
    <p class="community-text">{L("We are a charitable key sponsor of the <strong>Chinese Health & Wellbeing Clinic</strong> in London Chinatown, where NHS doctors and therapists see patients in Mandarin, Cantonese and English every Sunday.",
                                  "我們是倫敦唐人街<strong>華人健康福祉診所</strong>的主要慈善贊助方。診所每逢星期日由 NHS 醫生及治療師以普通話、廣東話及英語為病人診症。")}</p>
    {arrow_link("team.html#community", L("About the clinic", "了解診所"))}
  </div>
</section>

{contact_band()}'''
    page("index.html", key="home",
         title=L("Lu Oliphant Solicitors LLP · London solicitors since 1999", "Lu Oliphant 律師事務所 · 倫敦精品律師行"),
         description=L("Boutique London solicitors on Euston Road advising clients in the UK, China and worldwide on property, immigration, company, employment, disputes and wills, in English, Mandarin and Cantonese.",
                       "位於倫敦 Euston Road 的精品律師事務所，以英語、普通話及廣東話為英國、中國及世界各地客戶提供物業、移民、公司、勞動、訴訟及遺囑服務。"),
         body=body)


def insight_card(x):
    ext = x["external"]
    attrs = ' target="_blank" rel="noopener"' if ext else ""
    more = L("Read on LinkedIn", "於 LinkedIn 閱讀") if ext else L("Read article", "閱讀全文")
    return f'''<a class="insight" href="{x["href"]}"{attrs}>
  <p class="insight-meta"><span>{T(x["tag"])}</span><span>{T(x["date"])}</span></p>
  <h3>{T(x["title"])}</h3>
  <p>{T(x["dek"])}</p>
  <span class="link-arrow">{more} {icon("ext" if ext else "arrow", "ic ic-sm")}</span>
</a>'''


# ---------------------------------------------------------------- services
def services():
    index = "".join(f'<li><a href="#{s["id"]}">{T(s["title"])}</a></li>' for s in SERVICES)
    blocks = []
    for i, s in enumerate(SERVICES, 1):
        items = "".join(f"<li>{icon('check', 'ic ic-sm')}<span>{T(it)}</span></li>" for it in s["items"])
        fee = ""
        if s["fees"]:
            fee = arrow_link(f'fees.html#{s["fees"]}', L("See fees", "查看收費"))
        blocks.append(f'''<article class="svc" id="{s["id"]}">
  <div class="svc-head">
    <span class="svc-num">{i:02d}</span>
    <div><h2>{T(s["title"])}</h2><p class="svc-sub">{T(s["sub"])}</p></div>
  </div>
  <p class="svc-intro">{T(s["intro"])}</p>
  <h3 class="mini">{L("How we can help", "我們可協助的事項")}</h3>
  <ul class="ticks">{items}</ul>
  <div class="svc-actions">
    <a class="btn btn-ink btn-sm" href="contact.html?matter={s["id"]}">{L("Ask about this", "就此諮詢")}</a>
    {fee}
  </div>
</article>''')
    body = f'''{page_head(L("Services", "服務領域"), L("Expertise that is always tailored to you.", "始終為您量身定制的專業服務。"),
        L("We guide clients through UK legal processes however complex or sensitive, with a real understanding of their culture and how they like to work.",
          "無論事情多複雜或敏感，我們都會帶領您完成英國的法律程序，並真正理解您的文化背景和工作習慣。"))}
<section class="section section-tight">
  <div class="wrap with-aside">
    <aside class="side-index" aria-label="{L("Practice areas", "業務範疇")}">
      <p class="mini">{L("Practice areas", "業務範疇")}</p>
      <ol>{index}</ol>
    </aside>
    <div class="svc-stack">{"".join(blocks)}</div>
  </div>
</section>
{contact_band()}'''
    page("services.html", key="services", title=L("Services", "服務領域"),
         description=L("Conveyancing, immigration, company law, property financing, employment, disputes, wills and probate, powers of attorney and statutory declarations.",
                       "物業轉讓、移民、公司法、物業融資、勞動法、糾紛訴訟、遺囑及遺產、授權書及法定聲明。"),
         body=body)


# ---------------------------------------------------------------- fees
def fee_table(t):
    rows = []
    for (limit, label), fee in zip(F.BANDS, t["fees"] + [None]):
        val = money(fee) if fee else L(f'{t["pct"]}% of price', f'樓價的 {t["pct"]}%')
        rows.append(f"<tr><th scope=\"row\">{T(label)}</th><td>{val} <span class=\"vat\">+ VAT</span></td></tr>")
    return f'''<div class="table-card">
  <h4>{T(t["title"])}</h4>
  <table><thead><tr><th scope="col">{L("Price or value", "樓價或價值")}</th><th scope="col">{L("Our estimated fee", "預計律師費")}</th></tr></thead>
  <tbody>{"".join(rows)}</tbody></table>
</div>'''


def fees():
    nav = [("conveyancing", L("Conveyancing", "物業轉讓")), ("immigration", L("Immigration", "移民")),
           ("probate", L("Probate", "遺產認證")), ("employment", L("Employment tribunals", "勞動審裁")),
           ("debt-recovery", L("Debt recovery", "追討債務"))]
    nav_html = "".join(f'<a href="#{k}">{v}</a>' for k, v in nav)

    opts = "".join(f'<option value="{t["id"]}">{T(t["title"])}</option>' for t in F.CONVEYANCING)
    import json
    calc_data = json.dumps({t["id"]: {"fees": t["fees"], "pct": t["pct"]} for t in F.CONVEYANCING})
    tables = "".join(fee_table(t) for t in F.CONVEYANCING)
    disb = "".join(f"<tr><th scope=\"row\">{T(a)}</th><td>{T(b)}</td></tr>" for a, b in F.DISBURSEMENTS)
    stages = "".join(f"<li>{T(s)}</li>" for s in F.STAGES)

    imm = "".join(
        f'''<div class="table-card"><h4>{T(title)}</h4><table><tbody>{"".join(f"<tr><th scope=\"row\">{T(a)}</th><td>{T(b)}</td></tr>" for a, b in rows)}</tbody></table></div>'''
        for title, rows in F.IMMIGRATION)

    emp = "".join(f"<tr><th scope=\"row\">{T(a)}</th><td>{b}</td><td>{c}</td></tr>" for a, b, c in F.EMPLOYMENT)

    body = f'''{page_head(L("Price transparency", "收費透明"), L("Our fees, published in full.", "收費標準，全部公開。"),
        L("Wherever we can, we tell you in advance what the most common legal processes will cost. Every matter is different, so treat these as a guide and ask us for a figure based on your documents.",
          "我們盡可能讓您預先知道常見法律程序的費用。每宗個案都不同，以下僅供參考，我們會在了解您的文件後提供更準確的報價。"),
        f'<p class="rate-note">{L("Additional or complex work is charged by time:", "額外或複雜工作按時間收費：")} <strong>{T(F.PARTNER_RATES)}</strong>. {L("VAT at 20% where applicable.", "如適用另加 20% VAT。")}</p>')}
<nav class="fee-nav" aria-label="{L("Fee sections", "收費分類")}"><div class="wrap">{nav_html}</div></nav>

<section class="section fee-sec" id="conveyancing">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">01</p><h2>{L("Residential conveyancing", "住宅物業轉讓")}</h2>
    <p class="section-lede">{L("Our fee covers all the work to complete your purchase, including Land Registry registration and paying Stamp Duty Land Tax.",
                               "律師費已包括完成購買所需的全部工作，包括土地註冊處登記及繳交印花稅。")}</p></div>

    <div class="calc" data-calc='{calc_data}'>
      <div class="calc-in">
        <h3>{L("Estimate your legal fee", "估算律師費")}</h3>
        <label>{L("Type of transaction", "交易類型")}<select id="calc-type">{opts}</select></label>
        <label>{L("Purchase price or value (£)", "樓價或價值（英鎊）")}<input id="calc-price" type="text" inputmode="numeric" value="750,000" autocomplete="off"></label>
      </div>
      <div class="calc-out" aria-live="polite">
        <div class="calc-row"><span>{L("Legal fee", "律師費")}</span><strong id="calc-fee">—</strong></div>
        <div class="calc-row"><span>VAT 20%</span><strong id="calc-vat">—</strong></div>
        <div class="calc-row calc-total"><span>{L("Total before disbursements", "未計雜費總額")}</span><strong id="calc-total">—</strong></div>
        <p class="calc-note">{L("Disbursements and Stamp Duty are extra. Use", "雜費及印花稅另計。印花稅可用")} <a href="https://www.tax.service.gov.uk/calculate-stamp-duty-land-tax/" target="_blank" rel="noopener">{L("HMRC's SDLT calculator", "HMRC 計算器")}</a>{L(" for Stamp Duty; we cannot give tax advice.", " 估算；我們不提供稅務建議。")}</p>
      </div>
    </div>

    <div class="table-grid">{tables}</div>

    <div class="two-col">
      <div class="table-card">
        <h4>{L("Typical disbursements", "常見雜費")}</h4>
        <table><tbody>{disb}</tbody></table>
        <p class="small">{L("Paid to third parties on your behalf. Leasehold fees are set by the lease and confirmed once we have it. Estimated total for most purchases: £2,500 – £5,600, excluding SDLT.",
                             "代您支付予第三方。租賃業權相關費用由租約訂明，收到租約後確認。大部分交易的雜費估計共 £2,500 – £5,600（不含印花稅）。")}</p>
      </div>
      <div class="prose-card">
        <h4>{L("How long will it take?", "需時多久？")}</h4>
        <p>{L("Usually 4 – 8 weeks from offer accepted to completion. A cash purchase with no chain can be quicker; leasehold extensions, sitting tenants or delays in the chain can take 2 – 4 months or more, and additional charges may apply.",
              "由出價獲接納至成交，一般需時 4 – 8 星期。無按揭、無連鎖交易的可以更快；如涉及延長租約、租客未遷出或連鎖交易延誤，可能需 2 – 4 個月或以上，並可能產生額外費用。")}</p>
        <h4>{L("Key stages", "主要步驟")}</h4>
        <ol class="stages">{stages}</ol>
        <p class="small">{L("Referral fees are occasionally paid to agents from our own fee, at no cost to you. Where we are on a developer's panel we act independently, in your interest.",
                             "我們偶爾會從自己的律師費中支付介紹費予代理，不會增加您的費用。即使我們在發展商的律師名單上，也會獨立行事，以您的利益為先。")}</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-tint fee-sec" id="immigration">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">02</p><h2>{L("Immigration", "移民")}</h2>
    <p class="section-lede">{L("Every application is bespoke and charged on time spent, so these are guide ranges rather than fixed quotes. Home Office fees, the Immigration Health Surcharge, translations, TB tests and criminal record checks are extra.",
                               "每宗申請都按個別情況處理，並按實際工作時間收費，以下為參考範圍而非固定報價。內政部申請費、移民醫療附加費、翻譯、肺結核檢測及無犯罪記錄證明另計。")}</p></div>
    <div class="table-grid table-grid-3">{imm}</div>
    <div class="two-col">
      <div class="prose-card">
        <h4>{L("What's included", "服務包括")}</h4>
        <ul class="ticks">
          <li>{icon('check', 'ic ic-sm')}<span>{L("Confirming the right route for you and the alternatives", "確認最合適的申請途徑及其他選擇")}</span></li>
          <li>{icon('check', 'ic ic-sm')}<span>{L("Advice on the Immigration Rules and whether you meet them", "解釋移民規則及您是否符合要求")}</span></li>
          <li>{icon('check', 'ic ic-sm')}<span>{L("Reviewing your documents and helping obtain further evidence", "審閱文件並協助取得補充證據")}</span></li>
          <li>{icon('check', 'ic ic-sm')}<span>{L("Preparing and submitting the application", "準備及遞交申請")}</span></li>
          <li>{icon('check', 'ic ic-sm')}<span>{L("Advice on the outcome and next steps", "就結果及後續步驟提供建議")}</span></li>
        </ul>
      </div>
      <div class="prose-card">
        <h4>{L("Timing", "時間")}</h4>
        <p>{L("We normally submit within 2 – 4 weeks of your instructions. Home Office processing times are outside our control. Attending a Home Office interview with you is charged separately at £350 + VAT an hour, typically 2 – 4 hours.",
              "我們一般在接受委託後 2 – 4 星期內遞交申請，內政部的處理時間則非我們所能控制。如需陪同出席內政部面談，另按每小時 £350 + VAT 收費，一般需 2 – 4 小時。")}</p>
      </div>
    </div>
  </div>
</section>

<section class="section fee-sec" id="probate">
  <div class="wrap two-col two-col-head">
    <div class="section-head"><p class="eyebrow">03</p><h2>{L("Probate", "遺產認證")}</h2>
      <p class="section-lede">{L("Applying for the grant of probate, then collecting and distributing the estate.", "申請遺產認證，並收集及分配遺產。")}</p>
      <div class="big-figure"><strong>£2,800 – £4,800</strong><span>+ VAT · {L("10 – 20 hours of partner time", "合夥人工作 10 – 20 小時")}</span></div>
      <p>{L("Typically 6 – 12 months in total: around 8 – 12 weeks for the grant, 4 – 8 weeks to collect assets and 2 – 4 weeks to distribute them.",
            "整體一般需時 6 – 12 個月：取得遺產認證約 8 – 12 星期，收集資產 4 – 8 星期，分配資產 2 – 4 星期。")}</p>
    </div>
    <div class="prose-card">
      <h4>{L("This estimate assumes", "此估價假設")}</h4>
      <ul class="plain">
        <li>{L("A valid will, one property and no more than two bank accounts", "有有效遺囑、只有一項物業及不多於兩個銀行戶口")}</li>
        <li>{L("One or two beneficiaries, with no disputes or claims against the estate", "一至兩名受益人，沒有爭議或針對遺產的申索")}</li>
        <li>{L("No inheritance tax payable and no full HMRC account needed", "無須繳付遺產稅，亦無須向 HMRC 提交完整申報")}</li>
      </ul>
      <h4>{L("Disbursements", "雜費")}</h4>
      <ul class="plain">
        <li>{L("Probate application fee: £160", "遺產認證申請費：£160")}</li>
        <li>{L("Swearing the oath: £5 – £30 per executor", "宣誓：每名遺囑執行人 £5 – £30")}</li>
        <li>{L("Bankruptcy searches: £5 per beneficiary", "破產查冊：每名受益人 £5")}</li>
        <li>{L("Tracked post: £10 – £20; title deeds: £3.90 each", "掛號郵寄：£10 – £20；業權契據：每份 £3.90")}</li>
      </ul>
      <p class="small">{L("No will, shareholdings, overseas assets or a death abroad will add cost. Selling estate property is not included.",
                           "如無遺囑、涉及股票、海外資產或在海外離世，費用會增加。出售遺產物業不包括在內。")}</p>
    </div>
  </div>
</section>

<section class="section section-tint fee-sec" id="employment">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">04</p><h2>{L("Employment tribunals", "勞動審裁")}</h2>
    <p class="section-lede">{L("Bringing or defending an unfair or wrongful dismissal claim. Charged on time; guide ranges for our fees, plus VAT.",
                               "提出或抗辯不公平或不當解僱申索。按時間收費，以下為律師費參考範圍，另加 VAT。")}</p></div>
    <div class="two-col">
      <div class="table-card">
        <table><thead><tr><th scope="col"></th><th scope="col">{L("Employee", "僱員")}</th><th scope="col">{L("Employer", "僱主")}</th></tr></thead>
        <tbody>{emp}</tbody></table>
        <p class="small">{L("Counsel for the hearing is typically £750 – £2,000 + VAT a day. Each side usually pays its own costs in the tribunal, win or lose. We do not work on a no win, no fee basis.",
                             "出席聆訊的大律師費一般每日 £750 – £2,000 + VAT。審裁處一般由雙方各自承擔訟費，不論勝負。我們不提供「不成功不收費」安排。")}</p>
      </div>
      <div class="prose-card">
        <h4>{L("How long?", "需時多久？")}</h4>
        <p>{L("Settled in early conciliation: about 4 – 6 weeks. Through to a final hearing: about 6 – 10 months.",
              "如在早期調解階段和解：約 4 – 6 星期；如進入最終聆訊：約 6 – 10 個月。")}</p>
        <h4>{L("What makes a case more complex", "令個案更複雜的因素")}</h4>
        <ul class="plain">
          <li>{L("Discrimination or whistleblowing allegations", "涉及歧視或舉報指控")}</li>
          <li>{L("Many witnesses or documents", "證人或文件數量眾多")}</li>
          <li>{L("Preliminary issues, amendments or costs applications", "初步爭議、修改申索或訟費申請")}</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section fee-sec" id="debt-recovery">
  <div class="wrap two-col two-col-head">
    <div class="section-head"><p class="eyebrow">05</p><h2>{L("Debt recovery", "追討債務")}</h2>
      <p class="section-lede">{L("Business-to-business debts that are not disputed, charged at our partner hourly rates.",
                                 "無爭議的企業間債務，按合夥人時薪收費。")}</p>
      <p>{L("Expect anywhere from 12 to 52 weeks to payment, depending on how the debtor and the court respond. Court fees are set by", "視乎債務人及法院的回應，由委託到收款約需 12 至 52 星期。法院費用由")} <a href="https://www.gov.uk/make-court-claim-for-money/court-fees" target="_blank" rel="noopener">GOV.UK</a>{L(".", " 訂明。")}</p>
    </div>
    <div class="prose-card">
      <h4>{L("Our fee includes", "律師費包括")}</h4>
      <ol class="stages">
        <li>{L("Reviewing your documents and carrying out searches", "審閱文件及進行查冊")}</li>
        <li>{L("A letter before action", "發出律師信")}</li>
        <li>{L("Preparing and issuing the claim", "準備及提交申索")}</li>
        <li>{L("Applying for judgment in default if there is no response", "如對方無回應，申請缺席判決")}</li>
        <li>{L("Requesting payment and advising on next steps", "要求付款並就下一步提供建議")}</li>
      </ol>
      <p class="small">{L("VAT on our fees cannot be reclaimed from the debtor. Enforcement is not included.", "律師費的 VAT 不能向債務人追討。強制執行不包括在內。")}</p>
    </div>
  </div>
</section>
{contact_band()}'''
    page("fees.html", key="fees", title=L("Fees", "收費"),
         description=L("Lu Oliphant's published fees for residential conveyancing, immigration, probate, employment tribunals and debt recovery, with a conveyancing fee calculator.",
                       "Lu Oliphant 物業轉讓、移民、遺產認證、勞動審裁及追討債務的公開收費，附物業轉讓費用計算器。"),
         body=body)


# ---------------------------------------------------------------- team / about
def team():
    values = [
        (L("High performance", "專業表現"), L("Efficient, well-run matters, with risks anticipated rather than discovered.", "高效處理案件，預先識別風險，而非事後補救。")),
        (L("A personal touch", "個人化服務"), L("A small team, so the partner you meet is the partner on your file.", "團隊精簡，與您會面的合夥人就是處理您案件的人。")),
        (L("Cultural fluency", "跨文化理解"), L("We understand how clients from China and Hong Kong like to work, and explain UK law accordingly.", "我們了解來自中國內地及香港客戶的習慣，並據此解釋英國法律。")),
    ]
    vals = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in values)
    people = []
    for p in TEAM:
        langs = f'<p class="person-langs">{icon("globe", "ic ic-sm")} {T(p["langs"])}</p>' if p["langs"] else ""
        people.append(f'''<article class="person" id="{p["initials"].lower()}">
  <div class="person-id">
    <span class="mono mono-lg">{p["initials"]}</span>
    <div><h3>{T(p["name"])}</h3><p class="person-role">{T(p["role"])}</p></div>
  </div>
  <div class="person-body">
    <p class="person-focus">{T(p["focus"])}</p>
    {langs}
    <p>{T(p["bio"])}</p>
    <a class="link-arrow" href="mailto:{p["email"]}">{icon("mail", "ic ic-sm")} {p["email"]}</a>
  </div>
</article>''')
    body = f'''{page_head(L("Our firm", "律所與團隊"), L("The global destination for UK legal expertise.", "尋求英國法律專業服務的全球之選。"),
        L("Lu Oliphant is a boutique London firm with a global reach. Since 1999 we have helped thousands of overseas investors do business in the UK.",
          "Lu Oliphant 是一家具國際視野的倫敦精品律師事務所。自 1999 年起，我們已協助數以千計的海外投資者在英國開展業務。"))}
<section class="section section-tight">
  <div class="wrap intro-grid">
    <h2 class="display">{L("Above and beyond, case by case.", "超越期望，每一宗案件皆然。")}</h2>
    <div class="intro-copy">
      <p>{L("Our approach combines high performance with a personal touch. We know from experience that every client's situation is unique, so we look at every aspect and its implications for you, anticipate potential issues and reduce risk, now and in the long term.",
            "我們的工作方式結合高水準的專業表現與個人化服務。經驗告訴我們，每位客戶的情況都是獨特的，所以我們會研究每一個方面及其對您的影響，預先識別潛在問題，降低現在和將來的風險。")}</p>
      <p>{L("We are accredited under the Law Society's Conveyancing Quality Scheme, and many of our clients are private and corporate clients from the Far East.",
            "我們獲英國律師公會物業轉讓質量計劃（CQS）認證，不少客戶是來自遠東的私人及企業客戶。")}</p>
    </div>
  </div>
  <div class="wrap"><ul class="values">{vals}</ul></div>
</section>

<section class="section section-tint" id="people">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">{L("Meet the team", "我們的團隊")}</p>
      <h2>{L("Knowledgeable, expert and client focused.", "知識淵博，專業可靠，以客戶為中心。")}</h2>
      <p class="section-lede">{L("Our partners bring 85 years of combined practice to every case. With us it's personal: you deal directly with the people who matter.",
                                 "我們的合夥人累計執業 85 年。對我們而言，服務是個人化的：您會直接與負責的律師對接。")}</p>
    </div>
    <div class="people">{"".join(people)}</div>
  </div>
</section>

<section class="section" id="community">
  <div class="wrap two-col two-col-head">
    <div class="section-head">
      <p class="eyebrow">{L("In the community", "社區參與")}</p>
      <h2>{L("The Chinese Health & Wellbeing Clinic", "華人健康福祉診所")}</h2>
    </div>
    <div class="prose">
      <p>{L("Lu Oliphant is a charitable key sponsor of the Chinese Health & Wellbeing Clinic, which aims to improve access to healthcare for the British Chinese community.",
            "Lu Oliphant 是華人健康福祉診所的主要慈善贊助方。診所旨在改善英國華人社區獲得醫療服務的機會。")}</p>
      <p>{L("Experienced NHS doctors and therapists fluent in Mandarin, Cantonese and English run physical and mental health clinics and health workshops at the Chinese Community Centre in Chinatown, on Sundays from 11am to 4pm. Many older people and first-generation migrants cannot use new online services, so a face-to-face clinic helps them overcome language and cultural barriers.",
            "診所由精通普通話、廣東話及英語的資深 NHS 醫生及治療師主理，每逢星期日上午 11 時至下午 4 時在唐人街華人社區中心提供身心健康診症及健康講座。不少長者及第一代移民無法使用網上服務，面對面的診所能幫助他們跨越語言和文化障礙。")}</p>
      <p class="small">{L("A partnership of the London Chinese Community Centre, UK Chinese Medical Services and Catalyst Therapy Services. Chinese Community Centre, 2 Leicester Court, London WC2H 7DW · 020 7439 3822.",
                           "由倫敦華人社區中心、UK Chinese Medical Services 及 Catalyst Therapy Services 合辦。華人社區中心：2 Leicester Court, London WC2H 7DW · 020 7439 3822。")}</p>
    </div>
  </div>
</section>

<section class="section section-ink">
  <div class="wrap careers-teaser">
    <div>
      <p class="eyebrow eyebrow-light">{L("Careers", "招聘")}</p>
      <h2>{L("Our strength lies in our people.", "人才是我們的力量。")}</h2>
      <p>{L("A collaborative place to learn from experienced practitioners, do meaningful client work and grow a career in law.",
            "在這裡，您可以向資深律師學習，參與有意義的客戶工作，並發展法律事業。")}</p>
    </div>
    {arrow_link("careers.html", L("Current opportunities", "現有職位"), "btn btn-light")}
  </div>
</section>
{contact_band()}'''
    page("team.html", key="team", title=L("Our firm & team", "律所與團隊"),
         description=L("About Lu Oliphant Solicitors LLP and its partners and lawyers: Chi Wai Lu, Mei Lu, James Lau, Eugenie Chua and Nicholas Woo.",
                       "關於 Lu Oliphant 律師事務所及其合夥人和律師：劉志偉、劉芳媚、James Lau、Eugenie Chua 及胡衍陽。"),
         body=body)


# ---------------------------------------------------------------- testimonials
def testimonials():
    matters = []
    for t in TESTIMONIALS:
        if t[4] not in matters:
            matters.append(t[4])
    chips = f'<button type="button" class="chip" aria-pressed="true" data-filter="all">{L("All", "全部")}</button>' + "".join(
        f'<button type="button" class="chip" aria-pressed="false" data-filter="{m[0]}">{T(m)}</button>' for m in matters)
    cards = "".join(quote_card(t) for t in TESTIMONIALS)
    body = f'''{page_head(L("Client words", "客戶反饋"), L("In our clients' own words.", "客戶的心聲。"),
        L("Extracts from thank-you notes our clients have sent us. Names are withheld.",
          "節錄自客戶寄來的感謝信，已隱去姓名。"))}
<section class="section section-tight">
  <div class="wrap">
    <div class="chips" role="group" aria-label="{L("Filter by matter", "按事務篩選")}">{chips}</div>
    <div class="quotes quotes-wall">{cards}</div>
  </div>
</section>
{contact_band()}'''
    page("testimonials.html", key="testimonials", title=L("Client words", "客戶反饋"),
         description=L("What clients say about Lu Oliphant's immigration, property, employment and probate work.", "客戶對 Lu Oliphant 移民、物業、勞動法及遺產服務的評價。"),
         body=body)


# ---------------------------------------------------------------- insights + article
def insights():
    body = f'''{page_head(L("Insights", "法律資訊"), L("Notes on the rules that affect our clients.", "影響客戶的法規解讀。"),
        L("Written by our lawyers when the rules change, or when a question keeps coming up.", "每當法規變更或常見問題出現時，由我們的律師撰寫。"))}
<section class="section section-tight"><div class="wrap"><div class="insights">{"".join(insight_card(x) for x in INSIGHTS)}</div></div></section>
{contact_band()}'''
    page("insights.html", key="insights", title=L("Insights", "法律資訊"),
         description=L("Articles from Lu Oliphant's lawyers on UK immigration and property.", "Lu Oliphant 律師撰寫的英國移民及物業文章。"), body=body)


def article():
    ex = [
        (L("Example 1 · Whole qualifying period before 11 April 2024", "例子一：整個合資格期間在 2024 年 4 月 11 日之前"),
         L("The applicant completed 10 years on 10 April 2024, with two absences of 50 and 120 days, both finished before 11 April 2024. Neither exceeded 184 days and the total stayed under 548 days, so continuous residence is not broken.",
           "申請人於 2024 年 4 月 10 日完成十年居留，期間有兩次分別為 50 日及 120 日的缺席，均在 2024 年 4 月 11 日前結束。兩次都沒有超過 184 日，總數亦少於 548 日，因此連續居留沒有中斷。")),
        (L("Example 2 · Started before 11 April 2024, completed after", "例子二：在 2024 年 4 月 11 日前開始，之後完成"),
         L("The applicant completed 10 years on 20 January 2025 with five absences. The three completed before 11 April 2024 are tested against the 184-day single and 548-day total limits. An absence from 1 April to 1 July 2024 started before the change, so the 184-day single limit applies, and its days up to 10 April count towards the 548-day total. The absence from 1 August 2024 to 20 January 2025 is tested against 180 days in any rolling 12 months, starting from 1 August 2024. None breaks the rules, so residence is continuous.",
           "申請人於 2025 年 1 月 20 日完成十年居留，期間共缺席五次。2024 年 4 月 11 日前已結束的三次，按單次 184 日及總數 548 日的上限計算。2024 年 4 月 1 日至 7 月 1 日的缺席在新規定前開始，因此適用單次 184 日上限，而 4 月 10 日或之前的日數計入 548 日總數。2024 年 8 月 1 日至 2025 年 1 月 20 日的缺席，則按任何連續 12 個月不超過 180 日計算，由 2024 年 8 月 1 日起計。所有缺席均未超出上限，因此連續居留成立。")),
        (L("Example 3 · Qualifying period started on or after 11 April 2024", "例子三：合資格期間在 2024 年 4 月 11 日或之後開始"),
         L("The applicant completes 10 years on 30 April 2034 with one absence from 1 July to 10 August 2030. Only the 180-days-in-12-months rule applies, and it is met.",
           "申請人於 2034 年 4 月 30 日完成十年居留，期間只在 2030 年 7 月 1 日至 8 月 10 日缺席一次。只須符合任何 12 個月內不超過 180 日的規定，而申請人符合要求。")),
    ]
    ex_html = "".join(f'<div class="example"><h3>{h}</h3><p>{p}</p></div>' for h, p in ex)
    body = f'''<article class="article">
  <header class="article-head">
    <div class="wrap wrap-narrow">
      <p class="eyebrow"><a href="insights.html">{L("Insights", "法律資訊")}</a> · {L("Immigration", "移民")}</p>
      <h1>{L("Home Office clarifies the new 10-year long residence rules", "內政部澄清十年長期居留新規定")}</h1>
      <p class="lede">{L("Applications made after the April 2024 changes were held while the department worked out what the new rules meant. Its clarified position turns out to be a little more generous than feared.",
                          "2024 年 4 月規則修訂後，不少申請因內政部內部對新規定理解不一而被擱置。現在內政部已澄清立場，結果比預期稍為寬鬆。")}</p>
    </div>
  </header>
  <div class="wrap wrap-narrow prose article-body">
    <h2>{L("Three tests instead of two", "由兩項測試變為三項")}</h2>
    <p>{L("Absences over the 10 years are now split into two periods, before and after 11 April 2024. You must satisfy all three:",
          "十年內的缺席日數，現以 2024 年 4 月 11 日為界分為前後兩段。申請人必須同時符合以下三項：")}</p>
    <div class="rule-cards">
      <div><strong>184</strong><span>{L("days maximum for any single absence that started before 11 April 2024", "日：2024 年 4 月 11 日前開始的任何單次缺席上限")}</span></div>
      <div><strong>548</strong><span>{L("days maximum in total across the part of the qualifying period before 11 April 2024", "日：合資格期間中 2024 年 4 月 11 日前部分的缺席總數上限")}</span></div>
      <div><strong>180</strong><span>{L("days maximum outside the UK in any rolling 12 months from 11 April 2024", "日：2024 年 4 月 11 日起任何連續 12 個月內的離境上限")}</span></div>
    </div>
    <h2>{L("The Home Office's worked examples", "內政部的計算例子")}</h2>
    {ex_html}
    <h2>{L("What this means for you", "這對您有何影響")}</h2>
    <p>{L("If your application relies on residence before 11 April 2024, a total of more than 548 days, or a single absence of more than 184 days, in that period will break continuous residence. Your options are then to wait until those absences fall outside the 10-year window, or to show exceptional circumstances beyond your control, such as illness or pandemic travel disruption.",
          "如您的申請需要依賴 2024 年 4 月 11 日前的居留，該段期間缺席總數超過 548 日，或單次缺席超過 184 日，連續居留便會中斷。屆時可選擇等待有關缺席移出十年範圍，或證明存在非您所能控制的特殊情況，例如疾病或疫情導致的出行中斷。")}</p>
    <h2>{L("The new 12-month rule", "新的十二個月規定")}</h2>
    <p>{L("If your current visa was granted on or after 11 April 2024, you must also have held it for at least 12 months in the same route. That does not mean waiting a year after every renewal: an extension in the same category counts.",
          "如您現時的簽證於 2024 年 4 月 11 日或之後批出，您亦必須在同一途徑下持有該簽證至少 12 個月。這並不代表每次續簽後都要再等一年：同一類別的續簽可以合併計算。")}</p>
    <p>{L("For example, after 7 years on student and graduate visas you switch to a spouse visa for 2.5 years, then extend it for another 2.5. You only need 6 more months to reach 10 years and apply. If instead the relationship ended and you moved to a Skilled Worker visa, you would need 12 months on that visa before applying for long residence.",
          "例如：您持學生及畢業生簽證 7 年後轉為配偶簽證 2.5 年，其後再續簽 2.5 年。您只需再等 6 個月便可滿十年並遞交申請。但如果關係結束，您改為申請技術工作簽證，則須持有該簽證滿 12 個月，才可申請長期居留。")}</p>
    <aside class="callout">
      <p><strong>{L("Thinking of applying under long residence?", "考慮申請十年長期居留？")}</strong> {L("Absence calculations are easy to get wrong. We can check your travel history against all three tests before you apply.",
                                                                                                                       "缺席日數的計算很容易出錯。我們可以在您遞交申請前，按三項測試核對您的出入境紀錄。")}</p>
      <a class="btn btn-ink btn-sm" href="contact.html?matter=immigration">{L("Ask us to check", "請我們核對")}</a>
    </aside>
  </div>
</article>
{contact_band()}'''
    page("long-residence.html", key="insights", title=L("10-year long residence rules clarified", "十年長期居留新規定"),
         description=L("How the Home Office now calculates absences for the 10-year long residence route after the April 2024 changes.",
                       "內政部在 2024 年 4 月修訂後如何計算十年長期居留的缺席日數。"), body=body)


# ---------------------------------------------------------------- contact
def contact():
    opts = "".join(f'<option value="{s["id"]}">{T(s["title"])}</option>' for s in SERVICES)
    body = f'''{page_head(L("Contact", "聯繫我們"), L("We speak your language.", "我們說您的語言。"),
        L("We are here to listen, and can discuss your matter in Mandarin, Cantonese or English.", "我們傾聽您的需要，並可以普通話、廣東話或英語與您溝通。"))}
<section class="section section-tight">
  <div class="wrap contact-grid">
    <form class="enquiry" id="enquiry" novalidate data-email="{EMAIL}" data-subject="{L("Website enquiry", "網站諮詢")}">
      <h2>{L("Send an enquiry", "提交諮詢")}</h2>
      <p class="form-hint">{L("To help us handle it efficiently, first describe the current situation, then what you want to achieve.",
                               "為了更高效地處理您的諮詢，請先描述目前的情況，再告訴我們您想達成的目標。")}</p>
      <div class="field-row">
        <label>{L("Name", "姓名")}<input name="name" required autocomplete="name"></label>
        <label>{L("Email", "電郵")}<input name="email" type="email" required autocomplete="email"></label>
      </div>
      <div class="field-row">
        <label>{L("Phone or WeChat (optional)", "電話或微信（選填）")}<input name="phone" autocomplete="tel"></label>
        <label>{L("Preferred language", "希望使用的語言")}
          <select name="language"><option>English</option><option>普通话 Mandarin</option><option>廣東話 Cantonese</option></select></label>
      </div>
      <label>{L("Area of law", "法律範疇")}<select name="matter"><option value="">{L("Not sure", "不確定")}</option>{opts}</select></label>
      <label>{L("1 · The current situation", "1 · 目前的情況")}<textarea name="situation" rows="4" required placeholder="{L("What has happened so far, any deadlines, documents you have", "目前發生了什麼、是否有期限、手上有哪些文件")}"></textarea></label>
      <label>{L("2 · What you want to achieve", "2 · 您想達成的目標")}<textarea name="goal" rows="3" required placeholder="{L("The outcome you're hoping for", "您希望得到的結果")}"></textarea></label>
      <p class="form-note">{L("This opens your email app with the message ready to send. Please don't include passport numbers or bank details at this stage.",
                               "提交後會開啟您的電郵程式，信件已預先填好。此階段請勿提供護照號碼或銀行資料。")}</p>
      <p class="form-error" role="alert" hidden>{L("Please fill in your name, email and both questions.", "請填寫姓名、電郵及兩個問題。")}</p>
      <button class="btn btn-ink" type="submit">{L("Prepare email", "準備電郵")} {icon("arrow", "ic ic-sm")}</button>
    </form>
    <aside class="contact-side">
      <div class="contact-card">
        <h2>{L("Lu Oliphant Solicitors LLP", "Lu Oliphant 律師事務所")}</h2>
        <a class="contact-item" href="{TEL_HREF}">{icon("phone")}<span><em>{L("Telephone", "電話")}</em>{TEL_INTL}</span></a>
        <a class="contact-item" href="mailto:{EMAIL}">{icon("mail")}<span><em>{L("Email", "電郵")}</em>{EMAIL}</span></a>
        <a class="contact-item" href="{MAPS}" target="_blank" rel="noopener">{icon("pin")}<span><em>{L("Office", "辦公室")}</em>{ADDRESS_1}, {ADDRESS_2}</span></a>
        <p class="small">{L("A short walk from Euston Square, Euston and Warren Street stations. Please call ahead to arrange a meeting.",
                            "步行可達 Euston Square、Euston 及 Warren Street 站。請預先致電預約會面。")}</p>
      </div>
      <div class="contact-card contact-card-quiet">
        <h3>{L("Not happy with our service?", "對我們的服務不滿意？")}</h3>
        <p class="small">{L("Tell us so we can put it right.", "請告訴我們，讓我們改善。")} <a href="complaints.html">{L("Our complaints procedure", "投訴程序")}</a></p>
      </div>
    </aside>
  </div>
</section>'''
    page("contact.html", key="contact", title=L("Contact", "聯繫我們"),
         description=L("Contact Lu Oliphant Solicitors at 210 Euston Road, London NW1 2DA. 020 8952 8448, info@luoliphant.com. English, Mandarin and Cantonese.",
                       "聯繫 Lu Oliphant 律師事務所：210 Euston Road, London NW1 2DA。電話 020 8952 8448，電郵 info@luoliphant.com。英語、普通話及廣東話服務。"),
         body=body)


# ---------------------------------------------------------------- complaints
def complaints():
    steps = [
        (L("Within 5 days", "5 日內"), L("We acknowledge your complaint in writing and send you a copy of this procedure.", "我們以書面確認收到投訴，並附上本程序副本。")),
        (L("Investigation", "調查"), L("Our client care partner, Mr James Lau, reviews your file and speaks to the person who acted for you.", "客戶服務負責人 James Lau 先生會審閱您的檔案，並與負責您案件的同事了解情況。")),
        (L("Within 14 days", "14 日內"), L("Mr Lau invites you to a meeting to discuss and, we hope, resolve the complaint. He confirms what was agreed in writing within 3 days of the meeting.", "Lau 先生會邀請您會面商討，盡力解決問題，並在會面後 3 日內以書面確認雙方同意的方案。")),
        (L("Within 21 days", "21 日內"), L("If a meeting isn't wanted or possible, he sends a detailed written reply with his proposals instead.", "如您不希望或無法會面，他會以書面詳細回覆並提出解決建議。")),
        (L("Review", "覆核"), L("Still not satisfied? Tell us why. Another partner may review the decision, and we confirm our final position within 14 days.", "如仍不滿意，請告訴我們原因。我們可能安排另一位合夥人覆核，並在 14 日內確認最終立場。")),
    ]
    tl = "".join(f'<li><span class="tl-when">{w}</span><p>{p}</p></li>' for w, p in steps)
    body = f'''{page_head(L("Complaints", "投訴"), L("If something goes wrong, tell us.", "如有問題，請告訴我們。"),
        L("We are committed to a high-quality legal service. Telling us when we fall short helps us improve.", "我們致力提供高質素的法律服務。您的意見能幫助我們改進。"))}
<section class="section section-tight">
  <div class="wrap two-col two-col-head">
    <div class="prose">
      <h2>{L("How to complain", "如何投訴")}</h2>
      <p>{L("Contact us as soon as you are aware of the problem. Write to:", "請在發現問題後盡快聯繫我們，來函請寄：")}</p>
      <address>Mr James Lau<br>Lu Oliphant Solicitors LLP<br>{ADDRESS_1}<br>{ADDRESS_2}</address>
      <p>{L("or email", "或電郵至")} <a href="mailto:{EMAIL}">{EMAIL}</a>. {L("We have eight weeks to resolve your complaint. If we change any timescale we will tell you why.", "我們有八星期處理您的投訴。如需更改任何時限，我們會告知原因。")}</p>
    </div>
    <ol class="timeline">{tl}</ol>
  </div>
  <div class="wrap two-col">
    <div class="prose-card">
      <h3>{L("If we can't resolve it: the Legal Ombudsman", "如未能解決：法律申訴專員")}</h3>
      <p>{L("The Legal Ombudsman looks at complaints independently. You must complain to them within six months of our final response, and no more than one year from the problem, or from when you should reasonably have known about it.",
            "法律申訴專員會獨立審視投訴。您須在收到我們最終回覆後六個月內提出，且不超過問題發生日起一年，或您理應知悉問題之日起一年。")}</p>
      {arrow_link("https://www.legalombudsman.org.uk/", "legalombudsman.org.uk", ext=True)}
    </div>
    <div class="prose-card">
      <h3>{L("Concerns about our behaviour: the SRA", "對操守的關注：律師監管局")}</h3>
      <p>{L("The Solicitors Regulation Authority can help if you are concerned about dishonesty, the handling of your money, or unfair treatment because of age, disability or another characteristic.",
            "如您關注不誠實行為、款項處理，或因年齡、殘疾等特徵受到不公平對待，可聯繫英國律師監管局。")}</p>
      {arrow_link("https://www.sra.org.uk/consumers/problems/report-solicitor/", "sra.org.uk", ext=True)}
    </div>
  </div>
</section>'''
    page("complaints.html", key="complaints", title=L("Complaints procedure", "投訴程序"),
         description=L("How to make a complaint to Lu Oliphant Solicitors LLP, timescales, and the Legal Ombudsman and SRA.", "如何向 Lu Oliphant 律師事務所投訴、處理時限，以及法律申訴專員和律師監管局資料。"),
         body=body)


# ---------------------------------------------------------------- careers
def careers():
    reqs = [
        L("2:1 law degree or equivalent, ideally with a postgraduate law degree", "法律學位二級甲等或同等學歷，具法律研究生學位更佳"),
        L("Around 2 years' PQE in commercial and residential property", "約兩年商業及住宅物業執業經驗"),
        L("Fluent English with strong drafting and communication skills", "英語流利，草擬文件及溝通能力強"),
        L("New-build and high-net-worth experience is an advantage", "具新樓及高淨值客戶經驗者優先"),
        L("Commercial acumen, attention to detail and proven billing", "具商業觸覺、注重細節，並有良好計費紀錄"),
        L("Mandarin or Cantonese, and LEAP experience, are a bonus", "懂普通話或廣東話、熟悉 LEAP 系統者更佳"),
    ]
    req = "".join(f"<li>{icon('check', 'ic ic-sm')}<span>{r}</span></li>" for r in reqs)
    body = f'''{page_head(L("Careers", "招聘"), L("Grow your career in law with us.", "與我們一起發展法律事業。"),
        L("A CQS-accredited boutique firm in central London, advising clients in the UK and overseas, especially high-net-worth clients from the Far East.",
          "位於倫敦市中心、獲 CQS 認證的精品律師事務所，客戶遍及英國及海外，尤其是來自遠東的高淨值客戶。"))}
<section class="section section-tight">
  <div class="wrap two-col two-col-head">
    <article class="job">
      <p class="eyebrow">{L("Open position", "招聘職位")}</p>
      <h2>{L("Assistant Solicitor / Senior Paralegal, Commercial & Residential Property", "助理律師／高級律師助理（商業及住宅物業）")}</h2>
      <p class="job-meta">{L("Permanent · Full time · London NW1 · Two days working from home", "長期 · 全職 · 倫敦 NW1 · 每週兩天在家工作")}</p>
      <p>{L("A mix of commercial and residential work: acquisitions and sales, lease assignments, funding and finance, acting for lenders, landlord and tenant, rent reviews, refinancing and new-build developments, for high-net-worth individuals and companies. The role includes business development in the UK and abroad, and reports to the Principal Solicitor.",
            "工作涵蓋商業及住宅物業：收購及出售、租約轉讓、融資、代表貸款方、業主與租客事務、租金檢討、再融資及新樓項目，客戶包括高淨值人士及企業。職位亦包括本地及國際業務拓展，直接向主管律師匯報。")}</p>
      <h3 class="mini">{L("You will bring", "任職要求")}</h3>
      <ul class="ticks">{req}</ul>
      <p><strong>{L("Package:", "待遇：")}</strong> {L("salary depending on experience, discretionary bonus, private health insurance.", "薪酬視乎經驗而定，另有酌情花紅及私人醫療保險。")}</p>
    </article>
    <aside class="contact-card">
      <h3>{L("How to apply", "申請方法")}</h3>
      <p>{L("Send your CV and a cover letter to", "請將履歷及求職信寄至")}</p>
      <a class="contact-item" href="mailto:management@luoliphant.com">{icon("mail")}<span>management@luoliphant.com</span></a>
      <p class="small">{L("We are not accepting applications from agencies.", "恕不接受招聘代理申請。")}</p>
    </aside>
  </div>
</section>'''
    page("careers.html", key="careers", title=L("Careers", "招聘"),
         description=L("Career opportunities at Lu Oliphant Solicitors LLP in central London.", "Lu Oliphant 律師事務所的招聘職位。"), body=body)


def build():
    for lang in LANGS:
        set_lang(lang)
        home(); services(); fees(); team(); testimonials(); insights(); article(); contact(); complaints(); careers()
    print("built", len(LANGS), "languages")


if __name__ == "__main__":
    build()
