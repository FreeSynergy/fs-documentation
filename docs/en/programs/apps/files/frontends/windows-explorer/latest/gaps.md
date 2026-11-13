# Windows Explorer 11 — Gaps of our program

> [Windows Explorer](../index.md) · [workflows](workflows.md) · [acceptance](acceptance.md)

Our program is `fs-files`. State read from the repository on 2026-11-13 (`README.md`, `DESIGN.md`, `crates/fs-files-app`) and ADR 0070 (local provider: read and write at once). Today `fs-files` is **not a file manager**: its window is the generated Admin frontend (a list and form per data type) over the program's own store; it does not browse the computer's file system. What was not checked in code is marked `[nicht belegt]`.

| Workflow | Our state | Gap |
|----------|-----------|-----|
| W1 browse local system, drives, USB, network | Only the own store (a folder as backend, or S3). ADR 0070 plans the local provider (Home, USB) with immediate read and write; steps S3/S6 are not built | No browsing of Home, root, mounts, USB, network; no start page |
| W2 navigate, breadcrumb, typed path | The folder type lists by walking the tree up to a bound | No back/forward/up, breadcrumb, path field |
| W3 select | Generic list selection of the Admin frontend `[nicht belegt]` | Ranges, check boxes, select all unverified |
| W4 clipboard copy/move | Core has copy, move, rename calls | No clipboard in the window |
| W5 drag and drop | None | Missing |
| W6 two panes | None | Missing (only needed for the Total Commander style) |
| W7 conflict | Core refuses or keeps both (`name (2).ext`); replace does not exist | No dialog with a choice; no replace; no "for all" |
| W8 progress, cancel, pause | Resumable uploads; abort of an upload exists | No copy progress, pause or background list for copies |
| W9 rename | Core rename; refuses a taken name | Inline edit and name-rule messages unverified |
| W10 rename many | A bulk-rename command is described but the core does not answer it `[nicht belegt]` | Missing |
| W11 delete | Trash first; purge needs the file in trash; folder delete only if empty | Permanent delete of a non-empty folder is not offered |
| W12 trash | Restore, restore to another folder, restore as keep-both, purge, empty trash | Good; the view in the window is a list only `[nicht belegt]` |
| W13 undo/redo | None in the program; ADR 0070 plans activities with `Undo` | Missing |
| W14 new file/folder | Folders yes; a new empty file `[nicht belegt]` | Check |
| W15 properties | Fields of the object are shown by the generated form | No type-specific property sheet |
| W16 search | Search by word, sort, filters by size and date | Search over the local file system and cloud: missing |
| W17 sort/group | Sort by name, date, size, type | Group missing |
| W18 views | Only list/form | Icons, details, compact missing |
| W19 tabs | None | Missing |
| W20 open with | None; a chooser for local paths is not built (upload by typed `file:` link) | Missing |
| W21 archives | None | Missing |
| States | Disabled controls for unsupported commands exist | Empty/loading/offline states unverified |
| Shortcuts | None `[nicht belegt]` | Missing |
