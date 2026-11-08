# Reorder - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `animation` | string | `reorder` | Name der Animation |
| `fromIndex` | number | - | Position vor der Änderung |
| `toIndex` | number | - | Position nach der Änderung |
| `onReorderStart` | function | - | Wird ausgeführt, wenn die Bewegung beginnt |
| `onReorderEnd` | function | - | Wird ausgeführt, nachdem das Element eingerastet ist |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `320` | Dauer der Bewegung in ms |
| `timingFunction` | string | `ease-in-out` | sanft starten, genau einrasten |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `fillMode` | string | `forwards` | die neue Position nach dem Ende beibehalten |

## Positionsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `messung` | string | `flip` | `flip` (vorher/nachher messen) oder `transform` (nur verschieben) |
| `achse` | string | `auto` | `auto`, `y`, `x` – Bewegungsachse, meist die Richtung der Liste |
| `nurSichtbare` | boolean | `true` | Elemente außerhalb des Viewports springen ohne Animation |
| `maxElemente` | number | `40` | Obergrenze gleichzeitig animierter Elemente |
| `einrasten` | number | `0` | ein leichtes Überschwingen am Ziel in px und Zurückfedern |
| `andereZurueckhaltend` | number | `0.8` | Nachbarelemente wandern in `duration` × Faktor |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `aria-live` | string | `polite` | die neue Position ansagen ("Eintrag 3 von 12") |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `instant` | die Positionen ohne Bewegung tauschen |
