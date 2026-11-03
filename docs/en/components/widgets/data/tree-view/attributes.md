# Tree View - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `data` | array[] | - | array of node objects |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `simple` | style: `simple`, `with-icons`, `with-checkboxes`, `draggable` |
| `multiple` | boolean | `false` | multi-select? |
| `interactive` | boolean | `false` | interactive? |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showIcons` | boolean | `false` | show icons? |
| `showCheckboxes` | boolean | `false` | show checkboxes? |
| `indent` | number | `24` | indentation in px |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onExpand` | function | runs when expanding |
| `onCollapse` | function | runs when collapsing |
| `onSelect` | function | runs on selection |
| `onDragStart` | function | runs at the start of a drag |
| `onDragEnd` | function | runs at the end of a drag |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `tree` |

## Node attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | string | unique ID |
| `title` | string | title |
| `children` | array[] | child nodes |
| `icon` | string | icon name |
| `checked` | boolean | selected? |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
