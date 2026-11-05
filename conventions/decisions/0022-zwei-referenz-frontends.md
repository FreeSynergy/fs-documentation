# 0022 – Jedes Programm hat zwei Referenz-Frontends

Status: **superseded by 0038** (2026-11-05)

Status: akzeptiert (2026-11-05)

## Entscheidung
Zu jedem Programm bauen wir **zwei** Frontends: eines in der Art eines bekannten
(Closed-Source-)Vorbilds und unser eigenes. Zwei verschiedene Frontends auf demselben Vertrag
(ADR 0021) zeigen sofort, wenn die Schnittstelle bricht oder etwas nur für ein Frontend passt.
Weitere Frontends baut jeder, wie er möchte.

## Folgen
- Das Vorbild-Frontend wird aus den analysierten Frontends der Kategorie gewählt (ADR 0013);
  es bildet Funktionen und Abläufe nach, kopiert aber nichts.
