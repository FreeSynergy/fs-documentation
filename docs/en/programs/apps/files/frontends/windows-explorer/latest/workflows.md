# Windows Explorer 11 — Workflows

> [Windows Explorer](../index.md) · [description](description.md) · [acceptance](acceptance.md) · [gaps](gaps.md)

Each workflow: goal, preconditions, steps (user does X → program shows Y), error cases, undo. Evidence: ✅ stated on the official pages (2026-11-13); `[nicht belegt]` = not stated there (product knowledge, verify). IDs W1..W21 are the same in the three file-manager dossiers.

## W1 Browse the local file system
Goal: reach Home folder, root, drives, USB, network. Pre: none.
1. Press Win+E ✅ → window opens on Home or This PC (option ✅).
2. Click **This PC** in the navigation pane → drives and removable media appear `[nicht belegt]`.
3. Plug in a USB stick → a drive entry appears in the pane and in This PC `[nicht belegt]`.
4. Click **Network** in the pane → reachable computers `[nicht belegt]`.
5. Open the user's home folder via pinned Quick access ✅ (known folders restorable ✅).
Errors: drive not ready, network path unreachable → message, F5 ✅. Undo: n/a.

## W2 Navigate: open, back, up, breadcrumb, typed path
Goal: move between folders. 
1. Double-click a folder → its content shows `[nicht belegt]`.
2. Alt+Left / Backspace → previous folder; Alt+Right → next ✅.
3. Alt+Up or the Up arrow ✅ → parent folder.
4. Click a segment of the address bar `[nicht belegt]` → that folder.
5. Alt+D / Ctrl+L / F4 ✅ → path becomes editable; type path, Enter → folder opens `[nicht belegt]`.
Errors: path missing → message `[nicht belegt]`. Undo: Back.

## W3 Select
1. Click one item → selected.
2. Ctrl+arrow, Space ✅ → add separate items; or enable check boxes (View > Show > Item check boxes ✅).
3. Shift+arrows ✅ / Shift+click `[nicht belegt]` → range.
4. Ctrl+A → all `[nicht belegt]`; pattern by typing letters jumps only `[nicht belegt]`.
Errors: none. Undo: click empty space.

## W4 Copy / move with the clipboard
Pre: items exist; target folder reachable.
1. Select items (W3).
2. Ctrl+C (copy) or Cut on the bar ✅ → items remembered (cut faded `[nicht belegt]`).
3. Navigate to the target ✅.
4. Ctrl+V or Paste ✅ → progress dialog if long (W8), items appear.
Errors: clash → W7; no space/access → dialog. Undo: W13.

## W5 Copy / move by drag and drop
1. Select items, drag to a folder, pane entry or tab ✅.
2. Hold Ctrl → copy; Shift → move; Alt → shortcut ✅. Default (no key) depends on drive `[nicht belegt]`.
3. Drop → result as W4.
Errors: as W4. Undo: W13.

## W6 Two panes (Zweifenster)
Not offered: one pane per tab ✅ by absence; drag between two windows or tabs is the substitute `[nicht belegt]`.

## W7 Name conflict while copying
1. Paste/drop into a folder holding the same name → dialog "replace or skip" `[nicht belegt]`.
2. Choose replace, skip, or "let me decide for each file" → per-file dialog with both files' info `[nicht belegt]`.
3. "Do this for all" `[nicht belegt]`; keep-both via checking both boxes in the per-file dialog `[nicht belegt]`.
Errors: cancel closes everything. Undo: W13.

## W8 Progress, cancel, pause, background
1. Start a long copy → progress dialog `[nicht belegt]`.
2. Pause / Cancel buttons; "more details" shows speed chart `[nicht belegt]`.
3. Several operations queue in own dialogs/combined `[nicht belegt]`. Cancel keeps what was copied `[nicht belegt]`.

## W9 Rename one item
1. Select; F2 ✅ (or context Rename ✅) → name editable.
2. Type, Enter → renamed; Esc → cancel `[nicht belegt]`.
Errors: forbidden characters, reserved names (see index ✅ rules), name taken `[nicht belegt]`. Undo: W13.

## W10 Rename many
1. Select several, F2 `[nicht belegt]` → first item editable.
2. Enter → all get the same base name with (1), (2)… `[nicht belegt]`.
Errors as W9. Undo: W13.

## W11 Delete
1. Select; Delete or Ctrl+D ✅ → item goes to the Recycle Bin (confirm per setting `[nicht belegt]`).
2. Shift+Delete ✅ → permanent delete, confirm dialog `[nicht belegt]`.
Errors: in use, no right → dialog. Undo: W12/W13; permanent: none.

## W12 Recycle Bin
1. Open Recycle Bin from desktop `[nicht belegt]`.
2. Select item → Restore → returns to original place `[nicht belegt]`.
3. Empty Recycle Bin → confirm → gone `[nicht belegt]`.
Errors: original folder gone → recreated or ask `[nicht belegt]`.

## W13 Undo / redo
1. After copy/move/rename/delete press Ctrl+Z `[nicht belegt]` (not in the shortcut table ✅) → last action reversed; Ctrl+Y → redo.
Errors: permanent delete cannot be undone.

## W14 New file / folder
1. Ctrl+Shift+N ✅ → new folder with name in edit mode `[nicht belegt]`.
2. Context menu on empty space > New > type `[nicht belegt]` → file with name in edit mode.

## W15 Properties
1. Select; Alt+Enter ✅ → properties dialog. 2. Change attributes, OK. Undo: reopen.

## W16 Search
1. Ctrl+E / Ctrl+F / F3 ✅ → search box focused; type → results in the current folder `[nicht belegt]`.
2. From Home: searches PC and, if signed in, cloud ✅.
3. Open a result → opens; "open file location" `[nicht belegt]`.

## W17 Sort / group
1. Sort/Group in the command bar or column headers `[nicht belegt]` → list reorders; direction toggles.

## W18 Views
1. View menu ✅ or Ctrl+Shift+1..9 ✅ → icons, list, details, compact ✅; Ctrl+wheel resizes ✅.

## W19 Tabs
1. Ctrl+T ✅ → new tab. 2. Ctrl+Tab / Ctrl+1..9 ✅ switch. 3. Ctrl+W ✅ close. Drag item onto tab `[nicht belegt]`. Undo: reopen closed tab `[nicht belegt]`.

## W20 Open with
1. Double-click → default program `[nicht belegt]`. 2. Context menu > Open with > choose `[nicht belegt]`.

## W21 Archives
1. Select > Compress to ZIP `[nicht belegt]` → zip next to the files. 2. Open zip like a folder; Extract all `[nicht belegt]`.
