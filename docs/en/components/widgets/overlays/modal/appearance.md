# Modal - Appearance

## Base layout
A modal is an overlay window with focus on content.

```
┌─────────────────────────────────────────┐
│ [✕] Title                               │
├─────────────────────────────────────────┤
│                                         │
│   Content                               │
│   ...                                   │
│                                         │
├─────────────────────────────────────────┤
│  [Cancel]          [Save]              │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Size | Description |
|---------|------|-------------|
| **Small** | 300px | forms, confirmations |
| **Medium** | 500px | editing dialogs |
| **Large** | 700px | complete views |
| **Fullscreen** | 100% | complete view |

## Sizes

| Size | Width | Height | Use |
|------------|-------|-------------|--------------------------|
| Small | 300px | automatic | confirmation, short text |
| Medium | 500px | automatic | standard |
| Large | 700px | automatic | forms, lists |
| Fullscreen | 100% | 100% | complex view |

The upper limit is 85 % of the viewport height; the content scrolls, the header and footer
stay in place.

## Colours and states

| State | Colour | Description |
|-----------|--------|-------------|
| **Overlay** | dark | darken the background |
| **Header** | light | title bar |
| **Content** | light | content |
| **Footer** | light | actions |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `shadow` | stronger shadow |
| `border` | the border lights up |

## Responsive

The overlay lies over the page, blocks the background scroll and keeps the focus inside the
dialog (Escape closes, Tab circles within). On a narrow surface the modal automatically
becomes the full surface, with tall content only the body scrolls.

```css
.modal        { position: fixed; inset: 0; display: grid; place-items: center; }
.modal-panel  { width: min(500px, 92vw); max-height: 85vh;
                display: grid; grid-template-rows: auto 1fr auto; }
.modal-body   { overflow: auto; }              /* only the content scrolls */
body.modal-open { overflow: hidden; }          /* the background is locked */

@media (max-width: 600px) {
  .modal-panel { width: 100%; height: 100%; max-height: none; border-radius: 0; }
}
```

## Close button

```
┌─────────────────────────────────────────┐
│ [✕] Title                               │
├─────────────────────────────────────────┤
│                                         │
│   Content                               │
│                                         │
└─────────────────────────────────────────┘
```
