# Heimdall - Beschreibung

## Übersicht

Heimdall (Projekt `linuxserver/Heimdall`, heimdall.site) ist ein quelloffenes Dashboard, das Links zu den eigenen Webanwendungen als Kacheln anzeigt und sie auf Wunsch mit Live-Werten der jeweiligen Dienste anreichert. Es versteht sich als schlanke Startseite, nicht als Portal-Plattform.

## Was Heimdall macht

Heimdall stellt eine Weboberfläche mit **Panels** bereit: ein Panel enthält eine Gruppe von App-Kacheln, dazu kommen Such-, Statistik- und Hinweisbereiche. Apps sind Verknüpfungen mit Titel, URL, Icon und Farbe. Für viele bekannte Selbstbau-Dienste existieren **Enhanced Apps**: zuschaltbare Pakete, die den Dienst ansprechen und Zahlen wie blockierte Werbeanfragen, laufende Downloads oder Bibliotheksgrößen direkt in die Kachel schreiben. Server-Kacheln zeigen CPU, Arbeitsspeicher, Festplatte und Netzwerk des Heimdall-Rechners.

Das Projekt betont bewusst: keine eingebetteten Frames, keine Anwendungen in Anwendungen, keine Abstraktion fremder APIs.

## Vorteile

- **Schnell einsatzbereit**: Container starten, Admin-Konto anlegen, Apps eintragen
- **Klare Kachel-Optik**: große, gut lesbare Symbole statt kleinteiliger Widgets
- **Enhanced Apps**: Live-Daten bekannter Dienste ohne eigenen Code
- **Verschlüsselte Schlüssel**: API-Keys der Enhanced Apps liegen verschlüsselt in der Datenbank
- **Laravel-Basis**: bekannte PHP-Struktur, einfache eigene Anpassungen
- **Panel-Layout**: Bereiche lassen sich umbrechen, verschieben und ausblenden
- **Leichtgewichtig**: eine Anwendung, eine Datenbankdatei, kein Build-Schritt

## Abgrenzung zu anderen Systemen

### Heimdall vs. Homarr
- **Heimdall** arbeitet mit Panels und Kacheln, **Homarr** mit einem freien Widget-Raster (Resize, beliebige Positionen)
- **Homarr** kann Container starten und stoppen, **Heimdall** zeigt Daten an und verlinkt
- **Heimdall** konfiguriert Laufzeitdetails in `.env`, **Homarr** vollständig in der Oberfläche

### Heimdall vs. Homer
- **Homer** ist eine statische Seite ohne Backend, **Heimdall** ist eine PHP-Anwendung mit Datenbank und Login
- **Homer** wird in `config.yml` beschrieben, **Heimdall** über die Oberfläche gepflegt
- **Homer** hat keine Live-Werte, **Heimdall** zeigt Statistiken über Enhanced Apps

### Heimdall vs. Dashy
- **Dashy** wird überwiegend über `conf.yml`/`conf.json` gesteuert, **Heimdall** über die Oberfläche
- **Dashy** bietet ausgereiftes Theming, Statusprüfungen und eine optionale REST-API, **Heimdall** weder das eine noch das andere in dieser Form
- **Heimdall** ist in der Funktion überschaubarer, dafür in der Bedienung sehr direkt

## Technische Details

- **Backend**: PHP mit Laravel; Controller, Models und Blade-Templates
- **Database**: SQLite als Standard; MySQL/MariaDB und PostgreSQL über `.env` möglich
- **Frontend**: Blade-Templates mit jQuery (Kachel-Layout, Drag & Drop) und Chart-Anzeigen für Statistikwerte
- **Authentication**: lokale Konten (Standardinstallation ein Administratorkonto, neuere Versionen mit mehreren Nutzern); Login bei Bedarf deaktivierbar; Single-Sign-On nur über einen Reverse Proxy
- **Secrets**: Zugangsdaten der Enhanced Apps werden mit dem Laravel-`APP_KEY` verschlüsselt gespeichert
- **Hosting**: Docker-Image von LinuxServer.io (Port 80/443, häufig 8080), auch Bare-Metal mit PHP-FPM und Webserver; persistente Volumes für Datenbank und Hochladen-Icons

## Für wen ist Heimdall geeignet?

- **Nutzer, die eine aufgeräumte Link-Startseite** mit einigen Live-Kacheln wollen
- **PHP-/Laravel-Nutzer**, die Anpassungen im Quellcode bevorzugen
- **Homelabs mit bekannten Diensten** (Medienserver, Download-Clients, Werbefilter), für die Enhanced Apps existieren
- **Weniger geeignet** für feingliedrige Dashboards mit vielen verschiedenen Widgets (dann Homarr oder Dashy) oder für installationsfreie Umgebungen (dann Homer)
