# Hover - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onHoverStart` | function | - | Pointer enters the element |
| `onHoverMove` | function | - | Pointer moves over the element |
| `onHoverEnd` | function | - | Pointer leaves the element |

## Timing Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `enterDelay` | number | `300` | Delay until activation in ms |
| `exitDelay` | number | `100` | Delay until deactivation in ms |
| `hoverTimeout` | number | `0` | Auto-off after a time in ms (0 = never) |

## Feedback Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `hoverAnimation` | string | `lift` \| `highlight` \| `none` | Reaction of the element |
| `tooltip` | string \| node | - | Tooltip content |
| `liftElevation` | number | `4` | Shadow level when lifting |
| `showOnTouch` | boolean | `false` | Touch emulation: first tap shows the hover content? |

## Pointer Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `pointerTypes` | string[] | `mouse, pen` | Which pointer types trigger it? |
| `requirePrecise` | boolean | `true` | Accept only a precise pointer (mouse/trackpad/pen)? |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `focusEquivalent` | boolean | `true` | Shows the same content on keyboard focus? |
| `dismissible` | boolean | `true` | Closable with escape? |
| `hoverPersist` | boolean | `true` | Content stays visible long enough (WCAG 1.4.13)? |
