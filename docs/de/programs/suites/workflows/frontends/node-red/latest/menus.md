# Node-RED - Menüpunkte

## Kopfmenü (☰)

| Eintrag | Inhalt |
|---------|--------|
| Flows | Import/Export (JSON), Library, Collections, Undo-Verlauf |
| Manage palette | Palette verwalten: Installation/Updates von Nodes |
| Manage context | Flow-/Global-Context (JS-Scope) anzeigen |
| Configuration nodes | Commons (HTTP-Port, MQTT-Broker, Serial…) |
| View | Zoom, Grid, Sidebar-Toggles, Dark-Theme |
| Appearance | Node-Sizing/Labels |

## Node-Kontextmenü (Rechtsklick)

- Disable/Enable, Delete, Cut/Copy, „Trigger node“, Docs (Hilfe-Panel), Subflow-Grenzen setzen

## Sidebar-Tabs (rechts)

| Tab | Inhalt |
|-----|--------|
| Info | Node-Doku, Knoten-Informationen |
| Debug | Nachrichtenstrom (Debug-Knoten-Ausgaben) |
| Config nodes | Instanzen gemeinsamer Konfiguration |
| Dashboard | UI-Builder für Dashboards (Gruppe/Page/Widget) |

## Nodes-Palette (links, kategorisiert)

common (inject, debug, function, switch…) · network (http, mqtt, websocket) · sequence · parser (json, csv, yaml) · storage · analysis · social — plus Community-Paletten.

## Menüs nach Rolle

Node-RED hat keine Benutzerrollen im Kern (Deployment-Schutz: `adminAuth` in `settings.js` Reader/Writer).
