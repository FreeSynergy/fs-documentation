# Date Input - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | string | - | value (date, time or both depending on `type`) |
| `type` | enum | `date` | `date`, `time`, `datetime` (`time`/`datetime` replace the former own components) |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `minDate` | string | - | minimum date |
| `maxDate` | string | - | maximum date |
| `placeholder` | string | `null` | placeholder text |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showIcon` | boolean | `true` | show an icon? |
| `icon` | string | `calendar` | icon name |
| `format` | string | `YYYY-MM-DD` | date format |
| `format24h` | boolean | `true` | 24-hour format (for `time`/`datetime`) |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onCalendarOpen` | function | runs when the calendar opens |
| `onOpen` | function | runs when it opens |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `textbox` |

## Validation attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `required` | boolean | `false` | required? |
| `error` | string | - | error message |

## Range attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `range` | boolean | `false` | select a date range? |
| `endDate` | string | - | end date |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../basics/base.md)
