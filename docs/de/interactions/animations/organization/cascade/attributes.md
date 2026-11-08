# Cascade - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `cascade` | boolean | `false` | zeitversetzte Starts entlang einer Richtung |
| `richtung` | string | `top-left` | `top-left`, `top-right`, `bottom`, `center-out`, `in-center` |
| `kinder` | selector | `alle` | welche Kindelemente kaskadiert werden |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `delay` | number | `0` | Grundwartezeit der ganzen Gruppe |
| `iterationCount` | number \| `infinite` | `1` | wiederholt die ganze Gruppe |
| `direction` | string | `normal` | `reverse` beginnt am anderen Ende der Richtung |

## Zeitattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `stepBase` | number | `50` | Abstand der ersten beiden Starts in ms (Standard: `staggerStep`) |
| `stepGrowth` | number | `0` | Änderung des Abstands pro Element (negativ = schneller werdend) |
| `stepLimit` | number | `200` | Obergrenze des berechneten Abstands in ms |
| `achse` | string | `auto` | `auto`, `x`, `y` oder `diagonal` – entlang welcher Koordinate sortiert wird |
| `wellenLaenge` | number | `0` | Kindelemente, die gleichzeitig starten (0 = jedes einzeln) |
| `beimAusgangUmkehren` | boolean | `true` | der Ausgang läuft in die Gegenrichtung |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `instant` | `instant` (alle gleichzeitig) oder `short-fade` |
