# Separator - Appearance

## Base layout

```
horizontal:
──────────────────────────────

mit-beschriftung:
────────────  or  ────────────

vertical:
┌──────────┐ │ ┌──────────┐
│ Group A  │ │ │ Group B  │
└──────────┘ │ └──────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **horizontal** | 1 px line in a neutral divider colour |
| **vertical** | 1 px line, height = line height of the neighbours |
| **mit-beschriftung** | two line segments with text between them |
| **dekorativ** | same line, often stronger (2 px) and in the theme colour |
| **inset** | indented by the width of the list's icon column |

## Sizes

| Size | Line weight |
|------|-------------|
| `small` | 1 px |
| `medium` | 1 px |
| `large` | 2 px |

## Colours and states

| Part | Colour |
|------|--------|
| line (neutral) | divider colour, light grey in the light theme, darker in the dark one |
| caption | secondary text |
| dekorativ | theme accent possible |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| – | none; a separator is not operable |

## Responsive

- When bars wrap, a `vertical` separator becomes `horizontal`.
