# Emoji Picker - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | string | - | value (emoji) |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `placeholder` | string | `null` | placeholder text |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showSearch` | boolean | `true` | show the search? |
| `showRecent` | boolean | `true` | show recent emojis? |
| `showCategories` | boolean | `true` | show the categories? |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onOpen` | function | runs when opening |
| `onClose` | function | runs when closing |
| `onSelect` | function | runs on selection |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `button` |

## Categories attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `categories` | array[] | - | array of categories |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
