# Dolphin

> Category: [files](../../index.md) · [frontends](../index.md)

## What it is

The file manager of KDE Plasma. Local files and, through KDE's I/O layer, other places. Free software. ⚠️ (licence and I/O layer not read on the pages below.)

## Notable ideas

- **Panels you can switch on and move:** Places, Information, Folders, Terminal. The terminal follows the folder shown, and works only on local media ✅.
- **Split view:** two folders side by side to move or copy between them ✅.
- **Information panel with edit:** preview plus rating, tags and comments for the selected item ✅.
- **Saved searches in Places** ✅. A search finds names and contents, with wildcards, and can be narrowed by type, date, rating, tag ✅.
- **Batch rename with `#`** as a counter ✅.

## Capabilities seen

| Capability | Seen | Note |
|------------|------|------|
| List with icons, compact, details (tree in details), preview thumbnails | ✅ | Grouping by sort type in all modes |
| Select by rectangle, Ctrl, Shift, type-ahead, Ctrl+A | ✅ | |
| Undo of rename and move to trash (Ctrl+Z) | ✅ | The menu names the action |
| Filter bar by name part (Ctrl+I) | ✅ | |
| Search in names and contents (Ctrl+F), save the search | ✅ | |
| Rename many files (F2, `#`) | ✅ | |
| Bookmarks (Places), mount devices | ✅ | |
| Rating, tags, comments | ✅ | Shown in Information panel and details columns |
| Compare two files or folders (external tool) | ✅ | Needs Kompare |
| Tabs | ⚠️ | Only a mention on the view page; a bug report says split view belongs to a tab |
| Trash, service menus | ⚠️ | Only seen as chapter titles in the contents list |
| Remote locations, compress | ⚠️ | Not found in the handbook pages read |

## Name rules

Not documented by Dolphin; the file system decides. ⚠️

## What we take

Capabilities `file.search` (names and contents), `file.tag`, bulk rename (missing in the contract), undo of the last change (a frontend job, needs the engine to make moves reversible), saved search as a collection (see design: "an album can be a saved search").

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
No version documented in English yet.
<!-- /gen:versions -->

## Sources (read 2026-11-06)

- https://docs.kde.org/stable_kf6/en/dolphin/dolphin/ (contents)
- https://docs.kde.org/stable_kf6/en/dolphin/dolphin/dolphin-view.html
- https://docs.kde.org/stable_kf6/en/dolphin/dolphin/panels.html
- https://docs.kde.org/stable_kf6/en/dolphin/dolphin/quick-tips.html
- Not official, not used for claims: bug reports on split view and tabs (bugs.kde.org).
