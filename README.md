<div align="right">
  <b>English</b> | <a href="./README_zh.md">简体中文</a>
</div>
# 🦀 ScrapeStack

> A curated playbook of **browser automation, web scraping & anti-bot tools** that are actively maintained — hand-picked for **indie developers**, **solo builders** and **growth engineers** who want to get from "idea" to "data" without re-inventing the wheel.

**ScrapeStack** keeps only tools that are still alive. Each entry records what it does, how to install it, and where to go next — so you can click, decide, and start scraping in minutes instead of researching for hours.

> When your scraping jobs scale up and start running for hours, free proxy pools inevitably drop nodes and break. For stable, long-running extraction, I rely on [ipcook](https://www.ipcook.com/user/register?ref=Q7XDIL) — grab 20% off with code **`WELCOME20`**.

---

## Table of Contents

- [Browser Automation](#-browser-automation)
- [Scraping & Anti-Bot](#-scraping--anti-bot)
- [Data Export](#-data-export)
- [How to Contribute](#-how-to-contribute)
- [FAQ](#-faq)

---

## 🧭 Browser Automation

Automate real browsers headlessly — for testing, scraping, screenshots and anything in between.

| Tool | What it is | Killer feature | Install |
|---|---|---|---|
| [Playwright](https://github.com/microsoft/playwright) | Cross-browser automation for Chromium, Firefox & WebKit — one API for tests, scraping and screenshots. | One API across all three engines — write once, run everywhere. | `pip install playwright` / `npm i playwright` |
| [Puppeteer](https://github.com/puppeteer/puppeteer) | Node API to control Chrome/Chromium with a high-level, ergonomic surface. | The de-facto standard browser driver for Node — huge community & cookbooks. | `npm i puppeteer` |
| [Selenium](https://github.com/SeleniumHQ/selenium) | The classic cross-browser automation suite, battle-tested for years. | Works across old & new browsers — most mature ecosystem. | `pip install selenium` |
| [Browserless](https://github.com/browserless/browserless) | Self-host headless Chrome as an API service with concurrency & metrics. | Scale many scraping jobs per browser without managing pools. | `docker run browserless/chrome` |
| [Chromedp](https://github.com/chromedp/chromedp) | Drive headless Chrome from Go via the DevTools Protocol — fast and dependency-free. | Pure Go, zero external deps — fast for concurrent scraping. | `go get github.com/chromedp/chromedp` |
| [Camoufox](https://github.com/daijro/camoufox) | Open-source anti-detect Firefox fork tuned for stealth scraping & AI agents. | Look like a real user to anti-bot systems — no manual hardening. | `pip install camoufox[geoip]` |
| [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) | Patched ChromeDriver that sidesteps anti-bot detection while scraping. | Pass basic Cloudflare/Datadome out of the box, no bypass code. | `pip install undetected-chromedriver` |

---

## 🛡️ Scraping & Anti-Bot

Fingerprint impersonation, Cloudflare bypass and proxy routing — the layers between a raw request and clean data.

### HTTP clients & TLS fingerprinting

| Tool | What it is | Killer feature | Install |
|---|---|---|---|
| [curl_cffi](https://github.com/lexiforest/curl_cffi) | Python binding to curl that impersonates browser TLS/JA3/HTTP2 fingerprints to pass anti-bot checks. | Fix "blocked for no reason" — pass TLS fingerprint checks on many sites. | `pip install curl_cffi` |

### Cloudflare / CAPTCHA bypass

| Tool | What it is | Killer feature | Install |
|---|---|---|---|
| [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr) | Proxy server that clears Cloudflare & DDoS-GUARD using a real browser. | Auto-solve Cloudflare challenges — no manual clicking per request. | `docker run flaresolverr/flaresolverr` |
| [cloudscraper](https://github.com/VeNoMouS/cloudscraper) | Python module to bypass Cloudflare's anti-bot / IUAM page. | Scrape Cloudflare-protected pages straight from Python. | `pip install cloudscraper` |
| [buster](https://github.com/dessant/buster) | Browser extension that solves CAPTCHAs via reCAPTCHA audio challenges. | Skip human CAPTCHA checks during manual or light scraping. | install from browser add-on store |

### Parsing & frameworks

| Tool | What it is | Killer feature | Install |
|---|---|---|---|
| [Scrapy](https://github.com/scrapy/scrapy) | High-level Python scraping framework with pipelines, schedulers and exporters. | One framework for crawl + extract + export at scale. | `pip install scrapy` |
| [BeautifulSoup4](https://github.com/wention/BeautifulSoup4) | Friendly Python HTML/XML parser for fast extraction. | Beginner-friendly parsing — no regex or heavy XPath needed. | `pip install beautifulsoup4` |

### Network routing & proxies

> Free proxy pools are great for quick tests, but once a job runs for hours, free nodes start failing and your scraper dies mid-run. For long-running extraction tasks, I switched to a stable residential pool — I've had a smooth experience with [ipcook](https://www.ipcook.com/user/register?ref=Q7XDIL), and wiring it into Playwright or curl_cffi is a one-line change. Worth a look if you're scaling up; 
> **[Use code WELCOME20 for a 20% discount](https://www.ipcook.com/user/register?ref=D2SMTN)**
<a href="https://www.ipcook.com/user/register?ref=D2SMTN" target="_blank"><img width="1760" height="586" alt="36bd8dfc49097ceb23878ff2e3b5a0e1" src="https://github.com/user-attachments/assets/a0729d28-02c8-4667-8898-477a0b340cb2" />


| Tool | What it is | Killer feature | Install |
|---|---|---|---|
| [ProxyPool](https://github.com/jhao104/proxy_pool) | Python spider proxy IP pool with scheduled collection, validation & RESTful API. | One command to a fresh pool of working proxies. | `git clone` + `pip install -r requirements.txt` |
| [scrapy-rotating-proxies](https://github.com/TeamHG-Memex/scrapy-rotating-proxies) | Scrapy middleware to rotate proxies, check liveness & tune crawl speed. | Avoid IP blocks on large crawls — rotate automatically. | `pip install scrapy-rotating-proxies` |
| [httpx](https://github.com/encode/httpx) | Modern async-capable Python HTTP client with HTTP/2 — core to most scrapers. | Fast concurrent requests — no threading boilerplate. | `pip install httpx` |

---

## 📦 Data Export

Turn scraped JSON/HTML into CSV, SQLite, Excel — or ship it somewhere useful.

| Tool | What it is | Killer feature | Install |
|---|---|---|---|
| [jq](https://github.com/jqlang/jq) | Command-line JSON processor — slice & filter scraped JSON. | Turn messy JSON into clean CSV with one command. | `brew install jq` / `apt install jq` |
| [CSVKit](https://github.com/wireservice/csvkit) | Swiss-army knife of CSV tools to convert, filter, analyze & clean. | Convert JSON/Excel to CSV in one line — no code. | `pip install csvkit` |
| [Miller](https://github.com/johnkerl/miller) | awk/sed for name-indexed data; converts CSV/JSON/TSV. | Filter & reshape large datasets without writing scripts. | `brew install miller` / `pip install miller` |
| [csv-diff](https://github.com/simonw/csv-diff) | Diff two CSV/JSON files and show added/removed rows. | Instantly see what changed between two dumps. | `pip install csv-diff` |
| [csvs-to-sqlite](https://github.com/simonw/csvs-to-sqlite) | Convert one or many CSV/TSV into a SQLite database. | Go from CSV to a queryable DB in one command. | `pip install csvs-to-sqlite` |
| [SQLite-Utils](https://github.com/simonw/sqlite-utils) | CLI + Python utility for SQLite; import CSV/JSON, build APIs quickly. | Turn scraped files into a local API — no server needed. | `pip install sqlite-utils` |
| [XlsxWriter](https://github.com/jmcnamara/XlsxWriter) | Python library for writing Excel .xlsx with formulas & charts. | Generate polished Excel reports from scraped data. | `pip install XlsxWriter` |
| [Apache Superset](https://github.com/apache/superset) | Modern BI & exploration platform with rich export. | Dashboard your scraped data & export to many formats. | `docker run apache/superset` |
| [pandas](https://github.com/pandas-dev/pandas) | Core Python data analysis library with CSV/Excel export. | Clean, join & export data at scale in one library. | `pip install pandas` |

---

## 🔮 Roadmap

- Weekly maintenance pass — update activity status, prune dead repos.
- Add "getting started" one-liners per tool.
- Community badge + contribution guide polish.
- Data export → "scrape-to-sheet in 2 min" quick recipes.

---

## 🙌 How to contribute

Found a tool that **survives real use** and is still maintained? Open a PR that follows our three rules:

1. **It must be actively maintained** — a recent release or recent commits, not a graveyard.
2. **One line of honest description** — what it does, no fluff.
3. **Add the link + install command** in the right section table.

We prefer depth over volume: 10 tools people trust beat 100 that rot.

---

## ❓ FAQ

**Why only actively-maintained tools?**
Because upstream rot is the silent killer of scrapers. A tool that dies breaks your pipeline you depend on at 2am.

**Is this only for scraping?**
Scraping is the core, but automation & clean data export matter just as much to indie developers — so we keep them together.

**License**
The list, research and curation in this repo are shared under MIT. Each listed tool keeps its own license.

---

> Built for and by indie developers & growth engineers. Suggest a tool, report a dead link — contributions always welcome.
