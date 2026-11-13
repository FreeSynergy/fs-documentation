# Total Commander — States

> [Total Commander](../index.md) · [description](description.md)

✅ = stated in the official help of Total Commander 11.58 (retrieved 2026-11-13) or the official wiki; `[nicht belegt]` = not found there (verify in the program).

| State | What the user sees | What the user can do |
|-------|--------------------|----------------------|
| Start | Two panels; last folders restored (can be excluded per drive via "do not remember these drives") ✅; tabs `[nicht belegt]` as to start-up restore | Everything |
| Active panel | The panel with the frame is the **source**; it reacts to keys, the other is the target ✅ | Tab switches ✅; clicking a tab of the other panel activates it or not, by option ✅ |
| Empty folder | Only the parent entry `[nicht belegt]` | Make folder, paste |
| Loading / reading | Branch view and size counting can be aborted with Esc ✅; list reading on slow drives `[nicht belegt]` | Esc (for branch view) ✅ |
| Auto-refresh | List updates about one second after a change in the folder; optional footer and free-space update; off for chosen drives, virtual folders, and while in the background ✅; also on returning to the program ✅ | F2 / Ctrl+R to reread by hand; needed after a background operation ✅ |
| Error: no access / drive missing | Error message `[nicht belegt]`; for failed delete, copy or make-folder an extra offer to retry "as administrator" ✅ | Retry as administrator, cancel ✅ |
| Cursor only | One item under the cursor, not selected ✅ | Commands act on the cursor item if nothing is selected ✅ (calculate space, view) |
| Selection (items marked) | Marked names in another colour; status line shows count and size ✅ | Copy, move, delete, pack, rename |
| Pattern selection | Dialog for the pattern(s) with a history list ✅, then matching items marked | Edit pattern; Shift+Del removes a history entry ✅ |
| Selection saved / restored | Selection is saved automatically at every file operation; Num/ restores it ✅. Files left out by a copy filter stay selected, fully copied ones are deselected ✅ | |
| Quick search | Small box below the panel; cursor jumps to the next matching name; Up/Down next/previous; Esc closes; closes itself when another action starts ✅ | Esc ✅ |
| Quick filter | Ctrl+S filters the list live; Esc or Ctrl+F10 ends it ✅ | |
| Branch view | All files of the folder and subfolders in one list ✅ | Ctrl+B leaves it; with the cursor in a subfolder file, it goes to that subfolder ✅ |
| Quick View | The other panel shows the file under the cursor (a Lister); for a folder it shows occupied space ✅ | Ctrl+Q leaves; Lister keys work when it is active ✅ |
| Rename in place | An edit box on the item; Enter confirms, a click outside cancels ✅ | Up/Down moves to the neighbour file ✅ |
| Multi-Rename | Table old name → new name; `<Error!>` for a bad mask; nothing renamed before Start! ✅ | Edit, Start!, Undo ✅ |
| Conflict | Overwrite dialog per clash (or the chosen default mode) ✅ | See [dialogs](dialogs.md) |
| Operation running | Copy progress dialog with counts of files and bytes (click to switch to remaining), name tooltips ✅; a Cancel dialog for delete ✅ | Cancel; **Background** button during copy/move, pack/unpack, delete; back to the foreground if no other dialog is open ✅ |
| Operation in background | Work continues while the panels are usable ✅; separate **Background transfer manager** window with progress for the current file and overall, queue list, pause, speed limit ✅ | Add/remove jobs (the running job can be aborted), reorder while paused ✅ |
| Search running | Results fill the panel at the bottom; files can be viewed meanwhile ✅ | Stop, go to file, feed to listbox ✅ |
| Tab locked | Tab shown with `*` (option); changing folder opens a new tab, or (variant "locked but changes allowed") returns to the saved folder; `!` before the title when away from it ✅ | Unlock via tab menu ✅ |
| Archive open | The archive is a folder in the panel ✅; delete and some other functions go through the packer; many functions unavailable (calculate space, attributes, rename except single ZIP items) ✅ | Copy out, unpack, view (unpacked to a temp folder) ✅ |
| FTP connected | Server folders in the panel ✅ | Download, upload, background download |
| Sync compared | List with direction per row; status bar totals ✅ | Change direction, Sync |
| Locked source file | Error for a locked source; option to skip unreadable files ✅ | Skip or retry |
