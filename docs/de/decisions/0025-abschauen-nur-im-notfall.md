# 0025 – Abschauen nur im äußersten Notfall, nie bei Closed Source

Status: akzeptiert (2026-11-05) · ergänzt ADR 0013

## Entscheidung
- Grundsatz bleibt: **nichts kopieren** (ADR 0013).
- **Nur im äußersten Notfall** — wenn eine Funktion anders nicht in vertretbarer Zeit zu bauen
  ist — darf Code aus **offenen** Projekten übernommen werden. **Nie aus Closed Source.**
- Dann: **ganze Dateien**, **Original-Lizenz und Urheber bleiben im Dateikopf** (z. B. MPL-2.0 gilt
  dateiweise weiter), Eintrag in `NOTICE` im Repo, Hinweis im Commit. Nie still einbauen.
- Jeder Fall wird vorher mit dem Nutzer abgestimmt.
