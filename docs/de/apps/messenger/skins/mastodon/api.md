# Mastodon - API Dokumentation

## Übersicht
Mastodon bietet eine REST API für den Zugriff auf alle sozialen Funktionen. Die API ermöglicht das Lesen, Schreiben und Verwalten von Toots, Benutzern, Konten und Medien.

## Authentifizierung
Mastodon nutzt OAuth2:

- **OAuth2 Authorization Code Flow**: Für Web-Apps
- **OAuth2 Client Credentials**: Für App-only Zugriff

### Header
```
Authorization: Bearer <access-token>
Content-Type: application/json
```

## Endpunkte

### Accounts
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/api/v1/accounts/:id` | Account Details |
| GET | `/api/v1/accounts/verify_credentials` | Aktueller Account |
| PATCH | `/api/v1/accounts/update_credentials` | Account aktualisieren |
| GET | `/api/v1/accounts/:id/statuses` | Status Updates |
| POST | `/api/v1/accounts/:id/follow` | Folge Account |
| POST | `/api/v1/accounts/:id/unfollow` | Entfolge Account |

### Tooots (Status)
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/api/v1/timelines/home` | Home Timeline |
| GET | `/api/v1/timelines/public` | Öffentliche Timeline |
| GET | `/api/v1/timelines/tag/:hashtag` | Hashtag Timeline |
| GET | `/api/v1/statuses/:id` | Status Details |
| POST | `/api/v1/statuses` | Status erstellen |
| DELETE | `/api/v1/statuses/:id` | Status löschen |
| POST | `/api/v1/statuses/:id/favourite` | Favouriten |
| POST | `/api/v1/statuses/:id/reblog` | Reblog |
| POST | `/api/v1/statuses/:id/mute` | Status muten |
| POST | `/api/v1/statuses/:id/bookmark` | Status bookmarken |

### Medien
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| POST | `/api/v1/media` | Medien hochladen |
| GET | `/api/v1/media/:id` | Medien Details |

### Notifications
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/api/v1/notifications` | Notifications |
| POST | `/api/v1/notifications/:id/dismiss` | Notification entfernen |
| DELETE | `/api/v1/notifications` | Alle entfernen |

### Followers
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/api/v1/accounts/:id/followers` | Followers |
| GET | `/api/v1/accounts/:id/following` | Following |

### Search
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/api/v1/search` | Suche (Accounts, Hashtags, Status) |

### Mutes
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/api/v1/mutes` | Muted Accounts |
| POST | `/api/v1/accounts/:id/mute` | Account muten |
| POST | `/api/v1/accounts/:id/unmute` | Account unmuten |

### Blocks
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/api/v1/blocks` | Blocked Accounts |
| POST | `/api/v1/accounts/:id/block` | Account blockieren |
| POST | `/api/v1/accounts/:id/unblock` | Account entblocken |

### Filters
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/api/v1/filters` | Filter |
| POST | `/api/v1/filters` | Filter erstellen |
| PUT | `/api/v1/filters/:id` | Filter aktualisieren |

### Instances
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/api/v1/instance` | Instance Info |
| GET | `/api/v1/instance/peers` | Verbundene Instanzen |

## Beispiele

### Status erstellen
```bash
curl -X POST "https://mastodon.example.com/api/v1/statuses" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "status": "Hallo von Mastodon API!",
    "visibility": "public"
  }'
```

### Status mit Medien
```bash
# 1. Medien hochladen
curl -X POST "https://mastodon.example.com/api/v1/media" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -F "file=@image.jpg"

# 2. Status mit Media ID erstellen
curl -X POST "https://mastodon.example.com/api/v1/statuses" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "status": "Bild teilen",
    "media_ids": ["MEDIA_ID_HIER"]
  }'
```

### Python Example
```python
import requests
import json

MASTODON_API = "https://mastodon.example.com/api/v1"
ACCESS_TOKEN = "your-access-token"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Status erstellen
data = {
    "status": "Hallo, dies ist ein Test-Toot!",
    "visibility": "public"
}
response = requests.post(
    f"{MASTODON_API}/statuses",
    json=data,
    headers=headers
)
print(response.json())

# Home Timeline
response = requests.get(
    f"{MASTODON_API}/timelines/home",
    headers=headers
)
print(response.json())

# Account aktualisieren
profile_data = {
    "display_name": "Mein Name",
    "note": "Meine Beschreibung"
}
response = requests.patch(
    f"{MASTODON_API}/accounts/update_credentials",
    json=profile_data,
    headers=headers
)
print(response.json())
```

### Node.js Example
```javascript
const axios = require('axios');

const MASTODON_API = 'https://mastodon.example.com/api/v1';
const ACCESS_TOKEN = 'your-access-token';

const headers = {
    'Authorization': `Bearer ${ACCESS_TOKEN}`,
    'Content-Type': 'application/json'
};

// Status erstellen
const data = {
    status: 'Hallo von Node.js!',
    visibility: 'public'
};

axios.post(`${MASTODON_API}/statuses`, data, { headers })
    .then(response => console.log(response.data))
    .catch(error => console.error(error));

// Home Timeline
axios.get(`${MASTODON_API}/timelines/home`, { headers })
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
```

### Medien Upload (Python)
```python
import requests

MASTODON_API = "https://mastodon.example.com/api/v1"
ACCESS_TOKEN = "your-access-token"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

# Medien hochladen
with open('image.jpg', 'rb') as f:
    files = {'file': f}
    response = requests.post(
        f"{MASTODON_API}/media",
        headers=headers,
        files=files
    )
    media_id = response.json()['id']
    print(f"Media ID: {media_id}")
```

## Rate Limits
- Standard: 300 Anfragen pro 5 Minuten pro Token
- Antwort-Header:
  - `X-RateLimit-Limit`: Max. Anfragen (300)
  - `X-RateLimit-Remaining`: Verbleibende Anfragen
  - `X-RateLimit-Reset`: Reset Zeit (Unix Timestamp)

## Webhooks
Mastodon hat kein eingebautes Webhook-System, aber:
- **Streaming API**: Echtzeit über Server-Sent Events
- **Polling**: Regelmäßige Status-Abfragen

### Streaming API
```bash
curl -X GET "https://mastodon.example.com/api/v1/streaming/?stream=user" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Stream-Typen:
- `user`: User Notifications
- `public`: Öffentliche Timeline
- `hashtag`: Hashtag Stream
- `direct`: Direkte Nachrichten

## SDKs und Client-Bibliotheken
- **JavaScript**: `toot` (offiziell empfohlen)
- **Python**: `python-mastodon`
- **Ruby**: `mastodon-api`
- **Go**: `go-mastodon`
- **Java**: `mastodon4j`

Installieren:
```bash
# npm
npm install toot

# pip
pip install Mastodon.py

# Go
go get github.com/mattn/go-mastodon
```

## Siehe auch
- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
