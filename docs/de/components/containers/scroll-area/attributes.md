# Scroll Area (Laufbereich) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `direction` | enum | `vertikal` | `vertikal`, `horizontal`, `beides` |
| `height` | number/string | `auto` | feste Höhe der Fläche |
| `content` | array[] | - | Inhalte des Bereichs |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `follow` | boolean | `false` | ans Ende laufen, wenn neuer Inhalt hinzukommt |
| `scrollbar` | enum | `automatisch` | `automatisch`, `immer`, `nie` |
| `edges` | boolean | `true` | Verläufe an den Rändern |
| `snapTo` | string | `null` | Zeilenraster, an das das Laufen einrastet |
| `keepPosition` | boolean | `true` | Position beim Nachladen oben halten |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onScroll` | function | Position geändert |
| `onEndReached` | function | unteres oder rechtes Ende erreicht (Nachladen) |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `group` |
| `tabIndex` | number | Pflicht (`0`), damit Tastatur den Bereich bewegen kann |
| `aria-label` | string | Bereich benennen, z. B. „Nachrichten“ |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`,
`onClick`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../basics/base/)
