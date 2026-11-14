# KDE Discover — Workflows

> [KDE Discover](../index.md) · [description](description.md) · [acceptance](acceptance.md) · [gaps](gaps.md)

Format: goal, steps (user does X → program shows Y), errors, undo. ✅ userbase.kde.org/Discover (fetched 2026-11-14); `[nicht belegt]` not found. The page documents no error cases and no undo.

## W1 Search
Goal: find a program. Precondition: none.
1. Open the category (Applications, Plasma Add-ons or Application Add-ons) → the list shows ✅ (search is limited to the open category).
2. Type a name or a purpose in the search field (selected on start; Ctrl+F) → matching entries show ✅.
3. Select an entry → details on the right ✅. Back returns ✅.
Errors: empty result `[nicht belegt]`. Undo: n/a.

## W2 Install
Goal: install a program. Precondition: it is listed.
1. Select it, press Install (middle list or bottom right of the details) → installation starts ✅.
2. If a Sources button shows: choose repository, Snap or Flatpak ✅; the default comes from Preferences ✅.
Errors: failure messages, progress `[nicht belegt]`. Undo: Uninstall (W3).

## W3 Uninstall
Goal: remove a program.
1. Find it (its button reads "remove") or open Installed and scroll ✅.
2. Press "remove" → a password is asked ✅; enter it → removed ✅.
Errors: wrong password `[nicht belegt]`. Undo: install again (W2).

## W4 Update
Goal: update installed programs.
1. The update section at the bottom of the left column is bright yellow ✅ → click it → the list of updates shows ✅.
2. Optionally uncheck entries to hold them back; click a row for more information ✅.
3. Press Update at the top right ✅.
Errors, progress `[nicht belegt]`. Undo: `[nicht belegt]`.

## W5 Check for updates manually
1. Click Updates in the left column → the Updates view ✅.
2. Press "Check for updates" at the top right → the list is refreshed ✅ (result display `[nicht belegt]`).

## W6 Manage sources
Goal: choose where software comes from.
1. Open Settings → a check box per repository ✅.
2. Check to enable, uncheck to disable ✅.
3. "Make default" picks the preferred source ✅; "Software Sources" opens the advanced tool ✅.
Errors `[nicht belegt]`. Adding a new repository directly is not described ✅. Undo: toggle back.

## W7 Report a bug
The page shows only a picture ✅; steps `[nicht belegt]`.
