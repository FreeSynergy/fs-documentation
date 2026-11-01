# MediaMTX - API Dokumentation

## Übersicht

MediaMTX bietet eine **REST Control API (v3)** auf Port `9997` (`api: yes` nötig, standardmäßig nur von `localhost` erreichbar), dazu **Hooks** (Server ruft Befehle/HTTP auf), **Prometheus-Metriken** (`9998`) und einen **Playback-Server** (`9996`).

## Authentifizierung

Die API nutzt dasselbe Berechtigungssystem wie die Medienprotokolle:

| Methode | Konfiguration |
|---------|---------------|
| `internal` | `authInternalUsers` mit `action: api`, IP-Listen (Default: `127.0.0.1` darf `api`) |
| `http` | `authHTTPAddress` — POST pro Anfrage, 20x = erlaubt |
| `jwt` | `authJWTJWKS`, Claim `mediamtx_permissions`; Token im `Authorization`-Header |

### Header

```
Authorization: Bearer <jwt>      # bei authMethod: jwt
Content-Type: application/json
```

### URL-Format

```
http://<host>:9997/v3/<bereich>/<aktion>[/<name>]
```

## Endpunkte (Auswahl)

### Pfade

| Methode | Endpunkt | Beschreibung |
|---------|----------|--------------|
| GET | `/v3/paths/list` | aktive Pfade mit Reads, Bytes, remoto |
| GET | `/v3/paths/get/{name}` | Details eines Pfads |

### Konfiguration zur Laufzeit

| Methode | Endpunkt | Beschreibung |
|---------|----------|--------------|
| GET | `/v3/config/paths/list` | konfigurierte Pfade |
| POST | `/v3/config/paths/add/{name}` | Pfad anlegen (JSON-Body) |
| POST | `/v3/config/paths/edit/{name}` | Pfad ändern |
| POST | `/v3/config/paths/remove/{name}` | Pfad löschen |
| POST | `/v3/config/paths/healthcheck/{name}` | Quelle prüfen |
| GET | `/v3/config/global/get` | globale Einstellungen |

### Verbindungen und Protokoll-Brücken

| Methode | Endpunkt | Beschreibung |
|---------|----------|--------------|
| GET | `/v3/connections/list` | aktive Verbindungen inkl. Typ/Remote |
| GET/POST | `/v3/rtsp_to_webrtc/list` … | RTSP↔WebRTC-Brücken |
| POST | `/v3/rtsp_to_webrtc/add/{name}` | Brücke anlegen |
| GET | `/v3/restransmission/list` … | Retransmission (UDP-Hole-Punching) |

## Beispiele

### Aktive Pfade listen

```bash
curl -s http://localhost:9997/v3/paths/list | jq .
```

```json
{
  "itemCount": 1,
  "items": [{
    "name": "test1",
    "ready": true,
    "readers": ["RTSP/TCP client", "HLS client"],
    "bytesReceived": 1048576,
    "bytesSent": 3145728
  }]
}
```

### Dynamischen Pfad anlegen

```bash
curl -X POST http://localhost:9997/v3/config/paths/add/kamera2 \
  -H 'Content-Type: application/json' \
  -d '{"source":"rtsp://10.0.0.12:554/stream1","sourceOnDemand":true}'
```

### Python

```python
import requests

api = "http://localhost:9997/v3"
for p in requests.get(f"{api}/paths/list").json()["items"]:
    print(p["name"], p["ready"], len(p["readers"]))

requests.post(f"{api}/config/paths/add/test2",
              json={"source": "publisher"})
```

## Hooks (Server → eigene Anwendung)

Hooks sind keine Webhooks im klassischen Sinn, sondern Konfigurationsfelder, die Befehle oder HTTP-Aufrufe auslösen:

| Hook | Zeitpunkt |
|------|-----------|
| `runOnConnect` / `runOnDisconnect` | Verbindungsaufbau/-abbau (Variablen `MTX_CONN_TYPE`, `MTX_CONN_ID`, `RTSP_PORT`) |
| `runOnPublish` / `runOnPublishDone` / `runOnUnpublish` | Publisher meldet sich an/ab |
| `runOnReady` / `runOnUnready` | Pfad wird bereit/nicht bereit |
| `runOnDemand` | Quelle wird bei erstem Leser gestartet |

HTTP-Auth-Hook: `authHTTPAddress` empfängt POST mit `action`, `path`, `user`, `ip` und entscheidet über den Statuscode.

## Rate Limits

- **keine dokumentierten Rate Limits** (Selbstbetrieb)
- Schutz über Reverse-Proxy (nginx/Caddy), `apiTrustedProxies` und Firewall auf `9997`

## Webhooks

- keine Webhooks; Ereignisablage läuft über Hooks oder Polling der Control-API

## SDKs und Client-Bibliotheken

- **OpenAPI/Swagger**: liegt im Repository (`apifile.yaml`) → Client generierbar
- **Go**: `github.com/bluenviron/mediamtx` als Bibliothek nutzbar
- **HTTP-Client jeder Sprache** (requests, fetch, axios) — API ist reines JSON
- **Play-SDKs**: hls.js, video.js, webrtc-Adapter, ffmpeg/VLC als Konsumenten

## Siehe auch

- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
