# Tipp-Gesten (tap)

Tipp-Gesten sind kurze Berührungen **ohne zurückgelegten Weg**: Entscheidend
sind Kontakt, Zeit oder Druck – nicht eine Bewegung.

Die vier Basisgesten sind multipointfähig: Sie funktionieren mit beliebig
vielen Fingern bis zur Gerätegrenze (erkannt am Mittelpunkt aller Zeiger).
Die Multi-Finger-Varianten verlangen per Definition zwei oder mehr Finger –
ihre Anzahl ist eine Einstellung (`pointerCount`), kein eigener Gestetyp.

## Elemente

- **tap** - kurze Berührung (Auswahl, Klick)
- **double-tap** - zwei schnelle Berührungen (Zoom, Öffnen)
- **long-press** - lange Berührung (Kontextmenü, Markierung)
- **force-press** - Druck über Drucksensor (Peek & Pop)
- **multi-finger-tap** - Tippen mit zwei oder mehr Fingern (Sekundäraktion)
- **multi-finger-long-press** - Langdruck mit zwei oder mehr Fingern (Sekundär-Menü, Multiselect)

## Zuordnung

| Situation | Geste |
|-----------|-------|
| Element auswählen / Button auslösen | tap |
| Öffnen oder Zoomen per Doppeltipp | double-tap |
| Kontextmenü | long-press (oder force-press, wo verfügbar) |
| Sekundäraktion ohne Rechte-Maustaste | multi-finger-tap |
| Multiselect / Sekundär-Menü mit Halten | multi-finger-long-press |

## Barrierefreiheit

Die vier Basisgesten sind mit einem wie mit mehreren Fingern ausführbar; die
Multi-Finger-Varianten brauchen nach WCAG 2.5.1 eine Ein-Finger-Alternative
(long-press oder Button). Force Press ist ohne Drucksensor nicht verfügbar – immer ein
Long-Press-Fallback vorsehen.

## Siehe auch

- [Gesten Übersicht](../index.md)
- [Swipe](../swipe/swipe/description.md) - Wischen statt Tippen
- [Press-Animation](../../animations/feedback/press/description.md) - Antwort auf Druck
