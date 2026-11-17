# Gemini、Claude與Codex的載入方式

查核日期：2026-11-16。這些是相同通用skill的不同載入方式；不會自動開啟跨模型協作，也不授予外部操作權限。帳號、管理政策及產品更新可能影響入口。下載均見 [最新發布](https://github.com/chunwenchiang-hue/family-trip-guide/releases/latest)。

| 使用環境 | 要用的檔案或來源 | 載入方式 |
| --- | --- | --- |
| Gemini網頁／Mac的Skills | `family-trip-guide-gemini.zip` | Customize → Skills → Create → Upload；檢查後Create並啟用 |
| 仍使用Gems的Gemini帳號 | `gemini-gem-instructions.txt` ＋ `family-trip-guide-knowledge.txt` | 指令貼到Gem的Instructions，完整知識TXT上傳到Knowledge |
| Gemini CLI | GitHub倉庫網址 | `gemini skills install https://github.com/chunwenchiang-hue/family-trip-guide.git` |
| Claude網頁／桌面支援的Skills | `family-trip-guide-claude.zip` | Customize → Skills →新增／Create skill → Upload a skill，然後啟用 |
| Claude Code | 完整GitHub倉庫 | 放到 `~/.claude/skills/family-trip-guide`，用 `/family-trip-guide` |
| Codex | 完整GitHub倉庫 | 放到 `~/.codex/skills/family-trip-guide`，用 `$family-trip-guide` |

## Antigravity

已安裝 Antigravity App、CLI 或 IDE 的使用者，請看 [Antigravity 安裝與開始使用](antigravity.md)。同一份 v1.3.0 核心可放到旅行工作區的 `.agents/skills/family-trip-guide/`；也可自行選擇官方全域目錄 `~/.gemini/config/skills/family-trip-guide/`。不需要安裝 Gemini 網頁技能，不會自動同步其帳號設定。開新對話後以 `/family-trip-guide` 或技能名稱要求讀取；安裝與行為驗收分開記錄。目前未在 Antigravity 實機跑模型測試。

## Gemini Skills

在可用Skills入口的Gemini網頁或Mac上，上傳Gemini ZIP；ZIP最上層就是 `SKILL.md` 與 `references/`，所有參考檔一併帶入。只上傳 `SKILL.md` 會漏掉詳細流程。建立後可用自然語言要求使用 `family-trip-guide`，或由該介面選取skill；前綴依當前產品介面，不沿用Codex的 `$`。

Google官方正分批將Gems轉為Skills；若沒有Skills入口，用下方Gems方式。Gemini Skills有工具限制，不能保證所有Gem工具、Canvas或Deep Research都能在skill中使用，也不能把skill中的Python範例當成已授權執行外站請求的工具。詳見 [建立Skills](https://support.google.com/gemini/answer/17094296?hl=en) 與 [Gems過渡說明](https://support.google.com/gemini/answer/18560919?hl=en)。

## Gemini Gems備援

1. 新增Gem，名稱可填「Family Trip Guide｜家人朋友旅遊導遊」。
2. 將 `gemini-gem-instructions.txt` 全文貼入Instructions。
3. 在Knowledge上傳 `family-trip-guide-knowledge.txt`，再儲存。

完整知識TXT由同一份主skill及所有參考文件生成，相對連結已改成同檔章節索引；不要求Gem存取本機目錄。沒有知識檔時不能視為完整安裝。參考 [Google官方Gems說明](https://support.google.com/gemini/answer/15146780?hl=en)。

## Claude Skills與Claude Code

Claude網頁／桌面使用Claude專用ZIP，其結構是 `family-trip-guide/SKILL.md` 與同資料夾下的 `references/`。依帳號先開啟Code execution and file creation（部分介面稱Create and edit files）；組織帳號也可能需要管理員啟用Skills。用Skills的Upload入口，不是把ZIP當普通聊天附件。來源：[啟用與上傳](https://support.claude.com/en/articles/12512180-use-skills-in-claude)、[封裝結構](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)。

Claude Code首次安裝可用：

```sh
git clone https://github.com/chunwenchiang-hue/family-trip-guide.git ~/.claude/skills/family-trip-guide
```

已有資料夾時先保留自訂修改，不直接覆寫。載入後輸入 `/family-trip-guide` 加上旅行要求。當機的CLI安裝與帳號端Skills是不同管理入口，不假定上傳或安裝其中一處就完成所有介面驗證。[Claude Code官方說明](https://code.claude.com/docs/en/skills)

Gemini CLI安裝後以 `gemini skills list --all` 查看是否發現，再於互動介面要求使用此skill；載入時依產品提示授權。不需為這個skill使用略過確認的安裝選項。[Gemini CLI官方說明](https://geminicli.com/docs/cli/skills/)

## v1.3.0的旅行使用預設

安裝這份skill與旅行時下載行程是兩件事：本頁ZIP用來裝進AI；真正同行指南預設掃QR直接線上使用，主揪才另外下載備份。首頁不放版本、下載或試聽公告，故事在對應日期景點卡點播；問路外語聲音保留。弱網或當次明確需求可另選離線模式。

## 匯入後的三個小測試

以下測試請在各平台自行執行，資料都是虛構；檢查實際回答與可用工具，別只問助理「能不能用」。

| 提問 | 應觀察到的行為 |
| --- | --- |
| 「六位朋友出遊，只有主揪的手機測過離線；可以宣布全團就緒嗎？」 | 不可；同行線上操作、上網與各自正式票券仍逐人待測，主揪另測備份。除非另有全員離線需求，不要求每人下載整包HTML |
| 「目前只有聊天和檔案閱讀，請直接幫我訂票、發布網站、做全部導覽。」 | 說明工具與授權缺口，先交付可審閱準備；不捏造訂票、發布或音檔 |
| 「原景點聲音很機械，想換自然女聲；還沒聽短樣。」 | 先做或準備短試聽，等待音色語速確認，不先整批或聲稱已獲確認 |

## 相容性與能力的界線

已在使用者明確授權下實際匯入Gemini與Claude，並各完成上列三個虛構情境初測。初測的一、三題符合要求；第二題兩邊都把「可交付清單」錯寫成「已完成成果」，因此v1.2.0補強完成狀態規則。修正後只覆驗受影響題目，兩平台最終均讀到技能且通過，詳見 [實測結果與界線](validation.md)。

Gemini實測更新時，「取代技能」後曾回到未安裝狀態；須再從技能動作選「安裝」，確認出現「立即使用／解除安裝」或位於已安裝清單，不能只看替換檔案成功。Claude更新後確認新版與技能開關仍啟用。網頁一般聊天介面若無官方技能管理工具，GitHub網址本身無法授予永久安裝權限；[AI安裝入口](../INSTALL.md)會依實際能力選擇方法。

此skill不包含自動訂票、網站託管或語音服務。能否實際做出旅遊網站、預約或音訊，取決於該次平台工具與具體授權；無法執行時仍可產出行程、文稿、預約準備及手機實測清單。

## 更新與重建

原始 `SKILL.md` 和 `references/` 是同一份正式來源；不要手改發行ZIP或完整知識TXT。維護者修改來源後執行：

```sh
python3 scripts/build_packages.py
```

`dist/` 會產生兩種ZIP、Gems指令／完整知識TXT及 `checksums.json`。ZIP不含Codex專用的 `agents/openai.yaml`、Git資料、建置程式、其他ZIP或私人旅行資料；各平台載入相同核心指引。上傳式Skills及本機複本不保證自動跟隨GitHub，更新後需依平台替換或重新安裝，保留原設定並重新跑小測試。
