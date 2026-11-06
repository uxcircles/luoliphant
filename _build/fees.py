"""Fee schedules from luoliphant.com/pricing (conveyancing, immigration, probate, employment, debt recovery)."""

PARTNER_RATES = ("£400 + VAT an hour for equity partners, £350 + VAT for salaried partners",
                 "權益合夥人每小時 £400 + VAT，受薪合夥人每小時 £350 + VAT")

# Conveyancing bands: upper limit of price band (None = above £3m), fee, or percentage above £3m.
BANDS = [
    (500_000, ("Below £500,000", "£500,000 以下")),
    (1_000_000, ("£500,000 – £1m", "£50 萬 – £100 萬")),
    (1_500_000, ("£1m – £1.5m", "£100 萬 – £150 萬")),
    (2_000_000, ("£1.5m – £2m", "£150 萬 – £200 萬")),
    (3_000_000, ("£2m – £3m", "£200 萬 – £300 萬")),
    (None, ("Above £3m", "£300 萬以上")),
]

CONVEYANCING = [
    {
        "id": "freehold",
        "title": ("Secondary freehold (non-estate)", "二手永久業權（非屋苑）"),
        "fees": [2500, 2800, 3300, 4000, 5000], "pct": 0.2,
    },
    {
        "id": "leasehold",
        "title": ("New build, estates & secondary leasehold", "新樓、屋苑及二手租賃業權"),
        "fees": [2800, 3500, 4200, 5000, 6000], "pct": 0.25,
    },
    {
        "id": "equity",
        "title": ("Transfer of equity", "權益轉讓"),
        "fees": [2000, 2500, 3000, 3500, 4000], "pct": 0.175,
    },
]

DISBURSEMENTS = [
    (("Search fees", "查冊費"), "£300 – £700 + VAT"),
    (("HM Land Registry fee", "土地註冊處費用"), ("£40 – £910, by value", "£40 – £910，按物業價值")),
    (("Electronic money transfer", "電子匯款費"), ("£18 inc. VAT per transfer", "每次 £18（含 VAT）")),
    (("Notice of transfer (leasehold)", "轉讓通知費（租賃業權）"), ("Often £50 – £200", "通常 £50 – £200")),
    (("Notice of charge (if mortgaged)", "押記通知費（如有按揭）"), ("Often £50 – £200", "通常 £50 – £200")),
    (("Deed of covenant", "契諾契據費"), ("Often £50 – £300", "通常 £50 – £300")),
    (("Certificate of compliance", "合規證明費"), ("Often £50 – £200", "通常 £50 – £200")),
    (("HMRC agent fee for the SDLT return", "代辦印花稅申報"), "£100 + VAT"),
]

STAGES = [
    ("Taking your instructions and initial advice", "接受委託及提供初步建議"),
    ("Checking funds and liaising with the lender's solicitors", "確認資金並與貸款方律師聯絡"),
    ("Reviewing the contract documents and carrying out searches", "審閱合約文件並進行查冊"),
    ("Raising enquiries with the seller's solicitor", "向賣方律師提出查詢"),
    ("Advising you on everything received, including the mortgage offer", "就所有文件及按揭條件向您解釋"),
    ("Signing, agreeing completion and exchanging contracts", "簽署合約、確定成交日並交換合約"),
    ("Completion, paying SDLT and registering at the Land Registry", "完成交易、繳交印花稅並於土地註冊處登記"),
]

IMMIGRATION = [
    (("Tier 1 (Investor)", "投資者簽證（Tier 1）"), [
        (("Extension", "續簽"), "£6,000 – £10,000 + VAT"),
        (("Dependant, each", "每名受養人"), ("£900 + VAT if applicable", "£900（如適用另加 VAT）")),
    ]),
    (("Global Talent", "全球人才簽證"), [
        (("Initial application", "首次申請"), ("£5,000 – £10,000 + VAT if applicable", "£5,000 – £10,000（如適用另加 VAT）")),
        (("Extension", "續簽"), "£3,000 – £5,000 + VAT"),
        (("Dependant, each", "每名受養人"), ("£900 + VAT if applicable", "£900（如適用另加 VAT）")),
    ]),
    (("Innovator Founder", "創新創業者簽證"), [
        (("Initial application", "首次申請"), ("£5,000 – £10,000 + VAT if applicable", "£5,000 – £10,000（如適用另加 VAT）")),
        (("Extension", "續簽"), "£5,000 – £8,000 + VAT"),
        (("Dependant, each", "每名受養人"), ("£900 + VAT if applicable", "£900（如適用另加 VAT）")),
    ]),
    (("Skilled Worker & intra-company transfer", "技術工作簽證及跨國公司調派"), [
        (("Skilled Worker or ICT application", "技術工作或跨國調派申請"), ("£1,800 – £2,500, no VAT", "£1,800 – £2,500（無 VAT）")),
        (("Extension", "續簽"), "£1,800 – £2,000 + VAT"),
        (("Dependant, each", "每名受養人"), ("£900 + VAT if applicable", "£900（如適用另加 VAT）")),
    ]),
    (("Indefinite Leave to Remain", "永久居留（ILR）"), [
        (("Tier 1 Investor or Entrepreneur", "投資者或企業家簽證轉永居"), "£5,000 – £10,000 + VAT"),
        (("Other points-based categories", "其他積分制類別"), "£2,000 – £3,500 + VAT"),
        (("Dependant under points-based system, each", "積分制受養人（每名）"), ("£900 + VAT if applicable", "£900（如適用另加 VAT）")),
        (("Settlement under all other routes", "其他途徑的定居申請"), "£5,000 – £8,000 + VAT"),
        (("Dependant under other routes", "其他途徑受養人"), "£1,200 + VAT"),
    ]),
    (("Naturalisation", "入籍英國"), [
        (("Application", "申請"), "£1,800 – £2,200 + VAT"),
    ]),
]

EMPLOYMENT = [
    (("Simple case", "簡單個案"), "£5,000 – £7,500", "£7,500 – £12,000"),
    (("Medium complexity", "中等複雜"), "£7,500 – £12,000", "£12,000 – £15,000"),
    (("High complexity", "高度複雜"), "£12,000 – £15,000", "£15,000 – £20,000"),
]
