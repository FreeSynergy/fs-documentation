# Homer - Beschreibung

## Übersicht

Homer (Projekt `bastien64/homer`, Container-Image `b4bz/homer`) ist ein bewusst einfaches, statisches Dashboard. Eine YAML-Datei beschreibt Gruppen, Kacheln und Links; eine kleine Single-Page-Anwendung liest diese Datei im Browser und rendert die Startseite.

## Was Homer macht

Homer zeigt eine einzige Seite: Kopfzeile mit Titel, optionale Icon-Links, optional ein Suchfeld, darunter mehrere Spalten mit Gruppenüberschriften und Kacheln. Jede Kachel ist ein Link zu einem Dienst, sichtbar über Icon und Namen. Die Datei `assets/config.yml` enthält die komplette Beschreibung; sie wird zur Laufzeit geladen und kann über einen Query-Parameter gewechselt werden. Eine Benutzerverwaltung, Live-Statuswerte oder Aktionen gegen Dienste gibt es nicht.

## Vorteile

- **Winzig und schnell**: statische Dateien, keine Datenbank, keine laufende Anwendung
- **Konfiguration als Textdatei**: versionierbar in Git, in Sekunden geprüft
- **Kein Wartungsaufwand**: keine Migrationen, keine Updates von Abhängigkeiten im Betrieb
- **Mehrere Instanzen möglich**: verschiedene `config.yml` für verschiedene Teams oder Geräte
- **Beliebig hostbar**: nginx, Apache, object storage, GitHub Pages, auch `file://`
- **Sauberes Design**: helles und dunkles Schema, eigenes CSS über CSS-Variablen
- **Günstig in Ressourcen**: läuft auf einem Raspberry Pi ebenso wie auf einem CDN

## Abgrenzung zu anderen Systemen

### Homer vs. Homarr
- **Homer** ist statisch, **Homarr** ist eine Anwendung mit Login, Datenbank und Rechten
- **Homer** ändert man in der Datei, **Homarr** per Drag & Drop in der Oberfläche
- **Homarr** greift aktiv auf Docker und Dienste zu, **Homer** verlinkt ausschließlich

### Homer vs. Heimdall
- **Heimdall** zeigt Live-Werten über Enhanced Apps, **Homer** bleibt bei Icon und Namen
- **Heimdall** pflegt Inhalte über die Oberfläche in einer Datenbank, **Homer** über die YAML-Datei
- **Homer** hat keinen Login, **Heimdall** bringt lokale Konten mit

### Homer vs. Dashy
- **Beide** arbeiten mit Config-Dateien, **Dashy** zusätzlich mit einer mächtigen Oberfläche und optionaler REST-API
- **Dashy** bietet Statusprüfungen, Widgets, Themes und Authentifizierung, **Homer** nichts davon
- **Homer** ist deutlich kleiner und schneller, **Dashy** funktionsreicher und schwerer

## Technische Details

- **Backend**: keins. Eine Vue-basierte Single-Page-Anwendung läuft vollständig im Browser
- **Database**: keine; Zustand existiert nur in der Config-Datei und im lokalen Browserspeicher (einzelne Vorlieben)
- **Frontend**: HTML, CSS und JavaScript; die Config wird als YAML zur Laufzeit geladen
- **Authentication**: nicht vorhanden. Schutz ausschließlich über Reverse Proxy (Basic Auth, Authentik/Authelia), Netzwerksegmentierung oder IP-Filter
- **Hosting**: nginx-basiertes Container-Image, jeder statische Webserver, Datei-Hosting, CDN; Updates durch Austauschen der Dateien

## Für wen ist Homer geeignet?

- **Nutzer mit überschaubarer Diensteliste**, die vor allem Links brauchen
- **Admins, die Konfiguration als Code** behandeln: Git, Pull Requests, CI/CD
- **Umgebungen ohne Wartungsfenster** (Off-Grid, Backup-Portal, Notfallseite)
- **Teams, die jedem dieselbe Startseite** zeigen wollen, ohne Konten zu verwalten
- **Weniger geeignet**, wenn Live-Status, Container-Aktionen oder individuelle Dashboards pro Person erwartet werden
