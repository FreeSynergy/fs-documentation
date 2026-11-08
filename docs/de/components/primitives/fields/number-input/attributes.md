# Number Input - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `value` | number | - | Wert |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `min` | number | - | kleinster Wert |
| `max` | number | - | größter Wert |
| `step` | number | `1` | Schrittweite |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showStepButtons` | boolean | `true` | Schrittbuttons anzeigen? |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onKeyDown` | function | wird bei einem Tastendruck ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `spinbutton` |

## Validierungsattribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `required` | boolean | `false` | Pflichtfeld? |
| `error` | string | - | Fehlermeldung |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base-Komponente](../../basics/base.md)
