# Notion - API Documentation

## Overview
Notion offers a RESTful API for access to all Notion content. The API makes it
possible to read, write and manage pages, blocks, databases and users.

## Authentication
Notion uses OAuth2 and API tokens:

- **Internal integration token**: for integrations inside one workspace
- **OAuth2 authorization code**: for external apps
- **Bot token**: a special token for bots

### Header
```
Authorization: Bearer <your-integration-token>
Notion-Version: 2022-06-28
```

## Endpoints

### Pages
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/pages/:page_id` | Fetches a page |
| GET | `/v1/pages` | Lists pages (with a filter) |
| POST | `/v1/pages` | Creates a new page |
| PATCH | `/v1/pages/:page_id` | Updates a page |
| DELETE | `/v1/pages/:page_id` | Deletes a page |

### Blocks (content blocks)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/blocks/:block_id/children` | Lists the block children |
| PATCH | `/v1/blocks/:block_id` | Updates a block |
| POST | `/v1/blocks/:block_id/children` | Adds children |
| DELETE | `/v1/blocks/:block_id` | Deletes a block |

### Databases
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/databases/:database_id` | Fetches a database |
| POST | `/v1/databases` | Creates a database |
| POST | `/v1/databases/:database_id/query` | Query on a database |
| PATCH | `/v1/databases/:database_id` | Updates a database |

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/users` | Lists users |
| GET | `/v1/users/:user_id` | Fetches a user |
| GET | `/v1/users/me` | the current user |

### Search
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/v1/search` | Searches all content |

### Comments
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/v1/comments` | Creates a comment |

## Examples

### Fetching a page
```bash
curl -X GET "https://api.notion.com/v1/pages/12345" \
  -H "Authorization: Bearer YOUR_INTEGRATION_TOKEN" \
  -H "Notion-Version: 2022-06-28"
```

### Creating a page
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
              "content": "New Page"
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
                "content": "Content of the page"
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

### Python example
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

# Fetch a page
response = requests.get(f"{API_URL}/pages/page-id", headers=headers)
print(response.json())

# Create a page
data = {
    "parent": {
        "page_id": "parent-page-id",
        "type": "page_id"
    },
    "properties": {
        "title": {
            "title": [{"text": {"content": "New Page"}}]
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

## Rate limits
- 3 requests per second per integration
- 1 request per second for database queries
- Response headers:
  - `Notion-Request-Id`: request ID
  - `Retry-After`: waiting time when rate-limited

## Webhooks
Notion supports webhooks through the API:
- `page.created`: a new page
- `page.updated`: a page was updated
- `page.deleted`: a page was deleted
- `page.restored`: a page was restored

Configuration:
1. Create an integration with webhook permission
2. POST to `/v1/webhooks`
3. Configure the callback URL and the filter

## SDKs and client libraries
- **JavaScript**: `@notion/client` (official)
- **Python**: `notion-client` (official)
- **Go**: `go-notion` (community)
- **Java**: `notion-sdk-java` (community)
- **Ruby**: `notion-ruby` (community)
- **PHP**: `notion-php-sdk` (community)

Install:
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
