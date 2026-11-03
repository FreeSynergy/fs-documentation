# Calendar View - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `date` | string | - | current date |
| `events` | array[] | - | array of event objects |
| `onChange` | function | - | event on date change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `interactive` | boolean | `false` | interactive? |

## Events
| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | string | unique ID |
| `title` | string | title |
| `date` | string | date |
| `description` | string | description |

| Attribute | Type | Description |
|-----------|------|-------------|
| `onDateChange` | function | runs when the date changes |
| `onEventClick` | function | runs on clicking an event |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `grid` |

## Navigation attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showNavigation` | boolean | `true` | show navigation? |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
