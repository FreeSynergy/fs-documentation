# Notion - Keyboard Shortcuts

> **Status 2026-11-13:** Use the verified list below. The tables after it ("Earlier draft") include shortcuts that the official page [S11] does not list, among them Ctrl/Cmd+Shift+P (command palette), Ctrl/Cmd+, (settings), F1, Ctrl/Cmd+Shift+F, Ctrl/Cmd+Shift+A; they are **unverified** and must not be built on. See also the [2026-11-07 snapshot](../2026-11-07/shortcuts.md) and [changelog](../changelog.md).

## Verified shortcuts (S11 re-read as listed in the snapshot; S-numbers as in [index.md](../index.md))

Notion writes `cmd/ctrl`: cmd on macOS, ctrl on Windows and Linux.

| Workflow | Key | Function |
|----------|-----|----------|
| Search (W8) | cmd/ctrl+P, or cmd/ctrl+K when no block has the cursor | Open search / recent pages [S26][S11] |
| Search in page | cmd/ctrl+F | Find in page |
| Navigation | cmd/ctrl+[ and ] | Back / forward |
| Navigation | cmd/ctrl+shift+U | Up one level in the hierarchy |
| Navigation | cmd/ctrl+\ | Show or hide the sidebar |
| Create (W1) | cmd/ctrl+N | New page (desktop) |
| Create | cmd/ctrl+T | New tab (desktop) |
| Create | cmd/ctrl+option/shift+9 | New page block |
| Links (W12) | cmd/ctrl+L | Copy the page URL |
| Links | cmd/ctrl+K | Add link to selected text |
| Edit (W2) | Enter / shift+Enter | New block / line break in a block |
| Edit | Tab / shift+Tab | Nest / un-nest |
| Edit | Esc | Select the block, or clear the selection |
| Edit | cmd/ctrl+A | Select the current block |
| Edit | arrows, shift+arrows, shift+click | Select other blocks, extend, range |
| Edit | cmd/ctrl+D | Duplicate selected blocks (W6) |
| Edit | backspace / delete | Delete selected blocks (W7) |
| Edit | cmd/ctrl+shift+arrow | Move the selected block (W5) |
| Edit | option/alt+drag | Duplicate content |
| Edit | cmd/ctrl+/ | Change selected blocks |
| Edit | cmd/ctrl+Enter | Open a page, tick a to-do, toggle |
| Edit | cmd/ctrl+option/alt+T | Expand or close all toggles |
| Edit | cmd/ctrl+option/shift+0 to 8 | Text, headings 1-3, to-do, bullet, numbered, toggle, code |
| Format | cmd/ctrl+B / I / U | Bold / italic / underline |
| Format | cmd/ctrl+shift+S | Strikethrough |
| Format | cmd/ctrl+E | Inline code |
| Format | cmd/ctrl+shift+H | Last colour |
| Comment | cmd/ctrl+shift+M | Create a comment |
| View | cmd/ctrl+shift+L | Dark / light mode |
| View | cmd/ctrl++ / - | Zoom |
| View | space | Open or close a full-screen image |
| Tables | cmd/ctrl+R / D | Fill right / down |
| Database peek | ctrl+shift+K/J (Mac), ctrl+K/J (Win) | Previous / next database page |

Markdown typing and slash commands (`/h1`, `/page`, `/duplicate`, `/moveto`, `/delete`, `/template`, `/image`, `/file`, `/link`, `/turn`, `/color`) are listed in the [snapshot](../2026-11-07/shortcuts.md).

**No documented shortcut** for: rename, move via dialog, trash, restore, version history, import, export, share, offline toggle. Undo/redo on desktop: **[nicht belegt]** in the table read. Remapping shortcuts: **[nicht belegt]**.

## Earlier draft (partly unverified)

## Overview

Notion offers extensive keyboard shortcuts for working quickly with the block-based visual editor.

---

## General Shortcuts

| Shortcut | Function |
|----------|----------|
| `Ctrl+Shift+P` / `Cmd+Shift+P` | Open command palette |
| `Ctrl+,` / `Cmd+,` | Open settings |
| `F1` | Help |
| `Ctrl+K` / `Cmd+K` | Add link |
| `Ctrl+Shift+F` / `Cmd+Shift+F` | Global search |
| `Ctrl+Shift+A` / `Cmd+Shift+A` | Open app manager |

---

## Editor Shortcuts (Block Editor)

### Block Navigation

| Shortcut | Function |
|----------|----------|
| `Enter` | Create new line / block |
| `Shift+Enter` | Line break (within a block) |
| `Tab` | Indent (lists/blocks) |
| `Shift+Tab` | Remove indent (lists/blocks) |
| `Escape` | Leave block / lose focus |
| `Ctrl+Enter` / `Cmd+Enter` | Tick checkbox / run block |
| `Ctrl+↑` / `Cmd+↑` | Move block up |
| `Ctrl+↓` / `Cmd+↓` | Move block down |
| `Ctrl+Shift+↑` / `Cmd+Shift+↑` | Copy block up |
| `Ctrl+Shift+↓` / `Cmd+Shift+↓` | Copy block down |

### Block Actions

| Shortcut | Function |
|----------|----------|
| `Ctrl+D` / `Cmd+D` | Duplicate block |
| `Ctrl+Shift+D` / `Cmd+Shift+D` | Duplicate page |
| `Ctrl+Shift+Backspace` / `Cmd+Shift+Backspace` | Delete block |
| `Ctrl+Shift+C` / `Cmd+Shift+C` | Copy block |
| `Ctrl+Shift+V` / `Cmd+Shift+V` | Paste block |
| `Ctrl+Shift+X` / `Cmd+Shift+X` | Cut block |
| `Ctrl+Z` / `Cmd+Z` | Undo |
| `Ctrl+Y` / `Cmd+Y` | Redo |

### Formatting

| Shortcut | Function |
|----------|----------|
| `Ctrl+B` / `Cmd+B` | Bold |
| `Ctrl+I` / `Cmd+I` | Italic |
| `Ctrl+U` / `Cmd+U` | Underline |
| `Ctrl+Shift+X` / `Cmd+Shift+X` | Strikethrough |
| `Ctrl+E` / `Cmd+E` | Align center |
| `Ctrl+L` / `Cmd+L` | Align left |
| `Ctrl+R` / `Cmd+R` | Align right |
| `Ctrl+Shift+E` / `Cmd+Shift+E` | Justify |
| `Ctrl+K` / `Cmd+K` | Insert link |
| `Ctrl+Shift+K` / `Cmd+Shift+K` | Code tag |
| `Ctrl+Shift+C` / `Cmd+Shift+C` | Code block |
| `Ctrl+Shift+M` / `Cmd+Shift+M` | Quote (blockquote) |
| `Ctrl+Shift+A` / `Cmd+Shift+A` | Task (to-do) |

### Changing Block Types

| Shortcut | Function |
|----------|----------|
| `/` | Open block selection menu |
| `/h1` + `Enter` | Heading 1 (H1) |
| `/h2` + `Enter` | Heading 2 (H2) |
| `/h3` + `Enter` | Heading 3 (H3) |
| `/todo` + `Enter` | To-do list |
| `/bullist` + `Enter` | Bulleted list |
| `/numlist` + `Enter` | Numbered list |
| `/callout` + `Enter` | Callout box |
| `/quote` + `Enter` | Quote |
| `/code` + `Enter` | Code block |
| `/table` + `Enter` | Table |
| `/toggle` + `Enter` | Toggle block |
| `/embed` + `Enter` | Embed |

### Selecting Code Syntax

| Shortcut | Function |
|----------|----------|
| `/js` + `Enter` | JavaScript |
| `/python` + `Enter` | Python |
| `/html` + `Enter` | HTML |
| `/css` + `Enter` | CSS |
| `/sql` + `Enter` | SQL |
| `/md` + `Enter` | Markdown |
| `/bash` + `Enter` | Bash/Shell |
| `/c` + `Enter` | C |
| `/cpp` + `Enter` | C++ |
| `/java` + `Enter` | Java |
| `/json` + `Enter` | JSON |
| `/yaml` + `Enter` | YAML |

---

## File/Menu Shortcuts

| Shortcut | Function |
|----------|----------|
| `Ctrl+S` / `Cmd+S` | Save |
| `Ctrl+P` / `Cmd+P` | Print |
| `Ctrl+N` / `Cmd+N` | New page |
| `Ctrl+Shift+N` / `Cmd+Shift+N` | Child page |
| `Ctrl+O` / `Cmd+O` | Open page |
| `Ctrl+Shift+S` / `Cmd+Shift+S` | Save page as |
| `Ctrl+W` / `Cmd+W` | Close page |
| `Ctrl+Shift+E` / `Cmd+Shift+E` | Export page |
| `Ctrl+Shift+X` / `Cmd+Shift+X` | Delete page |
| `Ctrl+Shift+F` / `Cmd+Shift+F` | Share page |

---

## Search/Navigation Shortcuts

| Shortcut | Function |
|----------|----------|
| `Ctrl+F` / `Cmd+F` | Find |
| `Ctrl+Shift+F` / `Cmd+Shift+F` | Global search |
| `Ctrl+G` / `Cmd+G` | Next match |
| `Ctrl+Shift+G` / `Cmd+Shift+G` | Previous match |
| `Ctrl+H` / `Cmd+H` | Replace |
| `Ctrl+Shift+H` / `Cmd+Shift+H` | Replace (with context) |
| `Ctrl+K` / `Cmd+K` | Search bar (when focused) |
| `Ctrl+P` / `Cmd+P` | File search (panel) |
| `Ctrl+Shift+O` / `Cmd+Shift+O` | Open page structure |
| `Ctrl+Shift+D` / `Cmd+Shift+D` | Open page dashboard |
| `Ctrl+Tab` | Next tab |
| `Ctrl+Shift+Tab` | Previous tab |

---

## View Shortcuts

| Shortcut | Function |
|----------|----------|
| `F11` | Full-screen mode |
| `Ctrl+Shift+I` / `Cmd+Shift+I` | Developer tools |
| `Ctrl+B` / `Cmd+B` | Show/hide sidebar |
| `Ctrl+Shift+B` / `Cmd+Shift+B` | Show/hide status bar |
| `Ctrl+Enter` / `Cmd+Enter` | Preview/publish |
| `Ctrl+Shift+V` / `Cmd+Shift+V` | Live preview |

---

## Menu/Action Shortcuts

| Shortcut | Function |
|----------|----------|
| `Ctrl+M` / `Cmd+M` | Open menu (block menu) |
| `Ctrl+Shift+M` / `Cmd+Shift+M` | Insert macro |
| `Ctrl+Shift+T` / `Cmd+Shift+T` | Insert table |
| `Ctrl+Shift+I` / `Cmd+Shift+I` | Insert image |
| `Ctrl+Shift+E` / `Cmd+Shift+E` | Insert embed |
| `Ctrl+Shift+U` / `Cmd+Shift+U` | File upload |
| `Ctrl+Shift+V` / `Cmd+Shift+V` | Insert video |
| `Ctrl+Shift+L` / `Cmd+Shift+L` | Insert link |
| `Ctrl+Shift+A` / `Cmd+Shift+A` | Insert to-do task |
| `Ctrl+Shift+D` / `Cmd+Shift+D` | Open file explorer |
| `Ctrl+Shift+P` / `Cmd+Shift+P` | Preset selection |

---

## Mac Shortcuts

| Shortcut | Function |
|----------|----------|
| `Cmd+Shift+P` | Command palette |
| `Cmd+,` | Settings |
| `Cmd+K` | Add link |
| `Cmd+Shift+F` | Global search |
| `Cmd+Shift+N` | New page |
| `Cmd+Shift+S` | Save as |
| `Cmd+W` | Close page |

---

## Keyboard Navigation

| Shortcut | Function |
|----------|----------|
| `Tab` | Next focus |
| `Shift+Tab` | Previous focus |
| `Enter` | Activate |
| `Escape` | Leave focus / close dialog |
| `Space` | Select checkbox |
| `↑` | Next block (up) |
| `↓` | Next block (down) |
| `←` | Focus left |
| `→` | Focus right |

---

## Quick Navigation in the Editor

| Shortcut | Function |
|----------|----------|
| `Ctrl+↑` / `Cmd+↑` | Start of editor |
| `Ctrl+↓` / `Cmd+↓` | End of editor |
| `Ctrl+Home` / `Cmd+Home` | Start of editor |
| `Ctrl+End` / `Cmd+End` | End of editor |
| `Ctrl+Left` / `Cmd+Left` | Start of word (left) |
| `Ctrl+Right` / `Cmd+Right` | Start of word (right) |

---

## Summary

Notion offers extensive shortcuts for:
- **Block navigation**: Fast work with the block-based editor
- **Block actions**: Duplicate, delete, copy, move
- **Formatting**: All common formatting
- **Block types**: Switch between block types via the slash menu
- **Code syntax**: Change the language directly in the code block
- **Navigation**: Within the editor and between components
- **File operations**: Save, open, print, export
- **Search**: Local and global
- **View**: Full screen, sidebar, preview

Mac users benefit from the same shortcuts with `Cmd` instead of `Ctrl`.
