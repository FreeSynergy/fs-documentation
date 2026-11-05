# Fade Out

## Description

Fade Out gradually blends an element out: its opacity falls from 1 to 0 until
the element is invisible. After that it can be removed from the layout or stay
permanently hidden.

## Use

- let toasts disappear automatically after their display time
- close modal overlays and dialogs softly
- fade out list elements after deleting them
- let a spinner disappear once an action is finished
- close menus and popovers on a click outside
- keep the invisible element until `display: none` takes effect

## Duration

- Typical: 150–300ms
- Fade-outs are usually chosen shorter than fade-ins
- Large overlays (background): up to 400ms possible

## Difference from Fade In

- Fade Out: opacity falls from 1 to 0 – the element leaves the stage
- Fade In: opacity rises from 0 to 1 – the element enters the stage
