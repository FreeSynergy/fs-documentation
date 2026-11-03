# OTP Input (one-time password) - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `length` | number | `6` | number of characters |
| `value` | string | `""` | the code entered |

## Behaviour

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `digits` | number | `10`| character set: 10 digits, 36 alphanumeric |
| `paste` | boolean | `true` | allow pasting a whole code |
| `autoComplete` | string | `one-time-code` | autofill of the operating system |
| `verifyOnComplete` | boolean | `true` | verify once the last character is set |
| `mask` | boolean | `false` | hide the characters |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onChange` | function | partial value changed |
| `onComplete` | function | all characters set |
| `onResend` | function | new code requested |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | `group`, the individual fields `textbox` |
| `aria-label` | string | needed per box, e.g. "character 3 of 6" |
| `aria-describedby` | string | id of the help text below the boxes |

## Inherited from

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[base component](../../basics/base.md)
