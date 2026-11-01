# Whiteboard - Aussehen

## Grundlayout
Ein Whiteboard ist eine Zeichenfläche für Kollaboration.

```
┌─────────────────────────────────────────┐
│ [Pencil] [Eraser] [Shapes] [Text]       │  ← Toolbar
├─────────────────────────────────────────┤
│                                         │
│      🖌️                                  │
│      Whiteboard-Fläche                  │
│                                         │
│      (Zeichenfläche)                    │
│                                         │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **zeichnung** | Werkzeuge Stift und Radierer, freie Striche |
| **formen** | Werkzeugkasten mit Figuren und Verbindern |
| **notizen** | Karten auf der Fläche, farbige Zettel |
| **vorlage** | vorgezeichnete Flächen, Spalten und Ablaufschienen |

## Größen

| Größe | Breite/Höhe | Verwendung |
|-------|-------------|------------|
| Small | 400x300px | Inline |
| Medium | 600x400px | Standard |
| Large | 800x600px | Featured |
| Full | 100% | Volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Background** | Weiß/Grün | Hintergrund |
| **Pencil** | Schwarz | Stift |
| **Shapes** | Farbig | Formen |
| **Text** | Schrift | Text |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Vergrößerung |
| `shadow` | Schatten stärker |

## Reaktiv

- `Full` füllt den Viewport abzüglich Werkzeugleiste; sonst wächst die Fläche mit dem Inhalt
  und der Ausschnitt scrollt.
- Die Werkzeugleiste bleibt beim Scrollen erreichbar; auf schmalen Bildschirmen rutscht sie
  nach unten und die Knöpfe bleiben mindestens 44 px groß.
- `pinch`/`spread` ändern den Maßstab, `drag` verschiebt die Fläche; die Linienstärke bleibt
  gleich, die Striche werden nicht dicker.

## Toolbar-Buttons

| Button | Funktion |
|--------|----------|
| **Pencil** | Stift |
| **Eraser** | Radiergummi |
| **Shapes** | Formen |
| **Text** | Text |
| **Color** | Farbe |
| **Clear** | Alles löschen |
| **Export** | Exportieren |

## Grid-Background

```
┌─────────────────────────────────────────┐
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─               │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─               │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─               │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─               │
└─────────────────────────────────────────┘
```
