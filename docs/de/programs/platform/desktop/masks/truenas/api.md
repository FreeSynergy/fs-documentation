# TrueNAS - API Dokumentation

## Übersicht

Die Middleware (`middlewared`) stellt die komplette Funktionsmenge als **API v2.0** bereit: ein versioniertes **JSON-RPC-2.0**-Interface über HTTP (`/api/v2.0`) und WebSocket. Jede UI-Aktion ist ein Methodenaufruf (`pool.query`, `app.start`, `sharing.smb.create` …). Authentifiziert wird mit **API-Key als Bearer-Token** (HTTP) bzw. Login-Methoden (WebSocket). Dazu gehören Job-Tracking (`core.get_jobs`) und Event-Abos (`core.subscribe`). Altes TrueNAS CORE nutzte die Legacy-API v1 (`/api/v1.0`) — nur noch für Bestandsinstallationen relevant.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| JSON-RPC 2.0 (HTTP `POST /api/v2.0`) | alle Verwaltungsmethoden | Offiziell (neuere Versionen, versionabhängig) |
| JSON-RPC 2.0 (WebSocket) | dieselben Methoden + Event-Abos | Offiziell; Endpunktpfad unter `/api/docs/` am Gerät |
| Legacy REST v1 (`/api/v1.0`) | CORE-Installationen | Veraltet |
| CLI `midclaw` / `midclt` | Methodenaufruf auf dem Gerät | Offiziell |
| Webhooks | — | ❌ Nicht vorhanden |

## Authentifizierung

- **API-Keys**: pro Benutzer anlegbar über das **Benutzermenü (oben rechts) → API Keys** (oder Methode `api_key.create`). Keys haben Name, Rolle und optionale Ablaufe.
- **HTTP**: Header `Authorization: Bearer <api-key>` bei JSON-RPC-Aufrufen gegen `https://<host>/api/v2.0`.
- **WebSocket**: nach Verbindungsaufbau `auth.login` (Benutzer/Passwort, OTP-fähig), `auth.login_with_api_key` oder `auth.login_with_token`; danach `auth.me` zur Kontrolle.
- **2FA**: Bei aktivem Two-Factor für UI-Sitzungen laufen Skripte am saubersten über API-Keys (OTP-frei, widerrufbar).
- **Rollen**: Zugriff folgt den Privileges des API-Key-Inhabers (versionabhängig granular).

## JSON-RPC-Format

Anfrage:

```json
{ "jsonrpc": "2.0", "method": "core.ping", "params": [], "id": 1 }
```

Antwort:

```json
{ "jsonrpc": "2.0", "result": "pong", "id": 1 }
```

Fehler:

```json
{ "jsonrpc": "2.0",
  "error": { "code": 1, "message": "[ENOSYS] Method not found", "data": {} },
  "id": 1 }
```

## Methoden (Auswahl)

| Methode | Beschreibung |
|---------|--------------|
| `core.ping` | Verbindungstest |
| `core.get_methods` | alle Methoden auflisten |
| `core.get_jobs` / `core.job_wait` | Job-Status prüfen/abwarten |
| `core.subscribe` / `core.unsubscribe` | Event-Kanäle abonnieren (WebSocket) |
| `system.version`, `system.info` | Versions- und Systeminfo |
| `api_key.create/query/delete` | API-Keys verwalten |
| `pool.query`, `pool.dataset.query` | Pools und Datasets lesen |
| `pool.dataset.create/update/delete` | Datasets ändern (Job) |
| `pool.snapshot.create/query` | Snapshots |
| `pool.snapshottask.run` | geplanten Snapshot-Job ausführen |
| `app.query`, `app.start`, `app.stop`, `app.upgrade` | Apps (SCALE) |
| `sharing.smb.query/create` | SMB-Freigaben |
| `replication.create/run` | Replikationsaufgaben |
| `service.control` | Dienste starten/stoppen |
| `alert.list` | aktive Alarme |
| `auth.me` | eigene Sitzungsinfo |

## Beispiele

### curl: JSON-RPC über HTTP

```bash
curl -sk -X POST https://truenas.local/api/v2.0 \
  -H 'Authorization: Bearer DEIN_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","method":"system.version","params":[],"id":1}'
```

Antwort (gekürzt):

```json
{ "jsonrpc": "2.0",
  "result": "TrueNAS-SCALE-24.10.2",
  "id": 1 }
```

### curl: Datasets mit Filter

```bash
curl -sk -X POST https://truenas.local/api/v2.0 \
  -H 'Authorization: Bearer DEIN_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","method":"pool.dataset.query","params":[[["name","=", "tank/media"]],{"select":["name","used","available"]}],"id":2}'
```

### Jobs: Pool-Erweiterung abwarten

```bash
# Aufruf liefert eine Job-ID im result-Feld
curl -sk -X POST https://truenas.local/api/v2.0 \
  -H 'Authorization: Bearer DEIN_API_KEY' -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","method":"pool.expand","params":[1],"id":3}'

curl -sk -X POST https://truenas.local/api/v2.0 \
  -H 'Authorization: Bearer DEIN_API_KEY' -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","method":"core.get_jobs","params":[[["id","=","abc123"]]],"id":4}'
```

### CLI auf dem Gerät

```bash
# SCALE (aktuell)
midclaw call core.ping
midclaw call pool.dataset.query '[]'

# CORE / ältere Versionen
midclt call system.version
```

## Events statt Webhooks

- TrueNAS **versendet keine Webhooks** an externe Systeme und kennt **keine eingehenden Webhooks**.
- Echtzeitinformationen kommen über **JSON-RPC-Notificationen**: WebSocket-Verbindung mit `core.subscribe` auf Kanäle (z. B. Jobs, Pool-/App-Ereignisse) — der Weg für Live-Dashboards.
- Ausgehende **Alert Services** (E-Mail, Team-Kanäle; Umfang versionabhängig) benachrichtigen bei Alarmen, sind aber kein generisches Callback.

## Rate Limits und Betriebshinweise

- **Keine dokumentierte Ratenbegrenzung** der Middleware-API — trotzdem Polling-Intervalle vernünftig wählen (Events bevorzugen) und Keys rotieren.
- API-Doku der eigenen Version: `https://<host>/api/docs/` oder api.truenas.com (versionsbezogene Methodennamen prüfen).
- Self-Signed-Zertifikate: `curl -k` nur im Labor; besser internes CA-Zertifikat hinterlegen.
- API-Key nur einmal sichtbar; bei Verlust neu erzeugen und alten widerrufen.

## SDKs und Client-Bibliotheken

| Bibliothek | Sprache | Anmerkung |
|------------|---------|-----------|
| `truenas-api` (TrueNAS API Client, github.com/truenas/api_client) | Python | offizielles WebSocket-JSON-RPC-Paket inkl. CLI-Bezug |
| `py-nas` | Python | Community-WebSocket-Client (Basis älterer Integrationen) |
| Ansible-Module `community.general.truenas_*` | YAML | Declarative Aufgaben über die API |
| `midclaw`/`midclt` | CLI | direkt auf dem Gerät, JSON-Argumente |

## Testen und Referenz

1. **Eigene API-Doku öffnen**: `https://<host>/api/docs/` (versionsbezogene Methodenlisten) bzw. api.truenas.com.
2. **Key anlegen**: Benutzermenü → API Keys, Rolle bewusst wählen (Read-only für Dashboards).
3. **Verbindung prüfen**: `core.ping` → `pong`; danach echte Lese-Methoden testen.
4. **Events ausprobieren**: WebSocket-Client mit `auth.login_with_api_key` + `core.subscribe`, um Job-/Pool-Ereignisse live zu sehen.

## Siehe auch

- [index.md](index.md)
- [description.md](description.md)
- [features.md](features.md)
- [menu.md](menu.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
