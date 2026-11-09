# Notion Calendar

> Category: [calendar](../../index.md) · [frontends](../index.md)

## What it is

Notion Calendar (formerly Cron) is a calendar client by Notion for desktop and web. It connects to existing calendar accounts. ✅ Platform list beyond desktop and web: Open.

## Notable ideas

- **Time zones as a first-class feature:** several zones side by side, each with a label, and a "travel" mode that makes another zone the primary one for a while ✅. Why here: people in groups work across zones (ADR 0013).
- **Sharing free time:** a scheduling link, one-off or recurring, with booking window, expiry and location; the invitee picks a slot and the meeting appears in the calendar ✅.

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

- https://www.notion.com/help/availability-blocking-and-time-zones ✅ 2026-11-10
- https://www.notion.com/help/notion-calendar ❌ (404) 2026-11-10
