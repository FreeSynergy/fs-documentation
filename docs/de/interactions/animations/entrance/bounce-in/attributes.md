# Bounce In - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `onAnimateStart` | function | - | läuft, wenn die Bewegung beginnt |
| `onBounce` | function | - | läuft bei jedem Überschwingen |
| `onAnimateEnd` | function | - | läuft nach dem endgültigen Einpendeln |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `duration` | number | `500` | Gesamtdauer inklusive Zurückfedern in ms |
| `timingFunction` | string | `cubic-bezier(.34,1.56,.64,1)` | Federkurve mit Überschwingen |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `fillMode` | string | `forwards` | hält die Endposition nach dem Einpendeln |

## Amplitudenattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `overshoot` | number | `12` | Überschwingen über die Endposition in % |
| `bounceCount` | number | `2` | Anzahl der Rückfederungen |
| `startScale` | number | `0.5` | Startskalierung (0 = springt aus dem Nichts) |
| `dropHeight` | number | `0` | Fallhöhe von oben in px (größer als 0 für die Drop-Variante) |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `aria-label` | string | - | beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | - | `fade` – nur einblenden statt der Federbewegung |
