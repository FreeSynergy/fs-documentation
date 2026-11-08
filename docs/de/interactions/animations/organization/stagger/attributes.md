# Stagger - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `stagger` | boolean | `false` | zeitversetzte Starts für Kindelemente |
| `reihenfolge` | string | `index` | `index`, `umgekehrt` oder `zufall` |
| `kinder` | selector | `alle` | welche Kindelemente versetzt starten |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `delay` | number | `0` | Grundwartezeit der ganzen Gruppe |
| `iterationCount` | number \| `infinite` | `1` | wiederholt die ganze Gruppe |
| `direction` | string | `normal` | `reverse` staffelt ab dem letzten Kind |

## Stagger-Attribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `offsetProElement` | number | `50` | zeitlicher Abstand der Starts in ms (Standard: `staggerStep`) |
| `gruppenLimit` | number | `0` | maximale Anzahl gleichzeitig startender Kindelemente (0 = unbegrenzt) |
| `beimAusgangUmkehren` | boolean | `true` | der Ausgang beginnt beim letzten Kind |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
