# Homarr - Beschreibung

## Übersicht

Homarr ist ein quelloffenes Dashboard für selbst gehostete Umgebungen (Homelab, Heimserver, kleine Team-Infrastruktur). Es bündelt Links, Container-Status und Dienst-Integrationen in visuellen Boards, die vollständig per Mausklick eingerichtet werden.

## Was Homarr macht

Homarr stellt eine Weboberfläche bereit, in der sogenannte **Boards** angelegt werden. Ein Board ist ein Raster aus Widgets: App-Verknüpfungen, Statusanzeigen, Diagramme, Listen und Inhaltskacheln. Über **Integrationen** (Docker, Portainer, Pi-hole, qBittorrent, Sonarr/Radarr, Jellyfin/Plex, Kalender u. a.) holt sich Homarr Live-Daten und kann Aktionen auslösen, etwa einen Container neu starten. Die Konfiguration passiert vollständig in der Oberfläche und wird in einer SQLite-Datenbank gespeichert.

## Vorteile

- **Keine Config-Datei nötig**: Boards, Widgets und Layouts werden per Drag & Drop in der UI gebaut
- **Live-Integrationen**: Status, Auslastung und Inhalte echter Dienste in der Übersicht
- **Aktionen aus dem Dashboard**: Container starten/stoppen/neu starten, Requests an Medien-Tools
- **Mehrere Boards und Nutzer**: Rollen (Admin/Mitglied), Einladungen, geteilte Boards
- **Modernes UI**: React/Mantine, Themes, Hintergrundbilder, Blur, dunkler und heller Modus
- **Getrennte Desktop- und Mobil-Layouts** pro Board
- **API-Referenz vorhanden**: tRPC-Verfahren sind öffentlich dokumentiert

## Abgrenzung zu anderen Systemen

### Homarr vs. Heimdall
- **Homarr** ist widget-zentriert (viele kleine Datenkacheln), **Heimdall** ist kachel-zentriert (App-Kacheln mit optionalen Statistik-Overlays)
- **Homarr** wird komplett über die UI konfiguriert, **Heimdall** kombiniert UI-Verwaltung mit Laravel-Dateien/`.env`
- **Heimdall** ist lighter im Konzept, **Homarr** hat mehr Integrationen und Board-Verwaltung

### Homarr vs. Homer
- **Homer** ist eine statische Seite ohne Backend, **Homarr** ist eine Full-Stack-Anwendung mit Datenbank und Login
- **Homer** konfiguriert man in `config.yml`, **Homarr** in der Weboberfläche
- **Homer** hat keine Live-Aktionen, **Homarr** kann auf Docker und Dienste einwirken

### Homarr vs. Dashy
- **Dashy** konfiguriert primär über `conf.yml`/`conf.json` (mit optionalem UI-Editor), **Homarr** nur über die UI
- **Dashy** bietet starkes Theming und Status-Checks für Links, **Homarr** stärkere Docker-/Medien-Integrationen
- **Dashy** ist auch statisch hostbar, **Homarr** benötigt einen laufenden Server mit Authentifizierung

## Technische Details

- **Backend**: Node.js, Next.js (App-Router), tRPC für die interne API, Drizzle ORM
- **Database**: SQLite als Standard (Datei im Datenverzeichnis); externe Datenbanken sind nicht vorgesehen
- **Cache/Queues**: Redis wurde in älteren Versionen für Sessions und Hintergrundjobs genutzt; aktuelle Versionen kommen ohne eigenen Redis-Dienst aus
- **Frontend**: React mit Mantine-Komponenten, `react-grid-layout` für die Board-Raster
- **Authentication**: NextAuth mit lokaten Konten (Credentials), OIDC/Keycloak, optional header-basierte Auth hinter einem Reverse Proxy; Board-Berechtigungen und Rollen
- **Hosting**: Docker/Compose (offizielles Image), Kubernetes/Helm, Bare-Metal mit Node.js; HTTPS über Reverse Proxy empfohlen

## Für wen ist Homarr geeignet?

- **Homelab-Nutzer**, die Docker-Container und Medien-Stacks zentral überwachen wollen
- **Teams und Familien**, die verschiedene Boards mit unterschiedlichen Rechten brauchen
- **Admins, die keine YAML-Dateien pflegen** möchten, sondern alles in der Oberfläche einstellen
- **Weniger geeignet** für reine Link-Sammlungen (dann ist Homer einfacher) oder für Umgebungen ohne persistente Daten
