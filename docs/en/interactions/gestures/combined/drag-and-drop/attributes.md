# Drag and Drop - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `draggable` | boolean | `false` | The element may be grabbed |
| `onDragStart` | function | - | Grabbing (long press/instant) detected |
| `onDrag` | function | - | Movement while dragging |
| `onDrop` | function | - | Released in a valid drop zone |
| `onDragEnd` | function | - | Dragging ended (valid or aborted) |

## Target Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `dropZones` | string[] | `[]` | Allowed drop zones (`self`, `list`, `trash`, …) |
| `onDragEnter` | function | - | The drag enters a zone |
| `onDragLeave` | function | - | The drag leaves a zone |
| `onDragOver` | function | - | Movement over a zone (position for insertion) |
| `dataTransfer` | object | - | Data of the drag ( MIME, payload ) |

## Grab Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `grabMethod` | string | `long-press` \| `instant` \| `handle` | How is it grabbed? |
| `longPressThreshold` | number | `300` | Hold time for grabbing in ms |
| `liftThreshold` | number | `10` | Movement in px until the drag counts as started |
| `dragAxis` | string | `x` \| `y` \| `xy` | Allowed pull direction |

## Feedback Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `dragImage` | node \| auto | `auto` | Preview while dragging |
| `ghostAtOrigin` | boolean | `true` | Dim placeholder at the start position? |
| `targetHighlight` | boolean | `true` | Highlight the drop zone? |
| `insertIndicator` | boolean | `true` | Insertion line between elements? |
| `hapticFeedback` | boolean | `true` | Vibration on grabbing/dropping? |
| `dropAnimation` | string | `settle` \| `fly` \| `none` | Stowing animation |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `alternativeAction` | function | - | Up/down buttons or cut/paste (WCAG 2.5.7) |
| `keyboardDrag` | boolean | `false` | Space to grab, arrows to drop? |
| `announceDrop` | boolean | `true` | Announce the drop to a screen reader |
