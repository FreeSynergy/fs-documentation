# Map View - Aussehen

## Grundlayout
Ein Map View zeigt interaktive Karten an (Google Maps, Leaflet, OpenStreetMap).

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

| Variante | Aussehen |
|----------|----------|
| **standort** | ein Marker zentriert, Adresszeile darüber |
| **sammlung** | viele Marker, Liste oder Punktehaufen bei großer Dichte |
| **route** | Linien und Flächen, Start und Ziel als unterschiedliche Zeichen |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 300px | Inline |
| Medium | 500px | Standard |
| Large | 700px | Featured |
| Full | 100% | Volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Map** | Abhängig vom Theme | Karten-Theme |
| **Marker** | Rot/Primär | Markierungen |
| **Controls** | Weiß/Schwarz | Steuerungselemente |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | Zoom beim Scrollen |
| `drag` | Verschieben |

## Map-Types

| Type | Beschreibung |
|------|--------------|
| **Roadmap** | Standard-Straßenkarte |
| **Satellite** | Satellitenansicht |
| **Hybrid** | Hybrid aus Roadmap & Satellite |
| **Terrain** | Geländeansicht |

## Marker

```
┌─────────────────────────────────────────┐
│      📍                                 │
│   Standort                              │
└─────────────────────────────────────────┘
```

## Controls

```
┌─────────────────────────────────────────┐
│      [+]  [-]                           │
│  [Satellit] [Hybrid]                    │
└─────────────────────────────────────────┘
```

## Reaktiv

- Die Karte füllt die verfügbare Breite; als Inline-Karte ist sie mindestens 200 px hoch.
- Unter `small` Bildschirmbreite werden Zoom- und Stil-Knöpfe zu einer kleinen Leiste unten,
  die Steuerung bleibt mindestens 44 px groß.
- Zwei Finger bewegen und skalieren (`drag`, `pinch`); einfaches Scrollen über der Karte
  verschiebt die Seite, nicht die Karte — Zoom per Scrollen erst nach Klick auf die Karte.
