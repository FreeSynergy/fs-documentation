# Card

| Field | Value |
|-------|-------|
| **Category** | `containers` |
| **Inherits from** | `base` |
| **Variants** | `standard`, `flach`, `umrandet`, `medien` |
| **States** | `selected` |
| **Gestures** | `tap`, `drag`, `long-press` |
| **Animations** | `lift`, `fade-in`, `stagger` |
| **Related** | `panel`, `grid-view`, `list-view`, `hover-card`, `dashboard` |
| **Status** | documented |

## Description
The card is a container element that presents content in a structured box with a
title, content and optional actions. It is often used in dashboards, lists and
grid layouts.

## Purpose

- Grouping information that belongs together
- Visual separation of content
- Showing mini overviews (e.g. customer, task, message)

## Variants

| Variant | Description |
|---------|-------------|
| **standard** | slight elevation, soft edge |
| **flach** | no shadow, only surface colour |
| **umrandet** | thin border, no shadow |
| **medien** | image or media area above or beside the content |

## Features

- A header with a title and at most two actions
- The media, content and footer areas are optional
- Selected and dragging state (in grids and dashboards)
- Collapsible for long cards

## Distinction

- **Do not confuse with** [panel](../panel/): the panel gathers controls or a
  work area, the card presents **one** content with a title and actions.
- **Do not confuse with** a row in [list-view](../../data/list-view/): the row is compact
  and uniform, the card freely composed.
- **Do not confuse with** [hover-card](../../overlays/hover-card/): the preview card is an overlay.
- **Do not confuse with** [grid-view](../../data/grid-view/): the grid arranges cards, it is
  not the card itself.

## Best Practices

- One card, one topic; at most three actions, one of them prominent.
- Keep the title short, use the subtitle for context, do not swap the two.
- Build cards in series to the same height; truncate texts that are too long rather
  than letting them wrap.
- Clickable cards need clear feedback and a keyboard alternative.

## Typical content

- Title/heading
- Text content
- Icons/emojis
- Buttons/actions
- Images/thumbnails
- Status badges

## See also

- [containers – overview](../index.md)
- [Panel](../panel/) — frame for controls
- [Grid View](../../data/grid-view/) — arranging cards
- [Base component](../../../primitives/basics/base.md)
