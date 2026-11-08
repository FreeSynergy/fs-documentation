# Elastic - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `overshoot` | number | `30` | Überschwingen in % der zurückgelegten Strecke |
| `schwingungen` | number | `2` | Anzahl der Nachschwingungen bis zur Ruheposition |
| `achse` | string | `beide` | `x`, `y`, `skala` oder `beide` |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `duration` | number | `600` | Dauer inklusive Abklingen in ms |
| `timingFunction` | string | `spring` | Federfunktion, alternativ `cubic-bezier(...)` |
| `delay` | number | `0` | verzögerter Start in ms |

## Federattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `elasticity` | number | `0.6` | Federsteifigkeit: 0 = steif, 1 = sehr weich |
| `abklingfaktor` | number | `0.5` | Abnahme der Amplitude pro Schwingung (0–1) |
| `amplitude` | number | `auto` | maximales Überschwingen in px (überschreibt `overshoot`) |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `aria-label` | string | - | beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
