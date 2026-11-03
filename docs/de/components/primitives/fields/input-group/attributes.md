# Input Group (Feldgruppe) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/). Das eingebaute Feld bringt seine eigenen Attribute mit
([text-input](../text-input/)).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `field` | component | - | das Feld in der Gruppe (`text-input`, `number-input`, …) |
| `prefix` | string | `""` | Vorsatz links (Einheit, Vorzeichen, Protokoll) |
| `suffix` | string | `""` | Nachsatz rechts (Einheit, Status) |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `action` | string | `""` | Label der angebauten Schaltfläche; leer = keine Aktion |
| `prefixOptions` | array | - | Optionen für den Vorsatz als Auswahl (z. B. Landesvorwahl) |
| `attach` | boolean | `true` | Flächen zusammenfügen (`false` = mit Abstand) |
| `actionOnEnter` | boolean | `true` | `Enter` im Feld löst die Aktion aus |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onAction` | function | angebaute Schaltfläche betätigt |
| `onPrefixChange` | function | Vorsatz-Auswahl geändert |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `group`; das Feld behält seine eigene Rolle |
| `aria-label` | string | für die Gruppe, wenn Vorsatz und Beschriftung zusammen gehören |
| `aria-hidden` | boolean | Vorsatz-Text, wenn er bereits in `aria-label` des Feldes steht |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `variant`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../basics/base/)
