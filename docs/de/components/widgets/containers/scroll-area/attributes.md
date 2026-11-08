# Scroll Area - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `direction` | enum | `vertikal` | `vertikal`, `horizontal`, `beides` |
| `height` | number/string | `auto` | feste Höhe der Fläche |
| `content` | array[] | - | der Inhalt des Bereichs |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `follow` | boolean | `false` | bei neuem Inhalt ans Ende scrollen |
| `scrollbar` | enum | `automatisch` | `automatisch`, `immer`, `nie` |
| `edges` | boolean | `true` | Verläufe am Rand |
| `snapTo` | string | `null` | Zeilenraster, auf das sich das Scrollen einrastet |
| `keepPosition` | boolean | `true` | Position beim Nachladen oben beibehalten |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onScroll` | function | Position hat sich geändert |
| `onEndReached` | function | unteres oder rechtes Ende erreicht (Nachladen) |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `group` |
| `tabIndex` | number | nötig (`0`), damit die Tastatur den Bereich erreicht |
| `aria-label` | string | benennt den Bereich, z. B. „Nachrichten“ |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`,
`onClick`, `animation`, `gesture`, `aria-*` →
[Base-Komponente](../../../primitives/basics/base.md)
