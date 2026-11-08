# Scale In

## Beschreibung

Scale In lässt ein Element von 0 % auf 100 % wachsen, ohne dass es seinen Platz im Layout verlässt. Der Wachstumspunkt (`transformOrigin`) bestimmt, aus welcher Richtung das Element zu kommen scheint.

## Verwendung

- Dialoge und Popover, die sich beim Öffnen "aufklappen"
- Menüs und Tooltips, die aus ihrem Auslöser wachsen
- Badges, Chips und Zähler, die neu ins Layout kommen
- Icon-Wechsel, wenn ein Schalter betätigt wird
- Blickpunkt im Onboarding (das erste neue Element)
- Popover, das aus einem Icon-Button wächst

## Dauer

- Typisch: 150–300 ms
- Standardwert: 200 ms

## Unterschied zu Zoom In

- Zoom In: beginnt meist bei einem Zwischenwert (z. B. 50–70 %) und wirkt durch einen zusätzlichen Tiefen- oder Perspektiveneffekt wie ein Heranfahren an das Element.
- Scale In: beginnt genau bei 0 %, kommt ohne Perspektive aus und bleibt in der Betrachterebene flach.
- Bounce In: wächst ebenfalls auf 100 %, endet aber mit einem federnden Überschwingen über die Endgröße.
