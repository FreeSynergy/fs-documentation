# Synology DSM - Keyboard control

## Overview

DSM does **not provide a public shortcut list**. The portal is designed for mouse and touch; available are the browser standard keys as well as the field and list keyboard operation of the dialogues. This file lists what actually works, explicitly marks commonly assumed combinations as **not available**, and adds the **system commands** that are used instead of virtual shortcuts.

---

## General (browser standard)

| Shortcut | Function |
|----------|----------|
| `Tab` | Jump to the next control |
| `Shift+Tab` | Jump to the previous control |
| `Enter` | Selected button, dialogue action or open the marked file |
| `Space` | Toggle selection, trigger switch |
| `Esc` | Cancel dialogue, context menu or search |
| `F5` / `Ctrl+R` | Reload portal |
| `Alt+←` / `Alt+→` | Browser back/forward (within an application) |
| `Ctrl+P` | Print view (logs, reports) |
| `F12` | Developer tools (useful for observing `entry.cgi`) |

---

## Navigation in the portal

| Shortcut | Function |
|----------|----------|
| `Tab` | Reach upper bar, menu items and windows |
| `Enter` | Trigger menu item or icon, activate window |
| `↑` / `↓` | Scroll in lists and selection fields |
| `←` / `→` | Collapse/expand tree view (File Station) |
| `Home` / `End` | Start / end of list |
| `Esc` | Close main menu, context menu or search |
| `Backspace` | Delete in the search field; in some lists one level back |

**Not available:**

| Expected shortcut | Status |
|---------------------|--------|
| `/` for global search | ❌ Not available – the search field at the top must be clicked |
| `1`–`9` for packages | ❌ Not available |
| Alt+Tab between DSM windows | ❌ Not available – switch windows via app bar or window list |
| `Win` key as "main menu" | ❌ Not available – icon at top left |
| Jump to a desktop widget | ❌ Not available |

---

## Files and folders (File Station)

| Shortcut | Function |
|----------|----------|
| `Enter` | Open marked file or enter folder |
| `Ctrl+A` | Mark all entries in the current list |
| `Ctrl+Click` | Add individual entries to the selection |
| `Shift+Click` | Select range |
| `Del` | Move marked file to recycle bin (confirmation dialogue) |
| `Esc` | Cancel rename or selection process |
| Type text | Jump to the matching name in the list |

**Not clearly documented / not available:**

| Expected shortcut | Status |
|---------------------|--------|
| `F2` rename | not officially documented – use the context menu "Rename" |
| `Ctrl+C` / `Ctrl+V` copy/paste | ❌ Not available – use the context menu or target folder dialogue |
| `Ctrl+Z` undo action | ❌ Not available – use recycle bin or snapshot recovery |
| `Ctrl+X` move | ❌ Not available – use the "Move" dialogue |

---

## Tasks, windows and dialogues

| Shortcut | Function |
|----------|----------|
| `Enter` | Default action of the active dialogue ("OK", "Next") |
| `Esc` | Cancel dialogue, close task overlay |
| `Tab` / `Shift+Tab` | Step through fields in the dialogue |
| `Space` | Open selection list, toggle switch |
| `↑` / `↓` | Change values in number fields and selections |
| `Page Up` / `Page Down` | Switch list sections |

**Not available:** `Ctrl+W` close window (the browser closes the tab), `Ctrl+Q` sign out, dedicated keys for "minimise all windows".

---

## Search and filter

| Shortcut | Function |
|----------|----------|
| Click into search field + text | Start Universal Search |
| `Enter` | Run search, open marked hit |
| `Esc` | Clear search field or close result panel |
| `↑` / `↓` | Move through the results list |
| Filter fields (type, share) | set by clicking – no key shortcuts |

---

## Mac variants

On macOS the browser keys apply with `Cmd` instead of `Ctrl`.

| Shortcut | Function |
|----------|----------|
| `Cmd+R` | Reload portal |
| `Cmd+P` | Print |
| `Cmd+F` | Search text on the page (browser) |
| `Cmd+K` | Focus address bar (browser) |
| `Cmd+A` | Mark all entries |
| `Cmd+Click` | Multiple selection in lists |
| `Cmd+↑` / `Cmd+↓` | Start / end of page |
| `Cmd+Plus` / `Cmd+Minus` | Zoom |
| `Cmd+0` | Reset zoom |
| `Fn+Del` | Delete (corresponds to `Del`) |

**Not available:** `Cmd+E` (file dialogue), `Cmd+/` (search field), `Cmd+Z` (undo operation).

---

## Accessible operation

| Shortcut | Function |
|----------|----------|
| `Tab` | Reach bar, menu, windows and dialogues |
| `Enter` / `Space` | Trigger actions |
| `Esc` | Leave overlays and menus |
| `↑` / `↓` / `←` / `→` | Operate lists and trees |
| `Shift+Tab` | Navigate backwards |
| Browser zoom | usable without loss of function |

**Limitation**: arranging windows, drag-and-drop upload and rectangle multiple selection are only possible with a pointing device.

---

## System commands instead of shortcuts (SSH, admin)

For recurring tasks DSM uses command-line tools instead of key combinations. Access: **Control Panel → Terminal & SNMP → enable SSH service** (port 22).

| Command | Function |
|--------|----------|
| `sudo -i` | switch to root shell |
| `synopkglist` | list installed packages |
| `synopkg status <package>` / `start` / `stop` | control package |
| `synoservice --status` | view system services |
| `synosharectl --list` | list shared folders (parameters depend on DSM version) |
| `synouser --enum priv` | list local accounts |
| `synogroup --enum` | list groups |
| `synodsmnotify @administrators message "text"` | send portal notification |
| `smartctl -a /dev/sataX` | SMART values of a drive |
| `df -h`, `free -m`, `top` | utilisation and storage space |

**Note**: commands can change the system state; create a backup before interventions and record changes in the **Log Centre**.

---

## Summary

DSM offers **no application-specific shortcuts**. Usable are:

- **Browser keys** for reloading, printing, zoom and text search
- **`Tab`, `Enter`, `Esc`, arrow keys, `Ctrl/Cmd+A`** in windows, lists and dialogues
- **System commands** (`synopkg`, `synosharectl`, `synouser`, `synodsmnotify`) for recurring tasks
- **Task scheduler** and **event scripts** as the actual automation path
