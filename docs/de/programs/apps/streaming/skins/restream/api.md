# Restream - API Dokumentation

## Übersicht

Restream ist SaaS. Das öffentlich dokumentierte API-Surface (Stand der Recherche) umfasst **REST-Schnittstellen** für Konten, Kanäle, Events, Plattformen und Stream-Keys sowie **WebSocket-Schnittstellen** für Chat und Streaming-Status. Maßgeblich ist das Entwicklerportal des Anbieters; die folgende Übersicht ist bewusst konservativ gehalten.

## Authentifizierung

| Methode | Verwendung |
|---------|------------|
| OAuth-Zugangs-Token | REST- und WebSocket-Aufrufe im Namen des Kontos |
| Konto-Login (E-Mail/Passwort, 2FA) | nur Dashboard, nicht API |

### Header

```
Authorization: Bearer <access_token>
Content-Type: application/json
```

### URL-Format (REST)

```
https://api.restream.io/v1/<bereich>
```

## Endpunkte (übersichtlich)

| Bereich | Beschreibung |
|---------|--------------|
| **User** | Profil- und Kontoinformationen |
| **Platforms** | öffentlich verfügbare Zielplattformen |
| **Channels** | verbundene Ziele anlegen, auflisten, ändern, trennen |
| **Stream Keys** | Ingest-Keys und -URLs verwalten |
| **Events** | geplante Streams planen, ändern, starten, beenden |
| **Monitoring** | Statuswerte und Metriken zu Streams und Events |

> Die exakten Pfade, Feldnamen und Plan-Voraussetzungen stehen im Entwicklerportal des Anbieters (API-Katalog/Postman-Sammlung). Vor einer Skin-Implementierung dort abgleichen.

## WebSockets

| Schnittstelle | Zweck |
|---------------|-------|
| Chat | Nachrichten aller verbundenen Plattformen in Echtzeit senden/empfangen (`wss`) |
| Streaming Updates | Live-Status: ausgehender Stream, Plattform-Status, Viewerzahlen (`wss`) |

## Beispiele

### Verbundene Kanäle auflisten

```bash
curl -s https://api.restream.io/v1/channels \
  -H 'Authorization: Bearer <access_token>'
```

```json
[
  { "id": 1234, "type": "youtube", "title": "Hauptkanal", "isStreamOn": false },
  { "id": 1235, "type": "twitch",  "title": "Second Channel", "isStreamOn": true }
]
```

### Python: Statusstrom abonnieren (konzeptionell)

```python
import json, websocket

WS = "wss://streaming.api.restream.io/ws"

def on_message(ws, message):
    print(json.loads(message))   # Status, Plattform-Updates, Viewerzahlen

ws = websocket.WebSocketApp(WS,
        header={"Authorization": "Bearer <access_token>"},
        on_message=on_message)
ws.run_forever()
```

## Rate Limits

- **keine stabil dokumentierten Rate Limits**; mit moderaten Poll-Intervallen arbeiten und Statusereignisse über die WebSockets beziehen
- API-Zugang ist je nach Abo-Plan unterschiedlich umfangreich

## Webhooks

- keine klassisch dokumentierten Webhooks; Echtzeitereignisse kommen über die **WebSocket**-Schnittstellen

## SDKs und Client-Bibliotheken

- **keine offiziellen SDKs** — REST und WebSockets mit üblichen HTTP-/WS-Clients nutzen
- eingebetteter Player und Chat-Widgets als Dashboard-Snippets

## Siehe auch

- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
