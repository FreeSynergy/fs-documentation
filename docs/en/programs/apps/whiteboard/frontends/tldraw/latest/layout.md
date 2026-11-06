# tldraw - Structure and UI/UX

## Window structure

```
┌────────────────────────────────────────────────────────────────┐
│ tldraw ▾            Page 1 ▾                     Share  👥     │
│                                                                │
│                         (infinite canvas)            ┌──────┐  │
│        ▱ ──▶  ○                                    │Style │  │
│      ┌─Note──┐        ↗                             │Color │  │
│      │ Idea! │      Frame                           │ Fill │  │
│      └───────┘                                     │Size  │  │
│                                                    └──────┘  │
│   ┌──────────────────────────────────────────┐               │
│   │ ↖ ✋ ⌁ ✏ ⌫ ↗ ▭ ◯ ╲ △ ☁ 🗒 T 🖼 ⬒ | ℹ︎ ♟  │   (Tools)    │
│   └──────────────────────────────────────────┘               │
│ Minimap ◢                                          Zoom 100%  │
└────────────────────────────────────────────────────────────────┘
```

## UI/UX

- Radial/bottom toolbar, floating panels; canvas without fixed borders (infinite canvas)
- Minimalist, high keyboard affinity; context menu instead of an overloaded menu bar
- Dark/light mode via preferences

## Interactions

- **Pan/zoom**: hand tool, `Space`+drag, `Ctrl+wheel` to zoom; zoom buttons bottom right
- **Drag & drop**: move shapes, drag images/bookmarks from files/URLs
- **Resize and rotation handles** on the selection; snapping to edges/frames
- **Animations**: the selection outline "wobbles" minimally (hand-drawn style), panels fade; otherwise deliberately few animations
- **Multiplayer cursors**: coloured names of the other participants

## Responsive design

| Context | Behaviour |
|---------|-----------|
| Desktop | all panels |
| Tablet | compact toolbar, stylus support (pressure) |
| Mobile | panels overflow-safe, two-finger pan/zoom |

## Accessibility

- Keyboard control of the tools is central (shortcuts instead of chains of mouse clicks, see [shortcuts.md](shortcuts.md))
- Shapes are exposed as DOM/SVG elements with labels; screen reader support in the SDK can be extended
- Alternative text for images is possible (bookmark/alt field)

## Editor structure (SDK)

- The `<Tldraw/>` component with configurable parts (`Toolbar`, `StylePanel`, `MainMenu` replaceable)
- Store with records; the `Editor` API as the programming interface (see [api.md](api.md))
