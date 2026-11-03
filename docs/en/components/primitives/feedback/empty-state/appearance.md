# Empty State - Appearance

## Base layout

```
        ┌───────────────────────────────┐
        │                               │
        │            ▤                  │  icon 48 px, muted colour
        │   No tasks yet                │  one sentence, 15 px
        │  [ Create your first task ]   │  primary button
        │   Keyboard: Ctrl N            │  optional, muted
        │                               │
        └───────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **leer** | neutral icon, action in the primary colour |
| **kein-treffer** | search icon, the text names the search term |
| **fehler** | icon in the error colour, action "Try again" |

## Sizes

| Size | Icon | Text width | Minimum height |
|------|------|------------|----------------|
| `small` | 32 px | 320 px | 120 px |
| `medium` | 48 px | 420 px | 200 px |
| `large` | 72 px | 520 px | 320 px |

## Colours and states

| State | Appearance |
|-------|------------|
| `default` | icon and text muted, action in colour |
| `hover` | only the action reacts (tone) |
| `loading` | a skeleton instead of text and action |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `tone` | as for the [button](../../actions/button/) |
| `fade-in` | fades in when the list becomes empty |

## Responsive

- On narrow surfaces, icon, text and action stack; width at most 90 %.
- The text wraps in at most three lines.
