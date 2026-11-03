# Button - Appearance

## Base layout

```
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│    Save      │   │    Cancel    │   │   🗑 Delete   │
└──────────────┘   └──────────────┘   └──────────────┘
     primary            secondary           danger
```

With an icon:

```
┌──────────────────┐   ┌──────────┐
│   💾  Save       │   │    💾    │
└──────────────────┘   └──────────┘
  iconPosition="left"   icon-only
```

## Variants

| Variant | Appearance |
|---------|------------|
| **primary** | filled with the primary colour, light text |
| **secondary** | neutral surface, dark text |
| **outline** | 1 px border in the primary colour, transparent background |
| **ghost** | no border, background only on hover |
| **danger** | filled with the error colour |
| **link** | no border, text in the primary colour, underlined on hover |

## Sizes

| Size | Height | Padding (x) | Font |
|------|--------|-------------|------|
| `small` | 28 px | 10 px | 13 px |
| `medium` | 36 px | 14 px | 14 px |
| `large` | 44 px | 18 px | 16 px |

Icon-only buttons are square (height = width).

## Colours and states

| State | primary | outline | ghost |
|-------|---------|---------|-------|
| `default` | primary | primary border | transparent |
| `hover` | primary darkened | light primary tint | grey background |
| `active` | primary strongly darkened | primary tint | grey background |
| `focus` | 2 px focus ring outside | 2 px focus ring outside | 2 px focus ring outside |
| `disabled` | 40 % opacity, no pointer | same | same |
| `loading` | spinner instead of label, action locked | same | same |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `tone` | surface becomes one step darker |
| `shadow` | shadow lifts the button slightly |
| `ring` | focus ring for keyboard navigation, always visible |

## Responsive

- From `small` screen width, primary actions are set full-width below each other.
- Label wrapping is disabled; labels that are too long are truncated with an ellipsis.
