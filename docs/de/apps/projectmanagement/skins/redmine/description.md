# Redmine - Beschreibung

## Übersicht

Redmine ist eine quelloffene Projektverwaltungs-Webanwendung: mehrere Projekte, differenzierte Issue-Tracker, Zeiterfassung, Wiki und Foren - schlank, erprobt und extrem plugin-freundlich.

## Was Redmine macht

Redmine verwaltet **beliebig viele (Teil-)Projekte**, jedes mit eigenen Mitgliedern, Rollen und Modulen. Issues bekommen **Tracker** (z. B. Fehler, Unterstützung, Aufgabe), **Status**, **Priorität**, Kategorie, Meilenstein, Zuweisung und benutzerdefinierte Felder; der Statuswechsel folgt konfigurierbaren **Workflows** je Rolle und Tracker. **Zeiterfassungen** werden je Issue und Aktivität gebucht und über Berichte ausgewertet. Jedes Projekt kann **Wiki**, **Foren (Boards)**, **Dokumente**, **Dateianhänge**, **News**, **Roadmap** und **Kalender** aktivieren. Redmine ist seit 2006 erhältlich und wird community-getrieben weiterentwickelt.

## Vorteile

- **Schlank und stabil**: Rails-Kern ohne Ballast, über Jahre bewährt
- **Plugin-Ökosystem**: hunderte Erweiterungen (Kanban-Boards, Zwei-Faktor-Auth, Themes, CRM ...)
- **Mehrsprachig**: vollständige deutsche Oberfläche
- **Granulare Workflows**: Berechtigungen je Tracker, Rolle, Statusübergang und Feld
- **REST-API** mit XML und JSON sowie Atom-/ICS-Feeds
- **Versionsverwaltung**: integrierte Browser für Git und Subversion, Commit-Verknüpfung zu Issues
- **Kostenlos und self-hosted**: volle Datenhoheit

## Abgrenzung zu anderen Systemen

### Redmine vs. OpenProject
- **OpenProject** (aus Redmines ChiliProject-Ursprungslinie) liefert moderne UI, Gantt und agile Boards im Kern; **Redmine** hält den Kern klein und holt Funktionen per Plugin
- **OpenProject** braucht PostgreSQL, **Redmine** läuft auch mit MySQL/MariaDB
- **Redmine** ist stärker plugin-orientiert, **OpenProject** erweitert den Kern selbst

### Redmine vs. Jira
- **Jira** ist kommerziell mit SaaS-Betrieb und Marketplace, **Redmine** selbst gehostet und kostenlos
- **Jira** bietet JQL, Boards und Automation komfortabel, **Redmine** löst Gleiches über Filter, Plugins und Handarbeit
- **Redmine** ist eher Ticket-/Issue-System mit Projektanbau, **Jira** Produkt für agiles Software-Tracking

### Redmine vs. Trac
- **Trac** ist auf ein Projekt (Wiki + Changesets) ausgerichtet, **Redmine** von Grund auf mehrprojektig
- **Redmine** bringt Zeiterfassung, Workflows und ein differenziertes Rollenmodell von Haus aus mit, **Trac** nur Basis-Tickets
- **Trac** ist älter und minimalistischer, **Redmine** funktional deutlich breiter

## Technische Details

- **Backend**: Ruby on Rails
- **Database**: MariaDB/MySQL oder PostgreSQL empfohlen; SQLite je nach Version nur eingeschränkt/geprüft (versionsabhängig)
- **Frontend**: serverseitig gerendertes HTML (ERB), jQuery; kein Single-Page-Frontend
- **Authentication**: lokale Konten, LDAP; OpenID core-seitig entfallen (Redmine 5.0+), Alternativen über Plugins (CAS, SAML, OAuth - versionsabhängig)
- **Hosting**: Ruby-Umgebung (Phusion Passenger, Puma), Community-Docker-Images; kein offizielles Image

## Für wen ist Redmine geeignet?

- **Technische Teams und Dienstleister**, die Issues, Support und Zeiterfassung in einer selbst gehosteten Anwendung bündeln
- **Administratoren mit Plugin-Bedarf**, die Redmine per Erweiterung zur eigenen Plattform formen
- **Kostenbewusste Organisationen**, die Reife und Datenhoheit vor modernem Komfort stellen
- **Weniger geeignet** für Teams, die sofort moderne Scrum-Boards ohne Plugins erwarten
