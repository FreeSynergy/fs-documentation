# Total Commander — Dialogs

> [Total Commander](../index.md) · [description](description.md)

✅ official wiki (2026-11-13), changelog/forum, or the official help of Total Commander 11.58 (retrieved 2026-11-13); `[nicht belegt]` not found. Cancel closes without effect unless noted.

| Dialog | Purpose | Fields | Buttons | Default | Cancel | Mark |
|--------|---------|--------|---------|---------|--------|------|
| Copy / Move (F5/F6) | Choose the target and the overwrite rule | Target path with file mask (pre-filled with the other panel's path and `*.*`; the box also offers open tabs and sub-folders; wildcard renaming rules; F5/F6 pressed again selects the name, then the extension); "Only files of this type" filter (include and exclude patterns, `\|` excludes, folder patterns) plus a button for saved search filters; Verify (checksum re-read); Copy NTFS permissions; Keep relative paths (from branch view); Options (default overwrite behaviour Overwrite all / Skip all / Overwrite all older, can be saved; ignore read-only/hidden/system); a target panel with selected folders offers copying to all of them | OK, Cancel, **Tree** (pick target from a tree), **+ F7** (add/remove target in hotlist), **+ F8** (search filter), **F2 Queue** (add to the background transfer manager), Options; right click on OK/Queue flips copy and move | OK | nothing copied | ✅ |
| Overwrite question | One name clash (mode "ask") | Upper: details of the existing target; lower: details of the source; optional thumbnails of both and custom fields (also from content plugins) | Overwrite, Overwrite all, Skip, Skip all, Cancel (aborts the whole operation), Overwrite all older, Rename (copy), Append (source to target), **More Options**: Compare by content, Rename existing target, Auto-rename copied (name(1).ext), Auto-rename target, Rename older target and skip newer, Overwrite all older and same age, Copy all larger, Copy all smaller | none stated | Cancel stops the operation | ✅ (read-only and hidden/system targets ask again, by confirmation settings) |
| Delete confirmation | Before F8 / Del | Asks after selection; a further question for each non-empty folder; further questions for read-only and hidden/system files; each of these can be switched off in Configuration > Misc (confirmations) ✅ | Yes/No-style confirmation (exact captions `[nicht belegt]`) | | Cancel dialog can stop a running delete | ✅ |
| Copy progress | Running operation | Copied/total files and bytes (click to show remaining), names with full-name tooltip ✅ | Cancel, **Background** (also for pack/unpack, delete) ✅ | | | ✅ |
| Background transfer manager | Queue of copy, move, download jobs | Progress of current file and overall, queue list (reorder while paused), speed limit | **+** (add URL, selected items for download / copy / move, edit list file), **−** (remove; on the running job offers to abort), Pause | | | ✅ |
| Overwrite configuration | Confirmation switches | Confirm deleting non-empty folders; overwriting files; overwriting/deleting read-only; hidden/system; drag-and-drop (when off, dropping copies at once without a dialog) | | | | ✅ |
| Rename in place (Shift+F6) | Rename one item | Edit box on the name; Shift+F6 again selects the name only; several selected: wildcard dialog with "Rename each file separately" | Enter confirms; click outside cancels | | | ✅ |
| New folder (F7) | Create folder | Name (cursor item's name offered); several levels with backslash; several with `\|`; `<` prefix for placeholders and counter ranges | OK, Cancel | | | ✅ |
| New text file (Shift+F4) | Create file | Name; several with `\|`; placeholders with `<`; opens the editor unless several or the editor is "none" | OK, Cancel | | | ✅ |
| Change attributes | Files > Change attributes | Read-only, archive, hidden, system, date and time, apply to files in folders | OK, Cancel (details `[nicht belegt]`) | | | ✅ |
| Properties (Alt+Enter) | Files > Properties | The system's own Properties dialog (as in Explorer) | | | | ✅ |
| Select by pattern (Num+/Num-) | Mark by name | Pattern(s) separated by a vertical bar, a leading vertical bar excludes, `<` prefix regex, predefined filters | OK | | no change | ✅ |
| Search (Alt+F7) | Find files | Search for, Search in, Drives, RegEx, only selected, "Everything", archives, depth, Find text, whole words, case, regex, hex, NOT containing, encoding; tabs Advanced, Plugins, Load/Save | Start, Stop, New search, Go to file, Feed to listbox | | closes | ✅ (tab content `[nicht belegt]`) |
| Quick search | Jump / filter | Small box below the active panel; letters; Up/Down next/previous match; trigger key combination configurable (Ctrl+Alt+letter, Alt+letter, letters only, letters with box, off); filter via Ctrl+S | | | Esc closes | ✅ |
| Multi-Rename | Batch rename | Rename mask, extension, counter (start, step, digits), search/replace pairs, RegEx, Subst., upper/lower, result list | Start!, Undo, F5 next step, F2 settings, Result list | | closes without renaming | ✅ |
| Synchronize directories | Compare and sync | Left, right dir, file filter, Asymmetric, Subdirs, By content, Ignore date, FTP time offset, direction filters, Duplicates/Singles | Compare, Sync, Close | | Close returns to panels | ✅ |
| Sync confirmation | Before acting | List of choices and directions | | | | ✅ exists; content `[nicht belegt]` (page says it is missing) |
| Directory hotlist editor | Manage favourites | Entries, sub-menus | Add current, Remove current, Configure | | | ✅ |
| Pack files (Alt+F5) | Create archive | Archive name with packer prefix (e.g. `zip:`); pack with relative paths; recurse into subfolders; multi-disk; move to archive (delete originals after success); self-extracting; one archive per item; leave out base folder; encrypt; compression rate; packer choice | OK, Cancel, Configure | OK | nothing packed | ✅ |
| Unpack (Alt+F6 / Alt+F9) | Extract | Target path (empty = archive's folder); file mask (Alt+F9 only); name encoding; keep stored paths; overwrite existing without asking; one sub-folder per archive | OK, Cancel | OK | nothing unpacked | ✅ |
| FTP connection | Log in | Host, user name, password (help pages dialog_box__connect, dlg_connectdetails, dlg_newconnection) | | | | ✅ (fields; button captions `[nicht belegt]`) |
| Compare by content | Diff two files | | | | | ✅ named |
| Options (Configuration) | All settings incl. Quick search, confirmation | | | | | ✅ named |
| Choose command | named in the official help (dialog page) | | | | | ✅ named |
| Directory tree | named in the official help (dialog page) | | | | | ✅ named |
| Select duplicate files | named in the official help (dialog page) | | | | | ✅ named |
| Create checksum files | named in the official help (dialog page) | | | | | ✅ named |
| Verify checksums | named in the official help (dialog page) | | | | | ✅ named |
| Combine files | named in the official help (dialog page) | | | | | ✅ named |
| Split file | named in the official help (dialog page) | | | | | ✅ named |
| Encode file | named in the official help (dialog page) | | | | | ✅ named |
| Decode file | named in the official help (dialog page) | | | | | ✅ named |
| Edit comment | named in the official help (dialog page) | | | | | ✅ named |
| Print | named in the official help (dialog page) | | | | | ✅ named |
| Change UNIX attributes | named in the official help (dialog page) | | | | | ✅ named |
| Choose encoding | named in the official help (dialog page) | | | | | ✅ named |
| Firewall settings | named in the official help (dialog page) | | | | | ✅ named |
| Edit file type | named in the official help (dialog page) | | | | | ✅ named |
| Edit action | named in the official help (dialog page) | | | | | ✅ named |
| Associate | named in the official help (dialog page) | | | | | ✅ named |
| Change start menu | named in the official help (dialog page) | | | | | ✅ named |
| Change directory menu | named in the official help (dialog page) | | | | | ✅ named |
| Custom columns | named in the official help (dialog page) | | | | | ✅ named |
| System information | named in the official help (dialog page) | | | | | ✅ named |
| Configure lister | named in the official help (dialog page) | | | | | ✅ named |
