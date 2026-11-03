# Expand - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `expand` | Name der Animation |
| `dimension` | string | `height` | `height`, `width` oder `both` |
| `startHeight` | number | `0` | Ausgangshöhe in px |
| `endHeight` | string \| number | `auto` | Zielhöhe (`auto` = gemessene Inhaltshöhe) |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `300` | Dauer in ms |
| `timingFunction` | string | `ease-in-out` | für Höhenänderungen meist symmetrisch |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `both` | Start- und Endzustand außerhalb der Laufzeit halten |
| `onAnimateEnd` | function | - | Wird nach dem vollständigen Öffnen ausgeführt |

## Höhen-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `overflow` | string | `hidden` | Noch nicht sichtbarer Inhalt wird abgeschnitten |
| `measureMode` | string | `scroll` | Messung der Zielhöhe: `scroll`, `explicit`, `lazy` |
| `maxHeight` | number | `none` | Obergrenze in px, darüber Scrollbereich |
| `innerFade` | number | `0` | Kind-Elemente zusätzlich einblenden (0 = aus) |
| `deferRender` | boolean | `false` | Inhalt erst beim Öffnen rendern |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `focusOnOpen` | boolean | `false` | Fokus nach dem Öffnen in den neuen Inhalt legen |
