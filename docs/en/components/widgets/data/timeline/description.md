# Timeline

| Field | Value |
|-------|-------|
| **Category** | `data` |
| **Inherits from** | `base` |
| **Variants** | `senkrecht`, `waagerecht`, `karten`, `ereignisse` |
| **States** | `aktiv`, `abgeschlossen` |
| **Gestures** | `tap`, `swipe` |
| **Animations** | `fade-in`, `stagger`, `tick-draw` |
| **Related** | `calendar-view`, `list-view`, `wizard`, `progress` |
| **Status** | documented |

## Description
A timeline is a chronological display of events.

## Purpose

- Showing a history
- Activities
- History
- Project phases

## Variants

| Variant | Description |
|---------|-------------|
| **senkrecht** | entries below each other, line on the left (standard) |
| **waagerecht** | entries next to each other, scrolls sideways |
| **karten** | each entry as a card on the line |
| **ereignisse** | compact: icon, point in time, one text |

## Features

- Date
- Title
- Description
- Icon
- Actions

## Distinction

- **Do not confuse with** [calendar-view](../calendar-view/): the calendar has a time scale
  and shows occupancy, the timeline shows order without a scale.
- **Do not confuse with** [wizard](../../containers/wizard/): the assistant guides through steps that are
  still open, the timeline looks back on what is past.
- **Do not confuse with** [progress](../../../primitives/feedback/progress/): a bar shows a share,
  the timeline shows the individual points.
- A [list-view](../list-view/) is timeless and can be reordered; the timeline stays chronological.

## Best Practices

- Newest entries first when it is about activity; for plans the other way round, and label it
  clearly.
- Show the relative time ("3 days ago") and keep the exact point in time available as a tooltip.
- Group by day or week, otherwise the line loses its structure.
- Icon for the type, colour for the status — mixing both is no longer readable.
- Load backwards (older entries) so the beginning is visible right away.

## Layout

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

## See also

- [data – overview](../index.md)
- [Calendar View](../calendar-view/) — occupancy on a time scale
- [Wizard](../../containers/wizard/) — guiding through open steps
- [Base component](../../../primitives/basics/base.md)
