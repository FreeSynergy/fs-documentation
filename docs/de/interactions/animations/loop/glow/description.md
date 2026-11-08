# Glow

## Beschreibung

Glow legt einen weichen, farbigen Schein um die Kontur eines Elements. Der Schein kann konstant stehen oder langsam anschwellen und wieder abnehmen. Das Element selbst bewegt sich nicht – nur seine Umgebung leuchtet.

## Verwendung

- Auswahl in einem Editor: das markierte Element leuchtet dauerhaft
- Live-Status: Aufnahme, Streaming oder eine aktive Verbindung
- Anwesenheitsanzeige: ein Kontakt oder Cursor ist gerade aktiv
- Onboarding: ein Bedienelement wird sanft hervorgehoben
- Dashboards: die aktive Datenquelle bleibt sichtbar markiert
- Auswahllisten: die aktive Karte hebt sich ohne harten Rahmen ab

## Dauer

- Typisch: 1000–2000 ms pro Zyklus (endlose Schleife), Ein-/Ausblenden 200–400 ms

## Unterschied zu Pulse und Highlight

- Pulse: der ganze Körper des Elements schwillt an und schrumpft. Glow bewegt nichts, es ändert nur den Schein um die Kontur.
- Highlight: ein einmaliges, kurzes Aufleuchten des Hintergrunds (z. B. für eine gefundene Textstelle). Glow hält so lange an, wie der Status (Auswahl, Live) besteht.
