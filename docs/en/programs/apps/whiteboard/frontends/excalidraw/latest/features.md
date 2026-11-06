# Excalidraw - Features

## Overview

Excalidraw's core consists of canvas, toolbar and properties panel. The features divide into five areas: drawing tools, object model, real-time collaboration, files/libraries and embedding in your own applications.

---

## 1. Drawing tools

- **Selection tool** (`V`): select, move and scale elements; `Shift`+click for multiple selection
- **Hand tool** (`H`): move the canvas without selecting elements
- **Eraser** (`E`): remove elements by dragging; pulling back keeps them
- **Shapes**: rectangle (`R`), ellipse (`O`), diamond (`D`)
- **Lines and arrows** (`L`, `A`): arrows can dock onto shapes and follow them when moved
- **Freehand drawing** (`P`): pen strokes, also with a graphics tablet or touch pen
- **Text** (`X`): own text fields or labels bound to shapes
- **Images**: insert from file, clipboard or via drag & drop
- **Frames**: bounding areas like pages; content can dock to frames
- **Tool lock** (`Q`): the selected tool stays active after drawing

### Modifiers while drawing

- **`Shift`**: fixes line/arrow angles to 15° steps, scales proportionally
- **`Alt`+drag**: clone the element instead of moving it
- **Double-click** on a shape: edit the bound label
- **Arrow keys**: move selected elements pixel by pixel

---

## 2. Object model (elements)

- A scene is an ordered array of elements with types such as `rectangle`, `ellipse`, `diamond`, `arrow`, `line`, `freedraw`, `text`, `image`, `frame`, `embeddable`
- Common properties: `x`, `y`, `width`, `height`, `angle`, `strokeColor`, `backgroundColor`, `fillStyle` (hachure/solid), `strokeWidth`, `strokeStyle` (solid/dashed/dotted), `roughness`, `opacity`
- Grouping via `groupIds`, frames via `frameId`, text binding via `boundElements`
- Arrows store reference points on other elements and follow them when moved
- Synchronisation fields: `seed`, `version`, `versionNonce` — changes are exchanged element by element, the highest version wins per element (last-write-wins, not a full CRDT)
- Deletions mark elements with `isDeleted` instead of removing them from the scene immediately

### Scene file (excerpt)

```json
{
  "type": "excalidraw",
  "version": 2,
  "elements": [ { "type": "rectangle", "x": 10, "y": 10, "strokeColor": "#1e1e1e" } ],
  "appState": { "viewBackgroundColor": "#ffffff" }
}
```

---

## 3. Real-time collaboration

- Started through the live collaboration menu; the room link is copied with edit or view rights
- All participants see cursors, selections and (optionally) the names of the others
- End-to-end encryption: the server only relays encrypted messages, the key sits in the URL fragment (`#`)
- The cursors of other participants can be followed ("Follow")
- Built-in **laser pointer** for pointing without leaving marks on the canvas

### Synchronisation

Collaboration transmits differences at element level over WebSocket messages. In the event of a tie, `versionNonce` decides. Details in [api.md](api.md).

---

## 4. Files, export and libraries

- **Saving**: `.excalidraw` (JSON with scene and app state); in supported browsers directly `.excalidraw.png` with an embedded scene
- **Export**: PNG and SVG, optionally only the selection; copy as PNG/SVG to the clipboard
- **Libraries**: your own shape collections as `.excalidrawlib`, load and save through the library panel; public library at libraries.excalidraw.com
- **Mermaid**: convert Mermaid text into editable Excalidraw elements (Plus menu)

---

## 5. Embedding in your own applications

- The npm package `@excalidraw/excalidraw` provides a React component including the toolbar
- Props such as `initialData`, `onChange`, `viewModeEnabled`, `theme` and `langCode` control behaviour and appearance
- **View mode** (`viewModeEnabled`): read-only canvas with zoom and panning
- Callbacks such as `onPointerUpdate` and `onLinkOpen` enable your own integrations

---

## Configuration

- **Your own instance**: environment variables such as `VITE_APP_WS_SERVER_URL` (collaboration server) and `VITE_APP_FIREBASE_CONFIG` (room persistence); names and scope are version-dependent
- **Interface**: theme (light/dark), language, grid (`Ctrl+'`), zen mode (`?`)
- **Session**: the last canvas stays in the browser (localStorage); rooms are optionally persistent

---

## What Excalidraw does NOT do

- **No PDF export** — only PNG, SVG and the native JSON format
- **No comments and no chat** — communication happens outside the app
- **No fine-grained permission management** — only a link that "can edit" or "can view"
- **No version history of files** — only undo/redo within a session
- **No presentation, voting or agenda features** (that is what Miro offers, for example)
- **No public REST API and no webhooks** (see [api.md](api.md))
- **No task or kanban board** — it stays a free canvas

---

## Extensions and plugins

- **No official plugin marketplace** — extensibility through libraries, embedding and forks
- **Obsidian plugin "Excalidraw"** (community): whiteboards directly in the note-taking app
- **VS Code extension** (community): open and edit `.excalidraw` files in the editor
- **excalidraw-room** and the newer collab server: open-source WebSocket servers for self-hosted instances
- **Example apps** in the project repository ("Kitchen Sink") show all embedding variants
