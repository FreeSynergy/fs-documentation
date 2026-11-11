# YouTube Studio

> Category: [streaming](../../index.md) · Type: creator back office with live control room (SaaS) · Vendor: Google (YouTube) · Licence: proprietary

## What it is
YouTube Studio is the management area for channel owners on YouTube. For live broadcasts it contains the Live Control Room, a dashboard that shows the stream's health and real-time numbers while the broadcast runs, and an analytics area for the numbers afterwards.

## Notable ideas
- **Live control room** — stream health and audience numbers on one screen while live; a model for the operator view of our streaming program (ADR 0013).
- **Real-time versus processed analytics** — live figures (concurrent and peak viewers) are shown at once; the final figures arrive later and may differ because they are processed. Relevant for how we label numbers as preliminary.

## Documented versions
| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ |

## Protocols and standards used
Ingest by RTMP(S) or other encoder protocols: Open (not verified here). See [streaming requirements](../../requirements.md).

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Required files present |
|---------|------------------------|
| [latest](latest/description.md) | 6/7 |

### latest

| File | Contents |
|------|----------|
| [description.md](latest/description.md) | Detailed description, differentiation, who it suits |
| [features.md](latest/features.md) | What the program can do — and what not |
| [layout.md](latest/layout.md) | Window structure, regions, panels |
| [menus.md](latest/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](latest/shortcuts.md) | Keyboard shortcuts |
| [api.md](latest/api.md) | APIs and protocols, authentication, rate limits |

⚠️ Missing required files: `themes/index.md`
<!-- /gen:versions -->

## Sources
| Source | Kind | Retrieved |
|--------|------|-----------|
| https://support.google.com/youtube/answer/2853833 | official help page ✅ (via search summary) | 2026-11-10 |
| https://studio.youtube.com | sign-in required, not readable ⚠️ | 2026-11-10 |
