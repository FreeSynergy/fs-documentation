# Slider - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `value` | number | - | Wert |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `min` | number | `0` | minimaler Wert |
| `max` | number | `100` | maximaler Wert |
| `step` | number | `1` | Schrittweite |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showLabels` | boolean | `false` | Beschriftungen anzeigen? |
| `showValue` | boolean | `true` | Wert anzeigen? |
| `vertical` | boolean | `false` | vertikal? |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onChangeEnd` | function | wird am Ende einer Änderung ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `slider` |

## Bereichs-Attribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `range` | boolean | `false` | Bereichsauswahl? |
| `minRange` | number | - | minimale Bereichsgröße |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base.md)
