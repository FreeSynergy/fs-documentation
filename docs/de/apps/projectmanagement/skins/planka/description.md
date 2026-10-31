# Planka - Beschreibung

## Übersicht

Planka ist ein quelloffenes Kanban-Werkzeug zum Selbsthosten: Projekte enthalten Boards, Boards enthalten Listen (Spalten) mit Karten. Alles synchronisiert in Echtzeit zwischen allen Beteiligten, ohne dass man neu laden muss.

## Was Planka macht

Planka strukturiert Arbeit über **Projekte > Boards > Listen > Karten**. Karten tragen Beschreibungen in Markdown, Fälligkeiten, farbige **Labels**, Zugewiesene, **Checklisten (Tasks)**, Anhänge und Kommentare; Aktivitäten je Karte und Board protokollieren jede Änderung. Über **Benachrichtigungsdienste** (E-Mail/SMTP plus Anbindungen an über 100 Anbieter) und **Webhooks** lässt sich Planka in Automatisierungen einbinden. Die Community-Edition ist kostenlos selbst hostbar; die kommerzielle **Pro-Edition** ergänzt SSO (OIDC), Gastrollen, Kalender-/Timeline-Ansichten, Themes und mobile Optimierung.

## Vorteile

- **Extrem einfach**: vier Konzeptebenen, sofort bedienbar, ohne Konfigurationsballast
- **Echtzeit**: Änderungen erscheinen sofort auf allen Clients (Socket.IO)
- **Echt kostenlos self-hosted**: Community-Edition ohne Benutzerzahl- oder Feature-Schränken im Kern
- **Dokumentierte REST-API**: offizielle Swagger-Referenz und Webhooks inklusive
- **Zwei-Faktor-Authentifizierung** bereits in der Community-Edition
- **Leicht zu betreiben**: Docker Compose mit PostgreSQL, wenige Umgebungsvariablen
- **Mehrsprachig**, inkl. deutscher Oberfläche (Internationalisierung ausdrücklich Feature)

## Abgrenzung zu anderen Systemen

### Planka vs. Trello
- **Trello** ist SaaS mit Board-Automatisierung („Butler") und Mobility-Apps, **Planka** läuft auf eigener Infrastruktur
- **Trello** hat Power-Ups/Marketplace, **Planka** erweitert über API und Webhooks
- **Planka** speichert Daten ausschließlich lokal - Datenschutz-/DSGVO-Argument gegenüber Trello

### Planka vs. Wekan
- **Wekan** (Meteor) bringt viele Detailoptionen (Swimlanes, Templates) early, **Planka** bleibt bewusst minimalistisch
- **Planka** hat moderneres, ruhigeres UI und Echtzeit über Socket.IO; **Wekan** wirkt funktionsüberladen
- **Wekan** ist MIT-lizenziert, **Planka** fair-code (Community frei, Pro kommerziell)

### Planka vs. OpenProject
- **OpenProject** ist die volle Projekt-Suite (Gantt, Kosten, Workflows), **Planka** ist reines Kanban
- **Planka** ohne Zeiterfassungs-Reports, Gantt und Meeting-Module (Timeline nur in Pro)
- Beide self-hosted; **Planka** in Minuten aufgesetzt, **OpenProject** als Installations- und Pflegeaufwand deutlich größer

## Technische Details

- **Backend**: Node.js (Express), ORM Bookshelf/Knex
- **Database**: PostgreSQL als Standard; MySQL/MariaDB und SQLite werden je nach Version unterstützt (versionsabhängig)
- **Frontend**: React mit Redux/Redux-Sagas auf Semantic UI React; Drag & Drop über react-beautiful-dnd
- **Echtzeit**: Socket.IO-Kanal für Karten-/Board-Synchronisation
- **Authentication**: lokale Konten, 2FA (Community); SSO per OIDC und Gastrollen in der Pro-Edition; API-Tokens für Skripte
- **Hosting**: offizielles Docker-Image + Docker Compose; Reverse Proxy mit HTTPS empfohlen

## Für wen ist Planka geeignet?

- **Kleine und mittlere Teams**, die ein schnelles, datenschutzfreundliches Kanban ohne Scrum-Ballast wollen
- **Privatpersonen und Homelabs**, die Aufgaben-Boards selbst hosten
- **DSGVO-sensible Organisationen**, die Trello ersetzen, aber dessen Einfachheit behalten möchten
- **Weniger geeignet** für Wasserfall-Planung, Zeiterfassungs-Abrechnung oder streng getaktete Scrum-Prozesse
