# tldraw - API documentation

## Overview

tldraw has **no public REST API**. The integration rails are: (1) the **SDK** (the `tldraw` npm package, the `Editor` API) for embedding and extending, (2) the **snapshot file format** `.tldr` (JSON) and (3) the **sync protocol** for multiplayer. Anyone expecting calendar/data connectivity as with REST systems builds it around the SDK and the store.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| SDK `Editor` API | Create/change shapes, events, tools | official |
| `.tldr` snapshots | Export/import, persistence | official (TLSchema versioned) |
| Sync protocol (tldraw-sync) | Multiplayer store (WebSocket-based) | official (adapter interface) |
| REST endpoints | — | ❌ Not available |
| Webhooks | — | ❌ Not available (store events replace that) |

## SDK: the Editor API (excerpt)

```ts
import { Tldraw, createShapeId } from "tldraw";

const handle = (editor) => {
  editor.createShape({
    id: createShapeId(),
    type: "note",
    x: 100, y: 100,
    props: { text: "FreeSynergy skin", color: "yellow" },
  });

  editor.sideEffect(() => {
    editor.select(allShapeIds);
    editor.zoomToFit();
  });

  const un = editor.store.listen((entries) => {
    // records changed → attach persistence/analytics
  }, { source: "user", scope: "document" });
};

<Tldraw onMount={handle} />;
```

| API area | Examples |
|----------|----------|
| Shapes | `createShape`, `updateShape`, `deleteShapes`, `getShape` |
| Selection/camera | `select`, `zoomToFit`, `setCamera` |
| Pages | `createPage`, `setCurrentPageId` |
| Custom tools/shapes | `TldrawUtil`, `TLShapeUtil` |
| Store events | `store.listen(...)` (instead of webhooks) |

## File format `.tldr`

```json
{
  "tldrawState": {
    "store": {
      "document:doc": { "typeName": "document", "name": "Board" },
      "shape:zz1": { "typeName": "shape", "type": "note", "x": 100, "y": 100, "props": { "text": "Idea" } }
    }
  },
  "snapshot": { ... }
}
```

Migratable via `@tldraw/tlschema` (a versioned migration chain).

## Sync / multiplayer

- Interface `TLStore` + adapter (`tldraw-sync`): your own WebSocket server is possible
- The hosted variant (tldraw Pro) with link sharing and a ratcheting CRDT
- Rights: `owner`, `editor`, `viewer` (link-based)

## Authentication

- App/cloud: account respectively share link; ❌ no API keys
- Self-hosted sync: authentication is the job of your own adapter (e.g. JWT on connect)

## Rate limits

Cloud: documented fair-use limits without fixed public figures (as of: not conclusively published); self-hosted: set by yourself.

## SDKs and packages

| Package | Purpose |
|---------|---------|
| `tldraw` | App + editor |
| `@tldraw/tlschema` | Store schema/migrations |
| `@tldraw/utils` | Geometry helpers |
| `tldraw-sync` | Sync adapter |

## Frontend note

A FreeSynergy skin = the React embedding of `<Tldraw/>` plus your own persistence; whiteboard content can be mapped onto the block/file model ([models.md](../../../../../../data/models.md)) via snapshots.
