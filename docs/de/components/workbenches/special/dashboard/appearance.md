# Dashboard – Aussehen

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

| Variante | Aussehen |
| ---------- | ---------- |
| **vorlage** | Widgets ohne Griffpunkte, Raster nicht veränderbar |
| **anordbar** | Griffpunkt oben links, Rahmen zum Ziehen, Rasterlinien im Bearbeitungsmodus |
| **bericht** | wie `vorlage`, ohne Bearbeiten-Button, stattdessen Drucken/Aktualisieren |

## Größen

| Größe | Breite | Verwendung |
| ------- | -------- | ------------ |
| Small | 800px | kleines Dashboard |
| Medium | 1200px | Standard |
| Large | 1600px | großes Dashboard |

## Farben und Zustände

| Zustand | Farbe | Beschreibung |
| -------- | ------- | -------------- |
| **Hintergrund** | hell | Hintergrund |
| **Widget** | weiß | Hintergrund des Widgets |
| **Rahmen** | grau | Rahmen |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
| -------- | -------------- |
| `shadow` | stärkerer Schatten |
| `border` | der Rahmen leuchtet auf |

## Responsiv

- Ab 1600 px vier Spalten, ab 1200 px drei, ab 800 px zwei, darunter eine einzige
  Spalte; die gespeicherte Reihenfolge bleibt erhalten.
- Widgets behalten ihre Zeilenhöhe, solange sie in die neue Spaltenzahl passen; sonst werden
  sie höher.
- Auf Touch-Geräten beginnt das Verschieben erst nach einem langen Druck (`long-press`), die
  Nachbarn weichen mit `reorder` aus.

## Widget-Typen

| Typ | Beschreibung |
|-----|--------------|
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
