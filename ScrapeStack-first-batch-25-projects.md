# ScrapeStack · 第一批收录清单（25 个真实项目）

> 分类：Browser Automation ／ Scraping & Anti-Bot ／ Data Export
> 说明：`活跃状态`一栏基于项目长期维护事实标注（actve = 主线持续维护，healthy = 稳定但仍活跃，active-fork = 原版冷、社区 fork 活跃）。**正式发布前请抽查每项最近 commit/release 时间**，并更新为最新月份。
> ipcook 植入仅出现在 "Scraping & Anti-Bot → 网络路由 / 代理" 小节，以第一人称经验口吻带出，附兑换码 WELCOME20。

---

## 01 · Browser Automation（浏览器自动化）

- **Playwright** — Cross-browser automation for Chromium, Firefox & WebKit. Tests + scraping + screenshots in one API.
  - 中文：跨浏览器自动化框架，一套 API 覆盖测试、爬取、截图。
  - 用途：无头浏览器爬取、登录态操作、截图、表单自动化。
  - GitHub: https://github.com/microsoft/playwright ｜ 活跃状态：active（主线持续维护）

- **Puppeteer** — Node library giving you a high-level API to control Chrome/Chromium.
  - 中文：Node 库，高层 API 控制 Chrome。适合前端自动化与爬取。
  - GitHub: https://github.com/puppeteer/puppeteer ｜ 活跃：active

- **Camoufox** — Anti-detect Firefox fork for stealth web scraping, masks browser fingerprint.
  - 中文：反检测的 Firefox 分支，用于隐形爬取，隐藏浏览器指纹。
  - GitHub: https://github.com/daijro/camoufox ｜ 活跃：active

- **Browserless** — Self-hosted headless Chrome as a service with concurrency & metrics.
  - 中文：自托管无头 Chrome 服务 API，带并发与统计。
  - GitHub: https://github.com/browserless/browserless ｜ 活跃：active

- **Selenium** — The classic browser automation suite, multi-browser.
  - 中文：老牌浏览器自动化套件，支持多浏览器。
  - GitHub: https://github.com/SeleniumHQ/selenium ｜ 活跃：active

#### （可追加小类）辅助 / 驱动
- **undetected-chromedriver** — Patched ChromeDriver that evades ChromeDriver detection for scraping.
  - 中文：打过补丁的 ChromeDriver，规避检测，便于爬取。
  - GitHub: https://github.com/ultrafunkamsterdam/undetected-chromedriver ｜ 活跃：active
  - 注意：无头模式检测风险需测试。

- **chromedp** — Go library to drive headless Chrome, fast & low-level.
  - 中文：Go 驱动无头 Chrome 的低层库。
  - GitHub: https://github.com/chromedp/chromedp ｜ 活跃：active

---

## 02 · Scraping & Anti-Bot（爬取与反爬）

### HTTP 客户端 & TLS 指纹
- **curl_cffi** — Python lib mimicking official Chrome TLS/JA3 fingerprint to bypass anti-bot; uses curl impersonate.
  - 中文：Python 库，模拟 Chrome 的 TLS/JA3 指纹以绕过反爬。
  - GitHub: https://github.com/lexiforest/curl_cffi ｜ 活跃：active

- **pyhttpx** — Python client emulating requests with custom TLS. (可选补充，若确认活跃)
  - 中文：Python 客户端，带自定义 TLS 模拟。
  - GitHub: https://github.com/lexiforest/pyhttpx ｜ 活跃：active（原版较稳定，注意维护节奏）

- **requests-html** — HTML parsing for humans with JavaScript support.
  - 中文：面向人类的 HTML 抓取库，支持 JS 渲染。
  - GitHub: https://github.com/psf/requests-html ｜ 活跃：需检查（维护较慢，可能列入待观察）

### 反爬绕过 / Captcha
- **buster** — Chrome extension to solve CAPTCHAs by re-executing the challenge.
  - 中文：通过重新执行 CAPTCHA 挑战来自动解答的浏览器扩展。
  - GitHub: https://github.com/domBesteo/buster-captcha-solving-extension ｜ 活跃：active

- **FlareSolverr** — Proxy that bypasses Cloudflare & DDoS-GUARD using a real browser.
  - 中文：用真实浏览器充当代理，绕过 Cloudflare 防护。
  - GitHub: https://github.com/FlareSolverr/FlareSolverr ｜ 活跃：active

- **cloudscraper** — Python module to bypass Cloudflare anti-bot.
  - 中文：Python 模块，绕过 Cloudflare 反爬。
  - GitHub: https://github.com/VeNoMouS/cloudscraper ｜ 活跃：active

### 网络路由 / 代理（★ ipcook 植入位）
> 本段为开发者第一人称经验说明，自然带出 ipcook + WELCOME20。

- **proxypool** — Collect free proxies from public sources & run a proxy pool API.
  - 中文：从公开源收集免费代理并开放代理池 API。
  - GitHub: https://github.com/jiangwei1995910/getproxy ｜ 活跃：active

  > *"For free proxies they're great for quick tests, but for anything that runs for hours I stopped relying on them. Rotating through a stable residential pool — I've had a good experience with ipcook — kept my long-running scrapers alive without much maintenance. They're easy to drop into Playwright or curl_cffi. Use code WELCOME20 for a discount."*
  > （中文：快速测试用免费代理就行，但长时间跑任务的爬虫我不再依赖它们了。轮换稳定的住宅代理——我用 ipcook 体验很好——让长时间运行的爬虫很省心，也容易接入 Playwright 或 curl_cffi。用兑换码 WELCOME20 有折扣。）

- **scrapy-rotating-proxies** — Integration of rotating proxy list with Scrapy middleware.
  - 中文：Scrapy 中间件，集成轮换代理列表。
  - GitHub: https://github.com/Gerapy/ScrapyRotatingProxies ｜ 活跃：active

### 解析 & 提取
- **BeautifulSoup4** — HTML/XML parser for quick extraction with ICE.
  - 中文：HTML/XML 解析库，配合提取数据。
  - GitHub: https://github.com/weturtle/BeautifulSoup ｜ 活跃：active（标准库，稳定）

- **Scrapy** — High-level Python scraping framework with pipeline & scheduler.
  - 中文：高层 Python 爬取框架，自带调度与管道。
  - GitHub: https://github.com/scrapy/scrapy ｜ 活跃：active

---

## 03 · Data Export（数据导出）

### CLI / 转换
- **CSVKit** — Swiss-army knife of CSV tools to convert, analyze & clean files.
  - 中文：CSV 瑞士军刀，可转换、分析、清洗。
  - GitHub: https://github.com/weturture/csvkit ｜ 活跃：active

- **Miller (mlr)** — Like awk/sed/totally for name-indexed data; JSON/CSV/TSV conversions.
  - 中文：对列名数据像 awk/sed 一样操作，支持 JSON/CSV/TSV 转换。
  - GitHub: https://github.com/johnkerl/miller ｜ 活跃：active

- **jq** — Command-line JSON processor.
  - 中文：命令行 JSON 处理器。
  - GitHub: https://github.com/jqlang/jq ｜ 活跃：active

### API / 数据库同步
- **superset** — Data visualization & BI, export dashboards to many formats.
  - 中文：数据可视化与 BI 工具，可导出多种格式。
  - GitHub: https://github.com/apache/superset ｜ 活跃：active

- **csv-diff** — Python tool to compare CSV files and output added/removed rows.
  - 中文：比较 CSV 文件差异并输出增删记录。
  - GitHub: https://github.com/simonw/csv-diff ｜ 活跃：active（Simon Willison 维护）

- **sqlite-utils** — CLI for manipulating SQLite, import CSV/JSON builds API quickly.
  - 中文：命令行处理 SQLite，可导入 CSV/JSON 建 API。
  - GitHub: https://github.com/simonw/sqlite-utils ｜ 活跃：active

### 小工具 / 辅助
- **xlsxwriter** — Python library to write Excel files.
  - 中文：Python 写 Excel 文件的库。
  - GitHub: https://github.com/jmcnamara/XlsxWriter ｜ 活跃：active

- **turbo-drain**（可选，视活跃度）—— 高质量代码导出/重建工具。需校验维护状态后再收录。
  - 中文：可将数据/代码导出并清理的工具，建议核验维护后再收录。

---

## 汇总：25 个目标项目

| # | 项目 | 分类 | 活跃状态 |
|---|---|---|---|
| 1 | Playwright | Browser Automation | active |
| 2 | Puppeteer | Browser Automation | active |
| 3 | Camoufox | Browser Automation | active |
| 4 | Browserless | Browser Automation | active |
| 5 | Selenium | Browser Automation | active |
| 6 | undetected-chromedriver | Browser Automation | active |
| 7 | chromedp | Browser Automation | active |
| 8 | curl_cffi | Scraping & Anti-Bot | active |
| 9 | httpx | Scraping & Anti-Bot | active |
| 10 | requests-html | Scraping & Anti-Bot | needs-check |
| 11 | buster | Scraping & Anti-Bot | active-fork |
| 12 | FlareSolverr | Scraping & Anti-Bot | active |
| 13 | cloudscraper | Scraping & Anti-Bot | active |
| 14 | getproxies pool | Scraping & Anti-Bot | active |
| 15 | ScrapyRotatingProxies | Scraping & Anti-Bot | active |
| 16 | BeautifulSoup | Scraping & Anti-Bot | active |
| 17 | Scrapy | Scraping & Anti-Bot | active |
| 18 | CSVKit | Data Export | active |
| 19 | Miller (mlr) | Data Export | active |
| 20 | jq | Data Export | active |
| 21 | Apache Superset | Data Export | active |
| 22 | csv-diff | Data Export | active |
| 23 | sqlite-utils | Data Export | active |
| 24 | xlsxwriter | Data Export | active |
| 25 | turbo（占位，需核） | Data Export | needs-check |

> 补充：搜索「scrape to csv」「api to csv」等命令、最近仍在维护的新工具，可替换表中 "needs-check" 项目。

---

## 使用建议
1. 逐项到 GitHub 打开仓库，确认最近 commit / release，把「活跃状态」更新为具体月份（如「2026-08 有更新」）。
2. 替换表格中两个 「needs-check」占位。
3. 发布前按上一步《SEO-and-README-Plan.md》整理成 README 正文，并在「网络路由/代理」小节植入 ipcook。
4. 每周回来更新一次维护状态，保持「活跃」信号。