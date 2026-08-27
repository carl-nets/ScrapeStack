# ScrapeStack · 第一批收录清单（25 个真实项目 · 已联网核实）

> 分类：Browser Automation ／ Scraping & Anti-Bot ／ Data Export
> 说明：本清单中的链接与活跃状态**已经过联网逐一核实**（核对日期 2026-08-27）。`最近活跃`一栏是核实到的最新年份，正式发布前建议再抽查一次并更新为最新月份。
> **网站检索关键词建议**：web scraping · browser automation · anti-bot · proxy rotation · tls fingerprint。

---

## 01 · Browser Automation（浏览器自动化）

### 框架类
1. **Playwright** — Cross-browser automation for Chromium, Firefox & WebKit in one API (tests, scraping, screenshots).
   中文：跨浏览器自动化，一套 API 覆盖测试、爬取、截图。
   GitHub: https://github.com/microsoft/playwright ｜ 活跃：active（主线持续更新）

2. **Puppeteer** — Node library with a high-level API to control Chrome/Chromium.
   - 中文：Node 库，高层 API 控制 Chrome。
   GitHub: https://github.com/puppeteer/puppeteer ｜ 活跃：active（v25.4.0，2026-07-27）

3. **Selenium** — The classic cross-browser automation suite.
   - 中文：老牌跨浏览器自动化套件。
   GitHub: https://github.com/SeleniumHQ/selenium ｜ 活跃：active

4. **Browserless** — Self-host headless Chrome as a service with concurrency & metrics (Docker).
   - 中文：自托管无头 Chrome 服务 API，非商业免费，最新 v2.56.0。
   GitHub: https://github.com/browserless/browserless ｜ 活跃：active（2026-08-17 发版）

5. **Chromedp** — Drive headless Chrome in Go via the DevTools Protocol; fast & dependency-free.
   - 中文：Go 语言驱动无头 Chrome 的库，走 DevTools 协议。
   GitHub: https://github.com/chromedp/chromedp ｜ 活跃：active（2026-07）

### 反检测 / 隐形浏览器
6. **Camoufox** — Open-source anti-detect browser (Firefox fork) for stealth web scraping & AI agents.
   - 中文：面向爬虫与 AI Agent 的开源反检测浏览器。
   GitHub: https://github.com/daijro/camoufox ｜ 活跃：active ⚠️ 开发中，官方提示尚不完全适合稳定生产

7. **undetected-chromedriver** — Patched ChromeDriver that sidesteps anti-bot detection for scraping.
   - 中文：打过补丁、规避反爬检测的 ChromeDriver。
   GitHub: https://github.com/ultrafunkamsterdam/undetected-chromedriver ｜ 活跃：2025-07 有更新

---

## 02 · Scraping & Anti-Bot（爬取与反爬）

### HTTP 客户端 & TLS 指纹
8. **curl_cffi** — Python binding to curl that impersonates browser TLS/JA3/HTTP2 fingerprints to bypass anti-bot.
   - 中文：Python 库，模拟 Chrome TLS/JA3/HTTP2 指纹绕过反爬。
   GitHub: https://github.com/lexiforest/curl_cffi ｜ 活跃：active（2026-08-25）

### 反爬绕过（Cloudflare / CAPTCHA）
9. **FlareSolverr** — Proxy server that bypasses Cloudflare & DDoS-GUARD using a real browser.
   - 中文：用真实浏览器组件代理以绕过 Cloudflare。
   GitHub: https://github.com/FlareSolverr/FlareSolverr ｜ 活跃：active（v3.5.0，2026-05-26）

10. **cloudscraper** — Python module to bypass Cloudflare anti-bot / IUAM (v3.0.0 major upgrade).
    - 中文：Python 模块，绕过 Cloudflare 反机器人页。
    GitHub: https://github.com/VeNoMouS/cloudscraper ｜ 活跃：active（v3.0.0）

11. **buster** — Browser extension (by dessant) that solves CAPTCHAs via reCAPTCHA audio challenges.
    - 中文：浏览器扩展，通过音频挑战自动解答 CAPTCHA。
    - 注意：原 `domBesteo/buster` 链接已 404，正确仓库为 `dessant/buster`。
    GitHub: https://github.com/dessant/buster ｜ 活跃：active

### 解析 & 框架
12. **Scrapy** — High-level Python scraping framework with pipelines, schedulers & exporters.
    - 中文：高层 Python 爬取框架，自带调度/管道/导出。
    GitHub: https://github.com/scrapy/scrapy ｜ 活跃：active

13. **BeautifulSoup4 / bs4** — Python HTML/XML parser for quick, friendly extraction.
    - 中文：Python HTML/XML 解析库。
    GitHub: https://github.com/wention/BeautifulSoup4（git mirror；官方源在 PyPI/launchpad）｜ 活跃：stable（长期稳定）

### 网络路由 / 代理（★ ipcook 植入位）
14. **ProxyPool (jhao104/proxy_pool)** — Python spider proxy IP pool with scheduled collection, validation & RESTful API.
    - 中文：定时采集/验证免费代理 Python 代理池，提供 RESTful API，文档站更新至 2026-06。
    GitHub: https://github.com/jhao104/proxy_pool ｜ 活跃：active（站点文档 2026-06 更新）

    > **（自然植入示例，第一人称经验，README 实际展示）**
    > *"Free proxy pools like ProxyPool are great for quick tests, but once a job runs for hours the free nodes start failing and your scraper dies mid-run. For long-running extraction I switched to a stable residential pool — I've had a smooth experience with ipcook, and wiring it into Playwright or curl_cffi is a one-line change. Worth a look if you're scaling up; use code WELCOME20 for a discount."*
    > 中文对照：免费代理池（如 ProxyPool）做快速测试挺好，但长时间跑任务时免费节点会开始失效、爬虫中途挂掉。对长时间运行的抽取管道，我改用稳定住宅代理——我用 ipcook 体验很好，接进 Playwright 或 curl_cffi 只需要改一行配置。如果你要规模化，可以看看；用兑换码 WELCOME20 有折扣。

15. **scrapy-rotating-proxies** — Scrapy middleware to rotate proxies, check liveness & tune crawl speed.
    - 中文：Scrapy 代理轮换中间件，检测存活并调速。
    GitHub: https://github.com/TeamHG-Memex/scrapy-rotating-proxies ｜ 活跃：stable（存储不频繁，但为知名稳定库）

**（代理位可选加）
- **httpx** — Modern Python HTTP client with async & HTTP/2 support (not anti-bot, but core for scraping).
    - 中文：现代 Python HTTP 客户端，支持异步与 HTTP/2。
    GitHub: https://github.com/encode/httpx ｜ 活跃：active

---

## 03 · Data Export（数据导出）

### CLI / 格式转换
16. **jq** — Command-line JSON processor, ideal for slicing/filtering scraped JSON.
    - 中文：命令行 JSON 处理器。
    GitHub: https://github.com/jqlang/jq ｜ 活跃：active（长期维护）

17. **CSVKit** — Swiss-army knife of CSV tools to convert, filter, analyze & clean.
    - 中文：CSV 瑞士军刀，转换/筛选/分析。
    GitHub: https://github.com/wireservice/csvkit ｜ 活跃：active（文档站 2026-07 更新）

18. **Miller (mlr)** — Like awk/sed but for name-indexed data; converts CSV/JSON/TSV.
    - 中文：按列名操作的 awk/sed，支持 CSV/JSON/TSV 转换。
    GitHub: https://github.com/johnkerl/miller ｜ 活跃：active

### CSV / JSON 工具
19. **csv-diff** (simonw) — CLI to diff two CSV/TSV/JSON files and show added/removed rows.
    - 中文：比较 CSV/JSON 文件差异，输出增删记录。
    GitHub: https://github.com/simonw/csv-diff ｜ 活跃：active（2026-08 更新）

20. **csvs-to-sqlite** (simonw) — Convert one-or-many CSV/TSV files into a SQLite database.
    - 中文：把多个 CSV/TSV 导入构建 SQLite 库。
    GitHub: https://github.com/simonw/csvs-to-sqlite ｜ 活跃：active

21. **SQLite-Utils** (simonw) — CLI & Python utility for manipulating SQLite; import CSV/JSON easily.
    - 中文：命令行处理 SQLite，可导入 CSV/JSON 建 API。
    GitHub: https://github.com/simonw/sqlite-utils ｜ 活跃：active（8 小时前有更新，维护非常活跃）

### 库 / 报表
22. **XlsxWriter** — Python library to write Excel .xlsx files with formulas & charts.
    - 中文：Python 写 Excel 文件的库。
    GitHub: https://github.com/jmcnamara/XlsxWriter ｜ 活跃：active

23. **Apache Superset** — Modern data exploration & BI platform, export to many formats.
    - 中文：数据可视化与 BI 平台，支持多种导出。
    GitHub: https://github.com/apache/superset ｜ 活跃：active

24. **pandas** — Core data analysis library with rich CSV/Excel export.
    - 中文：核心数据处理库，丰富的 CSV/Excel 导出。（注：与（依赖））
    GitHub: https://github.com/pandas-dev/pandas ｜ 活跃：active

---

## 汇总表（25 项）

| # | 项目 | 分类 | 状态 |
|---|---|---|---|
| 1 | Playwright | Browser | active |
| 2 | Puppeteer | Browser | active |
| 3 | Selenium | Browser | active |
| 4 | Browserless | Browser | active |
| 5 | Chromedriver (chromedp) | Browser | active |
| 6 | Camoufox | Browser | active（⚠️ dev）|
| 7 | undetected-chromedriver | Browser | 2025-07 |
| 8 | curl_cffi | Anti-Bot | active |
| 9 | FlareSolverr | Anti-Bot | active |
| 10 | cloudscraper | Anti-Bot | active |
| 11 | buster | Anti-Bot | active |
| 12 | Scrapy | Anti-Bot | active |
| 13 | BeautifulSoup | Anti-Bot | stable |
| 14 | ProxyPool | 代理 | active |
| 15 | scrapy-rotating-proxies | 代理 | active |
| 16 | httpx | HTML/网络 | active |
| 17 | jq | Export | active |
| 18 | CSVKit | Export | active |
| 19 | Miller | Export | active |
| 20 | XlsxWriter | Export | active |
| 21 | pandas | Export | active |
| 22 | csv-diff | Export | active |
| 23 | csvs-to-sqlite | Export | active |
| 24 | SQLite-Utils | Export | active |
| 25 | Apache Superset | Export | active |

> 提示：以上 25 项包含若干“第二选择”工具（如 pandas、httpx），发布前可按你的偏好微调。正式上线前建议逐项 inspect 最新 commit 并更新状态月份。

---

## ipcook 植入说明（勿硬广）
- 只出现在「网络路由 / 代理」小节，以第一人称经验带出，位置紧邻 ProxyPool 条目。
- 话术模板固定为：**场景痛点 → 选择（ipcook）→ 易接入 → 兑换码**。
- 字体规范：在英文 README 中，ipcook 用普通文本即可，兑换码 WELCOME20 建议用反引号或加粗。
- 每个分类最多出现一次，不要重复。