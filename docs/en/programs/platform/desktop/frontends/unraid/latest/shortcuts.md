# Unraid - Keyboard shortcuts

## Overview

Unraid does **not ship its own keyboard shortcuts**. The web interface follows the usual browser keys; forms, dialogues and tables use the standard keyboard operation of HTML elements. This file lists what actually works and explicitly marks commonly assumed shortcuts as **not available**.

> Status: current Unraid versions (6.12/7.x). Minor changes are possible; this list should be checked after updates.

---

## General (browser standard)

| Shortcut | Function |
|----------|----------|
| `Tab` | Jump to the next control (buttons, fields, links) |
| `Shift+Tab` | Jump to the previous control |
| `Enter` | Trigger focused button/link, submit form |
| `F5` / `Ctrl+R` | Reload page (status is fetched fresh) |
| `Alt+←` / `Alt+→` | Browser back/forward between already visited tabs/pages |
| `Ctrl+F` | Search text on the page (browser, not Unraid) |
| `Ctrl+P` | Print page (e.g. array overview) |
| `F12` | Open developer tools (useful for API/form analysis) |
| `Alt+F4` / close tab | Close page — session remains open on the server until timeout |

---

## Navigation between tabs

| Shortcut | Function |
|----------|----------|
| `Tab` + `Enter` | Reach the tab link in the header and open it |
| Browser history (`Alt+←`) | Return to the last visited tab |

**Not available:**

| Desired shortcut | Status |
|----------------------|--------|
| `1`–`9` for tabs (Main, Shares, Docker …) | ❌ Not available |
| `g` then `s` (to Settings) | ❌ Not available |
| `/` for search | ❌ Not available — the app store search must be clicked |
| Quick start of a container by letter | ❌ Not available |

---

## Forms and dialogues

| Shortcut | Function |
|----------|----------|
| `Tab` / `Shift+Tab` | Step through fields of a dialogue |
| `Enter` | Trigger default action of the dialogue (usually "Apply") |
| `Esc` | Close some overlay dialogues (not implemented everywhere) |
| `Space` | Toggle checkboxes/switches, trigger buttons |
| `↑` / `↓` | Scroll in selection lists (disk assignment, template list) |
| `Backspace` / `Del` | Delete field content |

**Not available:**

| Desired shortcut | Status |
|----------------------|--------|
| `Ctrl+S` save | ❌ Not available — saving is always "Apply" by click |
| `Ctrl+Z` undo | ❌ Not available — changes take effect immediately |
| `Del` to delete share/container | ❌ Not available — use the button in the dialogue |
| Autocomplete in the terminal field | ❌ Not available (web terminal plugin: browser standard) |

---

## Docker and VM operation

| Shortcut | Function |
|----------|----------|
| `Tab` + `Enter` | Reach actions in the container/VM table (start, logs, …) |
| `Esc` | Leave webVNC/console overlay, provided UI focus is active |
| `Ctrl+C` (in web terminal) | Abort process in the embedded terminal (terminal standard) |

### webVNC console of a VM

In the browser VNC console the keys of the **guest VM** apply, not those of Unraid:

| Combination | Function |
|-------------|----------|
| Keys directly | passed through to the guest VM |
| `Ctrl+Alt` | may trigger browser shortcuts — when in doubt, click the VNC focus |
| Special actions (Ctrl+Alt+Del) | send via the webVNC toolbar, not via keyboard (version-dependent) |

**Not available:** no Unraid key that switches the VM console, stops it or toggles full-screen mode.

---

## App store and search

| Shortcut | Function |
|----------|----------|
| Click into search field + text | filter apps/plugins in the Apps/Docker tab |
| `Enter` | run search |
| `Esc` | partially clear search text (field-dependent) |

---

## Terminal/CLI on the server

On the console (screen at the server) or via SSH the normal Linux shell applies — no Unraid-specific keys. Practical real commands:

| Command | Function |
|--------|----------|
| `unraid-api status` | check status of the API component (current versions) |
| `unraid-api developer --sandbox true` | enable GraphQL sandbox |
| `diagnostics` | create a diagnostics package for support |

These are not shortcuts but console commands — listed for completeness.

---

## Mac variants

On macOS the browser keys apply with `Cmd` instead of `Ctrl`.

| Shortcut | Function |
|----------|----------|
| `Cmd+R` | Reload |
| `Cmd+P` | Print |
| `Cmd+F` | Search text on the page (browser) |
| `Cmd+K` | Focus address bar (browser) |
| `Cmd+↑` / `Cmd+↓` | Start/end of page (browser) |
| `Cmd+Plus` / `Cmd+Minus` / `Cmd+0` | Zoom of the interface |
| `Esc` | Close dialogue (where implemented) |

**Not available:** `Cmd+S` (save), `Cmd+/` (search), `Cmd+E` (edit).

---

## Accessible operation

| Shortcut | Function |
|----------|----------|
| `Tab` | Tabs, table actions and dialogue fields reachable |
| `Enter` / `Space` | Trigger buttons and links |
| `Esc` | Leave overlays (not implemented everywhere) |
| `↑` / `↓` / `←` / `→` | Operate selection fields and radio groups |
| `Shift+Tab` | Navigate backwards |

---

## Summary

Unraid offers **no application-specific shortcuts**. Usable are:

- **Browser keys** for reloading, printing, zoom and text search
- **`Tab`, `Enter`, `Space`, `Esc`, `↑`/`↓`** in forms and dialogues
- **Linux shell commands** (incl. `unraid-api`) on the console or SSH

Whoever expects shortcuts reaches them through structure: a fixed tab order, meaningful share and container names, and API keys for recurring tasks replace every keyboard combination.
