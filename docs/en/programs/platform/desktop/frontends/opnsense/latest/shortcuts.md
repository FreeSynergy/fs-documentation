# OPNsense - Keyboard shortcuts

## Overview

OPNsense does **not document its own keyboard shortcuts** for the web UI. The browser keys apply, as well as the standard keyboard operation of the form and table components (Ant Design/Bootstrap mix). Efficient keyboard paths exist only in the **console/shell** of the device (Linux-like BSD shell, vi, `opnsense-repl`). This file lists what is really usable and explicitly marks commonly assumed shortcuts as **not available**.

> Status: OPNsense 24.x/25.x (22.7+ UI). Check this list after major updates.

---

## General (browser standard)

| Shortcut | Function |
|----------|----------|
| `Tab` / `Shift+Tab` | Reach menu items, buttons, fields |
| `Enter` | Trigger the selected element, dialogue default action |
| `Space` | Toggle checkboxes/switches |
| `Esc` | Cancel edit dialogue, close selection lists |
| `F5` / `Ctrl+R` | Reload page |
| `Alt+←` / `Alt+→` | Browser back/forward between visited pages |
| `Ctrl+F` | Search text on the page (browser) |
| `Ctrl+P` | Print page (e.g. rule overview) |
| `F12` | Developer tools — officially recommended for reading UI calls (`/api/...`) for API use |

---

## Menu and navigation

| Shortcut | Function |
|----------|----------|
| `Tab` | Reach top menu, open with `Enter`, step through submenu |
| `↑` / `↓` | Scroll in open dropdowns |
| `Esc` | Close open menu |

**Not available:**

| Desired shortcut | Status |
|----------------------|--------|
| `/` for search | ❌ Not available — click the search field in the grid |
| `1`–`6` for top menus | ❌ Not available |
| Global command palette (`Cmd+K`) | ❌ Not available |
| Jump to "Firewall ▸ Rules" via key shortcut | ❌ Not available |

---

## Grids (rules, aliases, logs)

| Shortcut | Function |
|----------|----------|
| Click search field + text | Server-side search (`searchPhrase`), result list reloaded |
| `Enter` | Confirm search (where a search button exists) |
| `Tab` + `Enter` | Open the `⋮` row menu and trigger an item |
| `Esc` | Close row menu |

**Not available:**

| Desired shortcut | Status |
|----------------------|--------|
| Arrow keys to move a rule | ❌ Not available — drag and drop on the handle |
| `Del` to delete a rule | ❌ Not available — `⋮` menu Delete |
| `Ctrl+A` multi-select | ❌ Not available (no bulk editing in standard grids) |
| `x` to deactivate a rule | ❌ Not available — Deactivate in the menu |

---

## Forms and dialogues

| Shortcut | Function |
|----------|----------|
| `Tab` / `Shift+Tab` | Step through fields and accordion sections |
| `Enter` | Trigger "Save"/default action |
| `Esc` | Close dialogue (discard unsaved values) |
| `Space` | Toggle switches, change radio groups |
| `↑` / `↓` | Change number fields and selections |
| `Backspace` / `Del` | Delete field content |

Important: **Save** only stores the configuration — rules/services only become active via the **Apply** button at the top of the page (no keyboard path for this is documented).

---

## Type-ahead selects (selection fields)

| Input | Function |
|---------|----------|
| Type text | Filters long selection lists (interfaces, aliases, certificates) |
| `Enter` | Accept the highlighted entry |
| `Backspace` | Delete the last letter of the filter chain |
| Click the `x` in the field | Reset selection (no key documented) |

---

## Console and shell on the device

The console menu of the firewall is number-driven (numbers depend on the version – read the menu text); afterwards standard BSD shell rules apply:

| Input | Function |
|---------|----------|
| Digit + `Enter` | Console menu item (interfaces, shell, reboot …) |
| `Ctrl+C` | Abort (shell) |
| Tab completion | in `opnsense-repl` and modern shells |
| `opnsense-repl` | interactive Python REPL with system access |
| `opnsense update` / firmware menu item | updates (menu-guided, version-dependent) |

This is not web UI control, but the real keyboard path for maintenance.

---

## API workflows via keyboard (indirect)

The officially recommended way to learn API calls: **`F12` → Network tab → trigger UI action → copy request**. This does not replace a shortcut system, but it is the documented learning path (developer documentation).

---

## Mac variants

On macOS the browser keys apply with `Cmd` instead of `Ctrl`.

| Shortcut | Function |
|----------|----------|
| `Cmd+R` | Reload |
| `Cmd+P` | Print |
| `Cmd+F` | Text search (browser) |
| `Cmd+K` | Focus address bar (browser) |
| `Cmd+↑` / `Cmd+↓` | Start/end of page (browser) |
| `Cmd+Plus` / `Cmd+Minus` / `Cmd+0` | Zoom |
| `Esc` | Close dialogue/menu |

**Not available:** `Cmd+S` (save), `Cmd+/` (search), `Cmd+E` (edit).

---

## Accessible operation

| Shortcut | Function |
|----------|----------|
| `Tab` | Top menu, grid actions, dialogue fields reachable |
| `Enter` / `Space` | Trigger buttons and switches |
| `Esc` | Leave overlays |
| `↑` / `↓` | Operate selection lists and dropdowns |
| `Shift+Tab` | Navigate backwards |

---

## Summary

OPNsense offers **no application-specific shortcuts** in the web UI. Practically useful are:

- **Browser keys** plus `F12` network trace as the official API learning tool
- **`Tab`/`Enter`/`Esc`/arrow keys** in grids, accordions and dialogues
- **Console menu + shell** (`opnsense-repl`) for maintenance without a browser

Recurring rule/alias work belongs in the API anyway (see [api.md](api.md)) – there a `curl` replaces every click sequence and every missing shortcut.
