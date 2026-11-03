# Text Input - Appearance

## Base layout

A text input is a single-line input field for text.

## Variants

### Standard

```
┌─────────────────────────────────────────┐
│ Name                                    │
├─────────────────────────────────────────┤
│  John Doe                               │
│                                         │
└─────────────────────────────────────────┘
```

### Floating label

```
┌─────────────────────────────────────────┐
│  Name                                   │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│  John Doe                               │
└─────────────────────────────────────────┘
```

### Underline

```
┌─────────────────────────────────────────┐
│ Name                                    │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━     │
│ John Doe                                │
└─────────────────────────────────────────┘
```

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

- In forms, the fields stand full width below their label on narrow screens; two-column
  grids fall back to one column.
- On touch devices the height is at least 44 px; the text stays aligned left and scrolls
  inside the field, the font size does not grow beyond 16 px (no zoom on mobile).
- The active field is kept visible above the keyboard, the error line slips below it
  without covering the next field.

## Validation states

| State | Description |
|-------|-------------|
| **valid** | green |
| **invalid** | red |
| **warning** | orange |

## Placeholder

```
┌─────────────────────────────────────────┐
│ Name                                    │
├─────────────────────────────────────────┤
│  first name last name                   │
│                                         │
└─────────────────────────────────────────┘
```
