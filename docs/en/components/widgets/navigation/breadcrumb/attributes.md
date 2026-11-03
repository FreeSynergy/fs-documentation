# Breadcrumb - Attribute

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `items` | array[] | - | array of breadcrumb objects (label, href, icon) |
| `separator` | string | `>` | Separator: `>`, `>`, `/`, `›`, `•` |
| `activeIndex` | number | - | current index (for highlighting) |
| `collapsed` | boolean | `false` | collapsed when space is tight? |

## Behaviour

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `onHomeClick` | function | - | runs when home is clicked |
| `truncate` | boolean | `false` | shorten when space is tight? |

## Presentation
| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `showIcons` | boolean | `false` | show icons? |
| `color` | string | `neutral` | Colour |

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `responsive` | boolean | responsive layout? |
| `truncateBreakpoint` | number | breakpoint for shortening |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onNavigate` | function | runs on navigation |
| `onTruncate` | function | runs when the path is shortened |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | ARIA role: `navigation` |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
