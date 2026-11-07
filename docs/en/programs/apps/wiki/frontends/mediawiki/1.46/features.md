# MediaWiki 1.46 — Features (what it can and cannot do)

Version: 1.46.2. Feature list checked against https://www.mediawiki.org/wiki/MediaWiki_1.46, https://raw.githubusercontent.com/wikimedia/mediawiki/REL1_46/RELEASE-NOTES-1.46 and the REL1_46 source tree (https://github.com/wikimedia/mediawiki/tree/REL1_46).

"Core" means: present in the MediaWiki core repository. "Extension" means: a separate repository loaded by configuration.

## Can (core)

| Function | Core? | Evidence |
|----------|-------|----------|
| Read, create and edit pages in wikitext | yes | Action API module `edit` (`includes/Api/ApiEditPage.php`) |
| Preview an edit before saving | yes | Editing toolbar tooltip `tooltip-preview` (`languages/i18n/en.json`) |
| Show the difference between revisions | yes | `compare` REST route and `tooltip-diff` |
| Revision history | yes | `history` tooltip `tooltip-ca-history`; REST `/v1/page/{title}/history` (`coreRoutes.json`) |
| Undo several revisions at once (adds an automatic summary) | yes, new in 1.46 | RELEASE-NOTES-1.46, "New user-facing features" |
| Rollback by the last editor | yes | `ApiRollback.php`; token type `rollback` (`ApiQueryTokens.php`) |
| Move (rename) a page, with redirect and talk page | yes | `ApiMove.php`; 1.46 can move over an existing talk page (RELEASE-NOTES-1.46) |
| Delete and undelete | yes | `ApiDelete.php`, `ApiQueryDeletedRevisions.php` |
| Protect and unprotect | yes | `ApiProtect.php` |
| Block and unblock users | yes | `ApiBlock.php`, `ApiUnblock.php` |
| Change user rights (groups) | yes | `ApiUserrights.php`; token type `userrights` |
| Watchlist (watch, unwatch, list) | yes | `ApiWatch.php`, `ApiQueryWatchlist.php`, `ApiQueryWatchlistRaw.php`; `tooltip-ca-watch`, `tooltip-pt-watchlist` |
| Recent changes list with filters | yes | `ApiQueryRecentChanges.php`; API:RecentChanges |
| Categories (membership and listing) | yes | `ApiQueryCategories.php`, `ApiQueryCategoryMembers.php` |
| Upload files | yes | `ApiUpload.php`; `tooltip-t-upload` |
| Full-text and title search | yes (basic) | `ApiQuerySearch.php`, `ApiQueryPrefixSearch.php`; search backend choice unverified |
| Talk (discussion) page per content page | yes | `tooltip-ca-talk`, `tooltip-pt-mytalk` (namespace model) |
| Redirects | yes | REST `RedirectHandler` (coreRoutes.json) |
| Language links between pages | yes | REST `/v1/page/{title}/links/language` (coreRoutes.json) |
| Personal preferences | yes | `tooltip-pt-preferences`; Vector preferences list (`doc/configuration/configuration.md`) |
| Print version | yes | `tooltip-t-print` |
| Permanent link to a revision | yes | `tooltip-t-permalink` |
| Bot passwords for scripts | yes | `includes/User/BotPassword.php` |
| Special pages (lists, admin tools) | yes | Special pages exist; full list unverified in this run |
| Interface language switch (`uselang`) | yes | RELEASE-NOTES-1.46 preserves `uselang` on preview |
| Watchlist labels | yes, but off by default | `$wgEnableWatchlistLabels` default `false` (RELEASE-NOTES-1.46) |

## Cannot (core), or only with an extension

| Function | Status | Evidence |
|----------|--------|----------|
| OAuth login for third-party tools | extension | no OAuth module in REL1_46 core tree; API:Login recommends OAuth "if it is available" |
| LDAP login | extension | no LDAP file in REL1_46 core tree |
| Notifications (alerts, email digests) | extension (Echo) | https://www.mediawiki.org/wiki/Extension:Echo |
| Webhooks (HTTP push to a URL) | not in Echo | Echo page describes push settings and notifications; no URL webhook feature found (see `../../changelog.md`) |
| Syntax-highlighted source editor | extension (CodeMirror) | https://www.mediawiki.org/wiki/Extension:CodeMirror |
| Visual (WYSIWYG) editor | extension (VisualEditor) | https://www.mediawiki.org/wiki/VisualEditor/Portal/Keyboard_shortcuts |
| GraphQL endpoint | not in core | no GraphQL file in REL1_46 tree; existing page wrong |
| Real-time co-editing of one page | unverified | not found in any official page read in this run |
| Drag and drop of files into the source editor | unverified | not checked |
| Per-user "dark mode" choice | yes, in Vector 2022 | `vector-theme` preference: day, night, os (`doc/configuration/configuration.md`) |

## Editors

| Editor | Core? | Facts |
|--------|-------|-------|
| Wikitext source editor | yes (page form) | Plain text area with an edit toolbar and access-key save/preview (`shortcuts.md`). The CodeMirror extension adds highlighting, line numbers, search, go-to-line, bracket matching and a shortcut help dialog (https://www.mediawiki.org/wiki/Extension:CodeMirror). |
| VisualEditor | extension | Rich-text surface with Ctrl+B, Ctrl+I, Ctrl+K, Ctrl+Z, Ctrl+Shift+Z, template dialog, citations (https://www.mediawiki.org/wiki/VisualEditor/Portal/Keyboard_shortcuts). Can be disabled per wiki. |
| CodeMirror as default | from 1.47 (per extension page) | "from MediaWiki 1.47, most integrations use CodeMirror by default, except VisualEditor's Code block dialog" (https://www.mediawiki.org/wiki/Extension:CodeMirror). 1.47 is not released as of 2026-11-07. |

## Notes for our frontend

- Do not promise VisualEditor-equivalence. It is a large separate codebase.
- Plan the editor as a plain text editor with a toolbar. The toolbar actions map to wikitext snippets. Keyboard shortcuts for those actions are our own design, not MediaWiki's (see `shortcuts.md`).
- "Source editor" in the existing page described features (line numbers, syntax colouring, diff in a split view). The line numbers and highlighting come from CodeMirror, not core. The split-view claim is unverified.
