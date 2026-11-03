# Scale In

## Beschreibung

Scale In lässt ein Element von der Größe 0 % auf 100 % wachsen, ohne dass es seinen Platz im Layout verlässt. Der Wachstumspunkt (`transformOrigin`) bestimmt, aus welcher Richtung das Element zu erscheinen scheint.

## Verwendung

- Dialoge und Popovers, die beim Öffnen „aufgehen“
- Menüs und Tooltips, die aus ihrem Auslöser herauswachsen
- Badges, Chips und Zähler, die neu ins Layout kommen
- Icon-Wechsel beim Aktivieren eines Toggles
- Fokuspunkt im Onboarding (erstes neues Element)
- Popover, das aus einem Icon-Button herauswächst

## Dauer

- Typisch: 150–300 ms
- Standardwert: 200 ms

## Unterschied zu Zoom In

- Zoom In: startet meist bei einem Zwischenwert (z. B. 50–70 %) und wirkt durch zusätzliche Tiefen- bzw. Perspektivwirkung wie ein Heranfahren an das Element
- Scale In: beginnt exakt bei 0 %, arbeitet ohne Perspektive und bleibt flach in der Betrachterebene
- Bounce In: wächst ebenfalls auf 100 %, endet aber mit federndem Überschießen über die Endgröße
