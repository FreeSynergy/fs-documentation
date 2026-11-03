# Panel - Appearance

## Base layout
A panel is a large container with a header, content and footer.

```
┌─────────────────────────────────────────┐
│ Header / title                          │
├─────────────────────────────────────────┤
│                                         │
│   Content                               │
│   ...                                   │
│                                         │
├─────────────────────────────────────────┤
│ Footer / actions                        │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **standard** | standard with a header |
| **einklappbar** | the header collapses and expands the content |
| **verschiebbar** | can be moved |
| **filter** | with filter options |

## Sizes

| Size | Height | Use |
|------|--------|-----|
| small | 200px | smaller panels |
| medium | 300px | standard |
| large | 400px | large panels |
| full | 100% | full width |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **default** | light | standard |
| **primary** | primary colour | primary |
| **secondary** | secondary colour | secondary |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `shadow` | shadow becomes stronger |
| `border` | the border lights up |

## Responsive

Panels follow the available space: side by side, below each other, or as an
overlay. On a narrow surface a side panel becomes a [drawer](../../overlays/drawer/),
while its content stays unchanged.

```css
.panel-grid { display: grid; grid-template-columns: 2fr 1fr; gap: 16px; }
.panel-body { overflow: auto; }              /* the content scrolls, header/footer stay */

@media (max-width: 900px) {
  .panel-grid { grid-template-columns: 1fr; } /* panels stack below each other */
}
```
