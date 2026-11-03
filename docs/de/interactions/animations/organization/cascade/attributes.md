# Cascade - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `cascade` | boolean | `false` | zeitversetzte Starts entlang einer Richtung |
| `richtung` | string | `top-left` | `top-left`, `top-right`, `bottom`, `center-out`, `in-center` |
| `kinder` | selector | `alle` | welche Kind-Elemente kaskadiert werden |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `delay` | number | `0` | Basiswartezeit der gesamten Gruppe |
| `iterationCount` | number \| `infinite` | `1` | wiederholt die gesamte Gruppe |
| `direction` | string | `normal` | `reverse` beginnt am anderen Ende der Richtung |

## Zeitsteuerungs-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `stepBase` | number | `50` | Abstand der ersten beiden Starts in ms (Standard: `staggerStep`) |
| `stepGrowth` | number | `0` | Veränderung des Abstands pro Element (negativ = schneller werdend) |
| `stepLimit` | number | `200` | Obergrenze des berechneten Abstands in ms |
| `achse` | string | `auto` | `auto`, `x`, `y` oder `diagonal` – entlang welcher Koordinate sortiert wird |
| `wellenLaenge` | number | `0` | Kinder, die gleichzeitig starten (0 = jedes einzeln) |
| `beimAusgangUmkehren` | boolean | `true` | Ausgang läuft in Gegenrichtung |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `instant` | `instant` (alle gleichzeitig) oder `short-fade` |
