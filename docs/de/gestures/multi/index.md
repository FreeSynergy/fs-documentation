# Mehrfinger-Gesten (multi)

Mehrfinger-Gesten verwenden zwei oder mehr Finger gleichzeitig
(Multitouch). Sie transformieren meist Inhalt (Zoom, Rotation) statt zu
navigieren.

## Elemente

- **pinch** - zwei Finger zusammenziehen (Zoom out)
- **spread** - zwei Finger auseinanderziehen (Zoom in)
- **rotate** - zwei Finger drehen (Rotieren)
- **two-finger-tap** - Berührung mit zwei Fingern (Sekundäraktion)
- **two-finger-long-press** - langen Druck mit zwei Fingern (Sekundär-Menü)
- **three-finger-swipe** - Wischen mit drei Fingern (Systemnavigation)

## Zuordnung

| Situation | Geste |
|-----------|-------|
| Inhalt verkleinern | pinch |
| Inhalt vergrößern | spread |
| Objekt drehen | rotate |
| Rechte Maustaste ersetzen | two-finger-tap, two-finger-long-press |
| App-/Desktop-Wechsel | three-finger-swipe |

## Barrierefreiheit

Mehrpunkt-Gesten sind nach WCAG 2.5.1 (Pointer Gestures) nur zulässig, wenn
eine gleichwertige Ein-Finger-Bedienung existiert (Buttons, Slider, Menü).
`pinch`/`spread` brauchen immer eine Zoom-Steuerung, `rotate` einen
Dreh-Regler oder Eingabefeld.

## Siehe auch

- [Gesten Übersicht](../index.md)
- [Ein-Finger-Gesten](../single/) - Einzelalternative zu allen hier
- [Transformationen](../../animations/transition/) - visuelle Antwort auf Rotate & Zoom
