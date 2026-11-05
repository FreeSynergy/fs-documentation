# MapLibre - Keyboard shortcuts

## Overview

MapLibre defines **no keyboard API** (the arrow-key mode as in Leaflet is missing); control is via mouse/touch/controls.

> State: maplibre-gl 4.x.

## Interactions (mouse/touch)

| Input | Function |
|-------|----------|
| Drag | Pan |
| Scroll | Zoom |
| Right-click drag / `Shift+drag` | Rotate/pitch |
| Double-click / `Shift+double-click` | Zoom in/out |
| Pinch/rotate (touch) | Zoom/rotation |

## Explicitly not present

- No built-in keyboard movement (implementable yourself via the API `map.setCenter/zoomTo`)

## Mac

Identical (`Shift` as above).
