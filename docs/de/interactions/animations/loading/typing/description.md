# Typing

## Beschreibung

Typing ist der Tipp-Indikator: Drei Punkte (oder Balken) bewegen sich wellenförmig und zeigen an, dass ein Chat-Partner gerade schreibt.
Der Indikator erscheint meist in einer kleinen Sprechblase oberhalb des Eingabefelds.
Er verschwindet, sobald die Nachricht gesendet oder das Tippen beendet ist.

## Verwendung

- Chats: der Antwortpartner tippt gerade
- Assistenten- und KI-Antworten („denkt nach“)
- Kommentarspalten und Foren
- Gruppenchats mit mehreren Schreibenden (mehrere Indikatoren)
- Warteanzeige in Dialogen bei verzögerter Antwort

## Dauer

- Typisch: 1000–1400 ms pro Zyklus (Loop, solange getippt wird)

## Unterschied zu Pulse und Glow

- Pulse: Ein einzelnes Element schwillt als Ganzes an und ab; Typing ist eine
  Wanderwelle mehrerer kleiner Punkte.
- Glow: Statussignal als Leuchten um eine Kontur; Typing kündigt eine konkrete
  nächste Aktion an (eine eingehende Nachricht).
