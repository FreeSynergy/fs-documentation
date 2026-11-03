# Progress (Fortschrittsanzeige) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | number | `0` | aktueller Fortschritt |
| `min` | number | `0` | Untergrenze |
| `max` | number | `100` | Obergrenze |
| `indeterminate` | boolean | `false` | Wert unbekannt, Animation läuft |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `variant` | enum | `linear` | `linear`, `circular` |
| `showLabel` | boolean | `false` | Prozentwert oder Text anzeigen |
| `strokeWidth` | number | - | Balkenhöhe bzw. Ringstärke |
| `status` | enum | `active` | `active`, `success`, `error` |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onComplete` | function | Wert erreicht `max` |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `progressbar` |
| `aria-valuenow` | number | `value` |
| `aria-valuemin` / `aria-valuemax` | number | `min` / `max` |
| `aria-busy` | boolean | `true` solange `indeterminate` |
| `aria-label` | string | Worauf sich der Fortschritt bezieht |

## Geerbt von

`id`, `visible`, `size`, `theme`, `rounded`, `state`, `animation`, `aria-*` →
[Basiskomponente](../../basics/base/)
