# Changelog

## 2026-11-07: rewritten from official sources

The earlier pages were written from memory; these statements were wrong.

Checked against the official sources in [index.md](index.md) (fetched 2026-11-07). Status: **wrong** (official source contradicts), **unverified** (no source found; removed or to be checked), **outdated** (was true, no longer current).

### index.md

| Statement | Status | Correct fact | Source |
|-----------|--------|--------------|--------|
| "Notion is an all-in-one platform for notes, documentation and collaboration." | outdated | Notion calls itself an AI workspace for teams and their agents, with capture, find and automate | [S22] |
| "Notable ideas" section empty | gap | Filled in the new index | — |
| Documented versions: `latest` | gap | API version 2026-03-11; app has no version number | [S1], [S8] |

### latest/description.md

| Statement | Status | Correct fact | Source |
|-----------|--------|--------------|--------|
| Backend Node.js, PostgreSQL; frontend React, TypeScript | unverified | not stated in official docs | — |
| Hosting SaaS only | partly | Hosted service; no self-hosting option found on official pages | — |
| Advantages: 100+ embeds, strong mobile apps | unverified | embed types exist [S9], counts and mobile claims not verified | — |
| Comparisons with Tango.io, Confluence, XWiki | unverified | not in official sources; removed | — |
| Authentication: OAuth2, SSO | partly | OAuth 2.0 for public integrations is verified; SSO not | [S3] |
| "Who it suits" list | unverified | opinion; not in official sources | — |

### latest/features.md

| Statement | Status | Correct fact | Source |
|-----------|--------|--------------|--------|
| "No Markdown syntax in the editor" | wrong | Markdown prefixes and inline markdown work while typing | [S11] |
| Heading shortcut `##` etc. | verified | | [S11] |
| Callout types info, warning, success | unverified | Callouts exist as block type; type list not verified | [S9] |
| Code block with 40+ languages, list of languages | unverified | not in official sources read | — |
| LaTeX `$...$` | unverified | `/equation`, `/math`, `/latex` slash commands exist | [S11] |
| Mermaid diagrams | unverified | not in official sources read | — |
| Table, formula, rollup, relations | partly | Relation, rollup, formula, status, multi-select exist as API property types | [S8] |
| Formula examples (`concat`, `dateBetween`, `if`, `format`, `dateAdd`) | unverified | `prop()` reference verified | [S8] |
| Database views: table, kanban, calendar, list, gallery | wrong | Views are table, list, board, calendar, gallery, chart | [S13] |
| Database column types list | partly | Status, multi-select, relation, rollup, formula confirmed; others unverified | [S8] |
| Templates examples | unverified | templates exist; examples not verified | [S12] |
| Auto-save | unverified | no official statement read | — |

### latest/layout.md

| Statement | Status | Correct fact | Source |
|-----------|--------|--------------|--------|
| Sidebar items Home, Pages, Database, Templates, Members, Dashboard, Settings | wrong | Home, Chats with Notion AI, Meetings, Inbox, Library, Templates, Trash, Settings; sections Private, Shared, Teamspaces; Favorites | [S12] |
| Sidebar width, logo ~40px, element sizes | unverified | not in official sources | — |
| Right sidebar with versions, author | unverified | no official source read | — |
| Breadcrumbs | unverified | | — |
| Status bar with word and character count | unverified | | — |
| Mobile hamburger menu | unverified | | — |
| Design principles (minimalism, etc.) | unverified | marketing statements; not used | — |
| Accessibility claims (ARIA, contrast) | unverified | | — |
| Performance claims (lazy loading, debounce) | unverified | | — |

### latest/menus.md

| Statement | Status | Correct fact | Source |
|-----------|--------|--------------|--------|
| 13 main menu items (Workspace, Pages, Databases, Trash, Media, Users, Settings, Notifications, Search, Templates, Integrations, Resources, Preferences) | wrong or unverified | The sidebar tabs and items are listed in menus.md; the other items are not verified | [S12] |
| Context menus (page, database, block, user) | partly | Block menu: `/turn`, `/color`, block handle ⋮⋮ are verified; others unverified | [S11, S14] |
| Command palette `Ctrl+Shift+P` | unverified | not on official shortcut page | [S11] |
| Quick search `Ctrl+P` | partly | cmd/ctrl+P opens search or jumps to recent page | [S11] |
| Global search `Ctrl+Shift+F` | wrong | Search is cmd/ctrl+K (sidebar article) | [S12] |
| Block menu `/` | partly | `/` opens slash commands | [S11] |

### latest/shortcuts.md

| Statement | Status | Correct fact | Source |
|-----------|--------|--------------|--------|
| Ctrl+Shift+X strikethrough | wrong | cmd/ctrl+shift+S | [S11] |
| Ctrl+E align centre, Ctrl+L align left, Ctrl+R align right, Ctrl+Shift+E justify | unverified | not on official page. Ctrl+E is inline code | [S11] |
| Ctrl+Shift+K code tag | wrong | cmd/ctrl+E inline code | [S11] |
| Ctrl+Shift+C code block | wrong | cmd/ctrl+option/shift+8 | [S11] |
| Ctrl+Shift+M quote | wrong | Quote is `"` + space. cmd/ctrl+shift+M creates a comment | [S11] |
| Ctrl+Shift+A task | unverified | To-do via `[]` + space and cmd/ctrl+option/shift+4 | [S11] |
| Ctrl+Enter preview / publish | wrong | cmd/ctrl+Enter acts on current block (open page, tick to-do, toggle, full-screen) | [S11] |
| Ctrl+Shift+Backspace delete block | wrong | backspace or delete on selected blocks | [S11] |
| Ctrl+D duplicate block | partly | cmd/ctrl+D duplicates selected blocks | [S11] |
| Ctrl+Shift+D duplicate page | wrong | cmd/ctrl+D is blocks; page duplicate not documented | [S11] |
| Ctrl+↑/↓ move block | wrong | cmd/ctrl+shift+arrow moves selected block | [S11] |
| Ctrl+Shift+↑/↓ copy block | wrong | Move, not copy | [S11] |
| Ctrl+B show or hide sidebar | wrong | cmd/ctrl+B is bold; sidebar is cmd/ctrl+\ | [S11, S12] |
| Ctrl+Shift+L insert link | wrong | cmd/ctrl+K add link; cmd/ctrl+shift+L toggles dark mode | [S11] |
| Ctrl+Shift+F share page | unverified | not on official page | — |
| Ctrl+Shift+E export page | unverified | not on official page | — |
| Ctrl+S save | unverified | not documented | — |
| Ctrl+W close page, Ctrl+N new page | partly | cmd/ctrl+N new page (desktop); close not documented | [S11] |
| Ctrl+Shift+N subpage | unverified | | — |
| Ctrl+Shift+A app manager | unverified | | — |
| Ctrl+Shift+I developer tools, F11 full screen | unverified | | — |
| Ctrl+G, Ctrl+H find next, replace | unverified | | — |
| Ctrl+Tab next tab | unverified | cmd/ctrl+T new tab; tab switching not documented | [S11] |
| Ctrl+Y redo, Ctrl+Z undo | unverified | | — |
| Slash `/bullist`, `/numlist` | wrong | `/bullet`, `/num` | [S11] |
| Slash `/callout`, `/table`, `/md`, `/js`, `/python` and other language slashes | unverified | not on official page | [S11] |
| `/h1` + Enter etc. | verified | `/h1`, `/h2`, `/h3`, `/todo`, `/toggle`, `/quote`, `/code`, `/embed` | [S11] |
| Ctrl+K add link | verified | | [S11] |
| Esc, Tab, Shift+Tab, Enter | verified | | [S11] |
| Ctrl+Left/Right word navigation | unverified | | — |
| Mac shortcuts with cmd | partly | Official uses cmd/ctrl for both platforms | [S11] |

### latest/api.md

| Statement | Status | Correct fact | Source |
|-----------|--------|--------------|--------|
| `Notion-Version: 2022-06-28` | outdated | `2026-03-11` | [S1], [S8] |
| `GET /v1/pages` lists pages with a filter | unverified (not found) | No list-all pages endpoint found on the reference. Use `POST /v1/search` | [S10] |
| `DELETE /v1/pages/:id` deletes a page | wrong | Trash with `PATCH /v1/pages/{id}` and `in_trash: true` | [S21] |
| `POST /v1/pages` with `page_id` and `properties.title` | partly | Parent types: `page_id`, `database_id`, `data_source_id`, `workspace`. Max 100 children | [S20] |
| `GET /v1/blocks/:id/children` | verified | | [S19] |
| `POST /v1/blocks/:id/children` adds children | wrong | `PATCH /v1/blocks/{block_id}/children` | [S18] |
| `PATCH /v1/blocks/:id` updates, `DELETE /v1/blocks/:id` deletes | unverified | | — |
| `GET /v1/databases/:id` | partly | Returns child data sources; schema via `GET /v1/data_sources/{id}` | [S7] |
| `POST /v1/databases` | partly | Creates a database with `initial_data_source` | [S7] |
| `PATCH /v1/databases/:id` | partly | Only database-level fields; schema is on data sources | [S7] |
| `POST /v1/databases/:id/query` | outdated | `POST /v1/data_sources/{data_source_id}/query` (the upgrade guide summary says PATCH; the reference page says POST) | [S17], [S7] |
| `GET /v1/users`, `/v1/users/:id`, `/v1/users/me` | partly | Users endpoints exist with capability conditions; `/users/me` path not verified | [S16] |
| `POST /v1/search` | verified | Filter value `database` is now `data_source` | [S10], [S7] |
| `POST /v1/comments` | unverified path | Comment endpoints exist; path not verified | [S16], [S8] |
| Rate limits 3/s per integration, 1/s for database queries | wrong | 180 requests per minute (about 3/s) per connection; 600/min Business and Enterprise; data source queries about 3/s | [S2] |
| Rate-limit error | verified | 429, `rate_limited`, `Retry-After` in seconds | [S2] |
| `Notion-Request-Id` header | unverified | | — |
| Webhook setup with `POST /v1/webhooks` | wrong | Created in the integration's Webhooks tab | [S4] |
| Webhook events `page.created`, `page.updated`, `page.deleted`, `page.restored` | wrong | Real names: `page.created`, `page.content_updated`, `page.properties_updated`, `page.deleted`, `page.undeleted`, etc. | [S5] |
| SDK `@notion/client` | wrong | `@notionhq/client` | [S7] |
| SDK `notion-client` (Python) | unverified | not on the pages read | — |
| Community SDKs (Go, Java, Ruby, PHP) | unverified | not on official pages | — |
| Example `requests.post(...)` code | outdated | Uses old version and endpoints | [S1], [S17] |
| Auth via OAuth2 | verified | authorize and token endpoints as described | [S3] |
| Headers `Authorization: Bearer`, `Notion-Version` | verified | | [S6] |

### latest/features.md, layout.md, menus.md: cross-check summary

- The earlier pages described a product with a "Dashboard", "Members" and "Pages" sidebar, which does not match the official sidebar. Replaced.
- The earlier pages repeated the same generic comparison table. Removed.

### themes (new file, no earlier version)

The earlier pages had no themes file. The `index.md` requirement for `themes/index.md` is met in the new file set.
