# Stagger

## Beschreibung

Stagger ist keine eigene Bewegung, sondern übernimmt die Zeitsteuerung der Kind-Animationen, indem pro Index ein fester Offset addiert wird (Element 0 startet bei 0 ms, Element 1 bei `offsetProElement`, Element 2 beim Doppelten).
Welche Animation die Kinder ausführen – Fade, Slide, Scale –, bleibt deren eigene Entscheidung.
Der Effekt entsteht allein durch die Verschiebung der Startzeitpunkte.

## Verwendung

- Listenzeilen nacheinander beim Öffnen einfliegen lassen
- Karten eines Dashboards gestaffelt einblenden
- Menüeinträge beim Aufklappen kaskadieren
- Foto-Raster zeilenweise erscheinen lassen
- Ausgang umgekehrt: Kinder verschwinden in gegenläufiger Reihenfolge
- Formulare bauen ihre Felder Reihe für Reihe auf

## Dauer

- Typisch: 30–80 ms Offset pro Element (Gesamt = Animationsdauer + Offset × Anzahl)

## Unterschied zu Parallax und Delay

- Parallax: Ebenen unterscheiden sich in der Geschwindigkeit ihrer Bewegung;
  Stagger verschiebt nur den Startzeitpunkt, die Bewegung bleibt gleich.
- Delay: Eine einzelne, feste Wartezeit für eine Animation; Stagger berechnet
  den Versatz je Elementindex (auch umgekehrt oder zufällig möglich).
