# Timeline - Appearance

## Base layout
A timeline is a chronological display of events.

```
┌─────────────────────────────────────────┐
│  📅 20 January 2024                     │
│  📝 First step                          │
├─────────────────────────────────────────┤
│  📅 21 January 2024                     │
│  ✅ Step completed                      │
├─────────────────────────────────────────┤
│  📅 22 January 2024                     │
│  📝 Second step                         │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **senkrecht** | line on the left, entries to the right of it |
| **waagerecht** | line on top, entries next to each other below it |
| **karten** | entry as a card attached to the line |
| **ereignisse** | node on the line, one line of text |

## Sizes

| Size | Font size | Use |
|------|-----------|-----|
| small | 12px | inline |
| medium | 14px | standard |
| large | 16px | featured |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **Event** | primary colour | event |
| **Date** | grey | date |
| **Completed** | green | completed |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `color` | the colour changes |
| `border-left` | the line lights up |

## Responsive

- **senkrecht** stays one column; the distance between line and text shrinks, the text
  does not break into two columns.
- **waagerecht** scrolls sideways (`swipe`); below `small` screen width the timeline
  switches to the vertical form automatically.
- New entries slide in afterwards with `stagger`, completed nodes draw their tick
  with `tick-draw`.
