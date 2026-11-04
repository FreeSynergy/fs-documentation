# Rich Text Editor - Attributes

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `value` | string | - | value (HTML) |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `placeholder` | string | `null` | placeholder text |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onSave` | function | runs on save |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | ARIA role: `textbox` |

## Toolbar attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showToolbar` | boolean | `true` | show the toolbar? |
| `toolbarButtons` | array[] | - | array of buttons |

## Features attributes

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `enableImages` | boolean | `true` | allow images? |
| `enableLinks` | boolean | `true` | allow links? |
| `enableCode` | boolean | `true` | allow code? |
| `enablePreview` | boolean | `true` | allow a preview? |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
