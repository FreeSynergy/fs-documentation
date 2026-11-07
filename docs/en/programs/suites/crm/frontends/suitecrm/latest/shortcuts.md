# SuiteCRM - Keyboard shortcuts

## Overview

SuiteCRM does **not publish an official list of its own keyboard shortcuts**. It is operated via mouse, touch and the usual browser keys; forms, lists and dialogs follow the browser's standard keyboard behavior. This file documents what actually works and explicitly marks commonly expected shortcuts as **not available**.

> Status: SuiteCRM 7.14.x (LTS) and SuiteCRM 8.x. The interface changes between major versions; check this list after updates.

---

## General (browser standard)

| Shortcut | Function |
|----------|----------|
| `Tab` | Jump to the next control (menu, field, button) |
| `Shift+Tab` | Jump to the previous control |
| `Enter` | Trigger the focused button, submit form |
| `Space` | Toggle a checkbox in the list |
| `Esc` | Close open popup or selection window (version-dependent) |
| `F5` / `Ctrl+R` | Reload page (list is fetched again) |
| `Alt+←` / `Alt+→` | Browser back/forward (back path through lists and details) |
| `Ctrl+P` | Print current view |
| `Ctrl+F` | Search text on the page (browser, not SuiteCRM) |
| `Ctrl+A` | Select text in the focused field |

---

## Navigation

| Shortcut | Function |
|----------|----------|
| `Tab` | Reach the main menu items of the menu bar |
| `Enter` | Open menu item (module list) |
| `↑` / `↓` | Scroll through selection lists and dropdown fields |
| `Enter` | Selected row opens the detail view |
| `Tab` | Reach subpanel buttons (add entry, edit) |
| `Esc` | Cancel button corresponds to browser cancel logic (version-dependent) |

**Not available:**

| Expected shortcut | Status |
|---------------------|--------|
| `Ctrl+K` command palette / module search | ❌ Not available — reach the module via the menu or admin search |
| `/` for search focus | ❌ Not available — the search field must be clicked or reached via `Tab` |
| `1`–`9` for module switching | ❌ Not available |
| `Alt+L` for leads, `Alt+O` for opportunities | ❌ Not available |
| `g` then `l` (jump to leads) | ❌ Not available |
| Function keys (`F2` rename, `F9` save) | ❌ Not available |

---

## Editing (forms, lists)

| Shortcut | Function |
|----------|----------|
| `Tab` / `Shift+Tab` | Move through form fields in order |
| `Enter` | Default action of the focused dialog (usually save) |
| `Esc` | Close selection window (person, company) without applying |
| `Backspace` / `Del` | Clear field content |
| `Ctrl+Z` | Undo **within a text field** (browser function) |
| `Space` | Set checkbox in the list (for mass actions) |
| `↑` / `↓` | Operate multi-line fields and selection lists |

**Not available:**

| Expected shortcut | Status |
|---------------------|--------|
| `Ctrl+S` save record | ❌ Not documented — use the save button |
| `Ctrl+Enter` save in form | ❌ Not documented — applies only to a few browser text fields |
| `Ctrl+Z` undo record changes | ❌ Not available — saved changes can only be traced via the field history |
| `Del` delete record in the list | ❌ Not available — checkbox plus mass action "Delete" |
| Arrow keys to move dashlets | ❌ Not available — drag & drop on the dashboard |
| Inline editing via double-click in every column | ❌ Not available everywhere — only in fields set up for it (version-dependent) |

---

## Search and filters

| Shortcut | Function |
|----------|----------|
| Click into the quick search field at the top + text | Full-text search across modules |
| `Enter` | Submit search, open result list |
| `Esc` | Close autocomplete suggestions |
| `Backspace` | Delete search text when the field is focused |
| `Tab` | Reach filter panel fields, reach the "Apply filter" button |

Shortcuts in the search field (such as operator shortcuts) are **not** documented; search works with text input and filter fields.

---

## Dialogs and wizards

| Shortcut | Function |
|----------|----------|
| `Tab` / `Shift+Tab` | Move through fields in the dialog (import, convert, Module Loader) |
| `Enter` | Next step in the wizard, provided the input field is focused |
| `Esc` | Cancel, where the dialog supports it |
| `Space` | Toggle radio buttons and checkboxes |
| `↑` / `↓` | Operate selection lists (language, team, module) |

---

## Mac variants

On macOS the browser keys apply with `Cmd` instead of `Ctrl`.

| Shortcut | Function |
|----------|----------|
| `Cmd+R` | Reload |
| `Cmd+P` | Print |
| `Cmd+F` | Search text on the page (browser) |
| `Cmd+Z` | Undo in text field |
| `Cmd+A` | Select all |
| `Cmd+↑` / `Cmd+↓` | Top / bottom of page (browser) |
| `Cmd+Plus` / `Cmd+Minus` | Zoom the interface |
| `Cmd+0` | Reset zoom |
| `Cmd+W` | Close tab |

**Not available:** `Cmd+K` (command palette), `Cmd+S` (save), `Cmd+E` (edit), `Cmd+/` (search focus).

---

## Accessible keyboard operation

| Shortcut | Function |
|----------|----------|
| `Tab` | Header, filter panel, table rows and buttons in reading order |
| `Enter` / `Space` | Trigger the action of the focused element |
| `Esc` | Close overlay and return to content |
| `↑` / `↓` | Operate selection fields and suggestion lists |
| `Shift+Tab` | Navigate backwards |

---

## Operational commands (CLI, not shortcuts)

Maintenance and updates run via command-line calls on the server. These commands are **not** keyboard shortcuts but operational steps; the exact names are version-dependent and should be looked up in the official documentation.

| Command | Function |
|---------|----------|
| `php -f cron.php` | Run the scheduler (workflows, campaigns, cleanup); typically via a cron job |
| Admin ▸ "Repair" / "Clear cache" | Rebuild the metadata cache (interface, not a CLI command) |
| `php -f bin/suitecrm-cli/suitecrm cache:clear` | Cache maintenance via the CLI tool (since 7.11, names version-dependent) |
| `php -f bin/suitecrm-cli/suitecrm db:repair` | Database repair actions (names version-dependent) |
| `composer install` / `bin/console` (SuiteCRM 8) | Dependencies and Symfony commands of the 8.x shell |

Anyone looking for quick access works with saved filters, favorites on the dashboard and a personal theme; SuiteCRM itself offers no key combinations for this.

---

## Summary

SuiteCRM ships **no application-specific shortcuts**. Usable are:

- **Browser keys** for reload, print, zoom and text search
- **`Tab`, `Enter`, `Space`, `Esc`, `↑`/`↓`** in forms, lists, filters and dialogs
- **Drag & drop** exclusively for dashlets on the home page
- **CLI and admin maintenance** for cache, database repair and scheduler
