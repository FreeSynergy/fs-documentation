# MediaWiki - API Dokumentation

## Übersicht
MediaWiki bietet eine umfassende REST-basierte API für den Zugriff auf alle Wiki-Funktionen. Die API ist das Hauptmedium für Interaktion mit MediaWiki-basierten Wikis (wie Wikipedia) und unterstützt alle CRUD-Operationen.

## Authentifizierung
MediaWiki unterstützt mehrere Authentifizierungsmethoden:

- **Clientlogin**: Benutzername und Passwort (für Scripte)
- **OAuth**: OAuth 1.0a für third-party Apps
- **Bot passwords**: Spezielle Passwörter für Bots
- **Session cookies**: Authentifizierung über bestehende Session
- **PATRICIA**: Token-basierte Authentifizierung

### Login Flow
1. Rufe `action=query&meta=tokens&type=login` ab
2. Rufe `action=clientlogin` mit Token und Anmeldedaten auf

## Endpunkte

### Main API Endpoint
```
GET/POST /w/api.php
```

### Pages (Seiten)
| Aktion | Beschreibung |
|--------|--------------|
| `query` | Seite abrufen, listen, Suchen |
| `edit` | Seite erstellen/bearbeiten |
| `delete` | Seite löschen |
| `move` | Seite verschieben |
| `protect` | Seite schützen |
| `rollback` | Änderungen zurücksetzen |
| `purge` | Cache leeren |
| `history` | Versionshistorie abrufen |

### Users (Benutzer)
| Aktion | Beschreibung |
|--------|--------------|
| `query&list=users` | Benutzer listen |
| `query&list=userprop` | Benutzereigenschaften |
| `userrights` | Benutzerrechte ändern |
| `block` | Benutzer blockieren |
| `unblock` | Benutzer entblocken |

### Authentication
| Aktion | Beschreibung |
|--------|--------------|
| `login` | Login (veraltet) |
| `clientlogin` | Moderner Login |
| `logout` | Logout |
| `createaccount` | Account erstellen |

### Search
| Aktion | Beschreibung |
|--------|--------------|
| `query&list=search` | Volltextsuche |
| `opensearch` | OpenSearch API |

### Uploads
| Aktion | Beschreibung |
|--------|--------------|
| `upload` | Datei hochladen |
| `query&list=images` | Dateien listen |
| `deletefile` | Datei löschen |

### Meta
| Aktion | Beschreibung |
|--------|--------------|
| `query&meta=siteinfo` | Site-Informationen |
| `query&meta=tokens` | CSRF-Token |
| `query&meta=globalinfo` | Globale Informationen |

### Beispiel Parameter
```
action=query&prop=info&titles=Hauptseite&format=json
```

## Beispiele

### Seite abrufen
```bash
curl "https://wiki.example.com/w/api.php?action=query&prop=info&titles=Hauptseite&format=json"
```

### Seite bearbeiten (Python)
```python
import requests

API_URL = "https://wiki.example.com/w/api.php"

# 1. Login Token holen
session = requests.Session()
response = session.get(f"{API_URL}?action=query&meta=tokens&type=login&format=json")
login_token = response.json()['query']['tokens']['logintoken']

# 2. Login
response = session.post(f"{API_URL}?action=clientlogin&format=json", data={
    'logintoken': login_token,
    'username': 'Benutzer',
    'password': 'Passwort'
})

# 3. Seite bearbeiten
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
- Standard: 50 Anfragen pro Sekunde pro IP
- Authentifizierte Nutzer: 100 Anfragen pro Sekunde
- Bots: Konfigurierbar (Standard: 10/sec)
- Parameter in `DefaultSettings.php`:
  - `$wgRateLimit`
  - `$wgRateLimitLog`
  - `$wgUserRateLimit`

## Webhooks
MediaWiki unterstützt Webhooks über Extension "Echo":
- `edit`: Seite bearbeitet
- `new`: Neue Seite erstellt
- `move`: Seite verschoben
- `delete`: Seite gelöscht
- `protect`: Schutz geändert

Konfiguration über `$wgExtensionFunctions` oder Webhook-Extensions.

## SDKs und Client-Bibliotheken
- **JavaScript**: `mediawiki` (offiziell)
- **Python**: `mwclient`, `wikipedia-api`, `python-mwclient`
- **PHP**: `mediawiki-api-client`
- **Java**: `mwapi`
- **Ruby**: `mediawiki-gems`
- **Go**: `go-mediawiki`

## Siehe auch
- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
