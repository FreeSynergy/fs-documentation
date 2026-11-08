# Radial In - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `animation` | string | `radial-in` | Name der Animation |
| `onAnimateStart` | function | - | läuft am Anfang |
| `onAnimateEnd` | function | - | läuft, bevor das Menü aus dem Layout genommen wird |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `duration` | number | `160` | Dauer pro Ring in ms |
| `timingFunction` | string | `ease-in` | Punkte beschleunigen zum Anker (ein Zug) |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `fillMode` | string | `forwards` | hält das Schrumpfen bis zum Entfernen |

## Radialattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `origin` | string | `anchor` | Sammelpunkt: Ankermitte (`center`, `fab`, Zeiger …) |
| `toRadius` | number | `0` | Zielabstand vom Anker (0 = Kernmitte) |
| `fromScale` | number | `1` | Startgröße der Punkte |
| `toScale` | number | `0` | Endgröße |
| `staggerStep` | number | `10` | Versatz zwischen den Punkten in ms |
| `ringStep` | number | `50` | Versatz zwischen den Ringen in ms |
| `order` | string | `outside-in` | Reihenfolge: `outside-in`, `angle`, `all` |
| `fadePoints` | boolean | `true` | Punkte zusätzlich ausblenden? |
| `keepAnchorLast` | boolean | `true` | verschwindet der Ankerkern zuletzt? |
| `mirrorOf` | string | `radial-out` | Name der Gegenanimation |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `aria-label` | string | - | beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `fade-out` | `instant` (sofort ausgeblendet) oder `fade-out` |
