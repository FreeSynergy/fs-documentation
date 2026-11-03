# Text Input - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | string | - | value |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `type` | enum | `text` | `text`, `email`, `url`, `phone`, `password` (`email`/`url`/`phone` replace the former own components) |
| `placeholder` | string | `null` | placeholder text |
| `readOnly` | boolean | `false` | read-only mode? |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showLabel` | boolean | `true` | show the label? |
| `showIcon` | boolean | `false` | show an icon? |
| `prefix` | string | - | prefix |
| `suffix` | string | - | suffix |
| `countryCode` | string | `DE` | default country code (only `type="phone"`) |
| `showCountryCode` | boolean | `true` | show the country code (only `type="phone"`) |
| `icon` | string | `email` | icon name |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onKeyDown` | function | runs on a key press |
| `onSubmit` | function | runs on submit |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `textbox` |

## Validation attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `required` | boolean | `false` | required? |
| `error` | string | - | error message |
| `minLength` | number | - | minimum length |
| `maxLength` | number | - | maximum length |
| `pattern` | string | - | regex pattern |
| `isValidEmail` | function | - | own email validation (for `type="email"`) |
| `isValidURL` | function | - | own URL validation (for `type="url"`) |
| `isValidPhone` | function | - | own phone validation (for `type="phone"`) |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../basics/base.md)
