# Expand - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `animation` | string | `expand` | Name der Animation |
| `dimension` | string | `height` | `height`, `width` oder `both` |
| `startHeight` | number | `0` | Starthöhe in px |
| `endHeight` | string \| number | `auto` | Zielhöhe (`auto` = gemessene Inhaltshöhe) |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `duration` | number | `300` | Dauer in ms |
| `timingFunction` | string | `ease-in-out` | meist symmetrisch bei Höhenänderungen |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `fillMode` | string | `both` | hält Start- und Endzustand außerhalb der Laufzeit |
| `onAnimateEnd` | function | - | läuft, nachdem das Element vollständig geöffnet ist |

## Höhenattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `overflow` | string | `hidden` | noch nicht sichtbarer Inhalt wird abgeschnitten |
| `measureMode` | string | `scroll` | Messen der Zielhöhe: `scroll`, `explicit`, `lazy` |
| `maxHeight` | number | `none` | Obergrenze in px, darüber ein Scrollbereich |
| `innerFade` | number | `0` | Kindelemente zusätzlich einblenden (0 = aus) |
| `deferRender` | boolean | `false` | Inhalt erst beim Öffnen rendern |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `aria-label` | string | - | beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `focusOnOpen` | boolean | `false` | Fokus nach dem Öffnen in den neuen Inhalt setzen |
