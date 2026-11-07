# Homer - Structure & UI/UX

## Overview

Homer renders a single, vertically structured page. At the top a narrow header area, below it a grid of columns; in each column are group headings with tiles. Changes to the structure are made exclusively in the configuration file.

## Window structure

### Standard view

```
┌──────────────────────────────────────────────────────────────────────┐
│  Logo  Title · Subtitle                       [Icon link] [Icon link] │
├──────────────────────────────────────────────────────────────────────┤
│                 [ Search field ]                                     │
├──────────────────┬──────────────────┬────────────────────────────────┤
│  Group: Media    │  Group: Network  │  Group: Tools                  │
│  ┌────┐ ┌────┐   │  ┌────┐ ┌────┐   │  ┌────┐ ┌────┐                │
│  │Icon│ │Icon│   │  │Icon│ │Icon│   │  │Icon│ │Icon│                │
│  │Name│ │Name│   │  │Name│ │Name│   │  │Name│ │Name│                │
│  └────┘ └────┘   │  └────┘ └────┘   │  └────┘ └────┘                │
│  ┌────┐ ┌────┐   │  ┌────┐          │                               │
│  │Icon│ │Icon│   │  │Icon│          │  (order follows the file)     │
│  └────┘ └────┘   │  └────┘          │                               │
├──────────────────┴──────────────────┴────────────────────────────────┤
│  Footer                                                              │
└──────────────────────────────────────────────────────────────────────┘
```

### Filtered view (search text active)

```
┌──────────────────────────────────────────────────────────────────────┐
│  Header                                        [Icon links]          │
├──────────────────────────────────────────────────────────────────────┤
│                 [ down ]   ← search text                             │
├──────────────────────────────────────────────────────────────────────┤
│  Group: Network                                                      │
│  ┌────────┐ ┌────────┐                                              │
│  │Down…   │ │Down…   │   ← only matching tiles remain visible       │
│  └────────┘ └────────┘                                              │
└──────────────────────────────────────────────────────────────────────┘
```

### Mobile view

```
┌────────────────────────┐
│ Logo Title             │
│ [Search field]         │
│ Group: Media           │
│ ┌──────┐ ┌──────┐      │
│ │Tile  │ │Tile  │      │
│ └──────┘ └──────┘      │
│ Group: Network         │
│ ┌──────┐               │
│ │Tile  │               │
│ └──────┘               │
└────────────────────────┘
```

## Areas

| Area | Position | Content |
|---------|----------|--------|
| Header | Top | Logo, title, subtitle, icon links on the right |
| Search field | Below the header | filter field, if `search` is active |
| Columns | Middle | `columns` columns with groups |
| Groups | In columns | heading, optional logo/symbol, tiles |
| Tile | In groups | icon, name, optionally tag |
| Footer | Bottom | free text |
| Message | Overlay/line | loading, error or offline notice |

## UI/UX

### Design principles

- **Legibility before density**: large symbols, short name, plenty of white space
- **Structure from the file**: no operating elements that could change the structure
- **One screen, no menu**: everything is visible, search replaces navigation
- **Predictability**: positions change only with window size or file change

### Colour scheme and themes

- **Light and dark** via the `theme` entry, automatic switch according to the system setting possible
- **Own stylesheet** (`stylesheet`) for colours, font, spacing
- **CSS variables** overridden without editing the bundled files
- **Tile colours** are not configurable per tile; accents come from the theme or own CSS rules

### Interactions

- **Click**: opens the link in the configured target frame
- **Hover**: slight highlighting, tooltip on the icon link
- **Typing in the search field**: filters immediately, without reloading
- **Right-click**: shows the browser menu, no own context menu
- **No drag & drop**: moving and enlarging tiles is not possible
- **No animations**: transitions are limited to hover effects

### Responsive design

- **Desktop**: multiple columns, tiles side by side
- **Tablet**: number of columns reduces, groups stack
- **Mobile**: single-column view, large touch targets
- **Column control**: specified via `columns`; an own mobile layout like Homarr's does not exist
- **Wide windows**: tiles scale along, the content stays centred

### Accessibility

- **Keyboard**: tiles are real links and reachable via `Tab`, `Enter` opens
- **Screen readers**: headings structure the groups, `aria` attributes for the search field (version-dependent)
- **Search field**: labelled; filtering changes the DOM, which assistive technologies communicate
- **Zoom**: browser zoom without cut-off; on small screens tiles remain legible
- **Limitation**: colour accents carry no information, so the page remains operable independently of colour

### Performance

- **No server**: the page consists of static files, response times arise from the web server and CDN
- **Configuration is loaded**: the YAML file is an additional request and is delivered without auth
- **Very small amount of data**: no charts, no permanent loops, no polling intervals
- **Recommendation**: cache config and icons (cache headers), keep large icon folders lean, optionally HTTP/2 or CDN

## See also

- [menu.md](menus.md) - Operating elements and operating roles
- [features.md](features.md) - Tiles, search, themes
- [api.md](api.md) - `config.yml` in detail
- [shortcuts.md](shortcuts.md) - Keyboard and browser keys
