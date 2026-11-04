# Toolbar - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `buttons` | array[] | - | array of button objects |
| `variant` | enum | `default` | style: `default`, `floating`, `sidebar` |
| `position` | enum | `top` | position: `top`, `bottom`, `left`, `right` |
| `tabs` | array[] | - | array of tab objects |
| `activeTab` | string | - | active tab |
| `onChange` | function | - | event on tab change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showLabels` | boolean | `true` | show labels? |
| `showIcons` | boolean | `true` | show icons? |
| `collapsed` | boolean | `false` | collapsed? |
| `autoHide` | boolean | `true` | hide automatically? |
| `target` | DOM element | - | target element |
| `offset` | object | - | { x, y } offset from the position |
| `groups` | array[] | - | array of group objects |
| `commands` | array[] | - | array of command objects |
| `minimized` | boolean | `false` | minimized? |
| `collapsible` | boolean | `true` | collapsible? |
| `size` | enum | `standard` | size: `compact`, `standard`, `large` |

## Events
| Attribute | Type | Description |
|-----------|------|-------------|
| `onButtonClick` | function | runs on a button click |
| `onExpand` | function | runs on expanding |
| `onCollapse` | function | runs on collapsing |
| `onVisibilityChange` | function | runs when the visibility changes |
| `onSelect` | function | runs on selection |
| `onMinimize` | function | runs on minimizing |

| Attribute | Type | Default | Description |
|---|---|---|---|
| `keyboardShortcuts` | boolean | `true` | enable keyboard shortcuts? |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `toolbar` |

## Button attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | string | unique ID |
| `icon` | string | icon name |
| `label` | string | button label |
| `variant` | enum | `primary`, `secondary`, `danger` |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
