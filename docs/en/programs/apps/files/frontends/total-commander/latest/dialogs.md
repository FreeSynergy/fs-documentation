# Total Commander — Dialogs

> [Total Commander](../index.md) · [description](description.md)

✅ official wiki (2026-11-13) or changelog/forum; `[nicht belegt]` not found. Cancel closes without effect unless noted.

| Dialog | Purpose | Fields | Buttons | Default | Cancel | Mark |
|--------|---------|--------|---------|---------|--------|------|
| Copy / Move (F5/F6) | Choose the target and the overwrite rule | Target path (pre-filled with the other panel) ⚠️; overwrite mode list (1 ask, 2 overwrite all, 3 skip all, 4 overwrite older, 5 auto-rename; later one more: rename older, skip newer); option to overwrite system/hidden targets; option to skip unreadable sources | OK, Cancel, more `[nicht belegt]` | mode set by `CopyOverwriteDefault` | nothing copied | ✅ modes / ⚠️ rest |
| Overwrite question | One name clash (mode "ask") | Both files' info `[nicht belegt]` | Overwrite, Skip, Rename, Cancel (+ "all" variants `[nicht belegt]`) | `[nicht belegt]` | Cancel stops the operation | ✅ |
| Delete confirmation | Before F8 | `[nicht belegt]` | | | | `[nicht belegt]` |
| Progress | Running operation | | | | | `[nicht belegt]` |
| Select by pattern (Num+/Num-) | Mark by name | Pattern(s) separated by a vertical bar, a leading vertical bar excludes, `<` prefix regex, predefined filters | OK | | no change | ✅ |
| Search (Alt+F7) | Find files | Search for, Search in, Drives, RegEx, only selected, "Everything", archives, depth, Find text, whole words, case, regex, hex, NOT containing, encoding; tabs Advanced, Plugins, Load/Save | Start, Stop, New search, Go to file, Feed to listbox | | closes | ✅ (tab content `[nicht belegt]`) |
| Quick search | Jump / filter | Letters; filter icon or Ctrl+S | | | | ✅ |
| Multi-Rename | Batch rename | Rename mask, extension, counter (start, step, digits), search/replace pairs, RegEx, Subst., upper/lower, result list | Start!, Undo, F5 next step, F2 settings, Result list | | closes without renaming | ✅ |
| Synchronize directories | Compare and sync | Left, right dir, file filter, Asymmetric, Subdirs, By content, Ignore date, FTP time offset, direction filters, Duplicates/Singles | Compare, Sync, Close | | Close returns to panels | ✅ |
| Sync confirmation | Before acting | List of choices and directions | | | | ✅ exists; content `[nicht belegt]` (page says it is missing) |
| Directory hotlist editor | Manage favourites | Entries, sub-menus | Add current, Remove current, Configure | | | ✅ |
| Pack files (Alt+F5) | Create archive | Archive name, packer | | | | `[nicht belegt]` |
| Unpack (Alt+F6) | Extract | Target, options | | | | `[nicht belegt]` |
| FTP connection | Log in | Host, user, password | | | | `[nicht belegt]` |
| Compare by content | Diff two files | | | | | ✅ named |
| Options (Configuration) | All settings incl. Quick search, confirmation | | | | | ✅ named |
