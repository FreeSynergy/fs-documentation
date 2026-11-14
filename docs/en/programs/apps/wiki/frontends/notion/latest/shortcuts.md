# Notion - Keyboard Shortcuts

> **Status 2026-11-14:** The list is the official page [S11], read again on 2026-11-14 (see the re-check below). The unverified "Earlier draft" tables of this file (command palette, settings, F1, global search, app manager and others) were removed from `latest/`; the folder [2026-11-07](../2026-11-07/shortcuts.md) is frozen.

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

## Re-check 2026-11-14 (S11, S26, S12, S15)

The page was read again. Result: every row of the table above is still on the page. The fetch tool reported that its answer might come from a cache, so the points below carry that reservation until a live read confirms them. Platform split as the page gives it (Notion's "cmd/ctrl" is macOS / Windows and Linux):

| Action | macOS | Windows / Linux |
|--------|-------|-----------------|
| Search / recent pages | cmd+P or cmd+K | ctrl+P or ctrl+K |
| Copy page URL | cmd+L | ctrl+L |
| New window (desktop) | cmd+shift+N | ctrl+shift+N |
| Open page in new window | option+shift+click | **[nicht belegt]** |
| Open link in new Notion tab (desktop) | cmd+click | ctrl+click |
| System emoji picker (desktop) | ctrl+cmd+space | Windows key + . or Windows key + ; |
| Text block | cmd+option+0 | ctrl+shift+0 |
| Heading 1 / 2 / 3 | cmd+option+1 / 2 / 3 | ctrl+shift+1 / 2 / 3 |
| To-do / bullet / numbered / toggle / code | cmd+option+4 / 5 / 6 / 7 / 8 | ctrl+shift+4 / 5 / 6 / 7 / 8 |
| New page, or turn a line into a page | cmd+option+9 | ctrl+shift+9 |
| Toggle all toggles | cmd+option+T | ctrl+alt+T |
| Deselect or select one block | cmd+shift+click | alt+shift+click |
| Duplicate while dragging | option+drag | alt+drag |
| Block menu, or edit several database rows | cmd+/ | ctrl+/ |
| Previous / next database page (peek) | ctrl+shift+K / J | ctrl+K / J |
| Copy link of a search result | cmd+L or cmd+shift+C | **[nicht belegt]** for Windows [S26] |
| Hide or show the sidebar | cmd+\ | ctrl+\ [S12] |

Typed commands (same on all platforms):

| Typed | Result |
|-------|--------|
| `@` + name, page or date | mention; `@remind` + date adds a reminder; Esc closes the menu |
| `[[` + page name | link a page; choose "Add new sub-page" or "Add new page in..." to create one |
| `+` + page name | the same as `[[` |
| `:` + emoji name | inline emoji |
| `**x**`, `*x*`, `` `x` ``, `~x~` | bold, italic, inline code, strikethrough |
| `*`, `-`, `+` + space; `1.`, `a.`, `i.` + space; `[]` + space; `#`, `##`, `###` + space; `>` + space; `"` + space; `---` | bullet list, numbered list, to-do, headings, toggle, quote, divider |

Slash commands listed on the page: `/text` `/plain` `/page` `/bullet` `/num` `/todo` `/toggle` `/div` `/quote` `/h1` (`/#`) `/h2` (`/##`) `/h3` (`/###`) `/link` `/mention` `/date` `/reminder` `/equation` `/emoji` `/image` `/pdf` `/book` `/video` `/audio` `/code` `/file` `/embed` `/duplicate` `/moveto` `/delete` `/toc` `/button` `/template` `/bread` `/math` `/latex` `/turn` `/color` `/default`. Esc clears the slash menu.

Not on the page: shortcuts for export, import, share, trash, version history and rename [S11][S26].
