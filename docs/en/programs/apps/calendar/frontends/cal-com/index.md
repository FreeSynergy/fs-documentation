# Cal.com

> Category: [calendar](../../index.md) · [frontends](../index.md)

## What it is

Cal.com is a scheduling product: the owner defines event types and availability, and others book a slot on a public page. It has a hosted service and a REST API (v2). ✅ Licence of the current code base: Open (see below).

## Notable ideas

- **Booking pages:** a public page per event type; availability, buffers, minimum notice and slot intervals are set per event type ⚠️ (search snippet of the help index).
- **API with scoped access:** schedules, event types and bookings are API resources; OAuth and API keys ✅. Why here: this is the reference for our Booking part of the calendar (ADR 0013).

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

- https://cal.com/docs ✅ 2026-11-10 (API v2 introduction)
- https://github.com/calcom/cal.com ✅ 2026-11-10 (fetch returned the page of the fork Cal.diy: MIT, enterprise code removed; that the main repository changed licence is NOT confirmed)
- Third-party blogs on licence and self-hosting ⚠️ not used for claims
