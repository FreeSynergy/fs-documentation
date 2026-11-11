# Map View - Erscheinungsbild

## Grundlayout
Eine Kartenansicht zeigt interaktive Karten (Google Maps, Leaflet, OpenStreetMap).

```
┌─────────────────────────────────────────┐
│                                         │
│         🗺️                              │
│         Kartenansicht                   │
│                                         │
│      [Zoom+]  [Zoom-] [Satellit]        │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|---------|------------|
| **standort** | ein zentrierter Marker, darüber die Adresszeile |
| **sammlung** | viele Marker, bei hoher Dichte als Liste oder Cluster |
| **route** | Linien und Flächen, Start und Ziel als unterschiedliche Symbole |

## Größen

| Größe | Breite | Verwendung |
|------|-------|-----|
| Klein | 300px | in Textzeilen |
| Mittel | 500px | Standard |
| Groß | 700px | hervorgehoben |
| Voll | 100% | volle Breite |

## Farben und Zustände

| Zustand | Farbe | Beschreibung |
|-------|--------|-------------|
| **Karte** | hängt vom Thema ab | Kartenthema |
| **Marker** | Rot/Primärfarbe | Markierungen |
| **Bedienelemente** | Weiß/Schwarz | Steuerelemente |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|-------------|
| `zoom` | Zoomen beim Scrollen |
| `drag` | Karte verschieben |

## Responsives Verhalten

- Die Karte füllt die verfügbare Breite; als eingebettete Karte ist sie mindestens 200 px hoch.
- Unterhalb der Breite `small` werden die Zoom- und Stil-Schaltflächen zu einer kleinen Leiste
  am unteren Rand. Die Bedienelemente bleiben mindestens 44 px groß.
- Zwei Finger verschieben und skalieren (`drag`, `pinch`). Normales Scrollen über der Karte
  scrollt die Seite, nicht die Karte. Zum Zoomen per Scrollen zuerst auf die Karte klicken.

## Kartentypen

| Typ | Beschreibung |
|------|-------------|
| **Straßenkarte** | normale Straßenkarte |
| **Satellit** | Satellitenansicht |
| **Hybrid** | Mischung aus Straßenkarte und Satellit |
| **Gelände** | Geländeansicht |

## Marker

```
┌─────────────────────────────────────────┐
│      📍                                 │
│   Standort                              │
└─────────────────────────────────────────┘
```

## Bedienelemente

```
┌─────────────────────────────────────────┐
│      [+]  [-]                           │
│  [Satellit] [Hybrid]                    │
└─────────────────────────────────────────┘
```
