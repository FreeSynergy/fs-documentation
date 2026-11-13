# Confluence (Cloud, latest) · Gaps against our program

What our wiki program cannot do for the workflows of [workflows.md](workflows.md), and what is needed. Tests that these gaps fail: [acceptance.md](acceptance.md).

## Our state, as read (2026-11-13)

Read from `/srv/FreeSynergy/fs-wiki` (read only): `README.md`, `DESIGN.md`, `crates/fs-wiki-app/src/` (`gui.rs`, `mode_admin.rs`, `mode_reader.rs`, `args.rs`, `admin/*.rs`), `crates/fs-wiki-core/src/describe/support.rs`.

- **Version:** the workspace `Cargo.toml` says `0.0.6` and the README says latest tag `v0.0.6`; `DESIGN.md` still speaks of version 0.5.0. A version 0.0.8 or 0.0.9, as named in the assignment, is **[nicht belegt]** in the files read. The git history of the repo could not be read here, so a newer state may exist on another branch.
- **Two window modes.** The **default** is the generated Admin window (`mode_admin.rs`): one view per data type (Pages, Folders, History, Trash, Links), built from type descriptions; each command is a form with typed fields. The **`--reader`** mode (`mode_reader.rs`) is the older documentation reader: page tree, reading, links, back, search, Markdown text editor with Save, Export, draft backup. [DESIGN.md]
- **Words** in the Admin window are derived from translation keys ("Redirect to"); unknown keys show as themselves (`admin/say.rs`).
- **Text editor component** exists (`fs-components-text-editor`) but is **not wired** into the Admin window; multiline text is a plain input there.
- **Commands carried out** (`support.rs`): Page create, import, createFromTemplate, change, move, setTemplate, setRedirect, reorder, trash, delete, find, search, resolve, export; Folder find, create, rename, move, reorder, delete; Revision find, get, restore, purge; TrashEntry find, restore, purge; Link find. `purge` and `purgeRevision` need a hub; without one the answer is "unavailable".
- **Described but not carried out:** share, unshare, comment, openTalkPage, attach, detach, setLabels, watch, unwatch, createDatabase, joinSession, guides, embed, tags, canvas, unlinkedMentions. The Admin frontend shows every described command as a live button, so an uncarried command is a button that ends in an error.
- Refusals such as "path taken", "conflict", "not empty" reach the person only as "unavailable" (details in a log) — `DESIGN.md`, section "Unsupported".

## Why the person "cannot do anything" (cause)

1. **Everything is addressed by typed path or by id.** Move, create and restore ask for a path text; History needs the page id typed in a `page` field (`admin/revision.rs`: without a page the list is empty); Folder and Trash commands take ids. There is no tree to pick from, no "current page" context, so a path that does not match exactly fails.
2. **No file or folder dialog.** `import` takes a typed path, a media type and the pasted **text**; folder import happens once at start via `--docs` (reader mode, with `--export` for the way out). No system file chooser exists.
3. **No reading/editing context in the Admin window.** There is no rendered page there, no formatting, no links to follow.
4. **Conflicts and refusals are not explained.**

## Per workflow

| Workflow | Today | Needed |
|----------|-------|--------|
| W1 Create (empty / template) | Admin: `create` with typed path and content; `createFromTemplate` needs a template id. Reader: no create. No "Create" panel, no "+" at a tree entry | Create entry per place (tree "+"), template list to choose from, path derived from the chosen parent |
| W2 Edit, drafts, auto-save | Reader: edit with Save, cancel asks once, drafts backed up on disk, restore offered. Admin: `change` as a plain text field. No toolbar, no `/` menu, no autoformat verified, typing not verified by tests | Wire the text-editor component; toolbar; `/` menu; visible save state; drafts list; decide auto-save vs explicit Save |
| W3 Publish / update | **Not applicable as designed**: save writes to the database at once; no draft/published split, no schedule | Decide whether a draft state exists (page `kind`); if yes: publish dialog |
| W4 Rename | Not as a command for pages: a title is derived from the text; folders have `rename` | Title field with uniqueness check and clear message; move of path versus title decision |
| W5 Move, reorder | `move` with typed path (links rewritten, tested in core); `moveFolder`; `reorder` with typed placement and anchor id. No drag and drop, no dialog with tree and search | Tree view with drag and drop; Move dialog (browse + search tabs, start over); folder move; refusal messages |
| W6 Duplicate | Not present | Duplicate command with target and include-children option |
| W7 Delete, trash, restore, purge | `trash`, `delete`, `restore`, `purge` exist; Trash list is typed-filter only; purge needs hub; restore path optional. No "details before delete" (incoming links, children) | Confirm dialog showing links and children; trash view with Restore/Purge; hub for purge; rename on clash message |
| W8 Archive | Not present | Archive state, banner, list, restore |
| W9 History | History list needs a typed page id; `get`, `restore`, `purge` per `<page id>#<n>`. No compare view, no checkboxes | History opened from the page; two-version compare view; restore with comment; per-version delete confirmation |
| W10 Search | Admin: search with filters (prefix, path prefix, template, redirect, author, space, dates), list length capped by `LIST_LIMIT` (value not read); reader: name and content search, 200 hits. No global shortcut | Search entry always visible with shortcut; clear empty state; result open |
| W11 Import | Admin: typed path + media type + pasted text (Markdown). Reader: folder at start only. No file chooser, no Word/other-wiki import | File and folder chooser (system dialog); several files; placeholder parent for bulk; result report; Word and other formats (decide scope) |
| W12 Export | Admin `export` returns text; reader: explicit Export to one folder (`--export`), checks for overwrite | Export dialog with target chosen by the person; formats beyond Markdown (ours: decide) |
| W13 Links, backlinks | Core has links, backlinks, move rewriting; Admin Link view lists them (no page context). Reader follows links | Page details panel with incoming and outgoing links; link picker (Ctrl+K) |
| W14 Attachments | Not present (`attach`, `detach` described, not carried out) | Attachment storage (files interface), upload by drop, versions, list |
| W15 Permissions | Not present (`share`, `unshare` open, Sharing interface open) | Sharing interface first |

## Cross-cutting needs

- A **page tree with a current selection**, from which every command takes its object; no typed ids or paths for the ordinary case.
- **Dialogs** with a clear default button and Esc behaviour; the vorbild gives none, so we decide ([dialogs.md](dialogs.md)).
- A state for every case in [states.md](states.md): empty, loading, error, conflict, locked/offline.
- Messages for refusals (conflict, path taken, not empty) instead of "unavailable".
- Hide or disable commands that are not carried out instead of live buttons that fail.
