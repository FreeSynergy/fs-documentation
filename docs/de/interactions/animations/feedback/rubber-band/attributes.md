# Rubber Band - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `rubberBand` | boolean | `true` | Gummiband-Widerstand aktiviert |
| `achse` | string | `vertikal` | `vertikal`, `horizontal` oder `beide` |
| `widerstand` | number | `0.35` | Folgefaktor: 1 = folgt 1:1, kleiner = zäher |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `400` | Rückfederung nach dem Loslassen in ms |
| `timingFunction` | string | `spring` | federnder Rücklauf in die Randlage |

## Rubber-Band-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `maxAuszug` | number | `120` | maximaler Auszug über den Rand in px |
| `randEinzug` | number | `0` | freier Weg, bevor der Widerstand einsetzt (px) |
| `trigger` | string | `scroll` | `scroll`, `drag` oder `beides` |
| `seite` | string | `beide` | `beide`, `anfang`, `ende` der Liste |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
