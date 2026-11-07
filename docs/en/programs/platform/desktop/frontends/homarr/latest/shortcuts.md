# Homarr - Keyboard Shortcuts

## Overview

Homarr does **not document any own keyboard shortcuts**. Operation is via mouse, touch and the usual browser keys; dialogs and forms follow the standard keyboard behavior of the Mantine components. This file therefore lists what actually works and explicitly marks commonly assumed shortcuts as **not available**.

> Status: current Homarr versions (v1.x). Short-term changes are possible; this list should be checked after updates.

---

## General (browser standard)

| Shortcut | Function |
|----------|----------|
| `Tab` | Jump to the next control |
| `Shift+Tab` | Jump to the previous control |
| `Enter` | Trigger selected button or list |
| `Space` | Toggle switch/checkbox, activate marked tile |
| `Esc` | Close dialog, dropdown or menu |
| `F5` / `Ctrl+R` | Reload page (board is fetched again) |
| `Alt+←` / `Alt+→` | Browser back/forward (board switch, dialog history) |
| `Ctrl+P` | Print board (browser print dialog) |

---

## Navigation in the board

| Shortcut | Function |
|----------|----------|
| `Tab` | Reach tiles and links in reading order |
| `Enter` | Activated app tile opens the target URL |
| `↑` / `↓` | Scroll through dropdowns (board selection, integration selection) |
| `↑` / `↓` | Scroll through the autocomplete list of the search |
| `Enter` | Execute search suggestion |
| `Esc` | Close search suggestions, leave focus |
| `Backspace` | Delete search text when the search field is focused |

**Not available:**

| Desired shortcut | Status |
|----------------------|--------|
| `/` for search | ❌ Not available — search field must be clicked or reached via `Tab` |
| `1`–`9` for boards/tiles | ❌ Not available |
| Quick start of an app by letter | ❌ Not available |
| `g` then `b` (switch board) | ❌ Not available |

---

## Editing (board, widgets)

| Shortcut | Function |
|----------|----------|
| `Tab` | Reach floating tile tools (edit, remove) |
| `Enter` | Open the edit dialog of the focused tile |
| `Esc` | Close widget dialog without saving |
| `Enter` (in dialog) | Trigger default action "Save" |
| `Esc` (in edit mode) | Leave edit mode, provided no dialog is open |
| `Z` / `X` | ❌ Not available — no toggling of the mode by key, only via the button |

**Not available:**

| Desired shortcut | Status |
|----------------------|--------|
| `e` for edit mode | ❌ Not available |
| `Ctrl+Z` undo in the board | ❌ Not available — layout changes are saved immediately |
| `Del` to delete tile | ❌ Not available — use the tool symbol or right-click |
| Arrow keys to move a tile | ❌ Not available — drag & drop with mouse or touch |

### Moving and resizing tiles

| Gesture | Function |
|-------|----------|
| Drag at the grip zone | Move tile in the grid, target area snaps in |
| Drag at bottom edge/corner | Change width/height in grid steps |
| Long press (touch) | Pick up tile (mobile layout) |
| Board options → number of columns | Change grid density instead of stacking individual tiles |

---

## Search and web search

| Shortcut | Function |
|----------|----------|
| Click into search field + text | Filter the board matches |
| `↑` / `↓` | Go through the match list |
| `Enter` | Open first/highlighted match or start web search |
| `Esc` | Clear search field or close suggestions |

Shortcut commands in the search text (so-called bangs) are possible and are described in [features.md](features.md); they do not replace shortcuts.

---

## Dialogs and forms

| Shortcut | Function |
|----------|----------|
| `Tab` / `Shift+Tab` | Cycle through fields within the dialog |
| `Enter` | Confirm active field, trigger default action |
| `Esc` | Cancel dialog |
| `Space` | Open selection list, toggle switch |
| `↑` / `↓` | Change values in number fields and selections |
| `Backspace` / `Del` | Delete field content |

---

## Instance and user administration

| Shortcut | Function |
|----------|----------|
| `Tab` | Reach table rows and actions (users, integrations) |
| `Enter` | Open edit dialog of the selected entry |
| `Esc` | Close dialog |
| `/` in search fields | ❌ Not available — focus filter fields manually |

---

## Mac variants

On macOS the browser keys apply with `Cmd` instead of `Ctrl`.

| Shortcut | Function |
|----------|----------|
| `Cmd+R` | Reload |
| `Cmd+P` | Print |
| `Cmd+F` | Search text on the page (browser, not Homarr) |
| `Cmd+K` | Focus address bar (browser) |
| `Cmd+↑` / `Cmd+↓` | Start/end of the page (browser) |
| `Cmd+Plus` / `Cmd+Minus` | Interface zoom |
| `Cmd+0` | Reset zoom |
| `Esc` | Close dialog |

**Not available:** `Cmd+E` (edit), `Cmd+/` (search), `Cmd+Z` (undo layout).

---

## Accessible operation

| Shortcut | Function |
|----------|----------|
| `Tab` | Entire header, tiles and dialogs reachable |
| `Enter` / `Space` | Trigger tile actions |
| `Esc` | Leave overlays and menus |
| `↑` / `↓` | Operate selections and suggestion lists |
| `Shift+Tab` | Navigate backwards |

---

## Summary

Homarr offers **no application-specific shortcuts**. Usable are:

- **Browser keys** for reloading, printing, zoom and text search
- **`Tab`, `Enter`, `Space`, `Esc`, `↑`/`↓`** in dialogs, menus and suggestion lists
- **Drag & drop and touch gestures** for layout work

Anyone expecting abbreviations reaches them via board organization: few boards, clear tile names and a chosen default search engine make the mouse more dispensable than any key combination.
