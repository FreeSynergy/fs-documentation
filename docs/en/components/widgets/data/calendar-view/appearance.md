# Calendar View - Appearance

## Base layout
A calendar view shows appointments in a calendar.

```
┌─────────────────────────────────────────┐
│ Mo │ Tu │ We │ Th │ Fr │ Sa │ Su       │
├─────────────────────────────────────────┤
│    │  1 │  2 │  3 │  4 │  5 │  6       │
│  7 │  8 │  9 │ 10 │ 11 │ 12 │ 13       │
│ 14 │ 15 │ 16 │ 17 │ 18 │ 19 │ 20       │
│ 21 │ 22 │ 23 │ 24 │ 25 │ 26 │ 27       │
│ 28 │ 29 │ 30 │ 31 │    │    │          │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Monthly View** | month view |
| **Weekly View** | week view |
| **Daily View** | day view |
| **Agenda View** | list view |

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 250px | small calendars |
| medium | 350px | standard |
| large | 500px | large calendars |
| full | 100% | full width |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **Today** | primary colour | today |
| **Selected** | dark | selected day |
| **Event** | green | has an appointment |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `background` | the background changes |
| `border` | the border lights up |

## Responsive

- Changing the month by `swipe` is a `slide-in` of the whole grid.
- Below `small` screen width the week view shows three days, the day view stays
  full width; the agenda variant replaces the grid entirely.
- The time axis of the day and week views is at least 44 px wide per hour;
  `pinch` changes the time scale, the content stays readable.
