# Total Commander — Menus

> [Total Commander](../index.md) · [description](description.md)

Source: the official English help of Total Commander 11.58 (menu chapters and "Local menus", retrieved 2026-11-13) ✅. Entries are listed by name only, descriptions are in own words. The menu file can be changed by the user (wcmd_*.mnu), so a given installation may differ ✅. Every entry is an internal `cm_` command ✅.

## Menu bar

Files, Mark, Commands, Net, Show, Configuration, Start, Help ✅ (F9 opens the menu of the active panel, F10 the left one ✅).

### Files

Change attributes · Pack · Unpack specific files · Test archives · Compare by content · Associate with… · Internal associations · Properties · Calculate occupied space · Multi-rename tool · Edit comment · Print (submenu) · — · Split file · Combine files · Encode file · Decode file · Create checksum files · Verify checksums · — · Quit ✅.

### Mark

Select group · Unselect group · Select all · Unselect all · Invert selection · Select all with same extension · Save selection · Restore selection · Save selection to file · Restore selection from file · Copy selected names to clipboard · …names with path · …with all details · …with path and details · — · Compare directories · Mark newer, hide same ✅.

### Commands

CD tree · Search · Search in a separate process · Volume label · System information · Synchronize dirs · Directory hotlist · Go back · — · Open command prompt · — · Branch view · Open desktop folder · Background transfer manager · — · Source<->Target · Target=Source ✅.

### Net

Network connections · Disconnect network drives · Share directory · Unshare directory · Show admin shares · — · FTP commands · PORT connection to another PC ✅.

### Show

Brief · Full · Comments · Custom columns · Custom view modes · Tree · Separate tree · Thumbnail view · Quick view · Vertical alignment · New folder tab · — · All files · Programs · *.* · Custom… · Only selected files · — · Name · Extension · Time · Size · Unsorted · — · Reversed order · — · Reread source ✅.

### Configuration

Options · Change button bar · Button bar 2 (vertical) · Change settings files directly · Dark<->Normal · Save position · Save settings ✅.

### Start

User-defined list of favourite programs, started with the file under the cursor; editable through "Change start menu" ✅.

### Help

Index · Keyboard · Registration info · Website · Check for updates now · About (shows version and the location of the settings and program files) ✅.

## Context menus (right button / Shift+F10)

Opened by right click; in the file panels also by Shift+F10; if the right button is used for selecting, hold it about one second ✅. Right click can be set to select instead of open a menu ✅.

| Object | Entries | Mark |
|--------|---------|------|
| File or folder (also several selected) | The system shell menu of the item (extensions of other programs appear there), plus an "X64" submenu (in the 32-bit program) or "X32" submenu (in the 64-bit program) to reach shell extensions of the other bitness, configurable; Copy and Cut put the items on the clipboard | ✅ |
| Panel background or the current path | Submenu **New** to create files of a chosen type; Paste into the target path | ✅ |
| Current path / drive list / drive button | Local menu of the path and drive; one-second right click on the path opens the history list | ✅ |
| Folder tab | Duplicate; rename/lock; lock; locked but changes allowed; copy to other panel; save tabs (one or both sides); load tabs (keep or replace); close this; close all (locked stay); close duplicates; recently closed; configure view modes; list of view modes | ✅ |
| F8 button | Local menu for the recycle bin | ✅ |
| Button bar button | Edit or delete the button | ✅ |
| FTP list | Add chosen files to a list for later download | ✅ |
| Directory hotlist entry | Add current dir, Remove current dir, Configure | ✅ |
| Search result | Go to file, feed to listbox, view, edit | ✅ |
| Multi-Rename list item | Reorder (Shift+cursor or drag) | ✅ |
| Overwrite dialog, thumbnails/icons | The normal item context menu | ✅ |
| Copy/Move OK and Queue buttons | Right click switches copy to move (or move to copy) | ✅ |
| Archive | Entries of the shell menu | `[nicht belegt]` (no separate archive menu described) |

## Directory hotlist menu

Entries open folders, network folders, FTP, file-system-plugin folders, websites, internal functions, programs and documents ✅. Bottom: Add current dir (hidden if listed), Remove current dir (shown only if listed), Configure (editor to add, change, reorder, delete) ✅.
