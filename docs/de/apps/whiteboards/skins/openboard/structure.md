# OpenBoard - Struktur und UI/UX

## Seitenstruktur

```
┌──────────────────────────────────────────────────────────────────┐
│ Werkzeugbogen links │   Vollbild-Tafelseite (Seite 3/8)          │
│ ✏️🖍 🧽 ▢◯  T 🌐 📄 │                                            │
│ 📏📐 ⏱ 🎥 🗂       │     handschriftliche Elemente, Bilder,     │
│ (ausklappbar)      │     Textfelder, eingebettete PDFs          │
│                    │                                            │
│ Bibliothek (unten, einklappbar: Medien/Stacks/Dokumente)         │
│ Seitenreiter: ‹ 1 2 3 4 ›  + neue Seite                          │
└──────────────────────────────────────────────────────────────────┘
```

- Vollbild ohne Menüleiste; Werkzeugbögen klappen seitlich aus (Touch-Logik)

## UI/UX

- große, handschuh-/stifttaugliche Bedienelemente; dunkle Seitenhintergrund-Option (Beamer-Kontrast)
- Seitenwechsel wie Blättern, Presentation-Modus blendet UI aus

## Interaktionen

- Stift/Touch/Multitouch (Zoomen mit Fingern, Handflächen-Radiergummi je Gerätetreiber)
- Elemente mit Auswahlrahmen bewegen/skalieren; Gruppen („Stacks“)

## Responsive Design

entfällt (Desktop-/Whiteboard-Anwendung; mehrere Seitenformate)

## Accessibility

- Tastatursteuerung elementar (Shortcuts unten); primär Stift-/Touch-Bedienung — Screenreader nicht Kernziel

## Performance

- große Medienlast (Video) ruckelt auf alter Whiteboard-Hardware; PDF-Betten schlank halten
