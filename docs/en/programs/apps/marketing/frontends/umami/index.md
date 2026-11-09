# Umami

> Category: [marketing](../../index.md) · Type: web and product analytics · Vendor: Umami Software · Licence: MIT

## What it is
Umami is a privacy-focused web analytics tool. A tracking script sends page views and custom events to Umami, which shows traffic, campaigns, behaviour and conversions. It runs self-hosted (Next.js, PostgreSQL) or as a cloud service.

## Notable ideas
- **Product-analytics views on a light tool** — events, funnels, retention, journeys, goals and UTM tracking, without cookies or cross-site tracking (ADR 0013).
- **Teams** — groups share websites and reports.
- **MCP endpoint (optional, off by default)** — programmatic access for tools with API keys.

## Documented versions
| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ✅ |

## Protocols and standards used
HTTP/JSON API; no data standard for events found. See [data standards](../../../../data/standards.md).

## Sources
| Source | Kind | Retrieved |
|--------|------|-----------|
| https://docs.umami.is/docs/ | official docs ✅ | 2026-11-10 |
| https://github.com/umami-software/umami | source README ✅ | 2026-11-10 |
