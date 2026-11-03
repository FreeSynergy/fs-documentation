# Checkbox - Appearance

## Base layout
A checkbox is a yes/no or multiple-choice field.

```
┌─────────────────────────────────────────┐
│ [✓] Option 1                            │
│ [ ] Option 2                            │
│ [✓] Option 3                            │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Default** | standard square |
| **Toggle** | switch style |
| **Indeterminate** | partly selected |

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 20px | inline |
| medium | 24px | standard |
| large | 28px | featured |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **checked** | primary colour | selected |
| **unchecked** | grey | not selected |
| **disabled** | grey | deactivated |
| **hover** | lighter | hover state |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `scale` | enlargement |
| `shadow` | shadow becomes stronger |

## Responsive

- At narrow widths the label slips under the box; the hit area stays at least 44 px high.
- Option groups are stacked in one column, the indent of sub-items is kept.
- On touch devices the box scales up to `large` (28 px), the label keeps the font size of `medium`.

## With icons

```
┌─────────────────────────────────────────┐
│ [✓] Option 1   [Icon]                   │
│ [ ] Option 2   [Icon]                   │
│ [✓] Option 3   [Icon]                   │
└─────────────────────────────────────────┘
```
