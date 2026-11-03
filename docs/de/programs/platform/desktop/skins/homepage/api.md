# Homepage - API Dokumentation

## Übersicht

Homepage hat **keine öffentliche Verwaltungs-API**: Das Dashboard wird ausschließlich über YAML-Dateien unter `config/` gesteuert. Was es gibt, sind **interne Next.js-API-Routen** unter `/api/...`. Sie erfüllen zwei Zwecke: Sie holen als **Proxy** die Daten der angebundenen Dienste in den Browser (Schlüssel bleiben auf dem Server, CORS entfällt), und sie liefern Hilfsdaten wie Config-Hashes, Statusmeldungen oder Suchvorschläge.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| HTTP/JSON unter `/api/...` | Dienst-Proxy, Info-Widgets, Docker/Kubernetes-Status, Hilfsfunktionen | Intern, nicht als stabile Schnittstelle versioniert |
| Config-Schnittstelle | `config/*.yaml` + Umgebungsvariablen | Offiziell dokumentiert (maßgeblicher Weg) |
| MCP (`/api/mcp`) | KI-Assistenten lesen/ändern Konfigurationsdateien | Opt-in über `HOMEPAGE_MCP_ENABLED` |
| Webhooks | ❌ Nicht vorhanden | — |
| GraphQL | ❌ Nicht vorhanden | — |
| Write-API für Layout/Widgets | ❌ Nicht vorhanden (Ausnahme: MCP mit Schreibrecht) | — |

## Authentifizierung

- **Standard: keine.** Die Routen sind ohne Anmeldedaten erreichbar, sobald jemand die Seite erreicht. Schutz übernimmt der Reverse Proxy (Basic Auth, OAuth-Proxy, Authentik, VPN/Tailscale).
- **Host-Validierung**: Jede Route prüft den `Host`-Header gegen `HOMEPAGE_ALLOWED_HOSTS` (plus `localhost:<PORT>`). Passt der Host nicht, antwortet Homepage mit `400` und Hinweis im Log.
- **Optionale Sitzungsanmeldung**: Mit `HOMEPAGE_AUTH_ENABLED` prüft jede Route ein NextAuth-Sitzungs-Token (`NEXTAUTH_SECRET` bzw. `HOMEPAGE_AUTH_SECRET`). Ohne gültige Sitzung antwortet die Route mit `401 {"error":"Unauthorized"}`. Das schützt die Routen, ersetzt aber keine Rollen.
- **Dienst-Secrets**: API-Keys und Passwörter stehen in der Config und werden über `{{HOMEPAGE_VAR_*}}` / `{{HOMEPAGE_FILE_*}}` eingesetzt. Sie verlassen den Server nur in Richtung des jeweiligen Zieldienstes.
- **MCP-Token**: Für den MCP-Endpunkt wird `HOMEPAGE_MCP_TOKEN` (mindestens 32 Zeichen) verlangt, sofern keine Sitzungsanmeldung aktiv ist. Übergabe per `Authorization: Bearer <token>` oder `X-Homepage-MCP-Token: <token>`.

## Endpunkte

Die Routen sind innerhalb des Projekts definiert und können sich zwischen Versionen ändern. Parameter werden als Query-Parameter übergeben.

### Dienst-Proxy (Service-Widgets)

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/services/proxy` | Daten eines konfigurierten Dienstes abrufen (`group`, `service`, `index`) |
| `GET` | `/api/services/proxy?endpoint=<name>` | Einzelnen, im Widget hinterlegten Endpunkt des Dienstes abrufen |
| `GET` | `/api/services/proxy?...&query=<json>` | Zusätzliche, erlaubte Query-Parameter an den Zieldienst weitergeben |
| `GET` | `/api/services/proxy?...&segments=<json>` | Erlaubte Pfadsegmente einsetzen (z. B. IDs) |
| `POST` | `/api/services/proxy?...&endpoint=<name>` | Nur für Dienste mit hinterlegter POST-Zuordnung; unbekannte Typen/Endpunkte antworten mit `403`, ungültige Parameter mit `400` |
| `GET` | `/api/services/index` | Metadaten der konfigurierten Dienste (Gruppen, Namen, Typen) |

### Informations-Widgets

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/widgets/resources` | CPU-, RAM- und Plattennutzung des Hosts |
| `GET` | `/api/widgets/weather` | Wetter (interner Anbieter) |
| `GET` | `/api/widgets/openweathermap` | Wetterdaten von OpenWeatherMap |
| `GET` | `/api/widgets/openmeteo` | Wetterdaten von Open-Meteo |
| `GET` | `/api/widgets/stocks` | Kurse aus dem `stocks`-Widget |
| `GET` | `/api/widgets/glances` | Messwerte einer Glances-Instanz |
| `GET` | `/api/widgets/kubernetes` | Cluster-Übersicht für das Info-Widget |
| `GET` | `/api/widgets/longhorn` | Longhorn-Speicherwerte |
| `GET` | `/api/widgets/customapi` | Beliebige JSON-Quelle nach JSON-Pfad filtern |

### Infrastruktur-Status

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/docker/statuses` | Container-Status aus dem Docker-Socket |
| `GET` | `/api/docker/stats` | CPU/RAM je Container |
| `GET` | `/api/kubernetes/status` | Pod-/Deployment-Status |
| `GET` | `/api/kubernetes/stats` | Auslastungswerte aus dem Cluster |
| `GET` | `/api/proxmox/stats` | Statuswerte eines Proxmox-Hosts |
| `GET` | `/api/siteMonitor?groupName=&serviceName=` | HTTP-Erreichbarkeit und Laufzeit einer konfigurierten Kachel |
| `GET` | `/api/ping?groupName=&serviceName=` | ICMP-Ping auf eine konfigurierte Kachel |

### Seite, Konfiguration und Wartung

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/theme` | aktives Farbschema (`color`, `theme`) |
| `GET` | `/api/bookmarks` | Lesezeichen aus `bookmarks.yaml` |
| `GET` | `/api/search/searchSuggestion` | Suchvorschläge des konfigurierten Providers |
| `GET` | `/api/releases` | Letzte GitHub-Releases des Projekts (Update-Hinweis) |
| `GET` | `/api/hash` | Hashes der Config-Dateien (Änderungserkennung) |
| `GET` | `/api/validate` | YAML-Validierung mit Datei, Grund und Zeile |
| `GET` | `/api/revalidate` | Caches für Dashboard-Daten verwerfen |
| `GET` | `/api/healthcheck` | Gibt `up` zurück (Container-Healthcheck) |
| `GET` | `/api/config/<pfad>` | Zugriff auf Config-Inhalte für interne Funktionen |
| `POST` | `/api/mcp` | Model Context Protocol: Config lesen/ändern (opt-in) |
| `GET/POST` | `/api/auth/*` | Sitzungsanmeldung, nur mit `HOMEPAGE_AUTH_ENABLED` |

## Widget-Datenquellen

Service-Widgets sprechen die API des jeweiligen Dienstes an, nicht die von Homepage. Beispiele aus den Widget-Deskriptoren:

| Dienst | Zielmuster | Anmerkung |
|--------|-----------|-----------|
| Sonarr/Radarr/Lidarr | `{url}/api/v3/{endpoint}?apikey={key}` | `endpoint` z. B. `queue`, `series`, `command` |
| qBittorrent | `{url}/api/v2/{endpoint}` | Session-Login wird intern durchgeführt |
| UniFi | `{url}/proxy/network/...` | eigener JSON-RPC-Handler |
| Synology (Disk Station) | `{url}/webapi/entry.cgi` | eigener Handler, siehe [../synology-dsm/api.md](../synology-dsm/api.md) |
| Proxmox | `{url}/api2/json/{endpoint}` | Token-Auth |

## Beispiele

### Service-Widget-Daten abrufen

```bash
curl -s \
  -H "Host: homepage.example.internal" \
  "http://localhost:3000/api/services/proxy?group=Medien&service=Sonarr&index=0&endpoint=queue"
```

Antwort (gekürzt):

```json
{
  "totalRecords": 4,
  "page": 1,
  "pageSize": 10,
  "records": [
    { "title": "Folge 12", "sizeLeft": 524288000, "status": "downloading" }
  ]
}
```

### Status-Ampel einer Kachel

```bash
curl -s "http://localhost:3000/api/siteMonitor?groupName=Netzwerk&service=Pi-hole"
```

Antwort:

```json
{ "status": 200, "ok": true, "duration": 42 }
```

### Konfiguration validieren

```bash
curl -s "http://localhost:3000/api/validate"
```

Antwort bei Fehlern:

```json
{
  "status": "error",
  "errors": [
    { "name": "YAMLException", "config": "services.yaml", "reason": "bad indentation of a mapping entry", "mark": { "line": 17 } }
  ]
}
```

### MCP-Endpunkt nutzen

```bash
curl -s -X POST "http://localhost:3000/api/mcp" \
  -H "Authorization: Bearer $HOMEPAGE_MCP_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

## Rate Limits

- Homepage bringt **keine eigene Ratenbegrenzung** für `/api/...` mit.
- Antworten werden kurzzeitig prozessintern gecacht (`memory-cache`); identische Abfragen innerhalb des Cache-Fensters treffen den Zieldienst nicht erneut.
- Die tatsächliche Last bestimmen die Abfrageintervalle der Widgets (Standard: im Minutenbereich) und die Anzahl der Kacheln.
- Empfehlung: Ratenbegrenzung am Reverse Proxy (`limit_req` bei nginx, Middleware `ratelimit` bei Traefik) und Intervalle von 30 Sekunden oder mehr.

## Webhooks

- **Keine Webhooks**: Homepage versendet keine Ereignisse nach außen.
- **Anderer Weg**: Der MCP-Endpunkt nimmt Änderungen von außen entgegen; externe Skripte können `GET /api/revalidate` aufrufen, damit gecachte Dashboard-Daten verworfen werden.
- **Monitoring**: `/api/healthcheck` liefert `up` und eignet sich für Container-Healthchecks; `siteMonitor`/`ping` ersetzen keinen Monitoring-Stack.

## SDKs und Client-Bibliotheken

- **Kein offizielles SDK** für die internen Routen.
- Die **Service-Clients selbst** liegen im Quellbaum unter `src/utils/proxy/` und `src/widgets/<dienst>/proxy.js`; Beschreibung dieser Schicht: [../gethomepage/api.md](../gethomepage/api.md).
- Für eigene Skripte genügen `curl`, `fetch` oder `requests` mit den Query-Parametern oben.
- Für die **Zieldienste** gelten deren eigene SDKs (Sonarr/Radarr-Clients, Docker-API, Kubernetes-Client, Proxmox-API).

## Hinweise für den Betrieb

- `HOMEPAGE_ALLOWED_HOSTS` korrekt setzen – die Prüfung schützt vor Host-Header-Missbrauch und blockiert sonst auch legitime Aufrufe.
- Die Routen sind ein **SSRF-Werkzeug**: Sie dürfen nicht öffentlich erreichbar sein. Proxy-Schutz, VPN oder Firewall sind Pflicht.
- Secrets nie in die Config schreiben, sondern über `HOMEPAGE_VAR_*`/`HOMEPAGE_FILE_*` einsetzen.
- Änderungen an Routen sind interne Details: Für Automatisierung besser die YAML-Dateien (Git) verwenden.

## Siehe auch

- [description.md](description.md)
- [features.md](features.md)
- [menu.md](menu.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [../gethomepage/index.md](../gethomepage/index.md)
