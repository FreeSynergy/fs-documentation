# Table of Contents - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `items` | array[] | - | array of item objects (title, href, children) |
| `activeItem` | string | - | current section |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `collapsible` | boolean | `false` | collapsible? |
| `interactive` | boolean | `false` | interactive? |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onHover` | function | runs on hover |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `navigation` |

## Item attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | string | unique ID |
| `title` | string | title |
| `href` | string | link |
| `children` | array[] | sub-items |

## Scroll attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `scrollSpy` | boolean | `false` | enable scroll spy? |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
