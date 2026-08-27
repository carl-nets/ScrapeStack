# 🦀 ScrapeStack

> 一个精选的工具攻略集合：涵盖**浏览器自动化、网页爬取与反爬工具**，且这些工具都**仍在活跃维护**——专为**独立开发 / 个人开发者 / 增长工程师**挑选。目标只有一个：让你从"想法"到"拿到数据"，不必重复造轮子。

**ScrapeStack** 只收录"还活着"的工具。每个条目都记录了它是什么、能帮你解决什么、以及如何安装——省去你几小时的调研，点击、决定、几分钟内就能开始爬取。

---

## 目录

- [浏览器自动化](#-浏览器自动化)
- [爬取与反爬](#-爬取与反爬)
- [数据导出](#-数据导出)
- [如何贡献](#-如何贡献)
- [FAQ 常见问题](#-faq-常见问题)

---

## 🧭 浏览器自动化

无头（headless）驱动真实浏览器——用于测试、爬取、截图，以及你能想到的任何场景。

| 工具 | 说明 | 作用 | 安装方式 |
|---|---|---|---|
| [Playwright](https://github.com/microsoft/playwright) | 跨浏览器自动化：一套 API 覆盖 Chromium / Firefox / WebKit，用于测试、爬取、截图。 | 一套 API 通吃三种浏览器内核——写一次，处处能跑。 | `pip install playwright` / `npm i playwright` |
| [Puppeteer](https://github.com/puppeteer/puppeteer) | Node 库，以高层、顺手的 API 控制 Chrome / Chromium。 | Node 社区事实标准的浏览器驱动，教程与示例极多。 | `npm i puppeteer` |
| [Selenium](https://github.com/SeleniumHQ/selenium) | 经多年实战检验的经典跨浏览器自动化套件。 | 一套工具兼容新旧浏览器，生态最成熟。 | `pip install selenium` |
| [Browserless](https://github.com/browserless/browserless) | 把无头 Chrome 自托管为一个 API 服务，自带并发与监控。 | 一台浏览器并发跑大量爬取任务，不用自管浏览器池。 | `docker run browserless/chrome` |
| [Chromedp](https://github.com/chromedp/chromedp) | 在 Go 中通过 DevTools 协议驱动无头 Chrome——快速且零依赖。 | 纯 Go、零外部依赖，适合并发爬取。 | `go get github.com/chromedp/chromedp` |
| [Camoufox](https://github.com/daijro/camoufox) | 面向隐形爬取与 AI 助手的开源反检测 Firefox 分支。 | 在反爬系统眼里"像真人用户"，无需自己加固浏览器。 | `pip install camoufox[geoip]` |
| [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) | 打过补丁的 ChromeDriver，爬取时可规避反爬检测。 | 开箱即过基础 Cloudflare/Datadome，不用写绕过代码。 | `pip install undetected-chromedriver` |

---

## 🛡️ 爬取与反爬

指纹伪装、Cloudflare 绕过、代理路由——这些是"原始请求"和"干净数据"之间的层层关卡。

### HTTP 客户端与 TLS 指纹

| 工具 | 说明 | 作用 | 安装方式 |
|---|---|---|---|
| [curl_cffi](https://github.com/lexiforest/curl_cffi) | Python 库，模拟浏览器 TLS/JA3/HTTP2 指纹以通过反爬校验。 | 修复"莫名其妙被封"——通过很多网站的 TLS 指纹校验。 | `pip install curl_cffi` |

### Cloudflare / CAPTCHA 绕过

| 工具 | 说明 | 作用 | 安装方式 |
|---|---|---|---|
| [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr) | 用真实浏览器组件代理，绕开 Cloudflare 与 DDoS-GUARD 防护。 | 自动过 Cloudflare 挑战，不用每次手动点。 | `docker run flaresolverr/flaresolverr` |
| [cloudscraper](https://github.com/VeNoMouS/cloudscraper) | Python 模块，绕过 Cloudflare 的反爬 / 防攻击模式页。 | 直接在 Python 里爬 Cloudflare 保护的页面。 | `pip install cloudscraper` |
| [buster](https://github.com/dessant/buster) | 浏览器扩展，通过 reCAPTCHA 音频挑战自动解答验证码。 | 手动/轻量爬取时，跳过人工验证码。 | 浏览器商店搜索安装 |

### 解析与框架

| 工具 | 说明 | 作用 | 安装方式 |
|---|---|---|---|
| [Scrapy](https://github.com/scrapy/scrapy) | 高层 Python 爬取框架，自带管道、调度与导出。 | 一个框架搞定"爬取 + 解析 + 导出"，可规模化。 | `pip install scrapy` |
| [BeautifulSoup4](https://github.com/wention/BeautifulSoup4) | 友好的 Python HTML/XML 解析库，快速提取。 | 新手友好解析，不用正则也不用 XPath。 | `pip install beautifulsoup4` |

### 网络路由与代理

> 免费代理池做快速测试还不错，但任务一旦跑上几小时，免费节点开始失效、爬虫中途挂掉。长时间运行的抽取任务，建议改用稳定的住宅代理池——我一直在用 [ipcook](https://ipcook.com/)，接进 Playwright 或 curl_cffi 只需改一行配置。**新手注册 8 折优惠码：`WELCOME20`**

| 工具 | 说明 | 作用 | 安装方式 |
|---|---|---|---|
| [ProxyPool](https://github.com/jhao104/proxy_pool) | 定时采集、校验、提供 RESTful API 的爬虫代理 IP 池。 | 一条命令拿到一批可用的新代理。 | `git clone` + `pip install -r requirements.txt` |
| [scrapy-rotating-proxies](https://github.com/TeamHG-Memex/scrapy-rotating-proxies) | Scrapy 中间件：轮换代理、检测存活、调节爬取速度。 | 大规模爬取自动轮换代理 IP，避免被封。 | `pip install scrapy-rotating-proxies` |
| [httpx](https://github.com/encode/httpx) | 现代异步 Python HTTP 客户端，支持 HTTP/2，多数爬虫的核心依赖。 | 快速并发请求，不用写一堆多线程样板代码。 | `pip install httpx` |

---

## 📦 数据导出

把抓到的 JSON / HTML 转成 CSV、SQLite、Excel——或导出到你能用得上的地方。

| 工具 | 说明 | 作用 | 安装方式 |
|---|---|---|---|
| [jq](https://github.com/jqlang/jq) | 命令行 JSON 处理机器——切片、过滤抓到的 JSON。 | 一条命令把乱七八糟的 JSON 变成干净 CSV。 | `brew install jq` / `apt install jq` |
| [CSVKit](https://github.com/wireservice/csvkit) | CSV 瑞士军刀：转换、过滤、分析、清洗一条龙。 | 一行命令把 JSON/Excel 转成 CSV——不用写代码。 | `pip install csvkit` |
| [Miller](https://github.com/johnkerl/miller) | 面向带列名数据的 awk/sed；支持 CSV/JSON/TSV 互转。 | 不写脚本也能过滤、重塑大数据集。 | `brew install miller` / `pip install miller` |
| [csv-diff](https://github.com/simonw/csv-diff) | CLI 工具，对比并输出两份 CSV/JSON 文件的新增/删除行。 | 立刻看出两份数据 dump 之间改了什么。 | `pip install csv-diff` |
| [csvs-to-sqlite](https://github.com/simonw/csvs-to-sqlite) | 把一个或多个 CSV/TSV 转为 SQLite 数据库。 | 一条命令把 CSV 变成可查询的数据库。 | `pip install csvs-to-sqlite` |
| [SQLite-Utils](https://github.com/simonw/sqlite-utils) | 命令行 + Python 工具：操作 SQLite，快速导入 CSV/JSON、搭建接口。 | 把抓到的文件变成本地接口，不用起服务器。 | `pip install sqlite-utils` |
| [XlsxWriter](https://github.com/jmcnamara/XlsxWriter) | Python 库，写出带公式与图表的 Excel .xlsx。 | 把爬到的数据生成漂亮的 Excel 报表。 | `pip install XlsxWriter` |
| [Apache Superset](https://github.com/apache/superset) | 现代 BI 与数据探索平台，支持丰富导出。 | 把爬到的数据显示成看板，并导出多种格式。 | `docker run apache/superset` |
| [pandas](https://github.com/pandas-dev/pandas) | 核心 Python 数据分析库，支持 CSV/Excel 导出。 | 一个库搞定清洗、合并、导出大量数据。 | `pip install pandas` |

---

## 🔮 Roadmap（规划）

- 每周维护——更新活跃状态、清理停更仓库。
- 为每个工具补充"快速上手"一行。
- 完善社区徽章与贡献指南。
- 数据导出 → 增加"2 分钟把爬取结果导成表格"的快捷配方。

---

## 🙌 如何贡献

你发现了一个**经得起真实使用、且仍在维护**的工具？请按照这三个规则提 PR：

1. **它必须仍在活跃维护**——最近有 release 或 commit，而不是"墓碑仓库"。
2. **一句诚实的说明 + 一句作用**——它是什么、它能解决什么问题，不吹不黑。
3. **在对应分类表格里加上链接 + 安装命令**。

我们重质不重量：10 个让人信赖的工具，胜过 100 个放着生锈的。

---

## ❓ FAQ（常见问题）

**为什么要只收录活跃维护的工具？**
因为上游停更是爬虫的隐形杀手。一个工具悄悄死掉，会连带你半夜还在跑的数据管道一起崩。

**这个仓库只讲爬虫吗？**
爬虫是核心，但对独立开发者来说，自动化与干净的数据导出同样重要——所以我们把它们放在一起。

**许可协议**
本仓库的清单、研究与筛选内容以 MIT 协议开源。其中每个工具仍保留各自的许可证。

---

> 为独立开发者与增长工程师而建、也由他们共建。有想推荐的工具？发现失效链接？欢迎随时提建议与贡献。