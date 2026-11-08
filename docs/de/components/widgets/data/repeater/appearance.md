# Repeater - Erscheinungsbild

## Grundlayout
Ein Repeater ist ein sich wiederholendes Layout für Listen.

```
┌─────────────────────────────────────────┐
│ Element 1                               │
│ Inhalt 1                                │
├─────────────────────────────────────────┤
│ Element 2                               │
│ Inhalt 2                                │
├─────────────────────────────────────────┤
│ Element 3                               │
│ Inhalt 3                                │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **liste** | Einträge untereinander, Trennlinien dazwischen |
| **raster** | Einträge als Karten in Spalten |
| **eingabe** | Feldgruppen untereinander, unten ``+ Zeile hinzufügen`` |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 200px | kleine Repeater |
| medium | 300px | Standard |
| large | 400px | große Repeater |
| full | 100% | volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Item** | hell | Hintergrund des Eintrags |
| **Hover** | heller | Hover-Zustand |
| **Active** | Primärfarbe | aktiver Eintrag |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `shadow` | der Schatten wird stärker |
| `transform` | leichtes Anheben |
| `border` | der Rand leuchtet auf |

## Responsiv

- Auf schmalen Bildschirmen bricht die Bedienleiste (Suche, Filter, Sortierung) in zwei Zeilen um
  und bleibt beim Scrollen oben stehen.
- Die Rastervariante folgt denselben Spaltenschwellen wie [grid-view](../grid-view/);
  die Listenvariante bleibt einspaltig.
- Wechselt die Seite, wird der Listenanfang im `scroll-area` nach oben gesetzt;
  neue Einträge erscheinen mit `fade-in`.
