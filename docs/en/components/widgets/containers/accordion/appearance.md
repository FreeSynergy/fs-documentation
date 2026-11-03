# Accordion - Appearance

## Base layout
An accordion is a stack of headers that can collapse and expand content.

```
┌─────────────────────────────────────────┐
│ ▶ Header 1                              │
├─────────────────────────────────────────┤
│   Content 1                             │
├─────────────────────────────────────────┤
│ ▶ Header 2                              │
├─────────────────────────────────────────┤
│   Content 2                             │
├─────────────────────────────────────────┤
│ ▶ Header 3                              │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **standard** | headers below each other, one open |
| **mehrere** | several contents visible at the same time |
| **einzel** | a single header without grouping |

## Sizes

| Size | Font size | Use |
|------|-----------|-----|
| small | 12px | inline |
| medium | 14px | standard |
| large | 16px | featured |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **active header** | primary colour | active header |
| **inactive header** | grey | inactive header |
| **content** | dark | content |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `color` | the colour changes |
| `background` | the background changes |
| `border-bottom` | an underline appears |

## Responsive

- The accordion stack is always full width; the header row grows with the text,
  the content area is at most as high as the viewport.
- On narrow screens the arrow symbol slips to the left and the title stays
  aligned left; the header row becomes at least 44 px high.
- When closing, the following headers move up without a jump, the scroll position of
  the clicked header is kept.

## Animations

| Effect | Description |
|--------|-------------|
| `expand` | the content opens up |
| `collapse` | the content closes |
| `fade-in` | the content fades in |
| `rotate` | the arrow turns by 90 degrees |
