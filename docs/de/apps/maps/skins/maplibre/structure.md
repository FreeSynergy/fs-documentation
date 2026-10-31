# MapLibre - Struktur und UI/UX

## Layerraufbau

```
┌──────────────────────────────────────────────────────┐
│ Controls (zoom/geo/scale)   [NavigationControl…]     │
│  ╔══════ Canvas (WebGL) ══════╗   DOM-Overlay:       │
│  ║ background → fill → line → ║   Marker/Popups      │
│  ║ symbol → heatmap → hillshade║  (maplibregl.Marker) │
│  ╚════════════════════════════╝                      │
│ Attribution (Pflicht)                                │
└──────────────────────────────────────────────────────┘
style.json: layers[] in Zeichenreihenfolge, sources{}
```

- Stil-Layer **von unten nach oben** gezeichnet; Filter/Zoom-Stufen pro Layer
- Kamera: center/zoom + bearing/pitch (3D)

## UI/UX

- flüssige 60-fps-Kamera, Beschriftungen kollisionsfrei (symbol placement)
- Dark-/Light-Stile aus einem Stil-JSON (paint-Expressionen)

## Interaktionen

- Rechtsklick+Ziehen = Rotate/Tilt; `Shift+Drag` = Pitch
- `queryRenderedFeatures` für Hover/Click auf Vektorelemente

## Responsive Design

- Canvas skaliert; Mobile-Touch-Gesten (Pinch/Rotate) integriert

## Accessibility

- Canvas selbst nicht lesbar → **DOM-Overlays + ARIA-Buttons** für Interaktionen bereitstellen (App-Aufgabe)

## Performance

- Kachel-Overfetch begrenzen, `optimizeForTerrain`, Glyph-/Sprite-Caching; PMTiles reduziert Requests
