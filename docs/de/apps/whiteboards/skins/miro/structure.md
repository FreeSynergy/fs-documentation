# Miro - Struktur und UI/UX

## Seitenstruktur

```
┌──────────────────────────────────────────────────────────────────┐
│ Miro ▾   Titel…                 Seiten (1|2|3)     👥 👤 Share  │
│┌──┐                                                      ┌────┐  │
││S │        (Infinite Canvas mit Frames)                  │Sei-│  │
││R │        ┌──Frame: Retrospektive──┐                    │ten │  │
││O │        │ 🟦 Was lief gut? 🟨 …  │                    │mini│  │
││T │        │ [Sticky][Sticky]       │                    │atur│  │
││P │        └────────────────────────┘                    └────┘  │
││↗ │   Timer 🕐 · Voting ✓ · Presenter 🎥 (Moderation)            │
│└──┘                                                              │
└──────────────────────────────────────────────────────────────────┘
```

- linke vertikale Toolbar, rechte Seitenliste mit Miniaturen, Kopfzeile mit Teilnehmern/Share

## UI/UX

- poliertes helles Design, sanfte Zoom-/Pan-Übergänge, Tooltips für jedes Werkzeug
- Smart-Layout für Mindmaps/Organigramme

## Interaktionen

- **Multiplayer**: Cursor mit Namen, Auswahl-Locks, Live-Sticky-Eingaben
- **Drag & Drop**: Elemente, Frames gruppieren, Sammel-„Groups“
- **Präsentieren**: Fokussieren auf Frames, Presenter folgt Kamera-Pfad

## Responsive Design

- Web-desktopzentriert; iPad mit Pencil-Support; Mobil-App für Viewing/Kurzbearbeitung

## Accessibility

- Miro publiziert Accessibility-Roadmap/VPAT (Enterprise); Tastaturwerkzeuge: Shortcuts (siehe [shortcuts.md](shortcuts.md)), Sticky via Tastatur voll editierbar

## Performance

- Frames halten große Boards (>10k Items) bedienbar; ältere Browser schwach
