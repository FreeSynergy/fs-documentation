# Dashboard – Erscheinungsbild

## Grundlayout
Ein Dashboard ist eine Übersichtsseite mit Widgets.

```
┌─────────────────────────────────────────┐
│ [Widget 1] [Widget 2] [Widget 3]        │
│                                         │
│ [Widget 4] [Widget 5] [Widget 6]        │
│                                         │
│ [Widget 7] [Widget 8] [Widget 9]        │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
| ---------- | ---------- |
| **vorlage** | Widgets ohne Griffe, Raster nicht veränderbar |
| **anordbar** | Griff oben links, Rahmen zum Ziehen, Rasterlinien im Bearbeitungsmodus |
| **bericht** | wie `vorlage`, ohne Bearbeitungsknopf, stattdessen Drucken/Aktualisieren |

## Größen

| Größe | Breite | Verwendung |
| ------- | -------- | ------------ |
| Klein | 800px | kleines Dashboard |
| Mittel | 1200px | Standard |
| Groß | 1600px | großes Dashboard |

## Farben und Zustände

| Zustand | Farbe | Beschreibung |
| -------- | ------- | -------------- |
| **Hintergrund** | Hell | Hintergrund |
| **Widget** | Weiß | Hintergrund des Widgets |
| **Rahmen** | Grau | Rahmen |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
| -------- | -------------- |
| `shadow` | stärkerer Schatten |
| `border` | der Rahmen leuchtet auf |

## Responsiv

- Ab 1600 px vier Spalten, ab 1200 px drei, ab 800 px zwei, darunter eine einzelne Spalte; die
  gespeicherte Reihenfolge bleibt erhalten.
- Widgets behalten ihre Zeilenhöhe, solange sie in die neue Spaltenzahl passen; sonst wachsen sie in der Höhe.
- Auf Touchgeräten startet das Verschieben erst nach einem langen Druck (`long-press`), die Nachbarn weichen mit `reorder` aus.

## Widget-Typen

| Typ | Beschreibung |
|------------|-------------|
| **Card** | Karte |
| **Chart** | Diagramm |
| **List** | Liste |
| **Table** | Tabelle |
| **Stat** | Kennzahl |
| **Calendar** | Kalender |

## Drag & Drop

```
┌─────────────────────────────────────────┐
│ [Widget 1] [Widget 2] [Widget 3]        │
│      📦                                 │
│ [Widget 4] [Widget 5] [Widget 6]        │
│                                         │
│ [Widget 7] [Widget 8] [Widget 9]        │
└─────────────────────────────────────────┘
```
