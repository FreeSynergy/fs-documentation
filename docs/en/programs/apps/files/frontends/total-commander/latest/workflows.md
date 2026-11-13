# Total Commander — Workflows

> [Total Commander](../index.md) · [description](description.md) · [acceptance](acceptance.md) · [gaps](gaps.md)

Format: goal, steps (user does X → program shows Y), errors, undo. ✅ official wiki, changelog, or the official help of Total Commander 11.58 (2026-11-13); ⚠️ third-party only; `[nicht belegt]` not found in these sources. IDs W1..W21 match the other file-manager dossiers.

## W1 Browse the local file system
1. Start → two panels with folders ✅.
2. Click a **drive button** of a panel ✅ → that drive's root shows in the panel `[nicht belegt]` as to look.
3. USB stick plugged in → its drive letter becomes available as a drive button `[nicht belegt]`.
4. Network: the virtual folder "Network neighborhood" ✅ or a UNC path in the command line `[nicht belegt]`.
5. Home / Desktop: virtual folders ✅; favourite places via Ctrl+D ✅.
Errors: drive not ready → message `[nicht belegt]`. Undo: n/a.

## W2 Navigate
1. Enter on a folder opens it, Backspace or Ctrl+PgUp goes to the parent, Ctrl+\ to the root ✅.
2. Back / forward through the directory history: Alt+Left / Alt+Right (last 50 folders per panel); Alt+Down opens the history list, which by default only lists folders where the user stayed a while or worked (thinning); Alt+Shift+Down shows everything; a frequently-used-folders list is part of that list ✅.
3. Path: type `cd path` on the command line ✅, or use the directory hotlist (Ctrl+D ✅) or the CD-tree popup ✅.
4. Folder tabs keep several folders per panel ✅ (see W19).
5. Ctrl+Left/Right shows the folder under the cursor in the other panel; Ctrl+U swaps the panels ✅.
Errors: bad path `[nicht belegt]`.

## W3 Select
1. Cursor moves with arrows; Insert or Space marks and (Insert) moves on ✅; click, Ctrl+click, Shift+click ✅.
2. Range: Shift+Up/Down, Shift+Home/End, Shift+click ✅.
3. Pattern: Num+ → dialog → `*.txt`; `|*.exe` excludes; `<regex` ✅ → matching items are marked.
4. All: Ctrl+A or Ctrl+Num+; none: Ctrl+Num-; same extension: Alt+Num+; invert: Num*; restore last: Num/ ✅.
5. Save selection to a file and load back; load from clipboard ✅.
Errors: none. Undo: Ctrl+Num-.

## W4 Copy / move with the clipboard
1. Select items, Ctrl+C (copy) or Ctrl+X (cut) puts them on the clipboard ✅. 2. In the target folder press Ctrl+V ✅, or use Paste in the context menu of the target path ✅.
Whether a dialog appears on paste `[nicht belegt]`. The native way is W6.

## W5 Drag and drop
1. Press the left button on selected items and drag to the other panel, a subfolder, an archive (adds to it), the drive list or buttons, or the current-path bar ✅. A frame marks the drop target; a crossed circle means "not accepted" ✅.
2. Release → copy dialog, unless the drag-and-drop confirmation is switched off, then it copies at once ✅.
3. Alt or Shift while dragging moves (minus sign in the cursor); Ctrl+Shift creates shortcuts ✅. With the right button as the selection button, Shift before the drag is needed; with the left button as selection, dropping with the right button shows a menu copy / move / shortcut ✅.
4. Dropping on the F3, F4 or F8 buttons acts as pressing them; dropping on the button bar starts a program with the file ✅. Dragging to a tab-header gap opens the folders as tabs ✅.

## W6 Two panes: copy and move (F5 / F6)
Goal: transfer files between the two panels. Pre: source panel active, target folder open in the other panel.
1. Select items in the left panel (W3) → names marked.
2. Press F5 ✅ → copy dialog with the other panel's path and `*.*` as the target, an optional "only files of this type" filter, and the Options button for the overwrite mode ✅.
3. Change target or mode, press Enter/OK ✅ → copying begins with a progress dialog (files and bytes, switchable to remaining) ✅; Background moves it out of the way, F2 Queue puts it into the background transfer manager instead (one big job after another is more efficient than several in parallel) ✅.
4. Clash → W7. Done → press F2 or Ctrl+R if a background job ended and the list is not current ✅. Fully copied items are deselected, items skipped by the filter stay selected; Num/ restores the selection ✅.
5. F6 does the same but moves; with no target path (or the same folder) it renames; a file mask renames while moving ✅. Moving into an archive packs and deletes ✅.
Errors: target not writable, disk full `[nicht belegt]`; failed operations offer retry "as administrator" ✅; unreadable source: skip by option ✅. Undo: no general undo found in the help `[nicht belegt]`; move back with F6.

## W7 Conflict while copying
1. Mode "ask" (default 1 ✅) → overwrite dialog per existing name showing the existing file above and the source below (optionally with thumbnails/custom fields): Overwrite, Overwrite all, Skip, Skip all, Cancel (aborts the whole operation), Overwrite all older, Rename, Append ✅.
2. More Options: compare by content, rename the existing target, auto-rename copied or target files (`name(1).ext`), rename older target and skip newer, overwrite older or same age, copy only larger, copy only smaller ✅.
3. Unattended: choose Overwrite all / Skip all / Overwrite all older up front under Options in the copy dialog, optionally saved as default ✅.
4. Read-only and hidden/system targets ask again unless those confirmations are switched off ✅.
5. Appending one file to another: copy it onto the target and press Append ✅. Hotkeys in the dialog: F3 / Shift+F3 view, Ctrl+F3 compare ✅.
"Keep both" equals auto-rename ✅ (the product's wording differs). Undo: none.

## W8 Progress, cancel, pause, background
1. During copy/move, pack/unpack or delete the dialog has a **Background** button; the job then runs while the user keeps working; it can be brought back to the foreground when no other dialog is open ✅.
2. **Background transfer manager** (Commands menu): window with progress of the current file and the overall progress, queue list (reorderable while paused), **+** (add URL, selected items for copy / move / download), **−** (remove; on the first entry offers to abort the running transfer), **Pause**, speed limit ✅. Pasting an HTTP URL (Ctrl+V / Shift+Insert) starts a download into the current folder ✅.
3. Cancel: delete has a Cancel dialog ✅; copy progress `[nicht belegt]` as to button caption.

## W9 Rename one
1. Shift+F6 ✅ → an edit box opens on the item; pressing Shift+F6 again selects the name without extension ✅. (A second click on a selected name can also start it; switch off by ini setting ✅.)
2. Enter confirms; a click outside cancels ✅. Up/Down moves to the previous/next file and renames the edited one ✅. With several selected: dialog with wildcards, or "Rename each file separately" ✅.
Errors: name taken / forbidden `[nicht belegt]`. Undo: rename back by hand. Renaming a ZIP to EXE offers to create a self-extracting archive ✅.

## W10 Rename many (Multi-Rename Tool)
1. Select files, open the tool `[nicht belegt]` (how it is opened) → table old / new name ✅.
2. Type a rename mask with placeholders (`[N]`, `[C]`, `[Y]` …) and an extension mask ✅; set counter start, step, digits ✅.
3. Optionally search/replace pairs, regex, upper/lower ✅ → the preview list updates; bad masks show `<Error!>` ✅.
4. Press **Start!** → files renamed (clash gives a warning ✅).
5. **Undo** reverses last-first, even after reopening ✅; F5 applies another step to the same files ✅.

## W11 Delete
1. Select, press F8 or Delete ✅ → confirmation (can be switched off); an extra question for each non-empty folder, and for read-only or hidden/system files ✅ → the item goes to the recycle bin or is deleted directly, by setting; Shift flips the setting for this one call ✅. Dropping files on the F8 button does the same ✅.
2. A Cancel dialog can stop it; a Background button moves it out of the way ✅.
3. Inside an archive the files are deleted directly by the packer, not to the bin ✅.
Errors: failure offers "as administrator" ✅; file in use `[nicht belegt]`. Undo: restore from the recycle bin; the help warns there is no other undelete ✅.

## W12 Recycle bin
1. Open the virtual folder "Recycle bin" ✅ or the bin on the Desktop, where files are restored or removed for good ✅; the F8 button has its own local menu for the bin ✅. 2. Restore / empty: in the system bin ✅; the exact entries inside the virtual folder `[nicht belegt]`.

## W13 Undo / redo
No general undo of copy / move / delete was found in the help or key list `[nicht belegt]`. Undo exists in the Multi-Rename Tool ✅ and in the compare tool ✅; the recycle bin is the safety net for delete ✅; a saved selection can be restored (Num/) ✅.

## W14 New file / folder
1. F7 ✅ → dialog asks the folder name (the name under the cursor is offered); several levels with a backslash, several folders with `|`, counter ranges with `<1-10>[C]` ✅ → the folder appears; Shift+F7 creates it in the target panel ✅.
2. New file: Shift+F4 asks the name, creates the file and opens the editor (several names with `|` or counter ranges create files without the editor) ✅; other file types through the **New** submenu of the panel background menu ✅.

## W15 Properties
Alt+Enter or Files > Properties shows the system's properties dialog; on `..` it shows the current folder ✅. Change attributes (Files menu): read-only, archive, hidden, system, date and time, optionally in subfolders ✅. Ctrl+L / Calculate occupied space for the selection; Space on a folder shows its size; Alt+Shift+Enter counts all subfolders ✅ (can be turned off ✅).

## W16 Search
1. Alt+F7 ✅ → dialog. 2. Type name pattern; choose folders/drives, archives, depth; optionally text in files, regex, encoding ✅. 3. Start → results list at the bottom, usable while running ✅. 4. Go to file, or Feed to listbox ✅; Ctrl+C copies the results ✅.
Quick search: Ctrl+S, type; Ctrl+S inside toggles the live filter ✅.

## W17 Sort / group
Sort through the Show menu or Ctrl+F3..F7 (name, extension, date, size, unsorted) plus Reversed order ✅; name and extension sort ascending, size and time descending first ✅. Click on a column title `[nicht belegt]`; no grouping `[nicht belegt]`.

## W18 Views
Brief (Ctrl+F1), full (Ctrl+F2), comments, thumbnails (Ctrl+Shift+F1), tree (Ctrl+F8; Ctrl+Shift+F8 cycles one/two/no separate tree), custom columns, custom view modes, Quick View (Ctrl+Q; other panel shows the file, Ctrl+Q again or choosing a drive leaves; Ctrl+Shift+Q separate window), branch view (Ctrl+B), show filters (all, programs, custom; only selected) ✅.

## W19 Tabs
1. Open: Ctrl+T (same folder), Ctrl+Up (folder under cursor, stays on the current tab unless set otherwise), Shift with drive or hotlist choice, double or middle click in the free header space, drag folders to the header ✅.
2. Switch: click, Ctrl+Tab / Ctrl+Shift+Tab, Ctrl+Shift+A lists all tabs (pressed again toggles title/folder); options: list on Ctrl+Tab, jump to last visited ✅.
3. Close: Ctrl+W, middle click, double click (option), menu; Ctrl+Shift+W closes all; "close duplicates" and "recently closed" in the tab menu ✅. A confirm-close-all option exists ✅.
4. Lock / rename: fixed tabs, or locked with changes allowed that return to the saved folder ✅. Reorder by dragging, even to the other panel ✅. Save / load tab sets to files ✅.
5. Each tab keeps sort order, view mode and selection ✅.

## W20 Open with
Enter runs a program or the associated program, opens a folder/archive, or runs the command line if not empty ✅; F3 view (internal Lister, or external viewer, by setting; Shift/Alt flip), F4 edit ✅; Files > Associate with… edits associations ✅.

## W21 Archives
1. Enter on an archive → opens like a folder ✅ (formats ✅). 2. Copy files out with F5 → unpack dialog; copying into an archive shown in the target panel → pack dialog ✅. 3. Pack: Alt+F5 (Alt+Shift+F5 deletes the originals), unpack: Alt+F6 / Alt+F9 ✅. Viewing a file unpacks it to a temporary folder first ✅.

## W22 Synchronize directories (extra)
1. Set left and right folders, filter, options (Asymmetric, Subdirs, By content, Ignore date) ✅. 2. **Compare** → list with a direction per file ✅. 3. Change directions by hand ✅. 4. **Sync** → confirmation of choices ✅ → copies. Close leaves ✅.
