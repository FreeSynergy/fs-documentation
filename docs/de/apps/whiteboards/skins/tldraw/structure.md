# tldraw - Struktur und UI/UX

## Fensterstruktur

```
┌────────────────────────────────────────────────────────────────┐
│ tldraw ▾            Seite 1 ▾                    Share  👥     │
│                                                                │
│                         (Infinite Canvas)            ┌──────┐  │
│        ▱ ──▶  ○                                    │Stil  │  │
│      ┌─Notiz─┐        ↗                             │Farbe │  │
│      │ Idee! │      Frame                           │Füllung│  │
│      └───────┘                                     │Größe │  │
│                                                    └──────┘  │
│   ┌──────────────────────────────────────────┐               │
│   │ ↖ ✋ ⌁ ✏ ⌫ ↗ ▭ ◯ ╲ △ ☁ 🗒 T 🖼 ⬒ | ℹ︎ ♟  │  (Werkzeuge) │
│   └──────────────────────────────────────────┘               │
│ Minimap ◢                                          Zoom 100%  │
└────────────────────────────────────────────────────────────────┘
```

## UI/UX

- Radiale/untere Werkzeugleiste, schwebende Panels; Canvas ohne feste Ränder (Infinite Canvas)
- Minimalistisch, hohe Tastaturaffinität; Kontext-Menü statt überlader Menüleiste
- Dark-/Light-Mode über Preferences

## Interaktionen

- **Pan/Zoom**: Hand-Werkzeug, `Leertaste`+Ziehen, `Strg+Rad` zoomen; Zoom-Buttons unten rechts
- **Drag & Drop**: Shapes verschieben, aus Dateien/URLs Bilder/Bookmarks ziehen
- **Resize-Rotation-Handles** an Auswahl; Snap an Kanten/Frames
- **Animationen**: Auswahl-Outline „wobbles" minimal (Hand-drawn-Stil), Panels blenden; ansonsten bewusst wenige Animationen
- **Multiplayer-Cursor**: farbige Namen der Mitleser

## Responsive Design

| Kontext | Verhalten |
|---------|-----------|
| Desktop | alle Panels |
| Tablet | Werkzeugleiste kompakt, Stylus-Support (Druck) |
| Mobil | Panels überflowsicher, Zwei-Finger-Pan/Zoom |

## Accessibility

- Tastatursteuerung der Tools ist zentral (Shortcuts statt Mauszeiger-Ketten, siehe [shortcuts.md](shortcuts.md))
- Shapes sind als DOM-/SVG-Elemente mit Beschriftung exponiert; Screenreader-Support im SDK ausbaubar
- Alternativ-Text für Bilder möglich (Bookmark/Alt-Feld)

## Editor-Struktur (SDK)

- `<Tldraw/>`-Komponente mit konfigurierbaren Teilen (`Toolbar`, `StylePanel`, `MainMenu` ersetzbar)
- Store mit Records; `Editor`-API als Programmier-Schnittstelle (siehe [api.md](api.md))
