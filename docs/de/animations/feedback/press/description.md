# Press

## Beschreibung

Press senkt ein Element beim Drücken minimal ab (`scale` etwa 0.97) und hebt die Deckkraft oder den Schatten leicht an. Beim Loslassen federt es in die Ausgangslage zurück. Die Animation ist bewusst kaum sichtbar – sie bestätigt den Berührungspunkt, ohne die Aufmerksamkeit vom Inhalt zu ziehen.

## Verwendung

- Buttons, Icons und Chips bei gedrückter Taste oder Finger
- Karten und Zeilen, die beim Antippen aktivierbar sind, siehe [card](../../../components/containers/card/description.md)
- Tasten einer Werkzeugleiste und Segmentsteuerungen
- Umschalten von Schaltern (zusätzlich zum Zustandswechsel)
- Touchscreens, wo es keinen Hover-Zustand gibt
- Bedienelemente auf einer Tastatur, wenn die Leertaste oder Eingabe gehalten wird

## Dauer

- Typisch: 100–150 ms für das Absteigen, 120–180 ms für die Rückkehr
- Halten: Endzustand bleibt bis zum Loslassen stehen
- Nicht länger als 200 ms – sonst wirkt das Element träge

## Unterschied zu Ripple und Elastic

- Ripple zeichnet eine Welle vom Berührungspunkt und läuft nach dem Loslassen aus; Press verändert das ganze Element nur, solange gedrückt wird.
- Elastic überschießt nach einer Bewegung über die Endposition; Press bewegt sich innerhalb der Endposition nach innen.
