# Multi-Finger Long Press

## Description

A multi-finger long press is a **long press with two or more fingers**. It
combines the time logic of the long press with the multi-finger context of the
multi-finger tap, and functionally matches a right click with holding
(macOS: "hold secondary click").

Here too the number of fingers is a setting (`pointerCount`), not its own
gesture type.

## Usage

- Context menu with a delay (prevents accidental triggering)
- Marking the start of a selection, then extending it by swiping
- Starting multi-select mode (selecting several elements)
- Drag start for multiselect (hold all fingers, then pull)

## Duration

- Hold: at least `longPressThreshold` (typically 500ms)
- Then like Long Press: callback at the start, movement optional

## Detection

| Method | Description |
|--------|-------------|
| **Pointer Count + Time** | `pointerCount` pointers, no movement beyond the threshold |
| **Move Tolerance** | Movement < 10px still counts as a press |
| **Lift Rule** | One of the fingers lifts too early → aborted |

## Difference from Multi-Finger Tap

- **Multi-Finger Tap**: short, action immediately
- **Multi-Finger Long Press**: hold, action after a delay, then pulling possible

## Difference from Long Press

- **Long Press**: from one pointer up (default: one), primary context menu
- **Multi-Finger Long Press**: requires at least two pointers (`pointerCount`), secondary/multiselect context

## Accessibility

Like all multi-point gestures, only with a single-finger alternative
(WCAG 2.5.1): long press or a selection button.
