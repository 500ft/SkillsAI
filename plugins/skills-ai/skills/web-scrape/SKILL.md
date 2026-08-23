---
name: web-scrape
description: Extract structured data from websites — pick the right fetch tier (Firecrawl or scraping MCP if connected, harness web-fetch tools, browser automation for JS-rendered pages, curl/Python as fallback), handle pagination, parse into clean typed records, and save as JSON/CSV. Use this skill whenever the user wants data pulled from web pages — "scrape this site", "get all the listings/products/papers from", "pull the table from this page", "collect prices/jobs/posts from", "turn this website into a dataset" — even for a single page, if the goal is structured data rather than just reading.
---

# Web Scrape — Structured Extraction From Websites

Turn web pages into clean, structured datasets. The two failure modes of agent scraping are using the wrong fetch tier (fighting JS-rendered pages with curl) and re-fetching the world on every iteration (slow, rude, and ban-prone). This skill fixes both: pick the tier deliberately, fetch once, iterate on the cached copy.

## Step 1 — Recon, then pick the fetch tier

Fetch one representative page and look at what came back before writing any extraction logic:

1. **Scraping MCP** (Firecrawl or similar, if connected) — purpose-built: clean markdown, crawling, JS rendering handled. Use it when available.
2. **Harness fetch tools** (WebFetch or equivalent) — fine for static/server-rendered pages and most docs/article/listing sites.
3. **Browser automation MCP** (Chrome tools / preview tools, if connected) — for pages that arrive as an empty `<div id="root">`: client-rendered apps, infinite scroll, content behind interactions.
4. **`curl` / Python (`requests` + `BeautifulSoup`)** — last-resort fallback, and the right tool for bulk-fetching a known list of static URLs.

**Check for an API first.** Many "scrape this site" tasks are actually "this site has a JSON API the frontend calls" — look at network requests or common paths (`/api/`, `.json`, RSS/sitemap). Ten minutes finding the API beats two hours of brittle HTML parsing, and the data arrives already structured.

## Step 2 — Extract into typed records

- Define the record schema first (fields + types), from looking at 2-3 real pages — including the optional fields ("price missing on sold items").
- Parse with real selectors (CSS/XPath) against the cached HTML, not regex-over-HTML. Validate every record against the schema; log-and-skip malformed ones rather than silently emitting half-records, and report the skip count.
- Normalize at parse time: trim whitespace, parse numbers/dates to real types, resolve relative URLs to absolute, decode entities.

## Step 3 — Scale carefully

- **Cache everything**: save raw responses to a local dir keyed by URL before parsing. Iterating on extraction logic must hit the cache, not the site. (This is the single biggest time-saver in the whole job.)
- **Pagination**: find the real mechanism (page param, cursor, next-link, API offset) on page 1-2 before looping; cap the crawl with an explicit limit and report when the cap was hit.
- **Rate-limit**: ~1 request/second default, exponential backoff on 429/5xx, stop and report if errors persist. Hammering gets you blocked and gets the data center IP blocked for everyone.
- **Save incrementally** (append JSONL as you go) so a crash at page 80 of 100 doesn't lose everything; dedupe by a natural key at the end.

## Boundaries

Scrape only content you can lawfully access: respect robots.txt for bulk crawling, don't automate around logins, paywalls, or anti-bot measures, and check ToS when the job is large or commercial — flag concerns to the user rather than silently proceeding. Personal data gets extra care: don't compile it beyond what the task genuinely needs.

## Output

Deliver the dataset (JSON/JSONL/CSV — ask if unclear, default JSONL for >1k records) plus a 5-line summary: records collected, pages fetched, skip/error counts, schema, and where the raw cache lives so the extraction can be re-run without re-fetching.
