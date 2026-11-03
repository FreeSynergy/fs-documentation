# Range Calendar - Appearance

## Base layout

```
┌──────────────────────────┬──────────────────────────┐
│  ‹  October 2026         │  November 2026        ›  │
│  Mo Tu We Th Fr Sa Su    │  Mo Tu We Th Fr Sa Su    │
│      1  2  3  4          │              1  2        │
│  5 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     │       ▓▓▓ 7              │
├──────────────────────────┴──────────────────────────┤
│  14 days   ·   Today · 7 days · 30 days · Quarter   │
└─────────────────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **zwei-monate** | two grids next to each other, a divider between them |
| **ein-monat** | one grid, month change slides sideways |

## Sizes

| Size | Day area | Width |
|------|----------|-------|
| `small` | 28 px | 520 px |
| `medium` | 36 px | 660 px |
| `large` | 44 px | 800 px |

## Colours and states

| State | Appearance |
|-------|------------|
| `default` | days neutral |
| `selecting` | the range from the start to the pointer lightly tinted |
| `active` | start and end filled, middle light |
| `outOfRange` | days outside `min`/`max` greyed out |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `bridge` | one connected surface across both months |
| `ring` | focus ring on the start and the end |

## Responsive

- Below 700 px width switch to `ein-monat`.
- Month change by a swipe gesture, without buttons.
