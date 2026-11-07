# Wiki.js 3.1.1 — dependencies

Which UI components a frontend "in this style" needs, and which operations of our `texts.capnp` they call. Contract read: `/srv/FreeSynergy/fs-interfaces/schema/texts.capnp` (DRAFT 0.1, 15 methods on `Texts`). Only `texts.capnp` was read; `common.capnp` was read for `Cursor`, `Change`, `ChangeListener`, `Problem`, `Envelope`. Other contracts in `fs-interfaces/schema/` (files, history, people, groups, …) were not checked, so a gap below may be covered there. Marked "not checked here".

## A. UI components needed

| # | Component | What it shows or does | Wiki.js reference |
|---|-----------|----------------------|-------------------|
| 1 | App shell | header, drawer, content, page rail | `layout.md` |
| 2 | Navigation tree | menu from site navigation, browse menu | `NavSidebar.vue`, `NavBrowseMenu.vue` |
| 3 | Page view | rendered page with title, tags, last edited, TOC | `pages/Index.vue`, `common.page.*` |
| 4 | Editor host | one host, several editors chosen by type | `EditorMarkdown.vue`, `EditorVisual.vue`, `EditorAsciidoc.vue` |
| 5 | Create page dialog | path, editor, locale | `PageActionsCol.vue`, `helpers/editors.js` |
| 6 | Rename / move dialog | tree browser to pick a new path | `TreeBrowserDialog.vue` |
| 7 | Delete dialog and trash | soft delete, restore | `PageDeleteDialog.vue` |
| 8 | History list and version view | list versions; read one | `PageVersion.vue`, `.../history` |
| 9 | Source view | raw source of the stored text | `viewPageSource` |
| 10 | Search | query with filters and paging | `HeaderNav.vue`, `/_search` |
| 11 | Backlinks and links panel | what links here, what this links to | `pages.ts` (`backlinks`, `links`) |
| 12 | Tags | tag list, tag browse | `/_tags` |
| 13 | Live updates | refresh the view when another author saves | `collab.js` (Yjs), not a list refresh |
| 14 | Inbox and watching | notifications; watched pages | `/_inbox/*` |
| 15 | Admin | sites, users, groups, storage, theme | `routes.js` (`/_admin/*`) |
| 16 | Import and export | Markdown in and out | `backend/api/import.ts`, `pages.ts` (render) |

## B. Mapping: UI needs to `texts.capnp` operations

| `texts.capnp` method | Purpose there | Used by UI component |
|----------------------|---------------|----------------------|
| `supportReport` | what the provider can do | 15 (capability checks) |
| `create (path, markdown)` | new page from Markdown | 5 (only for Markdown) |
| `edit (id, document)` | save a page (document as JSON) | 4 |
| `move (id, path)` | rename or move one text; links follow | 6 |
| `delete (id)` | delete | 7 |
| `get (id)` | read a page | 3, 4, 9 |
| `getByPath (path)` | read by path | 3 |
| `list (prefix, cursor)` | list texts under a path | 2 (tree, partly) |
| `find (term, cursor)` | search by term | 10 |
| `links (id)` | outgoing links | 11 |
| `backlinks (path)` | incoming links | 11 |
| `importText (path, mediaType, text)` | import Markdown or other | 16 |
| `exportText (id, mediaType)` | export | 9, 16 |
| `subscribe (listener)` | change feed (`Change` union) | 13 |
| `moveFolder (prefix, path)` | move a folder and its texts | 6 |
| `editIf (id, revision, document)` | save only if nobody else saved first | 4 (conflict handling) |

Notes on the mapping:

- `editIf` is the only save path that protects against a parallel save. Its conflict answer is a text reason starting with `conflict:`, not a typed `Problem` (see section D).
- `subscribe` gives `Change` values with an `Envelope` for created and updated, and only a `Uuid` for deleted. The listener contract has `ended` for a broken feed; a consumer must re-read after resubscribing (`common.capnp`).
- `TextEntry.revision` exists for `editIf` and is never reset. The UI can show it, but there is no list of past revisions.

## C. What `texts.capnp` lacks for this style of frontend

| Gap | Needed by | Wiki.js 3.1.1 has | Suggested addition (append only, ADR 0045 rule) |
|-----|-----------|-------------------|------------------------------------------------|
| Folder list, create, delete | 2, 6 | folder endpoints under `tree/folders` | `listFolders`, `createFolder`, `deleteFolder`; or a `Node` union in `list` |
| Past versions: list, read, restore | 8 | `history`, `versions` endpoints | `history (id, cursor)`, `revisionAt (id, revision)`, `restore (id, revision)` |
| Trash: list deleted, restore | 7 | `pages/deleted`, `restore` endpoints | `listDeleted (prefix, cursor)`, `restore (id)` |
| Editor type on create and on save | 4, 5 | `editor` field on page input | `create` with an editor id; `edit` already takes JSON, so the type must be in the document or as a field |
| Locales: per text and per path | 3, 5, 10 | `locale` on page; locale relations | `locale` field on `TextEntry`; `localeRelations (id)` |
| Search filters and ordering | 10 | `tags`, `editor`, `publishState`, `creatorId`, `orderBy` | `find` with a filter struct and `orderBy` |
| Tags: list, add, count | 12 | tag endpoints and counts | `tags (prefix)`, `setTags (id, tags)` |
| Publish state | 3, 10 | `publishState` filter, unpublished warning | field on `TextEntry` or in the document, with a `publish` method |
| Title and description as fields | 3, 10 | `title`, `description` on page input | today only inside `document` (format not defined in the contract) |
| Rendered HTML or preview | 3, 9 | `render` endpoint | `render (id)` returning HTML; or state that `exportText` takes `text/html` |
| Watch and unwatch a text | 14 | watch endpoints | `watch (id)`, `unwatch (id)` |
| Comments | 3 (side panel) | comment endpoints | not in `texts`; a separate contract |
| Ratings | 3 | rating endpoints | not in `texts`; a separate contract |
| Suggested edits and review queue | 14 | approvals endpoints | not in `texts`; a separate contract |
| Page permissions and access rules | 2, 3, 6 | `userPermissions` endpoint, groups and page rules | depends on people and groups contracts (not checked here) |
| Page lock with password | 3 | `unlock` endpoint | `unlock (id, secret)` (only if we keep the feature) |
| Navigation menu | 2 | navigation endpoints | not in `texts`; a separate contract |
| Assets used by a page | 3, 16 | asset endpoints | `files.capnp` (not checked here) |
| Live co-editing | 4, 13 | Yjs websocket | `editIf` gives save-time conflicts only. Real-time editing needs its own channel. |
| Drafts (unsaved text) | 4 | local buffer | not in contract; keep on the client |
| Typed errors on `editIf` | 4 | RFC 9457 `Problem` in common | the conflict is a text prefix `conflict:`; change to a typed `Problem` with status 409 |

## D. Inconsistencies noticed in `texts.capnp` (not changed, report only)

1. `editIf` reports conflicts as a text reason starting with `conflict:`. `common.capnp` defines `Problem` (RFC 9457 shape) for errors. Both cannot be the rule. Suggest the `Problem` form.
2. `subscribe` says nothing about which texts it reports (all, or one prefix). The UI needs a filter by prefix for the tree and for a page view.
3. `delete (id)` has no way to say "already gone". Retries may return an error. Unverified: how the provider answers a second delete.
4. `list` and `find` take a `Cursor` but the contract does not say what an empty `next` means for the caller other than "start or end" (see `common.capnp`, which does say so).

## E. Operations of `texts.capnp` a Wiki.js-style frontend does not need

None are required by the UI in section A. `importText` and `exportText` are needed only for the import and export features (16).

## F. Minimal set for a first version

To show pages, edit them with conflict protection, move, delete, search, and show links, the frontend needs: `get`, `getByPath`, `list`, `find`, `create`, `editIf`, `move`, `delete`, `links`, `backlinks`, `subscribe`, `supportReport`. Everything in section C is a second step.
