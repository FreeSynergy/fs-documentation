# Select - Appearance

## Base layout
A field with the current value and a disclosure triangle; the options appear as a
list below it.

```
┌─────────────────────────────────────────┐
│ Country                                 │
├─────────────────────────────────────────┤
│  Germany ▼                              │
├─────────────────────────────────────────┤
│  Austria                                │
│  Switzerland                            │
│  France                                 │
│  Italy                                  │
│  +                                      │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **simple** | simple list |
| **multi-select** | multiple choice |
| **searchable** | with search |
| **custom** | customised |

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 150px | inline |
| medium | 250px | standard |
| large | 350px | featured |
| full | 100% | full width |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **default** | light | standard |
| **primary** | primary colour | primary |
| **active** | dark | active state |
| **disabled** | grey | deactivated |
| **hover** | lighter | hover state |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `background` | the background changes |
| `shadow` | shadow becomes stronger |

## Responsive

- The list is at most eight rows high and otherwise scrolls (`swipe`); if there is not
  enough room below, it opens upwards.
- On narrow screens the list opens full width and bottom-anchored, the rows stay
  at least 44 px high.
- With multiple choice the chips grow into the next line and the field increases its height;
  `full` sets it to the width of the container.
