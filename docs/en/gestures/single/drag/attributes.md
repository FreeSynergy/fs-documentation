# Drag - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onDragStart` | function | - | Executed on drag start |
| `onDragMove` | function | - | Executed on drag move |
| `onDragEnd` | function | - | Executed on drag end |

## Feedback Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `ghostElement` | boolean | `true` | Show ghost element? |
| `scaleElement` | boolean | `false` | Enlarge the element? |
| `showShadow` | boolean | `true` | Show shadow? |

## Threshold Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `dragThreshold` | number | `10` | Min. distance in px |
| `constrain` | boolean | `false` | Constrain? |

## Container Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `container` | string | `parent` | Container selector |
| `snap` | boolean | `false` | Snap to grid? |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `aria-label` | string | Descriptive text |
| `role` | string | ARIA role: `slider` |
