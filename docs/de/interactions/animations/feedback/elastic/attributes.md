# Elastic - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `overshoot` | number | `30` | Überschießen in % der Bewegungsstrecke |
| `schwingungen` | number | `2` | Anzahl Nachschwingungen bis zur Ruhelage |
| `achse` | string | `beide` | `x`, `y`, `skala` oder `beide` |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `600` | Dauer inklusive Abklingen in ms |
| `timingFunction` | string | `spring` | Federfunktion, alternativ `cubic-bezier(...)` |
| `delay` | number | `0` | verzögerter Start in ms |

## Feder-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `elasticity` | number | `0.6` | Federhärte: 0 = steif, 1 = sehr weich |
| `abklingfaktor` | number | `0.5` | Abnahme der Amplitude je Schwingung (0–1) |
| `amplitude` | number | `auto` | max. Überschießen in px (überschreibt `overshoot`) |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
