# Dashy - Beschreibung

## Übersicht

Dashy (Projekt `Lissy93/dashy`, dashy.to) ist ein quelloffenes, sehr anpassbares Startseite-Werkzeug für selbst gehostete Dienste. Der Schwerpunkt liegt auf einer textbasierten Konfiguration, aus der eine schnelle Kacheloberfläche mit Statusanzeigen, Widgets und themenfreundlichem Design entsteht.

## Was Dashy macht

Dashy liest eine Konfigurationsdatei (`conf.yml` oder `conf.json` im Ordner `user-data/`) und baut daraus **Sektionen** mit **App-Kacheln**: Icon, Titel, Beschreibung, Ziel-URL, Öffnungsart, Tags. Beim Aufruf prüft Dashy auf Wunsch die Erreichbarkeit jeder Kachel (HTTP oder Ping) und färbt sie entsprechend. Zusätzlich können Widgets (Uhr, Wetter, RSS, Kryptokurse, eigene Widgets) eingebunden werden. Es gibt drei Ansichten — normal, reduziert und Arbeitsbereich — sowie Themes, eine sofort filternde Suche und optional mehrere Unterseiten.

Die Konfiguration kann per Hand, über den interaktiven Editor in der Oberfläche oder über eine optionale REST-API geändert werden.

## Vorteile

- **Konfiguration als Datei**: versionierbar, testbar, in Sekunden verglichen
- **Interaktiver Editor**: Änderungen trotzdem ohne Texteditor möglich
- **Statusanzeigen**: grüne/rote Punkte an allen Kacheln, mit eigenen Prüfregeln
- **Themes und eigenes CSS**: umfangreiche mitgelieferte Schemata, Theme-Editor in der Oberfläche
- **Schnelle Suche**: sofortiges Filtern beim Tippen, Tags, URL-Aliasse, Websuche mit Kurzkommandos
- **Authentifizierung eingebaut**: HTTP-Basic, OIDC-Provider, lokale Nutzer mit Rollen und Zwei-Faktor-Option
- **Optionale REST-API**: Konfiguration programmatisch lesen und schreiben
- **Flexibles Hosting**: Container, Bare-Metal oder rein statisch

## Abgrenzung zu anderen Systemen

### Dashy vs. Homarr
- **Dashy** beschreibt das Dashboard in einer Datei, **Homarr** baut es per Drag & Drop in einer Datenbank
- **Homarr** steuert Container und Medien-Dienste, **Dashy** prüft nur Erreichbarkeit und zeigt Werte an
- **Dashy** ist optisch stark anpassbar, **Homarr** folgt einem einheitlichen Look

### Dashy vs. Heimdall
- **Dashy** nutzt Sektionen mit vielen Optionen pro Kachel, **Heimdall** Panels mit Kacheln und Enhanced Apps
- **Dashy** hat eine dokumentierte REST-API, **Heimdall** nicht
- **Heimdall** ist in den Möglichkeiten schmaler und dadurch schneller erfasst

### Dashy vs. Homer
- **Beide** sind dateibasiert, **Dashy** zusätzlich mit Serverfunktionen: Login, Statusprüfung, API, Config-Schreibzugriff
- **Homer** ist deutlich leichter und ohne jede Laufzeitlogik
- **Dashy** kann statisch gehostet werden, verliert dann aber Statusprüfungen und API

## Technische Details

- **Backend**: optional ein Node-Server (Express), der Statusprüfungen, Auth, Config-Zugriff und die API übernimmt
- **Database**: keine; Zustand liegt in `conf.yml`/`conf.json` und im lokalen Browserspeicher
- **Frontend**: Vue-Anwendung (historisch Vue 2, neuere Versionen mit Vite gebaut), responsive Darstellung
- **Authentication**: HTTP-Basic über den Server, OIDC-Provider (Keycloak, Zitadel u. a.), lokale Nutzer mit gehashten Schlüsseln, Rollen (Admin/Nutzer), optional Zwei-Faktor-Authentifizierung, Mindestrolle pro Funktion
- **Hosting**: Docker-Image (LinuxServer.io oder Original), Bare-Metal mit Node, statisch auf jedem Webserver/CDN (dann ohne Serverfunktionen)

## Für wen ist Dashy geeignet?

- **Admins, die ihre Startseite als Code** verwalten und trotzdem eine Oberfläche zum Nachziehen brauchen
- **Nutzer, die Statusanzeigen und Widgets** auf einer Seite sehen wollen
- **Umgebungen mit Anmeldung**, etwa Familien-Dashboards mit unterschiedlichen Rollen
- **Weniger geeignet** für reine Linklisten ohne Ansprüche (dann Homer) oder für Teams, die keine Dateien anfassen wollen (dann Homarr)
