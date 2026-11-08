# Transformations-Gesten (transform)

Transformations-Gesten bewegen **zwei oder mehr Zeiger relativ zueinander**: Die
Entfernung oder der Winkel der Zeiger verändert den Inhalt (Zoom, Drehung).

Ein Einzelpunkt ist hier unmöglich – Abstand und Winkel gibt es erst ab zwei
Zeigern. Die genaue Fingerzahl ist eine Einstellung (`pointerCount`), nach oben
begrenzt durch das Gerät: Auseinanderziehen mit fünf Fingern ist dieselbe Geste wie mit
zwei.

## Elemente

- **pinch** – Zeiger bewegen sich aufeinander zu (verkleinern)
- **spread** – Zeiger bewegen sich auseinander (vergrößern)
- **rotate** – Zeiger drehen sich um einen Mittelpunkt (Drehung)

## Zuordnung

| Situation | Geste |
|-----------|---------|
| Inhalt verkleinern | pinch |
| Inhalt vergrößern | spread |
| Drehen (Karten, Bilder, Canvas) | rotate |

## Barrierefreiheit

Nach WCAG 2.5.1 braucht jede Transformation eine Ein-Zeiger-Alternative (Zoom-
Knöpfe, Drehgriff, Schieberegler). Das Browser-Pinch-Zoom über
`touch-action` steuerbar halten.

## Siehe auch

- [Gesten-Übersicht](../index.md)
- [Zoom-in-Animation](../../animations/entrance/zoom-in/description.md) – Antwort auf Zoom-Gesten
- [Rotate-Animation](../../animations/transition/rotate/description.md) – Antwort auf Drehgesten
