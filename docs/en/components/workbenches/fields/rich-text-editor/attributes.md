# Rich Text Editor - Attribute

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `value` | string | - | Wert (HTML) |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `placeholder` | string | `null` | Placeholder-Text |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onSave` | function | Wird beim Speichern ausgeführt |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | ARIA role: `textbox` |

## Toolbar-Attribute

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `showToolbar` | boolean | `true` | Toolbar anzeigen? |
| `toolbarButtons` | array[] | - | Array von Buttons |

## Features attributes

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `enableImages` | boolean | `true` | Bilder erlauben? |
| `enableLinks` | boolean | `true` | Links erlauben? |
| `enableCode` | boolean | `true` | Code erlauben? |
| `enablePreview` | boolean | `true` | Vorschau erlauben? |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
