# Heimdall - Structure & UI/UX

## Overview

The Heimdall interface is a vertically stacked page: a narrow header at the top, with the panels one below the other. The panels contain square tiles in one row or several rows. Editing and settings dialogs appear as an overlay.

## Window structure

### Start page

```
┌──────────────────────────────────────────────────────────────────────┐
│  Header: title/logo                        Account menu | Settings    │
├──────────────────────────────────────────────────────────────────────┤
│  Search area: search field | search engine                            │
├──────────────────────────────────────────────────────────────────────┤
│  App panel                                                             │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐              │
│  │ Icon   │ │ Icon   │ │ Icon   │ │ Icon   │ │ Icon   │              │
│  │ Title  │ │ Title  │ │ Title  │ │ Title  │ │ Title  │              │
│  │ Value  │ │ Value  │ │        │ │        │ │        │  (enhanced)  │
│  └────────┘ └────────┘ └────────┘ └────────┘ └────────┘              │
├──────────────────────────────────────────────────────────────────────┤
│  Statistics area: CPU │ RAM │ Disk │ Network  (figures + mini chart)  │
├──────────────────────────────────────────────────────────────────────┤
│  Notice/support area (optional) · Footer                              │
└──────────────────────────────────────────────────────────────────────┘
```

### Layout editing

```
┌──────────────────────────────────────────────────────────────────────┐
│  Mode notice: editing layout | Save | Discard                         │
├───────────────────────────┬──────────────────────────────────────────┤
│  Panel A (grip zone)      │  Panel B                                 │
│  [⋮] move, wrap           │  [⋮] hide, delete                        │
│  ┌────┐┌────┐             │  ┌────┐┌────┐                           │
│  │Tile││Tile│  drag       │  │Tile││Tile│                           │
│  └────┘└────┘             │  └────┘└────┘                           │
└───────────────────────────┴──────────────────────────────────────────┘
```

### Settings dialog

```
┌────────────────────────────────────────────┐
│  Edit app                          [✕]     │
├────────────────────────────────────────────┤
│  Title · URL · Icon · Colour               │
│  Enhanced app · Target URL · API key       │
│  [ ] open in new tab                       │
├────────────────────────────────────────────┤
│            [Cancel]  [Save]                │
└────────────────────────────────────────────┘
```

## Areas

| Area | Position | Content |
|---------|----------|--------|
| Header | Top | Title/logo, account menu, settings |
| Search area | Top, below header | Search field, provider selection |
| App panels | Middle | Tiles with icon, title, optionally live values |
| Statistics area | Middle/bottom | CPU, RAM, disk, network |
| Notice area | Bottom | Project notices, version notes |
| Footer | Bottom | Version number, project notice |
| Dialogs | Overlay | App editing, icon selection, account settings |

## UI/UX

### Design principles

- **Tile first**: large icons, short titles, little border
- **No nesting**: no embedded frames, every tile is a link
- **Vertical order instead of grid**: panels stack instead of being positioned freely
- **Few controls**: management appears mostly on hover or in the settings

### Colour scheme and themes

- **Default** is a dark base scheme with light tiles
- **Tile colours** freely selectable, allowing colour grouping
- **Custom CSS**: include own stylesheets; a theme catalogue is missing
- **Contrast** remains easy to read thanks to strong surfaces and white labels

### Interactions

- **Hover**: tiles brighten, editing icons appear
- **Drag & drop**: drag tiles within and between panels, reorder panels
- **Click**: opens the target URL; for enhanced apps additionally value details in the tile
- **Forms**: dialogs with conventional fields and save/cancel
- **Animations**: sparing, essentially transitions when sorting and showing/hiding

### Responsive design

- **Desktop**: several tiles per row, panels side by side after wrapping
- **Tablet**: fewer tiles per row, statistics fields stack
- **Mobile**: single-column view, large tiles, controls as touch targets
- **Layout per account**: mobile display follows the saved layout; there is no separate mobile view

### Accessibility

- **Keyboard**: links, forms and dialogs reachable via `Tab`, `Esc` closes dialogs
- **Screen readers**: semantic lists for panels, alt texts for icon images
- **Zoom**: page zoom without cut-off tiles
- **Limitation**: drag & drop cannot be operated alternatively via keyboard; reordering requires a mouse or touch

### Performance

- **Server-side**: PHP renders the page; statistics values and enhanced apps are queried when needed
- **Delay**: unreachable services lengthen page loading, since the queries run server-side
- **Caching**: browser caching for static files; application cache via Laravel mechanisms
- **Recommendation**: limit the number of enhanced apps, put the database volume on fast storage, increase PHP timeouts when there are many queries

## See also

- [menu.md](menus.md) - Menu items by role
- [features.md](features.md) - Apps, enhanced apps, panels
- [shortcuts.md](shortcuts.md) - Keyboard control
- [api.md](api.md) - Routes and key management
