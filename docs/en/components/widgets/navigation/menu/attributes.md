# Menu (Menü) - Attribute

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `items` | array[] | - | Array von Menüpunkten |
| `activeItem` | string/number | - | Aktiver Menüpunkt |
| `onChange` | function | - | event on selection |
| `isOpen` | boolean | `false` | Ist geöffnet? |
| `onToggle` | function | - | Event beim Öffnen/Schließen |

## Behaviour

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `variant` | enum | `horizontal` | Stil: `horizontal`, `vertical` |
| `collapsible` | boolean | `false` | Ein-/Ausklappbar? |
| `closable` | boolean | `false` | Schließbar? |
| `closeOnOutsideClick` | boolean | `true` | Bei Klick außerhalb schließen? |
| `keyboardNavigation` | boolean | `true` | Keyboard-Navigation? |
| `animate` | boolean | `true` | enable animations? |
| `animationDuration` | number | `300` | duration in ms |

## Presentation
| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `showIcons` | boolean | `false` | show icons? |
| `showLabels` | boolean | `true` | Labels anzeigen? |
| `color` | enum | `default` | Farbe: `default`, `light`, `primary` |

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `responsive` | boolean | responsive layout? |
| `hamburgerBreakpoint` | number | Breakpoint für Hamburger |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onSelect` | function | Wird beim Selektieren ausgeführt |
| `onOpen` | function | runs when opened |
| `onClose` | function | runs when closed |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | ARIA role: `menubar` |
| `aria-expanded` | boolean | Ist erweitert? |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
