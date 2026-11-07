# Wiki.js - API Documentation

## Overview
Wiki.js provides a complete REST API and a GraphQL API for accessing all wiki features. The API enables reading, writing and managing pages, users, permissions and other wiki configuration.

## Authentication
Wiki.js supports several authentication methods:

- **API tokens**: Create API tokens in the administration settings under "Configuration > API Tokens"
- **Session cookie**: Authentication via an existing session (for internal use)
- **OAuth2**: Integration with supported OAuth2 providers

### API Token Header
```
Authorization: Bearer <your-api-token>
```

## Endpoints

### Pages
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/pages` | Lists all pages (with pagination) |
| GET | `/api/v1/pages/:id` | Retrieves a single page |
| GET | `/api/v1/pages/:id/content` | Retrieves the content of a page |
| POST | `/api/v1/pages` | Creates a new page |
| PUT | `/api/v1/pages/:id` | Updates a page |
| DELETE | `/api/v1/pages/:id` | Deletes a page |
| GET | `/api/v1/pages/:id/history` | Retrieves the version history |

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/users` | Lists all users |
| GET | `/api/v1/users/:id` | Retrieves a user |
| POST | `/api/v1/users` | Creates a new user |
| PUT | `/api/v1/users/:id` | Updates a user |
| DELETE | `/api/v1/users/:id` | Deletes a user |

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/login` | Log in user |
| POST | `/api/v1/auth/logout` | Log out user |
| POST | `/api/v1/auth/refresh` | Refresh token |

### Metadata
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/meta` | Retrieves wiki metadata |
| GET | `/api/v1/meta/stats` | Retrieves statistics |

### GraphQL API
Wiki.js also provides a complete GraphQL API at `/graphql` with query and mutation operations for all resources.

## Examples

### Retrieve page (REST)
```bash
curl -X GET https://wiki.example.com/api/v1/pages/1 \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

### Create page
```bash
curl -X POST https://wiki.example.com/api/v1/pages \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New page",
    "description": "Description",
    "content": "# Title\n\nContent",
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

# Retrieve page
response = requests.get(f"{BASE_URL}/pages/1", headers=headers)
print(response.json())

# Create page
data = {
    "title": "Test page",
    "content": "# Test\n\nThis is a test.",
    "path": "/test"
}
response = requests.post(f"{BASE_URL}/pages", json=data, headers=headers)
print(response.json())
```

## Rate Limits
- Standard: 100 requests per minute per API token
- Configurable in the administration settings
- Rate limit headers are returned in every response:
  - `X-RateLimit-Limit`: Max. requests per minute
  - `X-RateLimit-Remaining`: Remaining requests
  - `X-RateLimit-Reset`: Time of reset

## Webhooks
Wiki.js supports webhooks for the following events:
- `page.create`: New page created
- `page.update`: Page updated
- `page.delete`: Page deleted
- `page.move`: Page moved
- `page.revert`: Page restored

Configuration under: Configuration > Webhooks

## SDKs and Client Libraries
- **JavaScript/TypeScript**: `wiki.js-api-client` (official)
- **Python**: `pywikijs` (community)
- **Node.js**: Official SDK via npm

Installation:
```bash
npm install wiki.js-api-client
```

## See also
- [menu.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
