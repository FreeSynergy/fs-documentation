# Whiteboard

| Field | Value |
| ------ | ------ |
| **Category** | `special` |
| **Inherits from** | `base` |
| **Variants** | `zeichnung`, `formen`, `notizen`, `vorlage` |
| **States** | `gemeinsam`, `offline` |
| **Gestures** | `drag`, `tap`, `double-tap`, `pinch`, `spread` |
| **Animations** | `highlight`, `fade-in` |
| **Related** | `rich-text-editor`, `image`, `map-view`, `dashboard` |
| **Status** | documented |

## Description
A whiteboard is a drawing surface for collaboration.

## Purpose

- Brainstorming
- Planning
- Collaboration

## Variants

| Variant | Description |
| ---------- | -------------- |
| **zeichnung** | free drawing with pen and eraser |
| **formen** | rectangles, arrows and connectors, snapping |
| **notizen** | sticky notes as cards on the surface |
| **vorlage** | prepared surface (grid, columns, swimlanes) |

## Features

- Drawing
- Shapes
- Text
- Stencils
- Undo/Redo
- Export
- Collaboration

## Distinction

- **Do not confuse with** [rich-text-editor](../../fields/rich-text-editor/): there text is
  created, here a surface.
- **Do not confuse with** [map-view](../../../widgets/special/map-view/): the drawing surface has no geographic reference.
- **Do not confuse with** [gallery](../../../widgets/media/gallery/): a whiteboard produces content,
  a gallery shows existing content.

## Best Practices

- Surface without a hard boundary, the viewport is managed; an optional grid helps with
  alignment.
- Undo/redo belongs to the whiteboard — also after collaborative editing.
- When working together, the other people's pointers are visible and distinguishable by colour.
- Shapes snap and show alignment guides, otherwise nothing stays readable.
- Export as an image **and** as editable data, so work can continue later.

## See also

- [special – overview](../index.md)
- [Rich Text Editor](../../fields/rich-text-editor/) — text instead of a surface
- [Map View](../../../widgets/special/map-view/) — surface with a geographic reference
- [Base component](../../../primitives/basics/base.md)
