# Element - API Dokumentation

## Übersicht
Element (Matrix-Client) bietet eine vollständige REST API über die Matrix-Specification für den Zugriff auf Nachrichten, Räume, Benutzer und Medien. Die API ermöglicht vollständige Integration in das Matrix-Netzwerk.

## Authentifizierung
Element nutzt OAuth2 und Matrix-Authentifizierung:

- **Access Token**: Direkte Authentifizierung
- **OAuth2**: Für third-party Apps
- **Login Flow**: Password, Token, Recaptcha, SSO

### Header
```
Authorization: Bearer <access-token>
Content-Type: application/json
```

## Endpunkte (Matrix API)

### Räume (Rooms)
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/_matrix/client/v3/joined_rooms` | Join Räume |
| GET | `/_matrix/client/v3/rooms/:room_id/state` | Raum-Status |
| POST | `/_matrix/client/v3/rooms/:room_id/join` | Trete Raum bei |
| POST | `/_matrix/client/v3/rooms/:room_id/leave` | Verlasse Raum |
| POST | `/_matrix/client/v3/rooms/:room_id/ban` | Ban User |
| POST | `/_matrix/client/v3/rooms/:room_id/kick` | Kick User |
| POST | `/_matrix/client/v3/rooms/:room_id/create` | Erstelle Raum |

### Nachrichten
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/_matrix/client/v3/rooms/:room_id/messages` | Nachrichten (mit filter) |
| POST | `/_matrix/client/v3/rooms/:room_id/send` | Sende Nachricht |
| PUT | `/_matrix/client/v3/rooms/:room_id/send/:msgtype/:txn_id` | Idempotenter Send |
| POST | `/_matrix/client/v3/rooms/:room_id/redact` | Redakte Nachricht |
| GET | `/_matrix/client/v3/rooms/:room_id/event/:event_id` | Holt Event |

### Media
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/_matrix/media/v3/download/:server_name/:media_id` | Download Media |
| POST | `/_matrix/media/v3/upload` | Upload Media |
| GET | `/_matrix/media/v3/thumbnail/:server_name/:media_id` | Thumbnail |

### User
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/_matrix/client/v3/account/whoami` | Aktueller User |
| GET | `/_matrix/client/v3/profile/:user_id` | User Profil |
| PUT | `/_matrix/client/v3/profile/:user_id/displayname` | SetzeDisplayName |
| PUT | `/_matrix/client/v3/profile/:user_id/avatar_url` | Setze Avatar |

### Sync
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/_matrix/client/v3/sync` | Synchronisiere (Long Polling) |
| GET | `/_matrix/client/v3/sync?filter=:filter_id` | Mit Filter |

### Typing
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| PUT | `/_matrix/client/v3/rooms/:room_id/typing/:user_id` | Typing Status |

### Read Receipts
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| POST | `/_matrix/client/v3/rooms/:room_id/read_markers` | Read Receipt |

### Push Notifications
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/_matrix/client/v3/pushers` | List Pusher |
| POST | `/_matrix/client/v3/pushers/add` | Add Pusher |
| DELETE | `/_matrix/client/v3/pushers/:pusher_id` | Delete Pusher |

### Account Data
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| PUT | `/_matrix/client/v3/user/:user_id/account_data/:event_type` | Set account data |
| GET | `/_matrix/client/v3/user/:user_id/account_data/:event_type` | Get account data |

## Beispiele

### Nachricht senden
```bash
curl -X PUT "https://matrix.example.com/_matrix/client/v3/rooms/!roomid/send/m.room.message/m12345678901234" \
  -H "Authorization: Bearer <access-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "msgtype": "m.text",
    "body": "Hallo von Element API!"
  }'
```

### Raum erstellen
```bash
curl -X POST "https://matrix.example.com/_matrix/client/v3/createRoom" \
  -H "Authorization: Bearer <access-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Mein Raum",
    "topic": "Thema dieses Raums",
    "preset": "public_chat",
    "visibility": "public"
  }'
```

### Python Example
```python
import requests
import json

MATRIX_URL = "https://matrix.example.com"
ACCESS_TOKEN = "your-access-token"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Nachricht senden
room_id = "!roomid:example.com"
txn_id = "m12345678901234"
data = {
    "msgtype": "m.text",
    "body": "Hallo, dies ist eine Test-Nachricht!"
}
response = requests.put(
    f"{MATRIX_URL}/_matrix/client/v3/rooms/{room_id}/send/m.room.message/{txn_id}",
    json=data,
    headers=headers
)
print(response.json())

# Räume listen
response = requests.get(
    f"{MATRIX_URL}/_matrix/client/v3/joined_rooms",
    headers=headers
)
print(response.json())

# User Profile
user_id = "@user:example.com"
response = requests.get(
    f"{MATRIX_URL}/_matrix/client/v3/profile/{user_id}",
    headers=headers
)
print(response.json())
```

### Node.js Example
```javascript
const axios = require('axios');

const MATRIX_URL = 'https://matrix.example.com';
const ACCESS_TOKEN = 'your-access-token';

const headers = {
    'Authorization': `Bearer ${ACCESS_TOKEN}`,
    'Content-Type': 'application/json'
};

// Nachricht senden
const room_id = '!roomid:example.com';
const txn_id = 'm12345678901234';
const data = {
    msgtype: 'm.text',
    body: 'Hallo von Node.js!'
};

axios.put(
    `${MATRIX_URL}/_matrix/client/v3/rooms/${room_id}/send/m.room.message/${txn_id}`,
    data,
    { headers }
)
    .then(response => console.log(response.data))
    .catch(error => console.error(error));

// Room Information
axios.get(
    `${MATRIX_URL}/_matrix/client/v3/rooms/${room_id}/state`,
    { headers }
)
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
```

### WebSocket Sync (Long Polling)
```javascript
let since = null;

async function sync() {
    let url = `${MATRIX_URL}/_matrix/client/v3/sync`;
    if (since) {
        url += `?since=${since}`;
    }
    
    const response = await axios.get(url, { headers });
    
    // Verarbeile Updates
    console.log('Rooms:', response.data.rooms);
    console.log('Notifications:', response.data.next_batch);
    
    since = response.data.next_batch;
    
    // Next sync
    setTimeout(sync, 1000);
}

sync();
```

## Rate Limits
- Standard: 1000 Anfragen pro Tag pro User
- Synapse Server: Konfigurierbar in `synapse.cfg`
- Antwort-Header:
  - `Retry-After`: Wartezeit bei Limit
  - `X-Rate-Limit-Limit`: Max. Anfragen
  - `X-Rate-Limit-Remaining`: Verbleibende Anfragen

## Webhooks
Element/Matrix unterstützt keine direkten Webhooks, aber:
- **Push Notifications**: Über Push Gateway
- **Bot Clients**: Regelmäßige Sync-Polling
- **Federation Webhooks**: Für Server-Admins

## SDKs und Client-Bibliotheken
- **JavaScript/TypeScript**: `matrix-js-sdk` (offiziell)
- **Python**: `matrix-client`, `python-sdk`
- **Java**: `matrix-java-sdk`
- **Go**: `go-matrix-client`
- **C#**: `SimpleMatrixNet`
- **Rust**: `ruma`, `matrix-sdk`

Installieren:
```bash
# npm
npm install matrix-js-sdk

# pip
pip install matrix-client

# Go
go get github.com/matrix-org/gomatrix
```

## Siehe auch
- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
