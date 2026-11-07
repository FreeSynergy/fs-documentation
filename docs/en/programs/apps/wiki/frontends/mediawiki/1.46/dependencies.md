# MediaWiki 1.46 — Dependencies on our components

Purpose: list which UI components and which operations of our text contract (`/srv/FreeSynergy/fs-interfaces/schema/texts.capnp`, DRAFT 0.1, 2026-11-06) a frontend in the MediaWiki style needs.

## Contract as it stands (texts.capnp, interface `Texts`)

Operations present: `supportReport`, `create`, `edit`, `move`, `delete`, `get`, `getByPath`, `list` (prefix + cursor), `find` (term + cursor), `links`, `backlinks`, `importText`, `exportText`, `subscribe`, `moveFolder`, `editIf` (compare-and-set on `revision`).

Entry shape: `TextEntry` with `envelope` (AS2), `path`, `document` (JSON), `revision`. Links: `LinkRow` with `source`, `target` (path), `at`.

## UI components needed (MediaWiki style) and what they need from the contract

| UI component (MediaWiki equivalent) | Needs | Provided by texts.capnp | Gap |
|-------------------------------------|-------|--------------------------|-----|
| Page view (read) | get by id or path, rendered content | `get`, `getByPath`, `exportText` (for Markdown or HTML) | Rendering to HTML is not in the contract; `exportText` takes a media type, so `text/html` must be supported by the provider |
| Page editor (source) | get, edit with compare-and-set | `get`, `editIf` | none for basic editing |
| Edit conflict handling | revision number, conflict reason | `editIf` (`conflict:` prefix) | Reason text is a string; no machine-readable conflict field. Acceptable if the prefix is a stable contract. |
| Create page | create with path and Markdown | `create` | Create takes Markdown; the document form is not accepted. Confirm with the owner. |
| Move / rename page | move with link follow | `move`, `moveFolder` | none |
| Delete page | delete by id | `delete` | Delete is final in the contract; no trash or undelete operation (MediaWiki has delete and undelete) |
| Page history (revision list) | list of past revisions with author and time | none | Missing. `TextEntry` has only the current revision number. |
| Diff between two revisions | get a revision by number, compare | none | Missing. |
| Restore older revision | get old revision, write it as new | none | Missing. |
| Recent changes list | change feed with filters | `subscribe` (ChangeListener) | The contract has no query for "recent changes" with a time window and filter; `subscribe` gives events, not a list. |
| Watchlist | per-user watch set, list of watched texts, watch and unwatch | none | Missing: watch, unwatch, list, and user identity in the contract. |
| Talk (discussion) page per text | paired talk text, namespace model | none | Missing. The contract has paths only; a talk namespace or pairing rule is needed. |
| Namespaces | list of namespaces, namespace of a path | none (prefix in `list`) | Missing as an explicit concept. Prefix listing can emulate it, but not the namespace rules. |
| Categories | list of categories of a text, members of a category | none | Missing. |
| Category page | category membership list | none | Missing. |
| Templates (transclusion) | list of templates used by a text, transclusion dependencies | none | Missing. The contract has links only, not transclusions. |
| Backlinks | pages that link to a text | `backlinks` | none |
| What links here (special) | backlinks with location | `backlinks` (`LinkRow.at`) | none |
| Redirects | redirect source and target | none | Missing. |
| Search | title and full text, paged | `find` | Missing: search result snippet and highlight. Paging is present. |
| Search suggestions (typeahead) | prefix search, fast | `list` with prefix, or `find` | Prefix title search as a separate operation is not in the contract. |
| Special pages (lists of orphans, missing links, long pages) | server-side queries | none | Missing: these are reports; a report operation is needed if we want them. |
| Upload file / media | upload binary, list files, file page | none | Missing: texts.capnp is text-only. Files need their own contract or use `fs-*` file library. |
| Protect page (lock editing) | per-page protection level and set | none | Missing. |
| User rights and blocks | user roles, block state | none | Out of scope for this contract; comes from the identity side. |
| Preferences (text size, width, theme, language) | per-user settings | none | Out of scope for texts; belongs to the frontend or user settings. |
| Print view | rendered page for print | `exportText` (HTML) | Same as page view. |
| Live updates | change events | `subscribe` | Event payload fields are defined in `common.capnp` (not read in this run). |
| Import and export (Markdown) | import and export by media type | `importText`, `exportText` | none |
| Version/support | provider info | `supportReport` | none |

## Summary of gaps in texts.capnp

Operations or concepts needed by a MediaWiki-style frontend that the contract lacks:

1. Revision history: list revisions of a text, get a past revision, compare two.
2. Restore a past revision.
3. Undelete or trash.
4. Watchlist: watch, unwatch, list (with user identity).
5. Talk or discussion pages and their pairing rule.
6. Namespaces as a concept.
7. Categories: categories of a text and members of a category.
8. Templates or transclusion dependencies.
9. Redirects.
10. Recent changes query (time window, filter), not only a subscription.
11. Search results with snippets and highlight.
12. Prefix or title search for suggestions.
13. Protection state of a text.
14. Files and media (outside texts; needs its own contract).
15. Special or report queries (orphans, missing targets).
16. Rendered HTML as a first-class output (currently only through `exportText` media type).

Items 1, 2, 10, 11 are the most visible in the UI and should be decided first. Items 5 and 6 need a naming rule, not only an operation. Items 4 and 5 depend on the identity model, which is outside the texts contract.

## Notes

- This list is what the MediaWiki style needs. Other frontend styles may need less. Keep it as input to the owner's decision, not as a list of required changes.
- Rules from texts.capnp: evolution is append-only, so the gaps can only be filled by new operations.
