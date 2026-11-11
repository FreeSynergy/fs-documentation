# ActivityWatch

> Category: [history](../../index.md) · Type: automatic activity tracker · Vendor: ActivityWatch project · Licence: free and open source (licence text: Open)

## What it is
ActivityWatch records what you do on your computer: which program and window is in front, whether you are at the keyboard, which browser tab is open. Everything is stored locally and shown in a web interface.

## Notable ideas
- Watchers feed "buckets" of events through one local interface. Why: a clean place to import events from other sources.
- Raw data at high resolution, summaries made on demand by queries. Why: the same idea as our digest over raw activity.
- Data stays on your machine by default; no feature gates. Why: same stance as History.
- Categorisation rules (including regular expressions). Why: meaning is added later, not at capture.

## Documented versions
| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 (release v0.14.1, 2026-10-10) | ✅ |

## Protocols and standards used
HTTP/JSON, RFC 3339 timestamps.

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
| https://docs.activitywatch.net/en/latest/introduction.html ✅ | official docs | 2026-11-10 |
| https://docs.activitywatch.net/en/latest/api/rest.html ✅ | official docs | 2026-11-10 |
| https://docs.activitywatch.net/en/latest/watchers.html ✅ | official docs | 2026-11-10 |
| https://docs.activitywatch.net/en/latest/features.html ✅ | official docs | 2026-11-10 |
| https://github.com/ActivityWatch/activitywatch/releases ✅ | release list | 2026-11-10 |
