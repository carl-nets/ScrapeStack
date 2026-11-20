#!/usr/bin/env python3
"""
ScrapeStack maintenance checker.

Reads tools.json (single source of truth), queries the GitHub API for every
listed repo, and regenerates STATUS.md with per-tool health verdicts:

    ❌ archived  ->  must be removed from the list on the next pass
    ⚠️ stale     ->  no push in >--since-days days, or manually flagged "watch"
    ✅ healthy   ->  actively maintained

Also writes .github/report.txt with machine-readable verdict lines so CI
(weekly-status.yml) can open an issue when a repo dies.

Usage:
    python3 scripts/check_tools.py [--out STATUS.md] [--since-days 365]

Uses the GITHUB_TOKEN / GH_TOKEN environment variable when present (higher
rate limit); otherwise falls back to the unauthenticated GitHub API.
"""
import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SINCE_DAYS = 365


def api_get(path: str, token: str | None) -> dict:
    headers = {
        "User-Agent": "ScrapeStack-status-check",
        "Accept": "application/vnd.github+json",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request("https://api.github.com" + path, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fetch_repo(repo: str, token: str | None, cache: dict) -> dict | None:
    try:
        data = api_get(f"/repos/{repo}", token)
        cache[repo] = {k: data.get(k) for k in ("pushed_at", "stargazers_count", "archived")}
        return data
    except urllib.error.HTTPError as e:
        if e.code == 403:
            print(f"!! rate limited for {repo} — falling back to cache", file=sys.stderr)
        else:
            print(f"!! HTTP {e.code} for {repo}", file=sys.stderr)
    except Exception as e:  # noqa: BLE001
        print(f"!! failed to fetch {repo}: {e}", file=sys.stderr)
    if repo in cache:
        return {
            "pushed_at": cache[repo].get("pushed_at"),
            "stargazers_count": cache[repo].get("stargazers_count"),
            "archived": cache[repo].get("archived"),
        }
    return None


def verdict_for(repo: dict | None, watch: bool, since_days: int) -> tuple[str, str]:
    if repo is None:
        return "n/a", "API unavailable"
    if repo.get("archived"):
        return "❌", "archived"
    pushed = repo.get("pushed_at", "")[:10]
    if pushed:
        last = dt.date.fromisoformat(pushed)
        age = (dt.date.today() - last).days
        if age > since_days:
            return "⚠️", f"no push in {age}d (since {pushed})"
    if watch:
        return "⚠️", "manually flagged — watch"
    return "✅", "healthy"


def render_table(tools: list[dict], token: str | None, since_days: int, report_lines: list[str], cache: dict) -> str:
    rows = []
    for t in tools:
        repo = fetch_repo(t["gh"], token, cache) if t.get("gh") else None
        if repo is not None:
            pushed = repo.get("pushed_at", "")[:10] or "—"
            stars = repo.get("stargazers_count", 0)
            archived = "yes" if repo.get("archived") else "no"
            link = f"[{t['gh']}](https://github.com/{t['gh']})"
        else:
            pushed = "—"
            stars = "—"
            archived = "—"
            link = t.get("home", "—")
            if t.get("home"):
                link = f"[official site]({t['home']})"
        if not t.get("gh"):
            verdict, note = "n/a", "official site — not a GitHub repo to check"
        else:
            verdict, note = verdict_for(repo, t.get("watch", False), since_days)
        report_lines.append(f"{verdict}\t{t['name']}\t{t.get('gh') or t.get('home', '')}\t{note}")
        rows.append(
            f"| {t['name']} | {link} | {pushed} | {stars} | {archived} | {verdict} |"
        )
    return "\n".join(rows)


def load_cache(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_cache(cache: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="STATUS.md")
    ap.add_argument("--since-days", type=int, default=DEFAULT_SINCE_DAYS)
    ap.add_argument("--cache", default=".github/api_cache.json",
                    help="JSON cache of GitHub repo metadata; seeded automatically on success "
                         "and used as fallback when rate-limited (survives the 60/hr limit).")
    args = ap.parse_args()

    data = json.loads((ROOT / "tools.json").read_text(encoding="utf-8"))
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    checked = dt.date.today().isoformat()

    cache = load_cache(ROOT / args.cache)
    report_lines: list[str] = []
    table = render_table(data["tools"], token, args.since_days, report_lines, cache)
    save_cache(cache, ROOT / args.cache)

    counts = {"✅": 0, "⚠️": 0, "❌": 0}
    for line in report_lines:
        verdict = line.split("\t", 1)[0]
        if verdict in counts:
            counts[verdict] += 1

    retired = data.get("retired", [])
    retired_block = ""
    if retired:
        lines = ["\n## Recently retired\n\nReasoning behind removals:\n"]
        for r in retired:
            lines.append(f"- **{r['slug']}** (`{r['repo']}`) — {r['reason']}")
        retired_block = "\n".join(lines) + "\n"

    md = f"""# ScrapeStack — Status Report

> Auto-generated by [scripts/check_tools.py](scripts/check_tools.py) · last checked **{checked}**
> Policy: **❌ archived** → removed on the next pass · **⚠️** no push in >{args.since_days}d or flagged watch
> Regenerate locally: `python3 scripts/check_tools.py`

## Verdicts

| Tool | Repo | Last push | ⭐ Stars | Archived | Verdict |
|---|---|---|---|---|---|
{table}

**{counts['✅']} healthy · {counts['⚠️']} watch · {counts['❌']} archived**
{retired_block}
---
_This list only grows with tools we would bet a scheduled job on. See [README.md](README.md)._
"""
    out = ROOT / args.out
    out.write_text(md, encoding="utf-8")

    report_dir = ROOT / ".github"
    report_dir.mkdir(exist_ok=True)
    (report_dir / "report.txt").write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(f"STATUS.md regenerated ({len(data['tools'])} tools, last checked {checked}).")
    print("Verdicts:", " ".join(f"{k}={v}" for k, v in counts.items()))
    for line in report_lines:
        verdict, name, repo, note = line.split("\t")
        print(f"  {verdict} {name:24s} {repo:40s} {note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())