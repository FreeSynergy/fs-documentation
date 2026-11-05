# Leaflet - Structure and UI/UX

## DOM structure

```
<div class="leaflet-container">
  ├ pane "tile"      (tile <img>s, transformed)
  ├ pane "overlay"   (SVG/canvas: polyline/polygon)
  ├ pane "shadow"/"marker" (marker DOM)
  ├ pane "popup"/"tooltip"
  └ .leaflet-control-* (zoom, layers, scale, attribution)
</div>
```

## UI/UX

- Controls float above the map (zoom top left, attribution bottom right)
- Popups = speech bubbles with HTML, tooltips = hover nubs

## Interactions

- Inertial drag panning, scroll-wheel zoom, double-click zoom; touch pinch
- Events: `click`, `markerdragend`, `moveend` (for loading more "streaming tiles")

## Responsive design

- Automatic; `invalidateSize()` is needed after a layout change (the most common bug)

## Accessibility

- Keyboard mode (arrows/`+`/`-`, see [shortcuts.md](shortcuts.md)); markers need `alt`/`title` care by the app

## Performance

- Limit the tile count, `preferCanvas` with many polygons, marker clustering via plugin
