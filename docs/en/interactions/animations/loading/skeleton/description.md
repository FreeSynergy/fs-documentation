# Skeleton

## Description

Skeleton shows static placeholder shapes in the layout of the later content
while loading – bars, circles and blocks with a travelling shimmer. The user
recognises the coming structure before the data arrives, and no layout jump
arises when the real content takes its place.

## Use

- list views before the first data arrives, see [list-view](../../../../components/widgets/data/list-view/description.md)
- grid views while loading more, see [grid-view](../../../../components/widgets/data/grid-view/description.md)
- tables while the page is built, see [table](../../../../components/widgets/data/table/description.md)
- detail pages and cards that are filled asynchronously
- loading states: a replacement for the spinner when the layout of the content is
  known

## Duration

- Typical: 1200–1800 ms per shimmer cycle

## Difference from Progress and Glow

- Progress: shows a measurable value (e.g. 40 %); Skeleton makes no statement
  about how far the loading has progressed.
- Glow: a glow as a status signal (selection, live); Skeleton is a placeholder
  that disappears as soon as real content has arrived.
