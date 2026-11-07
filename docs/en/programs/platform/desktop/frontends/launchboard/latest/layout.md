# LaunchBoard - Structure & UI/UX

## Overview

After signing in, LaunchBoard shows exactly one area: the active board. Controls sit in a header bar, content in a tile grid. The editor lies as a panel over the board, settings dialogues as an overlay. The interface is designed for high information density and mouse-oriented operation.

## Window structure

### Board view

```
┌──────────────────────────────────────────────────────────────────────┐
│  Header: [Board ▾]   Search bar   [Edit]   [Account ▾]               │
├──────────────────────────────────────────────────────────────────────┤
│  Grid with widget tiles                                              │
│  ┌───────────────┐ ┌───────────────────┐ ┌──────────────────────┐   │
│  │ App tile      │ │ Docker status     │ │ Media / streams      │   │
│  │ Icon · Name   │ │ 8 running · 1 err │ │ 3 active             │   │
│  ├───────────────┤ ├───────────────────┤ ├──────────────────────┤   │
│  │ Indicator 200 │ │ Traffic chart     │ │ Pi-hole 1,240 block. │   │
│  └───────────────┘ └───────────────────┘ └──────────────────────┘   │
│  ┌───────────────────────────────┐  ┌──────────────────────────┐    │
│  │ Note / Markdown               │  │ JSON value from HTTP widget│   │
│  └───────────────────────────────┘  └──────────────────────────┘    │
├──────────────────────────────────────────────────────────────────────┤
│  Toast messages (bottom) · Loading state per tile                    │
└──────────────────────────────────────────────────────────────────────┘
```

### Edit mode

```
┌──────────────────────────┬──────────────────────────────────────────┐
│  Panel: Widget library   │  Grid with handles                       │
│  ┌────────────────────┐  │  ┌[⋮]───────[✎][⧉][✕]─────┐              │
│  │ Search for widgets │  │  │ Tile                    │              │
│  ├────────────────────┤  │  │  Resize corner ↘        │              │
│  │ Structure          │  │  └─────────────────────────┘              │
│  │  App · Text · Image│  │  Alignment lines while dragging          │
│  │ Status             │  │                                          │
│  │  Indicator · Cont. │  │  Board options (columns, spacing)        │
│  │ Integration        │  │  [Preview] [Done]                        │
│  │  Docker · Media    │  │                                          │
│  └────────────────────┘  │                                          │
└──────────────────────────┴──────────────────────────────────────────┘
```

### Settings dialogue (overlay)

```
┌──────────────────────────────────────────────┐
│  Widget settings                     [✕]     │
├──────────────────────────────────────────────┤
│  [General] [Data source] [Display] [Actions] │
│  Field · Selection · Switch · Interval        │
│  Result preview of the data source            │
├──────────────────────────────────────────────┤
│  [Remove]        [Test] [Cancel] [Save]       │
└──────────────────────────────────────────────┘
```

## Areas

| Area | Position | Content |
|---------|----------|--------|
| Header | Top | Board selection, search, edit, account menu |
| Grid | Centre | Widget tiles in columns and rows |
| Widget tile | In the grid | Title bar, icon, content, actions, loading state |
| Widget library | Left (editor) | Categorised tiles to drag in |
| Board settings | Side panel/overlay | Layout, appearance, sharing, devices |
| Instance administration | Own view with sidebar | Users, groups, integrations, auth, licence |
| Toast messages | Bottom | Success, errors, connection tests |
| Log | Instance administration | Event list of the instance |

## UI/UX

### Design principles

- **Mouse before keyboard**: everything essential is clickable, no hidden combinations
- **Immediate effect**: layout changes take effect without a save button
- **Curated selection**: widget library instead of endless possibilities

### Colour scheme and themes

- **Light and dark** plus system setting, switchable per account
- **Accent colour** and opacity/blur for tiles, corner radius and shadow adjustable
- **Background images** per board (upload or URL), with dimming for readability
- **Global themes** (administrators) apply as the default for all boards

### Interactions

- **Drag and drop**: drag a tile from the library into the grid; target area is highlighted
- **Move/resize**: handle and corner, snapping to the grid, guide lines
- **Right-click**: context menu on the tile (can be switched off)
- **Hover**: slight brightening, floating toolbar in the editor
- **Animations**: short transitions when reordering, skeleton placeholders when loading, gentle fade-in of new tiles
- **Dialogue transitions**: overlay fades in, focus moves to the first field
- **Preview**: data sources show a thumbnail of the response before the tile is saved

### Responsive design

- **Desktop**: full grid, editor as a fixed side panel, administration with sidebar
- **Tablet**: reduced number of columns, panels as overlay
- **Mobile**: own layout that is saved separately; navigation via dropdown, widgets stacked one below another
- **Touch**: long press picks up a tile, resizing via corners with finger input
- **Font sizes** remain readable on small screens; header collapses to an icon bar

### Accessibility

- **Keyboard**: dialogues, forms and menus reachable via `Tab`, `Esc` closes overlays
- **Focus indicator**: focused elements are clearly marked
- **Screen reader**: ARIA roles for dialogues, menus and status messages
- **Colour independence**: status additionally recognisable via symbol and text
- **Zoom**: browser zoom without cut-off controls
- **Limit**: pure drag and drop cannot be fully replaced by keyboard movement – for fine work the mouse remains necessary

### Performance

- **Query intervals** per widget, not permanent; slow integrations only slow their own tile
- **Server-side fetching**: requests run via the instance, keys stay there, CORS is not needed
- **Bundling and caching**: identical queries within the time window are combined
- **Skeleton views** prevent jumping layouts when reloading
- **Recommendation**: a few meaningful integration widgets instead of many status checks with short intervals; thin out charts with a large history

## See also

- [menu.md](menus.md) - Menu items by role
- [features.md](features.md) - Widgets and integrations
- [shortcuts.md](shortcuts.md) - Keyboard operation
- [api.md](api.md) - Interface and OIDC
