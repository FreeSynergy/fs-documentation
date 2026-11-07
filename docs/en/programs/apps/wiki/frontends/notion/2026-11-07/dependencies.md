# Notion — dependencies for a frontend in this style

What a frontend "in the style of Notion" needs from our components. It is based on the features in [features.md](features.md) and the operations in `fs-interfaces/schema/texts.capnp` (DRAFT 0.1, 2026-11-06).

## Current texts.capnp (summary)

Interface `Texts` (fs-wiki contract, DRAFT 0.1):

| Op | Signature (short) | Notes |
|----|-------------------|-------|
| `supportReport` | → report | |
| `create` | path, markdown → text | path + Markdown in |
| `edit` | id, document → text | whole document |
| `move` | id, path → text | links follow |
| `delete` | id → () | semantics (trash or hard delete) not stated |
| `get` | id → found, text | |
| `getByPath` | path → found, text | |
| `list` | prefix, cursor → page | path prefix list, cursor paged |
| `find` | term, cursor → page | term only |
| `links` / `backlinks` | id / path → rows | link rows: source, target, at |
| `importText` | path, mediaType, text → entry | |
| `exportText` | id, mediaType → text | |
| `subscribe` | listener → subscription | change stream of `ChangeListener` |
| `moveFolder` | prefix, path → moved | whole subtree |
| `editIf` | id, revision, document → text | compare-and-set on `revision` |

`TextEntry`: `envelope` (AS2 Article or Note), `path`, `document` (JSON, authoritative), `revision` (UInt64). `Envelope` (common.capnp) has `published`, `updated`, `attributedTo`, `to`, `cc`, `inReplyTo`, `name`, `context`, `sensitive`.

## Components a Notion-style frontend needs

| UI component | Needs | Covered by texts.capnp? |
|--------------|-------|-------------------------|
| Sidebar tree (pages, sections, favourites) | tree of paths, nesting, order | partly: `list` by prefix, `moveFolder`. No order, no favourite, no sections |
| Page list and search | list, search with filters and sort | partly: `list`, `find` (term only, no filters/sort) |
| Block editor | typed block tree, block ids, insert/move/update block | no: the document is opaque JSON; no block model in the contract |
| Slash menu, Markdown input | block type registry, transforms | no (frontend-side; needs block schema) |
| Inline mentions, page links | link rows with positions | partly: `links`, `backlinks` (`at` is text). No mention rows |
| Rich text | spans with marks and links | no: no schema for spans |
| Database views (table, list, board, calendar, gallery, chart) | collections, schema, rows, views with filter/sort/group | no: no database or view concept |
| Properties (status, select, date, relation, rollup, formula) | property types, values, relations | no |
| Comments and discussions | comment objects bound to a text or block | no |
| Page settings (font, width, icon, cover, TOC) | per-text presentation fields | no: would fit into `document` JSON only if specified |
| Trash and restore | deleted state, restore, list trashed | no: `delete` semantics unknown; no restore op |
| Version history | list of revisions with timestamps and authors | no: only `revision` counter; no history read |
| Permissions and sharing | ACL per text, roles | no; `Envelope.to/cc/audience` is a message-audience field, not a permission model |
| Notifications and live updates | change stream | yes: `subscribe` with `ChangeListener`; event granularity not stated |
| Import and export | Markdown and other media types | yes: `importText`, `exportText` |
| File and media uploads | blob storage | not in this contract; `common.capnp` has a `Blob` interface |
| Templates | template texts | no |
| Keyboard, layout, theme | none | out of scope for the contract |

## Gaps in texts.capnp (for the fs-wiki owner)

1. **Block model.** No typed block tree, no block ids, no child ordering. `document` as opaque JSON cannot support block operations (insert after, move, update one block) or live editing per block.
2. **Database model.** No collections, schemas, rows, properties or views.
3. **Views and filters.** No view objects. `find` takes a term only.
4. **Comments.** None.
5. **Permissions and sharing.** No ACL, no roles, no per-user visibility.
6. **Trash and restore.** `delete` does not say whether it is reversible. No `restore`, no `listTrashed`.
7. **History.** No revision listing, no revision read, no diff.
8. **Authorship.** `TextEntry` has no `createdBy`, `lastEditedBy` (only `Envelope.attributedTo` on the envelope; not defined as author of each revision).
9. **Search options.** No sort, no filters, no pagination order guarantees stated.
10. **Presentation.** Icon, cover, font, width: no fields.
11. **Mentions.** Only links; no typed mention rows.

These gaps are facts about the contract, not decisions. The fs-wiki owner decides how to close them (ADR process).

## Operation mapping for a Notion-style frontend

| Frontend action | texts.capnp operation today | Gap |
|-----------------|-----------------------------|-----|
| Open page | `getByPath` or `get` | none for read |
| Save page | `editIf` (with `revision`) | block-level save needs block ops |
| New page | `create` | none for simple text |
| Move page | `move`, `moveFolder` | none for simple case |
| Delete page | `delete` | reversibility unknown |
| Search | `find` | filters and sort |
| Backlinks panel | `backlinks` | none |
| Live update | `subscribe` | granularity unknown |
| Export | `exportText` | none |
| Database view | none | whole model missing |
| Comments | none | whole model missing |
| Version history | none | whole model missing |

## Notes

- `editIf` is atomic inside one provider process only (texts.capnp comment). Multi-node setups need another plan.
- The contract is DRAFT 0.1 with no consumers yet (texts.capnp header).
