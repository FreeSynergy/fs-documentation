# Files — Gaps of our program

> [Files](../index.md) · [workflows](workflows.md) · [acceptance](acceptance.md)

Our program `fs-files`: state read from the repository on 2026-11-13 (`README.md`, `DESIGN.md`, `crates/fs-files-app`) and ADR 0070 (local provider: read and write at once). Today `fs-files` shows **only its own store** through the generated Admin frontend (list and form per data type); it is not a file manager of the computer. `[nicht belegt]` = not checked in code.

| Workflow | Our state | Gap |
|----------|-----------|-----|
| W1 browse system, drives, USB, network | Own store (folder backend, S3). Local provider planned (ADR 0070, steps S3/S6/S7), not built | No Home page, drives, mounts, USB, network, cloud folders |
| W2 navigate / Omnibar | Tree walk of folders up to a bound | No breadcrumb, typed path, aliases, back/up |
| W3 select | Generic list selection `[nicht belegt]` | Range, all, check boxes unverified |
| W4 clipboard | Core copy/move/rename calls | No clipboard in the window |
| W5 drag and drop | None | Missing (also to sidebar places and tabs) |
| W6 second pane | None | Missing; also move between panes |
| W7 conflict | Refuse or keep both (`name (2).ext`); no replace | No dialog, no replace, no "for all" |
| W8 progress | Resumable uploads, abort of an upload | No copy progress, pause, background list |
| W9 rename | Core rename; taken name refused | Inline edit, extension warning |
| W10 rename many | Command described, core does not answer it `[nicht belegt]` | Missing |
| W11 delete | Trash, purge, empty trash; folder delete only if empty | No confirmation setting; no permanent delete of full folders |
| W12 bin | Restore, restore elsewhere, restore keep-both, purge, empty | Window view of the bin `[nicht belegt]` |
| W13 undo | None; ADR 0070 plans `Undo` activities | Missing |
| W14 new item | Folder yes; empty file `[nicht belegt]` | Check |
| W15 properties | Generated form fields | No info pane |
| W16 search | Search word, sort, size/date filters | No `tag:`, no local-disk or cloud search; no Omnibar |
| W17 sort/group | Sort by name, date, size, type | Group, folders-first rule |
| W18 views | List/form only | Six views missing |
| W19 tabs | None | Missing |
| W20 open with | None; no file chooser (upload by `file:` link) | Missing |
| W21 archives | None | Missing |
| Tags | None `[nicht belegt]` (sensitive marks only) | Missing |
| Shortcuts / action palette | None `[nicht belegt]` | Missing |
| FTP/FTPS | S3 only; SFTP/WebDAV planned (ADR 0070) | Missing |
