# Scale Out

## Beschreibung

Scale Out schrumpft ein Element von 100 % auf 0 %, bis es vollständig verschwunden ist. Der
Schrumpfpunkt liegt meist in der Mitte. Er kann aber auf den Auslöser gesetzt werden, um den
Zusammenhang mit der Geste zu zeigen.

## Verwendung

- Dialoge, Menüs und Popovers schließen
- einen Toast oder eine Benachrichtigung entfernen
- einen Listeneintrag oder Chip löschen
- einen Badge nach der Interaktion ausblenden
- das Element an einen anderen Ort übergeben („das Element fliegt in den Warenkorb“)
- einen Chip entfernen, wenn die Auswahl endet

## Dauer

- Typisch: 120–250 ms
- Standardwert: 180 ms

## Unterschied zu Fade Out

- Fade Out: nur die Deckkraft sinkt, das Element behält seine Größe und damit vorerst
  seinen Platz im Layout
- Zoom Out: endet bei einem Zwischenwert und nutzt Perspektive; das Element wirkt, als
  wandere es in die Tiefe
- Scale Out: endet genau bei 0 %, das Element zieht sich auf einen einzigen Punkt zusammen
