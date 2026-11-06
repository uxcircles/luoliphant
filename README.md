# luoliphant.com — Lu Oliphant Solicitors LLP 改版提案

[Lu Oliphant Solicitors LLP](https://www.luoliphant.com/) 的網站改版：位於倫敦 Euston Road 的精品律師事務所（1999 年成立），客戶以海外投資者及來自中國內地、香港的高淨值客戶為主，業務涵蓋物業轉讓、移民、公司法、勞動法、訴訟、遺囑及遺產。純靜態 HTML / CSS / JS，任何靜態主機都能直接部署。

> **概念設計展示**：這是由 [UX CIRCLES](https://ux-circles.com/web) 設計的改版提案，並非 Lu Oliphant 官方網站。
> 每頁頂端有「Concept」標示列，所有頁面都設為 `noindex`，`robots.txt` 也禁止搜尋引擎收錄，避免和官方網站搶搜尋結果。
> 如果律所正式採用：刪掉 `_build/layout.py` 裡的 `concept_bar()`、頁尾的 `concept-note` 和 `<meta name="robots" content="noindex, nofollow">`，重新建置，並把 `robots.txt` 改回 `Allow: /`。

## 設計方向

- 沿用原網站的標語「Small world. Limitless vision. / 世界有限，視野無邊。」
- 象牙白紙感底色、深夜藍、印章紅；以「LO」方印作為三種語言共用的品牌符號
- 首頁「兩地時區」卡片：即時顯示倫敦與北京／香港時間，呼應律所服務海外客戶的定位
- 原網站的收費資料散落在五個子頁、純文字排版，改為一頁表格化收費，並加入物業轉讓律師費計算器
- 原網站聯絡頁的建議（「先描述現況，再說明想達成的目標」）直接變成諮詢表單的兩個欄位

## 語言

| 路徑 | 版本 |
|---|---|
| `/` | English（預設） |
| `/zh/` | 繁體中文（原網站中文版為繁體） |
| `/sc/` | 简体中文（由繁體自動轉換，方便內地客戶） |

## 頁面

| 頁面 | 內容 |
|---|---|
| `index.html` | 首頁：主視覺 + 兩地時區、重點數字、十個業務範疇、工作方式、收費摘要、客戶感謝信、團隊、法律資訊、社區贊助 |
| `services.html` | 十個業務範疇：簡介、服務清單、對應收費、「就此諮詢」（自動帶入表單） |
| `fees.html` | 物業轉讓（計算器 + 三張收費表 + 雜費 + 時程）、移民、遺產認證、勞動審裁、追討債務 |
| `team.html` | 律所介紹、五位律師、華人健康福祉診所贊助、招聘入口 |
| `testimonials.html` | 客戶感謝信，可按事務類別篩選 |
| `insights.html`、`long-residence.html` | 文章列表；十年長期居留新規定全文（三項測試以數字卡呈現） |
| `contact.html` | 諮詢表單（開啟預先填好的電郵，不需要後端）、聯絡方式 |
| `complaints.html` | 投訴程序時間軸、Legal Ombudsman 及 SRA |
| `careers.html` | 招聘職位 |

手機版底部固定「致電 / 電郵 / 諮詢」列。

## 待律所確認

- SRA 編號（頁尾目前只寫「受 SRA 授權及監管」）及 SRA 數碼徽章
- 辦公時間（未提供，所以沒有「現在營業」顯示）
- Mei Lu、James Lau、Nicholas Woo 的工作語言（原網站未列明，暫不顯示）
- 律師照片（目前以姓名縮寫代替）
- 律所中文名稱（原網站未使用中文名稱）
- 隱私政策頁暫時連回官方網站

## 修改與建置

HTML 由 `_build/` 產生：

- 頁面內容：`_build/pages.py`（文字寫成 `L(English, 中文)`）
- 業務範疇、團隊、客戶感謝信、文章：`_build/data.py`
- 收費表：`_build/fees.py`
- 頁首 / 頁尾 / 聯絡資料：`_build/layout.py`

中文只需寫一次（繁簡皆可），建置時用 OpenCC 分別轉成繁體和簡體。

```
pip install opencc-python-reimplemented
python3 _build/pages.py
```

需要 Python 3.12 以上。本機預覽：

```
python3 -m http.server 5181
```

然後打開 http://localhost:5181。

## 結構

```
*.html              English
zh/                 繁體中文
sc/                 简体中文
assets/css/style.css
assets/js/main.js   手機選單、時區時鐘、收費計算器、段落定位、感謝信篩選、諮詢表單
assets/img/favicon.svg
_build/             頁面產生器
robots.txt
```
