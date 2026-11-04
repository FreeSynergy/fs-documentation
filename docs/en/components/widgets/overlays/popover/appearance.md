# Popover - Appearance

## Base layout

```
                     ┌──────────────────────┐
   ┌──────┐          │ ✎  Rename            │
   │  ⋯   │ ◀─────── │ ⎘  Duplicate         │
   └──────┘          │ 🗑  Delete            │
      trigger        └──────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **inhalt** | surface with text/image, same surface as `card` |
| **aktionen** | vertical action list with hover areas |
| **formular** | surface with fields and a confirm button |

## Sizes

| Size | Width |
|------|-------|
| `small` | up to 220 px |
| `medium` | up to 320 px |
| `large` | up to 480 px |

The height follows the content and becomes scrollable when it overflows.

## Colours and states

| Part | Colour |
|------|--------|
| surface | card colour plus shadow (one step higher than `card`) |
| `arrow` | same as the surface |
| actions | hover like menu items |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `fade-in` / `expand` | short fade-in coming from the trigger's direction |
| `focus-trap` | Tab circles inside the popover while it is open |

## Responsive

- On narrow screens the popover becomes a bottom drawer (full width, from below) —
  the same component, different presentation.

- It flips automatically when there is no space on the desired side.
