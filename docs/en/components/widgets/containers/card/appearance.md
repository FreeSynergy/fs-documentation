# Card - Appearance

## Base layout
A card is a container element that presents content in a structured box with a
title, content and optional actions.

```
┌─────────────────────────────┐
│ 🏠 Title of the card        │
├─────────────────────────────┤
│                             │
│   Here is the content       │
│   of the card.              │
│   Multi-line text.          │
│                             │
├─────────────────────────────┤
│  [Btn 1]  [Btn 2]  ⋯       │
└─────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **default** | standard with a header |
| **flat** | without shadow |
| **outlined** | only an outline |
| **elevated** | strongly elevated with a shadow |
| **media** | with an image/thumbnail |

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 200px | in list items |
| medium | 300px | standard |
| large | 400px | featured |
| full | 100% | full width |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **default** | light | standard |
| **primary** | primary colour | primary |
| **secondary** | secondary colour | secondary |
| **danger** | red | dangerous |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `shadow` | shadow becomes stronger |
| `transform` | slight lifting |
| `border` | the border lights up |

## Responsive

```css
.card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  transform: translateY(-2px);
}
```
