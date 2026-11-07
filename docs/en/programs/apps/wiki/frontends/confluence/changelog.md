# Changelog

## 2026-11-07: rewritten from official sources

The earlier pages were written from memory; these statements were wrong.

Source of the earlier pages: `fs-documentation/docs/en/programs/apps/wiki/frontends/confluence/` (index.md and latest/*.md). Each row gives the earlier statement, the verdict, the correct fact, and the source (S-numbers from [index.md](index.md)).

Verdict: **WRONG** = contradicted by a source. **UNVERIFIED** = no source found; removed or marked in the new files.

### api.md

| Earlier statement | Verdict | Correct fact | Source |
|-------------------|---------|--------------|--------|
| Base `https://confluence.example.com/rest/api` | WRONG | Cloud paths are `https://<site>.atlassian.net/wiki/api/v2` (v2) and `/wiki/rest/api` (v1) | S1, S2, S4 |
| Auth methods: basic, OAuth2, JWT, cookie | PARTLY WRONG | Basic auth (email + API token) for direct calls; OAuth 2.0 (3LO) for apps; JWT for Cloud apps. Cookie auth: unverified. | S1, S6, S7 |
| `Authorization: Basic base64(email:api-token)` | WRONG (literal text) | Real Base64 of `email:api_token`. The example is a placeholder, not a valid header. | S7 |
| API tokens created at `atlassian.com` | UNVERIFIED | Location not stated in S7 | S7 |
| Endpoints `/rest/api/content`, `/child/page`, `/history`, `/child/attachment`, `/child/macro`, `/child/comment` | UNVERIFIED (mostly) | v1 `content/{id}` path with `/wiki` prefix verified (S2). Other v1 sub-paths not confirmed. v2 list in S3. | S2, S3 |
| `GET /rest/api/user`, `GET /rest/api/user/view` | UNVERIFIED | Not confirmed; v2 has a User group (S1) | S1 |
| `GET /rest/api/search` with `cql` | UNVERIFIED | Not confirmed in pages read | - |
| Create page with `space.key` and `body.storage` (v1 example) | UNVERIFIED | `storage` is a valid body representation value in the v2 schema; v1 request shape not confirmed | S4 |
| Python and JS examples with `requests`, `axios`, `atlassian-python-api` | UNVERIFIED | Examples use placeholder hostnames; library names not confirmed as official | - |
| Rate limits: 200 requests per 5 minutes per user | WRONG | Points-based: 65,000 points per hour (global pool), points per object type | S5 |
| Rate limits: 100 requests per second | WRONG | Not in S5; burst limits are separate and undocumented in numbers | S5 |
| Headers `X-AUTH-_RATE-LIMIT-REMAINING`, `X-AUTH-_RATE-LIMIT-RESET` | WRONG | `X-RateLimit-Remaining`, `X-RateLimit-Reset`, `RateLimit-Reason`, `Retry-After` | S5 |
| Webhooks `page.created`, `page.updated`, `page.deleted`, `comment.created`, `space.created` | WRONG | Forge events `avi:confluence:created:page`, etc. Legacy Connect event names `page_created`, `page_updated`, etc. | S10, S11 |
| Webhook config `POST /rest/webhooks/1.0/webhook` | UNVERIFIED for Cloud | Connect webhooks are declared in the descriptor `modules.webhooks` (S11). Forge event subscription is in the Forge app, mechanism not read. | S10, S11 |
| SDK list (`@atlassian/confluence-api` "official", `atlassian-java-client`, etc.) | UNVERIFIED | Not confirmed; removed | - |
| `See also` link `structure.md` | WRONG link | File is `layout.md` | - |
| `Authorization` for OAuth with `refresh` not described | MISSING | Rotating refresh tokens; 90-day inactivity; `offline_access` scope | S6 |

### description.md

| Earlier statement | Verdict | Correct fact | Source |
|-------------------|---------|--------------|--------|
| Backend Java; DB PostgreSQL, MySQL, H2, Oracle; frontend "React (new), velocity (old)" | UNVERIFIED | Not in any Cloud source read. Removed. | - |
| Enterprise-ready, audit logs, strong mobile apps, extensive macro system | UNVERIFIED | Marketing or not checked. Removed. | - |
| Comparisons with Notion, XWiki, Wiki.js ("commercial", "better integrations") | UNVERIFIED | Opinion, not sourced. Removed. | - |
| Data Center only: databases | WRONG | Cloud has database objects and events | S10, S14 |
| Self-hosting as "Data Center" with no date | MISSING | Data Center end of life 2029-03-28 | S20 |
| Who it suits | UNVERIFIED | Not a product statement. Removed. | - |

### features.md

| Earlier statement | Verdict | Correct fact | Source |
|-------------------|---------|--------------|--------|
| "Visual editor is the default since Cloud" | UNVERIFIED | Not stated in the pages read | - |
| Wiki Markup source-code editor as a Cloud mode | UNVERIFIED | Not documented in Cloud pages read; Cloud docs describe Markdown autoformat | S12 |
| "No Markdown in the visual editor" | WRONG | Markdown autoformat triggers exist | S12 |
| Macro syntax `{note}`, `{code}`, `{table}`, `{embed}`, `{jira:...}` | UNVERIFIED | Not documented in Cloud pages read. Macro insertion exists (shortcut `Ctrl+Shift+A` / `Cmd+Shift+A`) | S12 |
| `{toc}`, `!image.jpg!`, `h1.` markup | UNVERIFIED | Wiki Markup syntax, not confirmed for Cloud | - |
| Keyboard `Ctrl+Shift+1` for heading 1 | WRONG | Heading 1 is `Ctrl+Alt+1` (Win) / `Cmd+Opt+1` (Mac) | S12 |
| Code highlighting "with an extension" | UNVERIFIED | Not checked | - |
| Language list for code blocks | UNVERIFIED | Not checked | - |
| Comparison table (Notion, Tango.io, XWiki) | UNVERIFIED | Removed | - |
| Live preview, status bar with word count | UNVERIFIED | Not checked | - |
| Embeds list (YouTube, Google Maps, Gist, Twitter) | UNVERIFIED | Not checked | - |

### layout.md

| Earlier statement | Verdict | Correct fact | Source |
|-------------------|---------|--------------|--------|
| Left sidebar: Logo, Pages, Spaces, Dashboard, Templates | WRONG | Sidebar: For you, Recent, Starred, Spaces, Apps, More, Teams, Drafts, Company Hub (conditional), Customize sidebar | S14 |
| Top bar "navigation, search, user menu" | PARTLY | Search, Create, Chat, Notifications, Help, Your profile and settings | S14 |
| Right sidebar fixed: page info, versions, author, permissions, tags | WRONG | Details panel opened from a floating action bar at bottom right; version history is a "..." menu item | S15 |
| Sidebar widths ~50 px and ~30 px | UNVERIFIED | Not checked | - |
| Breadcrumbs always in the header | WRONG (current beta layout) | Hidden at top left while working; caret shows the full path | S15 |
| Wiki Markup editor with split preview | UNVERIFIED | Not documented for Cloud | - |
| Colour scheme "light and custom" | PARTLY | Per user Light or Dark; site default under Settings > Look and feel > Themes | S17 |
| Typography 14–16 px | PARTLY | Applies to Atlassian Design System tokens (body 14 px, large body 16 px), not verified for Confluence's rendering | S19 |
| Auto-save, responsive tablet and mobile layouts, ARIA support, performance claims | UNVERIFIED | Not checked | - |

### menus.md

| Earlier statement | Verdict | Correct fact | Source |
|-------------------|---------|--------------|--------|
| Menu "Home / start page" | PARTLY | "For you" | S14 |
| Menu "Created", "Saved", "Mentions", "Dashboard" | WRONG or UNVERIFIED | Created maps to Recent with "Owned by me" filter; Saved maps to Starred; Mentions and Dashboard not found as menu names | S14 |
| "Profile" menu with "Sign out" | PARTLY | "Your profile and settings" | S14 |
| Quick search `Cmd/Ctrl+.` | WRONG | Quick search is `Alt+Shift+Z` (Win) / `Ctrl+Opt+Z` (Mac); `Ctrl+.` is next comment; Mac `Cmd+.` opens Rovo chat | S12 |
| Create menu: "create a question (Answers)" | UNVERIFIED | Create offers page, live doc, database, Loom, whiteboard, slides; blog post via shortcut | S14, S12 |
| Page menu items Edit, Copy, Move, Delete, Permissions, Print | UNVERIFIED | Documented items: Watch settings, Version history, Find and replace, Templates and import, Archive and delete, Export to Word and PDF | S15, S16 |
| Export (PDF, Word) from page menu | CORRECT | Path: "•••" > Export > Export to Word / Export to PDF | S16 |
| Space menu "Change the theme", "Organise the content" | UNVERIFIED | Space settings path: More actions (•••) > Space settings > General > Features | S14, S17 |
| "Space backup", "Space statistics" | UNVERIFIED | Not checked; a site data backup is a separate article | S16 |
| Dashboard widgets (add or remove, share) | UNVERIFIED | Not checked | - |

### shortcuts.md

Most of the earlier table is wrong. Key errors:

| Earlier | Verdict | Correct (Windows / Mac) | Source |
|---------|---------|-------------------------|--------|
| Ctrl+Shift+F global search | WRONG | Quick search Alt+Shift+Z / Ctrl+Opt+Z | S12 |
| Ctrl+, settings | WRONG | Previous comment | S12 |
| Ctrl+K command palette / Cmd+Shift+P | UNVERIFIED | Not in official table | S12 |
| Ctrl+Shift+1…6 headings | WRONG | Ctrl+Alt+1…6 (Win), Cmd+Opt+1…6 (Mac) | S12 |
| Ctrl+Shift+L bullet list | WRONG | Ctrl+Shift+L is align left; bullet list is Ctrl+Shift+8 | S12 |
| Ctrl+E / Ctrl+L / Ctrl+R alignment | WRONG | Align centre Ctrl+Alt+E; align left Ctrl+Shift+L; align right Ctrl+Alt+T | S12 |
| Ctrl+Shift+X strikethrough | WRONG | Ctrl+Shift+S (Win); Opt+Shift+S (Mac) | S12 |
| Ctrl+Shift+M quote | WRONG | Quote Ctrl+Shift+9; Ctrl+Shift+M is code block / inline code | S12 |
| Ctrl+Shift+T table | WRONG | Table Ctrl+Shift+I | S12 |
| Ctrl+Shift+D diagram | WRONG | Ctrl+Shift+D is "Insert markup" and "Create live doc" | S12 |
| Ctrl+Shift+A task | WRONG | Ctrl+Shift+A is Macro | S12 |
| Ctrl+B / Ctrl+I (Mac Cmd) | PARTLY | Windows correct; Mac Opt+B / Opt+I per official table | S12 |
| Ctrl+B sidebar toggle | WRONG | Ctrl+[ | S12 |
| Ctrl+Shift+I developer tools | WRONG | Ctrl+Shift+I opens the details panel | S12 |
| Ctrl+S, Ctrl+P, Ctrl+N, Ctrl+O, Ctrl+W, Ctrl+Shift+N/S/E/X | UNVERIFIED | Not in official table; Ctrl+Enter publishes | S12 |
| F1 help, F11 full screen | UNVERIFIED | Not in official table | S12 |
| Ctrl+Shift+V video, Ctrl+Shift+B box, Ctrl+Shift+E embed | UNVERIFIED | Not in official table | S12 |
| Ctrl+K link | CORRECT | Ctrl+K / Cmd+K | S12 |
| Ctrl+F find | CORRECT | Find and replace (Ctrl+F / Cmd+F) | S12 |
| Ctrl+Enter publish | CORRECT | Ctrl+Enter / Cmd+Enter | S12 |
| Ctrl+Z / Ctrl+Y undo, redo | CORRECT | Same keys, plus Ctrl+Shift+Z for redo | S12 |
| Shortcuts can be customised (implied) | UNVERIFIED | Not stated; General shortcuts can be turned off | S12, S13 |
| Table navigation with Tab / Shift+Tab | UNVERIFIED | Not in official table; official table lists add row and column shortcuts | S12 |

### api.md, events.md, limits.md: rate limits and events, summary

Covered above. The earlier claim of a "100 requests per second" Cloud limit and the 5-minute request budget are both replaced by the points model in S5.

### Earlier index.md

| Earlier statement | Verdict | Correct fact | Source |
|-------------------|---------|--------------|--------|
| "Notable ideas: To do" | MISSING | Filled in index.md of the new set | S1, S10, S14 |
| "Documented versions" table, 6/7 files present | Obsolete | Replaced by `latest/` with new file set | - |

### Items the earlier pages did not cover at all

- Atlassian Design System tokens (themes): S18, S19, S21
- Cloud navigation redesign and beta content layout: S14, S15
- Export options for spaces: S16
- Data Center end of life: S20
- GraphQL limits: S8
- OAuth refresh-token rules: S6
- Publishing-approval 409 change and IP-range change: S9
