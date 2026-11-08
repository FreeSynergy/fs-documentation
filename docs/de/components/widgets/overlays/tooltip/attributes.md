# Tooltip - Attribute

Nur **eigene** Attribute. Alles Übrige kommt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `content` | string | - | angezeigter Text, kein HTML und keine Aktionen |
| `placement` | enum | `auto` | `top`, `right`, `bottom`, `left`, `auto` |
| `open` | boolean | `null` | gesteuerte Sichtbarkeit (`null` = automatisch) |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `trigger` | enum | `hover` | `hover`, `focus`, `longpress` |
| `delay` | number | `400` | Verzögerung vor dem Einblenden in ms |
| `hideDelay` | number | `100` | Verzögerung vor dem Ausblenden in ms |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `arrow` | boolean | `true` | Pfeil, der auf das Bezugselement zeigt |
| `maxWidth` | number | `240` | maximale Breite in px |
| `offset` | number | `8` | Abstand zum Element in px |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onShow` | function | der Tooltip wurde angezeigt |
| `onHide` | function | der Tooltip wurde ausgeblendet |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `tooltip` |
| – | – | das Bezugselement erhält `aria-describedby`, das auf den Tooltip zeigt |
| – | – | interaktiver Inhalt ist nicht erlaubt |

## Geerbt von

`id`, `visible`, `size`, `theme`, `rounded`, `animation`, `aria-*` →
[Basiskomponente](../../../primitives/basics/base.md)
