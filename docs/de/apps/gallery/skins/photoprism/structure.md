# PhotoPrism - Struktur und UI/UX

## Oberfläche

```
┌──────────────────────────────────────────────────────────────────────┐
│ 🔍 Suche + Filterchips (Label, Person, Ort, Zeitraum)   ⚙  ☰  Avatar│
├──────────┬───────────────────────────────────────────────────────────┤
│ Seiten-  │  Mosaik (virtuell, Größen je Zoom)                        │
│ leiste   │  ┌────┐┌────┐┌────┐┌────┐                                 │
│ Suche    │  └────┘└────┘└────┘└────┘   Auswahl: Häkchen + Toolbar    │
│ Alben    │  ┌────┐┌────┐┌────┐┌────┐                                 │
│ Ordner   │  └────┘└────┘└────┘└────┘                                 │
│ Label    ├───────────────────────────────────────────────────────────┤
│ Gesichter│ Detail-Panel rechts: Vorschau, EXIF, Label, Album, Teilen │
└──────────┴───────────────────────────────────────────────────────────┘
```

- Zwei Modi: Mosaik (Kompaktansicht) und Listen-/Ordneransicht
- Detail-Panel öffnet rechts, Vollbild-Viewer mit `Esc`

## UI/UX

- Helle und dunkle Oberfläche, einstellbare Kachelgröße und Sortierung
- Filter als Chips über der Liste, jederzeit einzeln entfernbar
- Auswahl-Toolbar erscheint beim ersten Häkchen

## Interaktionen

- **Klick auf Label/Person** setzt den entsprechenden Suchfilter
- **Drag & Drop** von Dateien auf einen Ordner/Album (= Upload)
- **Teilen-Dialog**: Link mit Passwort, Ablauf, Download-Recht, Wasserzeichen (Plus)
- **Animationen**: dezente Übergänge beim Filtern, Skeleton-Kacheln beim Laden

## Responsive Design

| Breite | Verhalten |
|--------|-----------|
| Desktop | Seitenleiste + Mosaik + Detail-Panel |
| Tablet | Seitenleiste als Drawer, Detail als Overlay |
| Mobil | untere Navigation, einspaltiges Mosaik |

## Accessibility

- Tastatursteuerung im Viewer (`Esc`, Pfeile), Fokus-Sichtbarkeit in Kacheln
- Alt-Texte aus Label-Vorschlägen, Beschriftungen statt reiner Symbolfarben
- Screenreader: Live-Region bei Trefferzahl-Änderung

## Performance

- Index-Update inkrementell; Suche aus Datenbank plus Vektoren
- Vorschaustufen werden serverseitig gecacht, große Sammlungen virtualisiert
