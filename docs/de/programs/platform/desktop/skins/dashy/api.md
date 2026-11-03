# Dashy - API Dokumentation

## Übersicht

Dashy bietet eine **optionale REST-API** zum Lesen und Schreiben der Konfiguration. Sie wird vom Node-Server bereitgestellt und ist damit in Container- und Bare-Metal-Installationen verfügbar, **nicht** aber bei rein statischem Hosting (Netlify, Vercel, CDN). Die API ist standardmäßig deaktiviert.

**Schnittstellen im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST (`/api/config/...`) | Konfigurationsdateien, Sektionen und Kacheln lesen/schreiben | Offiziell dokumentiert, opt-in |
| Konfigurationsdatei | `user-data/conf.yml` bzw. `conf.json` als Haupt-Schnittstelle | Offiziell |
| JSON-Schema | `ConfigSchema.json` zur Prüfung der Konfiguration | Offiziell |
| OpenSearch | `/opensearch.xml` für Browser-Suchmasken | Offiziell |
| Webhooks | ❌ Nicht vorhanden | — |

## Aktivierung

```yaml
# docker-compose.yml (Auszug)
services:
  dashy:
    image: lissy93/dashy
    environment:
      - ENABLE_API=true
```

Ohne `ENABLE_API=true` antworten alle `/api/*`-Anfragen mit `404`.

## Authentifizierung

- **Bestehende Server-Authentifizierung**: Liest die API mit einer regulären Dashy-Anmeldung. Lese-Endpunkte verlangen eine angemeldete Person, Schreib-Endpunkte die Rolle **admin**.
- **HTTP-Basic**: bei aktivierter Basic-Auth (`ENABLE_HTTP_AUTH` oder `BASIC_AUTH_USERNAME` / `BASIC_AUTH_PASSWORD`) mit `curl -u` nutzbar.
- **OIDC / Keycloak / Zitadel**: Identitäts-Token als Bearer-Token senden.
- **API-Token**: `API_TOKEN` setzen und als `Authorization: Bearer <token>` senden. Ein gültiger Token bedeutet vollen (Admin-)Zugriff und funktioniert neben jeder anderen Methode. Ist kein anderer Schutz konfiguriert, sichert der Token die API gegen anonyme Zugriffe ab.
- Ohne jede Authentifizierung ist die API offen — wie der Rest der Installation.

```bash
curl -u alice:beispiel-passwort https://dashy.local/api/config
curl -H 'Authorization: Bearer <id-token>' https://dashy.local/api/config
curl -H 'Authorization: Bearer <API_TOKEN>' https://dashy.local/api/config
```
## Endpunkte

`:filename` ist eine YAML-Datei im Benutzerordner (`conf.yml` oder eine Unterseite wie `home-lab.yml`). `:key` ist einer der Top-Level-Schlüssel `pageInfo`, `appConfig`, `sections` oder `pages`. `:sid` und `:iid` sind entweder nullbasierte Indizes (`0`, `1`, …) oder exakte Namen (URL-kodiert).

### Konfigurationsdateien

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/config` | Konfigurationsdateien auflisten |
| `GET` | `/api/config/:filename` | Komplette Datei als JSON |
| `PUT` | `/api/config/:filename` | Datei vollständig ersetzen |
| `GET` | `/api/config/:filename/:key` | Top-Level-Schlüssel lesen |
| `PUT` | `/api/config/:filename/:key` | Top-Level-Schlüssel ersetzen |

### Sektionen

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `POST` | `/api/config/:filename/sections` | Sektion anlegen (`name` erforderlich) |
| `GET` | `/api/config/:filename/sections/:sid` | Sektion lesen |
| `PATCH` | `/api/config/:filename/sections/:sid` | Felder einer Sektion ändern |
| `DELETE` | `/api/config/:filename/sections/:sid` | Sektion löschen |

### Kacheln (Items)

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/config/:filename/sections/:sid/items` | Kacheln einer Sektion auflisten |
| `POST` | `/api/config/:filename/sections/:sid/items` | Kachel anlegen (`title` erforderlich) |
| `GET` | `/api/config/:filename/sections/:sid/items/:iid` | Einzelne Kachel lesen |
| `PATCH` | `/api/config/:filename/sections/:sid/items/:iid` | Felder einer Kachel ändern |
| `DELETE` | `/api/config/:filename/sections/:sid/items/:iid` | Kachel löschen |

**Semantik**: `PATCH` führt eine flache Zusammenführung aus — gesandte Felder werden geändert, verschachtelte Werte (etwa das `items`-Array einer Sektion) komplett ersetzt. `PUT` ersetzt das Ziel vollständig. Alle Bodies sind JSON; Fehler antworten mit passendem Statuscode.

```json
{ "success": false, "message": "Sektion nicht gefunden" }
```

## Beispiele

### Dateien auflisten

```bash
curl -H 'Authorization: Bearer <API_TOKEN>' https://dashy.local/api/config
```

```json
{
  "success": true,
  "files": ["conf.yml", "home-lab.yml"]
}
```

### Kachel anlegen

```bash
curl -X POST -H 'Authorization: Bearer <API_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"title":"Grafana","url":"https://grafana.local","icon":"hl-grafana"}' \
  https://dashy.local/api/config/conf.yml/sections/0/items
```

Antwort (sinngemäß):

```json
{
  "success": true,
  "item": {
    "title": "Grafana",
    "url": "https://grafana.local",
    "icon": "hl-grafana"
  }
}
```

### Sektion umbenennen

```bash
curl -X PATCH -H 'Authorization: Bearer <API_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name":"Monitoring"}' \
  https://dashy.local/api/config/conf.yml/sections/Medien
```

### Theme setzen

```bash
curl -X PUT -H 'Authorization: Bearer <API_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"theme":"nord-frost"}' \
  https://dashy.local/api/config/conf.yml/appConfig
```

Nach jeder Änderung die Seite neu laden, bis die neue Konfiguration erscheint.

## Konfigurationsdatei als Schnittstelle

Neben der API ist die Datei selbst der reguläre Weg:

Der Benutzerordner `user-data/` enthält `conf.yml` (Hauptdatei), die Dateien der Unterseiten, eigene Widget-Komponenten und den Ordner `config-backups/` mit den Sicherungen.

Wichtige Top-Level-Bereiche:

| Schlüssel | Inhalt |
|-----------|--------|
| `pageInfo` | Titel, Beschreibung, Logo, Fußzeile |
| `appConfig` | Theme, Suche, Ansichtsstandard, Statusprüfungen, Sprache, Authentifizierung |
| `sections` | Sektionen mit `name`, `displayData`, `items`, `widgets` |
| `pages` | Verweise auf Unterseiten |

Die Hauptdatei wird beim Speichern gegen das mitgelieferte JSON-Schema geprüft; ungültige Inhalte werden abgelehnt.

## Grenzen und Verhalten beim Schreiben

- Kommentare, Anker und eigene Formatierung gehen beim Schreiben verloren (in der Datei und über die API)
- Vor jedem Schreiben landet eine Sicherung in `user-data/config-backups/` (abschaltbar mit `DISABLE_CONFIG_BACKUPS=true`)
- Konfigurationsdateien sind auf **256 KB** begrenzt
- Gleichzeitige Schreibvorgaben laufen nach „letzter gewinnt“, ohne Sperre oder Versionsprüfung
- Unterseitendateien werden **nicht** gegen das Schema geprüft, weil sie nur Teile enthalten dürfen

## Rate Limits

- Dashy bringt **keine dokumentierte Ratenbegrenzung** für die API mit.
- Sinnvoller Schutz entsteht im Reverse Proxy (nginx `limit_req`, Traefik-Middleware) und durch die Authentifizierung.

## Webhooks und internes Eventing

- **Keine Webhooks**, kein Ereignisausgang, keine Benachrichtigungen aus der API.
- **Intern**: Der Node-Server beantwortet Statusprüfungen für Kacheln in Intervallen; die Oberfläche aktualisiert Punkte und Widgets durch erneutes Abfragen.

## SDKs und Client-Bibliotheken

- **Kein offizielles SDK.** Die API ist klassisches JSON-over-HTTP und wird mit `curl`, `fetch`, `axios`, `requests` oder Python-`httpx` genutzt.
- **JSON-Schema** (`ConfigSchema.json`) kann in Pipelines zur Validierung herangezogen werden, bevor eine Datei ausgerollt wird.

## Sicherheitshinweise

- `API_TOKEN` lang und zufällig wählen (zum Beispiel `openssl rand -hex 32`) und nur über HTTPS senden
- Schreibende Zugriffe auf Admin-Konten oder den Token beschränken

## Siehe auch

- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
