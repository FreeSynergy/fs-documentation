# Rule Editor - Appearance

## Base layout

```
┌─────────────────────────────────────────────┐
│ [on]  If [Sender ▾] [contains ▾] [news@]    │
│       Then [Move to ▾] [Newsletter ▾]  [+][−]│
├─────────────────────────────────────────────┤
│ [+ Add rule]                                │
└─────────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---|---|
| **list** | bordered rows, drag handle at the left |
| **simple** | single row without handle |

## Sizes

| Size | Height | Use |
|---|---|---|
| `medium` | auto | standard |
| `full` | 100% | settings page |

## Colours and states

| State | Appearance |
|---|---|
| Enabled | normal text |
| Disabled | muted row |
| Invalid | error outline and message at the row |
| Unsaved | accent mark |

## Hover and focus effects

| Effect | Description |
|---|---|
| `background` | row highlight |
| `border` | handle becomes visible |

## Responsive

- Condition and action stack vertically on narrow screens.
- Reordering uses move up/down buttons when drag is not available.
