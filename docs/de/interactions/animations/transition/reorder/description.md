# Reorder

## Beschreibung

Reorder lässt Listenelemente ihre Plätze weich tauschen, wenn sich ihre Reihenfolge ändert – nach dem Ziehen, Sortieren oder Filtern. Die alte und die neue Position werden gemessen. Danach wandert jedes Element den kürzesten Weg dorthin (das FLIP-Prinzip: First, Last, Invert, Play). Andere Elemente bewegen sich mit, statt abrupt zu springen.

## Verwendung

- Drag and Drop in Listen, siehe [Drag](../../../gestures/swipe/drag/description.md)
- Sortieren nach Datum, Name oder Priorität
- Filter setzen: herausgefilterte Elemente verschwinden, der Rest rückt nach oben
- Aufgaben in eine andere Spalte oder Gruppe einordnen
- Kanban- und Board-Ansichten, siehe [list-view](../../../../components/widgets/data/index.md)
- Anhänge und Bilder in einer Galerie umordnen

## Dauer

- Typisch: 250–400 ms
- Kurze Wege (Nachbarn tauschen): 200–250 ms
- Viele Elemente gleichzeitig: 300 ms, und die Bewegung auf die sichtbaren beschränken

## Unterschied zu Stagger und Rubber Band

- Stagger verschiebt nur die Startzeiten einer Animation. Reorder animiert die tatsächliche Positionsänderung der Elemente.
- Rubber Band federt beim Ziehen an einer Grenze zurück. Reorder wirkt erst nach dem Loslassen, wenn die neue Reihenfolge feststeht.
