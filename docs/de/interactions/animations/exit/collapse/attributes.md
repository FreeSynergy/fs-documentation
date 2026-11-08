# Collapse - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `animation` | string | `collapse` | Name der Animation |
| `dimension` | string | `height` | `height`, `width` oder `both` |
| `startHeight` | string \| number | `auto` | Starthöhe (`auto` = gemessene Inhaltshöhe) |
| `endHeight` | number | `0` | Zielhöhe in px (Standard 0) |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `250` | Dauer in ms |
| `timingFunction` | string | `ease-in-out` | symmetrisches Beschleunigen und Abbremsen |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `fillMode` | string | `forwards` | Endzustand (Höhe 0) halten, bis das Layout neu berechnet ist |
| `onAnimateEnd` | function | - | Wird ausgeführt, nachdem das Element geschlossen ist |

## Höhenattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `overflow` | string | `hidden` | Inhalt während der Animation abschneiden |
| `includePadding` | boolean | `true` | Innenabstände und Außenabstände mit einbeziehen |
| `minHeight` | number | `0` | Untergrenze, falls es nicht ganz schließen soll |
| `detachAfter` | boolean | `true` | Element nach dem Schließen aus dem DOM entfernen |
| `staggerChildren` | number | `0` | Kindelemente nacheinander in Schritten von ms schließen |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `ariaExpandedSync` | boolean | `true` | `aria-expanded` synchron zum Zustand setzen |
