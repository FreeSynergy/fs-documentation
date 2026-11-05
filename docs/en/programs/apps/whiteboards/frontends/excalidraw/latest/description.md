# Excalidraw - Description

## Overview

Excalidraw is an open-source whiteboard application (MIT licence) for sketchy diagrams, mockups and brainstorming. It starts without an account, saves locally, and allows real-time collaboration with end-to-end encryption.

## What Excalidraw does

- Sketches in a hand-drawn style: rectangles, ellipses, diamonds, arrows, lines, freehand lines, text, images and frames
- Real-time collaboration: shared rooms with cursor display and a shared scene
- Files in an open JSON format (`.excalidraw`) plus export as PNG, SVG and `.excalidraw.png`
- Reusable shape collections (`.excalidrawlib`) and a public library (libraries.excalidraw.com)
- Embedding in your own applications through the npm package `@excalidraw/excalidraw` (React component)
- Converting Mermaid text diagrams into editable Excalidraw elements

## Advantages

- **Free and open source**: MIT licensed, fully self-hostable
- **Ready immediately**: start on excalidraw.com without registration
- **Hand-drawn look**: the Rough.js rendering lowers the barrier for drafts
- **Privacy**: shared rooms are end-to-end encrypted (key in the URL fragment)
- **Simple format**: `.excalidraw` is readable, versionable JSON
- **Embeddable**: whiteboard features can be integrated directly into your own web apps
- **Lean**: short toolbar, minimal onboarding time

## Differentiation from other systems

### Excalidraw vs. draw.io
- **draw.io** focuses on exact technical diagrams with large shape libraries and an XML format
- **Excalidraw** focuses on fast sketches with few tools and a lot of drawing flow
- **draw.io** offers cloud storage (Drive, OneDrive), **Excalidraw** primarily stores locally

### Excalidraw vs. Miro
- **Miro** is a commercial platform with templates, voting, permission management and admin consoles
- **Excalidraw** is a lean tool without administration features
- **Miro** has a documented REST API, **Excalidraw** deliberately has no public API

### Excalidraw vs. tldraw
- **tldraw** sees itself primarily as a whiteboard library/SDK for your own apps
- **Excalidraw** ships a finished app and offers embedding on top
- **Excalidraw** has the distinctive hand-drawn style, **tldraw** draws cleanly

## Technical details

- **Backend**: no classic app backend; optional collaboration servers (Node.js, WebSocket), on excalidraw.com additionally Firebase for room persistence (version-dependent)
- **Database**: no database of its own in the core app; scenes live as JSON files or in the room persistence of the collaboration server
- **Frontend**: React + TypeScript, rendering on an HTML canvas with Rough.js
- **Authentication**: none for the community version; accounts only exist in the commercial Plus offering (version-dependent)
- **Hosting**: self-hosted via Docker (app plus collaboration server) or through excalidraw.com

## Who Excalidraw suits

- **Product and design teams**: fast wireframes, user flows and workshop results
- **Developers**: architecture and flow sketches, directly versionable as text JSON (Git-friendly)
- **Teachers and learners**: concepts that need explaining without drawing frustration
- **Privacy-critical environments**: self-hosted without user accounts, encrypted links
- **App developers**: whiteboard features as a React component in their own products
