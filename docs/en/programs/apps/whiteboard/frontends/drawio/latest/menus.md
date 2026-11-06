# draw.io - Menu items

## Overview

draw.io has the most classic menu bar of all whiteboard tools: **File, Edit, View, Arrange, Extras, Help**. Added to that are the shape library on the left, the formatting panel on the right, and context-dependent right-click menus. The names below follow the English interface; individual items exist differently depending on the version (web, desktop, embedded).

## Main menu items

### 1. File
- **Purpose**: new diagrams, open, save, export
- **Details**:
  - New, Open from (device, URL, this browser, Google Drive, OneDrive, Dropbox, GitHub, GitLab, Trello)
  - Recently opened files
  - Edit diagram (XML editor)
  - Save as (device, Google Drive, OneDrive, Dropbox, ...)
  - Export as (PNG, JPEG, SVG, PDF, HTML, XML, VSDX)
  - Versions (history of the cloud storage)
  - Document properties, print, PDF, close

### 2. Edit
- **Purpose**: clipboard, cell operations, text and data
- **Details**:
  - Undo, redo
  - Cut, copy, paste, duplicate, duplicate and move (clone)
  - Delete, select all
  - Edit style, insert/edit link, edit data, edit tooltip
  - Search shapes, lock/unlock
  - Group/ungroup, order (to front/back)

### 3. View
- **Purpose**: display of the canvas and panels
- **Details**:
  - Outline, show/hide search and shape fields
  - Grid, grid colour, tooltips, handles, connectors, page view
  - Scrollbars, scales (version-dependent)
  - Layers dialog
  - Light/dark theme (version-dependent), zoom in/out

### 4. Arrange
- **Purpose**: layout, order, alignment
- **Details**:
  - Layout applications: tree, organic, circle, compact, flow, horizontal/vertical flow, fan, radial, concentric and others
  - Enter/leave group
  - Insert (image, curve, shape templates)
  - Order, align, distribute, rotate, mirror
  - More actions (cell-dependent)

### 5. Extras
- **Purpose**: pages, links, styles, collaboration, language
- **Details**:
  - Realtime Sync (real-time collaboration on cloud files, version-dependent)
  - Pages: insert, duplicate, rename, background, delete
  - Links: edit link, open link, edit tooltip
  - Edit style, colours, reset views
  - To-dos (task markers in the diagram)
  - Current language, paginate/re-paginate (version-dependent)

### 6. Help
- **Purpose**: documentation and keyboard shortcuts
- **Details**:
  - Quick reference of the keyboard combinations
  - References to the diagrams.net documentation
  - Info/About dialog of the desktop version

## Sidebar (left)

- **Search field**: finds shapes across all active libraries
- **Shape libraries**: expandable folders (General, Arrows, BPMN, UML, AWS, Azure, ...)
- **More shapes**: enable additional libraries
- **My shapes**: store your own SVG shapes

## Formatting panel (right)

- **Options**: document settings (grid, background, auto-save)
- **Style**: fill, line, font, edge rendering
- **Arrange**: position, size, rotation, text alignment, data

## Context menus (right-click)

### On shapes
- Edit link, edit style, order, align/distribute
- Group/ungroup, duplicate, delete
- Replace (swap the shape), insert into group

### On edges
- Edit waypoints, direction/arrowheads, style, delete

### On page tabs (bottom)
- Insert page, duplicate, rename, background colour, delete

### On an empty canvas
- Paste, paste here, select all, grid/view shortcuts

## Menus by user role

### Operator / self-hosted admin
- Configure screen of the instance (storage keys, allowed services)
- `configure.js`/additional configuration, theme defaults, plugin selection
- The desktop version: filesystem permissions via the operating system

### Editor
- Full menu bar, all tools, save and export
- Start/leave Realtime Sync, manage pages

### Reader
- draw.io distinguishes **no app roles**: "read only" arises through
  - opening a file without write permission in the cloud storage
  - an embedded view without save buttons (`chrome=0`, `noSaveBtn`, version-dependent)
- In these modes view, zoom and export stay usable, saving is dropped

## Notes

- The web, desktop and embedded versions show different proportions of the menus (e.g. "Open from cloud" is dropped offline)
- Shortcuts for all items: [shortcuts.md](shortcuts.md)
