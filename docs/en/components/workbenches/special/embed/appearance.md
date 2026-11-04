# Embed - Appearance

## Base layout

```
┌──────────────────────────────────────────────┐
│  Title                          ⛶  ↗         │  header (optional)
├──────────────────────────────────────────────┤
│                                              │
│                                              │  embedded surface
│                                              │
└──────────────────────────────────────────────┘
```

The header is dropped with `showTitle = false`; the fullscreen and open-in-new symbols
only appear on hover or focus.

## Variants

| `source` | Appearance |
|----------|------------|
| **app** | like its own program window, without its own navigation bar |
| **widget** | compact surface, limited fill height, rarer border |
| **iframe** | foreign page without border, header only with `showTitle = true` |

## Sizes

| Size | Meaning |
|------|---------|
| `small` | row height 280 px, e.g. in lists |
| `medium` | 480 px height, standard in pages |
| `large` | fills the available height, for dashboards |

In addition, `ratio` determines the aspect ratio (`auto`, `16:9`, `4:3`, `1:1`).

## Colours and states

| State | Appearance |
|-------|------------|
| `default` | surface with a base colour, subtle 1 px border |
| `hover` | the header symbols become visible |
| `focus` | 2 px focus ring around the whole surface |
| `loading` | skeleton in the surface, the header stays operable |
| `error` | error notice in the surface, cause and a link outwards |
| `disabled` | surface dimmed, operation locked |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `reveal` | header tools only appear on hover or focus |
| `ring` | the focus ring marks the entire embedding |

## Responsive

- In a narrow window the surface goes full width, the header stays on one line.
- With `responsive = false` the surface keeps its fixed height and gets a scrollbar.
