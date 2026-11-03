# Node-RED - Struktur und UI/UX

## Editorstruktur

```
┌──────────────────────────────────────────────────────────────────┐
│ ☰  Flow 1 ▾                    [Deploy]        🔍 Zoom-/Grid-⌗  │
├───────────┬────────────────────────────────────┬─────────────────┤
│ Palette   │  Canvas (Nodes + Drähte)           │ Info | Debug    │
│ inject    │   [inject]──→[function]──→[debug]  │ msg.payload=…   │
│ function  │      ↘ [http in]→[template]        │ Node-Doku       │
│ switch …  │                                    │ Config          │
│ (Suche)   │   [MQTT in]→[dashboard chart]      │ Dashboard       │
└───────────┴────────────────────────────────────┴─────────────────┘
```

- Palette links (klick = Node auf Canvas), Canvas mit Raster, Sidebar rechts (Info/Debug/Config/Dashboard)
- „Deploy“ = Live-Veröffentlichen der Flows (grüne Nodes = deployed)

## UI/UX

- schlichter, zweckmäßiger Editor; Node-Kategoriefarben; Drähte mit Pfeilen/„Link“-Knoten für Übersichten
- Dark-Mode aktivierbar

## Interaktionen

- **Drag/Drop** Nodes; Klick+Ziehen = Verdrahten; Node-Auswahl mit `Shift`+Klick
- „Trigger node“ zum Testen, Debug-Seitenspalte als Stream
- Multi-User Editing nur über externe Synchronisation (nicht eingebaut)

## Responsive Design

- Desktop-Tool; Canvas mobil unpraktisch (Viewing okay)

## Accessibility

- Formular-/Tab-orientierte Panels; Canvas primär Maus
- Tastatur: Strg+C/V/Z/S usw. (siehe [shortcuts.md](shortcuts.md))

## Performance

- Flows laufen prozessintern; große Nachrichten (Base64-Streams) aufteilen; `flows.json` unter Versionskontrolle
