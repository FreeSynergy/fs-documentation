# Pol.is - Funktionen

## Hauptfunktionen

- **Massen-Deliberation**: tausende Teilnehmer, Kommentare + paarweise Bewertung; PCA-Clustering zeigt Meinungsgruppen (A/B/C…) und **Konsensaussagen** (gruppenübergreifend Zustimmung)
- **Trivia-Fragen** (Mehrfachauswahl) färben Cluster (z.B. nach District)
- Live-Meinungskarte + „was ist noch neu“-Kartenstapel
- Moderation: Merge/Flag/Sperren, Featured comments
- Ergebnisse exportierbar; Multiplikatoren-Berichte für Verwaltung

## Was Pol.is NICHT kann

- **keine Anträge/Beschlüsse** (Meinungsbild ≠ Entscheidung)
- keine delegierten Stimmen
- **Data API read-only**; Schreiben nur über Teilnehmer-Aktionen (Embed)
- Moderations-Intelligenz braucht Aufsicht (Trolling trotz Clustering möglich)
- Betrieb nur beim Anbieter (pol.is) — kein Self-Hosting der gehosteten Gespräche (Open-Source-Code vorhanden, aber Eigenbetrieb erfordert Dev-Work)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Embed (iframe/js) in eigene Seiten | offiziell |
| Data API (`developers.pol.is`, JSON) | Auswertung/Dashboards |
| Import von Kommentaren (Organisator) | API/Upload (Zugangsanfrage) |
