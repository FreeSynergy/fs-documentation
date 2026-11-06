# Der Gesamtplan

**Status: Entwurf (2026-11-06), in den Grundzügen vom Projektverantwortlichen vereinbart.** Er sagt, was wir planen und warum, damit jeder sehen kann, wohin wir wollen, und helfen kann. Warum wir das überhaupt tun: siehe das [Manifest](../../manifesto.md).

## Wie alles geordnet ist

Alles wird nach seinem Zweck sortiert, nicht danach, wie ein Werkzeug aussieht. Vier Fragen entscheiden, wohin etwas gehört:

| Frage | Dann ist es ein |
|-------|-----------------|
| Hat es eigene Daten mit eigenen Regeln? | **Programm** |
| Stellt es Programme für einen Zweck zusammen? | **Suite** |
| Zeigt es etwas, ohne zu wissen, was die Daten bedeuten? | **Komponente** (eine **Workbench** ist eine große Komponente) |
| Ist es eine Art, ein Programm zu nutzen? | **Frontend**, gegebenenfalls mit eingebauten Filtern |

Jedes Thema hat genau eine [Schnittstelle](../../interfaces/index.md), für jeden Anbieter dieselbe. **Jeder Standard hat genau ein besitzendes Programm, es gibt also einen Ursprung der Wahrheit,** und andere Programme erreichen ihn über diese Schnittstelle.

Ob Ansichten wie Galerie oder Kanban *zusätzlich* als eigenständige Programme angeboten werden sollen, ist noch offen. Sie können als eigenständige Apps erscheinen, indem sie Frontends sind, ohne eigene Daten zu haben.

## Programme

| Zweck | Programm | Status |
|-------|----------|--------|
| Objekte halten, zwischen Programmen teilen | [`fs-store`](https://github.com/FreeSynergy/fs-store), [`fs-hub`](https://github.com/FreeSynergy/fs-hub) | Vorhanden |
| Anmelden, Systemzugang | [Identitäts-Wrapper](../platform/identity.md) über Kanidm | Geplant |
| Zusammengehören, entscheiden, wer was darf | [`fs-groups`](../platform/groups.md) | Geplant, **neu** |
| Alles halten und finden | [`fs-files`](files/design.md) | Geplant |
| Wissen, wer jemand ist, mit Rollen | [`fs-people`](https://github.com/FreeSynergy/fs-people) | Kern vorhanden, keine GUI |
| Irgendwo zu einer Zeit sein | [`fs-calendar`](https://github.com/FreeSynergy/fs-calendar) | Kern vorhanden, keine GUI |
| Wissen, wo | [`fs-maps`](https://github.com/FreeSynergy/fs-maps) | Kern vorhanden, keine GUI |
| Gemeinsam schreiben und wissen | [`fs-wiki`](https://github.com/FreeSynergy/fs-wiki) (Crate `fs-text`) | Kern vorhanden, keine GUI |
| Jemandem etwas sagen | [`fs-messenger`](messenger/contract.md) | Vertragsentwurf |
| Wissen, was als Nächstes zu tun ist | [`fs-tasks`](https://github.com/FreeSynergy/fs-tasks) ([Design](tasks/design.md)) | Kern vorhanden, keine GUI; Schnittstelle als Entwurf |
| Erinnern, was ich oder wir getan haben | [`fs-history`](history/index.md) | Geplant, **neu**; eventuell eine Ansicht |
| Wissen, was wir haben und brauchen | [`fs-resources`](resources/index.md) | Geplant, **neu** |
| Fragen und gemeinsam entscheiden | [`fs-surveys`](surveys/design.md) | Geplant |
| Visuell denken | [`fs-whiteboard`](whiteboards/design.md) | Geplant |
| Etwas zeigen und überall hinbringen | [`fs-streaming`](streaming/design.md) | Geplant |

`fs-capnpc`, unser Cap'n-Proto-Compiler in reinem Rust, unterstützt sie alle. Details zu dem, was existiert, stehen in der `DESIGN.md` jedes Repositorys.

## Ansichten (Workbenches, keine Programme)

| Ansicht | Zeigt Daten aus |
|---------|-----------------|
| Galerie, Videothek, Musik | `fs-files` |
| Kanban-Board, Aufgabenliste | `fs-tasks` |
| Zeitleiste (Gantt) | `fs-tasks`, `fs-calendar` |
| Zeitleiste dessen, was passiert ist | `fs-history` |
| Ergebnis-Dashboards | `fs-surveys`, andere, mit [Diagrammen](../../components/charts.md) |

## Suiten

Ein Programm kann zu mehreren Suiten gehören.

| Suite | Enthält |
|-------|---------|
| Groupware | Personen, Kalender, Wiki, Karten, Messenger |
| **Projektmanagement** | Aufgaben, Verlauf, Ressourcen, Umfragen, Whiteboard, Wiki, Gruppen; eventuell Kosten |
| **Demokratie** | Umfragen, Gruppen, Wiki, Messenger, Aufgaben, Ressourcen |
| Medien | Dateien (mit Galerie), Streaming |
| ERP, CRM, andere | Später, teilen Ressourcen, Aufgaben und Personen |

## Reihenfolge

```text
1. Foundation     manifesto, interface catalogue, sharing model
                  fs-groups + identity wrapper, then fs-files
2. Components     shared ones first, plus charts; each built when the next program needs it
                  GUIs for the existing cores: people, calendar, maps, wiki
3. Work           GUI for fs-tasks, fs-history, then fs-surveys, fs-resources, fs-messenger
4. Together       live presence, fs-whiteboard
5. Suites         project management, democracy
6. Media          gallery frontends, fs-streaming
```

**Zuerst kommen die Komponenten, dann das Programm.** Wir dokumentieren Komponenten früh, damit wir wissen, was wir haben. Gebaut wird jede erst, wenn das nächste Programm sie braucht, denn Komponenten ohne echten Nutzer bekommen ihre Schnittstelle meist falsch.

## Was das lohnend macht

Ergebnisse aus den [Recherchenotizen](https://github.com/FreeSynergy/fs-documentation/tree/main/temp/research) vom 2026-11-06:

- **Entscheidungen als eigenständige Objekte.** Kein Projektwerkzeug, das wir uns angesehen haben, behandelt eine Entscheidung oder Abstimmung als Objekt, das mit Aufgaben verknüpft ist.
- **Eine Umfrage, die sich ausweitet.** Kein gefundenes Werkzeug lässt eine Umfrage in einer kleinen Gruppe beginnen und in deren übergeordnete Gruppe wechseln, wobei die Ergebnisse übernommen werden.
- **Eine Aufgabe, mehrere Zusammenhänge.** Persönliche und Gruppennutzung sind anderswo getrennte Produkte.
- **Kapazitätsplanung und Baselines.** Open-Source-Werkzeuge halten sie hinter kostenpflichtigen Tarifen oder bieten sie nicht an.
- **Systemisches Konsensieren.** Als Methode beschrieben, aber kein Open-Source-Werkzeug gefunden.
- **Einfaches, plattformübergreifendes, selbst gehostetes Streaming.** Kein offenes Werkzeug bietet alle drei zusammen.

Die proprietären Produkte wurden nur teilweise geprüft; jede Notiz nennt, was verifiziert wurde.

## Offene Entscheidungen

| # | Frage | Empfehlung |
|---|-------|------------|
| 1 | Sollen Ansichten auch eigenständige Programme sein? | Später besprechen |
| 2 | Beim Verlassen nach einem Export fragen? | Verschoben, nicht vergessen ([Details](files/design.md#speichern-und-exportieren)) |

**Entschieden am 2026-11-06:** ein `fs-people`, jede Person mit mehreren [Rollen](../../interfaces/roles.md); Codecs werden ausgelagert, offene zuerst; jeder bestehende Kern wird anhand des Schnittstellenkatalogs überarbeitet, und alle Schnittstellen liegen in `fs-interfaces`. Gemeinsames Arbeiten in Echtzeit führt Eigenschaften mit einer logischen Uhr zusammen und nutzt einen CRDT nur für gemeinsamen Text (`loro` und `yrs` sind bei Bedarf zu vergleichen).

## Was entschieden ist

ADR 0044 bis 0052 in [`conventions/decisions`](https://github.com/FreeSynergy/fs-documentation/tree/main/conventions/decisions).
