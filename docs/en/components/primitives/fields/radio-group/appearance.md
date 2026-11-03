# Radio Group - Appearance

## Base layout
A radio group is a group of radio buttons (single choice).

```
┌─────────────────────────────────────────┐
│ Option 1  (•)                           │
│ Option 2  ( )                           │
│ Option 3  ( )                           │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **einzeln** | circle with a dot, label to the right of it |
| **toggle** | row of buttons, the active option filled as a surface |
| **karte** | card with a radius, active border in the primary colour |

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 20px | inline |
| medium | 24px | standard |
| large | 28px | featured |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **selected** | primary colour | selected |
| **unselected** | grey | not selected |
| **disabled** | grey | deactivated |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `scale` | enlargement |
| `shadow` | shadow becomes stronger |
| `border` | the border lights up |

## Responsive

- Below `small` screen width the options go to one column and each row becomes at
  least 44 px high.
- The segmented variant stacks below each other in narrow space; the dividing lines
  are kept, so the group stays recognisable as belonging together.
- Card variants stack in one column, icon and description stay aligned left.

## With icons

```
┌─────────────────────────────────────────┐
│ (•) Option 1   [Icon]                   │
│ ( ) Option 2   [Icon]                   │
│ ( ) Option 3   [Icon]                   │
└─────────────────────────────────────────┘
```
