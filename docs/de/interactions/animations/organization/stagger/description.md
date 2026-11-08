# Stagger

## Beschreibung

Stagger ist keine Bewegung für sich. Es übernimmt die Zeitsteuerung der Kindanimationen, indem jedem Index ein fester Versatz gegeben wird (Element 0 startet bei 0 ms, Element 1 bei `offsetProElement`, Element 2 bei dem doppelten Wert). Welche Animation die Kinder ausführen – einblenden, schieben, skalieren – bleibt ihnen überlassen. Der Effekt entsteht allein durch das Verschieben der Startzeiten.

## Verwendung

- Listenzeilen beim Öffnen nacheinander einfliegen lassen
- Karten eines Dashboards stufenweise einblenden
- Menüeinträge beim Öffnen kaskadiert erscheinen lassen
- ein Fotoraster Zeile für Zeile erscheinen lassen
- den Ausgang rückwärts: die Kinder verschwinden in umgekehrter Reihenfolge
- Formulare bauen ihre Felder Zeile für Zeile auf

## Dauer

- Typisch: 30–80 ms Versatz pro Element (gesamt = Animationsdauer + Versatz × Anzahl)

## Unterschied zu Parallax und Delay

- Parallax: Ebenen unterscheiden sich im Tempo ihrer Bewegung. Stagger verschiebt nur den Startzeitpunkt, die Bewegung bleibt gleich.
- Delay: eine einzelne, feste Wartezeit für eine Animation. Stagger berechnet den Versatz pro Elementindex (auch umgekehrt oder zufällig möglich).
