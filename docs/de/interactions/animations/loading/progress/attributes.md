# Progress - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `wert` | number | `0` | Aktueller Fortschritt |
| `wertMin` | number | `0` | Untergrenze |
| `wertMax` | number | `100` | Obergrenze |
| `indikator` | string | `balken` | `balken`, `ring`, `segmente` |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `300` | übernimmt neue Werte sanft, in ms |
| `timingFunction` | string | `ease-out` | die Füllung wird zum Ende hin langsamer |
| `iterationCount` | number \| `infinite` | `1` | `infinite` nur für eine unbestimmte Anzeige |

## Fortschrittsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `unbestimmt` | boolean | `false` | eine laufende Anzeige ohne bekannten Wert |
| `farbe` | string | `accent` | Füllfarbe, ab 100 % optional `success` |
| `beschriftung` | string | `auto` | Prozentwert, eigener Text oder `keine` |
| `dicke` | number | `8` | Dicke des Balkens oder Breite des Rings in px |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
