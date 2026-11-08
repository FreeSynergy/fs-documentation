# Progress - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `value` | number | `0` | aktueller Fortschritt |
| `min` | number | `0` | untere Grenze |
| `max` | number | `100` | obere Grenze |
| `indeterminate` | boolean | `false` | Wert unbekannt, Animation läuft |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `variant` | enum | `linear` | `linear`, `circular` |
| `showLabel` | boolean | `false` | Prozentwert oder Text anzeigen |
| `strokeWidth` | number | - | Balkenhöhe oder Ringstärke |
| `status` | enum | `active` | `active`, `success`, `error` |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onComplete` | function | Wert erreicht `max` |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `progressbar` |
| `aria-valuenow` | number | `value` |
| `aria-valuemin` / `aria-valuemax` | number | `min` / `max` |
| `aria-busy` | boolean | `true`, solange `indeterminate` gilt |
| `aria-label` | string | worauf sich der Fortschritt bezieht |

## Geerbt von

`id`, `visible`, `size`, `theme`, `rounded`, `state`, `animation`, `aria-*` →
[Base-Komponente](../../basics/base.md)
