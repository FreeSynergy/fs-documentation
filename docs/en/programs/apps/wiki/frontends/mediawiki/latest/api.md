# MediaWiki - API Documentation

## Overview
MediaWiki provides a comprehensive REST-based API for accessing all wiki features. The API is the main means of interacting with MediaWiki-based wikis (such as Wikipedia) and supports all CRUD operations.

## Authentication
MediaWiki supports several authentication methods:

- **Clientlogin**: Username and password (for scripts)
- **OAuth**: OAuth 1.0a for third-party apps
- **Bot passwords**: Special passwords for bots
- **Session cookies**: Authentication via an existing session
- **PATRICIA**: Token-based authentication

### Login Flow
1. Call `action=query&meta=tokens&type=login`
2. Call `action=clientlogin` with the token and credentials

## Endpoints

### Main API Endpoint
```
GET/POST /w/api.php
```

### Pages
| Action | Description |
|--------|-------------|
| `query` | Retrieve, list, search pages |
| `edit` | Create/edit page |
| `delete` | Delete page |
| `move` | Move page |
| `protect` | Protect page |
| `rollback` | Revert changes |
| `purge` | Clear cache |
| `history` | Retrieve version history |

### Users
| Action | Description |
|--------|-------------|
| `query&list=users` | List users |
| `query&list=userprop` | User properties |
| `userrights` | Change user rights |
| `block` | Block user |
| `unblock` | Unblock user |

### Authentication
| Action | Description |
|--------|-------------|
| `login` | Login (deprecated) |
| `clientlogin` | Modern login |
| `logout` | Logout |
| `createaccount` | Create account |

### Search
| Action | Description |
|--------|-------------|
| `query&list=search` | Full-text search |
| `opensearch` | OpenSearch API |

### Uploads
| Action | Description |
|--------|-------------|
| `upload` | Upload file |
| `query&list=images` | List files |
| `deletefile` | Delete file |

### Meta
| Action | Description |
|--------|-------------|
| `query&meta=siteinfo` | Site information |
| `query&meta=tokens` | CSRF token |
| `query&meta=globalinfo` | Global information |

### Example Parameters
```
action=query&prop=info&titles=Hauptseite&format=json
```

## Examples

### Retrieve page
```bash
curl "https://wiki.example.com/w/api.php?action=query&prop=info&titles=Hauptseite&format=json"
```

### Edit page (Python)
```python
import requests

API_URL = "https://wiki.example.com/w/api.php"

# 1. Get login token
session = requests.Session()
response = session.get(f"{API_URL}?action=query&meta=tokens&type=login&format=json")
login_token = response.json()['query']['tokens']['logintoken']

# 2. Login
response = session.post(f"{API_URL}?action=clientlogin&format=json", data={
    'logintoken': login_token,
    'username': 'Benutzer',
    'password': 'Passwort'
})

# 3. Edit page
response = session.get(f"{API_URL}?action=query&meta=tokens&format=json")
edit_token = response.json()['query']['tokens']['edittoken']

response = session.post(f"{API_URL}?action=edit&format=json", data={
    'title': 'Hauptseite',
    'token': edit_token,
    'text': '# Neue Seite\n\nInhalt',
    'summary': 'Bearbeitung'
})
```

### GraphQL (MediaWiki 1.39+)
```bash
curl -X POST "https://wiki.example.com/graphql" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "{ pages(namespace: 0, prefix: \"Haupt\") { title content } }"
  }'
```

### JavaScript Example
```javascript
const API_URL = "https://wiki.example.com/w/api.php";

async function getPages() {
    const response = await fetch(`${API_URL}?action=query&list=allpages&format=json`);
    const data = await response.json();
    return data.query.allpages;
}

async function editPage(title, content, summary) {
    // Login token
    let response = await fetch(`${API_URL}?action=query&meta=tokens&type=edit&format=json`);
    let data = await response.json();
    const editToken = data.query.tokens.edittoken;
    
    // Edit page
    response = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({
            action: 'edit',
            title: title,
            text: content,
            token: editToken,
            summary: summary,
            format: 'json'
        })
    });
    
    return await response.json();
}
```

## Rate Limits
- Standard: 50 requests per second per IP
- Authenticated users: 100 requests per second
- Bots: Configurable (default: 10/sec)
- Parameters in `DefaultSettings.php`:
  - `$wgRateLimit`
  - `$wgRateLimitLog`
  - `$wgUserRateLimit`

## Webhooks
MediaWiki supports webhooks via the "Echo" extension:
- `edit`: Page edited
- `new`: New page created
- `move`: Page moved
- `delete`: Page deleted
- `protect`: Protection changed

Configuration via `$wgExtensionFunctions` or webhook extensions.

## SDKs and Client Libraries
- **JavaScript**: `mediawiki` (official)
- **Python**: `mwclient`, `wikipedia-api`, `python-mwclient`
- **PHP**: `mediawiki-api-client`
- **Java**: `mwapi`
- **Ruby**: `mediawiki-gems`
- **Go**: `go-mediawiki`

## See also
- [menu.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
