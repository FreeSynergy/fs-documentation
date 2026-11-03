# Description List (Beschreibungsliste) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `items` | array[] | - | Paare aus `label` und `value` |
| `columns` | number | `2` | Spalten der Liste |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `variant` | enum | `zweispaltig` | `zweispaltig`, `gestapelt`, `inline` |
| `showEmpty` | boolean | `false` | leere Werte als Platzhalter anzeigen |
| `dividers` | boolean | `false` | Trennlinien zwischen Zeilen |
| `copyable` | boolean | `false` | Wert pro Zeile kopierbar machen |
| `groups` | array[] | `null` | Zwischenüberschriften für lange Listen |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onCopy` | function | Wert wurde kopiert |
| `onValueClick` | function | Wert ist ein Verweis und wurde ausgelöst |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `list`, Zeilen mit `listitem` |
| `label` | string | Überschrift der Liste, z. B. „Details“ |
| `aria-label` | string | für Kopieren-Icon nötig |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../basics/base/)
