# XWiki - API Documentation

## Overview
XWiki offers an extensive REST API and a proprietary Java-based API for access
to all wiki functions. It also supports a JavaScript client and WebSocket-based
real-time features.

## Authentication
XWiki supports the following authentication methods:

- **Basic authentication**: username and password
- **XWiki authentication token**: token-based authentication
- **SSO**: SAML, LDAP, OAuth2, OpenID Connect
- **Anonymous access**: for public content

### Auth header (basic)
```
Authorization: Basic base64(username:password)
X-XWiki-Auth-token: your-auth-token
```

## Endpoints

### Pages
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/rest/wikis/{wiki}/spaces/{space}/pages/{page}` | Fetches a page |
| GET | `/rest/wikis/{wiki}/spaces/{space}/pages` | Lists the pages in a space |
| POST | `/rest/wikis/{wiki}/spaces/{space}/pages` | Creates a new page |
| PUT | `/rest/wikis/{wiki}/spaces/{space}/pages/{page}` | Updates a page |
| DELETE | `/rest/wikis/{wiki}/spaces/{space}/pages/{page}` | Deletes a page |
| GET | `/rest/wikis/{wiki}/spaces/{space}/pages/{page}/content` | Fetches the page content |
| GET | `/rest/wikis/{wiki}/spaces/{space}/pages/{page}/versions` | Lists the versions |

### Documents
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/rest/documents/{documentReference}` | Fetches a document |
| POST | `/rest/documents` | Creates/updates a document |

### Objects
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/rest/objects/{documentReference}` | Lists the objects |
| POST | `/rest/objects/{documentReference}` | Creates an object |
| PUT | `/rest/objects/{objectReference}` | Updates an object |
| DELETE | `/rest/objects/{objectReference}` | Deletes an object |

### Classes
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/rest/classes/{classReference}` | Fetches a class |
| GET | `/rest/classes/{classReference}/properties` | Lists the class properties |

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/rest/users` | Lists users |
| GET | `/rest/users/{username}` | Fetches a user |
| POST | `/rest/users` | Creates a user |
| PUT | `/rest/users/{username}` | Updates a user |
| DELETE | `/rest/users/{username}` | Deletes a user |

### Search
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/rest/searches/{searchName}` | Runs a search query |

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/rest/authentication/login` | Log in |
| POST | `/rest/authentication/logout` | Log out |
| GET | `/rest/authentication/currentuser` | the current user |

### JavaScript client
XWiki provides a JavaScript client library under `/jsondoc/` for AJAX
interactions.

## Examples

### Fetching a page
```bash
curl -X GET "https://xwiki.example.com/rest/wikis/xwiki/spaces/Main/pages/WebHome" \
  -H "Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=" \
  -H "Accept: application/json"
```

### Creating a page
```bash
curl -X POST "https://xwiki.example.com/rest/wikis/xwiki/spaces/Main/pages" \
  -H "Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New Page",
    "content": "# Title\n\nContent",
    "parent": "Main.WebHome"
  }'
```

### Java example (XWiki scripting)
```java
// In an XWiki script (Groovy, Python, JavaScript)
import org.xwiki.document.Document;
import org.xwiki.model.reference.DocumentReference;

DocumentReference ref = new DocumentReference("xwiki", "Main", "NewPage");
Document doc = documentAccessor.createNewDocument(ref);
doc.setContent("# Title\n\nContent");
doc.save();
```

### JavaScript client
```javascript
// XWiki JavaScript API
var doc = XWiki.getDocument("Main.NewPage");
doc.setContent("# Title\n\nContent");
doc.save({
    success: function() { console.log("Success!"); },
    error: function(e) { console.error(e); }
});
```

## Rate limits
- Default: 100 requests per minute per user
- Configurable in `xwiki.properties`
- Rate limiting can be enabled per IP or per user

## Webhooks
XWiki supports webhooks through its event system:
- `document.created`: a document was created
- `document.updated`: a document was updated
- `document.deleted`: a document was deleted
- `document.moved`: a document was moved
- `document.restored`: a document was restored

Configuration in `xwiki.cfg` or through extensions.

## SDKs and client libraries
- **Java**: the official SDK (XWiki Platform)
- **JavaScript**: the XWiki JavaScript API
- **Python**: `xwiki-python` (community)
- **PHP**: `xwiki-php-api` (community)
- **C#**: `XWiki.NET` (community)

## See also
- [menu.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
