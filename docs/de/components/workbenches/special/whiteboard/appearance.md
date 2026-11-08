# Whiteboard – Erscheinungsbild

## Grundlayout
Ein Whiteboard ist eine Zeichenfläche für die Zusammenarbeit.

```
┌─────────────────────────────────────────┐
│ [Stift] [Radierer] [Formen] [Text]      │  ← Werkzeugleiste
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

| Variante | Erscheinungsbild |
|---------|------------|
| **zeichnung** | Stift- und Radierwerkzeug, freie Striche |
| **formen** | Werkzeugkasten mit Figuren und Verbindern |
| **notizen** | Karten auf der Fläche, farbige Notizen |
| **vorlage** | vorbereitete Flächen, Spalten und Swimlanes |

## Größen

| Größe | Breite/Höhe | Verwendung |
|------|--------------|-------------|
| Klein | 400x300px | im Textfluss |
| Mittel | 600x400px | Standard |
| Groß | 800x600px | hervorgehoben |
| Voll | 100% | volle Breite |

## Farben und Zustände

| Zustand | Farbe | Beschreibung |
|--------------|-------------|----------------------|
| **Hintergrund** | weiß/grün | Hintergrund |
| **Stift** | schwarz | Stift |
| **Formen** | farbig | Formen |
| **Text** | Schrift | Text |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|-------------|
| `scale` | Vergrößerung |
| `shadow` | stärkerer Schatten |

## Responsiv

- `Voll` füllt den Viewport abzüglich der Werkzeugleiste; sonst wächst die Fläche mit dem Inhalt
  und der Viewport scrollt.
- Die Werkzeugleiste bleibt beim Scrollen erreichbar; auf schmalen Bildschirmen wandert sie nach unten, und die
  Knöpfe bleiben mindestens 44 px groß.
- `pinch`/`spread` ändern die Skalierung, `drag` verschiebt die Fläche; die Strichstärke bleibt
  gleich, die Striche werden nicht dicker.

## Werkzeugleisten-Knöpfe

| Knopf | Funktion |
|--------|----------|
| **Stift** | Stift |
| **Radierer** | Radierer |
| **Formen** | Formen |
| **Text** | Text |
| **Farbe** | Farbe |
| **Leeren** | alles löschen |
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
