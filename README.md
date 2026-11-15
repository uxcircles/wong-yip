# 曼城黃葉（香港）會計師樓：網站重新設計概念

UX CIRCLES 為 Wong & Yip Accountants Ltd 製作的**非官方**重新設計概念，並非該會計師樓的官方網站（官方網站：https://www.wongyipaccountants.co.uk/）。每頁頂部均有「Concept / 概念」標示，並設有 `noindex` 及 `robots.txt`，不會被搜尋引擎收錄。

網址：https://uxcircles.github.io/wong-yip/ （中文）· https://uxcircles.github.io/wong-yip/en/ （English）

## 頁面

| 頁面 | 中文 | English |
|---|---|---|
| 首頁：印花稅計算、HMRC 日子、服務、客戶行業、Henry Yip、客戶評語、地圖及查詢表格 | `index.html` | `en/index.html` |
| 服務（個人／公司／物業，共十項） | `services.html` | `en/services.html` |
| 印花稅計算、2025 年 4 月的改變、常見問題、海外業主 | `stamp-duty.html` | `en/stamp-duty.html` |
| 關於我們 | `about.html` | `en/about.html` |
| 私隱及無障礙（草擬） | `privacy.html` | `en/privacy.html` |
| 404 | `404.html` | |

## 如何修改

所有頁面由 `_build/pages.py` 產生，文字以 `L(英文, 中文)` 並排寫在一起：

```bash
python3 _build/pages.py      # 重建所有 HTML
python3 _build/fonts.py      # 改了中文字之後重新子集化字型
```

- 樣式：`assets/site.css`；互動：`assets/site.js`（印花稅計算、HMRC 日子、表格、地圖）；地圖配色：`assets/map.js` 頂部的 `C`
- 修改 CSS/JS 後，把 `_build/pages.py` 的 `V` 加一，避免手機繼續顯示舊檔案
- 表格沒有後台：按下後開啟 WhatsApp 或電郵程式並填好內容，網站不儲存任何資料

## 設計概念

- **標誌元素**：黃葉自己的 W·Y 標誌（黃色 W 與橙色 Y 交織），用在頁首、首屏、地圖圖釘、favicon、頁尾及 404。各區塊底部的 V 形缺口，取自同一個標誌。
- **首屏類型**：`tool-first`。客戶多是由香港來英、正準備買樓的人，最常見的問題就是印花稅。首屏直接放計算機：首次置業／只有這一個物業／多於一個物業，以及 2% 非居民附加費，並列出每一級的稅款。
- **字型**：Red Hat Display（粗而幾何，接近標誌字款）、Red Hat Text（內文）、Red Hat Mono（數字及收據）、Chiron Hei HK（香港字形的黑體）。
- **顏色**：全部取自標誌：紫 #360064、黃 #ffe900、橙 #ff9b00，配米白紙色。
- **標題**：「買樓之前，先計清楚印花稅」／ “Know your stamp duty before you make an offer”
- **與之前會計師概念的分別**：之前四個會計師網站都是「左文字、右卡片或拱形照片」，用海軍藍、金色或紅色，字型為 Inter、Fraunces、Hanken Grotesk。這一個沒有照片和資料卡，首屏是工具；用紫黃配色，字型是新的 Red Hat 家族。

## 需要黃葉確認的資料

- **印花稅頁面**：現有網站仍用 2022 年 9 月的稅率（£250,000 起徵、首次置業 £425,000 免稅），2025 年 4 月 1 日起已改為 £125,000 及 £300,000（GOV.UK）。本概念使用現行稅率。
- **其他過時數字**：現有網站寫增值稅登記門檻為 £85,000（2024 年 4 月起為 £90,000）；自我評估頁仍是 2022/23 稅率表（附加稅率門檻 £150,000，現為 £125,140）及舊的資產增值稅率（10%/20%、18%/28%，2024 年 10 月 30 日起統一為 18%/24%）。
- Henry Yip 的介紹沿用現有網站文字（non-dom 專家）。non-dom 制度已於 2025 年 4 月 6 日由以居住為基礎的新制度取代，建議更新。
- 辦公時間：現有網站沒有公佈，所以本概念沒有列出。
- 客戶評語：全部取自現有網站，未經改動。
- 私隱聲明為草擬，須黃葉審閱。
- 照片：沒有使用任何圖庫相片，只用了黃葉自己的標誌。
- 插圖：全部自行繪製，純剪紙風格（紙紋加陰影，沒有線條），每張只有兩三個大形狀，顏色取自黃葉標誌，沒有圖庫圖片。
  - 首頁首屏：香港唐樓、紙飛機、Ancoats 紡織廠及 Rochdale 運河；印花稅頁首屏：SDLT 收據及鎖匙
  - 服務：報稅表與 1 月 31 日月曆、小店、糧單信封與硬幣、TO LET 紅磚屋；404：紙飛機
  - 原檔由 `_build/illo/simple.py`（共用 `_build/illo/paper.py`）產生於 `assets/illo/`；網站使用匯出的 WebP，手機不必運算 SVG 濾鏡
- 地圖：MapLibre GL JS（BSD）＋ OpenFreeMap；步行時間來自 routing.openstreetmap.de 的路線。
