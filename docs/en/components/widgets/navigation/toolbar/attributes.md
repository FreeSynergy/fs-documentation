# Toolbar - Attribute

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `buttons` | array[] | - | Array von Button-Objekten |
| `variant` | enum | `default` | Stil: `default`, `floating`, `sidebar` |
| `position` | enum | `top` | Position: `top`, `bottom`, `left`, `right` |
| `tabs` | array[] | - | Array von Tab-Objekten |
| `activeTab` | string | - | Aktiver Tab |
| `onChange` | function | - | Event bei Tab-Wechsel |

## Behaviour

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `showLabels` | boolean | `true` | Labels anzeigen? |
| `showIcons` | boolean | `true` | show icons? |
| `collapsed` | boolean | `false` | Eingeklappt? |
| `autoHide` | boolean | `true` | Automatisch ausblenden? |
| `target` | DOM element | - | Ziel-Element |
| `offset` | object | - | { x, y } Offset zur Position |
| `groups` | array[] | - | Array von Group-Objekten |
| `commands` | array[] | - | Array von Command-Objekten |
| `minimized` | boolean | `false` | Minimiert? |
| `collapsible` | boolean | `true` | Ein-/Ausklappbar? |
| `size` | enum | `standard` | Größe: `compact`, `standard`, `large` |

## Events
| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onButtonClick` | function | Wird beim Button-Klick ausgeführt |
| `onExpand` | function | Wird beim Erweitern ausgeführt |
| `onCollapse` | function | Wird beim Einklappen ausgeführt |
| `onVisibilityChange` | function | Wird bei Sichtbarkeitsänderung ausgeführt |
| `onSelect` | function | Wird beim Selektieren ausgeführt |
| `onMinimize` | function | Wird beim Minimieren ausgeführt |

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `keyboardShortcuts` | boolean | `true` | Keyboard-Shortcuts aktivieren? |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | ARIA role: `toolbar` |

## Button-Attribute

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `id` | string | Eindeutige ID |
| `icon` | string | Icon-Name |
| `label` | string | Button-Label |
| `variant` | enum | `primary`, `secondary`, `danger` |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
