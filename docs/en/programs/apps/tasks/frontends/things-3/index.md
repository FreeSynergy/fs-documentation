# Things 3

> Category: [tasks](../../index.md) · Type: personal task manager (Apple platforms) · Vendor: Cultured Code · Licence: proprietary

## What it is
Things 3 is a personal to-do app for Mac, iPhone, iPad, Apple Watch and Vision Pro, built around a small set of fixed lists and a calm, fast capture flow.

## Notable ideas
Why this program is documented here (ADR 0013). Function analysis only, own wording.

- Fixed day-oriented lists: Today (with calendar events on top), This Evening (later the same day), Anytime and Someday (parked). The user decides when, not which list type — worth copying for our Tasks view of a day.
- Quick Entry: add a to-do from any list or from outside the app without opening the full window; the destination can be changed afterwards.
- Quick Find / type-to-jump to a project, to-do or tag.

## Documented versions
| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ partly verified, gaps marked "Open" |

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
| [dialogs.md](latest/dialogs.md) | Every dialog: purpose, fields, buttons, default, cancel |
| [workflows.md](latest/workflows.md) | Step-by-step workflows: goal, prerequisites, steps, failures, undo |
| [acceptance.md](latest/acceptance.md) | Acceptance checklist: each workflow as a yes/no click test |
| [gaps.md](latest/gaps.md) | What our program cannot do for these workflows, and what it needs |

⚠️ Missing required files: `themes/index.md`
<!-- /gen:versions -->

## Sources
| Source | Kind | Retrieved |
|--------|------|-----------|
| https://culturedcode.com/things/features/ | official features page | ✅ 2026-11-10 |
| https://culturedcode.com/things/support/articles/2803573/ | official URL-scheme reference | ✅ 2026-11-10 |
| https://culturedcode.com/things/support/articles/2803582/ | official support article (Gestures, Magic Plus) | ⚠️ brief 2026-11-10, 2026-11-14 |
| https://culturedcode.com/things/support/articles/2785159/ | official keyboard shortcuts (Mac) | ✅ 2026-11-14 |
| https://culturedcode.com/things/support/articles/2249437/ | official Quick Entry | ✅ 2026-11-14 |
| https://culturedcode.com/things/support/articles/2803564/ , 2803579, 2803581, 2803583, 2803584, 2803590, 2803555, 2803577, 2803580, 9651894, 3238254, 4001304, 6037627 (all under /things/support/articles/) | official support articles (repeat, when/deadline, tags, calendar, Quick Find, cloud, import, headings, windows, move, sidebar, lists, areas) | ✅ 2026-11-14 |
| https://culturedcode.com/things/guide/ | official handbook, intro only | ✅ 2026-11-14 |
