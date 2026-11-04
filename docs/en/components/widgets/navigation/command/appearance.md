# Command - Appearance

## Base layout

```
        ┌────────────────────────────────────────┐
        │ 🔍  Create task…                       │
        ├────────────────────────────────────────┤
        │ Actions                                │
        │   Create task                   Ctrl N │
        │ Views                                  │
        │   Switch to calendar            Ctrl 3 │
        │ Programs                               │
        │   Open whiteboard               Ctrl W │
        └────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **palette** | overlay centred, 640 px wide, dark background behind it |
| **inline** | no background, width of the parent box |

## Sizes

| Size | Input height | Row height | Max. hits |
|------|--------------|------------|-----------|
| `small` | 32 px | 28 px | 6 |
| `medium` | 40 px | 34 px | 10 |
| `large` | 48 px | 40 px | 14 |

## Colours and states

| State | Appearance |
|-------|------------|
| `default` | input field light, hit list neutral |
| `open` | focus in the input field, first hit marked |
| `hover` | row background one step darker |
| `empty` | notice "No match" plus suggestions |
| `loading` | skeleton in the hit list |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `reveal` | shortcut on the right of the row, subtle |
| `ring` | marking of the active hit across the whole row |

## Responsive

- On narrow screens the palette fills the full width and height.
- The hit list scrolls; the input row stays pinned at the top.
