# Force Press - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onForcePress` | function | - | Executed on Force Press |
| `onPeek` | function | - | Peek level reached |
| `onPop` | function | - | Open level reached |
| `onPressureChange` | function | - | Pressure value changes |

## Pressure Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `peekThreshold` | number | `0.5` | Peek begins at this pressure value (0–1) |
| `popThreshold` | number | `0.75` | The gesture opens at this pressure value |
| `fallbackLongPress` | boolean | `true` | Long press as a substitute without a pressure sensor? |
| `fallbackDelay` | number | `500` | Delay of the long-press fallback in ms |

## Preview Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `peekContent` | node \| url | - | Content of the preview card |
| `peekSize` | string | `small` \| `large` | Size of the preview |
| `peekDimming` | boolean | `true` | Dim the background behind the preview? |
| `quickActionItems` | array | `[]` | Context actions on the preview |

## Feedback Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `hapticFeedback` | boolean | `true` | Vibration when the level changes? |
| `pressAnimation` | boolean | `true` | Element sinks in while pressing? |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `alternativeAction` | function | - | Long press / menu item as an equivalent route |
| `requiresPressureHardware` | boolean | readonly | `true` when hardware is required |
| `aria-label` | string | - | Descriptive text |
