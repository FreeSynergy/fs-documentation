# Mention Input - Appearance

## Base layout
A mention input is a text field with user/contact mentions.

```
┌─────────────────────────────────────────┐
│ @John Doe @Jane Smith                   │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **feld** | single line, chosen people as chips with a close button |
| **inline** | normal text, mentioned names highlighted in colour |
| **mehrzeilig** | editor area, chips and text mix |

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 200px | inline |
| medium | 300px | standard |
| large | 400px | featured |
| full | 100% | full width |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **default** | light | standard |
| **mention** | primary colour | mentioned users |
| **active** | dark | active state |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `border` | the border lights up |
| `shadow` | shadow becomes stronger |

## Responsive

- The suggestion list follows the cursor position and flips upwards when there is no room below.
- On narrow screens the list becomes a bottom-anchored bar above the keyboard.
- Chips wrap into the next line; names that are too long are truncated with an ellipsis,
  the full name stays available as a tooltip.

## Auto-complete

```
┌─────────────────────────────────────────┐
│ @                                       │
├─────────────────────────────────────────┤
│  John Doe                               │
│  Jane Smith                             │
│  Bob Müller                             │
│  +                                      │
└─────────────────────────────────────────┘
```

## Selected users

```
┌─────────────────────────────────────────┐
│ @John Doe @Jane Smith (2 selected)      │
└─────────────────────────────────────────┘
```
