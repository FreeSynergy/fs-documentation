# Total Commander — Gaps of our program

> [Total Commander](../index.md) · [workflows](workflows.md) · [acceptance](acceptance.md)

Our program `fs-files`: state read from the repository on 2026-11-13 (`README.md`, `DESIGN.md`, `crates/fs-files-app`) and ADR 0070 (local provider: read and write at once). Today it shows **only its own store** through the generated Admin frontend; it is not a file manager of the computer and has one list, not two panes. `[nicht belegt]` = not checked in code.

| Workflow | Our state | Gap |
|----------|-----------|-----|
| W1 drives, USB, network | Own store only; local provider planned (ADR 0070) | No drive buttons, mounts, USB, network |
| W2 navigate | Tree walk | No history, typed path, hotlist, tabs |
| W3 select | Generic selection `[nicht belegt]` | Pattern, range, invert, restore, save: missing |
| W4/W5 clipboard, drag | None | Missing |
| W6 two panes F5/F6 | Core has copy and move calls | No second pane, no target pane, no dialog |
| W7 conflict | Refuse or keep both; no replace | No modes (overwrite, skip, older, ask), no per-file dialog |
| W8 progress | Resumable upload, upload abort | No copy progress, cancel, background |
| W9 rename | Core rename | In-place edit missing `[nicht belegt]` |
| W10 multi-rename | Bulk command described, not answered `[nicht belegt]` | Missing: mask, counter, preview, undo |
| W11 delete | Trash, purge, empty trash | No confirmation setting; folder delete only if empty |
| W12 bin | Restore, restore elsewhere, restore keep-both, purge, empty | View in window `[nicht belegt]` |
| W13 undo | None; ADR 0070 plans `Undo` | Missing |
| W14 new item | Folder yes | File `[nicht belegt]` |
| W15 properties | Generated form | No folder size on demand |
| W16 search | Word, sort, size/date filters | No content search, regex, archives, quick filter |
| W17 sort | By name, date, size, type | Column click `[nicht belegt]` |
| W18 views | List/form | Brief, thumbnails, Quick View missing |
| W19 tabs | None | Missing |
| W20 open with | None | Missing |
| W21 archives | None | Missing |
| W22 sync | None; sync is not in the Files plan (DESIGN.md: "no sync") | Missing |
| FTP | S3 only; SFTP/WebDAV planned | Missing |
| Shortcuts / key binding | None `[nicht belegt]` | Missing |
