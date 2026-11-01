# Hover Card (Vorschaukarte) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `target` | string | - | id oder Verweis auf das Ziel der Vorschau |
| `content` | object | - | vorbefüllte Felder der Karte |
| `placement` | enum | `top` | Seite der Karte: `top`, `bottom`, `left`, `right` |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `openDelay` | number | `300` | Verzögerung bis zum Öffnen in ms |
| `closeDelay` | number | `150` | Verzögerung bis zum Schließen in ms |
| `pressDuration` | number | `500` | Langdruck in ms, der die Karte auf Touch öffnet |
| `interactive` | boolean | `true` | Karte darf betreten und bedient werden |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onOpen` | function | Karte erscheint |
| `onClose` | function | Karte verschwindet |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `tooltip` |
| `aria-describedby` | string | id der Karte, auf den der Auslöser zeigt |
| `focusable` | boolean | Karte ist über Tastatur erreichbar, wenn `interactive` |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../basics/base/)
