# Wiki.js - API Documentation

## Overview
Wiki.js offers a complete REST API and a GraphQL API for access to all wiki
functions. The API makes it possible to read, write and manage pages, users,
permissions and other wiki configurations.

## Authentication
Wiki.js supports several authentication methods:

- **API tokens**: create API tokens in the administration settings under "Configuration > API Tokens"
- **Session cookie**: authentication through an existing session (for internal use)
- **OAuth2**: integration with supported OAuth2 providers

### API token header
```
Authorization: Bearer <your-api-token>
```

## Endpoints

### Pages
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/pages` | Lists all pages (with pagination) |
| GET | `/api/v1/pages/:id` | Fetches a single page |
| GET | `/api/v1/pages/:id/content` | Fetches the content of a page |
| POST | `/api/v1/pages` | Creates a new page |
| PUT | `/api/v1/pages/:id` | Updates a page |
| DELETE | `/api/v1/pages/:id` | Deletes a page |
| GET | `/api/v1/pages/:id/history` | Fetches the version history |

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/users` | Lists all users |
| GET | `/api/v1/users/:id` | Fetches a user |
| POST | `/api/v1/users` | Creates a new user |
| PUT | `/api/v1/users/:id` | Updates a user |
| DELETE | `/api/v1/users/:id` | Deletes a user |

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/login` | Logs a user in |
| POST | `/api/v1/auth/logout` | Logs a user out |
| POST | `/api/v1/auth/refresh` | Refreshes the token |

### Metadata
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/meta` | Fetches the wiki metadata |
| GET | `/api/v1/meta/stats` | Fetches the statistics |

### GraphQL API
Wiki.js also offers a complete GraphQL API under `/graphql` with query and
mutation operations for all resources.

## Examples

### Fetching a page (REST)
```bash
curl -X GET https://wiki.example.com/api/v1/pages/1 \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

### Creating a page
```bash
curl -X POST https://wiki.example.com/api/v1/pages \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New Page",
    "description": "Description",
    "content": "# Title\n\nContent",
    "path": "/new-page",
    "public": true
  }'
```

### GraphQL query
```bash
curl -X POST https://wiki.example.com/graphql \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "query { pages { edges { node { id title path } } } }"
  }'
```

### Python example
```python
import requests

API_TOKEN = "your-token"
BASE_URL = "https://wiki.example.com/api/v1"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# Fetch a page
response = requests.get(f"{BASE_URL}/pages/1", headers=headers)
print(response.json())

# Create a page
data = {
    "title": "Test Page",
    "content": "# Test\n\nThis is a test.",
    "path": "/test"
}
response = requests.post(f"{BASE_URL}/pages", json=data, headers=headers)
print(response.json())
```

## Rate limits
- Default: 100 requests per minute per API token
- Configurable in the administration settings
- The rate limit headers are returned in every response:
  - `X-RateLimit-Limit`: maximum requests per minute
  - `X-RateLimit-Remaining`: remaining requests
  - `X-RateLimit-Reset`: time of the reset

## Webhooks
Wiki.js supports webhooks for the following events:
- `page.create`: a new page was created
- `page.update`: a page was updated
- `page.delete`: a page was deleted
- `page.move`: a page was moved
- `page.revert`: a page was restored

Configuration under: Configuration > Webhooks

## SDKs and client libraries
- **JavaScript/TypeScript**: `wiki.js-api-client` (official)
- **Python**: `pywikijs` (community)
- **Node.js**: official SDK via npm

Install:
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
