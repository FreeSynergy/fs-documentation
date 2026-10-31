# Notion - API Dokumentation

## Übersicht
Notion bietet eine RESTful API für den Zugriff auf alle Notion-Inhalte. Die API ermöglicht das Lesen, Schreiben und Verwalten von Pages, Blocks, Datenbanken und Benutzern.

## Authentifizierung
Notion nutzt OAuth2 und API Tokens:

- **Internal Integration Token**: Für Integrationen innerhalb eines Workspaces
- **OAuth2 Authorization Code**: Für externe Apps
- **Bot Token**: Spezielles Token für Bots

### Header
```
Authorization: Bearer <your-integration-token>
Notion-Version: 2022-06-28
```

## Endpunkte

### Pages
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/v1/pages/:page_id` | Holt eine Page |
| GET | `/v1/pages` | Listet Pages (mit filter) |
| POST | `/v1/pages` | Erstellt eine neue Page |
| PATCH | `/v1/pages/:page_id` | Aktualisiert eine Page |
| DELETE | `/v1/pages/:page_id` | Löscht eine Page |

### Blocks (Inhaltsblöcke)
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/v1/blocks/:block_id/children` | Listet Block-Kinder |
| PATCH | `/v1/blocks/:block_id` | Aktualisiert Block |
| POST | `/v1/blocks/:block_id/children` | Fügt Kinder hinzu |
| DELETE | `/v1/blocks/:block_id` | Löscht Block |

### Databases (Datenbanken)
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/v1/databases/:database_id` | Holt Database |
| POST | `/v1/databases` | Erstellt Database |
| POST | `/v1/databases/:database_id/query` | Query auf Database |
| PATCH | `/v1/databases/:database_id` | Aktualisiert Database |

### Users
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/v1/users` | Listet Users |
| GET | `/v1/users/:user_id` | Holt User |
| GET | `/v1/users/me` | Aktueller User |

### Search
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| POST | `/v1/search` | Durchsucht alle Inhalte |

### Comments
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| POST | `/v1/comments` | Erstellt Comment |

## Beispiele

### Seite abrufen
```bash
curl -X GET "https://api.notion.com/v1/pages/12345" \
  -H "Authorization: Bearer YOUR_INTEGRATION_TOKEN" \
  -H "Notion-Version: 2022-06-28"
```

### Seite erstellen
```bash
curl -X POST "https://api.notion.com/v1/pages" \
  -H "Authorization: Bearer YOUR_INTEGRATION_TOKEN" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{
    "parent": {
      "page_id": "parent-page-id",
      "type": "page_id"
    },
    "properties": {
      "title": {
        "title": [
          {
            "text": {
              "content": "Neue Seite"
            }
          }
        ]
      }
    },
    "children": [
      {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
          "text": [
            {
              "type": "text",
              "text": {
                "content": "Inhalt der Seite"
              }
            }
          ]
        }
      }
    ]
  }'
```

### Datenbank query
```bash
curl -X POST "https://api.notion.com/v1/databases/12345/query" \
  -H "Authorization: Bearer YOUR_INTEGRATION_TOKEN" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{
    "filter": {
      "property": "Status",
      "status": {
        "equals": "Done"
      }
    }
  }'
```

### Python Example
```python
import requests
import json

API_URL = "https://api.notion.com/v1"
INTEGRATION_TOKEN = "your-integration-token"

headers = {
    "Authorization": f"Bearer {INTEGRATION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

# Seite abrufen
response = requests.get(f"{API_URL}/pages/page-id", headers=headers)
print(response.json())

# Seite erstellen
data = {
    "parent": {
        "page_id": "parent-page-id",
        "type": "page_id"
    },
    "properties": {
        "title": {
            "title": [{"text": {"content": "Neue Seite"}}]
        }
    }
}
response = requests.post(f"{API_URL}/pages", json=data, headers=headers)
print(response.json())

# Search
search_data = {
    "query": "Suchbegriff",
    "filter": {"value": "page", "property": "object"}
}
response = requests.post(f"{API_URL}/search", json=search_data, headers=headers)
print(response.json())
```

## Rate Limits
- 3 Anfragen pro Sekunde pro Integration
- 1 Anfrage pro Sekunde für Database Queries
- Antwort-Header:
  - `Notion-Request-Id`: Request ID
  - `Retry-After`: Wartezeit bei Rate Limit

## Webhooks
Notion unterstützt Webhooks über die API:
- `page.created`: Neue Page
- `page.updated`: Page aktualisiert
- `page.deleted`: Page gelöscht
- `page.restored`: Page wiederhergestellt

Konfiguration:
1. Erstelle Integration mit Webhook-Permission
2. POST zu `/v1/webhooks`
3. Konfiguriere callback URL und filter

## SDKs und Client-Bibliotheken
- **JavaScript**: `@notion/client` (offiziell)
- **Python**: `notion-client` (offiziell)
- **Go**: `go-notion` (community)
- **Java**: `notion-sdk-java` (community)
- **Ruby**: `notion-ruby` (community)
- **PHP**: `notion-php-sdk` (community)

Installieren:
```bash
# npm
npm install @notion/client

# pip
pip install notion-client

# Go
go get github.com/RunaHQ/go-notion
```

## Siehe auch
- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
