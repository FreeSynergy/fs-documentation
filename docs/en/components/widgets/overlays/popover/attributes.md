# Popover (Inhaltspopover) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `content` | slot | - | Inhalt des Popovers (Aktionen, Text, Formular) |
| `open` | boolean | `false` | geöffnet? (gesteuert) |
| `variant` | enum | `inhalt` | `inhalt`, `aktionen`, `formular` |

## Behaviour
| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `trigger` | enum | `click` | `click`, `hover`, `focus` |
| `placement` | enum | `bottom` | `top`, `right`, `bottom`, `left`, `auto` |
| `dismiss` | enum | `beides` | `click-outside`, `escape`, `beides`, `none` |
| `arrow` | boolean | `true` | Pfeil zum Auslöser |
| `offset` | number | `8` | Abstand zum Auslöser in px |

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `autoFocus` | boolean | `true` | Fokus beim Öffnen in das Popover legen |
| `returnFocus` | boolean | `true` | Fokus beim Schließen zum Auslöser zurück |
| `closeOnAction` | boolean | `false` | nach einer Aktion im Popover schließen |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onOpen` | function | Popover wurde geöffnet |
| `onClose` | function | Popover wurde geschlossen |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | `dialog` bei `variant="formular"`, sonst `presentation` |
| – | – | Auslöser erhält `aria-expanded` und `aria-controls` |
| – | – | Popover erhält eine Beschriftung (`aria-label` oder Überschrift) |

## Inherited from

`id`, `label`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Base component](../../../primitives/basics/base.md)
