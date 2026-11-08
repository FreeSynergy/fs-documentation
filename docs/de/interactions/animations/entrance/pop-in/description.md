# Pop In

## Beschreibung

Pop In blendet ein Element gleichzeitig über die Deckkraft und über seine Größe ein. Dabei
schießt es kurz über die endgültige Größe hinaus (ein Überschwingen von etwa 5 %). Das Element
wirkt dadurch prall und eindeutig „abgesetzt“, ohne dass sich Nachbarelemente im Layout bewegen.

## Verwendung

- Chips und Filtermarken hinzufügen, wenn der Nutzer etwas auswählt
- einen Avatar in eine Teilnehmer- oder Kommentatorenliste einfügen
- einen Zähler-Badge auf einem Icon erscheinen lassen (neue Nachricht)
- ein Häkchen bei einer Auswahl in Karten und Listen „hineinspringen“ lassen
- Pins und Marker auf einer Karte absetzen
- Onboarding-Elemente, die deutlich, aber kurz auftauchen sollen

## Dauer

- Typisch: 200–300 ms
- Mikro (Badge, Zähler, Häkchen): 150–200 ms
- Aufmerksamkeit (Onboarding-Pin): 300–400 ms

## Unterschied zu Scale In

- Scale In wächst genau von 0 % auf 100 % und ändert die Deckkraft nicht; Pop In beginnt
  teilweise transparent und schießt kurz über 100 % hinaus.
- Scale In endet ohne Bewegung; Pop In landet mit einem kurzen Zurückfedern, das den
  Endzustand betont.
