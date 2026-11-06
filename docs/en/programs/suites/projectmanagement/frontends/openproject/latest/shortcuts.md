# OpenProject - Keyboard shortcuts

## Overview

OpenProject publishes **no central list of its own keyboard shortcuts**. It is operated
via mouse, touch and the usual browser keys; form fields follow the standard keyboards
of the browser, the rich-text editor follows common editor conventions. This file lists
what actually works and explicitly marks widely assumed shortcuts as **not available**.

> State: current OpenProject versions (13.x/14.x line). Details can change per version; check this list after updates.

---

## General (browser standard)

| Shortcut | Function |
|----------|----------|
| `Tab` | jump to the next control (bar, filters, table) |
| `Shift+Tab` | jump to the previous control |
| `Enter` | trigger the selected button or form action |
| `Space` | mark checkboxes/cells of the multi-selection |
| `Esc` | close open overlay elements (autocomplete, pickers) |
| `F5` / `Ctrl+R` | reload the page |
| `Alt+←` / `Alt+→` | browser back/forward (module switching runs over URLs) |
| `Ctrl+P` | print the current view |
| `Ctrl+F` | search text on the page (browser, not OpenProject) |

---

## Navigation

| Shortcut | Function |
|----------|----------|
| `Tab` | control the module bar, project selector and table rows |
| `Enter` | open the marked table row (detail split) or follow a link |
| `↑` / `↓` | page through selection lists (project, user, version autocomplete) |
| `Esc` | close autocomplete suggestions |
| `Backspace` | delete the search text in the selection field when focused |
| Space + arrows | scroll large tables/Gantt without a mouse pointer (browser) |

**Not available:**

| Desired shortcut | Status |
|------------------|--------|
| `/` for search | ❌ not available — the search field must be clicked or reached via `Tab` |
| `Ctrl+K` / command palette | ❌ not available |
| `g` + letter (jump to module) | ❌ not available |
| `J` / `K` (next/previous item) | ❌ not available |
| Digit keys for modules | ❌ not available |

---

## Editing

| Shortcut | Function |
|----------|----------|
| `Enter` | confirm and save the inline field (inline editing, version-dependent) |
| `Esc` | cancel inline editing, reset the value |
| `Tab` | reach the next inline field (like the tabulator in a form) |
| `Ctrl+A` | select all text in the field/editor (browser) |
| `Ctrl+C` / `Ctrl+V` / `Ctrl+X` | copy, paste, cut (browser) |
| `Ctrl+Z` / `Ctrl+Y` | undo/redo **inside** a still-open text field; no global undo for saved changes |

### Rich-text editor (descriptions, comments)

The editors follow common conventions; an official shortcut list does not exist (version-dependent):

| Shortcut | Function |
|----------|----------|
| `Ctrl+B` | bold |
| `Ctrl+I` | italic |
| `Ctrl+U` | underline |
| `Ctrl+K` | insert link / open the editing bubble |
| `Ctrl+Shift+7` | numbered list (editor convention, not guaranteed) |
| `Ctrl+Shift+8` | bulleted list (editor convention, not guaranteed) |
| `Ctrl+Z` | undo in the editor text |

---

## Search

| Shortcut | Function |
|----------|----------|
| Click the magnifier symbol | open the global search |
| `Enter` | run the search term |
| `Esc` | close the open suggestion list |
| `Ctrl+F` | search the page text (browser) |

**Not available:**

| Desired shortcut | Status |
|------------------|--------|
| Central search hotkey (`/`, `s`, `Ctrl+K`) | ❌ not documented |
| `Ctrl+H` replace in fields | ❌ not available (only browser replace in address/text fields) |

---

## Mac variants

On macOS the browser keys apply with `Cmd` instead of `Ctrl`.

| Shortcut | Function |
|----------|----------|
| `Cmd+R` | reload |
| `Cmd+P` | print |
| `Cmd+F` | search text on the page (browser) |
| `Cmd+A` / `Cmd+C` / `Cmd+V` | select all, copy, paste |
| `Cmd+Z` | undo in the active text field |
| `Cmd+↑` / `Cmd+↓` | start/end of page (browser) |
| `Cmd+Plus` / `Cmd+Minus` / `Cmd+0` | zoom the UI |
| `Cmd+B` / `Cmd+I` / `Cmd+K` | bold, italic, link in the rich-text editor |

**Not available:** `Cmd+K` as the application's command palette (editor link convention see above), `Cmd+E` for edit, `Cmd+S` as a global save button (saving happens via buttons or inline confirmation).

---

## Accessible operation

| Shortcut | Function |
|----------|----------|
| `Tab` / `Shift+Tab` | reach the whole UI backwards/forwards |
| `Enter` / `Space` | trigger buttons, links and markings |
| `Esc` | leave pickers, autocomplete and menus |
| `↑` / `↓` | operate selections and suggestion lists |
| `Ctrl+Plus` | enlarge the UI without loss of function |

---

## Summary

OpenProject offers **no application-specific shortcuts**. Usable are:

- **browser keys** for reload, print, zoom and text search
- **`Tab`, `Enter`, `Esc`, `↑`/`↓`** in forms, autocompletes and the inline table
- **editor conventions** (`Ctrl+B/I/K`) in rich-text fields, covered differently per version

Speed comes instead from saved queries, inline editing and the keyboard confirmation of
table fields — not from hotkeys.
