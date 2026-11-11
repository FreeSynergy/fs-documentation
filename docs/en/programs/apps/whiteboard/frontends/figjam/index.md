# FigJam

> Category: [whiteboard](../../index.md) · Type: online whiteboard (SaaS) · Vendor: Figma · Licence: proprietary

## What it is
FigJam is the whiteboard product of Figma. It is a browser-based board with sticky notes, shapes, connectors and sections, built for meetings and workshops. Several people work on one board at the same time.

## Notable ideas
- **Stamps and emotes** — quick, low-effort feedback placed on objects or released as short bursts; the board feels social without needing text. Relevant for a light-weight reaction capability.
- **Timer, voting and music in one facilitation panel** — a host starts a session, everyone can see it; votes stay hidden until the session ends. Shows how facilitation can be a few small session objects rather than a mode of the whole board.
- **Cursor chat** — a short message attached to one's own pointer, gone after a moment. An ephemeral presence event.

## Documented versions
| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ |

## Protocols and standards used
None open. REST API with access tokens and OAuth2 (see [api](latest/api.md)). Board model: see the gap noted in [data standards](../../../../data/standards.md).

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
| https://help.figma.com/hc/en-us/articles/1500004362321-Guide-to-FigJam | help page ✅ | 2026-11-10 |
| https://help.figma.com/hc/en-us/articles/4402269549591-Stay-on-track-with-the-timer-in-FigJam | help page ✅ (via search summary) | 2026-11-10 |
| https://help.figma.com/hc/en-us/articles/1500004290981 | help page, voting ⚠️ (via search summary only) | 2026-11-10 |
| https://developers.figma.com/docs/rest-api/ | official API docs ✅ | 2026-11-10 |
