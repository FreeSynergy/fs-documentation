# Skeleton - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `ladezustand` | string | `geladen` | `laden` blendet das Skeleton ein/aus |
| `struktur` | string | `zeilen` | `zeilen`, `liste`, `karte`, `tabelle` |
| `zeilen` | number | `3` | Anzahl Platzhalterzeilen |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `1500` | Dauer eines Schimmer-Zyklus in ms |
| `timingFunction` | string | `linear` | konstant wandernder Schimmer |
| `iterationCount` | number \| `infinite` | `infinite` | läuft, bis die Inhalte eintreffen |

## Skeleton-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `blockFormen` | array | `balken` | Mischung aus `balken`, `kreis`, `block` je Zeile |
| `zeilenBreiten` | array | `auto` | prozentuale Breiten, z. B. `100 %, 60 %` |
| `rowHeight` | number | `16` | Höhe einer Platzhalterzeile in px |
| `zeilenAbstand` | number | `10` | Abstand zwischen den Zeilen in px |
| `schimmerFarbe` | string | `hell` | Farbe des wandernden Schimmers |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
