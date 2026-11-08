# Skeleton - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `ladezustand` | string | `geladen` | `laden` blendet das Skeleton ein oder aus |
| `struktur` | string | `zeilen` | `zeilen`, `liste`, `karte`, `tabelle` |
| `zeilen` | number | `3` | Anzahl der Platzhalterzeilen |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `1500` | Dauer eines Schimmerzyklus in ms |
| `timingFunction` | string | `linear` | ein Schimmer, der mit gleichbleibendem Tempo wandert |
| `iterationCount` | number \| `infinite` | `infinite` | läuft, bis der Inhalt eintrifft |

## Skeleton-Attribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `blockFormen` | array | `balken` | Mischung aus `balken`, `kreis`, `block` pro Zeile |
| `zeilenBreiten` | array | `auto` | Breiten in Prozent, z. B. `100 %, 60 %` |
| `rowHeight` | number | `16` | Höhe einer Platzhalterzeile in px |
| `zeilenAbstand` | number | `10` | Abstand zwischen den Zeilen in px |
| `schimmerFarbe` | string | `hell` | Farbe des wandernden Schimmers |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
