# Tabs - Attribute

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `tabs` | array[] | - | array of tab objects (id, label, content) |
| `activeTab` | string/number | - | active tab (id) |
| `onChange` | function | - | event on tab change |
| `position` | enum | `top` | position: `top`, `bottom`, `left`, `right` |

## Behaviour

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `closable` | boolean | `false` | are tabs closable? |
| `scrollable` | boolean | `false` | scrollable? |
| `collapsible` | boolean | `false` | collapsible? |

## Presentation
| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `showIcons` | boolean | `false` | show icons? |
| `showLabels` | boolean | `true` | show labels? |

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `responsive` | boolean | responsive layout? |
| `hideLabelsOnMobile` | boolean | hide labels on mobile? |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onSelect` | function | runs on selection |
| `onClose` | function | runs when closed |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | ARIA role: `tablist` |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
