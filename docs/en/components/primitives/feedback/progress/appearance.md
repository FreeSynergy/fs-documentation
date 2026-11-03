# Progress - Appearance

## Base layout

```
linear:
┌───────────────────────────────┐
│ ████████████░░░░░░░░░░░░░░░░░ │  45 %
└───────────────────────────────┘

circular:
        ╭─────╮
       ╱  45% ╲
       ╲      ╱
        ╰─╮ ╭╯
          ╰─╯
```

## Variants

| Variant | Appearance |
|---------|------------|
| **linear** | bar in the primary colour, remainder a neutral track |
| **circular** | ring, progress clockwise starting at 12 o'clock |
| **mit-label** | percentage or text above the bar or inside the circle |
| **unbestimmt** | a segment travelling in the track, without a percentage |

## Sizes

| Size | Height linear | Diameter circular | Ring weight |
|------|---------------|-------------------|-------------|
| `small` | 4 px | 24 px | 2 px |
| `medium` | 8 px | 48 px | 4 px |
| `large` | 12 px | 96 px | 6 px |

## Colours and states

| State | Appearance |
|-------|------------|
| `default` | primary colour |
| `success` (100 %) | green |
| `error` (abort/error) | red |
| `indeterminate` | segment in the primary colour, track visible |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `tooltip` | optional details ("12 of 40 files") |
| – | its own hover/focus is not intended |

## Responsive

- `linear` follows the container width; `circular` scales with `size`
  or an explicit `strokeWidth`.
