# Kbd - Appearance

## Base layout

```
einzeln:        kombination:

┌─────┐         ┌──────┐   ┌───┐
│ Esc │         │ Ctrl │ + │ S │
└─────┘         └──────┘   └───┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **einzeln** | small key cap: 1 px border, 4 px rounding, subtle shadow below |
| **kombination** | key caps with a "+" in the secondary colour between them |

## Sizes

| Size | Height | Font |
|------|--------|------|
| `small` | 18 px | 11 px |
| `medium` | 22 px | 12 px |
| `large` | 26 px | 14 px |

## Colours and states

| State | Appearance |
|-------|------------|
| `default` | light surface, primary text, border in the divider colour |
| `active` | surface in the primary colour, text inverted, shadow reduced |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| – | none; kbd is display only |

## Responsive

- Kbd wraps with the text; combinations are not torn apart
  (`white-space: nowrap` per key cap).
