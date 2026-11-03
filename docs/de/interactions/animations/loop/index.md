# Endlos (loop)

Endlos-Animationen laufen wiederholt, bis ein Zustand endet. Sie brauchen eine lange
Dauer (800–2000 ms pro Zyklus) und pausieren, sobald das Element nicht sichtbar ist.

## Elemente

- **spin** - dauerhaftes Drehen (Loader, Aktivität)
- **pulse** - zyklisches An- und Abschwellen (Aufmerksamkeit)
- **heartbeat** - doppelter Puls im Rhythmus einer Herzfrequenz
- **glow** - Leuchten um die Kontur (Auswahl, Live-Status)

## Abgrenzung

Dauerhafte Ladezustände mit Struktur stehen in [Laden (loading)](../loading/),
Bewegungen von Ebenen in [Bewegung (movement)](../movement/).

## Pflichtregeln

- `iterationCount: infinite` immer an einen Zustand binden (Fortschritt, Verbindung)
- außerhalb des Viewports pausieren (`playState: paused`)
- nie zwei Endlos-Animationen im selben Sichtfeld gleichzeitig

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Laden (loading)](../loading/)
- [Feedback (feedback)](../feedback/) - einmalige Antwort statt Dauerbetrieb
