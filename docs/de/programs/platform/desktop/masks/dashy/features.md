# Dashy - Funktionen

## Übersicht

Dashy verbindet zwei Welten: eine **textbasierte Konfiguration** (`conf.yml`, alternativ JSON) und eine **reiche Oberfläche** mit Statusanzeigen, Widgets, Ansichten, Themes und optionalem Schreibzugriff über Editor oder REST-API. Was die Datei beschreibt, rendert die Vue-Anwendung; was der Server ergänzt, sind Prüfungen, Anmeldung und API.

---

## 1. App-Kacheln

- **Felder pro Kachel**: `title`, `url`, `description`, `icon`, `target`/Öffnungsart, `keywords`/`tags`, `colour`
- **Öffnungsarten**: gleicher Tab, neuer Tab, neuer Fenster-Pop-up, Modal, Arbeitsbereich (Workspace), in die Zwischenablage kopieren
- **Tags**: machen Kacheln auffindbar, auch wenn der Begriff nicht in Titel oder URL steht
- **URL-Aliasse**: `alias` erlaubt den Sprung per Adresse, etwa `dashy.local/jelly`
- **Ausblendbar auf der Startseite**: `displayData.hideFromHomepage`, die Kachel bleibt in Suche und Workspace sichtbar
- **Hotkeys**: `hotkey` mit Ziffer `0`–`9` startet eine Kachel per Tastendruck
- **Darstellungsoptionen**: kompakte Kachel, Name ausblenden, Symbol ausblenden, Schriftgröße, eigene Farbe, Rahmenlos

## 2. Sektionen und Seiten

- **Sektionen** (`sections`) gruppieren Kacheln, mit Überschrift, eigenem Layout und optionalen Widgets
- **Unterseiten** (`pages`) liegen in eigenen Konfigurationsdateien und erscheinen im Seitenmenü
- **Spaltenanzahl** pro Sektion steuerbar, Kacheln rasten in ein Raster
- **Reihenfolge** folgt der Datei; im Bearbeitungsmodus per Drag & Drop änderbar

## 3. Statusprüfungen

- **Global einschaltbar** über die Konfiguration; danach prüft der Server jede Kachel
- **Prüf-URL pro Kachel** möglich, wenn die Ziel-URL nicht direkt testbar ist
- **Erwartete Antwort** konfigurierbar (Antworttext/Status), damit „erreichbar, aber kaputt“ erkennbar wird
- **Zustände**: unbekannt, prüft, erreichbar, nicht erreichbar, Fehler — als Punkt an der Kachel
- **Intervall** einstellbar; sehr kurze Intervalle erhöhen die Last spürbar
- **Hinweis**: Bei rein statischem Hosting (CDN, Netlify) entfallen die Prüfungen, weil kein Server mitprüft

## 4. Suche und Startseiten-Funktionen

- **Sofortsuche**: Tippen filtert sofort, ohne ein Feld zu fokussieren; behandelt Groß-/Kleinschreibung und Tippfehler großzügig
- **Suchfelder**: Titel, URL, Anbieter, Beschreibung, Alias und `tags`
- **Websuche**: `Enter` sendet den Begriff an eine eingestellte Suchmaschine (DuckDuckGo, Google, Brave, Searx, Whoogle über eigene URL u. v. m.)
- **Eigene Kurzkommandos** (`searchBangs`): `/w Begriff` öffnet Wikipedia, `:git Begriff` öffnet GitHub usw.
- **URL direkt öffnen**: sieht der Begriff wie eine URL aus, springt Dashy direkt dorthin (abschaltbar)
- **OpenSearch**: Dashy meldet sich als Suchmaschine im Browser an (`/opensearch.xml`)
- **Launchpad**: alle Kacheln aller Seiten in einer Rasteransicht

## 5. Ansichten

| Ansicht | Zweck |
|---------|-------|
| Startseite | normale Ansicht mit Sektionen und Widgets |
| Minimal | Kopfzeile, Suchfeld, Kacheln ohne Beiwerk |
| Workspace | eine Sektion groß dargestellt, gut für Bildschirmfüller |
| Login | Anmeldebildschirm bei konfigurierter Authentifizierung |
| Download | Konfiguration herunterladen (wenn erlaubt) |

## 6. Widgets

- **Eingebaute Typen** (Auswahl, je nach Version): Uhr, Wetter, RSS-Feeds, Börsen- und Kryptowerte, Nachrichtenübersicht, Arbeitsstatus, eingebettete Seite per iframe
- **Einbindung** pro Sektion: Typ, Optionen, Aktualisierungsintervall, Ausrichtung
- **Eigene Widgets**: Vue-Komponente im dafür vorgesehenen Ordner der Benutzerdaten; für rein statischen Betrieb ist ein Build nötig
- **Keine Aktionen**: Widgets zeigen Werte an, sie starten keine Container und rufen keine Schreib-APIs befreundeter Dienste auf

## 7. Themes und Darstellung

- **Viele eingebaute Schemata** (hell, dunkel, farbig), per Konfiguration und im Theme-Editor anwendbar
- **Eigene Werte** über CSS-Variablen; eigenes Stylesheet zusätzlich einbindbar
- **Pro Sektion/Kachel** Farben und Dichte einstellbar
- **Schriftarten**, Icon-Größen und Abstände konfigurierbar
- **Mehrsprachigkeit**: Oberfläche in vielen Sprachen, über `appConfig.lang`

## 8. Authentifizierung und Rollen

- **HTTP-Basic-Auth** über den Server (Nutzer/Passwort per Umgebungsvariable)
- **OIDC-Provider** (Keycloak, Zitadel und andere) für Single-Sign-On
- **Lokale Nutzer** mit gehashten Schlüsseln, Rollen `admin` und `user`, optional Zwei-Faktor-Code
- **Mindestrolle** für Funktionen wie Bearbeiten, Export oder API-Schreibzugriff
- **Konfiguration ausblenden**, wenn niemand Schreibzugriff haben soll

## 9. Konfiguration

- **Datei**: `user-data/conf.yml` (YAML) oder `conf.json`; mehrere Unterseiten in eigenen Dateien
- **Interaktiver Editor** in der Oberfläche: Sektionen, Kacheln, Themes, Grundeinstellungen bearbeiten und speichern
- **Optionale REST-API** für Lese- und Schreibzugriff (muss per `ENABLE_API=true` aktiviert werden)
- **Sicherung**: Jede Schreibaktion legt eine zeitgestempelte Sicherung in `user-data/config-backups/` ab
- **Import/Export** der Datei, optional Cloud-Sicherung mit Schlüssel
- **Grenzen**: geschriebene Dateien verlieren Kommentare und Formatierung, Größe ist begrenzt, gleichzeitige Schreiben folgen „letzter gewinnt“

## 10. Was Dashy NICHT kann

- **Keine Container-Steuerung**: kein Start, Stopp oder Neustart von Docker-Containern
- **Keine Datenbank**: alle Änderungen landen in der Konfigurationsdatei, es gibt keine Laufzeit-Datenhaltung
- **Keine Webhooks** und keine Ereignisausgänge
- **Kein Monitoringsystem**: Statuspunkte sind Momentaufnahmen ohne Historie und Alarme
- **Kein Plugin-Marktplatz**: eigene Widgets und Seiten erfordern Dateien und teilweise einen Build
- **Keine feinen Rechte pro Kachel**: Sichtbarkeit steuert über Rollen und Anzeigeeigenschaften, nicht über Gruppen pro Objekt
- **Serverfunktionen entfallen beim statischen Hosting** (Statusprüfungen, Auth, API)

## 11. Erweiterungen

- **Eigene Widgets** (Vue-Komponente) und **eigene Ansichten** im Projekt
- **Eigenes CSS/Themes** für vollständige optische Anpassung
- **REST-API** für Automatisierung: Kacheln anlegen, ändern, löschen, Seiten austauschen
- **Integration in Deployments**: Konfiguration im Git, Deployment prüft die Datei gegen das mitgelieferte Schema
- **Anbindung nach außen**: Verlinken auf Portale, Shortener oder Monitoring-Systeme statt eigener Funktion

---

## Vergleich der Dashboard-Typen

| Funktion | Dashy | Homarr | Heimdall | Homer |
|----------|-------|--------|----------|-------|
| Konfiguration | Datei + Editor + API | Oberfläche | Oberfläche + `.env` | Datei |
| Statusprüfungen | Ja | Ja (Integrationen) | Teilweise | Nein |
| Container-Aktionen | Nein | Ja | Nein | Nein |
| Themes | Sehr umfangreich | Mittel | Begrenzt | Begrenzt |
| Auth eingebaut | Ja | Ja | Ja | Nein |

---

## Siehe auch

- [menu.md](menu.md) - Kopfzeile, Einstellungspanel, Rechtsklick-Menüs
- [structure.md](structure.md) - Ansichten, Raster und Widgets
- [api.md](api.md) - REST-API und Authentifizierung
- [shortcuts.md](shortcuts.md) - Tastatur und Hotkeys
