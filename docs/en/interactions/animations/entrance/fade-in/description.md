# Fade In

## Description

Fade In gradually blends an element in by raising its opacity from 0 to 1.
Position and size stay unchanged, so nothing else shifts in the layout.

## Use

- blend toasts and notifications in gently
- let modal overlays and dialogs appear softly when opening
- blend images in after loading instead of letting them "pop" in
- cross-fade tabs and panels when switching
- blend onboarding elements in with a stagger (combined with Stagger)
- tooltip and popover reveal without distracting movement

## Duration

- Typical: 150–400ms
- Micro feedback (hover, tooltip): 100–200ms
- Modal areas and overlays: 250–400ms

## Difference from Fade Out

- Fade In: opacity rises from 0 to 1 – the element appears and keeps its layout
  position
- Fade Out: opacity falls from 1 to 0 – the element disappears and gives up its
  space
