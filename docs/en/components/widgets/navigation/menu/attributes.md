# Menu - Attributes

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `items` | array[] | - | array of menu items |
| `activeItem` | string/number | - | active menu item |
| `onChange` | function | - | event on selection |
| `isOpen` | boolean | `false` | is it open? |
| `onToggle` | function | - | event on opening/closing |

## Behaviour

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `variant` | enum | `horizontal` | style: `horizontal`, `vertical` |
| `collapsible` | boolean | `false` | collapsible? |
| `closable` | boolean | `false` | closable? |
| `closeOnOutsideClick` | boolean | `true` | close on a click outside? |
| `keyboardNavigation` | boolean | `true` | Keyboard-Navigation? |
| `animate` | boolean | `true` | enable animations? |
| `animationDuration` | number | `300` | duration in ms |

## Presentation
| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `showIcons` | boolean | `false` | show icons? |
| `showLabels` | boolean | `true` | show labels? |
| `color` | enum | `default` | colour: `default`, `light`, `primary` |

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `responsive` | boolean | responsive layout? |
| `hamburgerBreakpoint` | number | breakpoint for the hamburger |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onSelect` | function | runs on selection |
| `onOpen` | function | runs when opened |
| `onClose` | function | runs when closed |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | ARIA role: `menubar` |
| `aria-expanded` | boolean | is it expanded? |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
