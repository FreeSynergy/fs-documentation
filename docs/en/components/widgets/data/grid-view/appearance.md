# Grid View - Appearance

## Base layout
A grid view is a card/grid display of elements.

```
┌──────────┬──────────┬──────────┐
│          │          │          │
│  Card 1  │  Card 2  │  Card 3  │
│          │          │          │
├──────────┼──────────┼──────────┤
│          │          │          │
│  Card 4  │  Card 5  │  Card 6  │
│          │          │          │
└──────────┴──────────┴──────────┘
```

## Variants
| Variant | Description |
|---------|-------------|
| **Fixed Grid** | fixed number of columns |
| **Responsive Grid** | adjustable columns |
| **Masonry Grid** | irregular cards |

| Columns | Description |
|---------|-------------|
| **1** | one column |
| **2** | two columns |
| **3** | three columns |
| **4** | four columns |

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 200px | small grids |
| medium | 300px | standard |
| large | 400px | large grids |
| full | 100% | full width |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **Card** | light | card background |
| **Hover** | lighter | hover state |
| **Active** | primary colour | active card |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `shadow` | the shadow becomes stronger |
| `transform` | slight lift |
| `border` | the border lights up |

## Responsive

- **Responsive Grid** calculates with a minimum card width: 3 columns from 900 px, 2 from
  600 px, 1 below that; **Fixed Grid** keeps the number of columns and scales the cards.
- **Masonry Grid** fills the shortest column; on narrow screens it becomes one column.
- New cards appear with `stagger`; when reordering by `drag` the neighbours move
  into the gap (`reorder`).
