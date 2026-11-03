# Split View

| Field | Value |
|-------|-------|
| **Category** | `containers` |
| **Inherits from** | `base` |
| **Variants** | `Fixed Split`, `Resizable Split`, `Responsive` |
| **States** | `dragging`, `collapsed` |
| **Gestures** | `drag`, `tap` |
| **Animations** | `expand`, `collapse` |
| **Related** | `panel`, `accordion`, `drawer`, `tabs` |
| **Status** | documented |

## Description
A split view is a layout with two areas side by side.

## Purpose

- List + detail view
- Comparison views
- Sidebar + main content
- Previews

## Variants

| Variant | Description |
|---------|-------------|
| **Fixed Split** | fixed width |
| **Resizable Split** | width changed by dragging |
| **Responsive** | automatic adjustment |

!!! info "Classification"
    The building block usually called `resizable` in libraries is not a component
    of its own but the variant `Resizable Split` of this component (decision rule in
    [Base component](../../../primitives/basics/base.md): same data set, different behaviour while dragging).

## Features

- Resizable (changing the width)
- Draggable (moving)
- Responsive (automatic adjustment)
- Collapsible (collapse/expand)

## Distinction

- **Do not confuse with** [panel](../panel/): a panel is *one* container; the split view
  divides the surface into two related areas with a divider.
- **Do not confuse with** [drawer](../../overlays/drawer/): the drawer lies over the
  content; here both areas stay visible at the same time.
- **Do not confuse with** [tabs](../../navigation/tabs/): tabs switch the same area,
  the split view shows both areas at once (list and detail).
- **Do not confuse with** [accordion](../accordion/): stacked vertically and collapsible,
  not divided sideways.
- Collapsing one area is a state (`collapsed`), not a component of its own.

## Best Practices

- Clear order
- Responsive
- Accessibility
- Feedback

## Layout

```
┌─────────────────┬──────────────────────┐
│                 │                      │
│   Area 1        │     Area 2           │
│   (Sidebar)     │     (Main content)   │
│                 │                      │
└─────────────────┴──────────────────────┘
```

## See also

- [containers – overview](../index.md)
- [Base component](../../../primitives/basics/base.md)
