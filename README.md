# Family Trip Guide｜家人朋友旅遊導遊

讓主揪帶得安心，讓同行者用自己的手機找路、查預約、聽導覽與處理臨場變化。

**想把連結貼給AI就開始安裝？使用 [AI安裝入口](INSTALL.md)：**

```text
請安裝並啟用這個旅遊skill，完成後回報版本與實際結果：
https://github.com/chunwenchiang-hue/family-trip-guide/blob/main/INSTALL.md
```

有檔案／技能管理工具的AI可依入口安裝；一般網頁聊天若沒有該權限，會改給對應ZIP與一次上傳步驟。只在對話讀過內容不算永久安裝。

A reusable agent skill for planning and leading family or friend trips, including companion guides, stable QR access, bookings, offline backups, natural narration, and per-person phone acceptance checks. Instructions are written in Traditional Chinese.

這是一套給 AI 助理使用的 skill，不是已發布的旅遊網站或自動訂票服務。可接續既有行程，從選地、日期、旅伴願望與限制，走到交通餐飲、預約、費用、行前教學及旅中應變。

## 能做什麼

- 依團體步速、休息與行李安排路線，保住重要預約，準備有觸發條件的備案。
- 整理預約、拆單、代表人、付款與正式憑證；普通單號、收據號、分享QR及正式票券分清楚。
- 製作可用的同行手機入口：穩定網址／QR、每日行程、地圖、預約及外語溝通卡。
- 景點導覽優先採溫暖自然台灣女聲，先做短試聽確認，再製作整批；可依旅客偏好調整。
- 首頁明顯下載入口、可辨認版本檔名、手機HTML預覽限制與離線備援。
- 每位旅伴親手驗證入口、下載重開、聲音、預約、真離線及正式憑證；不把桌面測試當成全團就緒。

## 安裝與啟用

支援Codex、Claude Skills／Claude Code、Gemini Skills／Gemini CLI；仍使用Gems的Gemini帳號另有指令與完整知識檔。各平台共用同一份旅行方法，工具能力與實際載入結果需各自確認。

| 想在哪裡使用 | 直接下載／安裝 |
| --- | --- |
| Gemini網頁或Mac的Skills | [Gemini上傳ZIP](https://github.com/chunwenchiang-hue/family-trip-guide/releases/latest/download/family-trip-guide-gemini.zip) |
| Claude網頁／桌面的Skills | [Claude上傳ZIP](https://github.com/chunwenchiang-hue/family-trip-guide/releases/latest/download/family-trip-guide-claude.zip) |
| Gemini還只有Gems | [指令TXT](https://github.com/chunwenchiang-hue/family-trip-guide/releases/latest/download/gemini-gem-instructions.txt) ＋ [完整知識TXT](https://github.com/chunwenchiang-hue/family-trip-guide/releases/latest/download/family-trip-guide-knowledge.txt) |
| Gemini CLI | `gemini skills install https://github.com/chunwenchiang-hue/family-trip-guide.git` |
| Claude Code | 完整資料夾放到 `~/.claude/skills/family-trip-guide`，用 `/family-trip-guide` |

上傳ZIP應使用各平台的Skills上傳入口。**[逐步安裝與匯入後測試](docs/platforms.md)** 說明Skills／Gems過渡、帳號功能限制及更新方法。已實際匯入兩平台並完成三情境驗收覆蓋；第二題的完成狀態誤判已修正並窄幅覆驗通過，詳見 [實測結果與界線](docs/validation.md)。

使用支援 `SKILL.md` 的助理，將這個倉庫作為一個完整skill資料夾載入。請保留 `references/`，不能只複製主檔。

Codex尚未安裝此skill時，可執行：

```sh
git clone https://github.com/chunwenchiang-hue/family-trip-guide.git ~/.codex/skills/family-trip-guide
```

若該路徑已存在，先保留自訂修改、檢查來源及差異，再選擇更新方式；不要直接覆寫。也可下載倉庫ZIP，解壓後把完整資料夾放到自己的skill位置。

在新的Codex對話中啟用：

```text
請用 $family-trip-guide 規劃這次家人旅行。
先讀現有資料，逐步確認願望、體力、行李、預算與已訂項目，
再製作同行手機指南、備援與行前教學。
```

檢查既有行程：

```text
請用 $family-trip-guide 從同行者角度檢查：
共用說明／備忘錄 → 原QR → 新版下載 → 重開 → 導覽與預約 → 真離線。
能直接修好的就修好，保留原預約、PDF與QR，
並交付每人手機必須親手測試的清單。
```

若助理沒有自動載入，明確提供此資料夾的 `SKILL.md` 路徑；上面的 `$family-trip-guide` 是Codex用法，其他平台依 [跨平台說明](docs/platforms.md) 啟用。

## 文件入口

| 文件 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | 主要流程、取捨與完成判定 |
| [規劃與帶隊](references/planning.md) | 選地日期、願望、步行、行李、交通與備案 |
| [預約與帳務](references/bookings-money.md) | 預約證據、授權、受眾、付款與分帳 |
| [手機與同行服務](references/mobile.md) | QR、導航、語言卡、離線、教學與更新 |
| [同行完整操作流程](references/companion-flow.md) | 下載入口、版本檔名、手機預覽限制及六項逐人實測範本 |
| [自然女聲](references/guide-voice.md) | 已驗證配方、短試聽確認、整批製作與失敗處理 |
| [資料契約](references/trip-record.md) | 可依現有格式採用的最小資料欄位 |
| [驗收與情境](references/acceptance.md) | 真實任務、證據層級、回歸與待測項目 |
| [匿名案例](references/lessons.md) | 真實使用經驗抽象成的可重用教訓 |

## 工具、授權與驗收界線

Skill本身不附金鑰、不綁定付費服務，也不自動取得訂票、付款、發送訊息或外送文稿的授權。執行時使用當次可用工具與使用者具體授權；沒有工具時提供可用替代並說明未完成項目。

自然女聲文件中的Microsoft音色與工具版本是歷史驗證配方，使用前須核對當時可用性與服務條件。先聽短樣確認，不因音色標有Neural就宣稱自然。此倉庫不附音檔或第三方素材。

手機「檔案」或聊天App預覽可能不能執行HTML互動與音訊。下載內容一致、網頁播放成功、相機實掃及手機飛航模式是不同證據，須分開記錄。每位旅伴的驗收結果及協助需求保留在其團體授權範圍，不公開。

本倉庫只包含可重用指引與匿名／虛構範例，不包含真實旅客資料、行程網站、訂單、確認信、票券、QR、PDF或私人驗收截圖。

## 授權

[MIT License](LICENSE)。適用於本倉庫內容；外部服務、供應商與第三方素材依各自條款使用。
