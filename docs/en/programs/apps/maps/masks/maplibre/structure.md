# MapLibre - Structure and UI/UX

## Layer stack

```
┌──────────────────────────────────────────────────────┐
│ Controls (zoom/geo/scale)   [NavigationControl…]     │
│  ╔══════ Canvas (WebGL) ══════╗   DOM overlay:       │
│  ║ background → fill → line → ║   Marker/popups      │
│  ║ symbol → heatmap → hillshade║  (maplibregl.Marker) │
│  ╚════════════════════════════╝                      │
│ Attribution (mandatory)                              │
└──────────────────────────────────────────────────────┘
style.json: layers[] in drawing order, sources{}
```

- Style layers are drawn **from bottom to top**; filter/zoom levels per layer
- Camera: center/zoom + bearing/pitch (3D)

## UI/UX

- Smooth 60 fps camera, collision-free labels (symbol placement)
- Dark/light styles from one style JSON (paint expressions)

## Interactions

- Right-click + drag = rotate/tilt; `Shift+drag` = pitch
- `queryRenderedFeatures` for hover/click on vector elements

## Responsive design

- The canvas scales; mobile touch gestures (pinch/rotate) integrated

## Accessibility

- The canvas itself is not readable → provide **DOM overlays + ARIA buttons** for interactions (an app task)

## Performance

- Limit tile overfetch, `optimizeForTerrain`, glyph/sprite caching; PMTiles reduces requests
