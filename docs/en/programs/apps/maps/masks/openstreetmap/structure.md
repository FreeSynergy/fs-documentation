# OpenStreetMap - Structure and UI/UX

## Map UI

```
┌──────────────────────────────────────────────────────────────────┐
│ OSM  Search…             [Standard|Cycle|Trace]  Log in Edit     │
│ routing↗  share⤴  note✚                                          │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│        (Map tiles with POI clusters, layer overlays)             │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│zoom +/−   attribution: "© OpenStreetMap contributors"            │
└──────────────────────────────────────────────────────────────────┘
```

iD editor: preset search on the left, field panel (tags) on the right, "finish" at the top.

## UI/UX

- The map view is minimalist (Leaflet-based); iD guides with presets and warnings
- Changeset dialog with "what did I change?" + a help link

## Interactions

- **iD**: click objects, context menu ("draw rectangle", "split way"), undo/redo
- **JOSM**: multi-selection, relation editors, "validate" before upload
- Changes become visible live as a layer (the community tile after rendering)

## Responsive design

- The website is map-heavy; mobile editing via site skins (StreetComplete etc.)

## Accessibility

- iD is operable by keyboard (Tab/Enter for presets, shortcuts see [shortcuts.md](shortcuts.md)); label contrasts per WCAG efforts

## Performance

- Large JOSM datasets (>100k objects) need RAM; Overpass timeouts on worldwide queries
