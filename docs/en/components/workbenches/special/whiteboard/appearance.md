# Whiteboard - Appearance

## Base layout
A whiteboard is a drawing surface for collaboration.

```
┌─────────────────────────────────────────┐
│ [Pencil] [Eraser] [Shapes] [Text]       │  ← toolbar
├─────────────────────────────────────────┤
│                                         │
│      🖌️                                  │
│      whiteboard surface                 │
│                                         │
│      (drawing area)                     │
│                                         │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **zeichnung** | pen and eraser tools, free strokes |
| **formen** | tool box with figures and connectors |
| **notizen** | cards on the surface, coloured notes |
| **vorlage** | pre-drawn surfaces, columns and swimlanes |

## Sizes

| Size | Width/height | Use |
|------|--------------|-------------|
| Small | 400x300px | inline |
| Medium | 600x400px | standard |
| Large | 800x600px | featured |
| Full | 100% | full width |

## Colours and states

| State | Colour | Description |
|--------------|-------------|----------------------|
| **Background** | white/green | background |
| **Pencil** | black | pen |
| **Shapes** | coloured | shapes |
| **Text** | font | text |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `scale` | enlargement |
| `shadow` | stronger shadow |

## Responsive

- `Full` fills the viewport minus the toolbar; otherwise the surface grows with the content
  and the viewport scrolls.
- The toolbar stays reachable while scrolling; on narrow screens it moves to the bottom and
  the buttons stay at least 44 px large.
- `pinch`/`spread` change the scale, `drag` moves the surface; the line thickness stays the
  same, the strokes do not get thicker.

## Toolbar buttons

| Button | Function |
|--------|----------|
| **Pencil** | pen |
| **Eraser** | eraser |
| **Shapes** | shapes |
| **Text** | text |
| **Color** | colour |
| **Clear** | delete everything |
| **Export** | export |

## Grid background

```
┌─────────────────────────────────────────┐
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─               │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─               │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─               │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─               │
└─────────────────────────────────────────┘
```
