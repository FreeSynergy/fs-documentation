# uMap - Structure and UI/UX

## Layout

```
┌──────────────────────────────────────────────────────────────────┐
│ uMap  map "Meeting points Nordring"   ⚙ (editors only)  👁/✎      │
├───────────┬──────────────────────────────────────────────────────┤
│ Layers    │     (OSM tiles with markers/clusters)                │
│▸Routes    │            ⬤  ⬤⬤                                     │
│▸Places(12)│     Popup: title + text + image, "edit"              │
│ Filter…   │                                                      │
└──────────────────────────────────────────────────────────────────┘
Zoom +/− · attribution OSM
```

- The layer list on the left (newer uMap versions: a sheet list bottom right), the popup dialog centred
- The edit mode colours the tools; the read mode hides them

## UI/UX

- Deliberately simple: symbols instead of GIS terminology ("marker" instead of "feature")
- Popup fields freely configurable (an input form per layer)

## Interactions

- **Click on the map** = a new element in the active mode; dragging moves it
- Remote layers are read-only (symbol), import shows a preview

## Responsive design

- The web is responsive; mobile editing is possible, comfort on desktop

## Accessibility

- Standard web (Leaflet); popup contents can be designed accessibly with HTML

## Performance

- Thousands of markers → enable clustering; cache the remote GeoJSON
