# Wiki.js 3.1.1 — keyboard shortcuts

"Mod" means Ctrl on Windows and Linux, Cmd on macOS. Only bindings found in the 3.1.1 source are listed. Sources are named per table. Source tree: https://github.com/requarks/wiki/tree/3.1.1/frontend/src

No global application shortcuts were found. The old page's list (command palette, file search, live preview, new page, file tree and similar) is not in the 3.1.1 source and has been removed. See `../changelog.md`.

## Visual editor

Source: `frontend/src/editor/visual/commands.js` (`buildKeymap`). The comment in that file says the set is "deliberately close to what the Markdown editor binds".

| Shortcut | Action |
|----------|--------|
| Mod+Z | Undo (Yjs undo while collaborating) |
| Mod+Shift+Z | Redo |
| Mod+Y | Redo |
| Mod+B | Strong (bold) |
| Mod+I | Emphasis (italic) |
| Mod+U | Underline |
| Mod+Shift+X | Strikethrough |
| Mod+Shift+H | Highlight mark |
| Mod+E | Inline code |
| Mod+Shift+8 | Bullet list |
| Mod+Shift+9 | Numbered list |
| Mod+Shift+. | Blockquote |
| Mod+Shift+Enter | Toggle task checked |
| Mod+Shift+1 … 6 | Heading level 1 to 6 |
| Enter | Split list item or definition item |
| Tab | Next table cell, or sink list item |
| Shift+Tab | Previous table cell, or lift list item |
| Shift+Enter | Hard line break (leaves a code block when inside one) |
| Mod+Enter | Leave a code block, or the last block |
| Backspace, Delete | Custom handling for tables and list starts |

### Slash menu (inside the visual editor)

Source: `frontend/src/editor/visual/slash.js`.

| Key | Action |
|-----|--------|
| ArrowDown, ArrowUp | Move the highlight |
| Enter or Tab | Insert the highlighted item |
| Escape | Close the menu |

The menu opens when a `/` is typed (`handleTextInput`), not when the caret moves onto a line that starts with `/`, and not on paste.

## Markdown editor (Monaco)

Source: `frontend/src/components/EditorMarkdown.vue` (`editor.addAction` calls).

| Shortcut | Action |
|----------|--------|
| Mod+B | Toggle bold (`**`) |
| Mod+I | Toggle italic (`*`) |
| Mod+Alt+Right | Increase header level |
| Mod+Alt+Left | Decrease header level |
| Mod+S | Save. Asks the page header's Save button to run, so the reason-for-change dialog and the save state are the same as on screen. In a live note, Mod+S is claimed and does nothing. |

Monaco's own shortcuts (find, replace, multi-cursor, and so on) are not listed here because they are Monaco defaults and not Wiki.js bindings.

## AsciiDoc editor (Monaco)

Source: `frontend/src/components/EditorAsciidoc.vue`. Same bindings as the Markdown editor: Mod+B, Mod+I, Mod+Alt+Right, Mod+Alt+Left, Mod+S.

## Other editors

Excalidraw, Feedback, Blog, Redirect: no custom key bindings were found in the source files that were searched. Unverified.

## Global (app-wide)

A search for `keydown` in the frontend source found listeners only in `frontend/src/graph/engine.js`, `frontend/src/composables/previewScrollSync.js`, `frontend/src/editor/visual/nodeviews.js` and `frontend/src/editor/visual/slash.js`. No app-wide shortcut registry was found. Unverified: any global shortcut for search or navigation.
