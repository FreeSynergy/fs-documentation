# Homepage - Structure & UI/UX

## Overview

Homepage renders a single page: header, information widgets, below them the service groups as a tile grid, and at the end the footer. There are no dialogs, no navigation between views and no sidebar. What looks like a layout editor is in reality a YAML entry.

## Window structure

### Standard page

```
┌──────────────────────────────────────────────────────────────────────┐
│  Header: greeting · date/time · search bar · bookmarks               │
├──────────────────────────────────────────────────────────────────────┤
│  Info widgets left          │        Info widgets right              │
│  ├ Weather (openweathermap) │  ├ Resources (CPU/RAM/disk)            │
│  ├ Search bar (provider)    │  ├ Stocks                              │
│  └ Kubernetes status        │  └ Glances / search                    │
├──────────────────────────────────────────────────────────────────────┤
│  Group "Media"                                                       │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                 │
│  │ Jellyfin     │ │ Sonarr       │ │ qBittorrent  │  ← tiles with   │
│  │ Icon · Name  │ │ 3 requests   │ │ ↑ 2.4 MB/s   │    service      │
│  │ Widget row   │ │ Widget row   │ │ Widget row   │    values       │
│  └──────────────┘ └──────────────┘ └──────────────┘                 │
│  Group "Network"                                                     │
│  ┌──────────────┐ ┌──────────────┐                                  │
│  │ UniFi        │ │ Pi-hole      │                                  │
│  └──────────────┘ └──────────────┘                                  │
├──────────────────────────────────────────────────────────────────────┤
│  Footer (footer)                                      Theme switch   │
└──────────────────────────────────────────────────────────────────────┘
```

### Mobile view

```
┌────────────────────────────┐
│  Header (compact)          │
│  Info widgets (stacked)    │
│  Group 1                   │
│  ┌────────────────────┐    │
│  │ Tile (full         │    │
│  │ width)             │    │
│  └────────────────────┘    │
│  Group 2 …                 │
└────────────────────────────┘
```

## Areas

| Area | Position | Content | Configuration |
|---------|----------|--------|---------------|
| Header | Top | title, date, search bar, bookmarks | `settings.yaml`, `bookmarks.yaml` |
| Info widgets | Top left/right | weather, resources, stocks, status | `widgets.yaml` |
| Service groups | Middle | tiles with links and service widgets | `services.yaml` |
| Tile | In the grid | icon, name, description, widget rows | `services.yaml` |
| Footer | Bottom | text, notice | `settings.yaml` |
| Theme area | Whole page | background image, hue, opacity | `settings.yaml`, `custom_css.css` |
| Log / protocol | Container log | YAML and connection errors | not visible in the UI |

## UI/UX

### Design principles

- **Overview before operation**: the page serves for reading, not for editing
- **Dense information**: small number rows instead of large charts
- **One grid, no levels**: no overlays, tabs or dialogs
- **Predictability**: position and size of the tiles are in the configuration, not in the browser

### Colour scheme and themes

- **Light, dark and system setting** via `theme` in `settings.yaml`
- **Accent colour** via `color` (Tailwind colour names), background via `background` or `image`
- **Opacity/blur** of the tiles via `opacity` and `style`
- **Custom CSS** (`custom_css.css`) for fine-tuning; classes on tiles via `class`
- **Background images** locally in the config folder or via URL; scaling and gradient via CSS

### Interactions

- **Click on tile**: opens `href` in the configured target (`launch: new_tab` or same tab)
- **Search bar**: enter text, `Enter` opens the results page of the provider; suggestions appear as a dropdown
- **Hover**: slight highlighting of the tile, for some widgets additional values
- **Refresh**: data is reloaded at intervals (SWR), no manual reload needed
- **Animations**: deliberately minimal — fade transitions when reloading, no re-sorting animations
- **Right-click / drag & drop**: not available

### Responsive design

- **Desktop**: multi-column grid, info widgets left and right
- **Tablet**: reduced number of columns, info widgets move one below the other
- **Mobile**: single-column stacking, compact header, full-width search bar
- **Layout entries** in `settings.yaml` apply only to a limited extent per device; on mobile the browser width dominates

### Accessibility

- **Keyboard**: links and search field reachable with `Tab`, `Enter` triggers
- **Screen readers**: tiles are simple link structures with text; widget numbers are output as text
- **Contrast**: themes with sufficient contrast; background images can reduce contrast — increase `opacity` if needed
- **Zoom**: browser zoom works without cut-off areas, because the page flows
- **Language**: interface translated (`language`), number formats follow the language

### Performance

- **Static rendering**: HTML arrives fully rendered from the server-side Next.js process
- **Proxy caching**: responses of the widget queries are briefly cached in the process (`memory-cache`), identical queries are bundled
- **Query intervals**: widgets query at minute intervals, not permanently; intervals that are too short burden the target services
- **Sluggish services** slow only their own tile: it shows a loading or error state
- **Recommendation**: remove service widgets that are not needed, limit Docker detection to the containers required

## See also

- [menu.md](menus.md) - areas and roles
- [features.md](features.md) - widgets and configuration
- [shortcuts.md](shortcuts.md) - keyboard control
- [api.md](api.md) - data sources and proxy routes
