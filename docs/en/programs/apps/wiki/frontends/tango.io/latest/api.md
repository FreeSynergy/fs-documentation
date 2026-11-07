# Tango.io - API Documentation

## Overview
Tango.io provides a modern REST API for accessing all wiki and documentation features. The API is designed to streamline the workflow for developers and technical authors.

## Authentication
Tango.io uses OAuth2 for authentication:

- **OAuth2 Authorization Code Flow**: For web apps
- **OAuth2 Client Credentials**: For server-to-server communication
- **API Keys**: For simple authentication

### API Key Header
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
| GET | `/v1/pages/:id` | Retrieves a page |
| GET | `/v1/pages` (with `?path=/docs/beispiel`) | Retrieves a page by path |
| POST | `/v1/pages` | Creates a new page |
| PUT | `/v1/pages/:id` | Updates a page |
| DELETE | `/v1/pages/:id` | Deletes a page |
| GET | `/v1/pages/:id/versions` | Version history |

### Workspaces
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/workspaces` | Lists workspaces |
| GET | `/v1/workspaces/:id` | Retrieves workspace details |
| POST | `/v1/workspaces` | Creates workspace |

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/users` | Lists users |
| GET | `/v1/users/:id` | Retrieves user |
| GET | `/v1/users/me` | Current user |

### Comments
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/comments` | Lists comments |
| POST | `/v1/comments` | Creates comment |
| PUT | `/v1/comments/:id` | Updates comment |
| DELETE | `/v1/comments/:id` | Deletes comment |

### Search
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/search` | Search all content |

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/oauth/token` | Get token (client credentials) |
| POST | `/oauth/authorize` | Request authorization code |

## Examples

### Retrieve page
```bash
curl -X GET "https://api.tango.io/v1/pages/123" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Create page
```bash
curl -X POST "https://api.tango.io/v1/pages" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New page",
    "content": "# Title\n\nContent",
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

# Retrieve page
response = requests.get(f"{API_URL}/pages/123", headers=headers)
print(response.json())

# Create page
data = {
    "title": "Test page",
    "content": "# Test\n\nThis is a test.",
    "workspace_id": "workspace-123"
}
response = requests.post(f"{API_URL}/pages", json=data, headers=headers)
print(response.json())

# Search
response = requests.get(f"{API_URL}/search?q=example", headers=headers)
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

// Retrieve page
axios.get(`${API_URL}/pages/123`, { headers })
    .then(response => console.log(response.data))
    .catch(error => console.error(error));

// Create page
const data = {
    title: 'New page',
    content: '# Title\n\nContent',
    workspace_id: 'workspace-123'
};

axios.post(`${API_URL}/pages`, data, { headers })
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
```

## Rate Limits
- Standard: 1000 requests per hour per API key
- OAuth tokens: 100 requests per minute
- Headers in response:
  - `X-RateLimit-Limit`: Max. requests
  - `X-RateLimit-Remaining`: Remaining requests
  - `X-RateLimit-Reset`: Reset timestamp

## Webhooks
Tango.io supports webhooks for:
- `page.created`: Page created
- `page.updated`: Page updated
- `page.deleted`: Page deleted
- `comment.created`: Comment created
- `workspace.updated`: Workspace updated

Configuration under: Settings > Webhooks

## SDKs and Client Libraries
- **JavaScript/TypeScript**: `@tangoio/sdk` (official)
- **Python**: `tangoio-sdk` (official)
- **Go**: `tangoio-go` (official)
- **Java**: `tangoio-java-sdk` (official)

Installation:
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
