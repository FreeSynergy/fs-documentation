# 0049 – Gesamtplan: Programme nach Zweck, Workbench und Suite

Status: akzeptiert (2026-11-06) · ersetzt **0044** · öffentlich: `docs/en/programs/apps/roadmap.md`, `docs/en/manifesto.md`

## Kontext (Nutzer)
Bisher wurde Software danach geschnitten, was sich verkaufen lässt. Wir ordnen neu: Was gehört wirklich zusammen, und wofür
brauchen wir es? „Viel wichtiger als: was kann es.“ Software für Menschen, nicht Menschen, die sich an Software anpassen.

## Entscheidung (Nutzer)
1. **Vier Fragen:** eigene Daten → Programm; Zusammenstellung → Suite; Darstellung ohne Datenwissen → Component;
   **eine Workbench ist eine Teilmenge von Component**; eine Art, ein Programm zu nutzen → Frontend.
2. **Gallery ist kein eigenes Programm**, sondern Workbench und Frontend von `fs-files`. Ob solche Ansichten zusätzlich
   eigenständige Programme werden, wird später besprochen.
3. **Neu:** `fs-tasks` statt `fs-kanban`/`fs-timeline`; Kanban und Timeline sind Ansichten. `fs-history` zeigt die eigenen
   Daten als Timeline, persönlich und im Projekt. `fs-resources` für ERP, Projekte, Demokratie. `fs-groups`, verschachtelt.
4. **`fs-projectmanagement` ist eine Suite** (Tasks, History, Surveys, Whiteboard, Wiki, weitere; Kosten prüfen). Die
   Demokratie-Suite ist ebenso wichtig. Programme können in mehreren Suiten sein.
5. **Erst Components, dann das Programm.** Vorbereitet wird, was wir kennen; gebaut wird, wenn es gebraucht wird.
6. **Persönlich oder Gruppe ist keine Entscheidung am Anfang.**
7. **Live wie in Spielen:** Man sieht, was andere gerade tun.
8. **Umfragen:** verschiedene Typen (Konsens, Mehrheit …); auch komplett offen ohne Anmeldung, mit Schutz vor Massenabgaben;
   können unten starten und auf übergeordnete Gruppen ausgeweitet werden. Viele Charts, standardisiert und als Plugins.
9. **Streaming** ist Verteilung: einmal aufnehmen, gleichzeitig auf mehrere Plattformen, live und nicht live, ohne SaaS;
   Aufnahme einfacher als OBS; Videos verwalten über Files.
10. **Suche nach dem, was Open Source nicht hat,** und alles zusammenführen, für alle Programme.
11. Contacts und alles, was schon begonnen ist, bleibt im Plan.

## Folgen
- `programs/apps/kanban/` → `programs/apps/tasks/`. Weitere Umzüge (etwa `projectmanagement` unter `suites/`) folgen.
- Reihenfolge steht in der Roadmap und ist ein Vorschlag, dem der Nutzer im Grundsatz zugestimmt hat; `fs-groups` kam danach
  dazu und steht vor `fs-files`.
