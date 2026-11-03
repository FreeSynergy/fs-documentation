# OpenProject - Beschreibung

## Übersicht

OpenProject ist die führende freie Projektmanagement-Software zum Selbsthosten. Sie deckt klassische (Wasserfall-) und agile Methoden in einer Anwendung ab: Aufgaben (Arbeitspakete), Meilensteine, Gantt-Pläne, Scrum-/Kanban-Boards, Zeiterfassung und Kosten.

## Was OpenProject macht

OpenProject verwaltet **Projekte mit Arbeitspaketen** (Anforderungen, Tasks, Meilensteine, Risiken) inklusive Status, Priorität, Version, Verantwortlichem, Relationen und Abhängigkeiten. Agile Teams nutzen **Boards** (Scrum-Backlog, Sprint-Boards, task Boards, Kanban) mit Sprints und Epics. Dazu kommen **Gantt-Diagramme und Roadmap**, **Zeit- und Kostenverfolgung** mit Budgets, ein **Wiki**, **Meetings** mit Protokollen, **Diskussionsforen**, **Nachrichten** und Datei-Downloads. Rollen, Rechte und anpassbare Workflows (Status/Übergänge je Typ und Rolle) steuern den Prozess. Die Software erschien 2012 als Abspaltung von ChiliProject und wird laufend weiterentwickelt.

## Vorteile

- **Alles in einer Anwendung**: Aufgaben, Gantt, agile Boards, Wiki, Meetings, Zeiterfassung, Kosten
- **Self-Hosted und kostenlos**: Community-Edition unter freier Lizenz, eigene Datenhoheit
- **Anpassbare Workflows**: Status, Übergänge und Felder je Typ und Rolle konfigurierbar
- **REST-API v3 mit API-Browser**: gut dokumentierte Schnittstelle inklusive Webhooks
- **SSO-Optionen**: LDAP/AD, SAML und OpenID Connect (je nach Version und Edition)
- **Übersetzt**: Oberfläche u. a. auf Deutsch, Englisch und viele weitere Sprachen
- **Kommerzieller Support**: Enterprise-Edition mit Zusatzfunktionen und Cloud-Angebot

## Abgrenzung zu anderen Systemen

### OpenProject vs. Redmine
- **Redmine** ist ein schlankes Issue-System mit riesiger Plugin-Landschaft, **OpenProject** liefert mehr Funktionen out of the box (Gantt, agile Boards, Meetings)
- **OpenProject** hat eine modernere Oberfläche und REST-API v3, **Redmine** eine einfache XML/JSON-API
- Beide sind Open Source; **OpenProject** trennt klar Community- und Enterprise-Funktionen

### OpenProject vs. Jira
- **Jira** ist kommerziell (SaaS/Data Center) mit riesigem Marketplace, **OpenProject** ist selbst gehostet und kostenlos
- **Jira** ist auf Software-Teams und Anpassbarkeit (JQL, Schemata) optimiert, **OpenProject** auf integrierte Projektplanung
- **OpenProject** enthält Zeit-/Kostenverfolgung nativ, **Jira** nur Grundfelder (ausführliche Reports als App)

### OpenProject vs. Planka
- **Planka** ist ein reines Kanban-Board, leichtgewichtig und schnell, **OpenProject** eine volle Projekt Suite
- **Planka** hat keine Gantt-, Kosten- oder Meeting-Funktionen, **OpenProject** sehr wohl
- **OpenProject** ist rollen- und workflow-schwer, **Planka** bewusst einfach gehalten

## Technische Details

- **Backend**: Ruby on Rails
- **Database**: PostgreSQL (Pflicht; andere Datenbanken werden nicht unterstützt)
- **Frontend**: serverseitig gerenderte Views plus Angular-Komponenten (z. B. Arbeitspaket-Tabelle, Boards)
- **Authentication**: lokale Konten, LDAP/AD; SAML und OpenID Connect je nach Version/Edition (Enterprise-Anteile versionsabhängig)
- **Hosting**: Docker/Podman-Images, Paketinstallation, Helm Chart; optional OpenProject Cloud (SaaS)

## Für wen ist OpenProject geeignet?

- **Organisationen mit Datenhoheits-Anforderungen** (Behörden, Bildung, Unternehmen mit Self-Hosting-Strategie)
- **Hybride Teams**, die Wasserfall (Gantt, Meilensteine) und agil (Scrum, Kanban) mischen
- **Projekte mit Zeiterfassung und Kostenkontrolle** inklusive Budgets
- **Weniger geeignet** für Teams, die nur ein schnelles Kanban-Board brauchen (dann Planka oder Trello)
