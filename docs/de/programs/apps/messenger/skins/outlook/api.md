# Outlook - API Dokumentation

## Übersicht
Outlook bietet eine umfassende REST API über Microsoft Graph für den Zugriff auf E-Mails, Termine, Kontakte, Aufgaben und Kalender. Die API ermöglicht vollständige Integration in Microsoft 365-Dienste.

## Authentifizierung
Outlook nutzt OAuth2 über Microsoft Identity Platform:

- **OAuth2 Authorization Code Flow**: Für Web- und Desktop-Apps
- **Client Credentials Flow**: Für Daemon-Apps
- **On-Behalf-Of**: Für Server-zu-Server Kommunikation
- **Integrated Windows Auth**: Für intranet Anwendungen

### Token Header
```
Authorization: Bearer <access-token>
```

## Endpunkte

### Mail
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/v1.0/me/messages` | Listet Nachrichten |
| GET | `/v1.0/me/messages/:id` | Holt Nachricht |
| POST | `/v1.0/me/messages` | Erstellt Entwurf |
| POST | `/v1.0/me/messages/:id/send` | Sendet Nachricht |
| PATCH | `/v1.0/me/messages/:id` | Aktualisiert Nachricht |
| DELETE | `/v1.0/me/messages/:id` | Löscht Nachricht |
| POST | `/v1.0/me/sendMail` | Sendet Nachricht direkt |

### Kalender
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/v1.0/me/calendars` | Listet Kalender |
| GET | `/v1.0/me/calendars/:id/events` | Listet Termine |
| POST | `/v1.0/me/calendars/:id/events` | Erstellt Termin |
| PATCH | `/v1.0/me/events/:id` | Aktualisiert Termin |
| DELETE | `/v1.0/me/events/:id` | Löscht Termin |

### Kontakte
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/v1.0/me/contacts` | Listet Kontakte |
| POST | `/v1.0/me/contacts` | Erstellt Kontakt |
| PATCH | `/v1.0/me/contacts/:id` | Aktualisiert Kontakt |

### Aufgaben
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/v1.0/me/tasks` | Listet Aufgaben |
| POST | `/v1.0/me/tasks` | Erstellt Aufgabe |
| PATCH | `/v1.0/me/tasks/:id` | Aktualisiert Aufgabe |

### Kalender View
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/v1.0/me/calendarview?start=...&end=...` | Termine im Zeitraum |

### Users
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/v1.0/users` | Listet Benutzer |
| GET | `/v1.0/users/:id` | Holt Benutzer |
| GET | `/v1.0/me` | Aktueller Benutzer |

### Groups
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/v1.0/groups` | Listet Gruppen |
| POST | `/v1.0/groups` | Erstellt Gruppe |

## Beispiele

### E-Mail senden
```bash
curl -X POST "https://graph.microsoft.com/v1.0/me/sendMail" \
  -H "Authorization: Bearer <access-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "message": {
      "subject": "Test Nachricht",
      "body": {
        "contentType": "HTML",
        "content": "<p>Hallo,<br>Dies ist eine Test-Nachricht.</p>"
      },
      "toRecipients": [
        {
          "emailAddress": {
            "address": "empfaenger@example.com"
          }
        }
      ]
    },
    "saveToSentItems": "true"
  }'
```

### Termine abrufen
```bash
curl -X GET "https://graph.microsoft.com/v1.0/me/calendarview?start=2024-01-01&end=2024-01-31" \
  -H "Authorization: Bearer <access-token>"
```

### Python Example
```python
import requests
import json

GRAPH_URL = "https://graph.microsoft.com/v1.0"
ACCESS_TOKEN = "your-access-token"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# E-Mails abrufen
response = requests.get(f"{GRAPH_URL}/me/messages", headers=headers)
print(response.json())

# E-Mail senden
data = {
    "message": {
        "subject": "Python Test",
        "body": {
            "contentType": "HTML",
            "content": "<p>Hallo von Python!</p>"
        },
        "toRecipients": [{
            "emailAddress": {"address": "empfaenger@example.com"}
        }]
    },
    "saveToSentItems": "true"
}
response = requests.post(f"{GRAPH_URL}/me/sendMail", json=data, headers=headers)
print(response.json())

# Termine im Kalender
params = {
    "start": "2024-01-01T00:00:00",
    "end": "2024-01-31T23:59:59"
}
response = requests.get(f"{GRAPH_URL}/me/calendarview", params=params, headers=headers)
print(response.json())
```

### Node.js Example
```javascript
const axios = require('axios');

const GRAPH_URL = 'https://graph.microsoft.com/v1.0';
const ACCESS_TOKEN = 'your-access-token';

const headers = {
    'Authorization': `Bearer ${ACCESS_TOKEN}`,
    'Content-Type': 'application/json'
};

// E-Mails abrufen
axios.get(`${GRAPH_URL}/me/messages`, { headers })
    .then(response => console.log(response.data))
    .catch(error => console.error(error));

// Termin erstellen
const event = {
    subject: 'Meeting',
    body: {
        contentType: 'HTML',
        content: '<p>Meeting Beschreibung</p>'
    },
    start: {
        dateTime: '2024-01-15T10:00:00',
        timeZone: 'W. Europe Standard Time'
    },
    end: {
        dateTime: '2024-01-15T11:00:00',
        timeZone: 'W. Europe Standard Time'
    },
    attendees: [{
        emailAddress: {
            address: 'teilnehmer@example.com'
        }
    }]
};

axios.post(`${GRAPH_URL}/me/events`, event, { headers })
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
```

## Rate Limits
- Standard: 100.000 Anfragen pro Tag pro App
- Burst: 50 Anfragen pro Sekunde
- Antwort-Header:
  - `X-ResponseLatency`: Antwortzeit in ms
  - `X-RequestID`: Request ID für Support
  - `RateLimit-Limit`: Max. Anfragen
  - `RateLimit-Remaining`: Verbleibende Anfragen

## Webhooks
Outlook unterstützt Webhooks (Change Notifications):
- `Messages`: Neue E-Mails
- `Events`: Neue Termine
- `Contacts`: Neue Kontakte
- `Presence`: Anwesenheitsstatus

Konfiguration:
```bash
POST https://graph.microsoft.com/v1.0/subscriptions
```

## SDKs und Client-Bibliotheken
- **JavaScript**: `@microsoft/microsoft-graph-client` (offiziell)
- **Python**: `msgraph-sdk` (offiziell)
- **Java**: `microsoft-graph` (offiziell)
- **C#**: `Microsoft.Graph` (offiziell)
- **Go**: `go-sdk` (offiziell)

Installieren:
```bash
# npm
npm install @microsoft/microsoft-graph-client

# pip
pip install msgraph-sdk

# Maven
<dependency>
    <groupId>com.microsoft.graph</groupId>
    <artifactId>microsoft-graph</artifactId>
    <version>5.52.0</version>
</dependency>
```

## Siehe auch
- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
