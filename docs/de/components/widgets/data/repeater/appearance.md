# Repeater - Aussehen

## Grundlayout
Ein Repeater ist ein Wiederholtes Layout für Listen.

```
┌─────────────────────────────────────────┐
│ Item 1                                  │
│ Inhalt 1                                │
├─────────────────────────────────────────┤
│ Item 2                                  │
│ Inhalt 2                                │
├─────────────────────────────────────────┤
│ Item 3                                  │
│ Inhalt 3                                │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **liste** | Einträge untereinander, Trennlinien dazwischen |
| **raster** | Einträge als Karten in Spalten |
| **eingabe** | Feldgruppen untereinander, unten ``+ Zeile hinzufügen`` |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 200px | Kleine Repeaters |
| Medium | 300px | Standard |
| Large | 400px | Große Repeaters |
| Full | 100% | Volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Item** | Hell | Item-Hintergrund |
| **Hover** | Heller | Hover-Zustand |
| **Active** | Primärfarbe | Aktiver Item |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `shadow` | Schatten stärker |
| `transform` | Leichte Hebung |
| `border` | Rand leuchtet auf |

## Reaktiv

- Die Steuerleiste (Suche, Filter, Sortierung) bricht auf schmalen Bildschirmen in zwei Zeilen um
  und bleibt beim Scrollen oben stehen.
- Die Raster-Variante folgt denselben Spaltenschwellen wie [grid-view](../grid-view/);
  die Listen-Variante bleibt einspaltig.
- Beim Seitenwechsel wird der Listenanfang `scroll-area`-seitig nach oben gesetzt,
  neue Einträge erscheinen mit `fade-in`.
