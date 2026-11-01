# Input Group (Feldgruppe) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/). Das Eingabefeld in der Gruppe bringt seine
eigenen Attribute mit.

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `children` | slot | - | Feld und Gruppen-Elemente in Reihenfolge |
| `attached` | boolean | `true` | Elemente bündig an das Feld gesetzt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `group` |
| – | – | Statische Präfixe (Währung, Protokoll) mit `aria-hidden`, wenn der Kontext sie ersetzt |
| – | – | Interaktive Gruppen-Elemente brauchen eigenes `aria-label` |

## Gruppen-Elemente

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `prefix` | slot | `null` | links vorangestelltes Element |
| `suffix` | slot | `null` | rechts nachgestelltes Element |
| `interactive` | boolean | `false` | mindestens ein Gruppen-Element ist bedienbar |

## Geerbt von

`id`, `visible`, `size`, `theme`, `rounded`, `state`, `animation`, `aria-*` →
[Basiskomponente](../../basics/base/)
