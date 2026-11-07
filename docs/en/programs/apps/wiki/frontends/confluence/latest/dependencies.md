# Confluence (Cloud, latest) · Dependencies

What a frontend "in the Confluence style" on top of our wiki engine needs from the engine. Contract: `fs-interfaces/schema/texts.capnp`, DRAFT 0.1 (2026-11-06), interface `Texts`, plus `common.capnp` for `Envelope`, `Change`, `ChangeListener`, `Cursor`, `Problem`.

## 1. Operations of `texts.capnp` that map to Confluence features

| texts.capnp operation | Confluence feature it serves |
|-----------------------|------------------------------|
| `create(path, markdown)` @1 | Create page (no template parameter) |
| `edit(id, document)` @2 | Save in editor |
| `editIf(id, revision, document)` @15 | Save with conflict detection (compare-and-set) |
| `move(id, path)` @3 | Move page (links follow) |
| `moveFolder(prefix, path)` @14 | Move a page with its subtree |
| `delete(id)` @4 | Delete (hard delete; no trash) |
| `get(id)` @5, `getByPath(path)` @6 | Open a page, breadcrumbs from path |
| `list(prefix, cursor)` @7 | Sidebar tree and child lists (prefix = path) |
| `find(term, cursor)` @8 | Search (no snippet, no filter) |
| `links(id)` @9, `backlinks(path)` @10 | Details panel links, "linked pages" |
| `importText(path, mediaType, text)` @11 | Import Markdown or other text |
| `exportText(id, mediaType)` @12 | Export (text formats only; see gaps) |
| `subscribe(listener)` @13 | Live updates (`Change` created/updated/deleted) |
| `supportReport()` @0 | Capability check (unsupported = `Problem` with status 501) |

## 2. UI components and what they need

| UI component | Needs | Covered by contract | Status |
|--------------|-------|---------------------|--------|
| Top bar Search | Search with snippets, filters by space or type | `find` (TextPage) | Partial: no snippets, no filters |
| Top bar Create | Create with template choice | `create` | Partial: no template |
| Top bar Notifications and mentions | Notification feed, mentions | none | Gap |
| Sidebar tree | Children in custom order | `list(prefix)` | Partial: no sibling order field |
| Space selector and space overview | Space as a container with name, key, permissions | none (path prefix only) | Gap |
| Page view | Body from document JSON | `TextEntry.document` | Covered, but no schema for the JSON is referenced |
| Breadcrumbs | Ancestor path | derived from `path` | Covered |
| Header "Last updated" and editor | Last update time and last editor | `Envelope.updated`, `Envelope.attributedTo` | Partial: `attributedTo` may be creator, not last editor |
| Title area: owner, status, classification, views, read time | Owner, status, classification, view count | none | Gap |
| Details panel: labels | Labels | none | Gap |
| Details panel: attachments and linked files | Attachment list, blobs | `Blob` in common.capnp exists, not referenced from texts | Gap |
| Details panel: contributors | Edit history per user | none | Gap |
| Details panel: links | Links and backlinks | `links`, `backlinks` | Covered |
| Version history and diff | List versions, read old versions, restore | `revision` counter only | Gap |
| Comments | Comment threads | none | Gap |
| Watch, favourite, share | Per-user state | none | Gap |
| Permissions and restrictions | Read and write rules per text | none | Gap |
| Trash and restore | Soft delete, restore | `delete` is final | Gap |
| Templates and blueprints | Template store | none | Gap |
| Export to PDF or Word | Binary output | `exportText` returns `Text` | Gap (binary) |
| Presenter mode, page-level layouts | Frontend-only | not needed | Not an engine need |
| Keyboard shortcuts and themes | Frontend-only | not needed | Not an engine need |
| Live updates | Change feed | `subscribe` / `ChangeListener` | Covered; `deleted` carries only the `Uuid` |
| Caller identity for permissions | Who is asking | not in any call | Gap |
| Sibling ordering on drag and drop | Position value | none | Gap |

## 3. What `texts.capnp` lacks (summary)

1. Spaces or other containers above the path tree.
2. Version list, read of past versions, and restore.
3. Trash and restore.
4. Labels or tags.
5. Comments.
6. Permissions, restrictions, watch and favourite state.
7. Template store and template parameter in `create`.
8. Attachments, and binary export (PDF or Word).
9. Sibling order (position) for the sidebar.
10. Search result snippets and filters.
11. Document schema: `document` is "the document as JSON" with no schema id or version.
12. Caller identity and actor on writes.
13. Status, classification and view or read statistics.
14. Blog-post or other content kinds (only text entries exist; the difference is not in the contract).
15. Notifications and mentions.

## 4. Confluence concepts that map to an existing contract field

| Confluence concept | Mapping |
|--------------------|---------|
| Page tree | `path` with `/` separators (`list` prefix) |
| Page ID | `TextEntry.envelope.id` (Uuid) |
| Revision counter | `TextEntry.revision` (for editIf) |
| Last update | `Envelope.updated` |
| Page body representation | `document` (JSON), not Confluence storage format |

## 5. Note on Confluence storage format

Confluence's own body formats (`storage`, `atlas_doc_format`, `wiki`) appear in the v2 API [S4]. Our contract stores the document as JSON and exchanges Markdown through import and export. We do not need to implement any Confluence format; the earlier draft's claim that Confluence uses wiki markup as its main editor is unverified for Cloud.

Sources: [index.md](../index.md) S-numbers (S4 for body formats).
