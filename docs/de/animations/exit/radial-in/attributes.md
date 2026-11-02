# Radial In - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `radial-in` | Name der Animation |
| `onAnimateStart` | function | - | Wird beim Start ausgeführt |
| `onAnimateEnd` | function | - | Wird ausgeführt, bevor das Menü aus dem Layout genommen wird |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `160` | Dauer pro Ring in ms |
| `timingFunction` | string | `ease-in` | Punkte beschleunigen zum Anker (Sog) |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `forwards` | Schrumpfen bis zum Entfernen beibehalten |

## Radial-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `origin` | string | `anchor` | Sammelpunkt: Ankermitte (`center`, `fab`, Zeiger …) |
| `toRadius` | number | `0` | Zielabstand vom Anker (0 = Kernmitte) |
| `fromScale` | number | `1` | Startgröße der Punkte |
| `toScale` | number | `0` | Endgröße |
| `staggerStep` | number | `10` | Versatz zwischen Punkten in ms |
| `ringStep` | number | `50` | Versatz zwischen Ringen in ms |
| `order` | string | `outside-in` | Reihenfolge: `outside-in`, `angle`, `all` |
| `fadePoints` | boolean | `true` | Punkte zusätzlich ausblenden? |
| `keepAnchorLast` | boolean | `true` | Ankerkern verschwindet zuletzt? |
| `mirrorOf` | string | `radial-out` | Name der Gegenanimation |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `fade-out` | `instant` (sofort verdecken) oder `fade-out` |
