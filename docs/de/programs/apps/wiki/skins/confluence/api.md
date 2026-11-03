# Confluence - API Dokumentation

## Übersicht
Confluence bietet ein REST API für den Zugriff auf alle Wiki-Funktionen. Die API ermöglicht das Lesen, Schreiben und Verwalten von Pages, Spaces, Benutzern und Kommentaren.

## Authentifizierung
Confluence unterstützt mehrere Authentifizierungsmethoden:

- **Basic Authentication**: Benutzername und API Token
- **OAuth2**: Für third-party Apps
- **JWT**: Für server-zu-server Kommunikation
- **Cookie**: Authentifizierung über Session Cookie

### Basic Auth Header
```
Authorization: Basic base64(email:api-token)
```

### API Token
API Tokens werden unter `atlassian.com` erstellt (nicht im Confluence UI).

## Endpunkte

### Pages
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/rest/api/content/:id` | Holt Page |
| GET | `/rest/api/content` | Listet Pages (mit Filter) |
| POST | `/rest/api/content` | Erstellt Page |
| PUT | `/rest/api/content/:id` | Aktualisiert Page |
| DELETE | `/rest/api/content/:id` | Löscht Page |
| GET | `/rest/api/content/:id/child/page` | Listet Unterpages |
| GET | `/rest/api/content/:id/history` | Versionshistorie |

### Spaces
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/rest/api/space/:key` | Holt Space |
| GET | `/rest/api/space` | Listet Spaces |
| POST | `/rest/api/space` | Erstellt Space |

### Comments
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/rest/api/content/:id/child/comment` | Listet Comments |
| POST | `/rest/api/content/:id/child/comment` | Erstellt Comment |
| PUT | `/rest/api/content/:id/child/comment/:commentId` | Aktualisiert Comment |

### Users
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/rest/api/user` | Holt Benutzer |
| GET | `/rest/api/user/view` | Listet Benutzer |

### Search
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/rest/api/search` | Suche |

### Attachments
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/rest/api/content/:id/child/attachment` | Listet Attachments |
| POST | `/rest/api/content/:id/child/attachment` | Fügt Attachment hinzu |
| GET | `/rest/api/content/:id/child/attachment/:attachId` | Holt Attachment |

### Macro
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/rest/api/content/:id/child/macro` | Listet Macros |

## Beispiele

### Seite abrufen
```bash
curl -X GET "https://confluence.example.com/rest/api/content/12345" \
  -H "Authorization: Basic base64(user@example.com:api-token)" \
  -H "Accept: application/json"
```

### Seite erstellen
```bash
curl -X POST "https://confluence.example.com/rest/api/content" \
  -H "Authorization: Basic base64(user@example.com:api-token)" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "page",
    "title": "Neue Seite",
    "space": {
      "key": "SPACEKEY"
    },
    "body": {
      "storage": {
        "value": "<p>Dies ist eine neue Seite.</p>",
        "representation": "storage"
      }
    }
  }'
```

### Python Example
```python
import requests
import base64

API_URL = "https://confluence.example.com/rest/api"
EMAIL = "user@example.com"
API_TOKEN = "api-token"

# Basic Auth Header
auth = requests.auth.HTTPBasicAuth(EMAIL, API_TOKEN)
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Seite abrufen
response = requests.get(f"{API_URL}/content/12345", auth=auth, headers=headers)
print(response.json())

# Seite erstellen
data = {
    "type": "page",
    "title": "Neue Seite",
    "space": {"key": "SPACEKEY"},
    "body": {
        "storage": {
            "value": "<p>Inhalt der Seite</p>",
            "representation": "storage"
        }
    }
}
response = requests.post(f"{API_URL}/content", json=data, auth=auth, headers=headers)
print(response.json())

# Suche
params = {"cql": "title ~ 'Suchbegriff'"}
response = requests.get(f"{API_URL}/search", params=params, auth=auth, headers=headers)
print(response.json())
```

### JavaScript Example
```javascript
const axios = require('axios');

const API_URL = 'https://confluence.example.com/rest/api';
const EMAIL = 'user@example.com';
const API_TOKEN = 'api-token';

const auth = {
    username: EMAIL,
    password: API_TOKEN
};

const headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
};

// Seite abrufen
axios.get(`${API_URL}/content/12345`, { auth, headers })
    .then(response => console.log(response.data))
    .catch(error => console.error(error));

// Seite erstellen
const data = {
    type: 'page',
    title: 'Neue Seite',
    space: { key: 'SPACEKEY' },
    body: {
        storage: {
            value: '<p>Inhalt</p>',
            representation: 'storage'
        }
    }
};

axios.post(`${API_URL}/content`, data, { auth, headers })
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
```

## Rate Limits
- Standard: 200 Anfragen pro 5 Minuten pro Benutzer
- Confluence Cloud: 100 Anfragen pro Sekunde
- Antwort-Header:
  - `X-AUTH-_RATE-LIMIT-REMAINING`: Verbleibende Anfragen
  - `X-AUTH-_RATE-LIMIT-RESET`: Reset Zeit

## Webhooks
Confluence unterstützt Webhooks:
- `page.created`: Seite erstellt
- `page.updated`: Seite aktualisiert
- `page.deleted`: Seite gelöscht
- `comment.created`: Kommentar erstellt
- `space.created`: Space erstellt

Konfiguration: `POST /rest/webhooks/1.0/webhook`

## SDKs und Client-Bibliotheken
- **JavaScript**: `@atlassian/confluence-api` (offiziell)
- **Python**: `atlassian-python-api` (community)
- **Java**: `atlassian-java-client` (offiziell)
- **Go**: `go-confluence` (community)
- **PHP**: `atlassian-php-sdk` (community)

Installieren:
```bash
# npm
npm install @atlassian/confluence-api

# pip
pip install atlassian-python-api

# Go
go get github.com/ctessier/go-confluence
```

## Siehe auch
- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
