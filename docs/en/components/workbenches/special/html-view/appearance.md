# HTML View - Appearance

## Base layout

```
┌─────────────────────────────────────────┐
│ ⓘ Remote content blocked  [ Load ]      │
├─────────────────────────────────────────┤
│ Heading                                 │
│ Body text with a [link]                 │
│ ▢ (blocked image)                       │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---|---|
| **sanitised** | inert content, blocked images shown as placeholder |
| **remote-allowed** | same, with images loaded |

## Sizes

| Size | Height | Use |
|---|---|---|
| `medium` | auto | fits the content |
| `full` | 100% | reading pane |

## Colours and states

| State | Appearance |
|---|---|
| Default | adapted to the theme, mail colours limited ⚠️ |
| Blocked | placeholder outline |

## Hover and focus effects

| Effect | Description |
|---|---|
| `underline` | links underlined |
| `tooltip` | real link target |

## Responsive

- Content is scaled to the width; wide tables scroll horizontally.
- No fixed pixel widths are taken over from the source.
