# Stagger - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `stagger` | boolean | `false` | zeitversetzte Starts für Kind-Elemente |
| `reihenfolge` | string | `index` | `index`, `umgekehrt` oder `zufall` |
| `kinder` | selector | `alle` | welche Kind-Elemente gestaffelt werden |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `delay` | number | `0` | Basiswartezeit der gesamten Gruppe |
| `iterationCount` | number \| `infinite` | `1` | wiederholt die gesamte Gruppe |
| `direction` | string | `normal` | `reverse` staffelt ab dem letzten Kind |

## Stagger-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `offsetProElement` | number | `50` | Zeitabstand der Starts in ms (Standard: `staggerStep`) |
| `gruppenLimit` | number | `0` | max. gleichzeitig startende Kinder (0 = unbegrenzt) |
| `beimAusgangUmkehren` | boolean | `true` | Ausgang beginnt beim letzten Kind |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
