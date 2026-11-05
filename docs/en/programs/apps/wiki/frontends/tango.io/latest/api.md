# Tango.io - API Documentation

## Overview
Tango.io offers a modern REST API for access to all wiki and documentation
functions. The API is designed to optimise the workflow for developers and
technical writers.

## Authentication
Tango.io uses OAuth2 for authentication:

- **OAuth2 authorization code flow**: for web apps
- **OAuth2 client credentials**: for server-to-server communication
- **API keys**: for simple authentication

### API key header
```
Authorization: Bearer <your-oauth-token>
# or
X-API-Key: <your-api-key>
```

## Endpoints

### Pages
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/pages` | Lists all pages |
| GET | `/v1/pages/:id` | Fetches a page |
| GET | `/v1/pages` (with `?path=/docs/example`) | fetch a page by path |
| POST | `/v1/pages` | Creates a new page |
| PUT | `/v1/pages/:id` | Updates a page |
| DELETE | `/v1/pages/:id` | Deletes a page |
| GET | `/v1/pages/:id/versions` | Version history |

### Workspaces (work areas)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/workspaces` | Lists workspaces |
| GET | `/v1/workspaces/:id` | Fetches the workspace details |
| POST | `/v1/workspaces` | Creates a workspace |

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/users` | Lists users |
| GET | `/v1/users/:id` | Fetches a user |
| GET | `/v1/users/me` | the current user |

### Comments
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/comments` | Lists comments |
| POST | `/v1/comments` | Creates a comment |
| PUT | `/v1/comments/:id` | Updates a comment |
| DELETE | `/v1/comments/:id` | Deletes a comment |

### Search
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/search` | Search in all content |

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/oauth/token` | Fetch a token (client credentials) |
| POST | `/oauth/authorize` | Request an authorization code |

## Examples

### Fetching a page
```bash
curl -X GET "https://api.tango.io/v1/pages/123" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Creating a page
```bash
curl -X POST "https://api.tango.io/v1/pages" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New Page",
    "content": "# Title\n\nContent",
    "workspace_id": "workspace-123",
    "path": "/docs/new-page"
  }'
```

### Python example
```python
import requests

API_URL = "https://api.tango.io/v1"
ACCESS_TOKEN = "your-access-token"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Fetch a page
response = requests.get(f"{API_URL}/pages/123", headers=headers)
print(response.json())

# Create a page
data = {
    "title": "Test Page",
    "content": "# Test\n\nThis is a test.",
    "workspace_id": "workspace-123"
}
response = requests.post(f"{API_URL}/pages", json=data, headers=headers)
print(response.json())

# Search
response = requests.get(f"{API_URL}/search?q=example", headers=headers)
print(response.json())
```

### Node.js example
```javascript
const axios = require('axios');

const API_URL = 'https://api.tango.io/v1';
const ACCESS_TOKEN = 'your-access-token';

const headers = {
    'Authorization': `Bearer ${ACCESS_TOKEN}`,
    'Content-Type': 'application/json'
};

// Fetch a page
axios.get(`${API_URL}/pages/123`, { headers })
    .then(response => console.log(response.data))
    .catch(error => console.error(error));

// Create a page
const data = {
    title: 'New Page',
    content: '# Title\n\nContent',
    workspace_id: 'workspace-123'
};

axios.post(`${API_URL}/pages`, data, { headers })
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
```

## Rate limits
- Default: 1000 requests per hour per API key
- OAuth tokens: 100 requests per minute
- Headers in the response:
  - `X-RateLimit-Limit`: maximum requests
  - `X-RateLimit-Remaining`: remaining requests
  - `X-RateLimit-Reset`: reset timestamp

## Webhooks
Tango.io supports webhooks for:
- `page.created`: a page was created
- `page.updated`: a page was updated
- `page.deleted`: a page was deleted
- `comment.created`: a comment was created
- `workspace.updated`: a workspace was updated

Configuration under: Settings > Webhooks

## SDKs and client libraries
- **JavaScript/TypeScript**: `@tangoio/sdk` (official)
- **Python**: `tangoio-sdk` (official)
- **Go**: `tangoio-go` (official)
- **Java**: `tangoio-java-sdk` (official)

Install:
```bash
# npm
npm install @tangoio/sdk

# pip
pip install tangoio-sdk

# Go
go get github.com/tangoio/tangoio-go
```

## See also
- [menu.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
