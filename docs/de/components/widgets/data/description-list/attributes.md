# Description List - Attribute

Nur **eigene** Attribute. Alles Übrige kommt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `items` | array[] | - | Paare aus `label` und `value` |
| `columns` | number | `2` | Spalten der Liste |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `variant` | enum | `zweispaltig` | `zweispaltig`, `gestapelt`, `inline` |
| `showEmpty` | boolean | `false` | leere Werte als Platzhalter anzeigen |
| `dividers` | boolean | `false` | Trennlinien zwischen den Zeilen |
| `copyable` | boolean | `false` | Wert pro Zeile kopierbar machen |
| `groups` | array[] | `null` | Zwischenüberschriften für lange Listen |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onCopy` | function | der Wert wurde kopiert |
| `onValueClick` | function | der Wert ist ein Verweis und wurde ausgelöst |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `list`, Zeilen mit `listitem` |
| `label` | string | Überschrift der Liste, z. B. „Details“ |
| `aria-label` | string | nötig für das Kopiersymbol |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../../primitives/basics/base.md)
