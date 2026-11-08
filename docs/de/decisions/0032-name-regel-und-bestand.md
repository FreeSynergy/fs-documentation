# 0032 – name-Regel; Beschlossenes bleibt

Status: akzeptiert (2026-11-05) · löst `data/standards.md` offene Entscheidung 1

## Entscheidung
1. **name-Regel:** Fachstandards behalten ihre Feldnamen (`title` in JSCalendar, `name.full` in
   JSContact, Betreff in Mails). Die **AS2-Hülle hat immer `name`**, abgeleitet aus dem Inhalt.
   Nichts wird umbenannt; programmübergreifende Ansichten lesen nur die Hülle.
2. **Was beschlossen ist, bleibt so** (Nutzer, 2026-11-05). Wir halten uns an die Vorgaben. Stellt
   sich ein Beschluss als falsch heraus, war die Idee nicht in Ordnung — dann gibt es einen neuen ADR,
   der den alten ausdrücklich ersetzt; nie stilles Abweichen.
