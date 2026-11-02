# Drag and Drop

## Description

Drag and drop combines **grabbing, pulling, and dropping**: an element is
picked up (tap, long press, or instant drag), moved across the screen, and
released on a drop zone (drop target). iOS uses long-press-to-grab, desktop
more often instant dragging; on the web: the HTML5 drag & drop API and pointer
events with `setPointerCapture`.

## Usage

- Moving files/elements between areas (lists, folders, boards)
- Changing the order (reorder)
- Combining content (image into an editor, text into a field)
- Trash action: pulling an element onto the "delete" drop zone

## Grab Methods

| Method | Description |
|--------|-------------|
| **Instant Drag** | Dragging starts immediately (desktop, list grab handles) |
| **Long Press Drag** | Grabbing only after holding (touch standard, does not collide with scrolling) |
| **Double Tap & Hold** | Double tap + holding lifts the element (iOS accessibility) |

## Duration

- Grab delay (long press): 250–500ms
- Pulling: arbitrary
- Drop animation: 200–350ms

## Detection

| Method | Description |
|--------|-------------|
| **Drag Source** | The element reports grabbing, supplies data/representation |
| **Drop Target** | The zone signals readiness to accept (highlight) |
| **Ghost/Drag Image** | A preview follows the finger/pointer |

## Cancellation

| Route | Behaviour |
|-------|-----------|
| Back to the start position | Springs back, no change |
| Escape key | Aborts |
| Drop zone that does not accept | The element returns |

## Difference from Drag

- **Drag**: moving content/an element in itself (scroll, pan)
- **Drag and Drop**: moving **between** source and target with a data handover

## Accessibility

WCAG 2.5.7 (Dragging Movements): every drag action needs a single-pointer
alternative (select + cut/paste, up/down buttons).
