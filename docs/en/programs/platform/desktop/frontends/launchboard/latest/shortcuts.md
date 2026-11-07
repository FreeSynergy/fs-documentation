# LaunchBoard - Keyboard shortcuts

## Overview

LaunchBoard does **not document any dedicated application shortcuts** for building boards. Operation is via mouse, touch and the standard keyboard of the web components (dialogs, forms, lists). This file lists what actually works and explicitly marks commonly assumed key combinations as **not available**. Since the vendor does not publish a shortcut reference, the basics described here are what can be observed in current versions; details should be checked in the customer portal.

---

## General (browser standard)

| Shortcut | Function |
|----------|----------|
| `Tab` | Jump to the next control |
| `Shift+Tab` | Jump to the previous control |
| `Enter` | Trigger the selected button |
| `Space` | Toggle a switch, activate the marked tile |
| `Esc` | Close dialog, dropdown or menu |
| `F5` / `Ctrl+R` | Reload page |
| `Alt+←` / `Alt+→` | Browser back/forward |
| `Ctrl+P` | Print board |
| `F12` | Developer tools (troubleshooting widget requests) |

---

## Navigation on the board

| Shortcut | Function |
|----------|----------|
| `Tab` | Reach tiles and links in reading order |
| `Enter` | Focused app tile opens the target URL |
| `↑` / `↓` | Scroll through dropdowns (board selection, integration selection) |
| `↑` / `↓` | Scroll through the autocomplete list of the search |
| `Enter` | Execute search suggestion |
| `Esc` | Close suggestions, leave focus |
| `Backspace` | Delete search text when the field is focused |
| `Home` / `End` | Start / end of page (browser) |

**Not available:**

| Expected shortcut | Status |
|---------------------|--------|
| `/` for search field | ❌ Not documented – the field must be clicked or reached via `Tab` |
| `1`–`9` for boards | ❌ Not available |
| Letter jump to a tile | ❌ Not available |
| `g` then `b` (switch board) | ❌ Not available |

---

## Editing (board and widgets)

| Shortcut | Function |
|----------|----------|
| `Tab` | Reach the floating tile tools (edit, duplicate, remove) |
| `Enter` | Open the settings dialog of the focused tile |
| `Esc` | Close dialog without saving |
| `Enter` (in dialog) | Trigger the default action "Save" |
| `Esc` (in edit mode) | Leave the mode, provided no dialog is open |
| `Tab` / `Shift+Tab` | Move through fields within the dialog |
| `Space` | Open selection list, toggle switch |
| `↑` / `↓` | Change values in number fields and selections |

**Not available:**

| Expected shortcut | Status |
|---------------------|--------|
| `e` for edit mode | ❌ Not available – only via the button in the header |
| `Ctrl+Z` undo on the board | ❌ Not available – layout changes are saved immediately |
| `Del` to delete a tile | ❌ Not available – use the toolbar or right-click |
| Arrow keys to move a tile | ❌ Not available – drag and drop with mouse or touch |
| `Ctrl+C` / `Ctrl+V` copy a tile | ❌ Not available – use "Duplicate" in the context menu |
| `Ctrl+S` save | ❌ Not available – there is no separate save step |

### Moving and resizing a tile

| Gesture | Function |
|-------|----------|
| Drag at the handle (top left) | Move tile in the grid, target area snaps in |
| Drag at corner/bottom edge | Change width and height in grid steps |
| Long press (touch) | Pick up tile (mobile layout) |
| Board options → number of columns | Change grid density instead of stacking tiles |
| Show alignment lines | Align edges with neighbouring tiles |

---

## Search and start page functions

| Shortcut | Function |
|----------|----------|
| Click in the search bar + text | Matches from boards, apps and links |
| `↑` / `↓` | Move through the results list |
| `Enter` | Open highlighted match or start web search |
| `Esc` | Clear search field or close suggestions |

Short commands in the search text (prefix per search engine) do not replace shortcuts; they are part of the search field.

---

## Instance and user administration

| Shortcut | Function |
|----------|----------|
| `Tab` | Reach table rows and actions (users, integrations) |
| `Enter` | Open the edit dialog of the selected entry |
| `Esc` | Close dialog |
| `↑` / `↓` | Change selections (role, integration type) |
| Text in filter field | Restrict list – the field must be clicked to focus |

**Not available:** `/` for filtering, `Ctrl+F` as application search (the browser only searches visible text).

---

## Mac variants

On macOS the browser keys apply with `Cmd` instead of `Ctrl`.

| Shortcut | Function |
|----------|----------|
| `Cmd+R` | Reload |
| `Cmd+P` | Print |
| `Cmd+F` | Search text on the page (browser) |
| `Cmd+K` | Focus address bar (browser) |
| `Cmd+↑` / `Cmd+↓` | Start / end of page |
| `Cmd+Plus` / `Cmd+Minus` | Zoom the interface |
| `Cmd+0` | Reset zoom |
| `Esc` | Close dialog |

**Not available:** `Cmd+E` (edit), `Cmd+/` (search field), `Cmd+Z` (undo layout), `Cmd+D` (duplicate).

---

## Accessible operation

| Shortcut | Function |
|----------|----------|
| `Tab` | Reach header, tiles, dialog fields |
| `Enter` / `Space` | Trigger tile actions and switches |
| `Esc` | Leave overlays and menus |
| `↑` / `↓` | Operate selections and suggestion lists |
| `Shift+Tab` | Navigate backwards |

**Limitation**: arranging tiles is only possible with a pointing device; there is no keyboard alternative for moving and resizing.

---

## Browser and identity provider keys (at login)

Sign-in often runs via an external OIDC provider; its keys apply there (e.g. tab navigation in the form, `Enter` to submit). Browser password helpers (`Cmd+Shift+L` in some browsers for password management) are browser functions, not LaunchBoard functions.

---

## Summary

LaunchBoard offers **no application-specific shortcuts**. Usable are:

- **Browser keys** for reloading, printing, zoom and text search
- **`Tab`, `Enter`, `Space`, `Esc`, `↑`/`↓`** in dialogs, menus and suggestion lists
- **Drag and drop and touch gestures** for all layout work

Short paths come from organisation: few boards, clear tile names, a configured default search engine and frequently used board favourites in the header.
