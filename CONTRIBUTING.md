# Contributing to ScrapeStack

Thanks for helping keep this list honest. ScrapeStack's only promise:

> Every tool here is **actively maintained** — and we verify it, weekly, with
> an automated [status check](STATUS.md).

## The three rules

1. **It must be alive.** A release or commit in the last few months — not a
   graveyard. If the repo is archived, the PR will be closed.
2. **One honest line of description + one killer feature.** What it does, no
   marketing fluff.
3. **Add it everywhere, in one PR:** the table in `README.md`, the matching
   row in `README_zh.md`, **and** an entry in `tools.json` so the automated
   check can start watching it.

## Checklist for a new tool

- [ ] `tools.json`: `gh` is the exact `owner/repo` (or `home` for non-GitHub
      projects), `category` matches one of the README sections, `install` is a
      copy-pasteable command, `watch` is `false` unless it is already slowing
      down.
- [ ] Both READMEs stay in sync — English and 简体中文.
- [ ] The tool is genuinely useful to indie devs / solo builders / growth
      engineers, not just popular.
- [ ] Run `python3 scripts/check_tools.py --out STATUS.md` and make sure the
      new entry shows up healthy.

## Removing or demoting a tool

- **Archived** → open a PR that removes it from both READMEs and `tools.json`,
  and adds it to the `retired` list in `tools.json` with a one-line reason.
- **Stale (no push in 365+ days)** → set `watch: true` in `tools.json`; the
  weekly check will flag it in STATUS.md and it stays visible until it recovers
  or gets retired.

## Etiquette

- One tool per PR keeps review fast.
- No affiliate links in tool entries. The sponsored spot is reserved for the
  single, clearly-labelled sponsor slot in the README.
- Please don't add tools whose purpose is illegal scraping; we promote
  responsible use (respect `robots.txt` and each site's ToS).