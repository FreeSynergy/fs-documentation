# Date Picker - Appearance

## Base layout

```
┌───────────────────────────────┐
│  ‹  October 2026           ⌄  │
├───────────────────────────────┤
│  Mo Tu We Th Fr Sa Su         │
│   1  2  3  4  5  6  7         │
│  12 ● 14 ▪▪ 15 ▓ 16 ·         │
│  …                            │
├───────────────────────────────┤
│  14 October                   │
│  ● 10:00 Stand-up             │
│  ▪ 15:00 Review  · 2 days     │
│  + 3 more                     │
│  [+ Entry]                    │
├───────────────────────────────┤
│  Today · Tomorrow · Next week │
└───────────────────────────────┘

▓ selected   ● appointment   ▪ task   · one more entry
```

Without a data connection (`sources` empty) the grid markers and the day list are
dropped; the overlay then consists only of the month grid and the quick selection.

## Variants

| Variant | Appearance |
|---------|------------|
| **einzeln** | one day filled in colour |
| **bereich** | start and end filled, lightly tinted in between |
| **wiederkehrend** | calendar plus a rule line below it |

## Sizes

| Size | Day area | Overlay width | Day list |
|------|----------|---------------|----------|
| `small` | 28 px | 260 px | two rows, dots 4 px |
| `medium` | 36 px | 320 px | four rows, dots 6 px |
| `large` | 44 px | 400 px | six rows, dots 6 px |

## Colours and states

| State | Appearance |
|-------|------------|
| `default` | days neutral, weekend muted |
| `hover` | day area lightly tinted |
| `active` | day filled in the primary colour, light text |
| `outOfRange` | day greyed out, not selectable |
| `open` | overlay with a shadow, current month highlighted |
| `loading` | grid still usable, day list with skeleton rows |
| `error` | day list with an error row and retry, the markers of the window are missing |

Entry types keep their colour across all views; the assignment comes from
the record (`color`), otherwise from the type.

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `ring` | focus ring on the selected day, keyboard navigation |
| `fade-in` | the overlay fades in, month changes slide sideways |
| `tooltip` | shows the titles of the entries for a day marker (max. three) |
| `lift` | a dragged entry follows the pointer, the target day is tinted |

## Responsive

- Below 500 px width the overlay becomes a surface anchored to the bottom with a list view.
- Month changes by a swipe gesture.
- The day list is played out in full below the grid; the dots are dropped, the
  counter sits on the weekday.
- A long press on a day opens the quick entry for that day.

## Entries per day

| Element | Appearance |
|---------|------------|
| Day marker | one dot per entry, lined up horizontally, max. `entryLimit` |
| Counter marker | more entries than `entryLimit`: one dot with a number |
| Series marker | dot with a dashed border, signal for `recurrenceRule` |
| Done | dot muted, title struck through (`status = done`) |
| Multi-day | the marker continues across the affected days as one unbroken bar |
| Day list | title, time or `allDay`, type as a dot; the entries of the selected day |
| Quick entry | one row with title and time field below the list, only when `creatable` |
