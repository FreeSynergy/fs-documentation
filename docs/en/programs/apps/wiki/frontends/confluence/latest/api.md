# Confluence - API Documentation

## Overview
Confluence offers a REST API for access to all wiki functions. The API makes it
possible to read, write and manage pages, spaces, users and comments.

## Authentication
Confluence supports several authentication methods:

- **Basic authentication**: username and API token
- **OAuth2**: for third-party apps
- **JWT**: for server-to-server communication
- **Cookie**: authentication through the session cookie

### Basic auth header
```
Authorization: Basic base64(email:api-token)
```

### API token
API tokens are created at `atlassian.com` (not in the Confluence UI).

## Endpoints

### Pages
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/rest/api/content/:id` | Fetches a page |
| GET | `/rest/api/content` | Lists pages (with filters) |
| POST | `/rest/api/content` | Creates a page |
| PUT | `/rest/api/content/:id` | Updates a page |
| DELETE | `/rest/api/content/:id` | Deletes a page |
| GET | `/rest/api/content/:id/child/page` | Lists subpages |
| GET | `/rest/api/content/:id/history` | Version history |

### Spaces
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/rest/api/space/:key` | Fetches a space |
| GET | `/rest/api/space` | Lists spaces |
| POST | `/rest/api/space` | Creates a space |

### Comments
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/rest/api/content/:id/child/comment` | Lists comments |
| POST | `/rest/api/content/:id/child/comment` | Creates a comment |
| PUT | `/rest/api/content/:id/child/comment/:commentId` | Updates a comment |

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/rest/api/user` | Fetches a user |
| GET | `/rest/api/user/view` | Lists users |

### Search
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/rest/api/search` | Search |

### Attachments
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/rest/api/content/:id/child/attachment` | Lists attachments |
| POST | `/rest/api/content/:id/child/attachment` | Adds an attachment |
| GET | `/rest/api/content/:id/child/attachment/:attachId` | Fetches an attachment |

### Macro
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/rest/api/content/:id/child/macro` | Lists macros |

## Examples

### Fetching a page
```bash
curl -X GET "https://confluence.example.com/rest/api/content/12345" \
  -H "Authorization: Basic base64(user@example.com:api-token)" \
  -H "Accept: application/json"
```

### Creating a page
```bash
curl -X POST "https://confluence.example.com/rest/api/content" \
  -H "Authorization: Basic base64(user@example.com:api-token)" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "page",
    "title": "New Page",
    "space": {
      "key": "SPACEKEY"
    },
    "body": {
      "storage": {
        "value": "<p>This is a new page.</p>",
        "representation": "storage"
      }
    }
  }'
```

### Python example
```python
import requests
import base64

API_URL = "https://confluence.example.com/rest/api"
EMAIL = "user@example.com"
API_TOKEN = "api-token"

# Basic auth header
auth = requests.auth.HTTPBasicAuth(EMAIL, API_TOKEN)
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Fetch a page
response = requests.get(f"{API_URL}/content/12345", auth=auth, headers=headers)
print(response.json())

# Create a page
data = {
    "type": "page",
    "title": "New Page",
    "space": {"key": "SPACEKEY"},
    "body": {
        "storage": {
            "value": "<p>Content of the page</p>",
            "representation": "storage"
        }
    }
}
response = requests.post(f"{API_URL}/content", json=data, auth=auth, headers=headers)
print(response.json())

# Search
params = {"cql": "title ~ 'search term'"}
response = requests.get(f"{API_URL}/search", params=params, auth=auth, headers=headers)
print(response.json())
```

### JavaScript example
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

// Fetch a page
axios.get(`${API_URL}/content/12345`, { auth, headers })
    .then(response => console.log(response.data))
    .catch(error => console.error(error));

// Create a page
const data = {
    type: 'page',
    title: 'New Page',
    space: { key: 'SPACEKEY' },
    body: {
        storage: {
            value: '<p>Content</p>',
            representation: 'storage'
        }
    }
};

axios.post(`${API_URL}/content`, data, { auth, headers })
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
```

## Rate limits
- Default: 200 requests per 5 minutes per user
- Confluence Cloud: 100 requests per second
- Response headers:
  - `X-AUTH-_RATE-LIMIT-REMAINING`: remaining requests
  - `X-AUTH-_RATE-LIMIT-RESET`: reset time

## Webhooks
Confluence supports webhooks:
- `page.created`: a page was created
- `page.updated`: a page was updated
- `page.deleted`: a page was deleted
- `comment.created`: a comment was created
- `space.created`: a space was created

Configuration: `POST /rest/webhooks/1.0/webhook`

## SDKs and client libraries
- **JavaScript**: `@atlassian/confluence-api` (official)
- **Python**: `atlassian-python-api` (community)
- **Java**: `atlassian-java-client` (official)
- **Go**: `go-confluence` (community)
- **PHP**: `atlassian-php-sdk` (community)

Install:
```bash
# npm
npm install @atlassian/confluence-api

# pip
pip install atlassian-python-api

# Go
go get github.com/ctessier/go-confluence
```

## See also
- [menu.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
