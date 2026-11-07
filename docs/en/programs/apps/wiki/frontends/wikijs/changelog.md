# Changelog

## 2026-11-07: rewritten from official sources

The earlier pages were written from memory; these statements were wrong.

Existing pages: `/srv/FreeSynergy/fs-documentation/docs/en/programs/apps/wiki/frontends/wikijs/` (index.md and latest/*.md). They were written from memory and describe a mix of Wiki.js 2.x and generic wiki features. Status codes:

- **W** wrong for 3.1.1 (checked against source or official docs)
- **U** unverifiable (no source found; remove or mark)
- **M** missing from the old set
- **OK** correct, kept

Source base for 3.1.1: https://github.com/requarks/wiki/tree/3.1.1 (short form `3.1.1:<path>`). 2.x facts: https://github.com/requarks/wiki/tree/v2.5.315 (short form `2.5.315:<path>`).

### index.md

| Status | Old statement | Correct fact | Source |
|--------|---------------|--------------|--------|
| U | "modern, lightweight wiki system" | "lightweight" has no source. Official wording: "The open source wiki engine. Built and maintained in the open since 2017." | https://js.wiki/ |
| M | "Notable ideas: _To do_" | filled in `index.md` (storage targets, eight editors, Yjs, personal tokens, MCP) | `3.1.1:backend/modules/storage/`, `3.1.1:backend/models/sites.ts` |
| W | "Documented versions: latest" | the newest 3.x is **3.1.1** (2026-11-06); 3.1.0 exists (2026-11-05); 3.1 is released, not missing | https://github.com/requarks/wiki/releases |

### description.md

| Status | Old statement | Correct fact | Source |
|--------|---------------|--------------|--------|
| W | Database: "PostgreSQL, MySQL, SQLite" | 3.1.1 uses PostgreSQL only (pg driver, Drizzle `node-postgres`) | `3.1.1:backend/core/db.ts`, `3.1.1:backend/package.json` |
| W | Frontend: "Vue.js" | Vue 3.5, Vite 8, Pinia, Tailwind 4 (2.x used Vue 2 and Vuetify 2) | `3.1.1:frontend/package.json`, `2.5.315:package.json` |
| W | Authentication: "OAuth2, LDAP, SAML (via extensions)" | built in: local, LDAP, OIDC, SAML, GitHub, Google, Discord, Entra | `3.1.1:backend/modules/authentication/` |
| W | "Two editor modes: WYSIWYG for beginners, Markdown for advanced users" | eight editor types per site: markdown, visual, asciidoc, excalidraw, blog, feedback, redirect, plus live notes | `3.1.1:backend/models/sites.ts`, https://docs.js.wiki/guide/editors |
| W | "Confluence has better enterprise features (SSO, audit logs)" | 3.1.1 has an audit log, SAML, OIDC, SCIM, and groups. Comparison itself is not verifiable. | `3.1.1:backend/models/auditLog.ts`, `3.1.1:backend/api/scim.ts` |
| U | "Modularly extensible: plugin system for additional functions" | modules are discovered from disk for auth and storage; no plugin marketplace or editor plugin API was found | `3.1.1:backend/CLAUDE.md` (modules) |
| U | "Good performance", "Modern design", "more lightweight than MediaWiki", "more modern than MediaWiki" | opinion or marketing; no source | — |
| U | "Notion has better visual design" | opinion | — |
| U | "Who Wiki.js suits" list | not from the project; no source | — |
| U | "Hosting: self-hosted or cloud" | official install methods: Docker, Kubernetes, bare metal, cloud images. Wording of "cloud" as a hosted service was not checked. | https://js.wiki/ |
| OK | "Backend: Node.js" | Node.js >= 26 with Fastify 5 | `3.1.1:backend/package.json` |
| OK | "Open source" | AGPL v3 licence | `3.1.1:LICENSE` |

### features.md

| Status | Old statement | Correct fact | Source |
|--------|---------------|--------------|--------|
| W | "Two editor modes" (WYSIWYG and Markdown) | see description.md: eight editor types | as above |
| W | Extensible through plugins: "Mermaid, LaTeX, Kroki, MathJax, VideoJS, Embeds for Spotify, Twitter" | renderer modules present: katex, kroki, plantuml, markdown-it plugins. Mermaid, MathJax, VideoJS, Spotify and Twitter were not found. | `3.1.1:frontend/src/renderers/modules/` |
| U | "Syntax highlighting for 200+ languages" | highlight.js 11.12.0 is the library; the language count was not checked | `3.1.1:frontend/package.json` |
| U | Visual editor: "Alignment: left, centre, right, justified", "Text colour not supported", "no vertical text alignment" | not checked | — |
| U | "Notices/boxes: info, warning, success" | 3.1.1 has content blocks (`blocks/block-tabs`, `block-steps`, `block-spoiler`, `block-youtube`, `block-qr-code`, …); the notice set was not checked | `3.1.1:blocks/` |
| U | "Embeds: videos (YouTube, Vimeo), iframes" | YouTube block exists; Vimeo and iframes not checked | `3.1.1:blocks/block-youtube` |
| U | "Images: drag & drop" in both editors | pending asset upload queue exists; drag and drop not confirmed | `3.1.1:frontend/src/components/PageActionsCol.vue` |
| U | "Front matter: metadata for pages (title, description)" as user feature | front matter appears in the storage module (disk, git, sftp) only | `3.1.1:backend/helpers/storageFiles.ts` |
| U | "Snippets: templates for frequently used blocks" | Markdown editor has snippet inserts for some blocks (abbreviation); general snippet library not verified | `3.1.1:frontend/src/components/EditorMarkdown.vue` |
| U | "Live preview" in Markdown | preview with scroll sync exists | `3.1.1:frontend/src/composables/previewScrollSync.js` |
| U | Comparison table (Table editor visual vs text, "no WYSIWYG while editing") | not checked | — |
| OK | Markdown support: GitHub-style tables, task lists, strikethrough | markdown-it with task-list and multi-table plugins | `3.1.1:frontend/package.json` |
| M | (absent) collaboration, page history, comments, feedback boards, approvals, blogs, glossary, MCP | all present in 3.1.1 | see `3.1.1/features.md` |

### layout.md

| Status | Old statement | Correct fact | Source |
|--------|---------------|--------------|--------|
| W | Sidebar items: Home, Pages, Media, Users, Groups, Settings | drawer holds the site navigation tree, a browse menu and "Edit Nav"; admin sections are in the admin area | `3.1.1:frontend/src/components/NavSidebar.vue`, `3.1.1:frontend/src/router/routes.js` |
| W | "Sidebar (right): optional meta information (versions, author)" | the right side is the page actions rail (48 px) and the table of contents position; sidebar may be placed right, not a meta column | `3.1.1:frontend/src/css/_theme.scss`, `3.1.1:backend/models/sites.ts` |
| W | "Mobile: hamburger menu" | no menu button in the header; on narrow screens the drawer is an overlay opened by a button at the bottom left | `3.1.1:frontend/src/layouts/MainLayout.vue` (comment on the corner button) |
| U | "Breadcrumbs: the navigation path" | a breadcrumb component exists (`WBreadcrumbs.vue`); its use on the page view was not checked | `3.1.1:frontend/src/components/shared/WBreadcrumbs.vue` |
| U | "Status bar (words, characters, preview button)" in WYSIWYG | not checked | — |
| U | "Full-screen editor: only the editor" | not checked | — |
| U | "Auto-save" | not checked | — |
| U | Typography: "H1–H6", "14–16 px" | not extracted | — |
| U | "Tablet: reduced sidebar" | not checked | — |
| OK | Light and dark theme, custom colours | dark switch and five brand colours per site | `3.1.1:backend/models/sites.ts` |
| OK | Accessibility: keyboard navigation, ARIA labels | icon buttons carry `aria-label` | `3.1.1:frontend/src/components/HeaderNav.vue` |

### menus.md

The whole old menu list is wrong for 3.1.1.

| Status | Old statement | Correct fact | Source |
|--------|---------------|--------------|--------|
| W | Main menu: Home, Pages, Editor, Trash, Media, Users, Groups, Access, Settings, Appearance, Extensions, Logs, Search | header: Home, Search, Create, Library, Inbox, Administration, Login/Account. Admin: about 40 routes (Dashboard, Sites, General, Approvals, Analytics, Blocks, Comments, Editors, Locale, Login, Navigation, Storage, Theme, Auth, Groups, Users, SCIM, API, MCP, Webhooks, Audit, Extensions, Icons, Mail, Metrics, Notifications, Rendering, Scheduler, Search, Security, System, Terminal, Utilities, Flags, …) | `3.1.1:frontend/src/router/routes.js`, `HeaderNav.vue` |
| W | Context menu on a page: Edit, Move, Copy, Delete, Show history, Permissions | the page rail has: Page Properties, Page Data, History, Source, Actions (convert, rerender), Duplicate, Rename / Move, Delete. Permission view is an API call (`.../pages/userPermissions`), not a menu item seen in the rail. | `3.1.1:frontend/src/components/PageActionsCol.vue` |
| W | User menu: Profile, Settings, Sign out | profile sections: info, avatar, auth, groups, live notes, access tokens, notifications; logout in the header account item | `3.1.1:frontend/src/router/routes.js`, locale `common.header.logout` |
| U | "Trash: manage deleted pages" as a main menu item | deleted pages can be restored "from the administration area" (locale string); a list endpoint exists | `3.1.1:backend/api/pages.ts` (`/sites/:siteId/pages/deleted`) |
| U | "Logs" | admin has Audit, Metrics, System, Terminal; "Logs" name not checked | `routes.js` |
| U | "Search: filter options" | search exists with filters (see api.md); menu item name not checked | `3.1.1:backend/api/pages.ts` |

### shortcuts.md

Most of the old list is not in the 3.1.1 source. The correct list is in `3.1.1/shortcuts.md`.

| Status | Old shortcut | Correct fact | Source |
|--------|--------------|--------------|--------|
| W | Ctrl+Shift+P command palette | not found | search of frontend source |
| W | Ctrl+, settings; F1 help; Ctrl+Shift+F global search | not found | search of frontend source |
| W | Ctrl+K add link; Ctrl+K link shortcuts | not found in the Markdown or Visual keymaps | `3.1.1:frontend/src/editor/visual/commands.js`, `EditorMarkdown.vue` |
| OK | Ctrl+B bold (visual) | correct for both editors (Mod+B) | `3.1.1:frontend/src/editor/visual/commands.js`, `EditorMarkdown.vue` |
| W | Ctrl+B show or hide sidebar (view section) | Mod+B is bold in the editors; no sidebar shortcut found | as above |
| W | Ctrl+Shift+L bullet list | Mod+Shift+8 is bullet list (visual) | `3.1.1:frontend/src/editor/visual/commands.js` |
| W | Ctrl+Shift+1…6 headings | correct (visual, Mod+Shift+1 to 6) | `commands.js` |
| W | Ctrl+Shift+X strikethrough | correct (Mod+Shift+X) | `commands.js` |
| W | Ctrl+Shift+K code tag; Ctrl+Shift+C code block; Ctrl+Shift+M quote | code: Mod+E (inline code); quote: Mod+Shift+. (blockquote); code block: no binding (Mod+Enter exits a code block) | `commands.js` |
| W | Ctrl+E / Ctrl+L / Ctrl+R alignment; Ctrl+Shift+E justify | Mod+E is inline code; no alignment bindings | `commands.js` |
| W | Ctrl+Shift+H replace with context | Mod+Shift+H highlights text in the visual editor | `commands.js` |
| W | Ctrl+Enter preview or publish | Mod+Enter leaves a code block (visual); no publish shortcut found | `commands.js` |
| W | Ctrl+Shift+V live preview; Ctrl+Shift+F file tree; Ctrl+Shift+B status bar | not found | search |
| W | Ctrl+N new page; Ctrl+O open page; Ctrl+W close; Ctrl+Shift+N new folder; Ctrl+P print or file search | not found; Ctrl+P print is a browser shortcut | search |
| U | Ctrl+G / Ctrl+Shift+G next and previous match | Monaco default in the Markdown editor; not a Wiki.js binding | Monaco |
| OK | Ctrl+S save | Mod+S in the Markdown and AsciiDoc editors asks the header Save button | `EditorMarkdown.vue`, `EditorAsciidoc.vue` |
| OK | Ctrl+Z undo, Ctrl+Y redo | Mod+Z, Mod+Shift+Z, Mod+Y (visual) | `commands.js` |
| OK | Ctrl+Alt+Left/Right heading level | Mod+Alt+Left/Right in Markdown and AsciiDoc editors | `EditorMarkdown.vue` |
| U | F11 full screen; Ctrl+Shift+I developer tools | browser features, not Wiki.js | — |
| U | Keyboard navigation with arrow keys between blocks | only slash-menu arrows verified | `slash.js` |

### api.md

| Status | Old statement | Correct fact | Source |
|--------|---------------|--------------|--------|
| W | REST base `/api/v1/…` | REST base is `/_api/…`; site-scoped paths `/_api/sites/:siteId/pages/…` | `3.1.1:backend/index.ts` (`prefix: '/_api'`), `3.1.1:backend/api/pages.ts` |
| W | GraphQL at `/graphql`, "complete GraphQL API" | no GraphQL in 3.1.1. GraphQL existed in 2.x (`server/graph/schemas`). | `3.1.1` tree (no graphql); `2.5.315:server/graph/schemas/` |
| W | "API tokens: Configuration > API Tokens" | admin: Administration → API (route `api`); personal tokens: Profile → Access tokens (`/_profile/tokens`) | `3.1.1:frontend/src/router/routes.js`, `3.1.1:.claude/rules/personal-access-tokens.md` |
| W | Authentication endpoints `POST /api/v1/auth/login`, `/logout`, `/refresh` | not present. Logout is `POST /_api/sites/:siteId/auth/logout`; passkey login is `PUT /_api/sites/:siteId/auth/passkey/login`. Password login route: not found in the grep. | `3.1.1:backend/api/authentication.ts` |
| W | `GET /api/v1/meta`, `/meta/stats` | not found | `3.1.1:backend/api/` (list of files) |
| W | Users: `GET/POST/PUT/DELETE /api/v1/users` | users are under `/_api/users…` (prefix from `index.ts`); methods were not read. The old path is not valid. | `3.1.1:backend/index.ts` (`users.ts`, prefix `/users`) |
| W | Pages: `GET /api/v1/pages`, `PUT /api/v1/pages/:id`, `DELETE`, `GET /pages/:id/history` | equivalent exists under `/_api/sites/:siteId/pages…` (see `3.1.1/api.md`); base path and `:siteId` differ | `3.1.1:backend/api/pages.ts` |
| W | "Create page" body: `title, description, content, path, public` | the schema has `path, title, description, locale, editor, content` and more; a `public` field was not found | `3.1.1:backend/api/schemas/page.ts` |
| W | Rate limit "100 requests per minute per API token", `X-RateLimit-*` headers | not in 3.1.1; only a fixed-window limiter for authentication | `3.1.1:backend/models/rateLimits.ts` |
| W | Webhook events `page.create`, `page.update`, `page.delete`, `page.move`, `page.revert` | 3.1.1 events: `page:create`, `page:edit`, `page:rename`, `page:delete`, `asset:*`, `comment:*`, `user:join`, `user:login`, `user:logout` | `3.1.1:backend/models/hooks.ts` |
| W | Webhooks under "Configuration > Webhooks" | Administration → Webhooks (route `webhooks`) | `3.1.1:frontend/src/router/routes.js` |
| U | Official SDKs `wiki.js-api-client` (npm), `pywikijs` (PyPI) | not found in the official repo or docs. Do not list. | `3.1.1` tree; https://docs.js.wiki/dev/api |
| U | Python `requests` example | invented, not run; removed | — |
| W | "Session cookie: for internal use" | the UI itself uses the session cookie for all calls | `3.1.1:frontend/CLAUDE.md` |
| OK | Bearer header for API keys | `Authorization: Bearer <key>` is correct. Admin page is named API, and a system key acts for its groups, not a user. | https://docs.js.wiki/dev/api |
| M | Webhook signing not described | no signature header in 3.1.1; state this in the page | `3.1.1:backend/models/hooks.ts` |
| W | "See also" links: `menu.md`, `structure.md` | target files are `menus.md` and `layout.md` | `fs-documentation` folder listing |

### themes/index.md

| Status | Old statement | Correct fact | Source |
|--------|---------------|--------------|--------|
| M | File missing (the generated index flags it) | created in the new set: `3.1.1/themes/index.md` | `3.1.1:backend/models/sites.ts`, `3.1.1:frontend/src/pages/AdminTheme.vue` |

### Version folder

| Status | Old statement | Correct fact |
|--------|---------------|--------------|
| M | Folder `latest/` | use the exact release: `3.1.1/` (3.1.0 is the previous release; the set does not split 3.1.0 and 3.1.1 because the 3.1.1 notes contain only bug and security fixes; see `3.1.1/description.md`) |

Source for the bug-fix-only statement: https://github.com/requarks/wiki/releases/tag/3.1.1

### Not yet checked (open)

- Whether the docs site (https://docs.js.wiki) describes the same keyboard shortcuts. Its guide pages were listed, not read; no shortcut page was listed.
- The `Library` header button target.
- Exact webhook retry policy.
- The password login route.
