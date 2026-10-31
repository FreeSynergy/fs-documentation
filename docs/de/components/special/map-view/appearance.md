# Map View - Aussehen

## Grundlayout

Ein Map View zeigt interaktive Karten an (Google Maps, Leaflet, OpenStreetMap).

## Layout

```
┌─────────────────────────────────────────┐
│                                         │
│         🗺️                              │
│         Kartenansicht                   │
│                                         │
│      [Zoom+]  [Zoom-] [Satellit]        │
└─────────────────────────────────────────┘
```

## Größe-Varianten

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 300px | Inline |
| Medium | 500px | Standard |
| Large | 700px | Featured |
| Full | 100% | Volle Breite |

## Farb-Varianten

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Map** | Abhängig vom Theme | Karten-Theme |
| **Marker** | Rot/Primär | Markierungen |
| **Controls** | Weiß/Schwarz | Steuerungselemente |

## Map-Types

| Type | Beschreibung |
|------|--------------|
| **Roadmap** | Standard-Straßenkarte |
| **Satellite** | Satellitenansicht |
| **Hybrid** | Hybrid aus Roadmap & Satellite |
| **Terrain** | Geländeansicht |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | Zoom beim Scrollen |
| `drag` | Verschieben |

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
