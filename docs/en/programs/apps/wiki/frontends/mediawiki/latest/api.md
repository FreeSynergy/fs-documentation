# MediaWiki - API Documentation

## Overview
MediaWiki offers an extensive REST-based API for access to all wiki functions.
The API is the main medium for interacting with MediaWiki-based wikis (such as
Wikipedia) and supports all CRUD operations.

## Authentication
MediaWiki supports several authentication methods:

- **Clientlogin**: username and password (for scripts)
- **OAuth**: OAuth 1.0a for third-party apps
- **Bot passwords**: special passwords for bots
- **Session cookies**: authentication through an existing session
- **PATRICIA**: token-based authentication

### Login flow
1. Fetch `action=query&meta=tokens&type=login`
2. Call `action=clientlogin` with the token and the credentials

## Endpoints

### Main API endpoint
```
GET/POST /w/api.php
```

### Pages
| Action | Description |
|--------|-------------|
| `query` | fetch, list and search pages |
| `edit` | create/edit a page |
| `delete` | delete a page |
| `move` | move a page |
| `protect` | protect a page |
| `rollback` | revert changes |
| `purge` | clear the cache |
| `history` | fetch the version history |

### Users
| Action | Description |
|--------|-------------|
| `query&list=users` | list users |
| `query&list=userprop` | user properties |
| `userrights` | change user rights |
| `block` | block a user |
| `unblock` | unblock a user |

### Authentication
| Action | Description |
|--------|-------------|
| `login` | login (deprecated) |
| `clientlogin` | modern login |
| `logout` | logout |
| `createaccount` | create an account |

### Search
| Action | Description |
|--------|-------------|
| `query&list=search` | full-text search |
| `opensearch` | OpenSearch API |

### Uploads
| Action | Description |
|--------|-------------|
| `upload` | upload a file |
| `query&list=images` | list files |
| `deletefile` | delete a file |

### Meta
| Action | Description |
|--------|-------------|
| `query&meta=siteinfo` | site information |
| `query&meta=tokens` | CSRF token |
| `query&meta=globalinfo` | global information |

### Example parameters
```
action=query&prop=info&titles=Main_Page&format=json
```

## Examples

### Fetching a page
```bash
curl "https://wiki.example.com/w/api.php?action=query&prop=info&titles=Main_Page&format=json"
```

### Editing a page (Python)
```python
import requests

API_URL = "https://wiki.example.com/w/api.php"

# 1. Get the login token
session = requests.Session()
response = session.get(f"{API_URL}?action=query&meta=tokens&type=login&format=json")
login_token = response.json()['query']['tokens']['logintoken']

# 2. Log in
response = session.post(f"{API_URL}?action=clientlogin&format=json", data={
    'logintoken': login_token,
    'username': 'User',
    'password': 'Password'
})

# 3. Edit the page
response = session.get(f"{API_URL}?action=query&meta=tokens&format=json")
edit_token = response.json()['query']['tokens']['edittoken']

response = session.post(f"{API_URL}?action=edit&format=json", data={
    'title': 'Main Page',
    'token': edit_token,
    'text': '# New Page\n\nContent',
    'summary': 'Edit'
})
```

### GraphQL (MediaWiki 1.39+)
```bash
curl -X POST "https://wiki.example.com/graphql" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "{ pages(namespace: 0, prefix: \"Main\") { title content } }"
  }'
```

### JavaScript example
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

## Rate limits
- Default: 50 requests per second per IP
- Authenticated users: 100 requests per second
- Bots: configurable (default: 10/sec)
- Parameters in `DefaultSettings.php`:
  - `$wgRateLimit`
  - `$wgRateLimitLog`
  - `$wgUserRateLimit`

## Webhooks
MediaWiki supports webhooks through the "Echo" extension:
- `edit`: a page was edited
- `new`: a new page was created
- `move`: a page was moved
- `delete`: a page was deleted
- `protect`: the protection changed

Configuration through `$wgExtensionFunctions` or webhook extensions.

## SDKs and client libraries
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
