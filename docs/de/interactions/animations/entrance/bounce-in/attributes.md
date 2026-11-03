# Bounce In - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onAnimateStart` | function | - | Wird beim Start der Einbewegung ausgeführt |
| `onBounce` | function | - | Wird bei jedem Überschwingen ausgeführt |
| `onAnimateEnd` | function | - | Wird nach dem endgültigen Einpendeln ausgeführt |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `500` | Gesamtdauer inklusive Ausfedern in ms |
| `timingFunction` | string | `cubic-bezier(.34,1.56,.64,1)` | Federkurve mit Überschwingen |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `forwards` | Endposition nach dem Einpendeln beibehalten |

## Amplituden-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `overshoot` | number | `12` | Überschwingen über die Endposition in % |
| `bounceCount` | number | `2` | Anzahl der Rückfederungen |
| `startScale` | number | `0.5` | Startskalierung (0 = poppt aus dem Nichts) |
| `dropHeight` | number | `0` | Fallhöhe von oben in px (größer 0 für Drop-Variante) |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | - | `fade` – nur einblenden statt Federbewegung |
