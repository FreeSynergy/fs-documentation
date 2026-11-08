# Hover Card - Attribute

Nur **eigene** Attribute. Alles Übrige kommt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `target` | string | - | ID oder Verweis auf das Ziel der Vorschau |
| `content` | object | - | vorausgefüllte Felder der Karte |
| `placement` | enum | `top` | Seite der Karte: `top`, `bottom`, `left`, `right` |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `openDelay` | number | `300` | Verzögerung bis zum Öffnen in ms |
| `closeDelay` | number | `150` | Verzögerung bis zum Schließen in ms |
| `pressDuration` | number | `500` | langes Drücken in ms, das die Karte per Touch öffnet |
| `interactive` | boolean | `true` | die Karte darf betreten und bedient werden |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onOpen` | function | die Karte erscheint |
| `onClose` | function | die Karte verschwindet |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `tooltip` |
| `aria-describedby` | string | ID der Karte, auf die der Auslöser zeigt |
| `focusable` | boolean | die Karte ist per Tastatur erreichbar, wenn `interactive` gesetzt ist |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../../primitives/basics/base.md)
