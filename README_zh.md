<div align="right">
  <a href="./README.md">English</a> | <b>简体中文</b>
</div>

# 🦀 ScrapeStack

> 想找 2026 年**最好用的爬虫工具 / 网页爬取工具**？这里是一份持续维护的精选清单：涵盖 **Python 爬虫工具、浏览器自动化、反爬绕过（Cloudflare / 验证码）、爬取数据导出**——全部**仍在活跃维护**并每周机器体检，专为**独立开发 / 个人开发者 / 增长工程师**挑选。目标只有一个：让你从"想法"到"拿到数据"，不必重复造轮子。

**ScrapeStack** 只收录"还活着"的工具——而且**用证据说话**：每周自动对每个条目重新体检，实时报告见 [STATUS.md](STATUS.md)。每个条目都记录了它是什么、能帮你解决什么、以及如何安装——省去你几小时的调研，点击、决定、几分钟内就能开始爬取。

![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)
![List status](https://img.shields.io/badge/status-verified%20weekly-brightgreen.svg)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)

> 任务一旦跑上几小时，免费代理池的节点就开始失效、中途挂掉。长时间运行的抽取任务，我一直用 [ipcook](https://www.ipcook.com/user/register?ref=Q7XDIL) 来保障稳定，注册输入优惠码 **`WELCOME20`** 即可享受 8 折。 <sup>\*</sup>

---

## 目录

- [浏览器自动化](#-浏览器自动化)
- [AI 浏览智能体](#-ai-浏览智能体)
- [爬取与反爬](#-爬取与反爬)
- [数据导出](#-数据导出)
- [这份清单如何保持"活着"](#-这份清单如何保持活着)
- [如何贡献](#-如何贡献)
- [相关清单](#-相关清单)
- [FAQ 常见问题](#-faq-常见问题)

---

## 🧭 浏览器自动化

**浏览器自动化工具**精选：无头（headless）驱动真实浏览器，用于网页爬取、UI 测试、截图，以及你能想到的任何场景——Playwright、Puppeteer、Selenium，以及 Camoufox、nodriver 等反检测浏览器。

| 工具 | 说明 | 作用 | 安装方式 |
|---|---|---|---|
| [Playwright](https://github.com/microsoft/playwright) | 跨浏览器自动化：一套 API 覆盖 Chromium / Firefox / WebKit，用于测试、爬取、截图。 | 一套 API 通吃三种浏览器内核——写一次，处处能跑。 | `pip install playwright` / `npm i playwright` |
| [Puppeteer](https://github.com/puppeteer/puppeteer) | Node 库，以高层、顺手的 API 控制 Chrome / Chromium。 | Node 社区事实标准的浏览器驱动，教程与示例极多。 | `npm i puppeteer` |
| [Selenium](https://github.com/SeleniumHQ/selenium) | 经多年实战检验的经典跨浏览器自动化套件。 | 一套工具兼容新旧浏览器，生态最成熟。 | `pip install selenium` |
| [Browserless](https://github.com/browserless/browserless) | 把无头 Chrome 自托管为一个 API 服务，自带并发与监控。 | 一台浏览器并发跑大量爬取任务，不用自管浏览器池。 | `docker run -p 3000:3000 browserless/chrome` |
| [Chromedp](https://github.com/chromedp/chromedp) | 在 Go 中通过 DevTools 协议驱动无头 Chrome——快速且零依赖。 | 纯 Go、零外部依赖，适合并发爬取。 | `go get github.com/chromedp/chromedp` |
| [DrissionPage](https://github.com/g1879/DrissionPage) | 一套 API 同时驱动 Chromium 与 requests 会话并自由切换，反检测能力强，中文社区非常活跃的大杀器。 | 浏览器与人肉 request 混着用，Cookie/登录态互通，不用重复登录。 | `pip install DrissionPage` |
| [nodriver](https://github.com/ultrafunkamsterdam/nodriver) | undetected-chromedriver（同作者）的正统继任者：直接基于 DevTools 协议驱动 Chrome/Edge，不再依赖 Selenium，指纹痕迹更少。 | 不用补丁、不用维护改版驱动，就能过基础反爬检测。 | `pip install nodriver` |
| [Camoufox](https://github.com/daijro/camoufox) | 面向隐形爬取与 AI 助手的开源反检测 Firefox 分支。 | 在反爬系统眼里"像真人用户"，无需自己加固浏览器。 | `pip install camoufox[geoip]` |

---

## 🤖 AI 浏览智能体

2026 年网页自动化新趋势：**AI 网页智能体**——给 LLM 一个目标，它自己操作真实浏览器替你干活（**AI 爬取**），不用再写一条 CSS 选择器。

| 工具 | 说明 | 作用 | 安装方式 |
|---|---|---|---|
| [browser-use](https://github.com/browser-use/browser-use) | AI 智能体框架——让 LLM（GPT / Claude / DeepSeek …）自己操作真实浏览器完成任务：自动导航、点击、输入、提取。 | 你给目标、它自己规划并执行整个浏览过程。 | `pip install browser-use` |
| [Stagehand](https://github.com/browserbase/stagehand) | 基于 Playwright 的 AI 浏览器自动化框架：用自然语言完成操作 / 提取 / 观察。 | 一句 `extract()` 顶掉一打一改版就碎的 CSS/XPath 选择器。 | `npm i @browserbasehq/stagehand` |
| [Skyvern](https://github.com/Skyvern-AI/skyvern) | 开源视觉智能体（LLM + 计算机视觉）：自动填表、跑通端到端任务，专治布局天天变的页面。 | 它像人一样"看"页面——完全没有脆弱的 CSS 选择器要维护。 | `git clone` + `docker compose up` |

---

## 🛡️ 爬取与反爬

被反爬拦住怎么办？**TLS 指纹伪装、绕过 Cloudflare、自动过验证码、代理路由**——这些是"原始请求"和"干净数据"之间的层层关卡。

### HTTP 客户端与 TLS 指纹

模拟真实浏览器 TLS/JA3/HTTP2 指纹的隐形 HTTP 客户端——让请求通过反爬校验，而不是被直接封掉。

| 工具 | 说明 | 作用 | 安装方式 |
|---|---|---|---|
| [curl_cffi](https://github.com/lexiforest/curl_cffi) | Python 库，模拟浏览器 TLS/JA3/HTTP2 指纹以通过反爬校验。 | 修复"莫名其妙被封"——通过很多网站的 TLS 指纹校验。 | `pip install curl_cffi` |
| [httpx](https://github.com/encode/httpx) | 现代异步 Python HTTP 客户端，支持 HTTP/2，多数爬虫的核心依赖。 | 快速并发请求，不用写一堆多线程样板代码。 | `pip install httpx` |

### Cloudflare / CAPTCHA 绕过

自动清除 **Cloudflare 挑战页、DDoS-GUARD 与验证码**的工具。

| 工具 | 说明 | 作用 | 安装方式 |
|---|---|---|---|
| [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr) | 用真实浏览器组件代理，绕开 Cloudflare 与 DDoS-GUARD 防护。 | 自动过 Cloudflare 挑战，不用每次手动点。 | `docker run -p 8191:8191 flaresolverr/flaresolverr` |
| [cloudscraper](https://github.com/VeNoMouS/cloudscraper) | Python 模块，绕过 Cloudflare 的反爬 / 防攻击模式页。⚠️ 近期维护放缓，见 [STATUS.md](STATUS.md)。 | 直接在 Python 里爬 Cloudflare 保护的页面。 | `pip install cloudscraper` |
| [buster](https://github.com/dessant/buster) | 浏览器扩展，通过 reCAPTCHA 音频挑战自动解答验证码。 | 手动/轻量爬取时，跳过人工验证码。 | 浏览器商店搜索安装 |

### 解析与提取

快而稳的 HTML 解析与正文提取工具——把原始 HTML 变成干净文本、结构化数据或可直接使用的文章正文。

| 工具 | 说明 | 作用 | 安装方式 |
|---|---|---|---|
| [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) | 友好的 Python HTML/XML 解析库，快速提取。 | 新手友好解析，不用正则也不用 XPath。 | `pip install beautifulsoup4` |
| [parsel](https://github.com/scrapy/parsel) | Scrapy 同款选择器引擎（独立版）：CSS / XPath / 正则一体解析。 | 选好选择器写法，普通脚本和 Scrapy 里都能复用。 | `pip install parsel` |
| [lxml](https://github.com/lxml/lxml) | 工业级 C 加速 HTML/XML 解析与 XPath 引擎。 | 又快又稳的底层引擎，很多解析库都建立在它之上。 | `pip install lxml` |
| [selectolax](https://github.com/rushter/selectolax) | 基于 Lexbor 引擎的 Cython HTML5 解析器，CSS 选择器速度远超 lxml / BeautifulSoup。 | 同样的 CSS 语法，解析密集型任务快好几倍。 | `pip install selectolax` |
| [trafilatura](https://github.com/adbar/trafilatura) | 从 HTML 自动抽取干净的正文 / 标题 / 日期，去掉导航与广告噪音，专为语料与研究设计。 | 一个函数调用，网页变可用正文。 | `pip install trafilatura` |

### 爬虫框架

带调度、管道、代理轮换与内置反检测的**大规模爬虫框架**。

| 工具 | 说明 | 作用 | 安装方式 |
|---|---|---|---|
| [Scrapy](https://github.com/scrapy/scrapy) | 高层 Python 爬取框架，自带管道、调度与导出。 | 一个框架搞定"爬取 + 解析 + 导出"，可规模化。 | `pip install scrapy` |
| [botasaurus](https://github.com/omkarcloud/botasaurus) | 自带反检测、代理轮换、任务调度与图形界面调试的爬虫框架。 | 出厂自带久经考验的反检测配置，还能开着网页实时盯任务。 | `pip install botasaurus` |

### 网络路由与代理

让长时间任务不因 IP 被封而中断——从免费代理池到稳定的住宅代理。

> 免费代理池做快速测试还不错，但任务一旦跑上几小时，免费节点开始失效、爬虫中途挂掉。长时间运行的抽取任务，建议改用稳定的住宅代理池——我一直在用 [ipcook](https://www.ipcook.com/user/register?ref=Q7XDIL)，接进 Playwright 或 curl_cffi 只需改一行配置。
> **[新手注册 8 折优惠码：`WELCOME20`](https://www.ipcook.com/user/register?ref=Q7XDIL)**
<a href="https://www.ipcook.com/user/register?ref=Q7XDIL" target="_blank"><img width="1760" height="586" alt="ipcook 住宅代理——网页爬取爬虫专用稳定 IP 池" src="https://github.com/user-attachments/assets/c71e1aa5-04e9-40e8-9c7c-bd5d65187f83" /></a>

| 工具 | 说明 | 作用 | 安装方式 |
|---|---|---|---|
| [ProxyPool](https://github.com/jhao104/proxy_pool) | 定时采集、校验、提供 RESTful API 的爬虫代理 IP 池。 | 一条命令拿到一批可用的新代理。 | `git clone` + `pip install -r requirements.txt` |
| [scrapy-rotating-proxies](https://github.com/TeamHG-Memex/scrapy-rotating-proxies) | Scrapy 中间件：轮换代理、检测存活、调节爬取速度。 | 大规模爬取自动轮换代理 IP，避免被封。 | `pip install scrapy-rotating-proxies` |

---

## 📦 数据导出

把爬到的数据转成 **CSV、Excel、SQLite**——清洗、分析、一行命令发布你的爬取成果。

| 工具 | 说明 | 作用 | 安装方式 |
|---|---|---|---|
| [jq](https://github.com/jqlang/jq) | 命令行 JSON 处理机器——切片、过滤抓到的 JSON。 | 一条命令把乱七八糟的 JSON 变成干净 CSV。 | `brew install jq` / `apt install jq` |
| [CSVKit](https://github.com/wireservice/csvkit) | CSV 瑞士军刀：转换、过滤、分析、清洗一条龙。 | 一行命令把 JSON/Excel 转成 CSV——不用写代码。 | `pip install csvkit` |
| [Miller](https://github.com/johnkerl/miller) | 面向带列名数据的 awk/sed；支持 CSV/JSON/TSV 互转。 | 不写脚本也能过滤、重塑大数据集。 | `brew install miller` |
| [DuckDB](https://github.com/duckdb/duckdb) | 进程内列式分析数据库：一条 SQL 直接查 CSV / JSON / Parquet，无需导入。 | 爬下来的数据直接开查，一行导入代码都不用写。 | `pip install duckdb` |
| [csv-diff](https://github.com/simonw/csv-diff) | CLI 工具，对比并输出两份 CSV/JSON 文件的新增/删除行。⚠️ 活跃度低但功能稳定，见 [STATUS.md](STATUS.md)。 | 立刻看出两份数据 dump 之间改了什么。 | `pip install csv-diff` |
| [csvs-to-sqlite](https://github.com/simonw/csvs-to-sqlite) | 把一个或多个 CSV/TSV 转为 SQLite 数据库。 | 一条命令把 CSV 变成可查询的数据库。 | `pip install csvs-to-sqlite` |
| [SQLite-Utils](https://github.com/simonw/sqlite-utils) | 命令行 + Python 工具：操作 SQLite，快速导入 CSV/JSON、搭建接口。 | 把抓到的文件变成本地接口，不用起服务器。 | `pip install sqlite-utils` |
| [Datasette](https://github.com/simonw/datasette) | 一条命令把 SQLite 数据库变成可浏览的网站 + 只读 JSON API。 | 把爬取结果用一个网址分享出去，而不是发文件。 | `pip install datasette` |
| [visidata](https://github.com/saulpw/visidata) | 终端里的电子表格：几秒浏览、切片、重塑百万行 CSV/JSON。 | 先肉眼过一遍数据再决定怎么用，不用开 Jupyter。 | `pip install visidata` |
| [XlsxWriter](https://github.com/jmcnamara/XlsxWriter) | Python 库，写出带公式与图表的 Excel .xlsx。 | 把爬到的数据生成漂亮的 Excel 报表。 | `pip install XlsxWriter` |
| [Apache Superset](https://github.com/apache/superset) | 现代 BI 与数据探索平台，支持丰富导出。 | 把爬到的数据显示成看板，并导出多种格式。 | `docker run apache/superset` |
| [pandas](https://github.com/pandas-dev/pandas) | 核心 Python 数据分析库，支持 CSV/Excel 导出。 | 一个库搞定清洗、合并、导出大量数据。 | `pip install pandas` |

---

## 🔍 这份清单如何保持"活着"

"活跃维护"是个承诺——所以我们用机器验证，而不是靠猜：

1. `tools.json` 是**唯一数据源**（每个收录工具一条记录）。
2. [GitHub Action](.github/workflows/weekly-status.yml) 每周一运行，逐个查询仓库的 GitHub API，重新生成 [STATUS.md](STATUS.md)。
3. **已归档**仓库标 ❌，下一轮直接移除；**停更**仓库（365 天无 push）标 ⚠️，直到它恢复或被淘汰——每次移除的原因都会记录在 STATUS.md 里。

随时可以本地跑：`python3 scripts/check_tools.py --out STATUS.md`

---

## 🔮 Roadmap（规划）

- [x] 每周自动维护体检（STATUS.md + CI）。
- [ ] 为每个工具补充"快速上手"一行（带真实示例）。
- [ ] 爬取到表格（scrape-to-sheet）配方：常见场景的端到端 2 分钟工作流。
- [ ] browser-use / Stagehand / Skyvern 的 AI 智能体快速配方。
- [ ] 完善社区徽章与 issue 模板。

---

## 🙌 如何贡献

你发现了一个**经得起真实使用、且仍在维护**的工具？请按照这三个规则提 PR：

1. **它必须仍在活跃维护**——最近有 release 或 commit，而不是"墓碑仓库"。
2. **一句诚实的说明 + 一句作用**——它是什么、它能解决什么问题，不吹不黑。
3. **在对应分类表格里加上链接 + 安装命令**——别忘了同步 `tools.json`，让每周体检开始盯上它。

我们重质不重量：10 个让人信赖的工具，胜过 100 个放着生锈的。完整检查清单见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 📚 相关清单

- [awesome-web-scraping](https://github.com/lorien/awesome-web-scraping) —— 经典大而全的爬虫清单。
- [awesome-python · Web Scraping](https://github.com/vinta/awesome-python#web-scraping) —— 通用 Python 精选。
- [awesome-crawler](https://github.com/BruceDone/awesome-crawler) —— 多语言的爬虫框架合集。

我们刻意保持更小、更"体检驱动"：工具一旦死掉，一周内就会被标记出来。

---

## ❓ FAQ（常见问题）

**Python 爬虫用哪些库？**
看你撞的是哪堵墙：HTTP 层用 `httpx` / `curl_cffi`，解析用 `parsel` / `lxml` / `selectolax`，完整流水线用 Scrapy 或 botasaurus，JS 渲染页面用 Playwright / nodriver / DrissionPage——这份清单里收录的都是仍在活跃维护的。

**怎么把爬到的数据导出成 CSV / Excel？**
`jq`、CSVKit 一行把 JSON 变 CSV；Miller 做重塑；DuckDB 直接 SQL 查数据 dump；`pandas` 是经典之选，配 XlsxWriter 就能产出漂亮的 `.xlsx` 报表。

**被 Cloudflare 拦了怎么办？**
FlareSolverr 和 cloudscraper 是入门首选；更硬的反爬就换反检测浏览器（Camoufox、nodriver）或住宅代理（ipcook），通常能打破僵局。永远先尊重 `robots.txt` 和站点条款。

**为什么要只收录活跃维护的工具？**
因为上游停更是爬虫的隐形杀手。一个工具悄悄死掉，会连带你半夜还在跑的数据管道一起崩。

**你怎么知道一个工具还活着？**
不靠猜——每周的[状态检查](STATUS.md)会逐个调用 GitHub API 查最后推送日期和是否归档。

**这个仓库只讲爬虫吗？**
爬虫是核心，但对独立开发者来说，自动化、AI 浏览智能体与干净的数据导出同样重要——所以我们把它们放在一起。

**爬虫合法吗？**
请尊重每个站点的 `robots.txt` 与用户协议、遵守限速要求，只采集你有权拿到的数据。这份清单讲的是"把可靠的数据管道造稳"，不是"闯进不欢迎我们的系统"。

**清单里为什么有赞助？**
有且只有一个、明确标注的赞助位（ipcook），用来支撑维护工作。 <sup>\*</sup> 清单本身保持独立——带不带推广码，绝不决定一个工具能否入选。

**许可协议**
本仓库的清单、研究与筛选内容以 MIT 协议开源。其中每个工具仍保留各自的许可证。

---

> 为独立开发者与增长工程师而建、也由他们共建。从 **Python 网页爬取** 到 **浏览器自动化** 再到 **爬取数据导出**——在这里搭起你的爬虫工具箱。有想推荐的工具？发现失效链接？欢迎随时提建议与贡献。
>
> <sup>\*</sup> 广告披露：带 `ref=` 的链接为推广链接，我们可能因有效注册获得佣金。你的价格不受影响。
