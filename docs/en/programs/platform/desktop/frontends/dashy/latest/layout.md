# Dashy - Structure & UI/UX

## Overview

Dashy shows a header, below it the search bar, then the sections with tiles and optional widgets, and a footer at the end. Editing and settings areas overlay the view as a side panel or dialog. Three view forms (start page, minimal, workspace) change the same structure in density and scope.

## Window structure

### Standard view

```
┌──────────────────────────────────────────────────────────────────────┐
│  Header: title/subtitle   Page menu | Launchpad | Gear | Account     │
├──────────────────────────────────────────────────────────────────────┤
│                [ Search bar ]         (typing filters instantly)     │
├──────────────────────────────────────────────────────────────────────┤
│  Section: Media                           Section: Network           │
│  ┌─────────⊙──┐ ┌─────────⊙──┐          ┌─────────⊙──┐              │
│  │ Icon Title │ │ Icon Title │          │ Icon Title │   ⊙ = Status  │
│  │ Description│ │ Description│          │ Description│              │
│  └────────────┘ └────────────┘          └────────────┘              │
│  ┌────────────┐ ┌────────────┐          ┌────────────┐              │
│  │ Widget Clock│ │ Widget RSS│          │            │              │
│  └────────────┘ └────────────┘          └────────────┘              │
├──────────────────────────────────────────────────────────────────────┤
│  Footer                                                              │
└──────────────────────────────────────────────────────────────────────┘
```

### Edit mode

```
┌──────────────────────────────────────────────────────────────────────┐
│  Mode notice: editing active            Save | Discard | ✕           │
├──────────────────────────────────────────────────────────────────────┤
│  ┌─[⋮]──────────────[✎][🗑]─┐      ┌──────────────────────────────┐  │
│  │ Tile (drag to move        │      │ Section (grip zone)          │  │
│  │ within the grid)          │      │ Add tile                     │  │
│  └───────────────────────────┘      └──────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────┘
```

### Tile dialog

```
┌──────────────────────────────────────────┐
│  Edit tile                      [✕]      │
├──────────────────────────────────────────┤
│  Title · URL · Description · Icon        │
│  Opening mode · Colours · Tags · Hotkey  │
│  Status check · Display options          │
├──────────────────────────────────────────┤
│           [Cancel]  [Save]               │
└──────────────────────────────────────────┘
```

## Areas

| Area | Position | Content |
|---------|----------|--------|
| Header | Top | Title, logo, page menu, launchpad, settings, account |
| Search bar | Below the header | Filter field, web search, shortcut commands |
| Sections | Middle | Heading, tile grid, widgets |
| Tile | Within sections | Icon, title, description, status dot |
| Status dot | Top right of the tile | reachable / unreachable / checking / error |
| Widget area | Within sections or as a column | Clock, weather, RSS, custom widgets |
| Footer | Bottom | Notice, source attribution |
| Settings panel | Overlay/side panel | Interactive editor, theme, import/export |
| Login | Own view | Sign-in when authentication is configured |

## UI/UX

### Design principles

- **Act immediately**: typing starts the search, without a detour via a field
- **Information on the object**: status dot and description belong to the tile
- **Little chrome, many options**: standard view is plain, details via menus and configuration
- **One source**: what the file describes is the interface — no hidden state

### Colour scheme and themes

- **Built-in schemes** in a large selection, light and dark, plus theme editor
- **CSS variables** for custom colours, backgrounds and fonts
- **Per section and tile** custom colours and density possible
- **Automatic switch** between light and dark scheme according to the system setting, configurable

### Interactions

- **Hover**: tiles lift, description is emphasized
- **Right-click**: context menu with all opening modes
- **Drag & drop**: only in edit mode, tiles and sections in the grid
- **Keyboard**: typing, `Tab`, arrow keys, `Enter`, `Alt+Enter`, `Ctrl+Enter`, `Esc`
- **Animations**: smooth transitions when filtering and switching views; status dots change colour
- **Loading states**: status dots show "checking", widgets show placeholders

### Responsive design

- **Desktop**: multi-column sections, many tiles per row
- **Tablet**: fewer columns, widgets stack
- **Mobile**: single column, large touch targets, reduced header
- **Configurable number of columns** per section; the grid wraps automatically

### Accessibility

- **Keyboard operation**: search, navigation and launching fully possible without a mouse
- **Focus indicator**: focused tiles are clearly marked
- **Screen readers**: sections as headings, tiles as links with title and description
- **Colour independence**: status additionally recognizable via shape and text (theme-dependent)
- **Zoom**: page zoom without clipping

### Performance

- **Static at the core**: the application consists of static files, so delivery is fast
- **Server costs**: status checks and API calls run via the Node server and scale with the number of tiles
- **Config size**: the file is size-limited; very large collections belong distributed across subpages
- **Recommendation**: set check intervals moderately, remove unneeded widgets, use subpages for long lists

## See also

- [menu.md](menus.md) - Header, panels, context menus
- [features.md](features.md) - Tiles, status, widgets, themes
- [api.md](api.md) - REST API and authentication
- [shortcuts.md](shortcuts.md) - Keyboard control
