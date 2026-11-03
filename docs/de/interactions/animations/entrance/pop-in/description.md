# Pop In

## Beschreibung

Pop In blendet ein Element gleichzeitig über die Deckkraft und über seine Größe ein und lässt es dabei kurz über die Endgröße hinausschießen (Overshoot von etwa 5 %). Das Element wirkt dadurch prall und eindeutig „gesetzt“, ohne dass benachbarte Elemente im Layout wandern.

## Verwendung

- Chips und Filterlabels hinzufügen, wenn der Nutzer eine Auswahl trifft
- Avatar in eine Teilnehmer- oder Kommentatorenliste einfügen
- Zähler-Badge an einem Icon erscheinen lassen (neue Nachricht)
- Auswahlhaken in Karten und Listen „hineinspringen“ lassen
- Pins und Markierungen auf einer Karte ablegen
- Onboarding-Elemente, die deutlich, aber kurz auftreten sollen

## Dauer

- Typisch: 200–300 ms
- Mikro (Badge, Zähler, Haken): 150–200 ms
- Aufmerksam (Onboarding-Pin): 300–400 ms

## Unterschied zu Scale In

- Scale In wächst exakt von 0 % auf 100 % und ändert die Deckkraft nicht; Pop In startet teils transparent und überschießt kurz über 100 %.
- Scale In endet bewegungslos; Pop In landet mit einer kurzen Rückfederung, die den Endzustand betont.
