# Whiteboard - Attribute

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `toolbar` | array[] | - | array of toolbar buttons |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `interactive` | boolean | `true` | interactive? |
| `grid` | boolean | `true` | show a grid? |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onDraw` | function | runs when drawing |
| `onClear` | function | runs when clearing |
| `onExport` | function | runs on export |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | ARIA role: `region` |

## Features attributes

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `undoRedo` | boolean | `true` | undo/redo? |
| `collaborative` | boolean | `false` | collaborative? |

## Export attributes

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `exportFormats` | array[] | `['png', 'jpg', 'pdf']` |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
