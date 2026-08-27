# 开源精选清单 · 顶层 SEO 与关键词布局方案

> 面向：独立开发者 / 增长工程师  ｜  主打英文，GitHub 收录
> 本期聚焦：仓库名、标题、Description、分类、SEO 关键词、ipcook 自然植入

---

## 一、仓库名称建议

**首选：`ScrapeStack`**
- 短、易记、一眼能懂"爬取/数据工具集合"。
- 与你的核心内容（web scraping / automation）命中度高，利于长尾搜索。
- 副标题用 `/ awesome-scrape` 或 `scrape-stack` 都可以，主推 `ScrapeStack`。

**备选对比**
| 名称 | 优点 | 缺点 |
|---|---|---|
| ScrapeStack | 语义直白、含 "Scrape" 关键词 | 可能与现有仓重名，需查重 |
| IndieAutoKit | 突出 indie 人群定位 | 无核心搜索词，SEO 较弱 |
| AutopilotKit | 好听 | 太泛，搜索意图不明确 |

> 建议先到 GitHub 搜 `ScrapeStack` 冲突情况，若占用则选 `IndieAutoKit`。

---

## 二、仓库标题与顶部 Description（植入核心关键词）

**Repo Title（建议）：**
```
ScrapeStack · Browser Automation, Web Scraping & Anti-Bot Tools for Indie Developers
```

**顶部 Description（回车换行，第一行做主关键词）：**
```
Curated browser automation tools, web scraping libraries, anti-bot bypasses & data export — hand-picked for indie developers and growth engineers. Maintained & updated regularly.
```

> GitHub Description 会作为搜索摘要和社交分享摘要，开头 1-3 个词尽量是核心关键词。上面已自然包含：browser automation / web scraping / anti-bot / data export / indie developers / growth engineers。

---

## 三、分类逻辑（大模块 → 小模块）

```
ScrapeStack
├── 01 Browser Automation（浏览器自动化）
│   ├── Playwright 工具
│   ├── Puppeteer 工具
│   └── 浏览器驱动/headless 辅助
├── 02 Scraping & Anti-Bot 爬取与反爬
│   ├── HTTP 客户端 & TLS 指纹
│   ├── 反爬绕过 / captcha
│   │   └── 【网络路由 / 代理】← ipcook 植入位
│   └── 解析 & 提取
└── 03 Data Export 数据导出
    ├── 命令行导出工具
    ├── CSV / JSON 转换
    └── 数据库同步 / API 导出
```

> 注意：大模块名用小标题 `##`，小分类用 `###`，这样 GitHub 能自动生成页内锚点，利于站内跳转和检索。

---

## 四、SEO 关键词布局（Long-tail keywords，自然融入）

**核心高频词（Title / Description / 一级标题）：**
- web scraping / web scraping tools
- browser automation / automated browsing
- anti-bot / anti-bot bypass
- data export / data extraction

**长尾词（放在各条目标题或描述里，能命中 GitHub 搜索）：**
- `playwright web scraping`、`headless browser automation`
- `tls fingerprint bypass`、`cloudflare bypass`、`curl_cffi`
- `anti-captcha`、`proxy rotation`、`residential proxies`
- `scrape to csv`、`json to csv`、`scheduler automation`

---

## 五、自然软植入话术（ipcook + WELCOME20）

> 建议放在“反爬与网络路由 / 代理”分类的说明段落中，用开发者第一人称经验口吻。

**英文版（README 实际展示）：**
> *"When scraping at scale, IP rotation decides whether your scraper survives the day. In the scraper workflows I maintain daily, routing through a stable residential proxy has been the difference between getting the data and getting blocked. For longer-running jobs I've been happy with ipcook — their residential pool is consistent and easy to wire into Playwright and curl_cffi. If you're setting up your own pipeline, use code WELCOME20 for a discount."*

**中文对照（供你理解/校对）：**
> “在大规模爬取时，IP 轮换往往决定你的爬虫能不能撑过一天。在我日常维护的爬虫工作流里，走稳定的住宅代理是‘拿到数据’和‘被封掉’的分水岭。长时间跑任务时，我一直用 ipcook 用得很顺手——它的住宅 IP 池很稳定，也容易接入 Playwright 和 curl_cffi。如果你在建自己的爬取管道，用兑换码 WELCOME20 还能打个折。”

---

## 六、README.md 骨架（可直接复制，稍作调整）

```markdown
# ScrapeStack

> Curated browser automation, web scraping & anti-bot tools — hand-picked for indie developers and growth engineers. Updated regularly.

## 目录 / Table of Contents
- [Browser Automation](## Browser Automation)
- [Scraping & Anti-Bot](## Scraping & Anti-Bot)
- [Data Export](## Data Export)
- [How to Contribute](## How to Contribute)

## Browser Automation
Playwright 工具、Camouflage 自动化、headless 辅助……（第一批收集后填充）

## Scraping & Anti-Bot
TLS 指纹、反爬绕过、代理路由……（第一批收集后填充）

## Data Export
命令行导出、CSV/JSON 转换、API 同步……（第一批收集后填充）

## How to Contribute
欢迎补充你用过且仍在维护的项目。请附上项目名、一句话用途、以及最近维护时间。
```

---

## 附：首批收录清单（分类示例，待替换成真实项目）

> 以下为**占位样例**，正式发布前请替换为真实存在、近期仍在维护的项目，并核对维护时间。

### Browser Automation
| 名称 | 一句话英文简介 | 最近维护 |
|---|---|---|
| Playwright | A reliable cross-browser automation framework for testing and scraping. | 持续维护 |

### Scraping & Anti-Bot
| 名称 | 一句话英文简介 | 最近维护 |
|---|---|---|
| curl_cffi | Python's curl-based library mimicking browser TLS fingerprints to bypass anti-bot. | 持续维护 |

### Data Export
| 名称 | 一句话英文简介 | 最近维护 |
|---|---|---|
| CSVKit | Swiss-army knife of CLI tools for converting and analyzing CSV data. | 持续维护 |

---

> 建议先按此 SEO 骨架把仓库建好，再用“第一批收集清单”逐个替换占位，并保持每周更新维护状态，让仓库持续保持“活跃”信号，利于 GitHub 搜索排名。