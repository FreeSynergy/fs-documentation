# Projectmanagement — Frontend-Dokumentation

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Projectmanagement` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [Asana](asana/index.md) | [latest](asana/latest/description.md) | Asana ist Aufgaben- und Projektarbeit auf Portfolio-Ebene: Aufgaben mit Feldern (Fälligkeit, Assignees, Abhängigkeiten, Custom Fields) in Projekten (Liste/Tabelle/Timeline/Kanban), Teams, Workloads… |
| [Jira](jira/index.md) | [latest](jira/latest/description.md) | Jira (Atlassian) ist Issue- und Projekt-Tracking mit Workflows: Issues durchlaufen Status (To Do→In Progress→Done), mit Sprints (Jira Software), Typen, Prioritäten und mächtigem JQL. |
| [OpenProject](openproject/index.md) | [latest](openproject/latest/description.md) | OpenProject ist ein quelloffenes Projektmanagement-System zum Selbsthosten (Community-Edition plus kommerzielle Enterprise-Edition) mit Arbeitspaketen, Gantt-Planung, agilen Boards, Zeit- und Koste… |
| [Planka](planka/index.md) | [latest](planka/latest/description.md) | Planka ist ein selbst gehostetes, schlichtes Kanban-Board (fair-code: kostenlose Community-Edition plus kommerzielle Pro-Edition) mit Projekten, Boards, Listen und Karten in Echtzeit-Kollaboration. |
| [Redmine](redmine/index.md) | [latest](redmine/latest/description.md) | Redmine ist eine freie, webbasierte Projektverwaltungs- und Issue-Tracking-Anwendung auf Rails-Basis: mehrere Projekte mit Issue-Trackern, Zeiterfassung, Wiki, Foren, Gantt/Kalender und rollenbasie… |
| [Taiga](taiga/index.md) | [latest](taiga/latest/description.md) | Taiga ist das agile Open-Source-Projektmanagement (AGPL, Python/Django + modernes Frontend „Taigo“): Scrum (Sprints, Points) und Kanban in einem, dazu Epics, Issues, Wiki und CRM-Modul. |
| [Trello](trello/index.md) | [latest](trello/latest/description.md) | Trello (Atlassian) ist das digitale Kanban-Brett: Boards mit Listen und Karten, Fälligkeiten, Labels, Mitglieder, Checklisten und Automatisierung per „Butler“. |
| [Wekan](wekan/index.md) | [latest](wekan/latest/description.md) | Wekan ist der offene Trello-Klon (Meteor/Node, MongoDB): Boards, Listen, Karten, Swimlanen, Labels und Checklisten — selbst gehostet, mit OAuth2/LDAP und ausgehenden Webhooks. |

## Dateisatz pro Programm (ADR 0012)

```
programs/apps/projectmanagement/frontends/<program>/
├── index.md        was es ist, bemerkenswerte Ideen, dokumentierte Versionen, Quellen
├── changelog.md    Änderungen zwischen dokumentierten Versionen (≥ 2 Versionen)
└── <version>/
    ├── description.md    Pflicht · Ausführliche Beschreibung, Abgrenzung, für wen es passt
    ├── features.md       Pflicht · Was das Programm kann — und was nicht
    ├── layout.md         Pflicht · Fensterstruktur, Bereiche, Panels
    ├── menus.md          Pflicht · Menüstruktur, Kontextmenüs, Menüs nach Rolle
    ├── shortcuts.md      Pflicht · Tastatur-Shortcuts
    ├── api.md            Pflicht · APIs und Protokolle, Authentifizierung, Rate Limits
    ├── themes/index.md   Pflicht · Themes: Farben, Typografie, Abstände — was sich nachbauen lässt
    ├── interaction.md    bei Bedarf · Hover, Fokus, Ziehen, Gesten (Finger, Maus, Stift)
    ├── states.md         bei Bedarf · UI-Zustände und Übergänge
    ├── events.md         bei Bedarf · Ereignisse nach außen (Webhooks, Push, Streams)
    ├── limits.md         bei Bedarf · Bekannte Grenzen
    ├── i18n.md           bei Bedarf · Lokalisierung, Schreibrichtung
    └── dependencies.md   bei Bedarf · Welche unserer Bausteine ein Frontend dieser Art braucht
```

Protokolle (Matrix, IMAP, CalDAV, …) sind keine Frontends; sie stehen unter [data](../../../../data/standards.md).
