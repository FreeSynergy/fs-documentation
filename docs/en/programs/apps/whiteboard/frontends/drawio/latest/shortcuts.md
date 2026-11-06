# draw.io - Keyboard shortcuts

## Overview

draw.io ships an official shortcut list in the application help (Help menu). draw.io is a drawing program **without tool letters** — shapes come from libraries, not from a tool palette. Many keys are shown in the menus themselves; in places the web and desktop versions differ (version-dependent).

---

## General shortcuts

| Shortcut | Purpose |
|----------|---------|
| `Ctrl+Z` / `Cmd+Z` | Undo |
| `Ctrl+Y` / `Cmd+Y` | Redo |
| `Ctrl+A` / `Cmd+A` | Select all |
| `Ctrl+C` / `Cmd+C` | Copy (shape or selection) |
| `Ctrl+X` / `Cmd+X` | Cut |
| `Ctrl+V` / `Cmd+V` | Paste |
| `Del` / `Backspace` | Delete selection |
| `Esc` | Cancel editing, deselect |
| `Enter` | Edit the label of the selected cell |
| `F2` | Edit the data of the selected cell (Edit menu) |
| `Tab` / `Shift+Tab` | Select next / previous cell (version-dependent) |

---

## Selection and navigation

| Shortcut | Purpose |
|----------|---------|
| `Shift`+click | Add cells to the selection |
| Drag over empty area | Marquee selection |
| `Ctrl`+scroll | Zoom |
| Double-click on a shape | Edit text |
| Click a page tab | Switch page (bottom) |
| Right-button drag on empty area | Pan the canvas (version-dependent) |

---

## Editing

| Shortcut | Purpose |
|----------|---------|
| `Ctrl+D` / `Cmd+D` | Duplicate (Edit menu) |
| `Ctrl+G` / `Cmd+G` | Group |
| `Ctrl+Shift+G` / `Cmd+Shift+G` | Ungroup |
| `Alt`+drag | Clone the cell |
| `Shift`+drag on a handle | Proportional scaling |
| `Shift`+drag an edge | Fix the angle of the edge |
| Drag a point of an edge | Set a waypoint, `Alt`+click removes a point |

---

## Copy style (format transfer)

| Shortcut | Purpose |
|----------|---------|
| `Ctrl+Shift+C` / `Cmd+Shift+C` | Copy style |
| `Ctrl+Shift+X` / `Cmd+Shift+X` | Cut style |
| `Ctrl+Shift+V` / `Cmd+Shift+V` | Paste style |

---

## Align and distribute (multiple selection)

| Shortcut | Purpose |
|----------|---------|
| `Ctrl+Shift+L` / `Cmd+Shift+L` | Align left |
| `Ctrl+Shift+C` / `Cmd+Shift+C` | Centre horizontally |
| `Ctrl+Shift+R` / `Cmd+Shift+R` | Align right |
| `Ctrl+Shift+T` / `Cmd+Shift+T` | Align top |
| `Ctrl+Shift+M` / `Cmd+Shift+M` | Centre vertically |
| `Ctrl+Shift+B` / `Cmd+Shift+B` | Align bottom |

The layout routines (tree, organic, circle …) only exist in the **Arrange** menu.

---

## Text editing (in a cell label)

| Shortcut | Purpose |
|----------|---------|
| `Ctrl+B` / `Cmd+B` | Bold |
| `Ctrl+I` / `Cmd+I` | Italic |
| `Ctrl+U` / `Cmd+U` | Underline |
| `Esc` | End text editing |
| HTML tags | `<b>`, `<i>`, `<br>` in cell labels (when HTML is enabled) |

---

## Pages and zoom

| Shortcut / control | Purpose |
|--------------------|---------|
| `Ctrl`+scroll | Zoom in/out |
| Zoom slider at the bottom | Set the zoom level |
| View > Zoom (menu) | Zoom in, zoom out, choose a scale |
| `+` button next to the page tabs | Insert a new page |
| Right-click on a page tab | Rename, duplicate, delete |

---

## Search

Shape search works through the **search field on the left** — there is no shortcut for it. The browser's text search (`Ctrl+F`) only finds interface text, not cell contents.

---

## NOT available

| Common expectation | Status |
|--------------------|--------|
| Tool letters (`R`, `T`, `A` …) | ❌ Not available — draw.io has no tool keys |
| `Ctrl+S` save | ❌ The web version triggers the browser save dialog; saving runs through the menu bar (desktop: version-dependent) |
| `Ctrl+F` search in the diagram | ❌ Not documented as a draw.io feature |
| Command palette / `Ctrl+Shift+P` | ❌ Not available |
| Switching pages by key | ❌ Not documented — use the page tabs |
| `Ctrl+P` print | ❌ No documented key — menu File > Print |

---

## Mac variants

| Shortcut | Purpose |
|----------|---------|
| `Cmd+Z` / `Cmd+Y` | Undo / redo |
| `Cmd+A` | Select all |
| `Cmd+C` / `Cmd+X` / `Cmd+V` | Clipboard |
| `Cmd+D` | Duplicate |
| `Cmd+G` / `Cmd+Shift+G` | Group / ungroup |
| `Cmd+Shift+L/C/R/T/M/B` | Align |
| `Cmd+Shift+C/X/V` | Copy / cut / paste style |
| `Option`+drag | Clone (instead of `Alt`) |

---

## Mouse gestures (supplementary)

| Gesture | Purpose |
|---------|---------|
| Briefly hover a shape | Connection points appear |
| Drag the middle of an edge | Bend the edge, a waypoint is created |
| `Alt`+click on an edge segment | Remove a waypoint |
| Drag a shape into a container | The shape becomes a child |
| `Ctrl`+scroll | Zoom |
| Right mouse button | Context menu of the cell or area |

---

## Summary

draw.io relies on menu + mouse rather than quick-start keys:

- **Classics** for undo/redo, clipboard, selecting, grouping
- **`Ctrl+Shift`+letter** for aligning and style transfer — the most distinctive shortcut family
- **No tool keys, no search, no palette** — these expectations are deliberately not met (see the table above)
