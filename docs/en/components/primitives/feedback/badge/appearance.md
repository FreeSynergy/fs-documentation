# Badge - Appearance

## Base layout

```
┌────────┐   ┌────────┐   ●   ┌╌╌╌╌╌╌╌┐
│  open  │   │   12   │       │  open  │
└────────┘   └────────┘       └╌╌╌╌╌╌╌┘
   status      counter        dot      outline
```

On an element (a count over an icon):

```
        ┌───┐
        │ 3 │
   ┌────╨───┘
   │  ✉
   └────
```

## Variants

| Variant | Appearance |
|---------|------------|
| **status** | surface with the status colour, dark or light text depending on the colour |
| **counter** | rounded surface, digits, minimum height equal to the font size |
| **dot** | 8 px circle in the status colour |
| **outline** | 1 px border in the status colour, transparent background |

## Sizes

| Size | Height | Font |
|------|--------|------|
| `small` | 16 px | 10 px |
| `medium` | 20 px | 12 px |
| `large` | 24 px | 14 px |

The `dot` does not grow with them: it stays 8 px (small/medium) or 10 px (large).

## Colours and states

| Status | Colour |
|--------|--------|
| `neutral` | grey |
| `info` | primary colour |
| `success` | green |
| `warning` | orange |
| `error` | red |

Badges are display only: apart from a short show/hide animation when the value
changes, they have no hover or state changes.

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `tooltip` | optional short explanation of the status (see [tooltip](../../../widgets/overlays/tooltip/)) |
| – | its own hover is not intended |

## Responsive

- On narrow screens, a counter badge on a navigation item is replaced by a
  `dot` when the number is no longer readable.
