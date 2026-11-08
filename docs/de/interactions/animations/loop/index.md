# Schleife (Loop)

Schleifen-Animationen laufen wiederholt, bis ein Zustand endet. Sie brauchen eine lange Dauer
(800–2000 ms pro Zyklus) und pausieren, sobald das Element nicht sichtbar ist.

## Elemente

- **spin** – eine dauerhafte Drehung (Lader, Aktivität)
- **pulse** – ein zyklisches Anschwellen und Schrumpfen (Aufmerksamkeit)
- **heartbeat** – ein doppelter Puls im Rhythmus eines Herzschlags
- **glow** – ein Leuchten um die Kontur (Auswahl, Live-Status)

## Abgrenzung

Dauerhafte Ladezustände mit Struktur stehen in [loading](../loading/), Bewegungen
von Ebenen stehen in [movement](../movement/).

## Verbindliche Regeln

- `iterationCount: infinite` immer an einen Zustand binden (Fortschritt, Verbindung)
- außerhalb des Sichtbereichs pausieren (`playState: paused`)
- nie zwei Schleifen-Animationen gleichzeitig im selben Sichtfeld

## Siehe auch

- [Übersicht Animationen](../index.md)
- [Laden](../loading/)
- [Rückmeldung](../feedback/) – eine einmalige Antwort statt laufender Bewegung
