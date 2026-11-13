# Total Commander — Workflows

> [Total Commander](../index.md) · [description](description.md) · [acceptance](acceptance.md) · [gaps](gaps.md)

Format: goal, steps (user does X → program shows Y), errors, undo. ✅ official wiki or changelog (2026-11-13); ⚠️ third-party only; `[nicht belegt]` not found (the offline manual was not reachable). IDs W1..W21 match the other file-manager dossiers.

## W1 Browse the local file system
1. Start → two panels with folders ✅.
2. Click a **drive button** of a panel ✅ → that drive's root shows in the panel `[nicht belegt]` as to look.
3. USB stick plugged in → its drive letter becomes available as a drive button `[nicht belegt]`.
4. Network: the virtual folder "Network neighborhood" ✅ or a UNC path in the command line `[nicht belegt]`.
5. Home / Desktop: virtual folders ✅; favourite places via Ctrl+D ✅.
Errors: drive not ready → message `[nicht belegt]`. Undo: n/a.

## W2 Navigate
1. Enter on a folder → opens `[nicht belegt]`; the parent entry (`..`) goes up `[nicht belegt]`.
2. Back / forward through the directory history ✅ (feature named; keys `[nicht belegt]`).
3. Path: type `cd path` on the command line ✅, or use the directory hotlist (Ctrl+D ✅) or the CD-tree popup ✅.
4. Folder tabs keep several folders per panel ✅.
Errors: bad path `[nicht belegt]`.

## W3 Select
1. Cursor moves with arrows; Insert or Space marks and (Insert) moves on ✅; click, Ctrl+click, Shift+click ✅.
2. Range: Shift+Up/Down, Shift+Home/End, Shift+click ✅.
3. Pattern: Num+ → dialog → `*.txt`; `|*.exe` excludes; `<regex` ✅ → matching items are marked.
4. All: Ctrl+A or Ctrl+Num+; none: Ctrl+Num-; same extension: Alt+Num+; invert: Num*; restore last: Num/ ✅.
5. Save selection to a file and load back; load from clipboard ✅.
Errors: none. Undo: Ctrl+Num-.

## W4 Copy / move with the clipboard
Clipboard copy and paste into the panel `[nicht belegt]` (Ctrl+C / Ctrl+V exist ⚠️ not verified). The native way is W6.

## W5 Drag and drop
Drag marked items to the other panel or to a folder `[nicht belegt]`; the copy dialog appears ⚠️.

## W6 Two panes: copy and move (F5 / F6)
Goal: transfer files between the two panels. Pre: source panel active, target folder open in the other panel.
1. Select items in the left panel (W3) → names marked.
2. Press F5 ⚠️ → copy dialog with the other panel's path as the target and the overwrite mode ✅.
3. Change target or mode, press Enter/OK `[nicht belegt]` → copying begins; progress `[nicht belegt]`.
4. Clash → W7. Done → items appear in the other panel `[nicht belegt]`; the selection is saved, Num/ restores it ✅.
5. F6 does the same but moves; with the target in the same folder it renames ⚠️.
Errors: target not writable, disk full `[nicht belegt]`; unreadable source: skip by option ✅. Undo: no general undo `[nicht belegt]`; move back with F6.

## W7 Conflict while copying
1. Mode "ask" (default 1 ✅) → for each existing name a question: overwrite, skip, rename, cancel ✅.
2. "Overwrite all", "Skip all", "Overwrite all older", "Auto-rename copied" can be chosen up front in the copy dialog ✅ (numbered choices, set by `CopyOverwriteDefault`) ✅; later versions add "rename older, skip newer" ✅.
3. System/hidden target files need the extra option or a confirmation ✅.
"Keep both" equals auto-rename ✅ (wording `[nicht belegt]`). Undo: none.

## W8 Progress, cancel, pause, background
Progress window, cancel, background transfer, pause: exist in the product `[nicht belegt]` on the pages read.

## W9 Rename one
1. Shift+F6 ⚠️ (or F2 in newer versions `[nicht belegt]`) → edit the name in the list or in a dialog `[nicht belegt]`.
2. Enter confirms. Errors: name taken / forbidden `[nicht belegt]`. Undo: rename back.

## W10 Rename many (Multi-Rename Tool)
1. Select files, open the tool `[nicht belegt]` (how it is opened) → table old / new name ✅.
2. Type a rename mask with placeholders (`[N]`, `[C]`, `[Y]` …) and an extension mask ✅; set counter start, step, digits ✅.
3. Optionally search/replace pairs, regex, upper/lower ✅ → the preview list updates; bad masks show `<Error!>` ✅.
4. Press **Start!** → files renamed (clash gives a warning ✅).
5. **Undo** reverses last-first, even after reopening ✅; F5 applies another step to the same files ✅.

## W11 Delete
1. Select, press F8 or Delete ⚠️ → confirmation `[nicht belegt]` → item goes to the recycle bin or is deleted directly, by setting ⚠️.
Errors: file in use `[nicht belegt]`. Undo: from bin.

## W12 Recycle bin
1. Open the virtual folder "Recycle bin" ✅. 2. Restore / empty: through the Windows shell menu `[nicht belegt]`.

## W13 Undo / redo
Only in Multi-Rename ✅. General undo of copy/move/delete `[nicht belegt]`.

## W14 New file / folder
1. F7 ⚠️ → dialog asks the folder name `[nicht belegt]` → the folder appears. 2. New file: `[nicht belegt]`.

## W15 Properties
`[nicht belegt]`; Space on a folder shows its total size ✅ (can be turned off ✅).

## W16 Search
1. Alt+F7 ✅ → dialog. 2. Type name pattern; choose folders/drives, archives, depth; optionally text in files, regex, encoding ✅. 3. Start → results list at the bottom, usable while running ✅. 4. Go to file, or Feed to listbox ✅; Ctrl+C copies the results ✅.
Quick search: Ctrl+S, type; Ctrl+S inside toggles the live filter ✅.

## W17 Sort / group
Sort by column title click `[nicht belegt]`; no grouping `[nicht belegt]`.

## W18 Views
Brief, full, thumbnails, tree, Quick View ✅ names; the keys `[nicht belegt]` (Ctrl+Q ⚠️).

## W19 Tabs
Folder tabs per panel ✅; open/close/lock keys `[nicht belegt]`.

## W20 Open with
Enter runs the associated program `[nicht belegt]`; view F3 / edit F4 ⚠️.

## W21 Archives
1. Enter on an archive → opens like a folder ✅ (formats ✅). 2. Copy files out with F5 `[nicht belegt]`. 3. Pack: Alt+F5, unpack: Alt+F6 ⚠️.

## W22 Synchronize directories (extra)
1. Set left and right folders, filter, options (Asymmetric, Subdirs, By content, Ignore date) ✅. 2. **Compare** → list with a direction per file ✅. 3. Change directions by hand ✅. 4. **Sync** → confirmation of choices ✅ → copies. Close leaves ✅.
