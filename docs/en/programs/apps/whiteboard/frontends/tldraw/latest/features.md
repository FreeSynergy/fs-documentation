# tldraw - Features

## Overview

tldraw combines a slim whiteboard app with a developer SDK. The features group into tools/shapes, the record data model, files and pages, multiplayer synchronisation and SDK extensibility.

---

## 1. Tools and shapes

- **Selection tool** (`V`): select, move, scale, multi-select
- **Hand tool** (`H`): move the canvas
- **Pen** (`D`): freehand lines with a pressure look
- **Eraser** (`E`): erase shapes away
- **Arrow** (`A`): connectable arrows with end points and labels
- **Rectangle** (`R`) and **ellipse** (`O`): basic geometries with fill and line styles
- **Note** (`N`): sticky Post-its in several colours
- **Text** (`T`) and **line** (`L`)
- **Frame** (`F`): bounding area for grouping and export crops
- **Image/bookmark**: media via drag & drop or URL
- **Laser pointer**: a time-limited pointing beam (via the toolbar)

### Styles

- Colour, fill (solid/semi/hatched depending on version), line style (dashed/dotted)
- Three to four size steps, several font families, label colours
- Align, distribute, layers (to front/back), grouping, locking

## 2. Object model (records)

- The whole document state consists of **records** in a versioned store
- Shape records carry `type` (`rect`, `ellipse`, `arrow`, `draw`, `note`, `text`, `line`, `image`, `frame`, `group`, `bookmark`, `embed`) and `props` (position, size, style, label)
- **Bindings** join arrows permanently to shapes (they follow when moved)
- **Groups** and **frames** structure the surface; a `parentId` hierarchy as in scene graphs
- Besides shapes there are system records: `document`, `page`, `camera`, `pointer`, `user`, `styles`, `instance`
- The schema (`@tldraw/tlschema`) is versioned and migrates old files automatically

## 3. Files and pages

- **Several pages** per file, managed through the pages menu
- **Local auto-saving** in IndexedDB (bound to the session via `persistenceKey`)
- **Export/import**: PNG, SVG and snapshot file (`.tldraw`) through the main menu
- **Selection export**: only the marked shapes as an image
- PDF export does not exist (PDF workflow: export SVG and convert it)

## 4. Multiplayer and real-time synchronisation

- **Share dialog**: create a shared link; whoever opens the link draws along
- Presence: coloured cursors, name tags, "following" other participants
- Synchronisation works **record-based**: changes to shapes are exchanged as record deltas, the sync layer handles conflict resolution (a history-bearing store, not classic last-write-wins)
- Operation optionally through a **self-hosted TLSync server** (Node.js + Redis) or the **hosted tldraw-sync cloud** (version/plan-dependent)

## 5. SDK (tldraw as a library)

- The `<Tldraw />` component with full equipment: tools, panels, menus (switchable off)
- **Editor API**: read/write the document, control the camera, export (`getSnapshot`, `loadSnapshot`, `exportToSvg`, `zoomToFit`)
- **Your own shapes/tools/bindings**: class-based extensions with their own schema
- **Custom UI**: your own panels, menus and overlays in the product's design
- **Read-only mode** (`readonly`): show the canvas without editing

---

## Configuration

- **Component props**: `persistenceKey`, `initialState`, `snapshot`, `options` (hide menu items and panels individually), `readonly`
- **Sync connection**: the client package `@tldraw/sync` with server URL, room name and user info
- **UI adjustment**: theme light/dark/system, keyboard shortcut activation, canvas background

---

## What tldraw does NOT do

- **No public REST API and no webhooks** (see [api.md](api.md))
- **No comments** — communication only through cursors and presence
- **No fine-grained permission management in the standard setup** — a link usually means edit
- **No template catalogue** as with Miro — your own start snapshots replace that
- **No PDF export**, no VSDX/XML compatibility
- **No administration**: no user lists, audit logs or SSO out of the box
- **No native mobile app** — web app with touch gestures

---

## Modules and integrations

- **`tldraw`** (npm): complete package for React apps
- **`@tldraw/editor`, `@tldraw/tlschema`**: low-level layers for your own builds
- **`@tldraw/sync`**: client for synchronisation; **TLSync** as the reference server (Redis)
- **Example apps** on tldraw.dev: custom shapes, collaboration, chat overlays, whiteboard products

## Extensions and plugins

- **No plugin marketplace** — extensions are SDK code
- **Derivations**: generate derived shapes automatically from other records
- **Community examples**: diagrams from Markdown, timer panels, voting overlays (self-built, check quality)
