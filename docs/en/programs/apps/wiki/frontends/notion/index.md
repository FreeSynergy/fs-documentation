# Notion

> Category: [wiki](../../index.md)

## What it is

Notion is a hosted all-in-one workspace for notes, documents and databases, built from typed blocks. For this project the relevant parts are:

- pages made of typed blocks [S9, S11]
- databases with properties and views [S13, S7]
- a REST API with OAuth and internal tokens [S3, S6]
- webhooks for change events [S4, S5]

## Version facts

| Item | Value | Source |
|------|-------|--------|
| Product | Notion web/desktop app, state as of 2026-11-07 | [S22] (no product version number exists) |
| API version (current) | `2026-03-11` | [S1], [S8] |
| Next API version | announced, not released; will make Notion-flavoured Markdown the default on Markdown endpoints. Name and date not given | [S8] (entry Oct 30) |

Notion does not number its app versions. Notion's product is updated continuously. The folder `2026-11-07/` is the snapshot date.

## Notable ideas

- Every line, list, table, image and embed is a block. Blocks nest. A page is a tree of blocks [S9, S18].
- A database is a set of data sources. Since API version `2025-09-03` each data source has its own schema, and a database can hold several data sources [S7].
- Views (table, list, board, calendar, gallery, chart) show the same data in different layouts [S13].
- Markdown-style typing creates blocks while the user types, for example `# ` for a heading [S11].
- The sidebar is a left navigation with tabs (Home, Library, Trash, Settings and others), plus the sections Private, Shared, Teamspaces and Favorites [S12].
- Deleted pages stay in Trash for 30 days by default [S14].

## Files in this set

| File | Content |
|------|---------|
| [2026-11-07/description.md](2026-11-07/description.md) | What it is, who it suits |
| [2026-11-07/features.md](2026-11-07/features.md) | What it can and cannot do |
| [2026-11-07/layout.md](2026-11-07/layout.md) | Sidebar, content area, page header |
| [2026-11-07/menus.md](2026-11-07/menus.md) | Sidebar items, page menu, block menu |
| [2026-11-07/shortcuts.md](2026-11-07/shortcuts.md) | Keyboard shortcuts |
| [2026-11-07/api.md](2026-11-07/api.md) | REST API, auth, rate limits, pagination |
| [2026-11-07/themes/index.md](2026-11-07/themes/index.md) | Appearance options |
| [2026-11-07/events.md](2026-11-07/events.md) | Webhooks |
| [2026-11-07/limits.md](2026-11-07/limits.md) | Known limits |
| [2026-11-07/dependencies.md](2026-11-07/dependencies.md) | What a frontend in this style needs from texts.capnp |
| [changelog.md](changelog.md) | Errors in the earlier pages |

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Required files present |
|---------|------------------------|
| [2026-11-07](2026-11-07/description.md) | 7/7 |
| [latest](latest/description.md) | 6/7 |

### 2026-11-07

| File | Contents |
|------|----------|
| [description.md](2026-11-07/description.md) | Detailed description, differentiation, who it suits |
| [features.md](2026-11-07/features.md) | What the program can do — and what not |
| [layout.md](2026-11-07/layout.md) | Window structure, regions, panels |
| [menus.md](2026-11-07/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](2026-11-07/shortcuts.md) | Keyboard shortcuts |
| [api.md](2026-11-07/api.md) | APIs and protocols, authentication, rate limits |
| [themes/index.md](2026-11-07/themes/index.md) | Themes: colours, typography, spacing — what can be rebuilt |
| [events.md](2026-11-07/events.md) | Events to the outside (webhooks, push, streams) |
| [limits.md](2026-11-07/limits.md) | Known limitations |
| [dependencies.md](2026-11-07/dependencies.md) | Which of our components a frontend in this style needs |

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

Fetched 2026-11-07. Each fact cites the page it came from. Facts from search snippets only are marked "snippet".

| ID | URL |
|----|-----|
| S1 | https://developers.notion.com/reference/versioning |
| S2 | https://developers.notion.com/reference/request-limits |
| S3 | https://developers.notion.com/guides/get-started/authorization |
| S4 | https://developers.notion.com/reference/webhooks |
| S5 | https://developers.notion.com/reference/webhooks-events-delivery |
| S6 | https://developers.notion.com/reference/intro |
| S7 | https://developers.notion.com/guides/get-started/upgrade-guide-2025-09-03 |
| S8 | https://developers.notion.com/page/changelog |
| S9 | https://developers.notion.com/reference/block |
| S10 | https://developers.notion.com/reference/post-search |
| S11 | https://www.notion.com/help/keyboard-shortcuts |
| S12 | https://www.notion.com/help/navigate-with-the-sidebar |
| S13 | https://www.notion.com/help/intro-to-databases |
| S14 | https://www.notion.com/help/duplicate-delete-and-restore-content |
| S15 | https://www.notion.com/help/customize-and-style-your-content |
| S16 | https://developers.notion.com/reference/capabilities |
| S17 | https://developers.notion.com/reference/query-a-data-source |
| S18 | https://developers.notion.com/reference/patch-block-children |
| S19 | https://developers.notion.com/reference/retrieve-a-page |
| S20 | https://developers.notion.com/reference/post-page |
| S21 | https://developers.notion.com/reference/trash-page |
| S22 | https://www.notion.com/product |
| S23 | https://www.notion.so/help/appearance-settings (snippet only, page not fetched) |

Pages that returned 404 and are not used as sources: `notion.com/help/intro-to-notion`, `notion.com/help/trash`, `notion.com/help/customize-your-appearance-in-notion`, `developers.notion.com/reference/search-limitations`, `developers.notion.com/reference/get-pages`. The sidebar article (S12) was found under `navigate-with-the-sidebar`.
