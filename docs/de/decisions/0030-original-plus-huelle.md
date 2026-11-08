# 0030 – Original + Hülle: Empfangenes wird unverändert aufbewahrt

Status: akzeptiert (2026-11-05) · gilt, bis ein Fehler darin gefunden wird · ergänzt ADR 0020

## Entscheidung
- Was von außen kommt (E-Mail als MIME, Matrix-Event, MIMI-Nachricht, Kalendereinladung per iTIP,
  vCard-Import, …), wird **so gespeichert, wie es ankam** — das *Original*.
- Daneben steht die **einheitliche AS2-Hülle** mit den Feldern, die wir zum Suchen, Anzeigen und
  Verknüpfen brauchen (ADR 0020).
- Das Original wird **nie umgeschrieben**; Signaturen bleiben prüfbar, nichts geht beim Umwandeln
  verloren, ein besserer Umwandler kann später neu ableiten.

## Folgen
- Jede Domäne beschreibt in `data/<domain>/technical.md`: Original-Format, Hülle, extrahierte Felder.
- Speicherbedarf steigt (Original + Felder) — bewusst in Kauf genommen.
