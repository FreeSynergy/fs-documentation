# Message List - Appearance

## Base layout

```
┌─────────────────────────────────────────┐
│ ──────────── Yesterday ──────────────── │
│ ┌──────────────┐                        │
│ │ Hi!          │                        │
│ └──────────────┘                        │
│ ─────────── 2 unread ────────────────── │
│                        ┌──────────────┐ │
│                        │ Hello    ✓✓  │ │
│                        └──────────────┘ │
│ Anna is typing …                        │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---|---|
| **chat** | bubbles left/right by sender, bottom anchored |
| **thread** | narrow column, reply context shown on top |
| **mail** | one compact row per mail ⚠️ |

## Sizes

| Size | Height | Use |
|---|---|---|
| `small` | 200 px | embedded in another program |
| `medium` | 400 px | standard |
| `full` | 100% | messenger main area |

## Colours and states

| State | Appearance |
|---|---|
| Default | theme surface |
| Separator | muted line with centred label |
| Unread boundary | accent line |
| Empty | [empty-state](../../../primitives/feedback/empty-state/) |

## Hover and focus effects

| Effect | Description |
|---|---|
| `background` | row highlight (only if the row is selectable) |
| – | actions are shown by the bubble, gestures by the frontend |

## Responsive

- Bubbles use at most 80 % of the width on narrow screens.
- Older messages load behind a `skeleton` placeholder at the top.
