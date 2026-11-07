# Wiki.js 3.1.1 — features

Verified against the 3.1.1 source. Sources are given per row. "Unverified" means the feature was not confirmed in source or official docs.

## Pages

| Feature | Can | Source |
|---------|-----|--------|
| Create page at path with editor | yes; editor is one of the site's active editors | `backend/api/pages.ts` (`POST /sites/:siteId/pages`), `backend/api/schemas/page.ts` (`editor` field) |
| Edit page | yes; `PATCH` for metadata, `PUT .../editor` for content | `backend/api/pages.ts` |
| Rename / move | yes; `PUT .../path` | `backend/api/pages.ts` |
| Duplicate | yes (UI action "Duplicate Page") | `frontend/src/components/PageActionsCol.vue` |
| Delete | yes; soft delete, listed under `.../pages/deleted`, restore endpoint exists | `backend/api/pages.ts`, locale string `common.page.delete` ("can be restored from the administration area") |
| Version history | yes; list, read a version, read by version ID | `backend/api/pages.ts` (`.../history`, `.../history/:versionId`, `/sites/:siteId/versions/:versionId`) |
| View page source | yes ("Page Source" action) | `PageActionsCol.vue` |
| Re-render | yes ("Rerender" action and endpoint `.../render`) | `PageActionsCol.vue`, `backend/api/pages.ts` |
| Convert page to another editor | yes ("convertPage" action in the page actions menu) | `PageActionsCol.vue` |
| Publish state | yes; search filter `publishState`; unpublished warning | `backend/api/pages.ts`, locale `common.page.unpublishedWarning` |
| Password-locked page | yes; unlock endpoint `.../unlock` | `backend/api/pages.ts`, locale `common.page.locked` |
| Aliases and ID links | yes; `/a/:alias` and `/i/:pageId` routes | `frontend/src/router/routes.js` |
| Page ratings (thumbs up/down) | yes | locale `common.page.ratePage`, `ratingThumbsUp` |
| Watch a page | yes; `watching` routes | `frontend/src/router/routes.js` (`/_inbox/watching`), locale `common.page.watch` |
| Backlinks and outgoing links | yes; `.../backlinks`, `.../links` | `backend/api/pages.ts` |
| Tags | yes; tag browse page `/_tags`; search filter `tags` with `tagsMatch` | `routes.js`, `backend/api/pages.ts` |
| Locales | yes; site locales, locale relations (`.../locale-relations`) | `backend/api/pages.ts`, `backend/models/sites.ts` |
| Table of contents | yes; position is a theme setting | `backend/models/sites.ts` (`tocPosition`) |
| Print format | yes; print button is a theme setting | `backend/models/sites.ts` (`showPrintBtn`), locale `common.page.printFormat` |
| Page progress bar | yes; theme setting | `backend/models/sites.ts` (`showPageProgress`) |
| Suggested edits by readers | yes; suggestions go to an approval queue | locale `common.actions.suggestEdits`, `backend/models/approvals.ts`, route `/_inbox/review` |
| Comments | yes; admin area has a comments section | `backend/api/comments.ts`, `routes.js` (`:siteid/comments`) |
| Page ownership and lifecycle | yes | `.claude/rules/page-lifecycle.md`, `backend/api/pageOwners.ts`, `backend/api/pageLifecycle.ts` |

## Editors

Each editor has an ID that is stored with the page. A site lists which editors are active (`backend/models/sites.ts`, `editors` block).

| Editor ID | What it is | Source |
|-----------|-----------|--------|
| `markdown` | Monaco-based Markdown editor with a live preview and a left "insert" rail | `frontend/src/components/EditorMarkdown.vue` |
| `visual` | ProseMirror-based rich-text editor with slash menu, tables, tabs, and task lists | `frontend/src/editor/visual/` |
| `asciidoc` | Monaco-based AsciiDoc editor | `frontend/src/components/EditorAsciidoc.vue` |
| `excalidraw` | Drawing editor (Excalidraw 0.18.1), with collaboration | `frontend/src/components/EditorExcalidraw.vue`, `frontend/src/editor/excalidraw/` |
| `blog` | Blog page type with its own listing | `frontend/src/components/EditorBlog.vue` |
| `feedback` | Feedback board: ideas, categories, votes | `frontend/src/components/EditorFeedback.vue` |
| `redirect` | Page that sends the reader elsewhere; never searchable | `backend/api/schemas/page.ts` |

Docs list the same eight editors (https://docs.js.wiki/guide/editors). The docs page names "Live Notes Editor" as one of them; in the source, live notes are a separate route (`/n/`) and not an entry in the `editors` block.

### Markdown editor features that were verified

- Keyboard shortcuts for bold, italic, header level, and save (see `shortcuts.md`).
- Snippet-style inserts for abbreviations and other blocks (`EditorMarkdown.vue`, `snippetEscape`).
- Completions for links, tags, fences, and blocks (`frontend/src/composables/linkCompletions.js`, `tagCompletions.js`, `fenceCompletions.js`, `blockCompletions.js`).
- Image properties dialog over images (`frontend/src/composables/imagePropertiesDialog.js`).
- Real-time collaboration through the Yjs binding for Monaco (`y-monaco`).

### Visual editor features that were verified

- Block and mark commands listed in `shortcuts.md`.
- Slash menu (`frontend/src/editor/visual/slash.js`).
- Tabs block (`nodeviews.js`, locale `editor.visual.tabs.*`).
- Collaboration through Yjs (`frontend/src/editor/visual/collab.js`).

### Other features that were not verified

Snippets library, emoji picker menu (a file exists, `EditorEmojiMenu.vue`, but its behaviour was not read), table editor UI details, math and diagram rendering options, and the visual editor's markdown import/export round trip. Unverified.

## Navigation and search

| Feature | Can | Source |
|---------|-----|--------|
| Full-text search | yes; query plus filters `path`, `locales`, `tags`, `tagsMatch`, `editor`, `publishState`, `creatorId`, `authorId`, `orderBy`, `orderByDirection`, `offset`, `limit` | `backend/api/pages.ts` (`GET /sites/:siteId/pages/search`) |
| Suggest / autocomplete for pages | yes; `.../pages/suggest` and `.../pages/suggest-path` | `backend/api/pages.ts` |
| Browse tree | yes; `.../tree`, `.../tree/browse`, `.../tree/pages`, `.../tree/graph` | `backend/api/tree.ts` |
| Navigation editor | yes; admin "Navigation" and "Edit Nav" button in sidebar | `routes.js`, `frontend/src/components/NavEditMenu.vue` |
| Site map | yes; locale `common.header.siteMap` | locale file |
| Folder create / move / delete | yes; `.../tree/folders` endpoints | `backend/api/tree.ts` |
| File manager (assets) | yes; drag and drop move in 3.0.1 | https://github.com/requarks/wiki/releases/tag/3.0.1 |

## Accounts and access

| Feature | Can | Source |
|---------|-----|--------|
| Groups with page rules | yes | `routes.js` (`groups`), `backend/api/groups.ts` |
| Personal access tokens with scopes (`pages`, `assets`, `comments`, `glossary`, `navigation`, `approvals`, `profile`, `mcp`) | yes | `frontend/src/helpers/personalTokens.js` (mirrors `backend/models/personalTokens.ts`) |
| Profile sections (info, avatar, auth, groups, notes, tokens, notifications) | yes | `routes.js` (`/_profile/*`) |
| Two-factor and passkeys | yes, in account settings | `backend/models/passkeys.ts`, `backend/api/personalTokens.ts` comment ("passwords, 2FA, passkeys") |
| SCIM | yes; admin section and `/_scim` endpoint | `routes.js` (`scim`), `backend/api/schemas/scim.ts` |

## What Wiki.js 3.1.1 cannot do (verified or stated in the source)

| Limit | Source |
|-------|--------|
| No GraphQL endpoint | No `graphql` file or dependency in the 3.1.1 tree |
| Personal tokens cannot reach admin routes | `backend/index.ts` (bearer hook: tokens refused on routes without a scope), `.claude/rules/personal-access-tokens.md` |
| Personal tokens are accepted only on `/_api` and `/_mcp` | `backend/index.ts` |
| API keys cannot act for a user (no user attribution) | docs https://docs.js.wiki/dev/api |
| Single-process atomicity assumptions for some writes | `backend/CLAUDE.md` (HA set, advisory lock on startup) |

## Not verified (old pages claimed these; treat as unknown)

- Markdown front matter as a user-facing feature (only seen as a storage detail in `helpers/storageFiles.ts`).
- Auto-save interval.
- Keyboard shortcuts for a command palette, global search, file tree, live preview toggle, and new page (none found in the source).
- Plugin system for editors and renderers beyond the storage and auth modules.
- Mermaid, KaTeX, Kroki, and syntax-highlighting plugin names. The source has `frontend/src/renderers/modules/katex.js` and `kroki.js`; Mermaid was not checked.
