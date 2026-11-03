# Reorder - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `reorder` | Name der Animation |
| `fromIndex` | number | - | Position vor der Änderung |
| `toIndex` | number | - | Position nach der Änderung |
| `onReorderStart` | function | - | Wird beim Beginn der Bewegung ausgeführt |
| `onReorderEnd` | function | - | Wird nach dem Einrasten ausgeführt |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `320` | Dauer der Bewegung in ms |
| `timingFunction` | string | `ease-in-out` | sanft starten, präzise einrasten |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `forwards` | neue Position nach Ende beibehalten |

## Positions-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `messung` | string | `flip` | `flip` (vorher/nachher messen) oder `transform` (nur verschieben) |
| `achse` | string | `auto` | `auto`, `y`, `x` – Bewegungsachse, meist Listenrichtung |
| `nurSichtbare` | boolean | `true` | Elemente außerhalb des Viewports springen ohne Animation |
| `maxElemente` | number | `40` | Obergrenze gleichzeitig animierter Elemente |
| `einrasten` | number | `0` | leichtes Über- und Zurückfedern am Ziel in px |
| `andereZurueckhaltend` | number | `0.8` | Nachbar-Elemente laufen in `duration` × Faktor |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `aria-live` | string | `polite` | neue Position ansagen („Eintrag 3 von 12“) |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `instant` | Positionen ohne Bewegung tauschen |
