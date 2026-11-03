# Breadcrumb - Appearance

## Base layout
Breadcrumbs show the path (Home > Wiki > Page > Sub-item).

```
┌─────────────────────────────────────────┐
│ Home > Wiki > Seite > Unterpunkt        │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Description |
| --------- | -------------- |
| **Default** | with arrow separator (>) |
| **Arrow** | with arrow (→) |
| **Slash** | with slash (/) |
| **Chevron** | with angle brackets (›) |

## Sizes

| Size | Font size | Use |
| ------- | ------------- | ------------ |
| Small | 12px | Inline |
| Medium | 14px | Standard |
| Large | 16px | Featured |

## Colours and states

| State | Colour | Description |
| -------- | ------- | -------------- |
| **Home** | Primary colour | start |
| **Active** | Dark | current path |
| **Inactive** | Grey | inactive paths |
| **Hover** | Lighter | hover state |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `color` | the colour changes |
| `underline` | an underline appears |
| `opacity` | the opacity changes |

## Responsive

- The last entry is shortened first, then the middle: the root and the current location
  always stay visible, with `…` appearing in between as an expandable menu.
- On narrow screens `zurueck` is often enough — one button showing the previous name.
- The path never wraps; it stays on one line and grows with the available width.

## With Icons

```
┌─────────────────────────────────────────┐
│ 🏠 Home > 📚 Wiki > 📄 Seite > 📝 Text │
└─────────────────────────────────────────┘
```

## Collapsed Breadcrumbs (in tight spaces)

```
┌─────────────────────────────────────────┐
│ Home > ... > Seite > Unterpunkt         │
└─────────────────────────────────────────┘
```
