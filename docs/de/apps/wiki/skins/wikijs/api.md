# Wiki.js - API Dokumentation

## Übersicht
Wiki.js bietet eine vollständige REST API und ein GraphQL API für den Zugriff auf alle Wiki-Funktionen. Die API ermöglicht das Lesen, Schreiben und Verwalten von Seiten, Benutzern, Berechtigungen und anderen Wiki-Konfigurationen.

## Authentifizierung
Wiki.js unterstützt mehrere Authentifizierungsmethoden:

- **API Tokens**: Erstellen Sie API-Tokens in den Administrations-Einstellungen unter "Configuration > API Tokens"
- **Session Cookie**: Authentifizierung über bestehende Session (für interne Nutzung)
- **OAuth2**: Integration mit unterstützten OAuth2-Anbietern

### API Token Header
```
Authorization: Bearer <your-api-token>
```

## Endpunkte

### Pages (Seiten)
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/api/v1/pages` | Listet alle Seiten (mit Pagination) |
| GET | `/api/v1/pages/:id` | Holt eine einzelne Seite |
| GET | `/api/v1/pages/:id/content` | Holt den Inhalt einer Seite |
| POST | `/api/v1/pages` | Erstellt eine neue Seite |
| PUT | `/api/v1/pages/:id` | Aktualisiert eine Seite |
| DELETE | `/api/v1/pages/:id` | Löscht eine Seite |
| GET | `/api/v1/pages/:id/history` | Holt die Versionshistorie |

### Users (Benutzer)
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/api/v1/users` | Listet alle Benutzer |
| GET | `/api/v1/users/:id` | Holt einen Benutzer |
| POST | `/api/v1/users` | Erstellt einen neuen Benutzer |
| PUT | `/api/v1/users/:id` | Aktualisiert einen Benutzer |
| DELETE | `/api/v1/users/:id` | Löscht einen Benutzer |

### Authentication
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| POST | `/api/v1/auth/login` | Benutzer einloggen |
| POST | `/api/v1/auth/logout` | Benutzer ausloggen |
| POST | `/api/v1/auth/refresh` | Token aktualisieren |

### Metadata
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/api/v1/meta` | Holt Wiki-Metadaten |
| GET | `/api/v1/meta/stats` | Holt Statistiken |

### GraphQL API
Wiki.js bietet auch eine vollständige GraphQL API unter `/graphql` mit Query- und Mutation-Operationen für alle Ressourcen.

## Beispiele

### Seite abrufen (REST)
```bash
curl -X GET https://wiki.example.com/api/v1/pages/1 \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

### Seite erstellen
```bash
curl -X POST https://wiki.example.com/api/v1/pages \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Neue Seite",
    "description": "Beschreibung",
    "content": "# Titel\n\nInhalt",
    "path": "/neue-seite",
    "public": true
  }'
```

### GraphQL Query
```bash
curl -X POST https://wiki.example.com/graphql \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "query { pages { edges { node { id title path } } } }"
  }'
```

### Python Example
```python
import requests

API_TOKEN = "your-token"
BASE_URL = "https://wiki.example.com/api/v1"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# Seite abrufen
response = requests.get(f"{BASE_URL}/pages/1", headers=headers)
print(response.json())

# Seite erstellen
data = {
    "title": "Test Seite",
    "content": "# Test\n\nDies ist ein Test.",
    "path": "/test"
}
response = requests.post(f"{BASE_URL}/pages", json=data, headers=headers)
print(response.json())
```

## Rate Limits
- Standard: 100 Anfragen pro Minute pro API Token
- Konfigurierbar in den Administrations-Einstellungen
- Rate Limit Header werden in jeder Antwort zurückgegeben:
  - `X-RateLimit-Limit`: Max. Anfragen pro Minute
  - `X-RateLimit-Remaining`: Verbleibende Anfragen
  - `X-RateLimit-Reset`: Zeitpunkt des Resets

## Webhooks
Wiki.js unterstützt Webhooks für folgende Ereignisse:
- `page.create`: Neue Seite erstellt
- `page.update`: Seite aktualisiert
- `page.delete`: Seite gelöscht
- `page.move`: Seite verschoben
- `page.revert`: Seite wiederhergestellt

Konfiguration unter: Configuration > Webhooks

## SDKs und Client-Bibliotheken
- **JavaScript/TypeScript**: `wiki.js-api-client` (offiziell)
- **Python**: `pywikijs` (community)
- **Node.js**: Offizieller SDK über npm

Installieren:
```bash
npm install wiki.js-api-client
```

## Siehe auch
- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
