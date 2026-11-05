# Reorder

## Description

Reorder lets list elements softly swap their places when their order changes –
after dragging, sorting or filtering. The old and the new position are measured,
then each element travels along the shortest way there (the FLIP principle:
First Last Invert Play). Other elements move along instead of jumping abruptly.

## Use

- drag and drop in lists, see [drag](../../../gestures/swipe/drag/description.md)
- sorting by date, name or priority
- setting a filter: filtered-out elements disappear, the rest move up
- placing tasks in a different column or group
- kanban and board views, see [list-view](../../../../components/widgets/data/index.md)
- rearranging attachments and images in a gallery

## Duration

- Typical: 250–400 ms
- Short distances (neighbours swapping): 200–250 ms
- Many elements at the same time: 300 ms and restrict the movement to the visible
  ones

## Difference from Stagger and Rubber Band

- Stagger only shifts the start times of an animation; Reorder animates the actual
  change of position of the elements.
- Rubber Band springs back at a boundary while dragging; Reorder only takes effect
  after release, once the new order is settled.
