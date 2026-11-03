# Leaflet - Struktur und UI/UX

## DOM-Struktur

```
<div class="leaflet-container">
  ├ pane "tile"      (Kachel-<img>s, transformiert)
  ├ pane "overlay"   (SVG/Canvas: Polyline/Polygon)
  ├ pane "shadow"/"marker" (Marker-DOM)
  ├ pane "popup"/"tooltip"
  └ .leaflet-control-* (zoom, layers, scale, attribution)
</div>
```

## UI/UX

- Controls schweben über der Karte (oben links zoom, unten rechts attribution)
- Popups = Sprechblasen mit HTML, Tooltips = hover-Knubbels

## Interaktionen

- Drag-Panning inertial, Scroll-Wheel-Zoom, Doppelklick-Zoom; Touch-Pinch
- Events: `click`, `markerdragend`, `moveend` (für Lade-Nachladen „streaming tiles“)

## Responsive Design

- automatisch; `invalidateSize()` nach Layoutwechsel nötig (häufigster Bug)

## Accessibility

- Tastaturmodus (Pfeile/`+`/`-`, siehe [shortcuts.md](shortcuts.md)); Marker brauchen `alt`/`title`-Pflege durch die App

## Performance

- Kachelanzahl begrenzen, `preferCanvas` bei vielen Polygonen, Marker-Clusterung per Plugin
