# Homarr - Structure & UI/UX

## Overview

After signing in, Homarr shows exactly one area: the active board. Controls sit in a narrow header, content in a grid of tiles. Editing and settings dialogs overlay the board.

## Window structure

### Board view

```
┌──────────────────────────────────────────────────────────────────────┐
│  Header: board switcher | search bar | Edit | Account menu          │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   Grid with widget tiles                                             │
│   ┌───────────────┐ ┌───────────────┐ ┌──────────────────────────┐   │
│   │ App tile      │ │ Docker        │ │ Calendar / RSS           │   │
│   │ Icon + name   │ │ Container list│ │ Entries                  │   │
│   ├───────────────┤ ├───────────────┤ └──────────────────────────┘   │
│   │ Status        │ │ Chart         │ ┌──────────────────────────┐   │
│   │ URL indicator │ │ Traffic       │ │ JSON value / info        │   │
│   └───────────────┘ └───────────────┘ └──────────────────────────┘   │
│                                                                      │
├──────────────────────────────────────────────────────────────────────┤
│  Messages (toast, bottom) · Status line of the widgets               │
└──────────────────────────────────────────────────────────────────────┘
```

### Edit mode

```
┌──────────────────────────────────────────────────────────────────────┐
│  Header: edit active (highlighted) | Save/Close                      │
├───────────────┬──────────────────────────────────────────────────────┤
│  Palette      │  Grid with grip points                               │
│  widget       │  ┌─[⋮]────────[✎][✕]─┐                              │
│  selection,   │  │  Tile (resize      │                              │
│  search by    │  │  corner bottom     │                              │
│  name         │  │  right)            │                              │
│               │  └────────────────────┘                              │
│  Board options│                                                      │
└───────────────┴──────────────────────────────────────────────────────┘
```

### Settings dialog (overlay)

```
┌──────────────────────────────────────────┐
│  Dialog title                   [✕]      │
├──────────────────────────────────────────┤
│  Form (groups, tabs)                     │
│  Field · Field · Selection · Switch      │
├──────────────────────────────────────────┤
│           [Cancel]  [Save]               │
└──────────────────────────────────────────┘
```

## Areas

| Area | Position | Content |
|---------|----------|--------|
| Header | Top | Board switcher, search, edit, account menu |
| Grid | Middle | Widget tiles in columns/rows |
| Widget tile | In the grid | Title bar, icon, content, actions |
| Widget palette | Left (edit mode) | available tiles to drag in |
| Board settings | Overlay/side panel | grid, background, colours, shares |
| Instance settings | Separate view | users, invitations, integrations, certificates |
| Toast messages | Bottom | success, error, connection status |

## UI/UX

### Design principles

- **Content before chrome**: tiles dominate, controls stay small
- **Immediate feedback**: changes to the layout take effect immediately, errors appear as a message
- **One board per view**: no permanent side-by-side display of several dashboards
- **Reusable building blocks**: Mantine components for forms, dialogs, menus

### Colour scheme and themes

- **Light and dark** plus system setting, switchable per account
- **Accent colour** and opacity/blur for tiles adjustable
- **Background images** per board (upload or URL)
- **Contrast** remains high in both schemes; warning and success colours are fixed

### Interactions

- **Drag & drop**: pick up the tile at the grip zone, target area is highlighted, snapping to the grid
- **Resize**: drag at the bottom edge/corner, grid steps shown as preview
- **Right-click**: context menu on the tile (can be switched off)
- **Hover**: hovering shows the toolbar and a slight brightening
- **Animations**: short transitions when re-sorting, loading as skeleton/placeholder display
- **Autocomplete**: dropdown selection in integration and search fields

### Responsive design

- **Desktop**: full grid, all header elements, board and instance settings
- **Tablet**: reduced number of columns, menus as overlay
- **Mobile**: own, separately savable layout; navigation via dropdown and touch gestures
- **Font sizes** remain readable on small screens, tiles stack one below the other

### Accessibility

- **Keyboard**: dialogs, forms and menus reachable via Tab, `Esc` closes overlays
- **Screen readers**: Mantine sets ARIA roles for dialogs, menus and messages
- **Focus indicator**: focused elements are clearly marked
- **Colour independence**: status is additionally conveyed via symbol and text
- **Zoom**: browser zoom without cut-off controls

### Performance

- **Data retrieval**: widgets query integration endpoints at intervals, not permanently
- **Server-side relief**: requests to target services run via the Homarr server (CORS and keys stay there)
- **Caching**: cached values in the instance, loading state per tile
- **Sluggish integrations** do not slow the board: affected tiles show a loading or error state
- **Recommendation**: a few meaningful integration widgets instead of many status checks with short intervals

## See also

- [menu.md](menus.md) - Menu items by role
- [features.md](features.md) - Widgets and integrations
- [shortcuts.md](shortcuts.md) - Keyboard control
- [api.md](api.md) - Internal API and integration proxy
