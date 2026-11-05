# Zoom In

## Description

Zoom In fades an element in while it scales from a scale factor below 1 to its
full size (1) – usually accompanied by a simultaneous fade in. The element
therefore visibly "comes onto the stage".

## Use

- pull modal dialogs and lightboxes up when opening
- galleries: pull a thumbnail up to the full view
- let new list items appear gently (add item)
- softly open context menus and popovers
- zoom a camera or photo preview in from a corner
- highlight success messages and badges by scaling up

## Duration

- Typical: 200–350ms
- Default value: 250ms
- With a spring curve (`cubic-bezier`) a slight overshoot is possible

## Difference from Scale In

- Zoom In: fading in with a starting scale below 1, as a rule combined with a
  fade in opacity
- Scale In: a pure growth of size (e.g. 0 % → 100 %) with no change of opacity
