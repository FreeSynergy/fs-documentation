# Draw Gesture (Drawing Gesture)

## Description

A draw gesture is **drawing a shape or a letter** on the screen. The detection
compares the drawn path with known templates (shape matching). Letter
shortcuts in Edge ("V" = back, "C" = menu) and letter gestures on Android
devices became well known.

It belongs to the **path-based gestures** in the sense of WCAG 2.5.1 and always
needs a single-finger alternative.

## Finger Count

Exactly 1 per stroke – further fingers create their own, separate paths.

## Usage

- Letter shortcuts (browser commands, quick access)
- Shape recognition: circle = selection, checkmark = done, X = delete
- Handwritten note → command (scribble-like)
- Pattern unlocking (connection dots, rarer gesture, similar principle)

## Examples

| Shape | Typical action |
|-------|----------------|
| V | Back |
| C / B | Menu / forward |
| Circle | Select element / zoom in |
| Checkmark | Confirm |
| X | Close / delete |

## Duration

- Drawing: 200–1500ms
- Recognition time: < 100ms after lifting off

## Detection

| Method | Description |
|--------|-------------|
| **Path Sampling** | Normalize and compare the points of the path |
| **Template Matching** | Similarity to stored templates ($1/$2-Un recognizer) |
| **Primitives** | Combine stroke, arc, circle as building blocks |

## Pointer Count

One path is one connected stroke: the gesture is tied to **one pointer**. If
several fingers touch down at once, several separate paths emerge – that is
two single draw gestures (or an unknown pattern), not multipoint of the same
gesture.

## Difference from Swipe

- **Swipe**: a directed distance, the direction decides
- **Draw Gesture**: a free shape, the geometry decides

## Difference from Scribble

- **Draw Gesture**: the shape is interpreted as a command
- **Scribble**: writing is interpreted as text (pen input)
