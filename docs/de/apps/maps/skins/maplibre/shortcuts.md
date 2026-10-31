# MapLibre - Tastatur-Shortcuts

## Übersicht

MapLibre definiert **keine Keyboard-API** (Pfeiltasten-Modus wie Leaflet fehlt); Steuerung über Maus/Touch/Controls.

> Stand: maplibre-gl 4.x.

## Interaktionen (Maus/Touch)

| Eingabe | Funktion |
|---------|----------|
| Ziehen | Pan |
| Scroll | Zoom |
| Rechtsklick-Ziehen / `Shift+Ziehen` | Rotate/Pitch |
| Doppelklick / `Shift+Doppelklick` | Zoom in/out |
| Pinch/Drehen (Touch) | Zoom/Rotation |

## Ausdrücklich nicht vorhanden

- keine eingebauten Tastaturbewegungen (selbst implementierbar via API `map.setCenter/zoomTo`)

## Mac

identisch (`Shift` wie oben).
