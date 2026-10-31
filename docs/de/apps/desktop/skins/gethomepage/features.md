# gethomepage (Bibliothek) - Funktionen

## Übersicht

Die Bibliotheksschicht von Homepage besteht aus **Deskriptoren** (was ein Dienst kann), **Handlern** (wie angefragt wird), **Konfigurationslesern** (aus `config/*.yaml` wird ein Widget-Objekt) und **Werkzeugen** (URL-Bau, Cookies, Caching, Prüfung, Log). Dieser Artikel beschreibt, welche Funktionen diese Schicht bietet – ohne Benutzeroberfläche, ohne Menüs.

---

## 1. Dienst-Deskriptoren (je Modul eine Datei)

- **API-Schablone**: `api: "{url}/api/v3/{endpoint}?apikey={key}"` – Platzhalter werden aus Kachel- und Widget-Angaben gefüllt
- **Mehrere Schablonen**: Dienste mit alt/neu (z. B. Pi-hole `api` und `apiv5`)
- **Endpunkt-Zuordnungen** (`mappings`): Name → echter Endpunkt, erlaubte Methode, optionale Query-Parameter, Segmente
- **Antwort-Formung** (`map`): Felder reduzieren, sortieren, umbenennen – der Browser erhält nur Relevante
- **Antwort-Prüfung** (`validate`): erwartete Schlüssel müssen vorkommen, sonst gilt die Anfrage als Fehler
- **Standard-Handler oder Sonder-Handler**: `proxyHandler` zeigt auf ein Modul mit eigenem Ablauf
- **Feldvorgaben für die Config** (`fields`): Pflichtfelder wie `key`, `key2`, `version`, `watch` – geprüft, bevor die Seite zeichnet

## 2. Handler-Typen

- **Generischer HTTP-Handler**: gebaut auf `follow-redirects`, behandelt Redirects, Timeout, Statuscodes
- **Handler mit Anmelde-Schritt**: erst Login (z. B. qBittorrent, Synology, UniFi), dann Fachanfrage mit gespeicherten Cookies
- **JSON-RPC-Handler**: Umschlag nach `json-rpc-2.0` für RPC-Dienste (z. B. Docker-API-ähnliche Dienste, Media-Server)
- **Sonderhandler**: eigene Module für UniFi, Synology (`entry.cgi`) und Kalender (`ical.js`)
- **Roh-Schicht**: `httpProxy` für eine einzelne Anfrage, `cachedRequest` für eine Anfrage mit Cache-Fenster
- **Header-Kontrolle**: zusätzliche Header je Zuordnung (`mapping.headers`), etwa Content-Type oder API-Version

## 3. Konfigurationsleser

- **YAML-Laden**: `settings.yaml`, `services.yaml`, `widgets.yaml`, `bookmarks.yaml`, `docker.yaml`, `kubernetes.yaml`, `proxmox.yaml`
- **Vorlage und Fallback**: fehlt eine Datei, wird eine Beispielkopie angelegt, damit die Seite zeichnen kann
- **Widget-Auflösung**: `getServiceWidget(group, service, index)` liefert Name, Typ, URL, Schlüssel und Felder einer Kachel
- **Dienst-Helfer**: Gruppen- und Dienstsuche, Zähler für Mehrfach-Widgets derselben Art
- **Variablen-Ersetzung**: `{{HOMEPAGE_VAR_*}}` und `{{HOMEPAGE_FILE_*}}` werden vor dem Parsen eingesetzt
- **Pfadzugriff auf Werte** über einen kleinen Getter für verschachtelte Angaben
- **Validierung**: Parse-Fehler melden Datei, Grund und Zeile (auch über `/api/validate` abrufbar)

## 4. Anfrage-Werkzeuge

- **URL-Bau**: `formatApiCall(schablone, werte)` ersetzt Platzhalter und entfernt doppelte Schrägstriche
- **Proxy-URL-Bau**: `formatProxyUrl(widget, endpoint, queryParams)` erzeugt die Adresse für den Browser
- **Cookie-Ablage**: eigener Cookie-Jar auf Basis von `tough-cookie` für Dienste mit Sitzungs-Login
- **Antwort-Helfer**: `asJson`, `jsonArrayTransform` und Vergleichs-/Versionshilfen
- **Caching**: `memory-cache` mit kurzem Zeitfenster, identische Schlüssel bündeln sich
- **Spezialclients**: Docker-Socket (`dockerode`), Kubernetes (`@kubernetes/client-node`), Systemwerte (`systeminformation`), Ping (`ping`), Game-Server (`gamedig`), Backup (`urbackup-server-api`)

## 5. Browser-seitiger Datenfluss

- **Hook `useWidgetAPI(widget, endpoint, queryParams)`**: baut die Proxy-URL, fragt per SWR ab, liefert `{ data, error, mutate }`
- **Aktualisierungsintervall**: aus Widget-Angabe `refreshInterval` ableitbar
- **Fehler nach oben**: ein Fehler in der Antwort (`data.error`) wird als Top-Level-Fehler exponiert
- **Kein direkter Dienstzugriff im Browser**: CORS-Probleme und Schlüsselabfluss sind damit ausgeschlossen
- **Ladezustand**: Komponenten zeigen Platzhalter, bis die Proxy-Antwort eintrifft

## 6. Protokoll und Diagnose

- **Strukturierter Log** mit Namensraum je Schicht (`servicesProxy`, `siteMonitor`, `config`), geschrieben über `winston`
- **Debug-Stufen** über Log-Level, fehlerhafte Schalter werden nicht ins Protokoll geschrieben
- **Sichtbare Fehlerquellen**: unbekannte Typen, unverträgliche Methoden, unbekannte Endpunkte, manipulierte Segmente
- **Kein Trace der Schlüssel**: Logzeilen nennen Dienst und Endpunkt, nicht die Zugangsdaten

## 7. Was die Bibliothek NICHT kann

- **Keine eigene Oberfläche**: keine Menüs, keine Dialoge, keine Konfigurationsansicht
- **Kein npm-Paket**: nicht als Bibliothek veröffentlicht, daher kein `npm install` für eigene Projekte
- **Keine Schreibzugriffe auf Dienste**: Homepages Widgets lesen; Befehle an Dienste abzusetzen ist bewusst nicht vorgesehen
- **Keine Langzeitmessung**: keine Historie, keine Alarmierung, keine Kurven über Stunden
- **Keine Plugin-Schnittstelle zur Laufzeit**: neue Clients sind Quellcode-Dateien im Repository
- **Keine Persistenz**: nach einem Neustart sind Caches und Sitzungs-Cookies leer
- **Keine Mandantenfähigkeit**: eine Konfiguration, ein Satz Schlüssel, keine Trennung nach Gruppen

## 8. Erweiterungen und eigene Clients

- **Neuer Dienst**: Ordner unter `src/widgets/<name>/` mit `widget.js` (Deskriptor), optional `proxy.js` (Handler) und `component.jsx` (Anzeige im Dashboard)
- **Registry pflegen**: Eintrag in `src/widgets/widgets.js`, damit `type` und Felder bekannt sind
- **Vorhandene Endpunkte freischalten**: `mappings` um einen Eintrag erweitern statt neuen Handler schreiben
- **Eigene Datenquellen ohne Code**: `customapi`-Widget mit URL und JSON-Pfad – läuft über denselben generischen Handler
- **Tests**: `*.test.js`/`*.test.jsx` neben der Datei, mit Vitest ausführbar
- **Sprachdateien**: für Fehler- und Beschriftungstexte im Dashboard-Teil zuständig

---

## Funktionen im Überblick

| Ebene | Baustein | Ergebnis |
|-------|----------|----------|
| Deskriptor | `widget.js` | erlaubte Endpunkte, Felder, Schablonen |
| Handler | `proxy.js`, `utils/proxy/handlers/*` | fertige HTTP-/RPC-Antwort |
| Config | `utils/config/*` | Widget-Objekt aus YAML |
| Werkzeug | `utils/proxy/api-helpers.js`, `http.js`, `cookie-jar.js` | URL, Anfrage, Cookies |
| Client | `utils/proxy/use-widget-api.js` | Daten im Dashboard |
| Diagnose | `utils/logger.js`, `/api/validate` | nachvollziehbare Fehler |

---

## Siehe auch

- [menu.md](menu.md) - Modul- und Paketverzeichnis
- [structure.md](structure.md) - Ebenen und Aufrufpfad
- [api.md](api.md) - Clients, Methoden und Parameter
- [../homepage/index.md](../homepage/index.md) - Dashboard-Anwendung
