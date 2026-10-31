# Heimdall - Funktionen

## Übersicht

Heimdall besteht aus drei Elementen: **Apps** (Kacheln als Links), **Panels** (bereicheute Sammlungen von Kacheln und Inhalten) und **Enhanced Apps** (Pakete, die Live-Daten eines Dienstes in eine Kachel schreiben). Dazu kommen Server-Statistiken des Heimdall-Rechners und eine Verwaltung für Konten und Layouts.

---

## 1. Apps (App-Kacheln)

- **Anlegen**: Titel, Ziel-URL, Icon, Hintergrundfarbe
- **Icons**: hochladen, aus mitgelieferten Icon-Sets wählen oder automatisch das Favicon der Ziel-URL verwenden
- **Zielverhalten**: Kachel im gleichen Tab oder in neuem Tab öffnen
- **Sortierung**: Kacheln per Drag & Drop innerhalb eines Panels anordnen
- **Farben**: freie Farbwahl pro Kachel, auch für Gruppenzuordnung nutzbar
- **Keine iframes**: Heimdall bettet Zielanwendungen nicht ein, es verlinkt nur

## 2. Enhanced Apps (Kacheln mit Live-Daten)

- **Prinzip**: ein Enhanced-App-Paket kennt den Dienst, fragt ihn serverseitig ab und rendert Werte in die Kachel
- **Typische Dienste** (Auswahl versionsabhängig): Pi-hole, NZBGet, Sonarr, Radarr, Emby, Plex, Portainer, Transmission, NZBHydra2, Jackett, Bazarr, Healthchecks, Miniflux
- **Zugangsdaten**: Ziel-URL plus API-Key oder Benutzername/Passwort, getrennt pro App pflegbar
- **Verschlüsselung**: die Werte werden mit dem Laravel-`APP_KEY` verschlüsselt in der Datenbank gespeichert
- **Aktualisierung**: Werte werden beim Aufruf der Seite geholt; fehlerhafte Verbindungen erscheinen als Hinweis in der Kachel
- **Installation**: Pakete werden als Composer-Abhängigkeit ergänzt (in Docker-Installationen über den mitgelieferten Mechanismus des Images)

## 3. Server-Statistiken

- **Anzeige**: CPU-Auslastung, Arbeitsspeicher, Festplattennutzung, Netzwerkverkehr des Rechners, auf dem Heimdall läuft
- **Darstellung**: Zahlen und kleine Diagramme in eigenen Panels
- **Herkunft**: Werte werden lokal auf dem Server ausgelesen, nicht über das Netzwerk abgefragt
- **Grenze**: Momentaufnahme beim Seitenaufruf, keine Langzeitkurven und keine Alarme

## 4. Panels und Layout

- **Panel-Arten**: App-Panel, Suchpanel, Statistik-Panels, Hinweis-/Supportbereich
- **Layout-Bearbeitung**: eigene Ansicht, in der Panels verschoben, umbrochen und ausgeblendet werden
- **Panel löschen/ausblenden**: ungenutzte Bereiche verschwinden aus der Ansicht
- **Mehrere Panels**: Inhalte lassen thematisch trennen, etwa „Medien“, „Network“, „System“
- **Layout pro Konto**: die Anordnung wird je Nutzer gespeichert

## 5. Suche

- **Suchfeld** im Suchpanel der Startseite
- **Websuche**: Suchbegriff wird an eine eingestellte Suchmaschine übergeben (Standard: Google, weitere Anbieter konfigurierbar)
- **Keine Indexsuche** über alle Apps: der Name einer App wird nicht intern gefiltert, sondern nur über den Browser (Textsuche `Strg+F`) gefunden

## 6. Konten und Rechte

- **Standardinstallation**: ein Administratorkonto mit E-Mail-Adresse und Passwort, eingerichtet beim ersten Start
- **Mehrere Nutzer** (neuere Versionen): Anlegen über die Einstellungen, Rollen Administrator und normaler Nutzer
- **Eigenes Layout** je Nutzer, App-Verwaltung je nach Rolle
- **Login abschalten**: für Installationen, die vollständig hinter einem Proxy geschützt sind (versionsabhängige Einstellung)
- **Öffentliche Ansicht**: Mechanismen, ein Dashboard ohne Anmeldung sichtbar zu machen (versionsabhängig, vorsichtig einsetzen)

## 7. Konfiguration

- **`.env` im Projekt**: `APP_KEY` (verschlüsselt Secrets, unbedingt stabil halten), `APP_URL`, Datenbankverbindung, optionale Auth-Einstellungen
- **Persistente Daten**: Datenbankdatei (SQLite) sowie hochgeladene Icons und eigene Dateien in Volumes sichern
- **Webserver-Ebene**: Zeitzone, Speicher- und Ausführungszeiten für PHP; HTTPS über Reverse Proxy
- **Update**: neues Image ziehen oder Quellcode aktualisieren, danach `php artisan`-Schritte für Migrationen und Cache

## 8. Anpassung

- **Kachelfarben** und Icons als wichtigste Gestaltungsmittel
- **Eigenes CSS/Theme-Dateien**: eigene Stylesheets können eingebunden werden; ein Theme-Katalog wie bei Dashy existiert nicht
- **Support-/Hinweisbereich**: Meldungen des Projekts (abschaltbar, versionsabhängig)
- **Logo und Titel**: über die Einstellungen bzw. Template-Dateien änderbar

## 9. Was Heimdall NICHT kann

- **Keine Container-Steuerung**: kein Start, Stopp oder Neustart von Docker-Containern
- **Kein freies Raster**: Kacheln sitzen in Panels, Größe und Position sind an das Panel-System gebunden
- **Keine Statusprüfungen** im Stil von Dashy (weder Ampeln für alle Links noch einstellbare Prüfintervalle)
- **Keine dokumentierte API** für Automatisierung und keine Webhooks
- **Kein Monitoring**: keine Historie, keine Benachrichtigungen, keine Schwellwerte
- **Kein Single-Sign-On**: OIDC/LDAP werden nicht angeboten, ein Reverse Proxy muss das übernehmen
- **Keine mehrsprachige Oberfläche** in allen Versionen; Inhalte sind englischsprachig
- **Kein Rechte-System** mit feinen Berechtigungen pro Panel oder App

## 10. Erweiterungen und eigene Anpassungen

- **Enhanced-App-Pakete**: eigene Pakete schreiben (Laravel-Klasse plus Template), die einen Dienst abfragen
- **Eigenes CSS**: Farbschema, Abstände und Schrift anpassen
- **Template-Dateien (Blade)**: Kopfbereich, Fußzeile und Panels direkt verändern
- **Umgebungsvariablen des Images**: Zeitzone, Benutzer-/Gruppenkennung und Pfade für Docker-Betrieb
- **Datenbankanbindung wechseln**: SQLite gegen MySQL/MariaDB oder PostgreSQL tauschen, zum Beispiel für Backup-Konzepte

---

## Vergleich der Dashboard-Typen

| Funktion | Heimdall | Homarr | Homer | Dashy |
|----------|----------|--------|-------|-------|
| Kacheln mit Live-Daten | Ja (Enhanced Apps) | Ja (Integrationen) | Eingeschränkt | Ja (Widgets) |
| Container-Aktionen | Nein | Ja | Nein | Nein |
| Layout-Editor | Panels, eingeschränkt | Freies Raster | Nein | Raster über Config |
| Konfiguration | Oberfläche + `.env` | Oberfläche | `config.yml` | `conf.yml`/`conf.json` |
| API für Automatisierung | Nein | tRPC | Nein | Optionale REST-API |

---

## Siehe auch

- [menu.md](menu.md) - Menüpunkte und Kontextmenüs
- [structure.md](structure.md) - Panel- und Kachelstruktur
- [api.md](api.md) - Routen, Enhanced Apps und Schlüssel
- [shortcuts.md](shortcuts.md) - Tastatursteuerung
