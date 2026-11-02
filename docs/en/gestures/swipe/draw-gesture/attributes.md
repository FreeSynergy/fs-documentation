# Draw Gesture - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onDrawGesture` | function | - | Executed after a recognized shape |
| `onDrawStart` | function | - | Drawing started |
| `onDrawProgress` | function | - | Current path while drawing |
| `onDrawUnknown` | function | - | No template recognized |

## Recognition Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `shapes` | string[] | `[]` | Allowed shapes/letters (`v`, `c`, `circle`, …) |
| `matchThreshold` | number | `0.8` | From which similarity (0–1) does a shape count as recognized? |
| `sampleRate` | number | `60` | Points per second while recording |
| `strokeWidth` | number | `3` | Drawing stroke in px (visual only) |
| `caseInsensitive` | boolean | `true` | Ignore upper/lower case for letters? |

## Context Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `activationArea` | string | `fullscreen` \| `overlay` | Where drawing can be triggered |
| `confirmation` | boolean | `false` | Execute the action only after confirmation? |
| `showShapeHint` | boolean | `true` | Show the allowed shapes? |
| `maxStrokes` | number | `3` | Max. strokes per gesture |

## Feedback Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `trail` | boolean | `true` | Show the drawn path? |
| `recognizeLive` | boolean | `false` | Already recognize partially while drawing? |
| `hapticFeedback` | boolean | `true` | Vibration on recognition? |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `alternativeAction` | function | - | Mandatory: button/command instead of a shape (WCAG 2.5.1) |
| `alternativeLabel` | string | - | Description of the alternative |
