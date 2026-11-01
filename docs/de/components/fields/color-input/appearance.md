# Color Input - Aussehen

## Grundlayout
Ein Color Input ist ein Farbauswahl-Feld mit Farbpicker.

```
┌─────────────────────────────────────────┐
│ Farbe                                   │
├─────────────────────────────────────────┤
│  🎨 #3498db                             │
│                                         │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **palette** | Farbklappe mit Raster aus Farbflächen, kein Slider |
| **spectrum** | grosse Farbfläche, darunter Farbton- und Transparenz-Slider |
| **code** | einzeiliges Feld mit Farbklötzchen vor dem Wert |

## Varianten

| Variante | Aussehen |
|----------|----------|
| **palette** | Farbklappe mit Raster aus Farbflächen, kein Slider |
| **spectrum** | große Farbfläche, darunter Farbton- und Transparenz-Slider |
| **code** | einzeiliges Feld mit Farbklötzchen vor dem Wert |

## Größen

| Größe | Höhe | Verwendung |
|-------|------|------------|
| Small | 32px | Inline |
| Medium | 48px | Standard |
| Large | 64px | Featured |

## Farben und Zustände
| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Default** | Hell | Standard |
| **Primary** | Primärfarbe | Primär |
| **Active** | Dunkel | Aktiver Zustand |
| **Disabled** | Grau | Deaktiviert |

```
┌─────────────────────────────────────────┐
│ 🎨 #3498db                              │
├─────────────────────────────────────────┤
│  [Farben]                               │
│  🟥 🟧 🟨 🟩 🟦 🟪 ⬜ ⬛                  │
└─────────────────────────────────────────┘
```

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `border` | Rand leuchtet auf |
| `shadow` | Schatten stärker |

## Farbspektrum

```
┌─────────────────────────────────────────┐
│      🎨                                 │
│    🌈 Rainbow                           │
│                                         │
└─────────────────────────────────────────┘
```

## Reaktiv

- Das Auswahl-Overlay ist mindestens 280 px breit; auf schmalen Bildschirmen wird es
  statt unter dem Feld als bodenbündige Fläche geöffnet.
- Die Farbfläche skaliert proportional, der Slider bleibt mindestens 44 px hoch.
- Unter `small` wird die Variante `code` bevorzugt; Palette und Spektrum bleiben als
  Vollflächendialog erreichbar.

## Reaktiv

- Das Auswahl-Overlay ist mindestens 280 px breit; auf schmalen Bildschirmen wird es
  statt unter dem Feld als bodenbündige Fläche geöffnet.
- Die Farbfläche skaliert proportional, der Slider bleibt mindestens 44 px hoch.
- Unter `small` wird die Variante `code` bevorzugt; Palette und Spektrum bleiben als
  Vollflächendialog erreichbar.
