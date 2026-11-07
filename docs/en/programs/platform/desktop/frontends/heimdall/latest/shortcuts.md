# Heimdall - Keyboard Shortcuts

## Overview

Heimdall provides **no own keyboard shortcuts** and does not document any. Operation follows the usual browser keys and the standard keys of HTML forms. This file records what actually works and explicitly marks commonly expected shortcuts as **not available**.

> Status: current Heimdall versions (v2.x). Details may change with updates.

---

## General (browser standard)

| Shortcut | Function |
|----------|----------|
| `Tab` | Jump to the next control (link, field, button) |
| `Shift+Tab` | Select the previous control |
| `Enter` | Open focused tile, save form |
| `Space` | Toggle the checkbox "open in new tab" |
| `Esc` | Cancel browser dialog, leave focus from some fields |
| `F5` / `Ctrl+R` | Reload page (statistics values are fetched again) |
| `Alt+←` | Back to the previous page (browser) |
| `Ctrl+P` | Print the start page |

---

## Navigation on the start page

| Shortcut | Function |
|----------|----------|
| `Tab` | Reach panels and tiles in reading order |
| `Enter` | Focused tile opens the target URL |
| `↑` / `↓` | Scroll through selection lists (search engine, enhanced-app type) |
| `Spacebar` | Open the selection list when it is focused |
| `Home` / `End` | Start / end of the page (browser) |

**Not available:**

| Desired shortcut | Status |
|----------------------|--------|
| `/` for search field | ❌ Not available — the search field must be clicked or reached via `Tab` |
| Digits `1`–`9` for tiles | ❌ Not available |
| Letter quick-start for an app | ❌ Not available |
| `↑`/`↓` to switch between panels | ❌ Not available — only scrolling or keyboard scrolling |

---

## Editing (apps, panels, layout)

| Shortcut | Function |
|----------|----------|
| `Tab` | Reach the tile's edit symbols and dialog fields |
| `Enter` | Open the "Edit app" dialog or save |
| `Esc` | Cancel browser dialog ("Really delete?") |
| `Backspace` | Delete text in title/URL fields |
| `Enter` (in URL field) | Confirm field, not open the app |

### Arranging tiles and panels

| Gesture | Function |
|-------|----------|
| Drag the tile | Move tile within the panel |
| Drag tile onto another panel | Place tile in another area |
| Drag the panel grip zone | Reorder panels |
| Panel tool "wrap" | Split area so that tiles stand side by side |

**Not available:**

| Desired shortcut | Status |
|----------------------|--------|
| `e` for layout editing | ❌ Not available — only via the settings button |
| `Del` to delete a tile | ❌ Not available — use the delete symbol or dialog |
| `Ctrl+Z` for undo | ❌ Not available — changes are saved immediately |
| Arrow keys to reorder tiles | ❌ Not available — drag & drop with mouse or touch |

---

## Search

| Shortcut | Function |
|----------|----------|
| Click into the search field + text | Enter search term |
| `Enter` | Start search with the configured search engine |
| `Backspace` | Delete characters |
| `Esc` | No own behavior in Heimdall (search field stays filled) |
| `Ctrl+F` | Search text on the page (browser), to find app names |

---

## Forms and dialogs

| Shortcut | Function |
|----------|----------|
| `Tab` / `Shift+Tab` | Cycle through fields (title, URL, icon, colour) |
| `Enter` | Trigger the default action "Save" |
| `Space` | Toggle switches and checkboxes |
| `↑` / `↓` | Change values in selection fields |
| `Esc` | Cancel browser confirmation dialog |

---

## Sign-in

| Shortcut | Function |
|----------|----------|
| `Tab` | Switch between email field and password field |
| `Enter` | Sign in |
| `Caps Lock` | Browser notice when capitals are active |

---

## Mac variants

On macOS, `Cmd` combinations replace the `Ctrl` variants.

| Shortcut | Function |
|----------|----------|
| `Cmd+R` | Reload, update statistics values |
| `Cmd+F` | Search text on the page |
| `Cmd+P` | Print |
| `Cmd+K` | Focus address bar (browser) |
| `Cmd+↑` / `Cmd+↓` | Start / end of the page |
| `Cmd+Plus` / `Cmd+Minus` | Interface zoom |
| `Cmd+0` | Reset zoom |
| `Esc` | Cancel browser dialog |

**Not available:** `Cmd+E` (layout editing), `Cmd+/` (search field), `Cmd+Z` (undo in layout).

---

## Accessible operation

| Shortcut | Function |
|----------|----------|
| `Tab` | All links, fields and buttons reachable |
| `Enter` | Trigger tile and buttons |
| `Esc` | Cancel confirmation dialogs |
| `↑` / `↓` | Operate selection fields |
| `Shift+Tab` | Navigate backwards |

**Limitation**: reordering tiles and panels is possible only with pointing devices; there are no keyboard commands for it.

---

## Summary

Heimdall offers **no application-specific shortcuts**. Usable are:

- **Browser keys** for reloading, searching text, printing and zoom
- **`Tab`, `Enter`, `Space`, `Esc`** in forms, dialogs and confirmation prompts
- **Drag & drop** for all layout changes

Work does not get faster via keys, but via organization: few panels, clear tile names and a configured search engine.
