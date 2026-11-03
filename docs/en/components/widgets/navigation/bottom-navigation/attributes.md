# Bottom Navigation - Attributes

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `items` | array[] | - | array of nav objects (id, icon, label) |
| `activeItem` | string | - | active nav item |
| `onChange` | function | - | event on selection |

## Behaviour

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `circular` | boolean | `false` | round buttons? |

## Presentation
| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `color` | enum | `primary` | colour: `primary`, `secondary`, `neutral` |
| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `animate` | boolean | `true` | enable animations? |
| `animationDuration` | number | `300` | duration in ms |

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `responsive` | boolean | `true` | responsive layout? |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onSelect` | function | runs on selection |
| `onHover` | function | runs on hover |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | ARIA role: `navigation` |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
