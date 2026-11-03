# Switch - Appearance

## Base layout

A switch is an on/off switch (toggle).

## Variants

### Standard (rectangle)

```
┌─────────────────────────────────────────┐
│ [   ON   ]                              │
│                                         │
└─────────────────────────────────────────┘
```

### Round

```
┌─────────────────────────────────────────┐
│ (   ON   )                              │
│                                         │
└─────────────────────────────────────────┘
```

### Pill

```
┌─────────────────────────────────────────┐
│  [ ON ]                                 │
│                                         │
└─────────────────────────────────────────┘
```

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 40px | inline |
| medium | 56px | standard |
| large | 72px | featured |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **off** | grey | off |
| **on** | primary colour | on |
| **disabled** | grey | deactivated |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `scale` | enlargement |
| `shadow` | shadow becomes stronger |
| `border` | the border lights up |

## Responsive

- The switch does not scale below `small` (40 px); the hit area around it stays 44 px.
- In lists and on narrow screens the switch sits aligned right on its own line,
  the label wraps above it on the left.
- On touch devices the handle may also be pushed (`drag`); releasing switches to the
  nearer position.

## Animations

| Effect | Description |
|--------|-------------|
| `slide-in` | the handle travels to the other side |
| `fade-in` | the surface colour changes smoothly |

## With labels

```
┌─────────────────────────────────────────┐
│ Enable feature             [   ON   ]   │
└─────────────────────────────────────────┘
```
