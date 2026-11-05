# Excalidraw - Menu items

## Overview

Excalidraw has no classic application menu but a slim header, a toolbar, a Plus menu for inserting and a properties panel for the selection. Right clicks open context-dependent menus. The availability of individual items depends on the version and on whether the community version or the Plus offering is used.

## Main menu items

### 1. Main menu (hamburger icon, top left)
- **Purpose**: file and basic settings
- **Details**:
  - New canvas
  - Open (file from disk)
  - Save (as `.excalidraw`)
  - Export image (PNG, SVG, selection)
  - Clear canvas
  - Theme (light/dark) and language
  - Help and keyboard shortcuts
  - Own files respectively Plus account (only in the Plus offering, version-dependent)

### 2. Toolbar
- **Purpose**: choosing the drawing tool
- **Details**:
  - Selection, hand, eraser
  - Rectangle, diamond, ellipse
  - Arrow, line, freehand
  - Text, image
  - Frame and tool lock (`Q`)
  - Undo/redo and zoom level (in the header or the toolbar depending on version)

### 3. Live collaboration (collaboration icon)
- **Purpose**: start and share joint rooms
- **Details**:
  - "Start live collaboration"
  - Copy edit link
  - Copy view link
  - Stop collaboration
  - Participant list and "follow cursor"

### 4. Plus menu ("add elements")
- **Purpose**: insert advanced content
- **Details**:
  - Search the library
  - Insert image
  - Insert Mermaid diagram
  - Embedding/frame objects (version-dependent)

### 5. Properties panel (left, only on selection)
- **Purpose**: design the selected elements
- **Details**:
  - Stroke colour, background colour, fill style
  - Stroke width and stroke style (solid, dashed, dotted)
  - Roughness (sketch level) and opacity
  - Font family and font size, text alignment
  - Bring to front/send to back, duplicate, delete, lock
  - Add link to element

### 6. Library panel (right)
- **Purpose**: manage shape collections
- **Details**:
  - Create and save your own libraries (`.excalidrawlib`)
  - Load public libraries
  - Add the selection of current elements to a library

## Context menus (right-click)

### On elements
- To front / to back, bring to front / send to back
- Duplicate, copy, paste, cut
- Group / ungroup
- Delete
- Lock / unlock (version-dependent)
- Add link, add to library
- Align and distribute (with multiple selection)
- Mirror horizontally/vertically

### On the canvas (empty area)
- Select all
- Paste
- All objects to front/back

### On text
- Font and size (with an active selection)
- Line breaks and alignment

## Menus by user role

### Operator of an instance (admin)
- Configuration of the instance via environment variables (collaboration server, persistence)
- Decisions about Plus accounts and file storage
- No admin menu in the interface itself — administration is purely file-based

### Editor (edit link)
- All tools, properties panel, collaboration, saving and export
- Undo/redo, grouping, frames, libraries

### Reader (view link respectively view mode)
- Only zooming and panning (hand tool, scrolling)
- No tools, no properties panel, no saving of the scene
- Own name for the cursor display can be set optionally

## Notes

- The exact labelling and arrangement of the items changes with the versions; this list describes the community interface as the standard case
- Shortcuts for the menu items are in [shortcuts.md](shortcuts.md)
