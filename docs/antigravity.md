# 在 Antigravity 使用家人朋友旅遊導遊

給已安裝 **Google Antigravity App、CLI 或 IDE** 的人。這套指南不需要另裝 Gemini 網頁技能，也不需要 API 金鑰。AI 的功能、登入及使用額度依你的 Antigravity 帳號而定。

核心版本：**v1.3.0**。這次新增安裝教學，旅行指引保持同版。安裝方法依 [Google 官方技能文件](https://antigravity.google/docs/skills) 核對（2026-11-17）；尚未在你的裝置跑過模型實測。

## 第一次使用，照這四步走

不需要 GitHub 帳號。若 GitHub 先顯示檔案或程式碼，切到 **Preview／預覽** 看本文；從 LINE 開啟不順時，改用一般瀏覽器。文字框可用右上角複製鈕，或只選框內全文複製，不用包含前後的三個反引號。

1. **先開旅行資料夾。** 在自己的電腦建立一個資料夾，例如「我的旅行」。Antigravity App：左側 **New Project／新增專案 → Add Folder／加入資料夾 → 選「我的旅行」→ Create／建立**。如果是 Antigravity IDE，使用 **File → Open Folder／開啟資料夾**；CLI 則先進到該資料夾再啟動 `agy`。名稱可能隨版本不同，重點是讓這個對話連到你選定的資料夾，別只停在沒有資料夾的首頁聊天。
2. **貼下方安裝文字並送出。** 在 Antigravity 的對話輸入框貼上，不是 GitHub 的編輯框。若 App 問 Local／New worktree，這個新建旅行資料夾選 **Local**，讓技能與旅行資料保存在同一處。
3. **看安裝結果。** 應有實際資料夾位置、v1.3.0 檔案比對結果、主指引與八份參考是否完整。只有「讀過網址」「可以協助」不算裝好；如果沒有檔案操作能力，改用本頁「沒有 Git」的方法。
4. **留在同一個旅行專案開新對話**，貼本頁「第一次開始規劃」的範例。換到其他空白專案，不會自動載入只裝在這個工作區的技能。

工作區建立方式可對照 [官方開始專案說明](https://antigravity.google/docs/getting-started#start-a-project)。原有模型與其他設定沿用即可。

## 最簡單：把這段貼給 Antigravity

完成上方第一步後，把這段貼到 Antigravity 並送出：

```text
請在目前這個旅行工作區安裝 Family Trip Guide v1.3.0：
https://github.com/chunwenchiang-hue/family-trip-guide/blob/main/docs/antigravity.md

請先閱讀這頁的安裝方法，並讀取固定版本 manifest：
https://raw.githubusercontent.com/chunwenchiang-hue/family-trip-guide/v1.3.0/install.json
若不能讀 GitHub 預覽頁，改讀同一教學的原始文字：
https://raw.githubusercontent.com/chunwenchiang-hue/family-trip-guide/main/docs/antigravity.md
依你的實際檔案工具操作；無法讀取或下載時直說，不用憑名稱推定版本。
把固定版本的完整技能放到目前工作區的 .agents/skills/family-trip-guide/。
保留原有模型、帳號、權限、其他技能和設定；同名資料夾已存在時，先比較與備份自訂修改，不直接覆寫。
確認 SKILL.md、八份 references 與授權檔（LICENSE 或 LICENSE.txt）完整，並用 manifest 的 core_files 雜湊核對 v1.3.0。
只安裝這一個技能，不安裝其他應用、擴充套件或付費服務。
完成後回報實際位置、版本核對結果，以及是否已被技能清單發現；
無法安裝或無法核對時直說，不把閱讀這個連結當成永久安裝。
```

安裝後**在同一個旅行專案開新對話**，先輸入 `/family-trip-guide`。介面有技能選單時選取它，再附旅行需求；如果該介面沒有斜線選單，直接要求「使用 family-trip-guide，先讀取工作區內的 SKILL.md 與本次相關參考文件」。單純看到技能名稱或「我會使用」不代表實際讀取。

## 想自己安裝

### 方法一：已經有 Git

在**你選好的旅行資料夾**開終端機。只限第一次安裝，同名資料夾不存在時執行：

```sh
git clone --branch v1.3.0 --depth 1 https://github.com/chunwenchiang-hue/family-trip-guide.git .agents/skills/family-trip-guide
```

這會下載固定 v1.3.0 來源，Git 可能顯示 detached HEAD，屬於固定版本的正常狀態。不要從其他地方取得同名技能，也不要用強制覆寫選項。若資料夾已存在，改請 AI 先比較與保留修改。

### 方法二：沒有 Git

1. [下載 v1.3.0 完整資料夾 ZIP](https://github.com/chunwenchiang-hue/family-trip-guide/releases/download/v1.3.0/family-trip-guide-claude.zip)。檔名帶 `claude`，但內容是通用的完整技能資料夾，可供 Antigravity 讀取。
2. 到瀏覽器下載清單或電腦的「下載項目／Downloads」找 ZIP，再解壓縮。有些瀏覽器已自動解壓縮，若看見 `family-trip-guide` 資料夾就檢查裡面的檔案，不要再解一次。不要用網頁「另存新檔」把 GitHub 頁面當成 ZIP。
3. 在旅行資料夾裡準備 `.agents/skills/`。`.agents` 以點開頭，可能被隱藏；Mac Finder 可按 `⌘⇧.` 顯示隱藏檔，Windows 可在檔案總管的「檢視 → 顯示 → 隱藏的項目」開啟。也可直接請 Antigravity 建立指定資料夾，或從檔案總管的路徑列前往。
4. 把解壓縮後的 `family-trip-guide` 資料夾放進 `.agents/skills/`。若已有同名資料夾，先保留並比較修改，不直接覆蓋。
5. 請 Antigravity 讀回確認。避免多包一層 `family-trip-guide/family-trip-guide`，也不要只放 ZIP 而沒有解壓縮。

最後結構應是：

```text
你的旅行資料夾/
└── .agents/
    └── skills/
        └── family-trip-guide/
            ├── SKILL.md
            ├── references/
            │   ├── acceptance.md
            │   ├── bookings-money.md
            │   ├── companion-flow.md
            │   ├── guide-voice.md
            │   ├── lessons.md
            │   ├── mobile.md
            │   ├── planning.md
            │   └── trip-record.md
            └── LICENSE.txt
```

Git 方式另有 `VERSION`、`LICENSE`、說明與建置檔；ZIP 授權檔名為 `LICENSE.txt`。兩種方式的九份核心文件相同，請按 [固定 v1.3.0 manifest](https://raw.githubusercontent.com/chunwenchiang-hue/family-trip-guide/v1.3.0/install.json) 的 `core_files` 核對。ZIP SHA-256：`ce5bcd8146ce8683301c2830fd1d791301dd467c84b0ec964f38195af60941fd`。

### 想在所有工作區都用？

以上預設只裝到旅行工作區。若你自己選擇全域安裝，可將相同完整技能放到 `~/.gemini/config/skills/family-trip-guide/`，官方 App、CLI 和 IDE 都支援這個位置；`~` 代表目前使用者的家目錄。Windows 的家目錄一般是 `C:\Users\你的帳號`。

選工作區或全域其中一種即可，避免同名副本版本不同；已有副本先比較。不要為了這份指南匯入所有 Codex／Claude 設定或修改安全權限。載入後在新對話確認；CLI 已開著時可用官方 `/skills reload` 重新載入。

## 第一次開始規劃

在**同一個旅行專案的新對話**，先輸入 `/family-trip-guide` 並選取技能（若有選單），再貼需求。以下第一行也可連同全文一起貼上；若這個介面不接受斜線語法，把第一行改成「請使用 family-trip-guide」，其餘不變。

```text
/family-trip-guide
請先讀取主指引與本次相關參考文件，讀不到時直說。
我要規劃家人旅行：
出發地：台北
目的地：未定
日期：2027年秋天，約5天
同行者：4位成人、1位長輩
每人預算：新台幣5萬元，含交通住宿
願望：美食、風景、慢慢走
需要留意：少階梯、少換飯店、少拖行李；飲食限制待逐人確認
已訂：無

先整理已知與缺口，每輪最多問3題。不要自行補成已確認。
先不要訂票、付款、發布網站或製作整批音檔。
```

**第一則回覆看什麼？** 應整理已知條件與待確認事項，每輪最多三題；目的地未定就保持未定或提出少量候選，不虛構預約與已完成成果。若它說讀不到主指引或參考文件，先照下方排查，不急著提供真實訂單。

上面是虛構範例，請改成你的資料。新版預設同行掃 QR 直接看線上行程，主揪另外下載備份；故事放在對應日期的景點卡，首頁呈現旅行任務。實際網站、音訊與預約仍需工具及具體授權。

## 安裝後，實際測一次

在新對話選取技能後，貼以下**不含標準答案**的測試題：

```text
請使用 family-trip-guide，先實際讀取主指引與相關參考文件。
這是虛構規劃演練：六名成人於2027年4月10–12日遊一座虛構城市，手機旅途上網正常。
每日路線已定，包含甲寺、乙庭園、丙博物館。
主揪有兩份原預約PDF與既有同行QR，尚未提供；景點與問路音訊未製作。
請寫從朋友掃QR到當天使用的最小流程、首頁示例、同行與主揪分工、
聲音入口與備援、製作和更新順序。列實際讀到的文件與已完成／未完成。
只交付規劃草稿，不實際訂位、付款、發布或合成音訊，約900字內。
```

拿到回答後再檢查：

- 是否確實讀取 `SKILL.md` 及相關參考，讀取失敗有沒有直說？
- 同行是否直接線上使用，主揪是否另持離線備份，而非要求全員下載整包 HTML？
- 導覽是否放在對應日期／景點卡，首頁沒有版本、下載或試聽公告？
- 是否先做自然女聲短樣、經主揪確認再整批；問路沿用已確認的外語聲音，點了才播？
- 原 QR、PDF 是否保留，尚未提供的資料及未製作的網站／音訊是否保持未完成？

回答符合流程才記「規劃測試通過」；寫入檔案、技能清單發現、實際讀取與規劃通過分開。這不等於旅客手機、實際音訊或離線備份已驗收。其餘情境見 [三個小測試](platforms.md#匯入後的三個小測試)。

## 改天接著規劃

結束前請它把已確認條件、檔案位置、待辦與下一步存成旅行資料夾內的「旅行接續摘要.md」（若無寫檔工具，就把摘要貼給你保存）。下次開同一個專案，請它先讀技能和這份摘要。不要把自己的行程存到技能資料夾或這個公開 GitHub；技能更新時才不會混進私人資料。

## 如果讀不到

| 卡在哪裡 | 下一個動作 |
| --- | --- |
| 讀不到 GitHub 網頁 | 用安裝文字內的 raw 原始文字連結；仍不能讀就手動下載 ZIP，交給同一工作區的 Antigravity 處理 |
| 找不到 Git 或 clone 失敗 | 改用「沒有 Git」的 ZIP 方法，不需要為這份指南先安裝 Git |
| 同名資料夾已存在 | 停止覆寫，請 AI 比較版本並備份自訂修改；不要先刪除重裝 |
| 開了新對話卻沒有技能 | 確認仍在原旅行專案，檢查 `SKILL.md` 是否在 `.agents/skills/family-trip-guide/`；留意是否多一層同名資料夾 |
| 沒有 `/family-trip-guide` 選單 | 改用自然語言指名並讀取主指引；IDE 可在 agent 側欄的 Customizations 檢查技能，CLI 可用 `/skills reload`。能讀檔與自動發現仍分開記錄 |
| 顯示額度或登入問題 | 依該帳號介面處理，保留未完成狀態；不用買額度或改付費 API 才能完成本頁的檔案準備 |

先確認 Antigravity 正在開啟你安裝的那個旅行資料夾、目錄沒有多包一層，然後開新對話。仍讀不到時，請它列出實際技能位置與可讀文件；不要反覆重送同一題，也不要把網頁 Gemini 的 `@` 安裝方法套到 Antigravity。參考 [官方技能目錄與啟用說明](https://antigravity.google/docs/skills)。

日後更新請先備份自訂修改，核對新版本與實際變更，再更新相同位置；本頁固定版本不會自動跟 GitHub 升級。私人旅行資料放自己的受信任空間，不要上傳到這個公開倉庫。
