# tldraw - Description

## Overview

tldraw combines two products: a finished whiteboard app (tldraw.com) and a React library with which developers build their own drawing and diagramming apps. Both share the same canvas, the same data model and the same synchronisation layer.

## What tldraw does

- Free drawing on an unlimited surface: rectangles, ellipses, arrows, notes, text, lines, freehand, images, frames, groups
- Tools with styles: colours, fill types, line styles, sizes, fonts, alignment
- Files with several pages, automatic local saving and snapshot files (`.tldraw`)
- Multi-user operation: shared links, other people's cursors, following, presence — with your own sync server or the hosted sync cloud
- SDK for your own shapes, tools, panels and derivations (custom bindings/derivations)
- Embeddable read-only mode for displaying third-party products

## Advantages

- **SDK first**: whiteboard features as clean TypeScript building blocks (`@tldraw/editor`, `@tldraw/tlschema`)
- **Modern data model**: record-based, versioned, migratable — ideal for synchronisation
- **Synchronisation included**: sync packages and server are part of the project
- **Local-first**: fully workable without a network, files stay with the user
- **Active development**: well documented site tldraw.dev, frequent releases
- **Free to use**: app and source code are open (newer licence conditions version-dependent)

## Differentiation from other systems

### tldraw vs. Excalidraw
- **tldraw** draws cleanly and, as a library, targets product developers
- **Excalidraw** is the finished sketch app in a hand-drawn style
- **Excalidraw** encrypts collaboration end-to-end, **tldraw** does not

### tldraw vs. draw.io
- **draw.io** is a page- and shape-library-driven diagramming tool with a menu bar
- **tldraw** is a free canvas without a shape catalogue, but with multiplayer infrastructure
- **draw.io** exports VSDX/XML, **tldraw** exports PNG/SVG/snapshots

### tldraw vs. Miro
- **Miro** is a commercial platform with templates, permissions, a REST API and admin consoles
- **tldraw** supplies the shell: app plus SDK, but no administration
- **Miro** hosts everything, **you** operate **tldraw** yourself (or use the sync cloud on offer)

## Technical details

- **Backend**: the app is local-first with no backend of its own; multi-user operation via the `@tldraw/sync` client with a TLSync server (Node.js, Redis) or the hosted tldraw-sync cloud (version-dependent)
- **Database**: no mandatory standard server database; locally IndexedDB, server-side depending on how the sync setup is built (Redis with tlsync)
- **Frontend**: React + TypeScript, its own canvas renderer, an atom-like state layer
- **Authentication**: none in core and app; for self-hosted operation you supply login and room rights
- **Hosting**: static web app (Vite/Next), TLSync server or managed cloud; starter: `npm create tldraw@latest`

## Who tldraw suits

- **Product teams** that want to build a whiteboard into their own SaaS
- **Workshop facilitators** who want to share quickly and draw together
- **Prototype builders**: your own shape types and tools doable in hours
- **Open-source communities** looking for a maintainable canvas foundation
