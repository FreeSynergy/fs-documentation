# Collapse - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `collapse` | Name der Animation |
| `dimension` | string | `height` | `height`, `width` oder `both` |
| `startHeight` | string \| number | `auto` | Ausgangshöhe (`auto` = gemessene Inhaltshöhe) |
| `endHeight` | number | `0` | Zielhöhe in px (Standard 0) |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `250` | Dauer in ms |
| `timingFunction` | string | `ease-in-out` | symmetrisches Ein- und Ausbremsen |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `forwards` | Endzustand (Höhe 0) bis zum Umräumen halten |
| `onAnimateEnd` | function | - | Wird nach dem Schließen ausgeführt |

## Höhen-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `overflow` | string | `hidden` | Inhalt während der Animation abschneiden |
| `includePadding` | boolean | `true` | Padding und Margen mit einziehen |
| `minHeight` | number | `0` | Untergrenze, falls nicht ganz schließen |
| `detachAfter` | boolean | `true` | Element nach dem Schließen aus dem DOM entfernen |
| `staggerChildren` | number | `0` | Kind-Elemente in ms-Stufen nacheinander einklappen |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `ariaExpandedSync` | boolean | `true` | `aria-expanded` synchron zum Zustand setzen |
