# Chart - Aussehen

## Grundlayout

Ein Chart ist eine Datenvisualisierung (Diagramme).

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Line** | Verlauf über die Zeit |
| **Bar** | Vergleich einzelner Werte |
| **Pie** | Anteil an einem Ganzen |
| **Doughnut** | Anteil mit Freifläche für eine Gesamtzahl |
| **Scatter** | Zwei Größen gegeneinander |
| **Heatmap** | Dichte über zwei Achsen |
| **Radar** | Mehrere Dimensionen einer Entität |

### Line Chart

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

### Bar Chart

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

### Pie Chart

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
| Small | 300x200px | Inline |
| Medium | 500x300px | Standard |
| Large | 700x400px | Featured |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Background** | Weiß | Hintergrund |
| **Grid** | Grau | Gitterlinien |
| **Data** | Farben | Daten-Serien |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `tooltip` | Tooltip erscheint |
| `highlight` | Segment hervorheben |

## Reaktiv

- Das Diagramm skaliert in der Breite mit dem Container; die Höhe bleibt proportional,
  mindestens aber 200 px.
- Unter `small` Bildschirmbreite fällt die Legende unter die Zeichnung, Achsenbeschriftungen
  werden ausgedünnt (jede zweite Beschriftung).
- Zu viele Balken oder Punkte werden zu Gruppen zusammengefasst, statt überlappend gezeichnet;
  `pinch` vergrößert den Zeitabschnitt einer Linie, `drag` verschiebt ihn.
