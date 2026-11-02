# Wowza Streaming Engine - API Dokumentation

## Übersicht

Der Zugangsweg ist die **REST Server API v2** (Standard-Port `8087`): sie bildet Manager-Funktionen (Verbindungen, Anwendungen, Restream-Ziele, Neustarts) als JSON/HTTP ab. Referenz: Entwicklerdoku des Herstellers (`wowza.com/developer`). Für eigenes Verhalten in Streams gibt es zusätzlich die **Java-Modul-API**.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST Server API v2 | Verbindungen, Apps, Eigenschaften, Restream, Neustart | offiziell |
| Java-Modul-API | eigene Auth, Event-Hooks im Stream-Lebenszyklus | offiziell |
| Manager-Session | nur Web-Oberfläche | ❌ nicht für Automatisierung |
| Wowza Streaming Cloud (WSC) | früherer Cloud-Dienst | ⚠ eingestellt, nicht mehr verwenden |

## Authentifizierung

Basic Auth mit dem Manager-Konto (Konten in `managernames.properties`).

### Header

```
Authorization: Basic base64(user:pass)
Content-Type: application/json
```

## Endpunkte (Auswahl)

| Methode | Endpunkt | Beschreibung |
|---------|----------|--------------|
| GET | `/v2/connections` | aktive Ein-/Ausgänge |
| GET | `/v2/instances` | Instanzen (`_definst_`) |
| GET | `/v2/instances/{id}/applications` | Anwendungen auflisten |
| POST | `/v2/instances/{id}/applications/{app}/start` | Anwendung starten |
| POST | `/v2/instances/{id}/applications/{app}/stop` | Anwendung stoppen |
| POST | `/v2/instances/{id}/applications/{app}/restart` | Anwendung neu starten |
| GET | `/v2/instances/{id}/applications/{app}/restream` | Restream-Ziele lesen |
| PUT | `/v2/instances/{id}/applications/{app}/restream` | Restream-Ziele setzen |
| GET | `/v2/instances/{id}/applications/{app}/properties/{propName}` | Eigenschaft lesen |
| PUT | `/v2/instances/{id}/applications/{app}/properties/{propName}` | Eigenschaft setzen |
| GET | `/v2/instances/{id}/applications/{app}/streamgroups` | laufende Live-Gruppen |

## Beispiele

### Anwendung neu starten

```bash
curl -s -u admin:secret -X POST \
  http://localhost:8087/v2/instances/_definst_/applications/live/restart
```

### Python

```python
import requests

BASE = "http://wowza.example.com:8087/v2"
AUTH = ("admin", "secret")

for app in requests.get(f"{BASE}/instances/_definst_/applications",
                        auth=AUTH).json()["Applications"]["Application"]:
    print(app["name"], app["status"])
```

## Ereignisse (Input/Output)

❌ keine eingebauten Webhooks (❌). Ersatz: Java-Module mit Lebenszyklus-Callbacks (`onPublish`, `onPlay`, `onPublishDone` …), die dort HTTP-Aufrufe an eigene Dienste absetzen.

## Rate Limits

Keine dokumentierten Kontingente (Selbstbetrieb). Schutz über Reverse-Proxy und Firewalls; die API gehört netzseitig hinter Verwaltungszugriff.

## SDKs und Client-Bibliotheken

- **offiziell**: Java-Modul-API (im Installationsbaum), REST-Dokumentation mit Beispielen
- **Community**: REST-Wrapper für Python/Node, Admin-Skripte (Docker-Images inklusive)
- **Player-seitig**: hls.js, video.js, Shaka u. a. über die Wiedergabe-URLs

## Skin-Hinweis

Virtual Host → Anwendung → Stream entsprechen dem Standardmodell ([modelle.md](../../../../data/modelle.md)); URL-, Schlüssel- und Feldeigenschaften folgen [felder.md](../../../../data/felder.md).
