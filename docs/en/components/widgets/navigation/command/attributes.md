# Command - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `commands` | array[] | - | commands with title, group, shortcut and target |
| `query` | string | `""` | entered search text |
| `open` | boolean | `false` | the palette is visible |

## Behaviour

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `hotkey` | string | `ctrl+k` | keyboard shortcut for opening |
| `grouped` | boolean | `true` | show hits grouped |
| `maxResults` | number | `50` | upper limit of hits |
| `recentCount` | number | `5` | recently used commands without input |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onQuery` | function | search text changed |
| `onSelect` | function | command executed |
| `onOpen` | function | palette opened |
| `onClose` | function | palette closed |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | `dialog` |
| `aria-activedescendant` | string | id of the marked hit |
| `label` | string | required, e.g. "Search commands" |

## Inherited from

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Base component](../../../primitives/basics/base.md)
