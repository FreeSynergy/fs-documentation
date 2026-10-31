# gethomepage (Bibliothek) - Modul- und Paketverzeichnis

## Übersicht

Diese Datei enthält **kein Benutzermenü**: Die Bibliotheksschicht von Homepage hat keine Oberfläche. Stattdessen ist sie das **Verzeichnis der Module und Pakete** im Quellbaum – das, was bei einer Anwendung die Menüpunkte wären. Nummerierung folgt der Aufrufreihenfolge: zuerst die Anfrage aus dem Browser, zuletzt die Hilfsfunktionen.

Pfadbezug: Repository `gethomepage/homepage`, Verzeichnis `src/`.

## Modulverzeichnis („Hauptmenüpunkte“ der Bibliothek)

### 1. Proxy-Eingang: `src/pages/api/services/proxy.js`
- **Funktion**: nimmt alle Widget-Anfragen des Browsers an (`/api/services/proxy`)
- **Details**:
  - Parameter: `group`, `service`, `index`, optional `endpoint`, `segments`, `query`
  - sucht das Widget über `getServiceWidget` und den passenden Deskriptor
  - bildet `endpoint` über `mappings` auf den echten Endpunkt ab (Whitelist)
  - lehnt unbekannte Typen, Methoden und Segmente mit `403` ab

### 2. Registry: `src/widgets/widgets.js`
- **Funktion**: zentrales Nachschlagewerk aller Widget-Typen
- **Details**: verknüpft `type` → Deskriptor, Feldvorgaben und Handler; bestimmt, welche Config-Schlüssel erlaubt sind

### 3. Dienst-Module: `src/widgets/<dienst>/`
- **Funktion**: ein Ordner je integriertem Dienst (über 170)
- **Details**:
  - `widget.js` – Deskriptor (`api`-Schablone, `mappings`, `fields`)
  - `proxy.js` – optionaler Spezial-Handler
  - `component.jsx` – Anzeige im Dashboard (gehört nicht zur Datenbeschaffung)
  - `*.test.js` / `*.test.jsx` – Tests zum Modul

### 4. Handler: `src/utils/proxy/handlers/`
- **Funktion**: führt die eigentliche Anfrage aus
- **Details**:

| Datei | Einsatz |
|-------|---------|
| `generic.js` | Standard für REST-Dienste mit API-Key oder offener API |
| `credentialed.js` | Dienste mit Benutzername/Passwort und Session |
| `jsonrpc.js` | JSON-RPC-Umschlag |
| `synology.js` | Synology `entry.cgi` inkl. Session-Ablauf, siehe [../synology-dsm/api.md](../synology-dsm/api.md) |
| `unifi.js` | UniFi-Controller mit eigenem Login-/Cookie-Ablauf |

### 5. Anfrage-Werkzeuge: `src/utils/proxy/`
- **Funktion**: Bausteine, die jeder Handler nutzt
- **Details**:
  - `api-helpers.js` – `formatApiCall`, `formatProxyUrl`, `getURLSearchParams`, `asJson`, `jsonArrayTransform`
  - `http.js` – `httpProxy`, `cachedRequest`, Redirect-Behandlung
  - `cookie-jar.js` – Sitzungs-Cookies für Login-Dienste (`tough-cookie`)
  - `validate-widget-data.js` – prüft erwartete Felder der Antwort
  - `use-widget-api.js` – Browser-Hook (SWR)

### 6. Konfigurationsschicht: `src/utils/config/`
- **Funktion**: YAML → Objekte, Prüfen, Fehler melden
- **Details**:

| Datei | Inhalt |
|-------|--------|
| `yaml.js` | YAML lesen, Vorlage anlegen, Ersetzung von `HOMEPAGE_VAR_*`/`HOMEPAGE_FILE_*` |
| `config.js` | Einstiegs- und Prüffunktionen, Konfigurationsverzeichnis |
| `service-helpers.js` | Dienst-/Widget-Suche, Gruppen, Indexbildung |
| `widget-helpers.js` | Widget-Felder und Vorgaben |
| `docker.js` / `kubernetes.js` / `proxmox.js` | Provider-Erkennung und Labels/Annotations |
| `dashboard.js` | zusammengesetzte Dashboard-Daten samt Cache-Verwurf |
| `api-response.js` | einheitliche Antworten für Routen |
| `shvl.js` | Werte in verschachtelten Strukturen lesen |

### 7. Infrastruktur-Module
- **Funktion**: Zugang zur Plattform statt zu Diensten
- **Details**:
  - `src/utils/docker/` – Container über den Docker-Socket (`dockerode`)
  - `src/utils/kubernetes/` – Pods/Deployments (`@kubernetes/client-node`)
  - `src/utils/weather/` – Wetteranbieter
  - `src/utils/logger.js` – strukturierter Log (`winston`)
  - `src/utils/env.js` – Umgebungsvariablen der Anwendung

### 8. Externe Abhängigkeiten der Schicht
- **Funktion**: fertig eingebundene Clients
- **Details**: `follow-redirects`, `tough-cookie`, `js-yaml`, `memory-cache`, `json-rpc-2.0`, `dockerode`, `@kubernetes/client-node`, `systeminformation`, `ping`, `gamedig`, `ical.js`, `luxon`, `urbackup-server-api`, `minecraftstatuspinger`

## Querschnittsmodule (entsprechen Kontext-Menüs)

| Modul | Querschnittsaufgabe |
|-------|---------------------|
| `src/utils/auth.js` | Host-Prüfung (`withAllowedHost`), Sitzungsprüfung (`withAuth`) für jede Route |
| `src/utils/highlights.js` | Hervorhebungs-/Farbregeln für Widget-Werte |
| `src/utils/widget-fields.js` | Prüft Pflichtfelder je Widget-Typ |
| `src/utils/styles/` | CSS-Helfer für das Dashboard |
| `src/utils/hooks/`, `src/utils/contexts/` | React-Bausteinen des Dashboard-Teils |
| `src/utils/mcp/` | Werkzeugfunktionen für den MCP-Endpunkt |

## Zugriff nach Rolle

Die Bibliothek hat keine Benutzer, aber Zugriffsstufen im Entwicklerbetrieb:

### Nutzer des Dashboards
- Sieht nur Ergebnisse; erreicht keine Moduldatei
- Kann über die Browser-Entwicklerwerkzeuge die Proxy-Antworten einsehen (inkl. sensibler Werte bei manchen Diensten)

### Betrieb / Admin (Deploy-Seite)
- Darf `config/*.yaml`, `.env` und Umgebungsvariablen ändern
- Entscheidet über Docker-Socket-Zugriff und MCP-Endpunkt
- Kann Log-Level anpassen, um Handlerentscheidungen nachzuvollziehen

### Entwickler ( Quellbaum )
- Voller Zugriff auf `src/`, darf Deskriptoren, Handler und Tests ändern
- Nutzt `pnpm dev` für lokale Anfrageversuche mit Beispieldaten
- Reicht Änderungen als Pull Request ein

### Mitwirkende / Reviewer
- Prüfen neue Dienst-Module auf Registry-Eintrag, Feldvorgaben, Testabdeckung und Sicherheit
- Achten darauf, dass neue Endpunkte nur über `mappings` erreichbar sind

## Siehe auch

- [structure.md](structure.md) - Ebenen und Aufrufpfad
- [api.md](api.md) - Clients, Methoden und Parameter
- [features.md](features.md) - Funktionen der Schicht
- [../homepage/menu.md](../homepage/menu.md) - Bereiche der Dashboard-Oberfläche
