# Modal - Erscheinungsbild

## Grundlayout
Ein Modal ist ein Overlay-Fenster mit Fokus auf dem Inhalt.

```
┌─────────────────────────────────────────┐
│ [✕] Titel                               │
├─────────────────────────────────────────┤
│                                         │
│   Inhalt                                │
│   ...                                   │
│                                         │
├─────────────────────────────────────────┤
│  [Abbrechen]          [Speichern]       │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Größe | Beschreibung |
|----------|-------|--------------|
| **Small** | 300px | Formulare, Bestätigungen |
| **Medium** | 500px | Bearbeitungsdialoge |
| **Large** | 700px | vollständige Ansichten |
| **Fullscreen** | 100% | vollständige Ansicht |

## Größen

| Größe | Breite | Höhe | Verwendung |
|------------|--------|------|------------|
| Small | 300px | automatisch | Bestätigung, kurzer Text |
| Medium | 500px | automatisch | Standard |
| Large | 700px | automatisch | Formulare, Listen |
| Fullscreen | 100% | 100% | komplexe Ansicht |

Die Obergrenze liegt bei 85 % der Viewport-Höhe; der Inhalt scrollt, Kopf- und Fußbereich
bleiben an ihrem Platz.

## Farben und Zustände

| Zustand | Farbe | Beschreibung |
|-----------|-------|--------------|
| **Overlay** | dunkel | Hintergrund abdunkeln |
| **Kopfbereich** | hell | Titelleiste |
| **Inhalt** | hell | Inhalt |
| **Fußbereich** | hell | Aktionen |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `shadow` | stärkerer Schatten |
| `border` | der Rahmen leuchtet auf |

## Responsiv

Das Overlay liegt über der Seite, sperrt das Scrollen des Hintergrunds und hält den Fokus im
Dialog (Escape schließt, Tab wandert im Kreis innerhalb). Auf einer schmalen Fläche wird das Modal
automatisch zur Vollfläche; bei hohem Inhalt scrollt nur der Textbereich.

```css
.modal        { position: fixed; inset: 0; display: grid; place-items: center; }
.modal-panel  { width: min(500px, 92vw); max-height: 85vh;
                display: grid; grid-template-rows: auto 1fr auto; }
.modal-body   { overflow: auto; }              /* nur der Inhalt scrollt */
body.modal-open { overflow: hidden; }          /* der Hintergrund ist gesperrt */

@media (max-width: 600px) {
  .modal-panel { width: 100%; height: 100%; max-height: none; border-radius: 0; }
}
```

## Schließen-Schaltfläche

```
┌─────────────────────────────────────────┐
│ [✕] Titel                               │
├─────────────────────────────────────────┤
│                                         │
│   Inhalt                                │
│                                         │
└─────────────────────────────────────────┘
```
