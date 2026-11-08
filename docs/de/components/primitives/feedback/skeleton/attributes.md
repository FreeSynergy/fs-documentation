# Skeleton - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `shape` | enum | `text` | `text`, `rect`, `circle`, `card`, `list-item`, `table-row`, `avatar` |
| `width` | number \| string | - | Breite in px oder Prozent |
| `height` | number | - | Höhe in px |
| `lines` | number | `1` | Anzahl der Balken bei `text` |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `animation` | enum | `shimmer` | `shimmer`, `pulse`, `none` |
| `round` | boolean | `true` | abgerundete Ecken |

## Ereignisse

Es werden keine Ereignisse genutzt. Ein Skeleton dient nur der Anzeige.

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-hidden` | boolean | immer `true`. Der Platzhalter trägt keine Information. |
| – | – | der umgebende Bereich bekommt `aria-busy="true"` |

## Geerbt von

`id`, `visible`, `size`, `theme`, `rounded`, `animation`, `aria-*` →
[Base-Komponente](../../basics/base.md)
