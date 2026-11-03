# Tooltip (Kurzinfo) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `content` | string | - | angezeigter Text, kein HTML und keine Aktionen |
| `placement` | enum | `auto` | `top`, `right`, `bottom`, `left`, `auto` |
| `open` | boolean | `null` | gesteuerte Sichtbarkeit (`null` = automatisch) |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `trigger` | enum | `hover` | `hover`, `focus`, `longpress` |
| `delay` | number | `400` | Verzögerung vor dem Einblenden in ms |
| `hideDelay` | number | `100` | Verzögerung vor dem Ausblenden in ms |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `arrow` | boolean | `true` | Pfeil zum Bezugselement |
| `maxWidth` | number | `240` | maximale Breite in px |
| `offset` | number | `8` | Abstand zum Element in px |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onShow` | function | Tooltip wurde angezeigt |
| `onHide` | function | Tooltip wurde verborgen |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `tooltip` |
| – | – | Das Bezugselement erhält `aria-describedby` auf den Tooltip |
| – | – | Interaktiver Inhalt ist nicht zulässig |

## Geerbt von

`id`, `visible`, `size`, `theme`, `rounded`, `animation`, `aria-*` →
[Basiskomponente](../../basics/base/)
