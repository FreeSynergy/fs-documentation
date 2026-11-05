# Collapse

## Description

Collapse step by step reduces the height (optionally the width) of an element
to 0, until the space it occupies in the layout disappears. The content is
clipped away in the process, not scaled.

## Use

- close an accordion entry
- hide extended form fields
- slide a sidebar or filter area back in
- close table groups and nested lists
- hideable info boxes ("show less")
- a navigation group in the sidebar

## Duration

- Typical: 200–350 ms
- Default value: 250 ms

## Difference from Expand

- Expand: opposite direction – the height grows from 0 to the natural content
  height
- Fade Out: only the opacity falls, the layout space stays and does not
  collapse
- Scale Out: the whole element is shrunk (the text scales along with it);
  Collapse only cuts the content off
