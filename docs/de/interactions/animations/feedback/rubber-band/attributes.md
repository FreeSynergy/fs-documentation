# Rubber Band - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `rubberBand` | boolean | `true` | Gummibandwiderstand aktiviert |
| `achse` | string | `vertikal` | `vertikal`, `horizontal` oder `beide` |
| `widerstand` | number | `0.35` | Folgefaktor: 1 = folgt 1:1, kleiner = straffer |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `duration` | number | `400` | Zurückfedern nach dem Loslassen in ms |
| `timingFunction` | string | `spring` | federnde Rückkehr in die Randposition |

## Rubber-Band-Attribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `maxAuszug` | number | `120` | maximales Herausziehen über den Rand in px |
| `randEinzug` | number | `0` | freie Strecke, bevor der Widerstand einsetzt (px) |
| `trigger` | string | `scroll` | `scroll`, `drag` oder `beides` |
| `seite` | string | `beide` | `beide`, `anfang`, `ende` der Liste |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `aria-label` | string | - | beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
