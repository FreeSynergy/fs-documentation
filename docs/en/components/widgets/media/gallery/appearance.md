# Gallery - Appearance

## Base layout

Galleries show images in different layouts: a grid, a carousel or a tile view.

## Variants

### Grid (`raster`)

```
┌──────────┬──────────┬──────────┐
│  🖼️    │  🖼️    │  🖼️    │
│ Image 1│ Image 2│ Image 3│
├──────────┼──────────┼──────────┤
│  🖼️    │  🖼️    │  🖼️    │
│ Image 4│ Image 5│ Image 6│
└──────────┴──────────┴──────────┘
```

### Masonry (irregular)

```
┌──────────┬──────────┐
│  🖼️    │  🖼️    │
│ Image 1│ Image 2│
│        │        │
│        │        │
├──────────┼──────────┤
│  🖼️    │  🖼️    │
│ Image 3│ Image 4│
│        │        │
│        │        │
│        └──────────┤
│        │  🖼️    │
│        │ Image 5│
└──────────┴──────────┘
```

### Row (`zeile`)

```
┌────────┬────────┬────────┬────────┐
│  🖼️  │  🖼️  │  🖼️  │  🖼️ ▶ │
└────────┴────────┴────────┴────────┘
```

The sequence of single images is handled by [carousel](../carousel/).

### Lightbox (large view)

```
┌─────────────────────────────────────┐
│ [✕]                                 │
│                                     │
│        🖼️                          │
│                                     │
│   [◀]          [▶]                  │
│                                     │
└─────────────────────────────────────┘
```

## Sizes

| Size | Width/height | Use |
|------|--------------|-----|
| Thumbnail | 100px | Lists, grids |
| Small | 200px | Cards, small galleries |
| Medium | 400px | Standard galleries |
| Large | 600px | Featured galleries |
| Full | 800px+ | Hero galleries |

## Colours and states

| State | Appearance |
|-------|------------|
| `default` | tile without border, the image fills the cell |
| `hover` | slight zoom, a semi-transparent bar with actions |
| `selected` | 2 px border in the primary colour |
| `geöffnet` | darken the background, image centred in the lightbox |
| `geladen` | placeholder (`skeleton`) until the image has arrived |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `zoom` | the image grows (1.1x) |
| `overlay` | overlay with information/icons |
| `border` | the border lights up |
| `scale` | the image scales slightly |

## Responsive

| Breakpoint | Behaviour |
|------------|-----------|
| Desktop (>768px) | full gallery with navigation |
| Tablet (480-768px) | 2 columns, compact |
| Mobile (<480px) | 1 column, carousel |

## Overlay styling

```
┌────────────────────────┐
│  🖼️                  │
│  overlay             │
│  [🔍] [ℹ️] [❤️]       │
└────────────────────────┘
```

## Navigation buttons

| Button | Icon | Function |
|--------|------|----------|
| Prev | ⏮️ | previous image |
| Next | ⏭️ | next image |
| Close | ✕ | close the gallery |
| Fullscreen | ⛶ | fullscreen |
| Share | 🔗 | share |
