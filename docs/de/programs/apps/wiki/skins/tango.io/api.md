# Tango.io - API Dokumentation

## Übersicht
Tango.io bietet eine moderne REST API für den Zugriff auf alle Wiki- und Dokumentationsfunktionen. Die API ist darauf ausgelegt, den Workflow für Entwickler und technische Autoren zu optimieren.

## Authentifizierung
Tango.io nutzt OAuth2 für die Authentifizierung:

- **OAuth2 Authorization Code Flow**: Für Web-Apps
- **OAuth2 Client Credentials**: Für Server-zu-Server Kommunikation
- **API Keys**: Für einfache Authentifizierung

### API Key Header
```
Authorization: Bearer <your-oauth-token>
# oder
X-API-Key: <your-api-key>
```

## Endpunkte

### Pages (Seiten)
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/v1/pages` | Listet alle Seiten |
| GET | `/v1/pages/:id` | Holt eine Seite |
| GET | `/v1/pages` (mit `?path=/docs/beispiel`) | Seite über Pfad abrufen |
| POST | `/v1/pages` | Erstellt eine neue Seite |
| PUT | `/v1/pages/:id` | Aktualisiert eine Seite |
| DELETE | `/v1/pages/:id` | Löscht eine Seite |
| GET | `/v1/pages/:id/versions` | Versionshistorie |

### Workspaces (Arbeitsbereiche)
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/v1/workspaces` | Listet Workspaces |
| GET | `/v1/workspaces/:id` | Holt Workspace Details |
| POST | `/v1/workspaces` | Erstellt Workspace |

### Users (Benutzer)
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/v1/users` | Listet Benutzer |
| GET | `/v1/users/:id` | Holt Benutzer |
| GET | `/v1/users/me` | Aktueller Benutzer |

### Comments (Kommentare)
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/v1/comments` | Listet Kommentare |
| POST | `/v1/comments` | Erstellt Kommentar |
| PUT | `/v1/comments/:id` | Aktualisiert Kommentar |
| DELETE | `/v1/comments/:id` | Löscht Kommentar |

### Search
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/v1/search` | Suche in allen Inhalten |

### Authentication
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| POST | `/oauth/token` | Token abrufen (Client Credentials) |
| POST | `/oauth/authorize` | Autorisierungscode anfordern |

## Beispiele

### Seite abrufen
```bash
curl -X GET "https://api.tango.io/v1/pages/123" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Seite erstellen
```bash
curl -X POST "https://api.tango.io/v1/pages" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Neue Seite",
    "content": "# Titel\n\nInhalt",
    "workspace_id": "workspace-123",
    "path": "/docs/neue-seite"
  }'
```

### Python Example
```python
import requests

API_URL = "https://api.tango.io/v1"
ACCESS_TOKEN = "your-access-token"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Seite abrufen
response = requests.get(f"{API_URL}/pages/123", headers=headers)
print(response.json())

# Seite erstellen
data = {
    "title": "Test Seite",
    "content": "# Test\n\nDies ist ein Test.",
    "workspace_id": "workspace-123"
}
response = requests.post(f"{API_URL}/pages", json=data, headers=headers)
print(response.json())

# Suche
response = requests.get(f"{API_URL}/search?q=Beispiel", headers=headers)
print(response.json())
```

### Node.js Example
```javascript
const axios = require('axios');

const API_URL = 'https://api.tango.io/v1';
const ACCESS_TOKEN = 'your-access-token';

const headers = {
    'Authorization': `Bearer ${ACCESS_TOKEN}`,
    'Content-Type': 'application/json'
};

// Seite abrufen
axios.get(`${API_URL}/pages/123`, { headers })
    .then(response => console.log(response.data))
    .catch(error => console.error(error));

// Seite erstellen
const data = {
    title: 'Neue Seite',
    content: '# Titel\n\nInhalt',
    workspace_id: 'workspace-123'
};

axios.post(`${API_URL}/pages`, data, { headers })
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
```

## Rate Limits
- Standard: 1000 Anfragen pro Stunde pro API Key
- OAuth Tokens: 100 Anfragen pro Minute
- Headers in Antwort:
  - `X-RateLimit-Limit`: Max. Anfragen
  - `X-RateLimit-Remaining`: Verbleibende Anfragen
  - `X-RateLimit-Reset`: Reset Zeitstempel

## Webhooks
Tango.io unterstützt Webhooks für:
- `page.created`: Seite erstellt
- `page.updated`: Seite aktualisiert
- `page.deleted`: Seite gelöscht
- `comment.created`: Kommentar erstellt
- `workspace.updated`: Workspace aktualisiert

Konfiguration unter: Settings > Webhooks

## SDKs und Client-Bibliotheken
- **JavaScript/TypeScript**: `@tangoio/sdk` (offiziell)
- **Python**: `tangoio-sdk` (offiziell)
- **Go**: `tangoio-go` (offiziell)
- **Java**: `tangoio-java-sdk` (offiziell)

Installieren:
```bash
# npm
npm install @tangoio/sdk

# pip
pip install tangoio-sdk

# Go
go get github.com/tangoio/tangoio-go
```

## Siehe auch
- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
