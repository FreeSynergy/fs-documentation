# Notion (latest) · Gaps against our program

What our wiki program cannot do for the workflows of [workflows.md](workflows.md), and what is needed. Tests that fail because of these gaps: [acceptance.md](acceptance.md). The state of our program is described in the same words in the [Confluence gaps](../../confluence/latest/gaps.md) page (section "Our state"); it is summarised here.

## Our state, as read (2026-11-13)

Read (read only) from `/srv/FreeSynergy/fs-wiki`: `README.md`, `DESIGN.md`, `crates/fs-wiki-app/src/*`, `crates/fs-wiki-core/src/describe/support.rs`.

- Version: workspace `0.0.6` (README: tag `v0.0.6`); `DESIGN.md` says 0.5.0. A 0.0.8/0.0.9 is **[nicht belegt]** in what was read.
- Default window = generated Admin window with one view per type (Pages, Folders, History, Trash, Links) and **forms with typed paths and ids**. `--reader` = older reader with page tree, reading, search, editing, Save, Export, draft backup.
- The text-editor component is **not wired** into the Admin window; no block editor, no slash menu.
- Carried out: page create/import/createFromTemplate/change/move/reorder/trash/delete/find/search/resolve/export, folder create/rename/move/reorder/delete, revision find/get/restore/purge, trash restore/purge, link find. Not carried out: share, comment, attach, labels, watch, databases, co-editing, tags, canvas.
- Uncarried commands appear as live buttons that end in an error; refusals (conflict, path taken) show only as "unavailable".

## Why "nothing can be done" (cause)

1. Commands ask for typed paths and ids; there is no tree to pick from, no current page.
2. Import is typed path + media type + pasted text; no file or folder chooser; folder import only at start (`--docs`, reader).
3. History needs a typed page id; Trash is a typed-filter list.
4. No block editing and no slash menu in the window that is the default.

## Per workflow

| Workflow | Today | Needed |
|----------|-------|--------|
| W1 Create | Typed path and text (`create`); template needs an id; reader has no create. No "+" in a tree, no new-item menu | "+" at tree entries and sections; location chosen by position; template picker |
| W2 Edit | Reader: Markdown text editor with Save and draft backup; Admin: plain text field. No blocks, no `/` menu, no block handle, no selection model | Wire the text-editor component; slash menu; block actions; selection states; visible save state |
| W3 Publish | Save writes to the database at once, no draft state, no web publishing | Decide: stay "always live"; web publish needs a Sharing interface |
| W4 Rename | No page rename command (title derived from text); folder `rename` only | Rename in the tree menu; link-rewrite decision |
| W5 Move | `move` by typed path with link rewrite (tested in core), `moveFolder`, `reorder` by id. No drag and drop, no "Move to" chooser | Tree drag and drop; "Move to" chooser; message when access changes |
| W6 Duplicate | None | Duplicate command (pages, blocks) |
| W7 Delete | `trash`, `restore`, `purge`, `delete` exist; purge needs hub; no confirm, no drag-to-Trash, no filters by editor/location | Trash view in the sidebar; restore to original place; filters; retention rule |
| W8 Search | Filters exist in Admin search (author, dates, prefix, space); reader search by name and content, 200 hits. No shortcut, no recent list | Always-open search with recents and sort; in-page search |
| W9 History | History needs a typed id; `get` and `restore` exist; no list in context, no preview, no copy out | History opened from the page; preview; restore |
| W10 Import | See cause 2 | System file and folder chooser; progress list; per-format results; limits |
| W11 Export | Admin `export` returns text; reader Export to one folder given at start | Export dialog with chosen target, include sub-pages option, workspace export |
| W12 Links | Core links/backlinks; Link view without page context; reader follows links | Backlinks under the title; `@`/`[[` picker; copy link to block |
| W13 Attachments | None | File storage interface, upload, media blocks |
| W14 Permissions | None (Sharing interface open) | Sharing interface first |
| W15 Offline | None; drafts only backed up on disk in reader | Local copy with sync; conflict rule for non-text |

## Cross-cutting needs

- Tree with selection; every command acts on the selected object.
- Dialogs with defined default button and Esc behaviour (decide, [dialogs.md](dialogs.md)).
- A state for every row of [states.md](states.md).
- Real messages for refusals; hide or disable commands that are not carried out.
