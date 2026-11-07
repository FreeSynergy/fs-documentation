# TrueNAS - Keyboard shortcuts

## Overview

TrueNAS does **not document any own keyboard shortcuts** for the web UI. The browser keys apply, as well as the standard keyboard operation of the Angular/NG-ZORRO components (forms, dialogues, menus). Only the **console menu** on the server itself is keyboard-driven (digits for selection). This file lists what really works and explicitly marks commonly assumed shortcuts as **not available**.

> Status: TrueNAS SCALE 24.x/25.x as well as CORE 13. Menu items and console numbers change across versions; check after updates.

---

## General (browser standard)

| Shortcut | Function |
|----------|----------|
| `Tab` / `Shift+Tab` | Reach controls (sidebar, buttons, fields) |
| `Enter` | Trigger selected element, default action in dialogue |
| `Space` | Toggle checkboxes/switches, trigger button |
| `Esc` | Close dialogue, dropdown or job panel |
| `F5` / `Ctrl+R` | Reload page (SPA reloads the current area) |
| `Alt+←` / `Alt+→` | Browser back/forward between visited areas |
| `Ctrl+F` | Search text on the page (browser) |
| `Ctrl+P` | Print view (e.g. reports) |

---

## Search and navigation

| Shortcut | Function |
|----------|----------|
| Click on search field + text | Global search: pages, datasets, shares, apps |
| `↑` / `↓` | Scroll through search suggestions and selection lists |
| `Enter` | Open marked search suggestion |
| `Esc` | Clear search field / close suggestions |
| `Tab` | Reach sidebar items one after another |

**Not available:**

| Desired shortcut | Status |
|----------------------|--------|
| `/` or `Ctrl+K` for global search | ❌ Not documented — focus the search field by clicking/`Tab` |
| `1`–`9` for sidebar areas | ❌ Not available |
| Quick jump to a dataset via shortcut | ❌ Not available |
| `g` then `d` (to datasets) | ❌ Not available |

---

## Forms and wizards

| Shortcut | Function |
|----------|----------|
| `Tab` / `Shift+Tab` | Step through fields of a wizard |
| `Enter` | Trigger default action ("CREATE", "SAVE") |
| `Esc` | Cancel dialogue |
| `Space` | Toggle checkboxes and switches |
| `↑` / `↓` | Change number fields and selection lists |
| `Backspace` / `Del` | Delete field content |

**Not available:**

| Desired shortcut | Status |
|----------------------|--------|
| `Ctrl+S` save | ❌ Not available — saving means "SAVE" by click |
| `Ctrl+Z` undo | ❌ Not available — actions take effect immediately |
| `Del` to delete dataset/snapshot | ❌ Not available — use the three-dot menu |
| Autocomplete in dataset name fields | ❌ Not available (autocomplete only in selected selection fields, version-dependent) |

---

## Tables (datasets, snapshots, apps)

| Shortcut | Function |
|----------|----------|
| `Tab` | Reach row action (three-dot menu), open with `Enter` |
| `↑` / `↓` | Scroll in open menu lists |
| `Esc` | Close menu |

Sorting and filtering work exclusively via mouse clicks on column headers and filter fields.

---

## Confirmation dialogues

| Shortcut | Function |
|----------|----------|
| `Tab` | Reach the "CANCEL" button and the confirming button |
| `Enter` | Trigger confirmation button (in case of danger often only active after text entry) |
| `Esc` | Cancel without executing the action |

---

## App consoles and VM VNC

| Context | Behaviour |
|---------|-----------|
| App console (Docker logs/TTY in the UI) | terminal standard (`Ctrl+C` etc.), click to focus |
| VM VNC console (from 24.10) | keys go to the guest; special combinations (Ctrl+Alt+Del) via the VNC menu of the console, not as direct keys (version-dependent) |
| Web shell (earlier versions/alternative) | shell standard, no TrueNAS keys |

---

## Console menu on the server (keyboard-driven)

On the local screen/serial of the appliance, a menu appears that is operated by digit (numbers version-dependent — the menu item text decides):

| Input | Typical function |
|---------|-------------------|
| Digit + `Enter` | select menu item (network, shell, import, reset UI …) |
| `Enter` | menu back / confirm selection |
| `Ctrl+C` | abort running query (shell level) |

After choosing **"Shell"**, normal Linux bash applies (CORE: FreeBSD shell): `midclaw call` or `midclt call` for API calls (see [api.md](api.md)).

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
| `Esc` | Close dialogue |

**Not available:** `Cmd+S` (save), `Cmd+K` (search in TrueNAS), `Cmd+E` (edit).

---

## Accessible operation

| Shortcut | Function |
|----------|----------|
| `Tab` | Sidebar, tables, dialogues reachable |
| `Enter` / `Space` | Trigger actions |
| `Esc` | Leave overlays and menus |
| `↑` / `↓` / `←` / `→` | Operate selections, trees, menus |
| `Shift+Tab` | Navigate backwards |

---

## Summary

TrueNAS offers **no application-specific shortcuts** in the web UI. Efficient work relies on:

- **Global search** (click + typing) instead of clicking through the sidebar
- **`Tab`/`Enter`/`Esc`/arrow keys** in wizards and menus
- **Console menu and `midclaw`/`midclt`** for recurring maintenance steps

Whoever misses keyboard shortcuts automates via the API (see [api.md](api.md)) – there a JSON-RPC call replaces every click sequence.
