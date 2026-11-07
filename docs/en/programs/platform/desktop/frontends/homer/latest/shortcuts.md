# Homer - Keyboard Shortcuts

## Overview

Homer ships **no own keyboard shortcuts** and documents none. The page consists of links and a search field; operation is via the usual browser keys. This file lists what is actually available and explicitly marks commonly expected shortcuts as **not available**.

> Status: current Homer versions (v23/v24). Details may change; the bundled documentation of the version in use is authoritative.

---

## General (browser standard)

| Shortcut | Function |
|----------|----------|
| `Tab` | Jump to the next link or field (header, icon links, search field, tiles) |
| `Shift+Tab` | Select the previous element |
| `Enter` | Open the focused link |
| `Esc` | No behavior in Homer; at most cancels a browser dialog |
| `F5` / `Ctrl+R` | Reload, which loads `config.yml` again |
| `Alt+←` | Back (browser), helpful after clicking a tile |
| `Ctrl+P` | Print start page |
| `Ctrl+D` | Save start page as bookmark |

---

## Navigation on the page

| Shortcut | Function |
|----------|----------|
| `Tab` | Reach groups and tiles in reading order |
| `Enter` | Tile opens the set target (often new tab) |
| `Home` / `End` | Start / end of the page |
| `↑` / `↓` | Scrolling (browser standard, no jump list) |
| `Spacebar` | Scroll down (when no field is focused) |
| `Shift+Spacebar` | Scroll up |

**Not available:**

| Desired shortcut | Status |
|----------------------|--------|
| `/` for the search field | ❌ Not available — the field must be clicked or reached via Tab |
| Digits `1`–`9` for tiles | ❌ Not available |
| Letter quick start for a group | ❌ Not available |
| Jump to group via `g` + letter | ❌ Not available — there are no anchor jumps |

---

## Search

| Shortcut | Function |
|----------|----------|
| Click into the search field + text | Filters tiles immediately (name and `keywords`) |
| `Backspace` | Remove characters from the search text |
| `Ctrl+A` | Select search text (standard in input fields) |
| `Enter` | No own effect — Homer opens no match, it only shows the filter list |
| `Esc` | Does not clear the field automatically; delete text with `Ctrl+A` and `Del` |
| `Tab` | From the search field jump to the first tile |

**Note**: the search is a pure filter. There is no suggestion list that could be traversed with the arrow keys.

---

## Editing

Homer has **no editing mode** and no interface for changing the page.

| Shortcut | Function |
|----------|----------|
| — | ❌ No `e` for an edit mode |
| — | ❌ No `Del` to delete a tile |
| — | ❌ No `Ctrl+Z` (nothing is changed in the page) |
| — | ❌ No arrow keys to move tiles |

Changes are made in `assets/config.yml` and take effect after reloading:

| Step | Route |
|--------|-----|
| Edit file | editor, Git, deployment |
| Make effective | reload page (`F5` / `Ctrl+R`, Mac: `Cmd+R`) |
| Save | `git commit` or download of the configuration, if activated |

---

## Configuration change outside the page

| Step | Typical route |
|---------|---------------|
| Open file | `assets/config.yml` in the editor or in the Git client |
| Check change | run `git diff`, then reload the page |
| Roll out | deployment, volume exchange or `git pull` on the host |

## Icon links and header
| Shortcut | Function |
|----------|----------|
| `Tab` | Reach the icon links in the header |
| `Enter` | Open the link in the set target |
| `Shift+Click` / `Ctrl+Click` | Open link in new tab (browser) |
| `Middle mouse button` | Open link in new tab (browser) |

---

## Dialogs (browser dialogs only)

| Shortcut | Function |
|----------|----------|
| `Esc` | Close download or confirmation dialog of the browser |
| `Enter` | Confirm dialog |
| `Tab` | Switch between dialog buttons |

The configuration download creates a browser dialog; Homer itself opens no dialog windows.

---

## Mac variants

| Shortcut | Function |
|----------|----------|
| `Cmd+R` | Reload (load new configuration) |
| `Cmd+F` | Search text on the page (browser) |
| `Cmd+T` | New tab |
| `Cmd+Click` | Open tile in new tab |
| `Cmd+D` | Create bookmark |
| `Cmd+P` | Print |
| `Cmd+Plus` / `Cmd+Minus` | Zoom |
| `Cmd+0` | Reset zoom |
| `Cmd+↑` / `Cmd+↓` | Start / end of the page |

**Not available:** `Cmd+/` (search field), `Cmd+E` (edit), `Cmd+Z` (undo).

---

## Accessible operation

| Shortcut | Function |
|----------|----------|
| `Tab` | All tiles and links reachable |
| `Enter` | Trigger link |
| `↑` / `↓` / `Spacebar` | Scroll content |
| `Home` / `End` | Quickly to the start or end |
| `Shift+Tab` | Navigate backwards |

Since Homer renders only links, keyboard operation is complete; there are no complex operating elements requiring mouse skills.

---

## Summary

Homer offers **no application-specific shortcuts**. Usable are:

- **Browser keys** for reloading, text search, printing, zoom and bookmarks
- **`Tab`, `Enter`** to reach and open tiles
- **Typing in the search field** as the only interaction of the page

All changes to the structure happen in the configuration file — there the editor replaces every key combination.
