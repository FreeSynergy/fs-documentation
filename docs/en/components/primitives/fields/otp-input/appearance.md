# OTP Input (one-time password) - Appearance

## Base layout

```
┌───┬───┬───┬───┬───┬───┐
│ 4 │ 2 │ 9 │   │   │   │   one box per character, active box with a ring
└───┴───┴───┴───┴───┴───┘
        Code expired?  [Send new · 24 s]
```

## Variants

| Variant | Appearance |
|---------|------------|
| **einzelboxen** | separate squares with a border |
| **block** | one field, characters with letter spacing |

## Sizes

| Size | Box | Gap |
|------|-----|-----|
| `small` | 32 px | 4 px |
| `medium` | 44 px | 6 px |
| `large` | 56 px | 8 px |

## Colours and states

| State | Appearance |
|-------|------------|
| `default` | neutral border, field empty |
| `active` | active box with a primary ring |
| `filled` | all boxes filled, the verify button becomes active |
| `loading` | verify button with a spinner, fields locked |
| `error` | border in the error colour, a short shake, then cleared |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `ring` | primary ring on the active box |
| `shake` | on a wrong code, see [shake](../../../../interactions/animations/feedback/shake/) |

## Responsive

- The box size shrinks down to 32 px; below that the component switches to `block`.
- The help text below the boxes wraps, the boxes stay on one line.
