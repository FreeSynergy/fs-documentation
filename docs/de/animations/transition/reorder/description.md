# Reorder

## Beschreibung

Reorder lässt Listenelemente weich ihre Plätze tauschen, wenn sich ihre Reihenfolge ändert – nach Ziehen, Sortieren oder Filtern. Die alte und die neue Position werden gemessen, dann wandert jedes Element auf dem kürzesten Weg dorthin (FLIP-Prinzip: First Last Invert Play). Andere Elemente rücken mit, statt abrupt zu springen.

## Verwendung

- Ziehen und Ablegen in Listen, siehe [drag](../../../gestures/drag/description.md)
- Sortieren nach Datum, Name oder Priorität
- Filter setzen: herausgefilterte Elemente verschwinden, die übrigen rücken nach
- Aufgaben in einer anderen Spalte oder Gruppe einordnen
- Kanban- und Board-Ansichten, siehe [board](../../../components/special/index.md)
- Anhänge und Bilder in einer Galerie neu anordnen

## Dauer

- Typisch: 250–400 ms
- Kurze Strecken (Nachbarn tauschen): 200–250 ms
- Viele Elemente gleichzeitig: 300 ms und Bewegung auf die sichtbaren beschränken

## Unterschied zu Stagger und Rubber Band

- Stagger verschiebt nur die Startzeitpunkte einer Animation; Reorder animiert die tatsächliche Positionsänderung der Elemente.
- Rubber Band federt während des Ziehens an einer Grenze zurück; Reorder wirkt erst nach dem Loslassen, wenn die neue Reihenfolge feststeht.
