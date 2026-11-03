# Scale Out

## Beschreibung

Scale Out schrumpft ein Element von 100 % auf 0 %, bis es vollständig verschwunden ist. Der Schrumpfpunkt liegt meist in der Mitte, kann aber auf den Auslöser gesetzt werden, um den Zusammenhang zur Geste zu zeigen.

## Verwendung

- Schließen von Dialogen, Menüs und Popovers
- Entfernen eines Toasts oder einer Benachrichtigung
- Löschen eines Listeneintrags oder Chips
- Ausblenden eines Badges nach der Interaktion
- Übergabe an eine andere Stelle („Element fliegt zum Warenkorb“)
- Chip wird entfernt, wenn die Auswahl endet

## Dauer

- Typisch: 120–250 ms
- Standardwert: 180 ms

## Unterschied zu Fade Out

- Fade Out: nur die Deckkraft sinkt, das Element behält seine Größe und damit zunächst seinen Layout-Platz
- Zoom Out: endet bei einem Zwischenwert und nutzt Perspektive; das Element fährt scheinbar in die Tiefe
- Scale Out: endet bei exakt 0 %, das Element zieht sich flach auf einen Punkt zusammen
