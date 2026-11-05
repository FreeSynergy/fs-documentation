# Restream - API documentation

## Overview

Restream is SaaS. The publicly documented API surface (as of the research date) covers **REST interfaces** for accounts, channels, events, platforms and stream keys, plus **WebSocket interfaces** for chat and streaming status. The provider's developer portal is authoritative; the overview below is deliberately conservative.

## Authentication

| Method | Use |
|--------|-----|
| OAuth access token | REST and WebSocket calls on behalf of the account |
| Account login (email/password, 2FA) | dashboard only, not the API |

### Header

```
Authorization: Bearer <access_token>
Content-Type: application/json
```

### URL format (REST)

```
https://api.restream.io/v1/<area>
```

## Endpoints (overview)

| Area | Description |
|------|-------------|
| **User** | profile and account information |
| **Platforms** | publicly available target platforms |
| **Channels** | create, list, change and disconnect connected targets |
| **Stream keys** | manage ingest keys and URLs |
| **Events** | schedule, change, start and stop planned streams |
| **Monitoring** | status values and metrics for streams and events |

> The exact paths, field names and plan prerequisites are in the provider's developer portal (API catalogue/Postman collection). Compare against it before implementing a skin.

## WebSockets

| Interface | Purpose |
|-----------|---------|
| Chat | send/receive messages of all connected platforms in real time (`wss`) |
| Streaming updates | live status: outgoing stream, platform status, viewer counts (`wss`) |

## Examples

### List the connected channels

```bash
curl -s https://api.restream.io/v1/channels \
  -H 'Authorization: Bearer <access_token>'
```

```json
[
  { "id": 1234, "type": "youtube", "title": "Main channel", "isStreamOn": false },
  { "id": 1235, "type": "twitch",  "title": "Second Channel", "isStreamOn": true }
]
```

### Python: subscribe to the status stream (conceptual)

```python
import json, websocket

WS = "wss://streaming.api.restream.io/ws"

def on_message(ws, message):
    print(json.loads(message))   # status, platform updates, viewer counts

ws = websocket.WebSocketApp(WS,
        header={"Authorization": "Bearer <access_token>"},
        on_message=on_message)
ws.run_forever()
```

## Rate limits

- **no stably documented rate limits**; work with moderate poll intervals and take status events from the WebSockets
- API access differs in scope depending on the subscription plan

## Webhooks

- no classically documented webhooks; real-time events arrive through the **WebSocket** interfaces

## SDKs and client libraries

- **no official SDKs** — use REST and WebSockets with the usual HTTP/WS clients
- embedded player and chat widgets as dashboard snippets

## See also

- [menus.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [layout.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
