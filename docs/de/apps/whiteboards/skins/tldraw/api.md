# tldraw - API Dokumentation

## Übersicht

tldraw hat **keine öffentliche REST-API**. Die Integrationsschienen sind: (1) das **SDK** (`tldraw` npm-Paket, `Editor`-API) zum Einbetten und Erweitern, (2) das **Snapshot-Dateiformat** `.tldr` (JSON) und (3) das **Sync-Protokoll** für Multiplayer. Wer Kalender-/Datenanbindung wie bei REST-Systemen erwartet, baut sie um SDK und Store.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| SDK `Editor`-API | Shapes erstellen/ändern, Events, Tools | offiziell |
| `.tldr` Snapshots | Export/Import, Persistenz | offiziell (TLSchema versioniert) |
| Sync-Protokoll (tldraw-sync) | Multiplayer-Store (WebSocket-basiert) | offiziell (Adapter-Interface) |
| REST-Endpunkte | — | ❌ Nicht vorhanden |
| Webhooks | — | ❌ Nicht vorhanden (Store-Events ersetzen das) |

## SDK: Editor-API (Auszug)

```ts
import { Tldraw, createShapeId } from "tldraw";

const handle = (editor) => {
  editor.createShape({
    id: createShapeId(),
    type: "note",
    x: 100, y: 100,
    props: { text: "FreeSynergy-Skin", color: "yellow" },
  });

  editor.sideEffect(() => {
    editor.select(allShapeIds);
    editor.zoomToFit();
  });

  const un = editor.store.listen((entries) => {
    // Records_changed → Persistenz/Analytics andocken
  }, { source: "user", scope: "document" });
};

<Tldraw onMount={handle} />;
```

| API-Bereich | Beispiele |
|-------------|-----------|
| Shapes | `createShape`, `updateShape`, `deleteShapes`, `getShape` |
| Auswahl/Kamera | `select`, `zoomToFit`, `setCamera` |
| Seiten | `createPage`, `setCurrentPageId` |
| Custom Tools/Shapes | `TldrawUtil`, `TLShapeUtil` |
| Store-Events | `store.listen(...)` (statt Webhooks) |

## Dateiformat `.tldr`

```json
{
  "tldrawState": {
    "store": {
      "document:doc": { "typeName": "document", "name": "Board" },
      "shape:zz1": { "typeName": "shape", "type": "note", "x": 100, "y": 100, "props": { "text": "Idee" } }
    }
  },
  "snapshot": { ... }
}
```

Migrierbar über `@tldraw/tlschema` (versionierte Migrationskette).

## Sync / Multiplayer

- Interface `TLStore` + Adapter (`tldraw-sync`): eigener WebSocket-Server möglich
- Gehostete Variante (tldraw Pro) mit Link-Freigaben und Ratcheting-CRDT
- Rechte: `owner`, `editor`, `viewer` (link-based)

## Authentifizierung

- App/Cloud: Konto bzw. Share-Link; ❌ keine API-Keys
- Selbst gehostetes Sync: Auth ist Sache des eigenen Adapters (z.B. JWT beim Connect)

## Rate Limits

Cloud: dokumentierte Fair-Use-Grenzen ohne feste öffentliche Zahlen (Stand: nicht abschließend publiziert); self-hosted: selbst gesetzt.

## SDKs und Pakete

| Paket | Zweck |
|-------|-------|
| `tldraw` | App + Editor |
| `@tldraw/tlschema` | Store-Schema/Migrationen |
| `@tldraw/utils` | Geometrie-Helfer |
| `tldraw-sync` | Sync-Adapter |

## Skin-Hinweis

FreeSynergy-Skin = React-Einbettung von `<Tldraw/>` plus eigene Persistenz; Whiteboard-Inhalte lassen sich per Snapshot auf das Block-/File-Modell ([modelle.md](../../../../data/modelle.md)) mappen.
