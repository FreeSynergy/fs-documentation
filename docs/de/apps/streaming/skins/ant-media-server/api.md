# Ant Media Server - API Dokumentation

## Übersicht

AMS stellt eine **REST-API v2** bereit, die dieselben Fähigkeiten wie das Web-Panel abdeckt. Vollständige Methodenreferenz: `antmedia.io/rest` (Swagger/OpenAPI).

## Basis-URLs

| Dienst | Basispfad |
|--------|-----------|
| Broadcasts | `https://<host>:5443/{application}/rest/v2/broadcasts/…` |
| VoDs | `https://<host>:5443/{application}/rest/v2/vods/…` |
| Management (Panel-APIs) | `https://<host>:5443/rest/v2/…` |
| Cluster | `https://<host>:5443/rest/v2/cluster/…` |
| HTTP (Test) | `http://<host>:5080/{application}/rest/v2/…` |

`{application}` ist meist `live`, `WebRTCAppEE` oder eine eigene App.

## Authentifizierung

| Methode | Wirkung |
|---------|---------|
| **IP-Filter** | nur freigegebene Absender-IPs dürfen REST aufrufen (App-Einstellung) |
| **JWT** | `Authorization: Bearer <token>`, Token vom eigenen IdP oder AMS issued |
| Panel-Session | nur fürs Web-Panel, nicht für REST |

### Header

```
Authorization: Bearer <jwt>
Content-Type: application/json
```

## Endpunkte (Auswahl)

### Broadcasts

| Methode | Endpunkt | Beschreibung |
|---------|----------|--------------|
| POST | `/rest/v2/broadcasts/create` | Stream anlegen (JSON: streamId, name, type, …) |
| GET | `/rest/v2/broadcasts/list/{offset}/{size}` | Streams aufgelistet |
| GET | `/rest/v2/broadcasts/{streamId}` | Stream-Details |
| POST | `/rest/v2/broadcasts/{streamId}/stop` | Stream stoppen |
| POST | `/rest/v2/broadcasts/{streamId}/delete` | Stream löschen |
| POST | `/rest/v2/broadcasts/{streamId}/record/start` | Aufnahme starten |
| POST | `/rest/v2/broadcasts/{streamId}/record/stop` | Aufnahme stoppen |
| POST | `/rest/v2/broadcasts/{streamId}/restream` | Weiterleitung zu Zielen (Enterprise) |
| GET | `/rest/v2/broadcasts/{streamId}/track-list` | Tracks/Codecs eines Streams |
| GET | `/rest/v2/broadcasts/{streamId}/viewer-count` | aktive Zuschauer |

### VoD

| Methode | Endpunkt | Beschreibung |
|---------|----------|--------------|
| GET | `/rest/v2/vods/list/{offset}/{size}` | Aufnahmen/Uploads auflisten |
| POST | `/rest/v2/vods/upload` | Datei-Upload (multipart) |
| POST | `/rest/v2/vods/{vodId}/delete` | VoD löschen |

> Die exakte Schreibweise mancher Teilpfade variiert mit der Serverversion — Swagger unter `antmedia.io/rest` ist maßgeblich.

## Beispiele

### Stream anlegen

```bash
curl -s -X POST http://localhost:5080/live/rest/v2/broadcasts/create \
  -H 'Content-Type: application/json' \
  -d '{"streamId":"konzert-1","name":"Konzert","type":"livestream",
       "metaData":"{\"mainTrack\":\"konzert-1\"}"}'
```

### Aufnahme starten

```bash
curl -s -X POST http://localhost:5080/live/rest/v2/broadcasts/konzert-1/record/start
```

### Python

```python
import requests

BASE = "https://ams.example.com/live/rest/v2"
HEAD = {"Authorization": "Bearer <jwt>", "Content-Type": "application/json"}

r = requests.post(f"{BASE}/broadcasts/create", headers=HEAD,
                  json={"streamId": "meeting-42", "type": "livestream"})
print(r.json()["streamId"])

for b in requests.get(f"{BASE}/broadcasts/list/0/20", headers=HEAD).json():
    print(b["streamId"], b.get("status"))
```

## Rate Limits

- **keine dokumentierten Rate Limits** (Selbstbetrieb)
- IP-Filter und Reverse-Proxy-Limits (`limit_req`) sind der übliche Schutz

## Webhooks

- AMS kann **Webhooks pro Anwendung** senden: Ereignisse wie Publish-Start/-Ende, Aufnahme-Fertig, Viewer-Änderungen
- Ziel-URL und Ereignisse werden in den App-Einstellungen gesetzt; Payload ist JSON
- Alternative: Intervall-Abfrage über `viewer-count` und Broadcast-Details

## SDKs und Client-Bibliotheken

- **JavaScript**: `@antmedia/webrtc_adaptor` (WebSocket/WebRTC, WHIP/WHEP-artig), Panel-Playern
- **Android**: Ant Media Android SDK (Kotlin/Java)
- **iOS**: Ant Media iOS SDK (Swift/Obj-C)
- **Flutter**: Ant Media Flutter-Plugin (Enterprise)
- **REST**: jeder HTTP-Client (requests, fetch, axios, curl)

## Siehe auch

- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
