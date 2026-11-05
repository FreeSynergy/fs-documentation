# draw.io - Structure & UI/UX

## Overview

draw.io builds the workspace like a desktop program: menu bar at the top, shape library on the left, formatting panel on the right, canvas with page tabs in the middle and at the bottom. All side panels are collapsible; the canvas always remains the largest area.

## Window structure

### Default view

```
┌──────────────────────────────────────────────────────────────────────┐
│  File  Edit  View  Arrange  Extras  Help            [File name]      │
├───────────────┬──────────────────────────────────────────┬───────────┤
│ Search field  │                                          │ Format    │
│ Shape library │        Canvas (1..n pages)               │ Panel     │
│ - General     │   [shapes, edges, orange alignment       │ - Style   │
│ - Arrows      │    lines]                                │ - Arrange │
│ - BPMN / UML  │                                          │ - Options │
│ - AWS / Azure │                                          │           │
├───────────────┴──────────────────────────────────────────┴───────────┤
│  [Page 1] [Page 2] +        Zoom slider          View 100 %          │
└──────────────────────────────────────────────────────────────────────┘
```

### Area table

| Area | Position | Content |
|------|----------|---------|
| Menu bar | top | File, Edit, View, Arrange, Extras, Help |
| Title field | top right | file name, storage location, status (saved/modified) |
| Shape library | left | shape search, library folders, "More shapes" |
| Canvas | centre | pages with grid, rulers (optional), layers |
| Format panel | right | style, arrangement, text, document options |
| Bottom sidebar | bottom | page tabs, new page, zoom slider |
| Dialogs | overlay | layers, outline, versions, Realtime Sync, page dialog |

### Format panel (tabs)

- **Style**: fill colour, line style, font family/size, edge rendering
- **Arrange**: position and size numerically, rotation, text alignment, data
- **Options**: grid, guide lines, background, auto-save (version-dependent)

### Dialog overlay (example: layers)

```
┌──────────────────────────────────────┐
│  Layers                        [✕]   │
├──────────────────────────────────────┤
│  Name         Visible  Lock          │
│  Background     eye     padlock      │
│  Objects        eye     padlock      │
├──────────────────────────────────────┤
│  [Add layer]                         │
└──────────────────────────────────────┘
```

- Further overlays: outline, versions, Realtime Sync, page dialog, style templates
- Dialogs are modal above the canvas; the canvas stays active in the background

## UI/UX

### Design principles

- **Utility first**: panels and menus over elegance, maximum density of functions
- **Everything nameable**: styles, shapes and XML stay transparent to users
- **No onboarding**: a tool for users who already know diagrams
- **Consistent concept**: context menus mirror the items in the menu bar

### Colour scheme and themes

- **Default**: light grey control surfaces, white pages, dark lines
- **Dark mode/theme system**: present, naming and scope version-dependent
- **Shape palette**: preset pastel colours (blue, green, yellow, red) with standard style defaults
- **Page background**: selectable per page (Extras > Pages)

### Typography

- **Interface**: compact system font for menus, panels and status line
- **Cell labels**: standard font in a selectable size, HTML-like formatting (bold, italic, line breaks)
- **Mathematics**: LaTeX rendering for cell labels can be enabled (Extras menu, version-dependent)
- **Font sizes** set numerically in the style panel, scaling via zoom

### Interactions

- **Connection points**: inlets/outlets appear blue when hovering over a shape
- **Guide lines**: orange lines show alignment and equal spacing
- **Selection**: dashed frame with squares at corners and edges
- **Dragging and docking**: edges follow shapes, containers swallow shapes when you drag them in
- **Format transfer**: copy/paste a style onto other shapes
- **Animations**: practically none — redraw happens immediately; only menus fade in softly

### Responsive behaviour

- **Desktop**: fully developed panels and menus
- **Tablet**: touch drawing and panning possible, panel controls denser
- **Smartphone**: the web app is usable, but intended for fine diagram work; no native mobile interface

## Accessibility

- **Keyboard**: menu items and cell operations via shortcuts (see [shortcuts.md](shortcuts.md))
- **Screen readers**: limited — diagrams are drawn surfaces, XML is only indirectly accessible
- **Zoom**: browser zoom and app zoom can be combined for a larger display
- **Contrast**: standard styles are high contrast; colours are freely adjustable

## Performance

- **Compressed files**: `.drawio` files are deflate-compressed internally (can be switched off for readable XML)
- **Page rendering**: large works are drawn page by page; "paginating" keeps the visible area small
- **Shape libraries**: loaded lazily; few active sets keep the interface fast
- **Realtime Sync**: transmits editing steps of the cloud file; very large pages may lag
- **Plugins**: use your own extensions sparingly, they run along in the UI thread
