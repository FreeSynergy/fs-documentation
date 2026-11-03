# Homepage - Funktionen

## Übersicht

Homepage kennt drei Konfigurationsebenen: **Einstellungen** (`config/settings.yaml`) steuern Aussehen und Verhalten, **Dienste** (`config/services.yaml`) bauen die Kacheln inklusive Service-Widgets, und **Informations-Widgets** (`config/widgets.yaml`) füllen Kopf- und Fußzeile. Ergänzende Dateien beschreiben Container (`docker.yaml`), Pods (`kubernetes.yaml`), Lesezeichen (`bookmarks.yaml`) und Proxmox (`proxmox.yaml`).

---

## 1. Seitenlayout und Kopfzeile

- **Kopfzeile** mit Begrüßung, Uhrzeit/Datum, Suchleiste und frei mischbaren Informations-Widgets
- **Fußzeile** mit eigenem Text (`footer`)
- **Layout-Angabe** in `settings.yaml`: Reihenfolge und Spaltenverteilung der Gruppen, `columns` für das Kachelraster
- **Startseiten-Optionen**: `header`, `footer`, `widgets` oben/unten, Anzeige von Versions- und Update-Hinweisen
- **Sprache und Formatierung**: `language`, 12-/24-Stunden-Uhr, Datumsmasken, Zeilenumbruch pro Gruppe

## 2. Dienstgruppen und Kacheln

- **Gruppen** (`services.yaml`): eigene Namen, beliebige Anzahl, Anordnung über das Layout
- **Kachel**: `href`, `icon` (aus mitgelieferten Icon-Sets, eigene SVG unter `config/icons/`), `description`, `namespace`
- **Klickverhalten**: `settings.yaml → launch` steuert gleicher Tab oder neuer Tab
- **Eigene Klassen/Farben** über `class` und Custom-CSS
- **Unterbau aus Docker/Kubernetes**: Gruppen können aus Labels bzw. Annotations automatisch gefüllt werden

## 3. Service-Widgets (Live-Daten an der Kachel)

- **Ein Widget pro Kachel** durch Schlüssel `_<dienst>` in `services.yaml`, z. B. `_sonarr`, `_pihole`, `_qbittorrent`
- **Breites Angebot** (Auszug): Sonarr, Radarr, Lidarr, Prowlarr, Bazarr, qBittorrent, Transmission, SABnzbd, Deluge, Jellyfin, Plex/Tautulli, Emby, Pi-hole, AdGuard Home, NextDNS, UniFi, Tailscale, OPNsense, pfSense, Proxmox, Portainer, Uptime Kuma, Healthchecks, Immich, Nextcloud, Home Assistant, Paperless-ngx, Grafana, Prometheus, ntfy, Gotify
- **Mehrere Zeilen pro Widget**: Beispiel qBittorrent zeigt Up/Down-Geschwindigkeit und aktive Tasks, Jellyfin zeigt aktive Streams
- **Schema je Dienst** hinterlegt: Welche Endpunkte abfragbar sind, prüft die Anwendung beim Validieren der Konfiguration
- **Custom-API-Widget**: beliebiger HTTP-Endpunkt plus JSON-Pfad → eigene Zahl ohne Quellcode

## 4. Informations-Widgets

- **search**: Suchleiste mit Anbietern (`duckduckgo`, `google`, `bing`) oder eigener Such-URL, Vorschläge über `/api/search/searchSuggestion`
- **resources**: CPU, RAM, Festplatte des Hosts (Container mit `/proc`-Zugang) oder über Glances
- **glances / myspeed / speedtest**: Messwerte externer Dienste
- **weather, openweathermap, openmeteo**: Wetter mit Einheiten und Standort
- **stocks, date, datetime, greeting, logo, longhorn, kubernetes, unifi_controller, customapi**
- **Position**: `position` (links/rechts/oben/unten) und Reihenfolge in `widgets.yaml`

## 5. Docker- und Kubernetes-Integration

- **Docker-Socket** in den Container einhängen (`/var/run/docker.sock:ro`) oder TCP-Endpunkt nutzen
- **Labels** am Container erzeugen Kacheln: `homepage.group`, `homepage.url`, `homepage.name`, `homepage.icon`, `homepage.directory`, `homepage.style`
- **`docker.yaml`**: Zuordnung Container ↔ Dienst, damit Service-Widgets die richtige Instanz ansprechen
- **Kubernetes**: Provider `kubernetes` in `settings.yaml`, Pods/Deployments mit `homepage.*`-Annotations, `kubernetes.yaml` für Gruppierung und Namespaces
- **Statusanzeigen**: `running`, `exited`, `paused` mit eigener Farbe über Custom-CSS

## 6. Konfiguration und Betrieb

- **Dateien** im Volume `/app/config`: `settings.yaml`, `services.yaml`, `widgets.yaml`, `bookmarks.yaml`, `docker.yaml`, `kubernetes.yaml`, `proxmox.yaml`
- **Secrets** über Umgebungsvariablen: `HOMEPAGE_VAR_*` (Wert) und `HOMEPAGE_FILE_*` (Dateiinhalt), ersetzt als `{{HOMEPAGE_VAR_X}}` in jeder Config-Datei
- **Notwendige Umgebungsvariablen**: `HOMEPAGE_ALLOWED_HOSTS` (Host-Header-Prüfung), optional `PUID`/`PGID`, `PORT`
- **Optionale Anmeldung**: `HOMEPAGE_AUTH_ENABLED` mit `NEXTAUTH_SECRET` bzw. `HOMEPAGE_AUTH_SECRET` und `NEXTAUTH_URL`/`HOMEPAGE_EXTERNAL_URL`
- **Prüfen der Dateien**: die Anwendung loggt Konfigurationsfehler strukturiert; im Docker-Log erscheinen Widget- und YAML-Fehler mit Datei und Schlüssel
- **Änderungen wirksam**: Datei speichern, Seite neu laden; kein Neustart nötig, außer bei Umgebungsvariablen

## 7. Was Homepage NICHT kann

- **Keine Weboberfläche zum Bearbeiten**: Layout und Widgets entstehen ausschließlich in YAML
- **Keine Benutzer, Rollen oder Passwörter** (Standardinstallation): die Seite ist für alle, die sie erreichen, identisch
- **Keine Datenbank und kein Sitzungszustand**: keine gespeicherten Einstellungen pro Besucher
- **Kaum Aktionen**: Homepages Widgets lesen überwiegend; Container steuern oder Requests freigeben gehört nicht zum Funktionsumfang
- **Kein Monitoring mit Alarmierung**: Werte sind Momentaufnahmen, keine Langzeitkurven mit Alerts
- **Kein Plugin-Markt**: neue Integrationen sind Quellcode-Beiträge im Repository
- **Keine native Mobile-App**: Anzeige im Browser, mobil anders angerastert
- **Kein Multi-Tenant**: eine Instanz = ein Dashboard

## 8. Erweiterungen und eigene Anpassungen

- **`custom_css.css` und `custom_js.js`** im Config-Ordner: eigenes Design, eigene Logik im Browser
- **Custom-API-Widgets** (`_customapi`, Info-Widget `customapi`) für beliebige JSON-Quellen
- **Eigene Widget-Module**: Modulordner unter `src/widgets/<name>/` mit Deskriptor, Proxy-Handler und React-Komponente; Details in [../gethomepage/api.md](../gethomepage/api.md)
- **Icon-Sets**: mitgelieferte Sets (darunter `icons`-Schlüssel), eigene SVGs im Config-Ordner
- **Bookmarks** (`bookmarks.yaml`) als Lesezeichenleiste in der Kopfzeile
- **MCP-Endpunkt** (`/api/mcp`, standardmäßig deaktiviert) für KI-Assistenten, die Konfigurationsdateien lesen und – wenn erlaubt – schreiben dürfen
- **Sprachdateien**: Übersetzungen werden im Projekt gepflegt und per Release ausgeliefert

---

## Vergleich mit den anderen Dashboard-Typen

| Funktion | Homepage | Homer | Dashy | Homarr |
|----------|----------|-------|-------|--------|
| Konfiguration | `config/*.yaml` | `config.yml` | `conf.yml`/`conf.json` | Weboberfläche |
| Datenbank | keine | keine | keine | SQLite |
| Eigene Anmeldung | nein (optional aktivierbar) | nein | ja | ja |
| Live-Widgets | über 170 Module | keine | Status-Checks | Integrations-Widgets |
| Aktionen auf Infrastruktur | nein | nein | eingeschränkt | ja |
| Automatische Erkennung | Docker/Kubernetes | nein | nein | Docker |

---

## Siehe auch

- [menu.md](menu.md) - Bedienbereiche und Konfigurations-Menüs
- [structure.md](structure.md) - Seitenaufbau, Themes, Interaktionen
- [api.md](api.md) - Proxy-Endpunkte und Widget-Datenquellen
- [../gethomepage/index.md](../gethomepage/index.md) - Bibliotheksschicht der Widgets
