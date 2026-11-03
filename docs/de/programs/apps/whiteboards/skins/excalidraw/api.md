# Excalidraw - API Dokumentation

## Übersicht

Excalidraw bietet **keine offizielle öffentliche REST-API**. Die dokumentierten Schnittstellen sind das Dateiformat, das Bibliotheksformat, das React-SDK (npm) und der WebSocket-Kollaborationsserver. Die Raumpersistenz von excalidraw.com (Firebase) ist ein Implementierungsdetail und keine öffentliche API.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST-API | — | ❌ Nicht vorhanden |
| WebSocket (Kollaboration) | Räume, Cursors, Szenen-Diffs | Aus dem Quellcode ersichtlich, nicht als stabile API dokumentiert (versionsabhängig) |
| Dateiformat `.excalidraw` | Szenen speichern, laden, austauschen | Öffentlich dokumentiert |
| Bibliotheksformat `.excalidrawlib` | Formensammlungen | Öffentlich dokumentiert |
| npm-SDK `@excalidraw/excalidraw` | Einbettung in eigene Apps | Öffentlich dokumentiert |
| Webhooks | — | ❌ Nicht vorhanden |

## Authentifizierung

- **Keine** Authentifizierung der Kern-App: keine Tokens, kein OAuth, keine API-Keys
- **Ende-zu-Ende-Verschlüsselung**: Der Schlüssel eines Kollaborationsraums steht im URL-Fragment (`#`) und wird an Server nie übertragen
- **Plus-Angebot**: E-Mail-basierte Konten für gespeicherte Dateien (versionsabhängig), nicht als Entwickler-API geöffnet
- **Self-Hosted**: Zugangsschutz kann vorgeschaltet werden (Reverse Proxy, SSO) — Teil der Installation, nicht von Excalidraw

## Endpunkte

Öffentliche HTTP-Endpunkte existieren nicht. Der Kollaborationsaustausch läuft über WebSocket-Nachrichten zwischen Client und Collab-Server. Die konkreten Nachrichtentypen stammen aus dem Quellcode (excalidraw-room bzw. der neuere Collab-Server) und sind **nicht als stabile, öffentliche API dokumentiert**:

| Richtung | Nachrichtentyp (schematisch) | Beschreibung |
|----------|------------------------------|--------------|
| Client → Server | join / exit | Raum betreten oder verlassen |
| Server → Client | scene | Vollständige Szene beim Beitritt |
| Client → Server | update (Element-Diffs) | Geänderte Elemente mit `version`/`versionNonce` |
| Server → Client | Weiterleitung | Verteilt Diffs an alle anderen Teilnehmenden |

Konfliktlösung: pro Element gewinnt die höchste `version`; bei Gleichstand entscheidet `versionNonce` (Last-write-wins, kein vollwertiger CRDT).

## Dateiformat: die echte Schnittstelle

Eine `.excalidraw`-Datei ist JSON. Vollständiges Beispiel:

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
      "text": "Anfrage",
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

### Elementtypen und Schlüssel-Eigenschaften

| Typ | Besondere Eigenschaften |
|-----|-------------------------|
| `rectangle`, `ellipse`, `diamond` | `x`, `y`, `width`, `height`, `angle`, `roundness` |
| `line`, `arrow` | `points[]`, `startBinding`/`endBinding` (Andocken an Formen) |
| `freedraw` | `points[]`, `simulatePressure` |
| `text` | `text`, `fontSize`, `fontFamily`, `textAlign`, `containerId` (Bindung an Form) |
| `image` | `fileId` (Verweis in `files`), `status` |
| `frame` | `name`, Kinder referenzieren über `frameId` |
| `embeddable` | `src` (eingebettete URL, versionsabhängig) |

## Beispiel: Szene einlesen und auswerten (CLI)

```bash
# Anzahl und Typen der Elemente einer Datei
jq -r '.elements[].type' scene.excalidraw | sort | uniq -c
```

## Beispiel: Einbettung (React)

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

## Beispiel: Kollaboration testen (wscat statt curl)

Da keine HTTP-API existiert, gibt es keine sinnvollen curl-Aufrufe. Der Raum-Traffic lässt sich nur protokollseitig beobachten — die Message-Namen sind nicht stabil:

```bash
npm i -g wscat
wscat -c "wss://<collab-server>/?roomId=<room-id>"
# Client meldet sich (schematisch, aus dem Quellcode):
{"type":"join","roomId":"<room-id>"}
# Server antwortet mit verschlüsseltem Szenen-Update (E2E)
```

## Rate Limits

- Für Self-Hosted-Instanzen **nicht definiert**; es gelten die Grenzen des eigenen Servers
- Für excalidraw.com gelten die Limits der eingesetzten Infrastruktur (Firebase/WebSocket-Host), publicly nicht als Kontingente ausgewiesen (versionsabhängig)

## Webhooks

❌ Nicht vorhanden. Ereignisse (neue Elemente, Beitritte) können nur durch eigene Auswertung des Kollaborationsservers oder durch Pollen gespeicherter Dateien beobachtet werden.

## SDKs und Client-Bibliotheken

- **`@excalidraw/excalidraw`** (offiziell, npm): React-Komponente inkl. Toolpalette und Panels
- **excalidraw-room / offizieller Collab-Server** (offiziell, GitHub): WebSocket-Server zum Selbsthosten
- **Community**: Obsidian-Plugin „Excalidraw“, VS-Code-Erweiterung für `.excalidraw`
- **Eigene Clients**: Da das Format offenes JSON ist, genügen in jeder Sprache Standard-JSON-Bibliotheken

## Siehe auch

- [description.md](description.md)
- [menu.md](menu.md)
- [features.md](features.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
