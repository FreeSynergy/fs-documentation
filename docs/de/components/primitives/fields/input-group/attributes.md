# Input Group - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base.md). Das eingebaute Feld bringt eigene Attribute mit
([text-input](../text-input/)).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `field` | Komponente | - | das Feld in der Gruppe (`text-input`, `number-input`, …) |
| `prefix` | string | `""` | Präfix links (Einheit, Zeichen, Protokoll) |
| `suffix` | string | `""` | Suffix rechts (Einheit, Status) |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `action` | string | `""` | Beschriftung des angesetzten Buttons. Leer = keine Aktion |
| `prefixOptions` | array | - | Auswahloptionen für das Präfix (z. B. Ländervorwahl) |
| `attach` | boolean | `true` | Flächen verbinden (`false` = mit Abstand) |
| `actionOnEnter` | boolean | `true` | `Enter` im Feld löst die Aktion aus |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onAction` | function | angesetzter Button wurde benutzt |
| `onPrefixChange` | function | Auswahl im Präfix wurde geändert |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `group`. Das Feld behält seine eigene Rolle |
| `aria-label` | string | für die Gruppe, wenn Präfix und Beschriftung zusammengehören |
| `aria-hidden` | boolean | Präfixtext, wenn er schon im `aria-label` des Feldes steht |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `variant`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Base-Komponente](../../basics/base.md)
