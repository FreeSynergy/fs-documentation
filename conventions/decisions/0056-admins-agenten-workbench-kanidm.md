# 0056 – Oberster Admin; Agenten werden nie Admin; Workbench gibt Kontext; Kanidm flach

Status: akzeptiert (2026-11-06) · ergänzt ADR 0005, 0021, 0037, 0049, 0054, 0055 · öffentlich: `docs/en/programs/platform/groups.md`

## Entscheidung (Nutzer)
1. **Der Admin, der installiert, ist der oberste Admin.** In den Gruppen kann er weiteren den Admin-Status geben.
2. **Gespiegelt wird nach Option B.** Verschachtelung geht nur dorthin, wo Rechte wirklich weitergegeben werden. In unseren Gruppen ist die Weitergabe einstellbar.
   **Bei Kanidm geht das nicht:** Dort werden Rechte immer vom Kind nach oben weitergegeben. Wo das nicht gewollt ist, gibt es dort eine **flache Liste**. Das gilt nur für Kanidm.
3. **Andere Richtung:** Wer es andersherum braucht, baut den Baum andersherum auf, statt einzelne Ausnahmen zu vergeben.
4. **Eine Workbench gibt immer einen Kontext zurück;** sie läuft nicht für sich allein. Aber aus einer Workbench wird schnell eine App (etwa Editor oder Schreibprogramm): Die Workbench füllt
   den ganzen Bildschirm, mit Menü und weiteren Primitives, Widgets oder Workbenches, auch wenn es nur eine Ansicht ist (Beobachter mit verschiedenen Ansichten). Damit ist der Widerspruch zwischen `CONVENTIONS.md` §2 und ADR 0005 geklärt.
5. **Agenten laufen immer in einer eigenen Sandbox unter eigenem Systembenutzer.**
6. **Ein Agent darf niemals Admin werden,** und erst recht nicht Superadmin.

## Später gesondert besprechen (Nutzer)
- **Admin-Status nach Beteiligung:** Wer sehr oft dabei ist und etwas tut, könnte ihn bekommen. Die Idee bleibt erhalten, entschieden ist nichts.
- **Sicherheit und Recht bei KI:** Wer haftet, wenn eine KI etwas Strafbares übersieht oder falsch entscheidet? Rechtlich belangen lässt sie sich nicht. Zugleich kann sie viel früher eingreifen als ein Mensch.
  Und wäre sie Superuser und würfe alle hinaus, bliebe nur Neuinstallation, und alle Daten wären weg.

## Zu klären
- Ob nach „Trennung in zwei Einstellungen“ und „Zustimmung beider Seiten“ (Fragen B und C an den Nutzer) so gebaut wird.
- Wo die Daten eines Users liegen: `fs-people` oder Identitäts-Wrapper.
