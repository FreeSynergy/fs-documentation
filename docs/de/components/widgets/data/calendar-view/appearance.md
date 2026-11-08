# Calendar View - Erscheinungsbild

## Grundlayout
Eine Calendar View zeigt Termine in einem Kalender.

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

| Variante | Beschreibung |
|----------|--------------|
| **Monthly View** | Monatsansicht |
| **Weekly View** | Wochenansicht |
| **Daily View** | Tagesansicht |
| **Agenda View** | Listenansicht |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 250px | kleine Kalender |
| medium | 350px | Standard |
| large | 500px | große Kalender |
| full | 100% | volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Today** | Primärfarbe | heute |
| **Selected** | dunkel | ausgewählter Tag |
| **Event** | grün | hat einen Termin |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `background` | der Hintergrund ändert sich |
| `border` | der Rand leuchtet auf |

## Responsiv

- Den Monat per `swipe` zu wechseln ist ein `slide-in` des gesamten Rasters.
- Unterhalb einer kleinen Bildschirmbreite (`small`) zeigt die Wochenansicht drei Tage, die Tagesansicht
  bleibt volle Breite; die Agenda-Variante ersetzt das Raster vollständig.
- Die Zeitachse der Tages- und Wochenansicht ist pro Stunde mindestens 44 px breit;
  `pinch` ändert den Zeitmaßstab, der Inhalt bleibt lesbar.
