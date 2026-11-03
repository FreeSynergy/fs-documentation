# Whiteboard - Appearance

## Base layout
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

## Variants

| Variant | Appearance |
| ---------- | ---------- |
| **zeichnung** | Werkzeuge Stift und Radierer, freie Striche |
| **formen** | Werkzeugkasten mit Figuren und Verbindern |
| **notizen** | Karten auf der Fläche, farbige Zettel |
| **vorlage** | vorgezeichnete Flächen, Spalten und Ablaufschienen |

## Sizes

| Size | Width/height | Use |
| ------- | ------------- | ------------ |
| Small | 400x300px | Inline |
| Medium | 600x400px | Standard |
| Large | 800x600px | Featured |
| Full | 100% | Volle Breite |

## Colours and states

| State | Colour | Description |
| -------- | ------- | -------------- |
| **Background** | Weiß/Grün | Hintergrund |
| **Pencil** | Schwarz | Stift |
| **Shapes** | Farbig | Formen |
| **Text** | Schrift | Text |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `scale` | Vergrößerung |
| `shadow` | stronger shadow |

## Responsive

- `Full` füllt den Viewport abzüglich Werkzeugleiste; sonst wächst die Fläche mit dem Inhalt
  und der Ausschnitt scrollt.
- Die Werkzeugleiste bleibt beim Scrollen erreichbar; auf schmalen Bildschirmen rutscht sie
  nach unten und die Knöpfe bleiben mindestens 44 px groß.
- `pinch`/`spread` ändern den Maßstab, `drag` verschiebt die Fläche; die Linienstärke bleibt
  gleich, die Striche werden nicht dicker.

## Toolbar-Buttons

| Button | Function |
| -------- | ---------- |
| **Pencil** | Stift |
| **Eraser** | Radiergummi |
| **Shapes** | Formen |
| **Text** | Text |
| **Color** | Colour |
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
