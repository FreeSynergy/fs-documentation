# Windows Explorer 11 — States

> [Windows Explorer](../index.md) · [description](description.md)

The official page describes almost no states. Everything below is `[nicht belegt]` unless marked ✅; it records the behaviour known from the product and must be re-checked on a Windows machine (see BERICHT).

| State | What the user sees | What the user can do |
|-------|--------------------|----------------------|
| Start | Home (pinned folders, recent items) or This PC, by option ✅ | Open a folder, search, change option ✅ |
| Empty folder | An empty file area with a short "folder is empty" text | New, Paste, navigate away |
| Loading | Address bar fills with a green progress strip; list appears while reading | Navigate away, cancel by navigating |
| Loading search | Search results appear while the scan runs | Stop by clearing the box |
| Error: path missing / no access | A dialog or an inline message that the location cannot be reached | Retry, cancel, type another path |
| Error: network or drive gone | Same; the pane entry stays until refreshed | Refresh (F5 ✅), reconnect |
| One item selected | Item highlighted; command bar enables Rename, Share, Delete ✅; status bar shows one item | All commands for one item |
| Several items selected | All highlighted, optional check boxes ✅; count in status bar | Cut, Copy, Delete, Share; Rename of many applies a numbering scheme |
| Range / extended selection | Contiguous block highlighted (Shift+arrows ✅) | Same as several |
| Rename (editing) | Name becomes an edit field, base name selected, extension left out | Type, Enter confirms, Esc cancels |
| Cut pending | Cut items shown faded until pasted | Paste elsewhere, Esc ends |
| Drag in progress | Ghost of the items, tooltip "Copy to / Move to / Create link" (follows Ctrl/Shift/Alt ✅) | Drop or Esc |
| Conflict | Dialog for each name clash, see [dialogs](dialogs.md) | Replace / skip / decide per file |
| Copy in progress | Progress dialog, speed and time | Cancel, pause, details |
| Locked | "File in use" dialog | Retry, skip, cancel |
| Offline (cloud) | Cloud placeholder icons; online-only files fetched on open | Open (downloads), keep offline, free space |
| Preview pane on | Preview of the selected item ✅ (toggle Alt+P ✅) | Toggle |
| Recycle Bin view | List with original place and delete date | Restore, empty |
