# Total Commander — States

> [Total Commander](../index.md) · [description](description.md)

The official pages say little about states. ✅ stated; `[nicht belegt]` otherwise (verify in the program).

| State | What the user sees | What the user can do |
|-------|--------------------|----------------------|
| Start | Two panels with the last folders; tabs restored `[nicht belegt]` | Everything |
| Active panel | One panel is current (cursor bar bright) `[nicht belegt]`; it is the source, the other the target | Tab switches ⚠️ |
| Empty folder | Only the parent entry `[nicht belegt]` | Make folder, paste |
| Loading | List fills; slow drives show a wait `[nicht belegt]` | Esc `[nicht belegt]` |
| Error: no access / drive missing | Error message `[nicht belegt]` | Retry, cancel |
| Cursor only | One item under the cursor, not selected ✅ (selection is separate from the cursor) | Commands act on the cursor item if nothing is selected ⚠️ |
| Selection (items marked) | Marked names in a different colour; status line shows count and size ✅ (Space on a folder shows its size ✅) | Copy, move, delete, pack, rename |
| Pattern selection | Dialog for the pattern, then all matching marked ✅ | Edit pattern |
| Selection restored | After an operation Num/ brings it back ✅ | |
| Quick search | A small field at the panel's foot shows typed letters; cursor jumps or list filters (Ctrl+S) ✅ | Esc ends `[nicht belegt]` |
| Multi-Rename | Table old name → new name; `<Error!>` for a bad mask ✅; nothing is renamed before Start! ✅ | Edit, Start!, Undo ✅ |
| Conflict | Overwrite question for each clash (or the chosen default mode) ✅ | See [dialogs](dialogs.md) |
| Operation running | Progress window `[nicht belegt]` | Cancel `[nicht belegt]` |
| Search running | Results fill the panel at the bottom; files can be viewed meanwhile ✅ | Stop, go to file, feed to listbox ✅ |
| Archive open | The archive is a folder in the panel ✅ | Copy out, unpack |
| FTP connected | Server folders in the panel ✅ | Download, upload |
| Sync compared | List with direction per row; status bar totals ✅ | Change direction, Sync |
| Offline / locked | Error for a locked source; option to skip unreadable files ✅ | Skip or retry |
