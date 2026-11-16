# Family Trip Guide｜家人朋友旅遊導遊

**把旅行大小事整理好，讓主揪帶得安心，同行的人也能用手機自己找到需要的資訊。**

這是一套給 AI 使用的「旅行工作指南」（skill）。裝進 Gemini 或 Claude 後，你可以像平常聊天一樣，請它協助選目的地、排路線、整理預約、分帳、準備行前教學與臨時備案。**不需要會寫程式，也不需要 GitHub 帳號。**

第一次使用：**選你常用的 AI → 下載對應 ZIP → 上傳並啟用 → 貼上旅行需求。**

如果打開連結先看到一堆檔案，往下滑到這份說明即可，**不用點綠色 Code 按鈕**。也可以直接分享 [跳到使用說明的連結](https://github.com/chunwenchiang-hue/family-trip-guide#readme)。

第一次只要選 **Gemini 或 Claude 其中一個**，不需要兩邊都安裝。建議先用電腦瀏覽器完成安裝；手機也可先看範例，再依帳號支援的入口操作。

[Gemini 安裝](#gemini-安裝步驟) · [Claude 安裝](#claude-安裝步驟) · [複製安裝指令](#把安裝指令貼給-ai) · [開始規劃範例](#開始規劃旅行直接複製修改) · [複製分享文字](#複製分享給朋友)

### 下載後找不到檔案？

- 電腦：先看瀏覽器的下載清單或「下載項目／Downloads」資料夾。
- iPhone／iPad：先看瀏覽器下載清單，再到「檔案」App 找所選的下載位置；常見是 iCloud Drive 或「我的 iPhone」裡的「下載項目」。Android 可查看瀏覽器下載清單或檔案 App 的 Downloads。
- 若從 LINE 等 App 打開後無法下載或選檔，改用 Safari／Chrome 開啟這個頁面再試。
- 上傳時認完整檔名：Gemini 用 `family-trip-guide-gemini.zip`，Claude 用 `family-trip-guide-claude.zip`。**不要選 GitHub 的 Source code ZIP，也不要選另一平台的 ZIP。**
- 部分瀏覽器會自動解壓縮；上傳步驟若要求 ZIP，請從下載清單找原 ZIP。找不到時換另一個瀏覽器重新下載，不用修改安全設定。

## 它能幫你準備什麼？

| 旅行階段 | 可以請 AI 協助的事 |
| --- | --- |
| 還沒決定去哪 | 比較目的地和日期，了解每個人的願望、預算與體力 |
| 開始排行程 | 挑景點和餐廳、安排交通與休息、減少拖行李、準備雨天與人潮備案 |
| 預約與費用 | 整理要訂什麼、誰負責、截止日、確認資料與分帳 |
| 出發前 | 準備手機行程入口、QR、預約查找方式、離線備份與五分鐘教學 |
| 到了當地 | 找路、找預約、查外語溝通卡、聽導覽，依當天情況調整安排 |

手機網站、QR、音檔和實際預約是否能做出來，要看當次 AI 有哪些工具。它應該清楚告訴你哪些已完成、哪些還需要你操作。**安裝這套指南，不代表 AI 已經取得訂票、付款或發布網站的能力。**

## Gemini 安裝步驟

1. **[下載 Gemini 安裝檔](https://github.com/chunwenchiang-hue/family-trip-guide/releases/latest/download/family-trip-guide-gemini.zip)**。保留 ZIP，不必解壓縮。
2. 登入 [Gemini](https://gemini.google.com/)，在側邊欄找 **自訂／Customize → Skills**。沒有「自訂」時，先展開「更多」。
3. 點 **建立／Create → 上傳／Upload**，選剛下載的 `family-trip-guide-gemini.zip`。
4. 完成上傳、檢查內容，再按 **建立／Create**。確認這個技能已安裝；若動作選單仍顯示「安裝」，再點一次。
5. 開啟新對話，**輸入 `@`，從選單點選 `family-trip-guide`**，再貼上下面的旅行範例。

**裝好了嗎？** 技能出現在已安裝清單，或選單出現「立即使用／解除安裝」；對話中也能從 `@` 選單選到它。只在訊息裡打出技能名稱，不一定真的有載入。

### 只有 Gems，沒有 Skills？

可以用 Gems 的方式載入同一套內容：

1. 下載 [Gems 指令檔](https://github.com/chunwenchiang-hue/family-trip-guide/releases/latest/download/gemini-gem-instructions.txt) 和 [完整知識檔](https://github.com/chunwenchiang-hue/family-trip-guide/releases/latest/download/family-trip-guide-knowledge.txt)。
2. 在 Gemini 建立新的 Gem，名稱填「家人朋友旅遊導遊」。
3. 把指令檔的**全部文字**貼進「指令／Instructions」。
4. 把完整知識檔上傳至「知識／Knowledge」，儲存後從這個 Gem 開始聊天。

如果兩個入口都找不到，先看 [常見問題](#常見問題)。選單會隨帳號與介面更新而不同；可對照 [Google 官方 Skills 說明](https://support.google.com/gemini/answer/17094296?hl=en)。

## Claude 安裝步驟

1. **[下載 Claude 安裝檔](https://github.com/chunwenchiang-hue/family-trip-guide/releases/latest/download/family-trip-guide-claude.zip)**。保留 ZIP，不必解壓縮。
2. 登入 [Claude](https://claude.ai/)，進入 **自訂／Customize → Skills**。
3. 點 **＋ → 建立技能／Create skill → 上傳技能／Upload a skill**。
4. 選擇 `family-trip-guide-claude.zip`，完成匯入。
5. 確認 `family-trip-guide` 的**開關已開啟**，再開新對話，貼上下面的旅行範例，第一句請它使用這個技能。

**裝好了嗎？** Skills 清單裡看得到名稱，而且開關開啟。把 ZIP 當一般聊天附件傳給 Claude，不等於裝進 Skills。

若無法上傳或啟用，到 **設定／Settings → 功能／Capabilities** 確認「程式執行與檔案建立／Code execution and file creation」（有些介面稱「Create and edit files」）已開啟。公司帳號可能需要管理員開放。詳見 [Claude 官方安裝說明](https://support.claude.com/en/articles/12512180-use-skills-in-claude)。

## 把安裝指令貼給 AI

想先讓 AI 協助判斷怎麼安裝？複製整段到你要使用的 AI：

```text
請幫我安裝並啟用 Family Trip Guide（家人朋友旅遊導遊）：
https://github.com/chunwenchiang-hue/family-trip-guide/blob/main/INSTALL.md

請依你目前平台的實際能力操作。
如果無法替我安裝到帳號，請直接給我對應下載檔和需要手動做的步驟。
完成後回報：實際版本、是否已安裝、是否已啟用；不能確認的請明說。
不要把讀過連結或在這次對話使用，說成已永久安裝。
```

**貼連結不保證能自動安裝。** 有檔案或技能管理工具的 AI 可以依入口處理；一般網頁聊天若沒有修改 Skills 的權限，仍需要你按上面的步驟上傳一次。

## 開始規劃旅行：直接複製修改

不必一開始就把所有細節想完。把知道的填上，不知道的寫「未定」，讓 AI 帶你一步步補齊。Gemini 請先從 `@` 選單選取技能；Claude 請先確認技能開關已開。

### 第一次先試這段

先改下面的方括號內容，再複製文字框內的文字到 AI 對話，按傳送。不要把這段貼回 GitHub，也不用連同前後的三個反引號一起複製。

```text
請使用 family-trip-guide（家人朋友旅遊導遊），開始規劃我的旅行。
出發地：[填城市]
目的地：[填城市，還沒決定就寫未定]
日期與天數：[填年份、月份、天數，或未定]
同行者：[填人數與大致年齡層]
每人預算：[填金額、幣別，以及是否包含機票住宿，或未定]
最想做的事：[填願望，或未定]
需要留意：[填步行、階梯、飲食、行李需求；不知道就寫待確認]
已訂項目：[填已訂內容，或無]

請先讀取這個 skill 的主指引及本次相關參考文件；讀不到時直說。
先整理已知與待確認事項，再問最重要的問題，每輪最多 3 題。
缺少資料先保留未定；先不要訂票、付款或製作整批音檔。
```

**第一則回覆怎樣才算有開始？** 應先整理你提供的資訊與缺口，說明下一步；需要補問時，每輪最多三題。目的地未定時可先比較少量選擇，不能憑空補上限制、預約或「已完成」成果。它說「我會使用」不等於證明已讀取；若明說讀不到指引或參考文件，先回安裝頁確認啟用，再開新對話選取技能。

想檢查安裝後的行為，可再跑 [三個小測試](docs/platforms.md#匯入後的三個小測試)。這能檢查回答是否符合流程，不能單靠一句回答證明帳號已永久安裝。

### 範例一：還不知道去哪裡

```text
請使用 family-trip-guide（家人朋友旅遊導遊），陪我規劃一次家人旅行。

出發地：台北
目的地：未定，想先比較適合的地方
日期與天數：2027 年秋天，約 5～7 天（請改成自己的出發年份）
同行者：4 位成人、1 位長輩
預算：每人約新台幣 5 萬元，包含交通與住宿
我們喜歡：美食、風景、慢慢逛
需要照顧的事：長輩不想走太多階梯，希望少換飯店、少拖行李

先幫我比較 2～3 個可行選擇，說明取捨。
先問最影響決定的問題，每輪不超過 3 題，不要一次排滿所有行程。
```

### 範例二：地方和日期已決定

```text
請使用 family-trip-guide，規劃我們的朋友旅行。

目的地：京都、神戶
日期：2027 年 11 月 10～16 日
同行者：5 位成人
預算：每人約新台幣 6 萬元
願望：賞楓、散步、吃在地美食，每天留休息時間
限制：移動日盡量少拖行李；飲食限制尚待逐人確認
已訂項目：機票已訂，住宿未訂

先整理已知資料、缺少資訊和要決定的順序，再提出每日行程草案。
交通請說明選擇理由，遇到雨天、人潮或疲累時要有備案。
預約與付款先整理選項和條件，等我明確授權後再執行。

行程確認後，再依可用工具準備同行手機指南、離線備份、
預約查找方式、費用表與五分鐘行前教學。
景點聲音偏好溫暖自然的台灣女聲，先讓我聽短試聽，確認後才整批製作。
```

### 範例三：已經有行程，請幫我補漏

```text
請使用 family-trip-guide，從同行夥伴的角度檢查我接下來提供的行程。

檢查範圍：
共用說明／備忘錄 → 掃 QR → 下載最新版 → 重新開啟
→ 播放導覽 → 找到預約 → 飛航模式下查重要資料。

也請檢查交通銜接、拖行李、休息、雨天備案與費用管理。
原本的預約、PDF 和 QR 都要保留；能直接修好的先修好。
最後分別列出：已修正、仍缺資料、每位旅伴要在自己手機親手測試的項目。
沒有實測過的操作，不要標成通過。
```

以上都是虛構範例，請改成自己的旅行資料。訂單、聯絡方式與票券只放在你信任且有權限的對話或空間，不要貼在這個公開 GitHub 頁面或 Issues。

### 想改天再繼續？

結束前可以請 AI 整理交接摘要，下次貼回來，不必從頭說明：

```text
請整理這次旅行的接續摘要：已確認事項、每位旅伴的願望與限制、
已訂項目、最新檔案位置、未決問題，以及下一步。
請保留未知與待確認事項，讓我下次可以直接接著規劃。
```

## 常見問題

**一定要付費嗎？**  
這份指南以 MIT 授權公開分享，不另外收費。AI 平台的方案、功能與使用額度依各自規定；語音、託管或預約也可能有其他費用。指南不附付費服務，也不會自動替你購買。

**找不到 Skills，或 AI 讀不到 GitHub 連結？**  
先用上方直接下載連結，依平台上傳。Gemini 只有 Gems 時可用備援步驟。若帳號沒有這些功能，可將 [完整知識文字檔](https://github.com/chunwenchiang-hue/family-trip-guide/releases/latest/download/family-trip-guide-knowledge.txt) 當聊天附件，請 AI 讀完後依其規劃；這只是當次對話使用，沒有永久安裝。若連附件也不支援，先確認平台功能與管理限制。

**裝好了，但 Gemini 的 `@` 選單找不到技能？**  
先確認正在使用安裝時的同一個帳號，回 Skills 檢查是否已安裝；更新或取代後可能需要再按「安裝」。再開新對話選取。Claude 也請確認同一帳號／工作空間，以及技能開關已開啟。仍讀不到時可用上面的完整知識文字檔暫時在當次對話使用，並保留「未確認永久載入」的狀態。

**安裝後，為什麼沒有直接訂好票、產生網站或聲音？**  
這套指南教 AI 工作方法；實際操作仍需要對應工具和你的授權。沒有工具時，AI 應先整理可審閱資料，列出還需要你完成的步驟。

**手機下載了 HTML，卻不能按按鈕或播放聲音？**  
手機「檔案」或聊天 App 的預覽可能不支援互動。請依行程附的說明使用支援的瀏覽器或離線方案，並保留文字／PDF 備援。每個人都要在自己的手機測過，不能只測主揪一台。

**如何更新？**  
重新下載最新版，依平台取代或重新匯入；先保留自己的修改。Gemini 取代後要再確認已安裝，Claude 要確認開關仍開啟。上傳的版本不保證自動跟著 GitHub 更新。

**這份指南實際試過嗎？**  
核心版本 **v1.2.0** 已實際匯入 Gemini 與 Claude，完成三個虛構情境的驗收覆蓋：逐人離線檢查、工具與完成狀態、先試聽再整批。初測發現完成狀態誤判，修正後覆測受影響題目通過。詳見 [實測紀錄與範圍](docs/validation.md)；不代表每個帳號和手機都已測過。

## 進一步閱讀

- [完整跨平台教學、三個安裝後小測試](docs/platforms.md)
- [給 AI 的安裝入口](INSTALL.md) · [最新版下載](https://github.com/chunwenchiang-hue/family-trip-guide/releases/latest)
- [同行手機操作與逐人實測](references/companion-flow.md)
- [自然女聲製作方法](references/guide-voice.md)
- [主要旅行流程](SKILL.md)

<details>
<summary>給使用 Codex、Claude Code 或 Gemini CLI 的人</summary>

一般網頁使用者照上面的上傳步驟即可。以下指令適合已使用開發工具的人；既有同名資料夾請先保留自訂修改，不直接覆寫。

**Codex 首次安裝**

```sh
git clone https://github.com/chunwenchiang-hue/family-trip-guide.git ~/.codex/skills/family-trip-guide
```

新對話用 `$family-trip-guide` 加上旅行需求。

**Claude Code 首次安裝**

```sh
git clone https://github.com/chunwenchiang-hue/family-trip-guide.git ~/.claude/skills/family-trip-guide
```

使用 `/family-trip-guide` 加上旅行需求。

**Gemini CLI**

```sh
gemini skills install https://github.com/chunwenchiang-hue/family-trip-guide.git
gemini skills list --all
```

請依工具提示確認載入與授權。完整說明見 [跨平台教學](docs/platforms.md)。使用完整資料夾，保留 `SKILL.md` 與全部 `references/`。

</details>

## 複製分享給朋友

點文字框右上角的複製按鈕，或選取框內全文，就能貼到 LINE、訊息或其他聊天軟體轉傳。

```text
分享一套「家人朋友旅遊導遊」給你 ✈️

可以裝進 Gemini 或 Claude，像平常聊天一樣，請 AI 陪你選目的地、排行程、整理預約、交通、費用和行前準備。不需要會寫程式，也不用 GitHub 帳號。

使用說明：
https://github.com/chunwenchiang-hue/family-trip-guide#readme

選你常用的其中一個 AI，照教學下載、上傳並啟用，再複製「第一次先試這段」，填上旅行需求就能開始；還沒決定的寫「未定」即可。建議第一次先用電腦安裝。

指南免費公開，AI 平台功能與額度依你的帳號而定。只貼連結不一定能自動安裝，頁面有完整操作步驟。
```

## 分享與授權

把 [這個使用說明連結](https://github.com/chunwenchiang-hue/family-trip-guide#readme) 傳給朋友，就可以從安裝開始照做。

本倉庫只分享可重用指引與匿名／虛構範例，不包含私人行程、旅客資料、訂單、票券、PDF、QR 或私人測試截圖。[MIT License](LICENSE) 適用於本倉庫內容；外部服務與素材依各自條款使用。

安裝步驟核對日期：2026-11-16。
