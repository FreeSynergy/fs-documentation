# Badge - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `value` | string \| number | - | der angezeigte Text oder Zähler |
| `max` | number | `99` | Obergrenze, darüber „99+“ |
| `dot` | boolean | `false` | nur ein Punkt statt einer Fläche |
| `showZero` | boolean | `false` | Null anzeigen oder ausblenden |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `variant` | enum | `status` | `status`, `counter`, `dot`, `outline` |
| `status` | enum | `neutral` | `neutral`, `info`, `success`, `warning`, `error` |

## Ereignisse

Es werden keine Ereignisse genutzt. Ein Badge dient nur der Anzeige.

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | nötig, wenn `value` allein nicht verständlich ist („3 neue Nachrichten“) |
| `aria-live` | string | `polite`, wenn sich der Zähler ohne Zutun des Nutzers ändert |
| `role` | string | `status` für Zähler, sonst keine interaktive Rolle |

## Geerbt von

`id`, `visible`, `size`, `theme`, `rounded`, `state`, `animation`, `gesture`, `aria-*` →
[Base-Komponente](../../basics/base.md)
