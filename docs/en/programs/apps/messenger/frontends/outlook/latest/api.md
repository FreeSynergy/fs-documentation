# Outlook - API documentation

## Overview
Outlook offers a comprehensive REST API through Microsoft Graph for access to emails, appointments, contacts, tasks and calendars. The API allows full integration into the Microsoft 365 services.

## Authentication
Outlook uses OAuth2 via the Microsoft identity platform:

- **OAuth2 authorization code flow**: for web and desktop apps
- **Client credentials flow**: for daemon apps
- **On-behalf-of**: for server-to-server communication
- **Integrated Windows authentication**: for intranet applications

### Token header
```
Authorization: Bearer <access-token>
```

## Endpoints

### Mail
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/v1.0/me/messages` | Lists messages |
| GET | `/v1.0/me/messages/:id` | Fetches a message |
| POST | `/v1.0/me/messages` | Creates a draft |
| POST | `/v1.0/me/messages/:id/send` | Sends a message |
| PATCH | `/v1.0/me/messages/:id` | Updates a message |
| DELETE | `/v1.0/me/messages/:id` | Deletes a message |
| POST | `/v1.0/me/sendMail` | Sends a message directly |

### Calendar
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/v1.0/me/calendars` | Lists calendars |
| GET | `/v1.0/me/calendars/:id/events` | Lists appointments |
| POST | `/v1.0/me/calendars/:id/events` | Creates an appointment |
| PATCH | `/v1.0/me/events/:id` | Updates an appointment |
| DELETE | `/v1.0/me/events/:id` | Deletes an appointment |

### Contacts
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/v1.0/me/contacts` | Lists contacts |
| POST | `/v1.0/me/contacts` | Creates a contact |
| PATCH | `/v1.0/me/contacts/:id` | Updates a contact |

### Tasks
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/v1.0/me/tasks` | Lists tasks |
| POST | `/v1.0/me/tasks` | Creates a task |
| PATCH | `/v1.0/me/tasks/:id` | Updates a task |

### Calendar view
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/v1.0/me/calendarview?start=...&end=...` | Appointments in a period |

### Users
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/v1.0/users` | Lists users |
| GET | `/v1.0/users/:id` | Fetches a user |
| GET | `/v1.0/me` | Current user |

### Groups
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/v1.0/groups` | Lists groups |
| POST | `/v1.0/groups` | Creates a group |

## Examples

### Sending an email
```bash
curl -X POST "https://graph.microsoft.com/v1.0/me/sendMail" \
  -H "Authorization: Bearer <access-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "message": {
      "subject": "Test message",
      "body": {
        "contentType": "HTML",
        "content": "<p>Hello,<br>this is a test message.</p>"
      },
      "toRecipients": [
        {
          "emailAddress": {
            "address": "recipient@example.com"
          }
        }
      ]
    },
    "saveToSentItems": "true"
  }'
```

### Fetching appointments
```bash
curl -X GET "https://graph.microsoft.com/v1.0/me/calendarview?start=2024-01-01&end=2024-01-31" \
  -H "Authorization: Bearer <access-token>"
```

### Python example
```python
import requests
import json

GRAPH_URL = "https://graph.microsoft.com/v1.0"
ACCESS_TOKEN = "your-access-token"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# fetch emails
response = requests.get(f"{GRAPH_URL}/me/messages", headers=headers)
print(response.json())

# send an email
data = {
    "message": {
        "subject": "Python test",
        "body": {
            "contentType": "HTML",
            "content": "<p>Hello from Python!</p>"
        },
        "toRecipients": [{
            "emailAddress": {"address": "recipient@example.com"}
        }]
    },
    "saveToSentItems": "true"
}
response = requests.post(f"{GRAPH_URL}/me/sendMail", json=data, headers=headers)
print(response.json())

# appointments in the calendar
params = {
    "start": "2024-01-01T00:00:00",
    "end": "2024-01-31T23:59:59"
}
response = requests.get(f"{GRAPH_URL}/me/calendarview", params=params, headers=headers)
print(response.json())
```

### Node.js example
```javascript
const axios = require('axios');

const GRAPH_URL = 'https://graph.microsoft.com/v1.0';
const ACCESS_TOKEN = 'your-access-token';

const headers = {
    'Authorization': `Bearer ${ACCESS_TOKEN}`,
    'Content-Type': 'application/json'
};

// fetch emails
axios.get(`${GRAPH_URL}/me/messages`, { headers })
    .then(response => console.log(response.data))
    .catch(error => console.error(error));

// create an appointment
const event = {
    subject: 'Meeting',
    body: {
        contentType: 'HTML',
        content: '<p>Meeting description</p>'
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
            address: 'attendee@example.com'
        }
    }]
};

axios.post(`${GRAPH_URL}/me/events`, event, { headers })
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
```

## Rate limits
- Standard: 100,000 requests per day per app
- Burst: 50 requests per second
- Response headers:
  - `X-ResponseLatency`: response time in ms
  - `X-RequestID`: request id for support
  - `RateLimit-Limit`: maximum requests
  - `RateLimit-Remaining`: requests left

## Webhooks
Outlook supports webhooks (change notifications):
- `Messages`: new emails
- `Events`: new appointments
- `Contacts`: new contacts
- `Presence`: presence status

Configuration:
```bash
POST https://graph.microsoft.com/v1.0/subscriptions
```

## SDKs and client libraries
- **JavaScript**: `@microsoft/microsoft-graph-client` (official)
- **Python**: `msgraph-sdk` (official)
- **Java**: `microsoft-graph` (official)
- **C#**: `Microsoft.Graph` (official)
- **Go**: `go-sdk` (official)

Installing:
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

## See also
- [menus.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [layout.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
