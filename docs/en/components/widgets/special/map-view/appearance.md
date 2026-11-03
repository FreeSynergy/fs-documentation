# Map View - Appearance

## Base layout
A map view shows interactive maps (Google Maps, Leaflet, OpenStreetMap).

```
┌─────────────────────────────────────────┐
│                                         │
│         🗺️                              │
│         map view                        │
│                                         │
│      [Zoom+]  [Zoom-] [Satellite]       │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **standort** | one marker centred, address line above it |
| **sammlung** | many markers, a list or clusters at high density |
| **route** | lines and areas, start and goal as different symbols |

## Sizes

| Size | Width | Use |
|------|-------|-----|
| Small | 300px | Inline |
| Medium | 500px | Standard |
| Large | 700px | Featured |
| Full | 100% | Full width |

## Colours and states

| State | Colour | Description |
|-------|--------|-------------|
| **Map** | depends on the theme | map theme |
| **Marker** | red/primary | markers |
| **Controls** | white/black | control elements |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `zoom` | zoom on scrolling |
| `drag` | moving the map |

## Responsive

- The map fills the available width; as an inline map it is at least 200 px high.
- Below `small` screen width the zoom and style buttons become a small bar at the bottom,
  the controls stay at least 44 px large.
- Two fingers move and scale (`drag`, `pinch`); plain scrolling over the map moves the
  page, not the map — zoom by scrolling only after clicking on the map.

## Map types

| Type | Description |
|------|-------------|
| **Roadmap** | standard street map |
| **Satellite** | satellite view |
| **Hybrid** | hybrid of roadmap and satellite |
| **Terrain** | terrain view |

## Marker

```
┌─────────────────────────────────────────┐
│      📍                                 │
│   Location                              │
└─────────────────────────────────────────┘
```

## Controls

```
┌─────────────────────────────────────────┐
│      [+]  [-]                           │
│  [Satellite] [Hybrid]                   │
└─────────────────────────────────────────┘
```
