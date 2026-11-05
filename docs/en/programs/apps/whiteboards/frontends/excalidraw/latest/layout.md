# Excalidraw - Structure & UI/UX

## Overview

Excalidraw shows exactly one surface: an infinite canvas. Controls sit above it as a slim bar and collapsible panels. In the read-only view mode the entire editing interface disappears.

## Window structure

### Editing view

```
┌──────────────────────────────────────────────────────────────────────┐
│  Header: main menu | tools | undo/zoom | collaboration               │
├────────────┬──────────────────────────────────────────┬──────────────┤
│ Properties │                                          │ Library      │
│ (only when │        Infinite canvas                   │ (right,      │
│ selected)  │   [elements, cursors of participants]    │  collapsible)│
│ - Stroke   │                                          │ - own        │
│ - Fill     │                                          │   collections│
│ - Opacity  │                                          │ - public     │
│ - Text     │                                          │              │
├────────────┴──────────────────────────────────────────┴──────────────┤
│  Optional: help dialog, stats (elements, FPS), zoom indicator        │
└──────────────────────────────────────────────────────────────────────┘
```

### Panel areas

| Area | Position | Content |
|------|----------|---------|
| Header | top | main menu, tool palette, undo/redo, zoom, collaboration |
| Properties panel | left (only on selection) | colours, stroke, fill, text, layers |
| Library panel | right | shape collections, import/export |
| Canvas | centre | free canvas, infinitely large |
| Help/stats | overlays | shortcut overview, performance figures |

## UI/UX

### Design principles

- **Canvas first**: tools step back behind the drawing surface
- **Little choice**: nine basic tools instead of full menu trees
- **Direct manipulation**: everything changes by dragging, clicking and typing
- **Sketch aesthetics**: hand-drawn lines (Rough.js) take the pressure of judgement out of drafts

### Colour scheme and themes

- **Light**: white canvas, dark lines (`#1e1e1e` as the default stroke colour)
- **Dark**: dark canvas, adjusted element colours (switchable in the main menu)
- **Element palette**: muted default colours for stroke and fill, freely selectable in the panel
- **Fonts**: hand-drawn default font, plus a normal and a monospace font

### Interactions

- **Drawing**: pick a tool, drag on the canvas; selection frame with corner points
- **Shift**: angle-true drawing and proportional scaling
- **Alt+drag**: clone; **double-click**: edit text
- **Zooming**: scroll or use the bar; zoom follows the cursor
- **Cursors**: coloured names of participants move along smoothly
- **Animations**: short fade pulses when creating, gentle zoom transitions; no heavy animations

### Responsive behaviour

- **Desktop**: full panels and tool palette
- **Tablet/touch**: drawing gestures with pen or finger, pinch zoom, panels via icons
- **Smartphone**: compact bar, restricted panel use; drawing remains fully possible

### Read-only view mode

```
┌──────────────────────────────────────────────────────────────────────┐
│  Header: title | zoom | collaboration (view only)                    │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│        Canvas (elements fixed, moving and zooming allowed)           │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

- No tool palette, no properties panel, no library panel
- Participants still see the cursors of the others

### Mobile view (compact layout)

```
┌────────────────────────────────┐
│ Menu | selection | undo | share│
├────────────────────────────────┤
│                                │
│   Canvas (pen and              │
│   touch drawing)               │
│                                │
├────────────────────────────────┤
│ Tools (icon bar at the bottom) │
└────────────────────────────────┘
```

### Typography

- **Elements**: hand-drawn default font for all labels
- **Interface**: neutral system font for panels and menus
- **Sizes**: four font steps for text, switchable via panel or number keys

## Accessibility

- **Keyboard**: tool selection and most actions are reachable via shortcuts
- **Screen readers**: limited — content exists as drawn elements, not as semantic text
- **Contrast**: default colours are high contrast; element colours freely adjustable
- **Note**: for accessible alternatives use text export (SVG contains text elements)

## Performance

- **Canvas rendering**: only changed areas are redrawn; large scenes with thousands of elements stay fluid
- **Collaboration**: only element differences (with `version`) are transmitted, not the whole scene
- **Image sizes**: inserted images are stored compressed (in `files` of the scene)
- **Stats dialog**: shows element count and FPS for diagnosis
- **Self-hosted**: performance depends on the collaboration server; rooms without persistence are lighter
