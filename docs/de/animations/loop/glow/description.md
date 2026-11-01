# Glow

## Beschreibung

Glow legt ein weiches, farbiges Leuchten um die Kontur eines Elements.
Der Schein kann konstant stehen oder langsam an- und abschwellen.
Das Element selbst bleibt unbewegt – nur seine Umgebung leuchtet.

## Verwendung

- Auswahl im Editor: das markierte Element leuchtet dauerhaft
- Live-Status: Aufnahme, Streaming oder Verbindung sind aktiv
- Präsenz-Anzeige: ein Kontakt oder Cursor ist gerade aktiv
- Onboarding: ein Bedienelement wird sanft hervorgehoben
- Dashboards: die aktive Datenquelle bleibt sichtbar markiert
- Auswahllisten: die aktive Karte hebt sich ohne harten Rahmen ab

## Dauer

- Typisch: 1000–2000 ms pro Zyklus (Endlos-Loop), Ein-/Ausstieg 200–400 ms

## Unterschied zu Pulse und Highlight

- Pulse: Der ganze Körper des Elements schwillt an und ab; Glow bewegt nichts,
  sondern verändert ausschließlich das Leuchten rund um die Kontur.
- Highlight: Ein einmaliges, kurzes Aufleuchten des Hintergrunds (z. B. für eine
  Fundstelle); Glow dauert an, solange der Status (Auswahl, Live) besteht.
