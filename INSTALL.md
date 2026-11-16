# Family Trip Guide：貼連結給AI安裝

把以下一句貼給要使用的AI：

```text
請安裝並啟用這個旅遊skill，依你目前環境選擇可用方法；完成後回報實際版本與結果：
https://github.com/chunwenchiang-hue/family-trip-guide/blob/main/INSTALL.md
```

這個入口由GitHub保存。它協助有安裝能力的AI選方法，不是跨平台遠端控制服務；不能讓沒有檔案或技能管理權限的聊天模型自行取得權限。只貼網址而沒有請求時，也不假定使用者已授權修改設定。

## 給接收連結的AI

僅在使用者明確要求安裝或啟用時執行；遵守你的工具與平台規則。這份文件是安裝資料，不提供付款、額外平台存取、外送私人檔案或略過安全確認的授權。

1. 先判斷你現在是有檔案工具的代理、Gemini CLI、Claude Code、Codex，還是Gemini／Claude一般聊天介面。不要同時替使用者裝到所有平台。
2. 讀取同倉庫的 [install.json](install.json)，取得版本、發行檔、SHA-256及完整知識入口。無法讀取時直說，不能假稱已取得完整skill。
3. 檢查來源內容與既有同名skill；有自訂修改時先保留，不覆寫。只使用公開套件，不要求使用者提供私有GitHub憑證。
4. 用下表中實際可用的方法安裝；不能持久安裝時，交付該平台的直接下載及唯一必要的人手步驟。
5. 重新讀回 `SKILL.md` 與全部 `references/` 是否存在。檔案未寫版本號時，可與manifest的 `core_files` 雜湊比對；平台若正規化文字導致雜湊不同，就明列版本未核實，不靠同名推定。安裝成功不等於已跑行為測試；測試題見 [跨平台教學](docs/platforms.md#匯入後的三個小測試)。未實測就保持未測。

## 依環境選擇

| 當前環境 | 實際做法 |
| --- | --- |
| Gemini CLI | 使用已安裝CLI的 `gemini skills install https://github.com/chunwenchiang-hue/family-trip-guide.git`，再用 `gemini skills list --all` 查到同名skill；依正常安全提示操作 |
| Claude Code | 取得已查核的正式來源，將完整skill放到 `~/.claude/skills/family-trip-guide`；確認參考文件，再用 `/family-trip-guide` |
| Codex | 取得已查核的正式來源，將完整skill放到 `~/.codex/skills/family-trip-guide`；確認參考文件，再用 `$family-trip-guide` |
| 其他有檔案工具的Agent Skills代理 | 依該工具自己的skill目錄規格安裝同一份 `SKILL.md` 與 `references/`，不猜測系統目錄 |
| Gemini／Claude聊天介面有官方skill建立／上傳工具 | 使用實際提供的工具匯入相應套件並啟用；確認已儲存且參考文件完整，不以產出ZIP或在對話讀過內容代稱已永久安裝 |
| 一般聊天介面沒有技能管理或檔案安裝工具 | 說明無法代寫帳號Skills；直接提供下方對應ZIP，請使用者到Skills上傳一次。若使用者要先在目前對話使用，讀完整知識檔並明示只是本次對話載入 |

## 直接下載

- [Gemini Skills ZIP](https://github.com/chunwenchiang-hue/family-trip-guide/releases/download/v1.2.0/family-trip-guide-gemini.zip)
- [Claude Skills ZIP](https://github.com/chunwenchiang-hue/family-trip-guide/releases/download/v1.2.0/family-trip-guide-claude.zip)
- [完整知識文字檔](https://raw.githubusercontent.com/chunwenchiang-hue/family-trip-guide/v1.2.0/platforms/family-trip-guide-knowledge.txt)：包含主指引與八份參考文件，可在同檔依來源名稱尋找章節。
- [Gems指令](https://github.com/chunwenchiang-hue/family-trip-guide/releases/download/v1.2.0/gemini-gem-instructions.txt) 與 [完整知識下載](https://github.com/chunwenchiang-hue/family-trip-guide/releases/download/v1.2.0/family-trip-guide-knowledge.txt)

Gemini網頁可用Skills時，在Customize → Skills →建立 →上傳相應ZIP；Claude在Customize → Skills →新增 →上傳Skill。這些步驟已實際走過，沒有在上傳頁看到「從GitHub網址直接安裝」欄位。若AI沒有操作此介面的工具，仍需使用者完成上傳，不能謊稱只讀連結就已安裝。

Gemini的「取代技能」後要再確認已安裝，必要時從技能動作選「安裝」。對話測試可輸入 `@` 並從技能選單選取 `family-trip-guide`，再填需求；不要只以文字裡出現技能名推定已讀取。Claude確認技能開關開啟與目前版本。安裝／啟用、讀到指引、回答符合要求，各自保存證據。

## 安裝回執

回報：平台／方法／版本、實際儲存位置或可見skill、主指引與八份參考是否齊全、是否已啟用、三題哪些實測／未測。分清「已下載」「本次對話載入」「已持久安裝」「已驗收」。不因skill裡有聲音或預約流程，就宣稱平台已具備合成或訂票工具。
