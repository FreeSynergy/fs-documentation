# Calendar View - Aussehen

## Grundlayout
Eine Calendar View zeigt Termine in einem Kalender an.

```
┌─────────────────────────────────────────┐
│ Mo │ Di │ Mi │ Do │ Fr │ Sa │ So       │
├─────────────────────────────────────────┤
│    │  1 │  2 │  3 │  4 │  5 │  6       │
│  7 │  8 │  9 │ 10 │ 11 │ 12 │ 13       │
│ 14 │ 15 │ 16 │ 17 │ 18 │ 19 │ 20       │
│ 21 │ 22 │ 23 │ 24 │ 25 │ 26 │ 27       │
│ 28 │ 29 │ 30 │ 31 │    │    │          │
└─────────────────────────────────────────┘
```

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Monthly View** | Monatsansicht |
| **Weekly View** | Wochenansicht |
| **Daily View** | Tagesansicht |
| **Agenda View** | Listenansicht |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 250px | Kleine Kalender |
| Medium | 350px | Standard |
| Large | 500px | Große Kalender |
| Full | 100% | Volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Today** | Primärfarbe | Heute |
| **Selected** | Dunkel | Ausgewählter Tag |
| **Event** | Grün | Mit Termin |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `background` | Hintergrund ändert sich |
| `border` | Rand leuchtet auf |

## Reaktiv

- Der Monatswechsel per `swipe` ist ein `slide-in` der gesamten Rasters.
- Unter `small` Bildschirmbreite zeigt die Wochenansicht drei Tage, die Tagesansicht bleibt
  vollbreit; die Agenda-Variante verdrängt das Raster ganz.
- Die Zeitachse der Tages- und Wochenansicht ist mindestens 44 px pro Stunde breit;
  `pinch` ändert die Zeitskala, der Inhalt bleibt lesbar.
