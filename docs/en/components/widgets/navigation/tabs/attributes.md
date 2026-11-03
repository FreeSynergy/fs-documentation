# Tabs - Attribute

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `tabs` | array[] | - | Array von Tab-Objekten (id, label, content) |
| `activeTab` | string/number | - | Aktiver Tab (id) |
| `onChange` | function | - | Event bei Tab-Wechsel |
| `position` | enum | `top` | Position: `top`, `bottom`, `left`, `right` |

## Behaviour

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `closable` | boolean | `false` | Tabs schließbar? |
| `scrollable` | boolean | `false` | Scrollbar? |
| `collapsible` | boolean | `false` | Ein-/Ausklappbar? |

## Presentation
| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `showIcons` | boolean | `false` | show icons? |
| `showLabels` | boolean | `true` | Labels anzeigen? |

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `responsive` | boolean | responsive layout? |
| `hideLabelsOnMobile` | boolean | Labels auf Mobile verstecken? |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onSelect` | function | Wird beim Selektieren ausgeführt |
| `onClose` | function | runs when closed |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | ARIA role: `tablist` |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
