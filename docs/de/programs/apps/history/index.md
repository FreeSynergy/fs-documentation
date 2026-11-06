# Verlauf

`FreeSynergy.History` (`fs-history`) beantwortet die Frage: **Was habe ich oder was haben wir getan?** Es zeigt deine eigenen Daten als Zeitleiste, ob für eine Person oder für ein Projekt. Das hieß früher `fs-timeline`.

**Status: geplant, noch kein Code (2026-11-06).** Siehe den [Gesamtplan](../roadmap.md).

## Idee

Ein **Beobachter** dessen, was geschieht. Jedes Programm führt bereits ein Aktivitätsprotokoll (ADR 0020), und `fs-history` hört zu:

- **Persönlich:** Was habe ich letzte Woche getan, über alle Programme hinweg? Ein Tagebuch (`fs-diary`) ist dann einfach das, gefiltert auf mich selbst: ein Frontend mit eingebautem Filter. Dort geschriebener Text ist ein Wiki-Eintrag wie jeder andere (ADR 0031).
- **Projekt:** Was ist passiert, wann und von wem? Ein Projektbericht muss nicht aus dem Gedächtnis geschrieben werden.
- **Telemetrie als Import:** Auch technische Ereignisse können hinzukommen, etwa mit einem Standard wie OpenTelemetry (Kandidat, noch nicht gelesen). Sie bleiben **lokal, wenn du nicht anders entscheidest**: Telemetrie woanders heißt, Daten wegzuschicken, und hier geschieht das nicht.

## Offene Fragen

1. **Hat es eigene Daten?** Als Beobachter liest es vor allem die Protokolle anderer Programme. Wenn ja, könnte es eine Workbench und kein Programm sein.
2. **Privatsphäre:** Persönlicher Verlauf zeigt alles, was ich getan habe. Er muss meiner bleiben, solange ich ihn nicht teile, und die Sicht einer Gruppe darf nicht mehr zeigen, als ich zugestimmt habe. Das braucht Sorgfalt.
3. **Zeiterfassung:** Lässt sie sich aus dem Verlauf ableiten, sodass niemand ein Formular ausfüllen muss?
4. **Welche Einträge zählen?** Ein Protokoll enthält zu viel. Wie zeigen wir, was bedeutsam ist?
