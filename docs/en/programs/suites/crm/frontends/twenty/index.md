# Twenty

> Category: [crm](../../index.md) · Type: open-source CRM · Vendor: Twenty (twentyhq) · Licence: open core, AGPL-3.0 for most code ⚠️ (a separate commercial licence for files marked Enterprise, from a third-party listing)

## What it is
Twenty is an open-source CRM built as an alternative to the large commercial ones. It has people, companies and opportunities, customisable views and workflows, and is extensible as code. It runs as a cloud service or self-hosted with Docker Compose.

## Notable ideas
- **Own objects as first-class** — custom objects and fields are declared in code with an SDK, versionable and reviewable; custom objects get the same tables and permissions as built-in ones (ADR 0013). Relevant for our CRM as a suite over people (see [requirements](../../requirements.md)).
- **Views as the working surface** — table, kanban and calendar views, each with filters, sorting and grouping.
- **Webhooks and both REST and GraphQL** for the same records.

## Documented versions
| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ✅ |

## Protocols and standards used
REST, GraphQL, webhooks. See [data standards](../../../../data/standards.md).

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
| https://github.com/twentyhq/twenty | source README ✅ | 2026-11-10 |
| https://docs.twenty.com/developers/introduction | official docs ✅ | 2026-11-10 |
| https://docs.twenty.com/getting-started/key-features | official docs ⚠️ (via search only) | 2026-11-10 |
