# Excalidraw - API documentation

## Overview

Excalidraw offers **no official public REST API**. The documented interfaces are the file format, the library format, the React SDK (npm) and the WebSocket collaboration server. The room persistence of excalidraw.com (Firebase) is an implementation detail and not a public API.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST API | — | ❌ Not available |
| WebSocket (collaboration) | Rooms, cursors, scene diffs | Evident from the source code, not documented as a stable API (version-dependent) |
| File format `.excalidraw` | Save, load and exchange scenes | Publicly documented |
| Library format `.excalidrawlib` | Shape collections | Publicly documented |
| npm SDK `@excalidraw/excalidraw` | Embedding in your own apps | Publicly documented |
| Webhooks | — | ❌ Not available |

## Authentication

- **No** authentication in the core app: no tokens, no OAuth, no API keys
- **End-to-end encryption**: the key of a collaboration room sits in the URL fragment (`#`) and is never transmitted to the server
- **Plus offering**: email-based accounts for stored files (version-dependent), not opened as a developer API
- **Self-hosted**: access protection can be placed in front (reverse proxy, SSO) — part of the installation, not of Excalidraw

## Endpoints

Public HTTP endpoints do not exist. The collaboration exchange runs over WebSocket messages between client and collab server. The concrete message types come from the source code (excalidraw-room respectively the newer collab server) and are **not documented as a stable, public API**:

| Direction | Message type (schematic) | Description |
|-----------|--------------------------|-------------|
| Client → server | join / exit | Enter or leave the room |
| Server → client | scene | Complete scene on joining |
| Client → server | update (element diffs) | Changed elements with `version`/`versionNonce` |
| Server → client | relay | Distributes diffs to all other participants |

Conflict resolution: per element the highest `version` wins; in a tie `versionNonce` decides (last-write-wins, not a full CRDT).

## File format: the real interface

A `.excalidraw` file is JSON. Complete example:

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
    {
      "id": "x1K9_rect",
      "type": "rectangle",
      "x": 100, "y": 100, "width": 180, "height": 90,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "#a5d8ff",
      "fillStyle": "hachure",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "seed": 123456,
      "version": 1,
      "versionNonce": 987654,
      "isDeleted": false,
      "boundElements": [ { "id": "x1K9_text", "type": "text" } ]
    },
    {
      "id": "x1K9_text",
      "type": "text",
      "x": 140, "y": 130,
      "text": "Request",
      "fontSize": 20,
      "fontFamily": 1,
      "textAlign": "center",
      "containerId": "x1K9_rect"
    }
  ],
  "appState": { "viewBackgroundColor": "#ffffff", "gridSize": null },
  "files": {}
}
```

### Element types and key properties

| Type | Special properties |
|------|--------------------|
| `rectangle`, `ellipse`, `diamond` | `x`, `y`, `width`, `height`, `angle`, `roundness` |
| `line`, `arrow` | `points[]`, `startBinding`/`endBinding` (docking onto shapes) |
| `freedraw` | `points[]`, `simulatePressure` |
| `text` | `text`, `fontSize`, `fontFamily`, `textAlign`, `containerId` (binding to a shape) |
| `image` | `fileId` (reference in `files`), `status` |
| `frame` | `name`, children reference it via `frameId` |
| `embeddable` | `src` (embedded URL, version-dependent) |

## Example: read and evaluate a scene (CLI)

```bash
# count and types of the elements in a file
jq -r '.elements[].type' scene.excalidraw | sort | uniq -c
```

## Example: embedding (React)

```jsx
import { Excalidraw } from "@excalidraw/excalidraw";

function Board({ scene }) {
  return (
    <Excalidraw
      initialData={{ elements: scene.elements, appState: {} }}
      viewModeEnabled={false}
      theme="light"
    />
  );
}
```

## Example: testing collaboration (wscat instead of curl)

Since no HTTP API exists, there are no meaningful curl calls. The room traffic can only be observed at the protocol level — the message names are not stable:

```bash
npm i -g wscat
wscat -c "wss://<collab-server>/?roomId=<room-id>"
# the client announces itself (schematic, from the source code):
{"type":"join","roomId":"<room-id>"}
# the server answers with an encrypted scene update (E2E)
```

## Rate limits

- For self-hosted instances **not defined**; the limits of your own server apply
- For excalidraw.com the limits of the infrastructure in use apply (Firebase/WebSocket host), not published as quotas (version-dependent)

## Webhooks

❌ Not available. Events (new elements, joins) can only be observed by evaluating the collaboration server yourself or by polling stored files.

## SDKs and client libraries

- **`@excalidraw/excalidraw`** (official, npm): React component including tool palette and panels
- **excalidraw-room / official collab server** (official, GitHub): WebSocket server for self-hosting
- **Community**: Obsidian plugin "Excalidraw", VS Code extension for `.excalidraw`
- **Your own clients**: since the format is open JSON, standard JSON libraries in any language suffice

## See also

- [description.md](description.md)
- [menus.md](menus.md)
- [features.md](features.md)
- [layout.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
