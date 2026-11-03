# Tags Input - Appearance

## Base layout
A tags input is a list of tags/labels.

```
┌─────────────────────────────────────────┐
│ Tags:                                   │
├─────────────────────────────────────────┤
│  [Java] [Python] [React]                │
│  + New tag                              │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **frei** | chips inside the field, then free input with an insert button |
| **vorschlag** | input with a suggestion list, new chips are blocked |
| **nur-lesbar** | chips without a close button, no input field |

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 200px | inline |
| medium | 300px | standard |
| large | 400px | featured |
| full | 100% | full width |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **tag** | primary colour | tag colour |
| **hover** | lighter | hover state |
| **disabled** | grey | deactivated |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `background` | the background changes |
| `shadow` | shadow becomes stronger |

## Responsive

- Chips wrap into the next line and the field grows in height; `full` fills the width
  of the container.
- On narrow screens the suggestion list becomes a bottom-anchored bar, the chips
  stay visible at the top.
- The close button is at least 24 px large; on touch devices a long press is enough
  to remove, so the chip does not vanish by accident.

## Chip shapes

| Shape | Description |
|-------|-------------|
| **simple** | text only |
| **with icon** | icon on the left inside the chip |
| **with remove** | `✕` on the right to remove |

## Auto-complete

```
┌─────────────────────────────────────────┐
│ Tags:                                   │
├─────────────────────────────────────────┤
│  [Java] [Pyth]                          │
│  Python                                 │
│  Python 3                               │
│  Pythonista                             │
│  +                                      │
└─────────────────────────────────────────┘
```
