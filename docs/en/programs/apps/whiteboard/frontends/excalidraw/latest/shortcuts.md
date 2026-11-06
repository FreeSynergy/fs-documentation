# Excalidraw - Keyboard shortcuts

## Overview

Excalidraw documents its shortcuts directly in the app (help dialog via `/`). This list is based on the official shortcut overview on docs.excalidraw.com. On macOS `Cmd` replaces the `Ctrl` key. Edge cases change with the versions and are marked as version-dependent.

---

## General shortcuts

| Shortcut | Purpose |
|----------|---------|
| `Ctrl+Z` / `Cmd+Z` | Undo |
| `Ctrl+Shift+Z` / `Cmd+Shift+Z` | Redo |
| `Ctrl+A` / `Cmd+A` | Select all elements |
| `Ctrl+C` / `Cmd+C` | Copy selection |
| `Ctrl+X` / `Cmd+X` | Cut selection |
| `Ctrl+V` / `Cmd+V` | Paste |
| `Ctrl+S` / `Cmd+S` | Save as `.excalidraw` |
| `Del` / `Backspace` | Delete selection |
| `Esc` | Cancel tool; pressing twice deselects |
| `/` | Show/hide the help dialog (shortcut overview) |
| `?` | Toggle zen mode (hide the UI) |
| `Ctrl+'` / `Cmd+'` | Show/hide the grid |

---

## Tool selection

| Shortcut | Purpose |
|----------|---------|
| `V` | Selection tool |
| `H` | Hand (move the canvas) |
| `E` | Eraser |
| `R` | Rectangle |
| `D` | Diamond |
| `O` | Ellipse |
| `A` | Arrow |
| `L` | Line |
| `P` | Draw freehand |
| `X` | Text |
| `Q` | Toggle tool lock (tool stays active) |
| `1`–`4` | Stroke width, font size or font depending on selection (assignment version-dependent) |

---

## Selection and navigation

| Shortcut | Purpose |
|----------|---------|
| `Shift`+click | Add elements to the selection |
| Drag over empty area | Marquee selection (drag out several) |
| `Alt`+click | Depth selection: hit overlapping elements underneath |
| `Tab` / `Shift+Tab` | Select next / previous element (version-dependent) |
| `Ctrl`+scroll | Zoom |
| `Ctrl+=` / `Cmd+=` | Zoom in |
| `Ctrl+-` / `Cmd+-` | Zoom out |
| `Ctrl+Shift+0` / `Cmd+Shift+0` | Reset zoom to 100 % |
| `Ctrl+1` / `Cmd+1` | Zoom to content |
| `Ctrl+Shift+1` / `Cmd+Shift+1` | Zoom to selection |

---

## Editing

| Shortcut | Purpose |
|----------|---------|
| Arrow keys | Move the selection |
| `Shift`+arrow keys | Move the selection in larger steps (version-dependent) |
| `Shift`+drag | Scale proportionally / fix angles to 15° steps |
| `Alt`+drag | Clone the element |
| `Ctrl+G` / `Cmd+G` | Group |
| `Ctrl+Shift+G` / `Cmd+Shift+G` | Ungroup |
| `Shift+H` | Mirror horizontally |
| `Shift+V` | Mirror vertically |
| `]` / `[` | Bring to front / send to back |
| `Alt+]` / `Alt+[` | One layer forward / back |
| `Ctrl+K` / `Cmd+K` | Add a link to the selected element |
| Double-click | Edit the text respectively label of the element |

---

## Align and distribute (multiple selection)

| Shortcut | Purpose |
|----------|---------|
| `Ctrl+Shift+L` / `Cmd+Shift+L` | Align left |
| `Ctrl+Shift+C` / `Cmd+Shift+C` | Centre horizontally |
| `Ctrl+Shift+R` / `Cmd+Shift+R` | Align right |
| `Ctrl+Shift+T` / `Cmd+Shift+T` | Align top |
| `Ctrl+Shift+M` / `Cmd+Shift+M` | Align centre vertically |
| `Ctrl+Shift+B` / `Cmd+Shift+B` | Align bottom |

The matching distribute actions (equal spacing) only exist in the context menu.

---

## Search

Excalidraw has **no search in the canvas**. Things are only found via the library search (panel) and the browser's `Ctrl+F` for the interface itself.

---

## NOT available

| Common expectation | Status |
|--------------------|--------|
| `Ctrl+F` search in the canvas | ❌ Not available — no search function |
| Command palette (`Ctrl+Shift+P`) | ❌ Not available |
| `Ctrl+N` new canvas | ❌ No shortcut — only through the main menu |
| `Ctrl+E` export image | ❌ No documented shortcut — use the main menu |
| `Ctrl+P` print | ❌ Not an app feature — only browser printing |
| `Ctrl+Shift+S` save as | ❌ Not available — `Ctrl+S` suffices |
| Chat shortcuts | ❌ Not available — no chat feature |

---

## Mac variants

| Shortcut | Purpose |
|----------|---------|
| `Cmd+Z` / `Cmd+Shift+Z` | Undo / redo |
| `Cmd+C` / `Cmd+X` / `Cmd+V` | Copy / cut / paste |
| `Cmd+S` | Save |
| `Cmd+A` | Select all |
| `Cmd+=` / `Cmd+-` / `Cmd+Shift+0` | Zoom as above |
| `Cmd+G` / `Cmd+Shift+G` | Group / ungroup |
| `Cmd+K` | Add link |
| `Cmd+'` | Toggle grid |

---

## Mouse and touch gestures (supplementary)

| Gesture | Purpose |
|---------|---------|
| Scroll / two-finger swipe | Move the canvas |
| Pinch (touch) | Zoom |
| Press and hold (touch) | Depth selection like `Alt`+click |
| Drag on selection edges | Scale |
| Drag an arrow end | Reconnect the link to another element |

---

## Summary

Excalidraw deliberately keeps its shortcuts small:

- **Letters** switch tools (`V H E R D O A L P X`), `Q` locks the tool
- **`Ctrl`/`Cmd` + classics** for clipboard, undo/redo, saving, selecting
- **Zoom and view** fully keyboard-controlled, aligning likewise
- **Search and command palette do not exist** and are replaced by panels respectively the menu
