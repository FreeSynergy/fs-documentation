# Cascade

## Description

Cascade takes over the timing of the child animations as [Stagger](../stagger/description.md)
does, but adds a direction and a variable step: the start travels across the
layout (from left to right, from top to bottom, from the outside inward), and the
distance between the starts can grow or shrink per element. The effect reads
like a wave running across a surface.

## Use

- cascade menu entries down from the bar
- let a photo grid appear diagonally from the upper left corner
- let long lists start accelerating (a shrinking distance)
- build dashboard cards up from the outside inward
- an exit as a running-out wave, so a surface empties "from right to left"
- wizard steps that build up one after another

## Duration

- Typical: 30–80 ms distance per element, total as with Stagger
- A growing step: start at 20 ms, +10 ms per element
- Direction-dependent: it is better to brake long lists (`stepLimit`), otherwise
  it feels sluggish

## Difference from Stagger

- Stagger uses a fixed offset per index; Cascade aligns the starts to the layout
  and is allowed to change the step.
- Stagger has no direction; Cascade needs a `richtung` (or derives it from the
  layout).
