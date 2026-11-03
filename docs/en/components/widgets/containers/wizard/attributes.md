# Wizard - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `steps` | array[] | - | array of step objects |
| `activeStep` | number | 0 | current step |
| `onChange` | function | - | event on step change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `validation` | boolean | `false` | validate per step? |
| `clickable` | boolean | `false` | clickable? |
| `animate` | boolean | `true` | enable animations? |
| `animationDuration` | number | `300` | duration in ms |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onNext` | function | runs on clicking next |
| `onBack` | function | runs on clicking back |
| `onComplete` | function | runs on clicking finish |
| `onStepClick` | function | runs on clicking a step |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `region` |

## Step attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | string | unique ID |
| `title` | string | title |
| `description` | string | description |
| `content` | string/node | content |
| `completed` | boolean | completed? |

## Validation attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `validateStep` | function | validation function |
| `errorMessages` | object | error messages |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
