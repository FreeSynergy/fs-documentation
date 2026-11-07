# Tango: dependencies for a frontend in this style

Target: a frontend in the style of Tango (capture-to-guide documentation with step lists, shared views and a team library) on top of the FreeSynergy wiki engine. Contract: `fs-interfaces/schema/texts.capnp` (DRAFT 0.1, 2026-11-06, 0 consumers yet).

## UI components needed

1. Step list editor: ordered list of steps, drag reorder, add step at position, per-step title, description, image.
2. Image annotation: arrows, boxes, text, zoom, blur region (blur optional, Pro-level in Tango).
3. Guide view: scroll view, slideshow view, embed view.
4. Guided walkthrough (optional): step-by-step overlay on the target app. Needs an external runtime (browser extension); not a texts.capnp concern.
5. Share/export panel: link, copy HTML, export Markdown/HTML/PDF.
6. Team library: list with multi-select and bulk actions (move, duplicate, share, delete).
7. Branding panel: logo, accent colour, badge toggle.
8. Undo/redo.

## texts.capnp operations that map to these

| Need | Operation | Note |
|---|---|---|
| Load a guide | `get`, `getByPath` | `document` is JSON, the content is opaque to the contract |
| Lists, folder view | `list(prefix, cursor)` | path-based folders |
| Search | `find(term, cursor)` | |
| Create guide | `create(path, markdown)` | takes Markdown, not a step document |
| Save edits | `edit(id, document)`, `editIf(id, revision, document)` | `editIf` needed for concurrent editors (single provider process only) |
| Move, rename | `move`, `moveFolder` | links follow |
| Delete | `delete` | |
| Export | `exportText(id, mediaType)` | returns text only; PDF is binary and not covered |
| Import | `importText(path, mediaType, text)` | Markdown in |
| Links | `links`, `backlinks` | |
| Live updates | `subscribe(listener)` | |

## What texts.capnp lacks (gaps)

1. **Binary assets.** No upload, get, or delete of images or files. Steps with screenshots need an asset store, and a reference from `document` to the asset. Not in the contract.
2. **Step model.** No definition of steps, screenshots, highlights or positions. Only "the document as JSON". A shared step schema is missing if guides are to be portable.
3. **Capture session.** No operation to start, pause, complete or discard a recording. (Capture likely lives in a client; the contract would still need to accept the result.)
4. **Version history.** `revision` is a counter only. No list of past revisions, no read of revision N, no restore.
5. **Sharing and visibility.** No share links, embed tokens, public/private flags, expiry.
6. **Permissions.** No roles or per-text rights. Admin-only settings (branding) absent.
7. **Branding/theme settings.** No operation to store logo or colours per workspace.
8. **Export formats.** `exportText` is text-only; no PDF or HTML bundle with assets.
9. **Walkthrough/state.** No "viewer progress" or events for guided views. `events.md` is "if needed" in ADR 0012.
10. **Analytics.** No view counts or insights.
11. **Translations and multi-path (branching) structure.** Not modelled.
12. **Templates.** No template operation.

## Plan-gated features

Not a contract matter. Keep in our product rules, not in texts.capnp.
