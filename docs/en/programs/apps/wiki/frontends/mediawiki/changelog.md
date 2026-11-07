# Changelog

## 2026-11-07: rewritten from official sources

The earlier pages were written from memory; these statements were wrong.

Checked against the sources named in each row, on 2026-11-07, for MediaWiki 1.46.2. Existing pages: `/srv/FreeSynergy/fs-documentation/docs/en/programs/apps/wiki/frontends/mediawiki/` (index.md, latest/*.md).

Status key: **WRONG** = contradicted by a source. **UNVERIFIED** = no source found in this run; do not use without checking. **PARTLY** = true with a missing or wrong detail.

### api.md

| # | Existing statement | Status | Correct fact | Source |
|---|--------------------|--------|--------------|--------|
| A1 | "MediaWiki offers an extensive REST-based API for access to all wiki functions ... supports all CRUD operations" | WRONG | The Action API (`api.php`) is the full API. The REST API (`rest.php`) is a smaller set of resources. | https://www.mediawiki.org/wiki/API:REST_API ; https://www.mediawiki.org/wiki/API:Main_page |
| A2 | Auth methods: "Clientlogin, OAuth, Bot passwords, Session cookies, PATRICIA" | PARTLY | Clientlogin and bot passwords are core. OAuth is an extension, not core. "PATRICIA" is not a MediaWiki auth method found in core or in API docs. | https://www.mediawiki.org/wiki/API:Login ; source tree `includes/User/BotPassword.php`; no OAuth or PATRICIA module in REL1_46 |
| A3 | Endpoint `GET/POST /w/api.php` | PARTLY | `/w/` is only the path on Wikimedia sites. The path depends on the install. Find it on Special:Version. | https://www.mediawiki.org/wiki/API:Main_page |
| A4 | Table "Pages": action `history` | WRONG | No `history` action module. Revisions come from `prop=revisions` (or REST `/v1/page/{title}/history`). | source tree `includes/Api/ApiQueryRevisions.php`; `coreRoutes.json` |
| A5 | `query&list=images` "list files" | WRONG | `list=allimages` lists files. `prop=images` lists files used by a page. | `includes/Api/ApiQueryAllImages.php`, `ApiQueryImages.php` |
| A6 | `query&list=userprop` "user properties" | WRONG | No `list=userprop`. Use `list=users` with `usprop`, or `meta=userinfo`. | `includes/Api/ApiQueryUsers.php`, `ApiQueryUserInfo.php` |
| A7 | `deletefile` "delete a file" | WRONG (module) | No `ApiDeleteFile` module in REL1_46. File deletion is not a separate module here (path not identified). | source tree file list |
| A8 | `createaccount` "create an account" | UNVERIFIED | A class `ApiAMCreateAccount` exists; the registered module name was not checked. | `includes/Api/ApiAMCreateAccount.php` |
| A9 | `query&meta=globalinfo` | WRONG (core) | Not in core. It belongs to an extension (CentralAuth). No `ApiQueryGlobalInfo` in REL1_46. | source tree |
| A10 | `query&meta=siteinfo`, `query&meta=tokens` | PARTLY | `tokens` is correct. `siteinfo` is documented, but its module file was not checked in this run. | `ApiQueryTokens.php` |
| A11 | Edit flow: `action=query&meta=tokens&type=edit` and `edittoken` | WRONG | Edit token type is `csrf`. `edittoken` is not a token name in core. | `includes/Api/ApiQueryTokens.php` (`getTokenTypeSalts`: `csrf`, `watch`, `patrol`, `rollback`, `userrights`, `login`, `createaccount`) |
| A12 | Login flow with `clientlogin` and `logintoken` | PARTLY | Correct in outline. The sample omits the clientlogin fields the server requires (for example the return URL); status handling (UI, REDIRECT, `logincontinue`) is missing. | https://www.mediawiki.org/wiki/API:Login |
| A13 | Python and JS edit examples | WRONG (token) | Same as A11. The examples fail on current core with the edit token name. | A11 |
| A14 | "GraphQL (MediaWiki 1.39+)" and `/graphql` endpoint | WRONG | No GraphQL in core. Any GraphQL endpoint is from an extension, not checked. The sample query is not an existing API. | source tree (no GraphQL module) |
| A15 | Rate limits: "50 req/s per IP", "100 req/s authenticated", "bots 10/sec" | WRONG | No such defaults. Core limits are per action in `$wgRateLimits`: edit 8/60 s per IP and newbie, 90/60 s per user; move 2/120 s newbie, 8/60 s user; upload 8/60 s IP and newbie; rollback 10/60 s user. Reads have no default limit in the config. | https://github.com/wikimedia/mediawiki/blob/REL1_46/includes/config-schema.php (key `RateLimits`); https://www.mediawiki.org/wiki/API:Etiquette (summary-only) |
| A16 | Config names `$wgRateLimit`, `$wgRateLimitLog`, `$wgUserRateLimit`, `$wgExtensionFunctions` | WRONG | The key is `$wgRateLimits`. `$wgRateLimitLog` and `$wgUserRateLimit` do not appear in the config schema. | config-schema.php |
| A17 | Webhooks via Echo: edit, new, move, delete, protect events | WRONG | Echo is an in-wiki notification extension (alerts, web and email notifications, push settings). It is not a webhook system. No URL webhook documented. | https://www.mediawiki.org/wiki/Extension:Echo |
| A18 | SDK list (mediawiki JS official, mwclient, wikipedia-api, mediawiki-api-client, mwapi, mediawiki-gems, go-mediawiki) | UNVERIFIED | Not checked in this run. | — |
| A19 | "See also" links `menu.md`, `structure.md` | WRONG (link) | Files are `menus.md` and `layout.md`. | file set |
| A20 | Action list "login (deprecated)", "logout", "userrights", "block", "unblock", "purge", "rollback", "protect", "move", "upload" | CORRECT | Modules exist in REL1_46. | `includes/Api/Api*.php` |

### description.md

| # | Existing statement | Status | Correct fact | Source |
|---|--------------------|--------|--------------|--------|
| D1 | "Database: PostgreSQL, MySQL, MariaDB" | PARTLY | Also SQLite. MariaDB is recommended. Minimums: MariaDB 10.3+, MySQL 5.7+, PostgreSQL 10+, SQLite 3.8+. | RELEASE-NOTES-1.46 (Compatibility) |
| D2 | "Authentication: local accounts, OAuth, LDAP" | WRONG (core) | Local accounts and bot passwords are core. OAuth and LDAP are not in core (extensions). | source tree; https://www.mediawiki.org/wiki/API:Login |
| D3 | "Frontend: JavaScript, PHP templates" | PARTLY | The default skin (Vector 2022) uses Mustache templates and JavaScript modules with Codex design tokens. | https://github.com/wikimedia/mediawiki-skins-Vector/tree/REL1_46 |
| D4 | "MediaWiki is the most popular wiki software" | UNVERIFIED | Not checked. Use "widely used; runs Wikipedia" only if a source is added. | — |
| D5 | Comparisons with Wiki.js, XWiki, Confluence (speed, licence costs, macro systems, Jira integration) | UNVERIFIED | No source in this run. Remove or source them. | — |
| D6 | "Scalable: millions of pages" | UNVERIFIED | Wikimedia wikis are large; no figure checked. | — |
| D7 | "Established: very stable and well tested" | UNVERIFIED | Opinion. Replace with the lifecycle facts (support table). | https://www.mediawiki.org/wiki/Version_lifecycle |
| D8 | "Who MediaWiki suits" list | UNVERIFIED | Opinion. | — |

### features.md

| # | Existing statement | Status | Correct fact | Source |
|---|--------------------|--------|--------------|--------|
| F1 | "VisualEditor: no direct wiki-syntax editing in visual mode" | PARTLY | VisualEditor has an "Edit source" entry (access key `e`, message `accesskey-ca-editsource`). It can switch to the source editor. | https://www.mediawiki.org/wiki/Help:Keyboard_shortcuts (access-key table, extension rows) |
| F2 | "Sources: citations and references" in VisualEditor | PARTLY | VisualEditor has an "Insert citation" action (Ctrl+Shift+K). Automatic citation (Citoid) is an extension, not checked. | https://www.mediawiki.org/wiki/VisualEditor/Portal/Keyboard_shortcuts |
| F3 | "Math formulas: LaTeX (optional)", "Diagrams: Graphviz", "Score", "Kartographer", "Linter", "Citoid", "Graph" as VisualEditor extensions | UNVERIFIED | Extensions. Not checked in this run. | — |
| F4 | "Source-code editor: syntax highlighting, line numbers, autocompletion, diff in context" as part of the source editor | PARTLY | Highlighting, line numbers, search, bracket matching and a shortcut dialog come from the CodeMirror extension, not core. Autocompletion is off by default for wikitext. CodeMirror becomes the default for most integrations in 1.47. | https://www.mediawiki.org/wiki/Extension:CodeMirror |
| F5 | "Edit source code (alternative mode)", "Code editor for developers" | UNVERIFIED | Not a core mode. Treat as CodeMirror. | https://www.mediawiki.org/wiki/Extension:CodeMirror |
| F6 | "MediaWiki Source Editor variant ... Diff view: the changes in context" | UNVERIFIED | No source for a split diff view. | — |
| F7 | "WikiEditor: extended toolbar" | UNVERIFIED | Page https://www.mediawiki.org/wiki/Help:WikiEditor returned HTTP 404 in this run. | — |
| F8 | "Templates (visual)" in VisualEditor | PARTLY | The template dialog exists (keys listed in the VisualEditor shortcut page). Its limits were not checked. | https://www.mediawiki.org/wiki/VisualEditor/Portal/Keyboard_shortcuts |
| F9 | "Live preview: yes" for VisualEditor and "no (optional)" for source | UNVERIFIED | Not checked. Source editor has a preview action (access key `p`). | https://www.mediawiki.org/wiki/Help:Keyboard_shortcuts |
| F10 | Recommendations (beginners use VE, advanced use source) | UNVERIFIED | Opinion. | — |

### layout.md

| # | Existing statement | Status | Correct fact | Source |
|---|--------------------|--------|--------------|--------|
| L1 | Sidebar (left) holds logo, search and languages | WRONG | In Vector 2022 the search box and logo are in the header. The left sidebar is the main menu (pinnable). Languages are in the header (ULS button) or in the content. | `includes/templates/Header.mustache` (contains MainMenuDropdown, Logo, SearchBox, UserLinks); `skin.mustache`; `SkinVector22.php` |
| L2 | "Colour scheme: light theme" only | WRONG | Vector 2022 has a night mode: preference `vector-theme` = `day`, `night`, `os`. | https://github.com/wikimedia/mediawiki-skins-Vector/blob/REL1_46/doc/configuration/configuration.md |
| L3 | "Breadcrumbs (optional)" in the content header | WRONG (not in skin) | No breadcrumb partial in Vector 2022 templates. | `includes/templates/skin.mustache`, `Header.mustache` |
| L4 | Content header with "share" action | UNVERIFIED | No "share" item in Vector 2022 templates or core messages checked. | — |
| L5 | Font sizes 14–16 px; "Heading H1–H6" | PARTLY | Vector sets `@font-size-heading-1` 1.8em, heading-2 1.5em, heading-3 1.2em, base line-height 1.6. Heading 4–6 not defined in these variables. Text size is a user preference (0/1/2). | `resources/skins.vector.styles/variables.less`; `configuration.md` |
| L6 | "Auto-save in the editor" | UNVERIFIED | Not found in the sources read. | — |
| L7 | "Drag & drop for media uploads" | UNVERIFIED | Not checked. | — |
| L8 | Responsive "tablet" and "mobile hamburger" | UNVERIFIED | Vector 2022 responsive mode is an experimental flag (`wgVectorResponsive`). The hamburger/main-menu behaviour is not confirmed. | `configuration.md` |
| L9 | Visual editor layout: formatting bar, status bar with word count and preview button | UNVERIFIED | Not checked. | — |
| L10 | Source editor layout: left editor, right diff/preview | UNVERIFIED | Not checked. | — |
| L11 | Accessibility claims (ARIA, contrast, zoom) | UNVERIFIED | Generic. Not checked. | — |

### menus.md

| # | Existing statement | Status | Correct fact | Source |
|---|--------------------|--------|--------------|--------|
| M1 | "Actions (sidebar): ... print the page" | WRONG (group) | Print is a Tools item (`tooltip-t-print`, the "t" portlet), not a page action. | `languages/i18n/en.json` (`tooltip-t-print`); Help:Keyboard_shortcuts (accesskey `p` on "any page" rows) |
| M2 | "Tools (sidebar): what links here, related changes, new pages, special pages, printable version" | PARTLY | What links here, related changes, permanent link, page information and print are Tools items. "New pages" and "special pages" as Tools items were not checked. | `en.json` tooltips `tooltip-t-whatlinkshere`, `tooltip-t-recentchangeslinked`, `tooltip-t-info`, `tooltip-t-permalink` |
| M3 | "Main page (menu item 1)", "Pages (menu item 2)" | UNVERIFIED | Vector 2022 main menu content comes from site config; "Pages" is not a core menu. | `MainMenu.mustache` |
| M4 | "Special pages", "user contributions", "upload", "orphaned pages", "unlocalised pages", "random page" as special pages | PARTLY | Random page is a main-menu item (`tooltip-n-randompage`). Upload has `tooltip-t-upload`. The rest were not checked. | `en.json` |
| M5 | User menu for logged-out users: "discussion page, contributions, create an account, log in" | PARTLY | Create account (`tooltip-pt-createaccount`) and log in (`tooltip-pt-login`) exist. | `en.json` |
| M6 | User menu for logged-in users: "watchlist, changes on the watchlist, settings, login status" | PARTLY | Watchlist and preferences exist (`tooltip-pt-watchlist`, `tooltip-pt-preferences`). "Login status" and "changes on the watchlist" as items were not checked. | `en.json` |
| M7 | Roles menus (anonymous, registered, sysop) | UNVERIFIED | Depends on `$wgGroupPermissions` and extensions. Not checked. | — |
| M8 | Sysop: "delete/restore pages, protect, block, rename, delete files, view logs" | PARTLY | Delete, undelete, protect, block, move (rename) exist as modules. "Delete files" has no module (see A7). "View logs" was not checked. | api.md section 1 |
| M9 | Edit menu: "edit the source, visual editor, preview, summarise" | PARTLY | Preview (`p`), summary (`b`), edit (`e`) and source/VE switch exist. The "summarise" action name is not a core item. | Help:Keyboard_shortcuts |
| M10 | Discussion menu: "add a new section, edit a section, end the discussion" | PARTLY | "Add a new section" is `ca-addsection` (key `+`). "Edit a section" and "end the discussion" are not core features (talk features are extensions). | Help:Keyboard_shortcuts |
| M11 | Version menu: "show differences, restore, history" | PARTLY | Diff (`v` in edit), history (`h`) and rollback exist. "Restore" is undelete for deleted pages, not a general restore of an old revision. | Help:Keyboard_shortcuts; `ApiUndelete` not checked |

### shortcuts.md

Most of the file is wrong. MediaWiki core does not use Ctrl+letter page shortcuts. It uses access keys (one letter plus a browser-specific modifier, see `1.46/shortcuts.md`).

| # | Existing statement | Status | Correct fact | Source |
|---|--------------------|--------|--------------|--------|
| S1 | Ctrl+Shift+P command palette; Ctrl+, settings; F1 help; Ctrl+Shift+F global search; Ctrl+K search bar | WRONG | No command palette or these shortcuts in core. Search is access key `f`; preferences are `Special:Preferences` (no access key listed for opening it). Ctrl+K in VisualEditor is "Insert link". | Help:Keyboard_shortcuts; VisualEditor/Portal/Keyboard_shortcuts |
| S2 | Ctrl+S save; Ctrl+P print; Ctrl+N new page; Ctrl+O open; Ctrl+W close; Ctrl+Shift+S save as; Ctrl+Shift+P export | WRONG | Ctrl+S is not a MediaWiki save shortcut. Save is access key `s` (VisualEditor: Alt+S on Windows/Linux, Ctrl+Option+S on Mac). Print is access key `p`. Ctrl+P, Ctrl+N, Ctrl+O, Ctrl+W, Ctrl+Shift+S are browser functions, not MediaWiki. | Help:Keyboard_shortcuts; VisualEditor/Portal/Keyboard_shortcuts; jquery.accessKeyLabel.js |
| S3 | VisualEditor Ctrl+U underline; Ctrl+E/L/R/Shift+E alignment; Ctrl+Shift+1–6 headings; Ctrl+Shift+L bullet list; Ctrl+Shift+M quote; Ctrl+Shift+D image; Ctrl+Shift+V video; Ctrl+Shift+T table/template; Ctrl+T template editor | WRONG or UNVERIFIED | The VisualEditor shortcut page lists Ctrl+B, Ctrl+I, Ctrl+K, Ctrl+Shift+K (cite), Ctrl+Shift+V (paste as plain text), Ctrl+Z, Ctrl+Shift+Z, Tab/Shift+Tab (list indent), Ctrl+\ or Ctrl+M (clear formatting), Alt+S (save), Ctrl+Shift+X (writing direction). Underline, alignment, headings, quote, image, video, table and template-editor keys are not in that list. | VisualEditor/Portal/Keyboard_shortcuts |
| S4 | Ctrl+Shift+X strikethrough | WRONG | Ctrl+Shift+X in VisualEditor switches writing direction. | VisualEditor/Portal/Keyboard_shortcuts |
| S5 | Source editor: Ctrl+B bold, Ctrl+I italic, Ctrl+Shift+L bullet, Ctrl+Shift+N numbered, Ctrl+Shift+1/2/3 headings, Ctrl+K link | UNVERIFIED | Not found in any official page read in this run. | — |
| S6 | Source editor: Ctrl+Shift+F toggle syntax highlighting | UNVERIFIED | CodeMirror has a keyboard shortcut help dialog; this key was not confirmed. | https://www.mediawiki.org/wiki/Extension:CodeMirror |
| S7 | Ctrl+F search; Ctrl+G next match; Ctrl+H replace; Ctrl+Shift+O page structure; Ctrl+P file search panel | WRONG or UNVERIFIED | Ctrl+F, Ctrl+G, Ctrl+H are browser or editor functions. The file search panel and page structure are not MediaWiki shortcuts. | — |
| S8 | F11 full screen; Ctrl+Shift+I developer tools; Ctrl+B show/hide sidebar; Ctrl+Shift+B status bar | WRONG (MediaWiki) | F11 and Ctrl+Shift+I are browser shortcuts. Ctrl+B is bold in VisualEditor, not a sidebar toggle. | VisualEditor/Portal/Keyboard_shortcuts |
| S9 | Ctrl+Enter preview/publish | WRONG | Preview is access key `p`; publish is `s`. | Help:Keyboard_shortcuts |
| S10 | Extension shortcuts: Ctrl+Shift+M math, Ctrl+Shift+C code block, Ctrl+Shift+G Graphviz, Ctrl+Shift+A ASCII art, Ctrl+Shift+Q quote | UNVERIFIED | Not checked. Ctrl+Shift+G conflicts with browser shortcuts, so it is doubtful. | — |
| S11 | Mac shortcuts (Cmd+Shift+P, Cmd+, etc.) | WRONG | Same as S1 and S2. | — |
| S12 | Keyboard navigation (Tab, Shift+Tab, Enter, Escape, Space, arrows) | UNVERIFIED | Generic browser behaviour. | — |
| S13 | Access keys used by MediaWiki (e, h, m, d, u, w, t, c, r, x, z, q, f, j, k, l, y, n, ., o, p, s, v, i, b, =, +) | MISSING | These are the real MediaWiki shortcuts. The existing page lists none of them. | Help:Keyboard_shortcuts; jquery.accessKeyLabel.js |
| S14 | Modifier for access keys: Ctrl | WRONG | Modifier depends on browser: Firefox and Chrome on Windows/Linux use Alt+Shift or Alt; macOS uses Ctrl+Option. | jquery.accessKeyLabel.js (lines 38–78) |

### Facts in the existing pages that are correct (for reference)

- Vector 2022 is the default skin; Wikipedia and other Wikimedia sites use MediaWiki (the Wikimedia part is a general fact, not checked in this run).
- The login flow via `meta=tokens&type=login` and `clientlogin` is the current approach (A12).
- VisualEditor and a wikitext source editor both exist.
- Watchlist, recent changes, categories and what-links-here exist as features (see `1.46/features.md`).
