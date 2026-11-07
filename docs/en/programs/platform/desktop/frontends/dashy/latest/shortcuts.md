# Dashy - Keyboard Shortcuts

## Overview

Dashy is designed for keyboard operation: there is **no activation key for the search** — simply typing is enough. In addition there are keys for navigating, opening and clearing, as well as optional **hotkeys per tile** (`0`–`9`). The combinations shown here correspond to the official documentation; keys beyond these do not exist.

---

## General

| Shortcut | Function |
|----------|----------|
| *just type* | Start search without focusing a field; matches filter in real time |
| `Esc` | Clear search term, close open modal windows |
| `Enter` | Open the first match or start the web search |
| `Tab` | Cycle through tiles or matches |
| `Shift+Tab` | Backwards through tiles/matches |
| `↑` `↓` `←` `→` | Navigate between tiles and matches |
| `0` – `9` | Start the tile with the stored `hotkey` (must be set in the configuration) |
| `F5` / `Ctrl+R` | Reload, status indicators are checked again |

---

## Starting tiles

| Shortcut | Function |
|----------|----------|
| `Enter` | Start tile with the configured opening mode (`target`: new tab, same tab, modal, workspace …) |
| `Alt+Enter` | Open tile in modal window |
| `Ctrl+Enter` | Open tile in a new tab |
| Digit (`0`–`9`) | Open the tile with this hotkey immediately (replaces searching) |
| Right-click | Context menu with all opening modes (mouse, no shortcut) |

---

## Search

| Shortcut | Function |
|----------|----------|
| Typing | Filters by title, URL, provider, description, alias and `tags` |
| `Enter` | Start web search with the configured search engine |
| `/w term` | Shortcut command (`searchBangs`): search the term on Wikipedia |
| `:git term` | Example of a custom shortcut command from the configuration |
| Entering `https://…` | If the option is enabled, jumps directly to the address instead of searching |
| `Esc` | Delete search text, reset view |
| `Backspace` | Remove single characters from the search text |
| `Ctrl+A` | Select search text (standard in the input field) |

**Note on URL aliases**: an `alias` in the configuration allows jumping via the address (`dashy.local/jelly`) — this is not a shortcut but a route.

---

## Navigation

| Shortcut | Function |
|----------|----------|
| `Tab` | Switch between header elements, search bar and tiles |
| `↑` / `↓` | Scroll through result lists and selection fields |
| `←` / `→` | Jump to tiles in the row |
| `Enter` | Trigger the selected element |
| `Esc` | Close open dialogs, withdraw filter |
| `Alt+←` | Back to the previous view (browser) |

**Not available:**

| Desired shortcut | Status |
|----------------------|--------|
| `/` for search field | ❌ Not needed and not assigned — typing works without focus |
| `g` then `s` (switch page) | ❌ Not available — use the page menu or the address |
| Jump to minimal view by key | ❌ Not available — view via menu or URL |

---

## Editing (edit mode)

| Shortcut | Function |
|----------|----------|
| `Tab` | Reach a tile's edit and delete icons |
| `Enter` | Open the edit dialog or save in the dialog |
| `Esc` | Close dialog without saving |
| `Tab` / `Shift+Tab` | Cycle through fields in the tile dialog |
| `↑` / `↓` | Change values in number and selection fields |
| `Enter` (field "URL") | Confirm field |

### Moving and arranging

| Gesture | Function |
|-------|----------|
| Drag the tile | Move tile in the grid (only in edit mode) |
| Drag the section grip zone | Reorder section |
| Context menu → Edit | Change the tile's fields |
| Save | Writes the change to the configuration file |

**Not available:**

| Desired shortcut | Status |
|----------------------|--------|
| `e` for edit mode | ❌ Not documented — use the button in the header area |
| `Del` to delete a tile | ❌ Not available — delete icon in edit mode |
| `Ctrl+Z` undo | ❌ Not available — there are timestamped backups in the `user-data` folder |
| Arrow keys to move | ❌ Not available — only drag & drop |

---

## Views and settings panel

| Shortcut | Function |
|----------|----------|
| `Esc` | Close settings panel and dialogs |
| `Tab` | Cycle through areas of the settings panel |
| `Enter` | Open the selected area, trigger save |
| `Ctrl+F` | Search text on the page (browser), not built into Dashy |

---

## Mac variants

The official documentation names the combinations with `Ctrl` and `Alt`. On macOS the usual equivalents apply; the `Cmd` variants are not documented separately.

| Shortcut | Function |
|----------|----------|
| `Esc` | Clear search, close dialog |
| `Option+Enter` | Open tile in modal (equivalent to `Alt+Enter`) |
| `Cmd+Enter` | Open tile in new tab (equivalent to `Ctrl+Enter`) |
| `Cmd+R` | Reload |
| `Cmd+F` | Text search in the browser |
| `Cmd+K` | Focus address bar (browser) |
| `Cmd+Plus` / `Cmd+Minus` | Zoom |
| `0` – `9` | Tile hotkeys (identical) |

---

## Accessible operation

| Shortcut | Function |
|----------|----------|
| `Tab` | All tiles, links and dialog elements reachable |
| `Enter` | Open tile, save dialog |
| `↑` `↓` `←` `→` | Address grid and targets |
| `Esc` | Leave filter and overlays |
| Typing | Search without mouse click |

Keyboard control fully covers search, navigation and starting; layout changes remain mouse or touch tasks.

---

## Summary

Of the four dashboard programs, Dashy is the only one that offers **consistent keyboard operation**:

- **Typing** starts the search without a focus key
- **`Tab`, `Shift+Tab`, arrow keys** move through tiles and matches
- **`Enter`, `Alt+Enter`, `Ctrl+Enter`** open with different opening modes
- **`Esc`** resets search and overlays
- **`0`–`9`** start tiles stored with a `hotkey`
- **No shortcuts** exist for edit mode, for undo and for reordering
