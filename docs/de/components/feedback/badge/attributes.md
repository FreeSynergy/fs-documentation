# Badge (Abzeichen) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string \| number | - | angezeigter Text oder Zähler |
| `max` | number | `99` | Obergrenze, darüber „99+“ |
| `dot` | boolean | `false` | nur Punkt statt Fläche |
| `showZero` | boolean | `false` | Null anzeigen oder ausblenden |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `variant` | enum | `status` | `status`, `counter`, `dot`, `outline` |
| `status` | enum | `neutral` | `neutral`, `info`, `success`, `warning`, `error` |

## Events

Es werden keine Events genutzt; ein Badge ist reine Anzeige.

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Pflicht, wenn `value` allein nicht verständlich ist („3 neue Nachrichten“) |
| `aria-live` | string | `polite`, wenn sich der Zähler ohne Nutzeraktion ändert |
| `role` | string | `status` bei Zählern, sonst kein interaktives role |

## Geerbt von

`id`, `visible`, `size`, `theme`, `rounded`, `state`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../basics/base/)
