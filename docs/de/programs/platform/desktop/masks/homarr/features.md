# Homarr - Funktionen

## Übersicht

Homarr kombiniert drei Bausteine: **Boards** (Layout-Raster), **Widgets** (Inhaltskacheln) und **Integrationen** (Angaben zu Diensten samt URL und Schlüssel), die den Widgets Live-Daten und Aktionen liefern. Alles wird zur Laufzeit über die Weboberfläche geändert und in der SQLite-Datenbank abgelegt.

---

## 1. Boards (Dashboards)

- **Beliebig viele Boards**: zum Beispiel „Homelab“, „Medien“, „Familie“
- **Raster-Layout** mit einstellbarer Spaltenanzahl, Widget-Größe in Zeilen/Spalten, Verschieben per Drag & Drop
- **Getrennte Layouts** für Desktop und Mobilgerät (eigenes Raster pro Endgerät)
- **Sichtbarkeit**: öffentlich, nur eigene, oder für bestimmte Nutzer/Gruppen freigegeben
- **Duplizieren, Umbenennen, Löschen** sowie Start-Board pro Endgerät auswählbar
- **Zurücksetzen** einer versehentlich verbogenen Anordnung

## 2. Widgets (Kacheln)

### Struktur-Widgets
- **App-Kacheln**: Name, URL, Icon, Ziel (neuer Tab/gleicher Tab), optional Ordner-/Linklisten-Widget
- **Text, Bild, Einbettung (iframe), Lesezeichen-Liste** für reine Inhalte
- **Bruchstück-Kachel („public API“/JSON)**: zeigt Werte aus einer beliebigen JSON-Quelle über JSON-Pfade an

### Status- und Diagnose-Widgets
- **Statusanzeige** (Erreichbarkeit einer URL, grün/gelb/rot)
- **Server-/Board-Informationen**: Version, Host-Informationen, Uhrzeit/Datum
- **Diagramme** für Traffic und Auslastung (Datenquelle wird als Integration hinterlegt)

### Integrations-Widgets (Auswahl, je nach Version)
- **Docker**: Container-Liste mit Status, CPU/RAM, Aktionen (Stopp, Start, Neustart)
- **Portainer**: alternative Container-Ansicht für Portainer-Umgebungen
- **Pi-hole / AdGuard Home**: Blockstatistik, Aktivität
- **Downloads**: qBittorrent, Transmission, Deluge, SABnzbd (Aktivität, Kontingent)
- **Medien-Bibliotheken**: Jellyfin, Plex, Emby (aktive Streams, Bibliotheken)
- **Kalender**: Termine über CalDAV-Kalender
- **Medien-Requests**: Overseerr/Jellyseerr (ausstehende Anfragen)
- **Indexer**: Sonarr, Radarr, Prowlarr
- **Wetter, Suche, Benachrichtigungen, RSS** für informative Kacheln

## 3. Integrationen (Dienst-Anbindung)

- **Integration anlegen**: Typ auswählen, interne/externe URL, Schlüssel oder Benutzername/Passwort
- **Verbindungstest** direkt im Dialog („Verbindung testen“)
- **Mehrere Integrationen desselben Typs** möglich, Widgets zeigen die gewünschte Integration an
- **Aktionen** aus dem Widget heraus: Container-Neustart, Request genehmigen, Download-Pause
- **Schlüssel liegen verschlüsselt** in der Datenbank (Secrets werden mit dem Instanz-Secret verschlüsselt)

## 4. Suche und Startseiten-Funktionen

- Suchleiste im Kopfbereich, findet konfigurierte Apps/Links der Boards
- **Websuche** über eine einstellbare Suchmaschine, inklusive Kurzkommandos im Suchtext
- **Tastatur-Autocomplete** in Dropdowns und Auswahlfeldern
- **Nutzer-Einstellungen**: Standard-Suchmaschine, Verhalten von DuckDuckGo-Kurzkommandos, Suchverhalten

## 5. Authentifizierung, Rollen und Freigaben

- **Lokale Konten** mit Passwort (Registrierung abschaltbar), Einladungen für neue Nutzer
- **OIDC / Keycloak** für Single-Sign-On, optional header-basierte Authentifizierung hinter einem Reverse Proxy
- **Rollen**: Administrator, Mitglied, nicht zugewiesene bzw. Gast-Nutzer
- **Board-Berechtigungen**: Board-Besitz, Gruppenfreigabe, öffentliche Boards
- **Persönliche Einstellungen**: Farbschema, erstes Wochentag, Kopfzeilen-Layout, Rechtsklick auf Widgets

## 6. Konfiguration

- **Keine Config-Datei**: Boards, Widgets, Integrationen und Nutzer liegen in der Datenbank
- **Umgebungsvariablen** für den Start, insbesondere:
  - `SECRET_PASSWORD` (verschlüsselt Secrets, muss stabil bleiben)
  - `NEXTAUTH_SECRET` (Session-Signierung)
  - `DATABASE_URL` (Pfad zur SQLite-Datei)
  - Optionen für Registrierung, Header-Auth und Zeitzone
- **Datenverzeichnis** (Volume) enthält Datenbank und Uploads (Hintergrundbilder, Icons)
- **Backups**: Datenbankdatei und Volume sichern, damit Boards und Secrets erhalten bleiben

## 7. Was Homarr NICHT kann

- **Keine Konfiguration per Datei**: es gibt keine exportierbare YAML-Datei, die das Dashboard beschreibt
- **Kein Reverse-Proxy-Ersatz**: Homarr startet Dienste nur, es übernimmt kein Routing und keine Zertifikatsverwaltung
- **Kein Monitoring im Sinne von Prometheus/Grafana**: Statuswerte sind Momentaufnahmen, keine Langzeitmessung mit Alerts
- **Keine Offline-Nutzung**: ohne laufenden Server und Login funktioniert nichts
- **Keine klassische Plugin-API**: Erweiterungen sind Quellcode-Beiträge, kein zur Laufzeit installierbares Plugin-System
- **Kein Mobile-App-Ersatz**: Darstellung im Browser, keine nativen Apps
- **Keine Mandantenfähigkeit**: eine Instanz ist eine Gemeinschaft, keine getrennte Mehrkunden-Umgebung

## 8. Erweiterungen und eigene Anpassungen

- **Eigene Widgets**: im Quellcode als React-Komponente; für Homelabs bleibt der Weg der eigene Fork
- **JSON-/Public-API-Kachel**: Daten beliebiger HTTP-Endpunkte per JSON-Pfad anzeigen — ohne Code der einfachste Weg zur eigenen Kachel
- **Integrationen erweitern**: neue Integrationstypen werden im Repository gepflegt und über Releases ausgeliefert
- **CalDAV und RSS** als Standardwege für Kalender- und Nachrichten-Inhalte
- **Icon-Quellen**: lokale Uploads, mitgelieferte Icon-Sets sowie URLs
- **Updates über Container-Images** (z. B. mit Watchtower oder Compose-Neustart)

---

## Vergleich mit den anderen Dashboard-Typen

| Funktion | Homarr | Heimdall | Homer | Dashy |
|----------|--------|----------|-------|-------|
| Konfiguration | Weboberfläche | Weboberfläche + `.env` | `config.yml` | `conf.yml`/`conf.json` |
| Backend | Ja (Next.js) | Ja (Laravel) | Nein | Optional (Node) |
| Login/Rollen | Ja | Ja (einfach) | Nein (Proxy) | Ja |
| Container-Aktionen | Ja | Eingeschränkt | Nein | Nein |
| Theme-System | Ja | Begrenzt | Begrenzt | Sehr umfangreich |

---

## Siehe auch

- [menu.md](menu.md) - Menüpunkte und Bedienebenen
- [structure.md](structure.md) - Board-Aufbau und UI-Details
- [api.md](api.md) - tRPC-Verfahren und Integrations-Proxy
- [shortcuts.md](shortcuts.md) - Tastatursteuerung
