# Proxmox VE - Keyboard shortcuts

## Overview

Proxmox VE does **not document any own global keyboard shortcuts** for the web interface. Operation is via tree, tabs, buttons and dialogues with the usual browser and form keys. Dedicated keyboard paths exist only **inside the consoles** (node shell, VM serial, noVNC/xterm.js) – there, terminal and guest system conventions apply. This file separates both cleanly and marks commonly assumed shortcuts as **not available**.

> Status: Proxmox VE 8.x. The console technology changes between versions (noVNC → xterm.js); check this list after updates.

---

## General (browser standard)

| Shortcut | Function |
|----------|----------|
| `Tab` / `Shift+Tab` | Reach controls (tree, tabs, buttons, fields) |
| `Enter` | Open/confirm selected element (default action in dialogue) |
| `Space` | Toggle checkboxes/switches, trigger the marked button |
| `Esc` | Close dialogue, dropdown or overlay without change |
| `F5` / `Ctrl+R` | Reload page (state is freshly loaded from the API) |
| `Alt+←` / `Alt+→` | Browser back/forward (object/tab history) |
| `Ctrl+F` | Search text on the page (browser) |
| `Ctrl+P` | Print view (e.g. summary) |

---

## Navigation in the tree and tabs

| Shortcut | Function |
|----------|----------|
| `↑` / `↓` | Scroll in the resource tree and selection lists |
| `←` / `→` | Collapse/expand tree node |
| `Enter` | Open the highlighted tree node |
| `Tab` | Reach the tab bar, switch tab with `Enter` |
| `Ctrl+F` + search text | Search in long tables (browser function) |

**Not available:**

| Desired shortcut | Status |
|----------------------|--------|
| `/` to jump to the search bar | ❌ Not available — click the search field or reach it via `Tab` |
| `1`–`9` for tabs | ❌ Not available |
| Start VM by VMID + Enter | ❌ Not available — use the search field + buttons |
| `g` then `n` (to nodes) | ❌ Not available |

---

## Dialogues and wizards

| Shortcut | Function |
|----------|----------|
| `Tab` / `Shift+Tab` | Step through fields and tabs of the dialogue |
| `Enter` | Trigger default action ("Create", "OK") |
| `Esc` | Cancel dialogue |
| `Space` | Toggle switches, change radio groups |
| `↑` / `↓` | Change number fields and selections |
| `Backspace` / `Del` | Delete field content |

**Not available:**

| Desired shortcut | Status |
|----------------------|--------|
| `Ctrl+S` save | ❌ Not available — saving means "OK/Create/Apply" by click |
| `Ctrl+Z` undo | ❌ Not available — actions take effect immediately, no undo exists |
| `Del` to delete VM/rule | ❌ Not available — action menu (`⋮`) or delete button |
| Arrow keys to reorder boot order | ❌ Not available — drag and drop |

---

## Tables (grids)

| Shortcut | Function |
|----------|----------|
| `↑` / `↓` | Mark row (grid standard) |
| `Enter` | Default action of the marked row (object-dependent) |
| `Tab` | Navigate in rows to action menus/buttons |
| `Esc` | Close open action menus (`⋮`) again |

Everything else works via mouse clicks: `⋮` menus, edit dialogues, task panel.

---

## Consoles: node shell and terminal

The browser shell (`xterm.js`) is a real Linux shell – shell conventions apply, not Proxmox keys:

| Shortcut | Function |
|----------|----------|
| `Ctrl+C` | Abort foreground process |
| `Ctrl+D` | Exit shell |
| `Ctrl+L` | Clear screen |
| `Arrow up/down` | Command history |
| `Tab` | Completion/autocompletion (bash) |

Useful real commands instead of shortcuts: `pvesh get /version`, `qm list`, `pct list`, `pvesm status`.

---

## Consoles: noVNC / xterm.js graphical console of VMs

Keyboard input goes to the **guest** – Proxmox does not send special combinations via direct keys:

| Action | Route |
|--------|-----|
| `Ctrl+Alt+Del` (guest) | Send via the console menu (cog/keys menu) – otherwise the browser would trigger browser actions for this combination (version-dependent) |
| Special characters/F keys | Console menu "Special keys" or guest-faithful input after clicking into the console |
| Clipboard/paste | Via console menu (version-dependent) |

**Not available:** no Proxmox key for switching between console types (noVNC/xterm.js/SPICE) – this is handled by the dropdown in the object header.

---

## Mac variants

On macOS the browser keys apply with `Cmd` instead of `Ctrl`; consoles forward `Cmd` combinations to the guest depending on settings (version-dependent).

| Shortcut | Function |
|----------|----------|
| `Cmd+R` | Reload |
| `Cmd+P` | Print |
| `Cmd+F` | Text search (browser) |
| `Cmd+K` | Focus address bar (browser) |
| `Cmd+↑` / `Cmd+↓` | Start/end of page (browser) |
| `Cmd+Plus` / `Cmd+Minus` / `Cmd+0` | Zoom |
| `Esc` | Close dialogue |

**Not available:** `Cmd+S` (save), `Cmd+/` (search), `Cmd+E` (edit).

---

## Accessible operation

| Shortcut | Function |
|----------|----------|
| `Tab` | Tree, tabs, buttons, dialogue fields reachable |
| `Enter` / `Space` | Trigger actions |
| `Esc` | Leave overlays |
| `↑` / `↓` / `←` / `→` | Operate tree, lists, selections |
| `Shift+Tab` | Navigate backwards |

---

## Summary

Proxmox VE offers **no application-specific shortcuts** in the web UI. Working efficiently means:

- **Search bar** (VMID/name/tag) instead of clicking through the tree, **`Tab`/`Enter`/`Esc`** in dialogues
- **Browser keys** for reloading, search and zoom
- **Shell/console** with Linux standard keys and `pvesh`/`qm`/`pct` for recurring tasks

Whoever needs real shortcuts moves them into the API or CLI (see [api.md](api.md)) – there a single command replaces every mouse click chain.
