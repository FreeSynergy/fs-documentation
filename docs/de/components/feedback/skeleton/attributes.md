# Skeleton (Platzhalter) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `shape` | enum | `text` | `text`, `rect`, `circle`, `card`, `list-item`, `table-row`, `avatar` |
| `width` | number \| string | - | Breite in px oder Prozent |
| `height` | number | - | Höhe in px |
| `lines` | number | `1` | Balkenanzahl bei `text` |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | enum | `shimmer` | `shimmer`, `pulse`, `none` |
| `round` | boolean | `true` | abgerundete Ecken |

## Events

Es werden keine Events genutzt; ein Skeleton ist reine Anzeige.

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-hidden` | boolean | immer `true` – der Platzhalter enthält keine Information |
| – | – | Der umgebende Bereich erhält `aria-busy="true"` |

## Geerbt von

`id`, `visible`, `size`, `theme`, `rounded`, `animation`, `aria-*` →
[Basiskomponente](../../basics/base/)
