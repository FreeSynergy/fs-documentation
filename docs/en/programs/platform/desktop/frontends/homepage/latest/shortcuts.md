# Homepage - Keyboard Shortcuts

## Overview

Homepage ships **no application-specific keyboard shortcuts**. There is no edit mode, no command palette and no jump keys to groups. Operation is via the browser keyboard and the usual input field keys; changes are made in YAML files, for which your own editor is responsible. This file lists what actually works and explicitly marks commonly assumed keys as **not available**.

> Status: current Homepage versions (2.x). This list should be checked after updates.

---

## General (browser standard)

| Shortcut | Function |
|----------|----------|
| `Tab` | Jump to the next link / input field |
| `Shift+Tab` | Jump to the previous element |
| `Enter` | Open focused tile, submit search query |
| `Space` | Trigger focused element |
| `Esc` | Close search suggestions, remove focus from the field |
| `F5` / `Ctrl+R` | Reload page (layout and widgets are rendered again) |
| `Ctrl+P` | Print overview |
| `Alt+←` / `Alt+→` | Browser back/forward (relevant when the target service is open in the same tab) |
| `F12` | Developer tools (troubleshooting widget requests) |

---

## Navigation on the page

| Shortcut | Function |
|----------|----------|
| `Tab` | Reach tiles in reading order |
| `Enter` | Open the displayed target URL of the service |
| `↑` / `↓` | Scroll through the suggestion list of the search bar |
| `Enter` | Execute highlighted search suggestion |
| `Backspace` | Delete search text when the field is focused |
| `Home` / `End` | Start / end of the page (browser) |
| `Ctrl+F` | Search text on the page (browser, not Homepage) |

**Not available:**

| Expected shortcut | Status |
|---------------------|--------|
| `/` for search field | ❌ Not available – the field must be clicked or reached via `Tab` |
| `1`–`9` for groups | ❌ Not available |
| Letter jump to a tile | ❌ Not available |
| `g` then `g` (switch group) | ❌ Not available |
| Jump mark per widget | ❌ Not available |

---

## Editing (dashboard, widgets)

The Homepage interface is **read-only**. All changes are made in files.

| Action | Route | Shortcut |
|--------|-----|----------|
| Add tile | entry in `config/services.yaml` | ❌ none in Homepage |
| Activate widget | add `_<service>` to the tile | ❌ none |
| Change order | `layout` in `config/settings.yaml` | ❌ none |
| Change icon | write the `icon:` key | ❌ none |
| Make changes effective | reload page (`F5`) | ✅ browser key |
| Check configuration | read container log | ❌ no UI view |

**Not available:**

| Expected shortcut | Status |
|---------------------|--------|
| `e` for edit mode | ❌ Not available – there is no edit mode |
| `Del` to delete a tile | ❌ Not available – delete the entry in the YAML |
| `Ctrl+Z` undo change | ❌ Not available – use version control (Git) |
| `Ctrl+S` save | ❌ Not available – files are saved outside |
| Arrow keys to move | ❌ Not available – no drag & drop, no grid editing |

---

## Search

| Shortcut | Function |
|----------|----------|
| Text in search field + `Enter` | open search query at the configured provider |
| `↑` / `↓` | go through suggestions (`searchSuggestion`) |
| `Esc` | hide suggestions |
| `Enter` (empty field) | ❌ No function |

**Note**: the search bar is shown only if a provider (`providers.search`) is set in `config/settings.yaml`. A local search across all services does not exist.

---

## Configuration files (editor notes)

These keys come from the text editor used, not from Homepage. They are listed here because work on Homepage consists almost entirely of editing files:

| Shortcut | Function |
|----------|----------|
| `Ctrl+Shift+P` (VS Code) | command palette, trigger YAML formatting |
| `Ctrl+Shift+I` / `Ctrl+Alt+F` | format YAML file |
| `Ctrl+K Ctrl+S` | open keybindings of the editor |
| `Ctrl+Shift+V` | Markdown preview for notes on the config |
| `Ctrl+F` / `Ctrl+H` | search/replace in `services.yaml` |

---

## Mac variants

On macOS the browser keys apply with `Cmd` instead of `Ctrl`.

| Shortcut | Function |
|----------|----------|
| `Cmd+R` | reload (new config is rendered) |
| `Cmd+P` | print |
| `Cmd+F` | search text on the page (browser) |
| `Cmd+K` | focus address bar (browser) |
| `Cmd+↑` / `Cmd+↓` | start / end of the page |
| `Cmd+Plus` / `Cmd+Minus` | zoom |
| `Cmd+0` | reset zoom |
| `Esc` | hide search suggestions |

**Not available:** `Cmd+E` (edit), `Cmd+/` (search), `Cmd+B` (sidebar – there is no sidebar), `Cmd+Z` (undo change).

---

## Accessible operation

| Shortcut | Function |
|----------|----------|
| `Tab` | reach header, search field and all tiles |
| `Enter` / `Space` | open service |
| `Esc` | leave suggestion list |
| `↑` / `↓` | operate search suggestions |
| `Shift+Tab` | navigate backwards |
| Browser zoom | usable without loss of function |

---

## Server-side keys and commands (abbreviation instead of shortcut)

For operation there are no key combinations, but commands; fully in [../gethomepage/shortcuts.md](../../gethomepage/latest/shortcuts.md):

| Command | Function |
|--------|----------|
| `docker compose restart homepage` | restart container (after changed `.env`) |
| `docker logs -f homepage` | view configuration errors |
| `docker exec homepage cat /app/config/settings.yaml` | check active configuration |

---

## Summary

Homepage offers **no own shortcuts**. Usable are:

- **Browser keys** for reloading, printing, zoom and text search
- **`Tab`, `Enter`, `Esc`, `↑`/`↓`** in the search bar and on tiles
- **File editing in your own editor** for every change to the dashboard

Short paths come from configuration discipline: clearly named groups, few meaningful widgets and a set-up search bar replace any key combination.
