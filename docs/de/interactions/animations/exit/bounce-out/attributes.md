# Bounce Out - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `onAnimateStart` | function | - | Wird ausgeführt, wenn der Abschied beginnt |
| `onAnticipation` | function | - | Wird bei der Vorbereitung (Stauchung) ausgeführt |
| `onAnimateEnd` | function | - | Wird ausgeführt, sobald das Element vollständig verschwunden ist |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `400` | Gesamtdauer von Vorbereitung und Sprung in ms |
| `timingFunction` | string | `ease-in` | beschleunigter Abflug |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `fillMode` | string | `forwards` | der unsichtbare Endzustand bleibt erhalten |

## Vorbereitungsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `anticipation` | number | `8` | Zurückziehen entgegen der Ausgangsrichtung in % der Elementgröße |
| `squash` | number | `0.9` | Stauchung der Skalierung vor dem Abflug (1 = keine) |
| `exitDirection` | string | `up` | Richtung des Ausgangssprungs: `up`, `down`, `left`, `right` |
| `endScale` | number | `0.2` | Skalierung im Moment des Verschwindens (0 = ganz geschrumpft) |
| `removeOnEnd` | boolean | `true` | Element nach dem Verschwinden aus dem DOM entfernen? |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | - | `instant` – sofort ausblenden, ohne Federn |
