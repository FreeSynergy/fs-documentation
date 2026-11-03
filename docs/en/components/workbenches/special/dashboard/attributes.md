# Dashboard - Attribute

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `widgets` | array[] | - | Array von Widgets |

## Behaviour

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `dragAndDrop` | boolean | `true` | Drag & Drop aktivieren? |
| `responsive` | boolean | `true` | responsive layout? |

## Presentation

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `columns` | number | `3` | number of columns |
| `gap` | number | `16` | Abstand zwischen Widgets |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onWidgetMove` | function | Wird beim Verschieben ausgeführt |
| `onWidgetResize` | function | Wird beim Resizen ausgeführt |
| `onWidgetRemove` | function | Wird beim Entfernen ausgeführt |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | ARIA role: `region` |

## Widget-Attribute

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `id` | string | Eindeutige ID |
| `type` | string | Widget-Typ |
| `title` | string | Titel |
| `content` | string/node | Inhalt |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
