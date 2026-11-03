# Combobox - Appearance

## Base layout
A combobox is a text field plus a dropdown.

```
┌─────────────────────────────────────────┐
│ Country                                 │
├─────────────────────────────────────────┤
│  Germany ▼                              │
│                                         │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **einzeln** | field with an arrow, the suggestion list below it |
| **freitext** | like `einzeln`, but no forced choice; the cursor sits in the field |
| **mehrfach** | values already chosen as tags inside the field, the list stays up |

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

- The suggestion list is at most `medium` high (8 rows) and otherwise scrolls;
  `swipe` moves it on touch devices.
- If the list does not fit below the field, it opens upwards.
- On narrow screens the list renders full width over the field, the result rows
  stay at least 44 px high.

## Dropdown

```
┌─────────────────────────────────────────┐
│ Country                                 │
├─────────────────────────────────────────┤
│  Germany ▼                              │
├─────────────────────────────────────────┤
│  Austria                                │
│  Switzerland                            │
│  +                                      │
└─────────────────────────────────────────┘
```

## Auto-complete

```
┌─────────────────────────────────────────┐
│ Country                                 │
├─────────────────────────────────────────┤
│  Germ ▼                                 │
├─────────────────────────────────────────┤
│  Germany                                │
│  Germaneness                            │
│  +                                      │
└─────────────────────────────────────────┘
```
