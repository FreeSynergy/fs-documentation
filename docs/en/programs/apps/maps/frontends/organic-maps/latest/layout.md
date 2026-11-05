# Organic Maps - Structure and UI/UX

## App layout

```
┌──────────────────────────────────┐
│       (fullscreen map, 3D)       │
│             ⬤⬤ Favourites        │
│  Layer◧  Compass⌖                │
├──────────────────────────────────┤
│ [🔍 Search or address …]          │
│ Category grid (when nothing      │
│ is selected)                     │
│ Tab: Map | Saved | Navigation    │
└──────────────────────────────────┘
POI details as a sheet from below (swipeable)
```

## UI/UX

- Apple-like clarity: one sheet, one search field, icons with labels
- Categories in colourful tiles (offline POI classification)

## Interactions

- Panning/zooming/two-finger rotation; pull the sheet up for POI details
- "Route" = a two-button workflow (start/destination via map/search)

## Responsive design

- Phone + tablet; desktop preview (mind the project progress)

## Accessibility

- VoiceOver/TalkBack basics; voice guidance in navigation

## Performance

- Region downloads staged; offline search results <1 s
