# OpenStreetMap - Struktur und UI/UX

## Karten-UI

```
┌──────────────────────────────────────────────────────────────────┐
│ OSM  Suchen…            [Standard|Cycle|Trace]  Anmelden Bearb. │
│ routing↗  share⤴  notiz✚                                        │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│        (Kartenkacheln mit POI-Clustern, Ebenen-Layer)            │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│zoom +/−   attribution: „© OpenStreetMap contributors“            │
└──────────────────────────────────────────────────────────────────┘
```

iD-Editor: links Preset-Suche, rechts Feld-Panel (Tags), oben „Fertig“.

## UI/UX

- Kartenansicht minimalistisch (Leaflet-basiert); iD führt mit Presets, Warnungen
- Changeset-Dialog mit „Was habe ich geändert?“ + Hilfe-Link

## Interaktionen

- **iD**: Objekte anklicken, Kontextmenü („Rechteck zeichnen“, „Straße teilen“), Undo/Redo
- **JOSM**: Multiselektion, Relationen-Editoren, „Konflikte prüfen“ vor Upload
- Änderungen werden live als Ebene sichtbar (Community-Kachel nach Rendering)

## Responsive Design

- Website kartenlastig; Mobil-Editieren über site-Skins (StreetComplete etc.)

## Accessibility

- iD tastaturbedienbar (Tab/Enter für Presets, Shortcuts siehe [shortcuts.md](shortcuts.md)); Beschriftungs-Kontraste nach WCAG-Bemühen

## Performance

- große JOSM-Datensätze (>100k Objekte) brauchen RAM; Overpass-Timeouts bei Weltabfragen
