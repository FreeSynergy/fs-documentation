# Date Input - Appearance

## Base layout
A date input is a date selection field with a calendar.

```
┌─────────────────────────────────────────┐
│ Date                                    │
├─────────────────────────────────────────┤
│  📅 2024-01-15                          │
│                                         │
└─────────────────────────────────────────┘
```

## Variants

| Variant (`type`) | Appearance |
|------------------|------------|
| **date** | field with a calendar symbol, calendar overlay below it |
| **time** | field with a clock symbol, a grid of times instead of a calendar |
| **datetime** | two segments in one field, first calendar then time |

## Sizes

| Size | Height | Use |
|------|--------|-----|
| small | 32px | inline |
| medium | 48px | standard |
| large | 64px | featured |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **default** | light | standard |
| **primary** | primary colour | primary |
| **active** | dark | active state |
| **disabled** | grey | deactivated |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `border` | the border lights up |
| `shadow` | shadow becomes stronger |

## Responsive

- The calendar overlay is at least 280 px wide; on narrow screens it opens
  bottom-anchored as a full-screen dialog.
- Month changes via `swipe`, the transition is `slide-in`.
- The day areas stay at least 40 px high even in a narrow grid; below
  `small` screen width the field is set to `large`.

## Calendar overlay

```
┌─────────────────────────────────────────┐
│        January 2024                     │
│ Mo Tu We Th Fr Sa Su                    │
│          1  2  3  4  5  6  7            │
│  8  9 10 11 12 13 14 [15] 16 17         │
│ 18 19 20 21 22 23 24 25 26 27 28 29 30  │
│ 31                                       │
└─────────────────────────────────────────┘
```

## Range selection

```
┌─────────────────────────────────────────┐
│ From - To                               │
├─────────────────────────────────────────┤
│  [01/01/2024] ━━━━━━━━━━━ [15/01/2024] │
└─────────────────────────────────────────┘
```
