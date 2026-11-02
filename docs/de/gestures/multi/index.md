# Mehrfinger-Gesten (multi)

Mehrfinger-Gesten verwenden zwei oder mehr Finger gleichzeitig
(Multitouch). Sie transformieren meist Inhalt (Zoom, Rotation) statt zu
navigieren.

## Anzahl ist Konfiguration, kein Gestetyp

Jede Geste dieser Familie arbeitet **ab zwei Zeigern** und ist unabhängig
davon, ob mit zwei, drei oder fünf Fingern gearbeitet wird: strecken (spread)
funktioniert mit fünf Fingern, drehen (rotate) mit drei, der Mehrfinger-Wisch
auch mit zwei. Erkannt wird aus Distanz, Winkel und Bewegung der Zeiger –
nicht aus ihrer Zahl. Die Mindestanzahl stellt `pointerCount` ein.

Der **Single-Point ist ausgeschlossen**: mit einem einzigen Zeiger existieren
weder Abstand noch Winkel, deshalb sind pinch, spread und rotate wie auch die
Mehrfinger-Varianten mit einem Finger physikalisch nicht ausführbar. Nach oben
gilt wie bei allen Gesten die Gerätegrenze (typisch fünf bis zehn Finger).

Eine weitere Zähl-Stufe erzeugt deshalb **keine neue Geste**: „Drei-Finger-
Wisch“ und „Vier-Finger-Wisch“ sind derselbe multi-finger-swipe mit anderem
`pointerCount`. Neue Gesten entstehen nur durch neues Verhalten (neue Richtung,
neue Aktion, neuer Sensor), nicht durch zusätzliche Finger.

## Elemente

- **pinch** - Zeiger ziehen sich zusammen (Zoom out), ab zwei Fingern
- **spread** - Zeiger ziehen sich auseinander (Zoom in), ab zwei Fingern
- **rotate** - Zeiger drehen um einen Mittelpunkt (Rotieren), ab zwei Fingern
- **multi-finger-tap** - Berührung mit mehreren Fingern (Sekundäraktion)
- **multi-finger-long-press** - langer Druck mit mehreren Fingern (Sekundär-Menü, Multiselect)
- **multi-finger-swipe** - Wischen mit mehreren Fingern (Systemnavigation)

## Zuordnung

| Situation | Geste |
|-----------|-------|
| Inhalt verkleinern | pinch |
| Inhalt vergrößern | spread |
| Objekt drehen | rotate |
| Rechte Maustaste ersetzen | multi-finger-tap, multi-finger-long-press |
| App-/Desktop-Wechsel | multi-finger-swipe |

## Fingeranzahl

| Geste | Default `pointerCount` | Funktioniert ebenso mit | Single-Point |
|-------|------------------------|-------------------------|------------|
| pinch / spread / rotate | 2 | 3, 4, 5 … Fingern (Gerätegrenze) | ✗ |
| multi-finger-tap / multi-finger-long-press | 2 | 3, 4, 5 … Fingern (Gerätegrenze) | ✗ |
| multi-finger-swipe | 3 | 2 oder 4 Fingern | ✗ |

## Barrierefreiheit

Mehrpunkt-Gesten sind nach WCAG 2.5.1 (Pointer Gestures) nur zulässig, wenn
eine gleichwertige Ein-Finger-Bedienung existiert (Buttons, Slider, Menü).
`pinch`/`spread` brauchen immer eine Zoom-Steuerung, `rotate` einen
Dreh-Regler oder Eingabefeld.

## Siehe auch

- [Gesten Übersicht](../index.md)
- [Ein-Finger-Gesten](../single/) - Einzelalternative zu allen hier
- [Transformationen](../../animations/transition/) - visuelle Antwort auf Rotate & Zoom
