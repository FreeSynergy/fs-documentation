# Pipedrive - Keyboard shortcuts

## Overview

Pipedrive does **not publish a comprehensive list of its own keyboard shortcuts**. Work is done with mouse and touch plus the usual browser keys; dialogs, filters and forms follow the standard keyboard behavior of the web interface. This file describes what actually works and explicitly marks commonly expected shortcuts as **not available**.

> Status: current Pipedrive version in the browser. The interface changes continuously; re-check this list after updates.

---

## General (browser standard)

| Shortcut | Function |
|----------|----------|
| `Tab` | Jump to the next control (navigation, filter, tile) |
| `Shift+Tab` | Jump to the previous control |
| `Enter` | Trigger the focused button or tile |
| `Space` | Toggle checkboxes and buttons |
| `Esc` | Close detail area, dialog or suggestion list |
| `F5` / `Ctrl+R` | Reload view |
| `Alt+←` / `Alt+→` | Browser back/forward |
| `Ctrl+F` | Search text on the page (browser, not Pipedrive) |
| `Ctrl+P` | Print current view |
| `Ctrl+C` / `Ctrl+V` | Copy and paste in fields |

---

## Navigation

| Shortcut | Function |
|----------|----------|
| `Tab` | Reach items in the left navigation bar |
| `Enter` | Activate navigation item (open module) |
| `↑` / `↓` | Scroll through dropdowns (pipeline, stage, owner) |
| `↑` / `↓` | Scroll through autocomplete suggestions in search |
| `Enter` | Open the highlighted search suggestion |
| `Esc` | Leave search and suggestion list |
| `Backspace` | Delete search text when the search field is focused |

**Not available:**

| Expected shortcut | Status |
|---------------------|--------|
| `/` for search focus | ❌ Not available — click the search field or reach it via `Tab` |
| `Ctrl+K` command palette / jump to module | ❌ Not documented |
| `1`–`8` for navigation modules | ❌ Not available |
| `D` for deals, `A` for activities | ❌ Not available |
| `?` for shortcut overview | ❌ Not available — there is no help overview of this kind |
| `g` then `d` (jump to deals) | ❌ Not available |

---

## Editing (deals, activities, fields)

| Shortcut | Function |
|----------|----------|
| `Tab` / `Shift+Tab` | Move through form fields in order |
| `Enter` | Default action in the dialog (usually save) |
| `Esc` | Leave dialog without changes |
| `Backspace` / `Del` | Clear field content |
| `Ctrl+Z` | Undo **within a text field** (browser function) |
| `↑` / `↓` | Operate selection fields (stage, person, activity type) |
| `Enter` (in list) | Focused row opens the detail area |

**Not available:**

| Expected shortcut | Status |
|---------------------|--------|
| `Ctrl+S` save deal | ❌ Not documented — use the save button |
| `Del` delete deal in the list | ❌ Not available — action in the detail area or the tile menu |
| `Ctrl+Z` undo stage change | ❌ Not available — move the deal back manually |
| Arrow keys to move a tile | ❌ Not available — drag & drop with mouse or touch |
| `N` new deal | ❌ Not available — use the "Add" action button |
| `E` edit record | ❌ Not available |

---

## Search and filters

| Shortcut | Function |
|----------|----------|
| Click into the search field at the top + text | Global search dialog with contacts, companies and deals |
| `↑` / `↓` | Move through result types and hits |
| `Enter` | Open the highlighted hit |
| `Esc` | Close search |
| `Tab` | Reach the filter bar, reach the filter value field |
| `↑` / `↓` | Choose values in filter dropdowns |

Shortcuts in the search field (operators or bangs) are not documented; search works with free text and filters.

---

## Dialogs and forms

| Shortcut | Function |
|----------|----------|
| `Tab` / `Shift+Tab` | Move through fields in the dialog (create deal, add field) |
| `Enter` | Trigger the next dialog step when an input field is focused |
| `Esc` | Cancel, where the dialog allows it |
| `Space` | Toggle checkboxes and switches |
| `↑` / `↓` | Operate selection lists (currency, stage, user) |
| `Backspace` | Remove multiple selections in person fields |

---

## Pipeline board

| Gesture / key | Function |
|---------------|----------|
| Drag the tile | Move deal to another stage column; target column is highlighted |
| `Tab` | Reach tiles in reading order |
| `Enter` | Focused tile opens the detail area |
| `Esc` | Close detail area and return to the board |
| Long press (touch) | Pick up the tile and move it |

Moving by keyboard is not provided; when a loss decision is made, a confirmation dialog appears, operated with `Tab` and `Enter`.

---

## Mac variants

On macOS the browser keys apply with `Cmd` instead of `Ctrl`.

| Shortcut | Function |
|----------|----------|
| `Cmd+R` | Reload |
| `Cmd+P` | Print |
| `Cmd+F` | Search text on the page (browser) |
| `Cmd+C` / `Cmd+V` | Copy and paste |
| `Cmd+Z` | Undo in text field |
| `Cmd+A` | Select all |
| `Cmd+↑` / `Cmd+↓` | Top / bottom of page (browser) |
| `Cmd+Plus` / `Cmd+Minus` | Zoom the interface |
| `Cmd+0` | Reset zoom |
| `Esc` | Close detail area and dialogs |

**Not available:** `Cmd+K` (command palette), `Cmd+S` (save), `Cmd+/` (search focus), `Cmd+N` (new deal).

---

## Accessible keyboard operation

| Shortcut | Function |
|----------|----------|
| `Tab` | Navigation, filters, tiles, detail area and dialogs in reading order |
| `Enter` / `Space` | Trigger the action of the focused element |
| `Esc` | Leave overlay and return to content |
| `↑` / `↓` | Operate selection fields and suggestion lists |
| `Shift+Tab` | Navigate backwards |

---

## Useful alternatives to shortcuts

Since shortcuts are missing, these settings speed up work most in Pipedrive:

- **Saved filters** per pipeline instead of repeated filtering
- **Custom fields with default values** to keep forms short
- **Workflows** that set tasks and field values automatically
- **Home page with due list** instead of searching for activities
- **Browser bookmarks** to filtered deal views (the URL contains the filters)

---

## Summary

Pipedrive offers **no application-specific shortcuts**. Usable are:

- **Browser keys** for reload, print, zoom and text search
- **`Tab`, `Enter`, `Space`, `Esc`, `↑`/`↓`** in navigation, forms, filters and dialogs
- **Drag & drop and touch gestures** for stage changes on the pipeline board

Anyone who needs shortcuts can bookmark filtered views and move routine work into workflows.
