# Color Input - Appearance

## Base layout
A color input is a colour selection field with a colour picker.

```
┌─────────────────────────────────────────┐
│ Colour                                  │
├─────────────────────────────────────────┤
│  🎨 #3498db                             │
│                                         │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **palette** | colour popover with a grid of colour surfaces, no slider |
| **spectrum** | large colour area, below it hue and transparency sliders |
| **code** | single-line field with a colour swatch before the value |

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

```
┌─────────────────────────────────────────┐
│ 🎨 #3498db                              │
├─────────────────────────────────────────┤
│  [Colours]                              │
│  🟥 🟧 🟨 🟩 🟦 🟪 ⬜ ⬛                  │
└─────────────────────────────────────────┘
```

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `border` | the border lights up |
| `shadow` | shadow becomes stronger |

## Responsive
- The selection overlay is at least 280 px wide; on narrow screens it opens as a
  bottom-anchored surface instead of under the field.
- The colour area scales proportionally, the slider stays at least 44 px high.
- Below `small` the `code` variant is preferred; palette and spectrum stay reachable
  as a full-screen dialog.

## Colour spectrum

```
┌─────────────────────────────────────────┐
│      🎨                                 │
│    🌈 Rainbow                           │
│                                         │
└─────────────────────────────────────────┘
```
