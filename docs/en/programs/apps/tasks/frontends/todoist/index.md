# Todoist

> Category: [tasks](../../index.md) · Type: personal and team task manager (web, apps) · Vendor: Doist · Licence: proprietary

## What it is
Todoist is a cross-platform task manager with projects, sections, labels, priorities and natural-language dates.

## Notable ideas
Why this program is documented here (ADR 0013). Function analysis only, own wording.

- Filter language: a small query syntax over tasks with AND, OR, NOT, grouping, wildcards and multi-list output — a model for a saved-query language in our Tasks program.
- Filters are saved and listed in the sidebar like projects.

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
| https://www.todoist.com/help/articles/introduction-to-filters-V98wIH | official help, filters | ✅ 2026-11-10 |
