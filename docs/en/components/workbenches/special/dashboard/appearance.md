# Dashboard - Appearance

## Base layout
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

## Variants

| Variant | Appearance |
| ---------- | ---------- |
| **vorlage** | Widgets ohne Greifpunkte, Raster unveränderlich |
| **anordbar** | Greifpunkt oben links, Rahmen zum Ziehen, Rasterlinien im Bearbeiten-Modus |
| **bericht** | wie `vorlage`, ohne Bearbeiten-Knopf, dafür Drucken/Aktualisieren |

## Sizes

| Size | Width | Use |
| ------- | -------- | ------------ |
| Small | 800px | Kleines Dashboard |
| Medium | 1200px | Standard |
| Large | 1600px | Großes Dashboard |

## Colours and states

| State | Colour | Description |
| -------- | ------- | -------------- |
| **Background** | Hell | Hintergrund |
| **Widget** | Weiß | Widget-Hintergrund |
| **Border** | Grau | Rand |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `shadow` | stronger shadow |
| `border` | the border lights up |

## Responsive

- Vierte Spalten ab 1600 px, drei ab 1200 px, zwei ab 800 px, darunter einspaltig;
  die gespeicherte Reihenfolge bleibt erhalten.
- Widgets behalten ihre Zeilenspannung, soweit sie in die neue Spaltenzahl passen;
  sonst wachsen sie in die Höhe.
- Auf Touch-Geräten beginnt das Verschieben erst nach langem Drücken (`long-press`),
  die Nachbarrücken mit `reorder` zur Seite.

## Widget-Typen

| Type | Description |
| ------ | -------------- |
| **Card** | Karte |
| **Chart** | Diagramm |
| **List** | Liste |
| **Table** | Tabelle |
| **Stat** | Statistik |
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
