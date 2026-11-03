# Description List - Appearance

## Base layout

```
Label                Value
──────────────────────────────
Name                 Anna Berger
Role                 Project planning
Due date             12 Nov 2026
Status               ● open
```

## Variants

| Variant | Appearance |
|---------|------------|
| **zweispaltig** | label 160 px, value fills the rest |
| **gestapelt** | label small and muted above the value |
| **inline** | `Name: Anna Berger · Role: Project planning` |

## Sizes

| Size | Row height | Label width |
|------|------------|-------------|
| `small` | 24 px | 120 px |
| `medium` | 32 px | 160 px |
| `large` | 40 px | 200 px |

## Colours and states

| State | Appearance |
|-------|------------|
| `default` | label muted, value in the base colour |
| `hover` | row lightly tinted, copy icon appears |
| `empty` | "no value" in the third colour level, or the row is hidden |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `reveal` | copy icon on the right of the row |
| `line` | subtle divider between rows, optional |

## Responsive

- Below 600 px width automatically `gestapelt`.
- `inline` wraps at the delimiters, never in the middle of a value.
