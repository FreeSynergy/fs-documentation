# Tooltip (Kurzinfo) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `content` | string | - | angezeigter Text, kein HTML und keine Aktionen |
| `placement` | enum | `auto` | `top`, `right`, `bottom`, `left`, `auto` |
| `open` | boolean | `null` | gesteuerte Sichtbarkeit (`null` = automatisch) |

## Behaviour

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `trigger` | enum | `hover` | `hover`, `focus`, `longpress` |
| `delay` | number | `400` | Verzögerung vor dem Einblenden in ms |
| `hideDelay` | number | `100` | Verzögerung vor dem Ausblenden in ms |

## Presentation

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `arrow` | boolean | `true` | Pfeil zum Bezugselement |
| `maxWidth` | number | `240` | maximale Breite in px |
| `offset` | number | `8` | Abstand zum Element in px |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onShow` | function | Tooltip wurde angezeigt |
| `onHide` | function | Tooltip wurde verborgen |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | `tooltip` |
| – | – | Das Bezugselement erhält `aria-describedby` auf den Tooltip |
| – | – | Interaktiver Inhalt ist nicht zulässig |

## Inherited from

`id`, `visible`, `size`, `theme`, `rounded`, `animation`, `aria-*` →
[Base component](../../../primitives/basics/base.md)
