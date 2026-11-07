# Notion — features (2026-11-07)

## Can do (verified)

| Area | Feature | Source |
|------|---------|--------|
| Blocks | Typed blocks: paragraph, heading 1–4, bulleted and numbered list item, to-do, toggle, quote, callout, code, table, table row, image, video, audio, file, pdf, embed, bookmark, equation, divider, column list, column, table of contents, synced block, child page, child database, link preview | [S9] (block type enum; `code`, `tab`, `audio`, `meeting_notes` are in the reference but missing in the enum list) |
| Editing | Markdown prefixes create blocks while typing (`# `, `- `, `[] `, `1. `, `> `, `" `, `---`) | [S11] |
| Editing | Nest and un-nest with Tab and Shift+Tab; select, move, duplicate and delete blocks with keyboard | [S11] |
| Editing | Slash commands, for example `/h1`, `/todo`, `/toggle`, `/quote`, `/code`, `/embed`, `/image`, `/pdf`, `/video`, `/audio`, `/file`, `/equation`, `/toc`, `/template`, `/turn`, `/color` | [S11] |
| Text | Bold, italic, underline, strikethrough, inline code, link, text colour and highlight (`/color`) | [S11] |
| Mentions | `@` mentions a person, links a page inline, inserts a date, adds a reminder | [S11] |
| Links | `[[` or `+` links to a page or creates a sub-page | [S11] |
| Tables | Fill cells right or down; table rows are blocks | [S11, S9] |
| Pages | Sub-pages, favourites, drag to reorder and nest pages | [S12] |
| Pages | Font (Default, Serif, Mono), small text, full width, table of contents, icon, cover | [S15] |
| Pages | Move, duplicate, trash, restore | [S14, S21] |
| Pages | Comments on pages (create with cmd/ctrl+shift+M) | [S11, S16] |
| Databases | Views: table, list, board, calendar, gallery, chart | [S13] |
| Databases | Views can be locked; locking stops changes to properties and views | [S13] |
| Databases | Property types include status, multi-select, relation, rollup, formula (names found in API changelog) | [S8] |
| Databases | Formulas use `prop("Name")` references | [S8] (Aug 12 entry) |
| Search | Search pages and data sources (API `POST /v1/search`) | [S10] |
| Search | In the app: cmd/ctrl+K or cmd/ctrl+P opens search or jumps to a recent page | [S11, S12] |
| Export | Pages can be exported and the API serves Markdown (Notion-flavoured Markdown endpoints) | [S8] (Feb 26, Mar 2 and Jun 29 entries). App export menu not verified |
| API | Create, read, update and trash pages; read and update blocks; append children (max 100 per request) | [S19, S20, S21, S18] |
| API | Query data sources with filters and sorts | [S17] |
| API | Webhook events for pages, databases, data sources and comments | [S5] |

## Cannot do (verified) or not supported by the API

| Limit | Source |
|------|--------|
| Small text and full width are desktop and web only | [S15] |
| The API cannot set a `block_id` as the parent of a new page; parents are `page_id`, `database_id`, `data_source_id` or `workspace` | [S20] |
| A trashed page cannot be edited until restored | [S14] |
| Restoring a database restores its pages and properties, but not the text inside those pages | [S14] |
| Views and filters: a user with "Can edit content" cannot change filters or sorts | [S13] |
| The API cannot read the full page content in the page-retrieve call; use block children | [S19] |
| Webhook payloads carry ids and metadata, not full content | [S5] |
| Search covers pages and data sources only; `database` is no longer a valid filter value | [S10, S7] |

## Not verified (removed or marked)

- "No Markdown syntax in the editor" (earlier page). Wrong; Markdown input exists [S11].
- Callout types (info, warning, success); callouts exist [S11] but the type list is unverified.
- Code block language list (40+ names). Language list not on any official page read: unverified.
- Mermaid diagrams. Unverified.
- Embed counts (100+ services). Unverified.
- Template system details and example templates. Templates exist [S12]; details unverified.
- Mobile apps and their features. Unverified.
- Auto-save. Unverified (no official statement read).
- SSO, formula function list (`concat`, `dateBetween`, `if`, etc.). Unverified.
