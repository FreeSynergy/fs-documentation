# Chart - Erscheinungsbild

## Grundlayout

Ein Chart ist eine Datenvisualisierung (Diagramm).

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Line** | Verlauf über die Zeit |
| **Bar** | Vergleich einzelner Werte |
| **Pie** | Anteil am Ganzen |
| **Doughnut** | Anteil mit freiem Raum für eine Summe |
| **Scatter** | zwei Größen gegeneinander |
| **Heatmap** | Dichte über zwei Achsen |
| **Radar** | mehrere Dimensionen eines Objekts |

### Liniendiagramm

```
┌─────────────────────────────────────────┐
│  100 ┤  ╱╲                               │
│      │ ╱  ╲                              │
│   50 ┤╱    ╲                             │
│      │      ╲                            │
│    0 ┼────────╲────────                  │
│      └───────────────────                │
└─────────────────────────────────────────┘
```

### Balkendiagramm

```
┌─────────────────────────────────────────┐
│  100 ┤  ▓▓                               │
│      │  ▓▓                               │
│   50 ┤  ▓▓  ▓▓                           │
│      │  ▓▓  ▓▓  ▓▓                       │
│    0 ┤  ▓▓  ▓▓  ▓▓  ▓▓                   │
│      └───────────────────                │
└─────────────────────────────────────────┘
```

### Kreisdiagramm

```
┌─────────────────────────────────────────┐
│      ╱─────╲                            │
│    ╱         ╲                          │
│   │    50%    │                         │
│    ╲         ╱                          │
│      ╲_____/                            │
└─────────────────────────────────────────┘
```

## Größen

| Größe | Breite/Höhe | Verwendung |
|-------|-------------|------------|
| small | 300x200px | inline |
| medium | 500x300px | Standard |
| large | 700x400px | hervorgehoben |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Background** | weiß | Hintergrund |
| **Grid** | grau | Gitterlinien |
| **Data** | Farben | Datenreihen |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `tooltip` | ein Tooltip erscheint |
| `highlight` | hebt ein Segment hervor |

## Responsiv

- Das Chart skaliert in der Breite mit dem Container; die Höhe bleibt proportional,
  aber mindestens 200 px.
- Unterhalb einer kleinen Bildschirmbreite (`small`) wandert die Legende unter die Zeichnung,
  Achsenbeschriftungen werden ausgedünnt (jede zweite).
- Zu viele Balken oder Punkte werden zusammengefasst, statt sich zu überlappen;
  `pinch` vergrößert den Zeitabschnitt einer Linie, `drag` verschiebt ihn.
