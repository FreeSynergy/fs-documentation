# Notion - API Documentation

## Overview
Notion provides a RESTful API for accessing all Notion content. The API enables reading, writing and managing pages, blocks, databases and users.

## Authentication
Notion uses OAuth2 and API tokens:

- **Internal Integration Token**: For integrations within a workspace
- **OAuth2 Authorization Code**: For external apps
- **Bot Token**: Special token for bots

### Header
```
Authorization: Bearer <your-integration-token>
Notion-Version: 2022-06-28
```

## Endpoints

### Pages
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/pages/:page_id` | Retrieves a page |
| GET | `/v1/pages` | Lists pages (with filter) |
| POST | `/v1/pages` | Creates a new page |
| PATCH | `/v1/pages/:page_id` | Updates a page |
| DELETE | `/v1/pages/:page_id` | Deletes a page |

### Blocks (Content Blocks)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/blocks/:block_id/children` | Lists block children |
| PATCH | `/v1/blocks/:block_id` | Updates block |
| POST | `/v1/blocks/:block_id/children` | Adds children |
| DELETE | `/v1/blocks/:block_id` | Deletes block |

### Databases
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/databases/:database_id` | Retrieves database |
| POST | `/v1/databases` | Creates database |
| POST | `/v1/databases/:database_id/query` | Queries database |
| PATCH | `/v1/databases/:database_id` | Updates database |

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/users` | Lists users |
| GET | `/v1/users/:user_id` | Retrieves user |
| GET | `/v1/users/me` | Current user |

### Search
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/v1/search` | Searches all content |

### Comments
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/v1/comments` | Creates comment |

## Examples

### Retrieve page
```bash
curl -X GET "https://api.notion.com/v1/pages/12345" \
  -H "Authorization: Bearer YOUR_INTEGRATION_TOKEN" \
  -H "Notion-Version: 2022-06-28"
```

### Create page
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
              "content": "New page"
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
                "content": "Page content"
              }
            }
          ]
        }
      }
    ]
  }'
```

### Database query
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

# Retrieve page
response = requests.get(f"{API_URL}/pages/page-id", headers=headers)
print(response.json())

# Create page
data = {
    "parent": {
        "page_id": "parent-page-id",
        "type": "page_id"
    },
    "properties": {
        "title": {
            "title": [{"text": {"content": "New page"}}]
        }
    }
}
response = requests.post(f"{API_URL}/pages", json=data, headers=headers)
print(response.json())

# Search
search_data = {
    "query": "search term",
    "filter": {"value": "page", "property": "object"}
}
response = requests.post(f"{API_URL}/search", json=search_data, headers=headers)
print(response.json())
```

## Rate Limits
- 3 requests per second per integration
- 1 request per second for database queries
- Response headers:
  - `Notion-Request-Id`: Request ID
  - `Retry-After`: Wait time on rate limiting

## Webhooks
Notion supports webhooks via the API:
- `page.created`: New page
- `page.updated`: Page updated
- `page.deleted`: Page deleted
- `page.restored`: Page restored

Configuration:
1. Create an integration with webhook permission
2. POST to `/v1/webhooks`
3. Configure callback URL and filter

## SDKs and Client Libraries
- **JavaScript**: `@notion/client` (official)
- **Python**: `notion-client` (official)
- **Go**: `go-notion` (community)
- **Java**: `notion-sdk-java` (community)
- **Ruby**: `notion-ruby` (community)
- **PHP**: `notion-php-sdk` (community)

Installation:
```bash
# npm
npm install @notion/client

# pip
pip install notion-client

# Go
go get github.com/RunaHQ/go-notion
```

## See also
- [menu.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
