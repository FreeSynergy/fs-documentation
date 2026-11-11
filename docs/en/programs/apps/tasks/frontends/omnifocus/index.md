# OmniFocus

> Category: [tasks](../../index.md) · Type: personal task manager / GTD (Apple platforms) · Vendor: The Omni Group · Licence: proprietary

## What it is
OmniFocus is a task manager for Mac, iPhone, iPad, Apple Watch and Vision Pro, plus OmniFocus for the Web, aimed at long-term projects and the weekly review.

## Notable ideas
Why this program is documented here (ADR 0013). Function analysis only, own wording.

- Perspectives: saved views over all tasks (standard ones plus custom ones in Pro) defined by filters, grouping and sorting — maps to our idea of saved queries over the task owner's data.
- Review: projects get a review interval and are marked reviewed; a dedicated perspective lists what is due for review.
- Availability model: sequential, parallel and single-action projects decide which actions are available; On Hold and Dropped states hide items.

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

⚠️ Missing required files: `themes/index.md`
<!-- /gen:versions -->

## Sources
| Source | Kind | Retrieved |
|--------|------|-----------|
| https://www.omnigroup.com/omnifocus/ | official product page | ✅ 2026-11-10 |
| https://support.omnigroup.com/documentation/omnifocus/universal/4.7.1/en/welcome/ | official reference manual | ✅ 2026-11-10 |
| https://support.omnigroup.com/documentation/omnifocus/mac/4.0.3/en/perspectives | official manual, Perspectives (read partly, 100000 of 137815 characters) | ⚠️ 2026-11-10 |
