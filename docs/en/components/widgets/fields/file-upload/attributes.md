# File Upload - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | file/array | - | file(s) |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `multiple` | boolean | `false` | several files? |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showProgress` | boolean | `true` | show the progress? |
| `showPreview` | boolean | `false` | show a preview? |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onDrop` | function | runs on drop |
| `onError` | function | runs on an error |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `button` |

## Validation attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `accept` | string | accepted file types (e.g. `.jpg,.png`) |
| `maxSize` | number | maximum file size in bytes |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
