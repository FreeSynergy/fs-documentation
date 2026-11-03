# Bottom Navigation - Appearance

## Base layout

Bottom navigation is a navigation at the bottom of the screen, typical for
mobile-first design.

## Variants

### Active Icon (the active item is highlighted)

```
┌─────────────────────────────────────────┐
│   🏠    📩   📅   👥   ⚙️              │
│   Home  Mail CalContactsSettings      │
└─────────────────────────────────────────┘
```

### Text Labels (with text)

```
┌─────────────────────────────────────────┐
│ Home │ Mail │ Cal │ Cont. │ Settings    │
└─────────────────────────────────────────┘
```

### Icon Only (icons only)

```
┌─────────────────────────────────────────┐
│ 🏠  📩  📅  👥  ⚙️                     │
└─────────────────────────────────────────┘
```

## Sizes

| Size | Height | Icon size | Use |
|------|--------|-----------|-----|
| Small | 48px | 20px | Few items |
| Medium | 56px | 24px | Standard |
| Large | 64px | 28px | Many items |

## Colours and states

| State | Colour | Description |
|-------|--------|-------------|
| **Active** | primary colour | active item |
| **Inactive** | grey | inactive items |
| **Hover** | lighter | hover state |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `color` | the colour changes |
| `scale` | enlargement |
| `shadow` | shadow |

## Responsive

- The bar is always full width and stays at the bottom edge; its content is spread
  evenly over the items.
- When there is not enough room for labels it falls back to `icon only` and the name
  appears as a short text only after the item is chosen.
- On large screens the application usually switches to [sidebar](../sidebar/) or
  [toolbar](../toolbar/); the bar is kept when the application stays mobile, otherwise
  it is dropped.

## Max 5 items

```
┌─────────────────────────────────────────┐
│   🏠    📩   📅   👥   ⚙️              │
└─────────────────────────────────────────┘
```

## Animations

| Effect | Description |
|--------|-------------|
| `fade-in` | the label fades in |
| `scale-in` | the active symbol grows |
| `slide-in` | the indicator travels to the active item |
