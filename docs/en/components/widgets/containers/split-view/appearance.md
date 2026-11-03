# Split View - Appearance

## Base layout
A split view is a layout with two areas side by side.

```
┌─────────────────┬──────────────────────┐
│                 │                      │
│   Area 1        │     Area 2           │
│   (Sidebar)     │     (Main content)   │
│                 │                      │
└─────────────────┴──────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Fixed Split** | fixed width |
| **Resizable Split** | width changed by dragging |
| **Responsive** | automatic adjustment |

## Sizes

| Area | Width | Use |
|------|-------|-----|
| **Sidebar** | 250px | standard |
| **Content** | auto | remaining space |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **Sidebar** | light | sidebar background |
| **Content** | light | content background |
| **Separator** | grey | divider line |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `resize-cursor` | resize cursor |
| `border` | the border lights up |

## Responsive

| Breakpoint | Behaviour |
|------------|-----------|
| Desktop (>768px) | side by side |
| Tablet (480-768px) | vertical stack |
| Mobile (<480px) | accordion |
