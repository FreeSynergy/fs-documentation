# OsmAnd - Structure and UI/UX

## App layout

```
┌──────────────────────────────────┐
│ ⚙️ status bar · Search…          │
│                                  │
│     (fullscreen map, 3D/2D)      │
│         ⬤ My Places layer        │
│                                  │
│ [Navigation][Plan][My Places]    │  ← bar at the bottom
│ [OSM-Wiki][nearby][configure…]   │
└──────────────────────────────────┘
Side bars: left (downloads/settings),
right (layers/measuring/night) — as chips at the edge
```

- Navigation mode: turn tile at the top + info line at the bottom (distance/time)

## UI/UX

- High feature density; the context menu (long press on the map) is the hub
- Map profiles (standard/ski/topo…) switch style + profiles together

## Interactions

- **Gestures**: double click zoom, two-finger rotation/tilt (3D), long press = context menu (destination/note)
- Drag points for route planning; track-follow mode ("follow route")

## Responsive design

- Phone UI; tablet layout; no desktop version (desktop = OsmAnd? no)

## Accessibility

- Strong voice output (navigation without sight possible); UI contrasts partly weak (dark menus)

## Performance

- Large regions (>1 GB) → mind the storage; building the tile cache costs startup time
