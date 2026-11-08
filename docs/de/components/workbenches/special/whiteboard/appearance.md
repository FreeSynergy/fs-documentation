# Whiteboard – Aussehen

## Grundlayout
Ein Whiteboard ist eine Zeichenfläche für die Zusammenarbeit.

```
┌─────────────────────────────────────────┐
│ [Pencil] [Eraser] [Shapes] [Text]       │  ← Werkzeugleiste
├─────────────────────────────────────────┤
│                                         │
│      🖌️                                  │
│      Whiteboard-Fläche                  │
│                                         │
│      (Zeichenbereich)                   │
│                                         │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **zeichnung** | Stift- und Radiergummi-Werkzeuge, freie Striche |
| **formen** | Werkzeugkasten mit Figuren und Verbindern |
| **notizen** | Karten auf der Fläche, farbige Notizen |
| **vorlage** | vorgezeichnete Flächen, Spalten und Swimlanes |

## Größen

| Größe | Breite/Höhe | Verwendung |
|-------|-------------|------------|
| Small | 400x300px | inline |
| Medium | 600x400px | Standard |
| Large | 800x600px | hervorgehoben |
| Full | 100% | volle Breite |

## Farben und Zustände

| Zustand | Farbe | Beschreibung |
|---------|-------|--------------|
| **Hintergrund** | weiß/grün | Hintergrund |
| **Stift** | schwarz | Stift |
| **Formen** | farbig | Formen |
| **Text** | Schrift | Text |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Vergrößerung |
| `shadow` | stärkerer Schatten |

## Responsiv

- `Full` füllt den Anzeigebereich abzüglich der Werkzeugleiste; sonst wächst die Fläche mit dem Inhalt
  und der Anzeigebereich scrollt.
- Die Werkzeugleiste bleibt beim Scrollen erreichbar; auf schmalen Bildschirmen wandert sie nach unten,
  und die Buttons bleiben mindestens 44 px groß.
- `pinch`/`spread` ändern die Skalierung, `drag` verschiebt die Fläche; die Strichstärke bleibt
  gleich, die Striche werden nicht dicker.

## Werkzeugleisten-Buttons

| Button | Funktion |
|--------|----------|
| **Pencil** | Stift |
| **Eraser** | Radiergummi |
| **Shapes** | Formen |
| **Text** | Text |
| **Color** | Farbe |
| **Clear** | alles löschen |
| **Export** | Export |

## Rasterhintergrund

```
┌─────────────────────────────────────────┐
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─               │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─               │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─               │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─               │
└─────────────────────────────────────────┘
```
