# Transformations-Gesten (transform)

Transformations-Gesten bewegen **zwei oder mehr Zeiger relativ zueinander**:
Abstand oder Winkel der Zeiger verändert den Inhalt (Zoom, Rotation).

Single-Point ist hier ausgeschlossen – Abstand und Winkel existieren erst ab
zwei Zeigern. Die genaue Fingerzahl ist eine Einstellung (`pointerCount`),
nach oben durch das Gerät begrenzt: Spread zu fünft ist dieselbe Geste wie
zu zweit.

## Elemente

- **pinch** - Zeiger zusammenziehen (Zoom out)
- **spread** - Zeiger auseinanderziehen (Zoom in)
- **rotate** - Zeiger um einen Mittelpunkt drehen (Rotation)

## Zuordnung

| Situation | Geste |
|-----------|-------|
| Inhalt verkleinern | pinch |
| Inhalt vergrößern | spread |
| Drehen (Karten, Bilder, Canvas) | rotate |

## Barrierefreiheit

Nach WCAG 2.5.1 braucht jede Transformation eine Einzeiger-Alternative
(Zoom-Buttons, Rotations-Griff, Slider). Pinch-Zoom im Browser über
`touch-action` steuerbar halten.

## Siehe auch

- [Gesten Übersicht](../index.md)
- [Zoom-In-Animation](../../animations/entrance/zoom-in/description.md) - Antwort auf Zoom-Gesten
- [Rotate-Animation](../../animations/transition/rotate/description.md) - Antwort auf Dreh-Gesten
