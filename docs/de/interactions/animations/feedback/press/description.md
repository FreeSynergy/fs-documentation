# Press

## Beschreibung

Press senkt ein Element beim Drücken minimal ab (`scale` um 0.97) und hebt die Deckkraft oder den
Schatten leicht an. Beim Loslassen federt es in seine Ausgangsposition zurück. Die Animation ist
bewusst kaum sichtbar: Sie bestätigt den Berührungspunkt, ohne die Aufmerksamkeit vom Inhalt
abzulenken.

## Verwendung

- Schaltflächen, Icons und Chips, solange Taste oder Finger gehalten werden
- Karten und Zeilen, die per Tippen aktiviert werden können, siehe [card](../../../../components/widgets/containers/card/description.md)
- Werkzeugleisten-Schaltflächen und Segmentsteuerungen
- Schalter beim Umlegen (zusätzlich zur Zustandsänderung)
- Touchscreens, auf denen es keinen Hover-Zustand gibt
- Bedienelemente per Tastatur, wenn Leertaste oder Eingabe gehalten werden

## Dauer

- Typisch: 100–150 ms beim Herunterdrücken, 120–180 ms bei der Rückkehr
- Halten: Der Endzustand bleibt bis zum Loslassen
- Nicht länger als 200 ms, sonst wirkt das Element träge

## Unterschied zu Ripple und Elastic

- Ripple zeichnet eine Welle vom Berührungspunkt, die nach dem Loslassen ausläuft; Press verändert
  das ganze Element nur, solange es gedrückt wird.
- Elastic schießt nach einer Bewegung über die Endposition hinaus; Press bewegt sich nach innen,
  innerhalb der Endposition.
