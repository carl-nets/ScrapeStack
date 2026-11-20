<div align="right">
  <b>English</b> | <a href="./README_zh.md">简体中文</a>
</div>

# 🦀 ScrapeStack

> Looking for the **best web scraping tools and browser automation frameworks** in 2026? This curated directory covers **web scraping tools, headless browser automation, anti-bot bypass and scraped data export** — every entry still actively maintained, hand-picked for **indie developers**, **solo builders** and **growth engineers** who want to get from "idea" to "data" in Python, Node or Go without re-inventing the wheel.

**ScrapeStack** keeps only tools that are still alive — and **proves it**: every entry is re-checked automatically every week, and the live report lives in [STATUS.md](STATUS.md). Each entry records what it does, how to install it, and where to go next — so you can click, decide, and start scraping in minutes instead of researching for hours.

![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)
![List status](https://img.shields.io/badge/status-verified%20weekly-brightgreen.svg)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)

> When your scraping jobs scale up and start running for hours, free proxy pools inevitably drop nodes and break. For stable, long-running extraction, I rely on [ipcook](https://www.ipcook.com/user/register?ref=Q7XDIL) — grab 20% off with code **`WELCOME20`**. <sup>\*</sup>

---

## Table of Contents

- [Browser Automation](#-browser-automation)
- [AI Browsing Agents](#-ai-browsing-agents)
- [Scraping & Anti-Bot](#-scraping--anti-bot)
- [Data Export](#-data-export)
- [How This List Stays Alive](#-how-this-list-stays-alive)
- [How to Contribute](#-how-to-contribute)
- [Similar Lists](#-similar-lists)
- [FAQ](#-faq)

---

## 🧭 Browser Automation

The best **headless browser automation tools** for web scraping, UI testing, screenshots and anything in between — Playwright, Puppeteer, Selenium and anti-detect alternatives.

| Tool | What it is | Killer feature | Install |
|---|---|---|---|
| [Playwright](https://github.com/microsoft/playwright) | Cross-browser automation for Chromium, Firefox & WebKit — one API for tests, scraping and screenshots. | One API across all three engines — write once, run everywhere. | `pip install playwright` / `npm i playwright` |
| [Puppeteer](https://github.com/puppeteer/puppeteer) | Node API to control Chrome/Chromium with a high-level, ergonomic surface. | The de-facto standard browser driver for Node — huge community & cookbooks. | `npm i puppeteer` |
| [Selenium](https://github.com/SeleniumHQ/selenium) | The classic cross-browser automation suite, battle-tested for years. | Works across old & new browsers — most mature ecosystem. | `pip install selenium` |
| [Browserless](https://github.com/browserless/browserless) | Self-host headless Chrome as an API service with concurrency & metrics. | Scale many scraping jobs per browser without managing pools. | `docker run -p 3000:3000 browserless/chrome` |
| [Chromedp](https://github.com/chromedp/chromedp) | Drive headless Chrome from Go via the DevTools Protocol — fast and dependency-free. | Pure Go, zero external deps — fast for concurrent scraping. | `go get github.com/chromedp/chromedp` |
| [DrissionPage](https://github.com/g1879/DrissionPage) | Drive Chromium and raw `requests` sessions through one unified API, switching between them freely. Strong anti-detection, hugely popular in the Chinese dev community. | Mix browser power and raw-request speed in one workflow — cookies and logins carry across both. | `pip install DrissionPage` |
| [nodriver](https://github.com/ultrafunkamsterdam/nodriver) | Successor to undetected-chromedriver from the same author: drives Chrome/Edge over the raw DevTools Protocol — no Selenium layer, fewer fingerprinting artifacts. | Stays invisible to basic anti-bot without patching or maintaining a patched driver. | `pip install nodriver` |
| [Camoufox](https://github.com/daijro/camoufox) | Open-source anti-detect Firefox fork tuned for stealth scraping & AI agents. | Look like a real user to anti-bot systems — no manual hardening. | `pip install camoufox[geoip]` |

---

## 🤖 AI Browsing Agents

The 2026 trend in web automation: **AI web agents** that operate a real browser for you — **AI web scraping** without writing a single CSS selector. Point an LLM at a goal; it navigates, clicks, types and extracts.

| Tool | What it is | Killer feature | Install |
|---|---|---|---|
| [browser-use](https://github.com/browser-use/browser-use) | AI agent framework — an LLM (GPT, Claude, DeepSeek, …) drives a real browser end-to-end: navigate, click, type, extract. | Describe the goal — the model plans and executes the whole browsing session. | `pip install browser-use` |
| [Stagehand](https://github.com/browserbase/stagehand) | AI browser automation built on Playwright — natural-language act / extract / observe primitives. | One `extract()` call replaces fragile CSS/XPath selectors that break on every redesign. | `npm i @browserbasehq/stagehand` |
| [Skyvern](https://github.com/Skyvern-AI/skyvern) | Open-source vision-based browser agent (LLM + computer vision) that fills forms and runs end-to-end flows on ever-changing layouts. | It "sees" the page like a human — no brittle selectors to maintain at all. | `git clone` + `docker compose up` |

---

## 🛡️ Scraping & Anti-Bot

How to scrape protected websites: **TLS fingerprint impersonation**, **Cloudflare bypass**, **CAPTCHA solving** and proxy routing — the layers between a raw request and clean data.

### HTTP clients & TLS fingerprinting

Stealth HTTP clients that impersonate real browser TLS, JA3 and HTTP/2 fingerprints — so your requests pass anti-bot checks instead of being blocked.

| Tool | What it is | Killer feature | Install |
|---|---|---|---|
| [curl_cffi](https://github.com/lexiforest/curl_cffi) | Python binding to curl that impersonates browser TLS/JA3/HTTP2 fingerprints to pass anti-bot checks. | Fix "blocked for no reason" — pass TLS fingerprint checks on many sites. | `pip install curl_cffi` |
| [httpx](https://github.com/encode/httpx) | Modern async-capable Python HTTP client with HTTP/2 — core to most scrapers. | Fast concurrent requests — no threading boilerplate. | `pip install httpx` |

### Cloudflare / CAPTCHA bypass

Tools that automatically clear **Cloudflare challenge pages, DDoS-GUARD and CAPTCHAs** during a scrape.

| Tool | What it is | Killer feature | Install |
|---|---|---|---|
| [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr) | Proxy server that clears Cloudflare & DDoS-GUARD using a real browser. | Auto-solve Cloudflare challenges — no manual clicking per request. | `docker run -p 8191:8191 flaresolverr/flaresolverr` |
| [cloudscraper](https://github.com/VeNoMouS/cloudscraper) | Python module to bypass Cloudflare's anti-bot / IUAM page. ⚠️ Maintained more slowly lately — see [STATUS.md](STATUS.md). | Scrape Cloudflare-protected pages straight from Python. | `pip install cloudscraper` |
| [buster](https://github.com/dessant/buster) | Browser extension that solves CAPTCHAs via reCAPTCHA audio challenges. | Skip human CAPTCHA checks during manual or light scraping. | Browser add-on store |

### Parsing & extraction

Fast, robust HTML parsers and content extractors — turn raw HTML into clean text, structured data or article-ready copy.

| Tool | What it is | Killer feature | Install |
|---|---|---|---|
| [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) | Friendly Python HTML/XML parser for fast extraction. | Beginner-friendly parsing — no regex or heavy XPath needed. | `pip install beautifulsoup4` |
| [parsel](https://github.com/scrapy/parsel) | Scrapy's selector engine, standalone — CSS, XPath and regex extraction in one small API. | Write selectors once, reuse them in plain scripts or inside Scrapy. | `pip install parsel` |
| [lxml](https://github.com/lxml/lxml) | Industrial-grade C-accelerated HTML/XML parsing and XPath engine. | The fast, robust backbone most other Python parsers build on. | `pip install lxml` |
| [selectolax](https://github.com/rushter/selectolax) | Cython HTML5 parser built on the Lexbor engine — CSS-selector speed far beyond lxml/BeautifulSoup. | Parsing-heavy jobs run several times faster with the same familiar CSS API. | `pip install selectolax` |
| [trafilatura](https://github.com/adbar/trafilatura) | Extracts clean main text, title and date from raw HTML — strips navigation and ads, built for corpora and research. | Raw page → article-ready text in one function call. | `pip install trafilatura` |

### Scraping frameworks

Full-scale **web scraping frameworks** with scheduling, pipelines, proxy rotation and built-in anti-detection.

| Tool | What it is | Killer feature | Install |
|---|---|---|---|
| [Scrapy](https://github.com/scrapy/scrapy) | High-level Python scraping framework with pipelines, schedulers and exporters. | One framework for crawl + extract + export at scale. | `pip install scrapy` |
| [botasaurus](https://github.com/omkarcloud/botasaurus) | Scraping framework with built-in anti-detection, proxy rotation, task scheduling and a GUI for debugging jobs. | Battle-tested anti-detect defaults plus a ready-made UI to watch jobs live. | `pip install botasaurus` |

### Network routing & proxies

Keep long-running scrapers alive with rotating proxies — from free proxy pools to stable residential proxies for web scraping.

> Free proxy pools are great for quick tests, but once a job runs for hours, free nodes start failing and your scraper dies mid-run. For long-running extraction tasks, I switched to a stable residential pool — I've had a smooth experience with [ipcook](https://www.ipcook.com/user/register?ref=Q7XDIL), and wiring it into Playwright or curl_cffi is a one-line change. Worth a look if you're scaling up —
> **[Use code WELCOME20 for a 20% discount](https://www.ipcook.com/user/register?ref=Q7XDIL)**
<a href="https://www.ipcook.com/user/register?ref=Q7XDIL" target="_blank"><img width="1760" height="586" alt="ipcook residential proxy for web scraping — stable IP pool" src="https://github.com/user-attachments/assets/a0729d28-02c8-4667-8898-477a0b340cb2" /></a>

| Tool | What it is | Killer feature | Install |
|---|---|---|---|
| [ProxyPool](https://github.com/jhao104/proxy_pool) | Python spider proxy IP pool with scheduled collection, validation & RESTful API. | One command to a fresh pool of working proxies. | `git clone` + `pip install -r requirements.txt` |
| [scrapy-rotating-proxies](https://github.com/TeamHG-Memex/scrapy-rotating-proxies) | Scrapy middleware to rotate proxies, check liveness & tune crawl speed. | Avoid IP blocks on large crawls — rotate automatically. | `pip install scrapy-rotating-proxies` |

---

## 📦 Data Export

Turn scraped JSON/HTML into **CSV, Excel, SQLite** — clean, analyze and publish your scraped data with one-liners.

| Tool | What it is | Killer feature | Install |
|---|---|---|---|
| [jq](https://github.com/jqlang/jq) | Command-line JSON processor — slice & filter scraped JSON. | Turn messy JSON into clean CSV with one command. | `brew install jq` / `apt install jq` |
| [CSVKit](https://github.com/wireservice/csvkit) | Swiss-army knife of CSV tools to convert, filter, analyze & clean. | Convert JSON/Excel to CSV in one line — no code. | `pip install csvkit` |
| [Miller](https://github.com/johnkerl/miller) | awk/sed for name-indexed data; converts CSV/JSON/TSV. | Filter & reshape large datasets without writing scripts. | `brew install miller` |
| [DuckDB](https://github.com/duckdb/duckdb) | In-process columnar analytics database — query CSV/JSON/Parquet files directly with SQL, zero import. | Ad-hoc analytics on scraped dumps without writing a single load script. | `pip install duckdb` |
| [csv-diff](https://github.com/simonw/csv-diff) | Diff two CSV/JSON files and show added/removed rows. ⚠️ Low activity, but stable for what it does — see [STATUS.md](STATUS.md). | Instantly see what changed between two dumps. | `pip install csv-diff` |
| [csvs-to-sqlite](https://github.com/simonw/csvs-to-sqlite) | Convert one or many CSV/TSV into a SQLite database. | Go from CSV to a queryable DB in one command. | `pip install csvs-to-sqlite` |
| [SQLite-Utils](https://github.com/simonw/sqlite-utils) | CLI + Python utility for SQLite; import CSV/JSON, build APIs quickly. | Turn scraped files into a local API — no server needed. | `pip install sqlite-utils` |
| [Datasette](https://github.com/simonw/datasette) | Turn a SQLite database into a browsable website and read-only JSON API in one command. | Share a scraped dataset as a URL instead of a file. | `pip install datasette` |
| [visidata](https://github.com/saulpw/visidata) | A spreadsheet in your terminal — browse, slice & reshape million-row dumps in seconds. | Explore data before deciding what to ship — no Jupyter needed. | `pip install visidata` |
| [XlsxWriter](https://github.com/jmcnamara/XlsxWriter) | Python library for writing Excel .xlsx with formulas & charts. | Generate polished Excel reports from scraped data. | `pip install XlsxWriter` |
| [Apache Superset](https://github.com/apache/superset) | Modern BI & exploration platform with rich export. | Dashboard your scraped data & export to many formats. | `docker run apache/superset` |
| [pandas](https://github.com/pandas-dev/pandas) | Core Python data analysis library with CSV/Excel export. | Clean, join & export data at scale in one library. | `pip install pandas` |

---

## 🔍 How This List Stays Alive

"Actively maintained" is a promise — so we verify it instead of assuming it:

1. `tools.json` is the **single source of truth** (one entry per listed tool).
2. A [GitHub Action](.github/workflows/weekly-status.yml) runs every Monday,
   queries the GitHub API for every repo, and regenerates [STATUS.md](STATUS.md).
3. **Archived** repos are flagged ❌ and get removed on the next pass.
   **Stale** repos (no push in 365+ days) are flagged ⚠️ until they recover or
   get retired — the reasoning behind every removal is logged in STATUS.md.

Run it yourself anytime: `python3 scripts/check_tools.py --out STATUS.md`

---

## 🔮 Roadmap

- [x] Weekly automated maintenance check (STATUS.md + CI).
- [ ] "Getting started" one-liner with a real example per tool.
- [ ] Scrape-to-sheet recipes: end-to-end 2-minute workflows per common use case.
- [ ] AI-agent quick recipes for browser-use / Stagehand / Skyvern.
- [ ] Community badge & issue templates polish.

---

## 🙌 How to contribute

Found a tool that **survives real use** and is still maintained? Open a PR that follows our three rules:

1. **It must be actively maintained** — a recent release or recent commits, not a graveyard.
2. **One line of honest description + one killer feature** — what it does, no fluff.
3. **Add the link + install command** in the right section table — and don't forget `tools.json`, so the weekly check starts watching it.

We prefer depth over volume: 10 tools people trust beat 100 that rot. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full checklist.

---

## 📚 Similar Lists

- [awesome-web-scraping](https://github.com/lorien/awesome-web-scraping) — the classic, broader catalog.
- [awesome-python·Web Scraping](https://github.com/vinta/awesome-python#web-scraping) — general-purpose Python picks.
- [awesome-crawler](https://github.com/BruceDone/awesome-crawler) — crawling frameworks across languages.

We intentionally stay smaller and verification-driven; if a tool dies, it gets flagged within a week.

---

## ❓ FAQ

**What are the best web scraping tools for Python?**
It depends on the wall you're hitting: `httpx` / `curl_cffi` for HTTP-level crawling, `parsel` / `lxml` / `selectolax` for parsing, Scrapy or botasaurus for full pipelines, and Playwright / nodriver / DrissionPage for JavaScript-heavy pages — every option in this list is actively maintained.

**How do I scrape a website to CSV or Excel?**
`jq` and CSVKit turn JSON into CSV in one line, Miller reshapes it, DuckDB lets you query raw dumps directly with SQL, `pandas` is the classic workhorse, and pandas + XlsxWriter produce polished `.xlsx` reports.

**How do I bypass Cloudflare when scraping?**
FlareSolverr and cloudscraper are the go-to starting points; for harder walls, anti-detect browsers (Camoufox, nodriver) or a residential proxy (ipcook) usually tip the balance. Always respect `robots.txt` and the site's ToS.

**Why only actively-maintained tools?**
Because upstream rot is the silent killer of scrapers. A tool that dies breaks your pipeline you depend on at 2am.

**How do you know a tool is still alive?**
We don't guess — the weekly [status check](STATUS.md) queries each repo's GitHub API for last-push date and archived flag.

**Is this only for scraping?**
Scraping is the core, but automation, AI browsing agents & clean data export matter just as much to indie developers — so we keep them together.

**Is scraping legal?**
Respect each site's `robots.txt` and Terms of Service, obey rate limits, and only collect data you're entitled to. This list is about building reliable pipelines — not breaking into systems that don't want us there.

**Why is there a sponsor in the list?**
A single, clearly-labelled sponsored slot (🎁ipcook) funds the maintenance work. <sup>\*</sup> The list itself stays independent — affiliate status never decides what gets listed.

**License**
The list, research and curation in this repo are shared under MIT. Each listed tool keeps its own license.

---

> Built for and by indie developers & growth engineers. From **web scraping with Python** to **headless browser automation** and **scraped data export** — build your scraping toolkit here. Suggest a tool, report a dead link — contributions always welcome.
>
> <sup>\*</sup> Affiliate disclosure: links with `ref=` are referral links — we may earn a commission on qualifying sign-ups. Prices for you are unaffected.
