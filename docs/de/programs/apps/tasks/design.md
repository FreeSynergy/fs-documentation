# Tasks — Design

**Status (2026-11-06): Elemente und `subscribe` sind gebaut; Boards und Ansichten sind Vorschläge.** Zurück zum [Gesamtplan](../roadmap.md) · [Anforderungen](requirements.md).

## Idee

Eine Person will wissen, was als Nächstes zu tun ist. Ein Board, eine Liste und eine Zeitleiste sind Arten, das zu sehen; also sind sie Ansichten eines Programms, keine Programme selbst. Das ersetzt den früheren Plan für `fs-kanban` und `fs-timeline`.

- **Ein Programm, persönlich oder für eine Gruppe.** Der Besitzer einer Aufgabe ist eine Person oder eine Gruppe und kann wechseln. Nichts wird von vornherein festgelegt.
- **Eine Aufgabe, mehrere Zusammenhänge.** Dieselbe Aufgabe kann auf einem Projekt-Board, auf meiner persönlichen Liste und im Kalender erscheinen.
- **Eine Aufgabe steht für sich (entschieden, ADR 0050).** `fs-tasks` besitzt JSCalendar `Task`. `fs-calendar` besitzt `Event` und zeigt Aufgaben nur über die Schnittstelle von `fs-tasks`. `fs-calendar` hat kein eigenes `Task`-Modell mehr.

`fs-projectmanagement` ist eine Suite darüber: Aufgaben, Verlauf, Ressourcen, Umfragen, Whiteboard, Wiki.

## Daten

| Teil | Standard | Hinweise |
|------|----------|----------|
| Aufgabe | JSCalendar 2.0 `Task` | [Projekt-Standards](../../../data/projects/standards.md) |
| Abhängigkeiten | RFC 9253 | „blocks“ und „duplicates“ sind eine Lücke |
| Erweiterter Status | RFC 10051 | |
| Board, Spalte (`List`), Swimlane, Limit | ❌ keiner | **Eigene Spezifikation** (Kandidat Nr. 3); erstes Modell in [Projekte, technisch](../../../data/projects/technical.md) |
| Karte verschieben | `Update` auf `task_link`, nicht auf der Aufgabe | Eine Karte auf meinem Board zu verschieben darf die Aufgabe für alle nicht ändern |
| Verknüpfung zu einer Entscheidung | Lücke | Lässt eine Aufgabe sagen, warum sie existiert; verbindet mit `fs-surveys` |

## Open-Source-Lücken, die sich zu schließen lohnen

Aus der [Recherche](https://github.com/FreeSynergy/fs-documentation/blob/main/temp/research/projectmanagement-landscape.md): eine Entscheidung als Objekt, das mit Aufgaben verknüpft ist, eine Aufgabe in mehreren Zusammenhängen und die persönliche und gemeinsame Nutzung derselben Daten. Kapazität und Baselines gehören zu [`fs-resources`](../resources/index.md).

## Muster

| Muster | Verwendung |
|--------|------------|
| Repository | `TaskRepository`, `BoardRepository` über `Store` |
| Command | Verschieben und Bearbeiten, mit `apply` und `invert` für Rückgängig (ADR 0042) |
| Strategy | Abbildung von Spalte auf Status; Sortierung |
| Observer | Live-Aktualisierungen für Frontends und Präsenz |
| Facade | `Tasks` als einziger Einstiegspunkt des Kerns |

## Schnittstellen-Skizze

| Schnittstelle | Fähigkeiten |
|---------------|-------------|
| `Tasks` (Wurzel) | `capabilities()`, gibt die anderen heraus |
| `Items` | `task.create`, `task.edit`, `task.assign`, `relation.create`, `label.assign` |
| `Boards` (Platzhalter) | `board.open`, `board.create`, `column.create`, `column.limit`, `card.move` |
| `subscribe` | Live-Änderungen |

Anhänge laufen über `fs-files`, Personen über `fs-people`, Gruppen über `fs-groups`.

## Ansichten

Workbench `kanban-board` sowie eine kompakte Ansicht „Meine nächsten Aufgaben“, `task-list` und `timeline-gantt`, die jeweils innerhalb anderer Programme nutzbar sind. Siehe [geplante Komponenten](../../../components/planned.md).

## Offene Fragen

1. Sind Spalten Status? Die analysierten Werkzeuge unterscheiden sich: Bei manchen sind sie Status, bei anderen freie Listen. Wir schlagen eine optionale Zuordnung vor.
2. Zeiterfassung: Teil von `fs-tasks` oder von `fs-history`? Wir schlagen vor, sie als Verlauf zu erfassen.
