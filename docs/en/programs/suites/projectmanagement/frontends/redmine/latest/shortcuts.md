# Redmine - Keyboard shortcuts

## Overview

Redmine ships only **a single own shortcut**: `/` puts the focus into the search field of
the header line (included since several major versions; older installations without this
behaviour: version-dependent). Beyond that the browser keyboard and the standard
navigation in forms apply. Widely assumed shortcuts (`c`, `j/k`, `Ctrl+Enter`) do **not**
exist in the core; some plugins add shortcuts.

> State: Redmine 5.x/6.x line. Check the list after updates or plugin installations.

---

## General (browser standard)

| Shortcut | Function |
|----------|----------|
| `Tab` | jump to the next control |
| `Shift+Tab` | jump to the previous control |
| `Enter` | trigger a button, link or the form's default action |
| `Space` | toggle checkboxes/ticks (filters, module selection) |
| `F5` / `Ctrl+R` | reload the page |
| `Alt+←` / `Alt+→` | browser back/forward (tab navigation follows URLs) |
| `Ctrl+P` | print (Redmine ships its own print stylesheet) |
| `Ctrl+F` | search text on the page (browser) |
| `Ctrl+click` | open an issue link in a new tab |

---

## Redmine's own shortcuts

| Shortcut | Function |
|----------|----------|
| `/` | put the focus in the search field of the header line (typing starts the search) |
| `Esc` | close open autocomplete/suggestion popups (form standard) |

**Not available:**

| Desired shortcut | Status |
|------------------|--------|
| `c` create a new issue | ❌ not in the core — use the "new issue" button |
| `j` / `k` next/previous item | ❌ not in the core |
| `Ctrl+Enter` submit note/save | ❌ not in the core — save button or `Enter` in the field |
| `Ctrl+S` save | ❌ not intercepted — the browser saves the page |
| `g` + letter (jump to modules) | ❌ not available |
| `?` shortcut overview | ❌ not available |
| `Alt` + digit for tabs | ❌ not in the core (browser/OS locale only) |

---

## Navigation

| Shortcut | Function |
|----------|----------|
| `Tab` | control the header line, tabs, breadcrumb and table |
| `Enter` | open an issue link, trigger a tab |
| `↑` / `↓` | page through selection fields (tracker, status, assignee) |
| `Esc` | close autocomplete suggestions |
| `Backspace` | delete the search field text when focused |

Tip: the breadcrumb and tab bars are ordinary links — `Tab` + `Enter` replaces every navigation hotkey.

---

## Editing

| Shortcut | Function |
|----------|----------|
| `Tab` / `Shift+Tab` | run through form fields (status, priority, note) |
| `Enter` | default save action in the focused form |
| `Ctrl+A` / `Ctrl+C` / `Ctrl+V` / `Ctrl+X` | select all, copy, paste, cut |
| `Ctrl+Z` | undo **inside** a text field; saved changes cannot be taken back via undo |
| `Shift+click` | select text in blocks in wiki/comment fields (browser) |

### Wiki and comment fields (Textile/Markdown)

Redmine formats via syntax, not via hotkey:

| Input | Function |
|-------|----------|
| `**text**` | bold |
| `*text*` | italic |
| `h2.` / `##` | heading (Textile / Markdown) |
| `[[WikiPage]]` | internal wiki link |
| `#1234` | issue reference (linked automatically) |
| `{{...}}` | inline code (Textile) |

**Not available:** `Ctrl+B`/`Ctrl+I` in the wiki editor (unless a plugin provides them).

---

## Search

| Shortcut | Function |
|----------|----------|
| `/` | focus the search field (Redmine's own shortcut) |
| `Enter` | run the search |
| `Ctrl+F` | search the page text (browser) |

---

## Mac variants

On macOS the browser keys apply with `Cmd` instead of `Ctrl`.

| Shortcut | Function |
|----------|----------|
| `/` | focus the search field (as on Windows/Linux) |
| `Cmd+R` | reload |
| `Cmd+P` | print (print stylesheet) |
| `Cmd+F` | search text on the page (browser) |
| `Cmd+A` / `Cmd+C` / `Cmd+V` | select all, copy, paste |
| `Cmd+Z` | undo in the active text field |
| `Cmd+click` | open a link in a new tab |
| `Cmd+Plus` / `Cmd+Minus` / `Cmd+0` | zoom the UI |

**Not available:** `Cmd+E` (edit), `Cmd+S` (save), `Cmd+K` (palette).

---

## Maintenance on the command line (no UI, but real)

Redmine administration uses `rake`/`bundle` in the installation directory; that replaces no
shortcuts, but belongs to working quickly:

| Command | Function |
|---------|----------|
| `bundle exec rake db:migrate` | run database migrations |
| `bundle exec rake redmine:load_default_data` | load default data (trackers, status) |
| `bundle exec rake generate_secret_token` | generate the session secret |
| `bundle exec rails server -e production` | start the development server (production: Puma/Passenger) |

---

## Accessible operation

| Shortcut | Function |
|----------|----------|
| `Tab` / `Shift+Tab` | complete navigation without a mouse |
| `Enter` / `Space` | trigger links and buttons |
| `Esc` | leave popups and suggestions |
| `↑` / `↓` | operate selection fields |
| `Ctrl+Plus` | enlarge the UI without loss of function |

---

## Summary

Redmine offers exactly **one own shortcut**: `/` for search. Everything else runs via:

- **browser keys** (reload, print, zoom, text search)
- **`Tab`/`Enter`/`Esc`/arrow keys** in forms and selection fields
- **syntax shorthands** (Textile/Markdown, `#1234` issue references) instead of formatting hotkeys

Plugin extensions can supply additional shortcuts — then the plugin documentation does not
replace this list, it only adds to it.
