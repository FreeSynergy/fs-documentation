# Number Input - Appearance

## Base layout
A number input is an input field for numbers.

```
┌─────────────────────────────────────────┐
│ Quantity                                │
├─────────────────────────────────────────┤
│  [ 123 ]                                │
│                                         │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **einfach** | number field without controls |
| **stepper** | small arrow keys stacked on the right of the field |
| **formatiert** | value aligned right, unit in grey behind the value |

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

- The step buttons are square and at least 32 px, 44 px on touch devices;
  at `small` screen width they are placed outside next to the field on the left.
- The value stays aligned right; long numbers are not truncated, the field grows with them.
- On touch devices the numeric keyboard appears, for `formatiert` without grouping characters.

## Step buttons

```
┌─────────────────────────────────────────┐
│ Quantity                                │
├─────────────────────────────────────────┤
│  [ 123 ]   [▲]                          │
│            [▼]                          │
└─────────────────────────────────────────┘
```

## Validation states

| State | Description |
|-------|-------------|
| **valid** | green |
| **invalid** | red |
| **warning** | orange |
