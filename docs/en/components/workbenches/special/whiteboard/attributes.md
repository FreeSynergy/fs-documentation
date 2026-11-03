# Whiteboard - Attribute

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `toolbar` | array[] | - | Array von Toolbar-Buttons |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `interactive` | boolean | `true` | Interaktiv? |
| `grid` | boolean | `true` | Raster anzeigen? |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onDraw` | function | Wird beim Zeichnen ausgeführt |
| `onClear` | function | Wird beim Löschen ausgeführt |
| `onExport` | function | Wird beim Exportieren ausgeführt |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | ARIA role: `region` |

## Features attributes

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `undoRedo` | boolean | `true` | Rückgängig/Wiederherstellen? |
| `collaborative` | boolean | `false` | Kollaborativ? |

## Export-Attribute

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `exportFormats` | array[] | `['png', 'jpg', 'pdf']` |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
