# Ein-Finger-Gesten (single)

Ein-Finger-Gesten werden mit genau einem Finger (oder einem einzelnen Zeiger:
Maus, Stift) ausgeführt. Sie sind die häufigste Gesten-Familie und ersetzen
weitgehend Klick-Interaktionen.

## Elemente

- **tap** - kurze Berührung (Auswahl, Klick)
- **double-tap** - zwei schnelle Berührungen (Zoom, Öffnen)
- **long-press** - lange Berührung (Kontextmenü, Markierung)
- **swipe** - Wischen in eine Richtung (Navigation, Switchen)
- **flick** - schnelles Wischen mit Abheben und Schwung (Throw-Scrolling)
- **drag** - gedrücktes Ziehen (Reorder, Scroll, Verschieben)
- **edge-swipe** - Wischen vom Bildschirmrand (Zurück, Systemleisten)
- **force-press** - fester Druck mit Drucksensor (Peek & Pop)
- **hover** - Zeiger über Element ohne Kontakt (Tooltip, Vorschau)
- **draw-gesture** - Zeichnen einer Form/Buchstabe (Verknüpfung)

## Zuordnung

| Situation | Geste |
|-----------|-------|
| Element auslösen | tap |
| Schnell öffnen/zoomen | double-tap |
| Mehr Optionen | long-press, hover |
| Seitlich wechseln | swipe, edge-swipe |
| Schwungvolles Scrollen | flick |
| Element bewegen | drag |
| Vorschau dann Öffnen | force-press |
| Verknüpfung ohne Menü | draw-gesture |

## Barrierefreiheit

Ein-Finger-Gesten sind die empfohlene **Einzelalternative** für Mehrfinger- und
Pfadgesten (WCAG 2.5.1). Pfadbasierte Gesten wie draw-gesture benötigen immer
eine Alternative aus dieser Familie.

## Siehe auch

- [Gesten Übersicht](../index.md)
- [Mehrfinger-Gesten](../multi/) - pinching, drehen, zwei Finger
- [Kombinationen](../combined/) - drag-and-drop, pull-to-refresh
