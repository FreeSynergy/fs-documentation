# Dashboard - Attribute

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `widgets` | array[] | - | array of widgets |

## Behaviour

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `dragAndDrop` | boolean | `true` | enable drag & drop? |
| `responsive` | boolean | `true` | responsive layout? |

## Presentation

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `columns` | number | `3` | number of columns |
| `gap` | number | `16` | distance between widgets |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onWidgetMove` | function | runs when moving |
| `onWidgetResize` | function | runs when resizing |
| `onWidgetRemove` | function | runs when removing |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | ARIA role: `region` |

## Widget attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | string | unique ID |
| `type` | string | widget type |
| `title` | string | title |
| `content` | string/node | content |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
