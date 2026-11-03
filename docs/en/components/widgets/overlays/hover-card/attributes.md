# Hover Card (Vorschaukarte) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `target` | string | - | id oder Verweis auf das Ziel der Vorschau |
| `content` | object | - | vorbefüllte Felder der Karte |
| `placement` | enum | `top` | Seite der Karte: `top`, `bottom`, `left`, `right` |

## Behaviour

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `openDelay` | number | `300` | Verzögerung bis zum Öffnen in ms |
| `closeDelay` | number | `150` | Verzögerung bis zum Schließen in ms |
| `pressDuration` | number | `500` | Langdruck in ms, der die Karte auf Touch öffnet |
| `interactive` | boolean | `true` | Karte darf betreten und bedient werden |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onOpen` | function | Karte erscheint |
| `onClose` | function | Karte verschwindet |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | `tooltip` |
| `aria-describedby` | string | id der Karte, auf den der Auslöser zeigt |
| `focusable` | boolean | Karte ist über Tastatur erreichbar, wenn `interactive` |

## Inherited from

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Base component](../../../primitives/basics/base.md)
