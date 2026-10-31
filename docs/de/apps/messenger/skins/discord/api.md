# Discord - API Dokumentation

## Übersicht
Discord bietet eine REST API über die Discord API für den Zugriff auf Server, Kanäle, Nachrichten, Benutzer und Bots. Die API ermöglicht vollständige Integration in Discord-Server und Bot-Entwicklung.

## Authentifizierung
Discord nutzt OAuth2 und Bot Token:

- **Bot Token**: Für Bots (ohne OAuth2)
- **OAuth2 Access Token**: Für User-Apps
- **Bearer Token**: Für Application-Commands

### Header
```
Authorization: Bot <bot-token>
# oder
Authorization: Bearer <access-token>
Content-Type: application/json
```

## Endpunkte

### Server (Guilds)
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/guilds/:guild_id` | Server Details |
| GET | `/users/@me/guilds` | Server des Users |
| PATCH | `/guilds/:guild_id` | Server aktualisieren |
| DELETE | `/guilds/:guild_id` | Server löschen |
| GET | `/guilds/:guild_id/members` | Server Mitglieder |
| POST | `/guilds/:guild_id/members/:user_id` | Member hinzufügen |

### Kanäle
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/channels/:channel_id` | Kanal Details |
| POST | `/guilds/:guild_id/channels` | Kanal erstellen |
| PATCH | `/channels/:channel_id` | Kanal aktualisieren |
| DELETE | `/channels/:channel_id` | Kanal löschen |
| GET | `/channels/:channel_id/messages` | Nachrichten |

### Nachrichten
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/channels/:channel_id/messages/:message_id` | Nachricht |
| POST | `/channels/:channel_id/messages` | Nachricht senden |
| PATCH | `/channels/:channel_id/messages/:message_id` | Nachricht bearbeiten |
| DELETE | `/channels/:channel_id/messages/:message_id` | Nachricht löschen |
| POST | `/channels/:channel_id/messages/:message_id/reactions` | Reaktion hinzufügen |
| DELETE | `/channels/:channel_id/messages/:message_id/reactions/:emoji` | Reaktion entfernen |

### Benutzer
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/users/:user_id` | User Details |
| GET | `/users/@me` | Aktueller User |
| PATCH | `/users/@me` | User aktualisieren |
| GET | `/users/@me/guilds/:guild_id/member` | Server Member Info |

### Rollen (Roles)
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/guilds/:guild_id/roles` | Rollen |
| POST | `/guilds/:guild_id/roles` | Rolle erstellen |
| PATCH | `/guilds/:guild_id/roles/:role_id` | Rolle aktualisieren |
| DELETE | `/guilds/:guild_id/roles/:role_id` | Rolle löschen |

### Bots (Commands)
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/applications/:application_id/commands` | Global Commands |
| POST | `/applications/:application_id/commands` | Command erstellen |
| PUT | `/applications/:application_id/commands/:command_id` | Command aktualisieren |
| DELETE | `/applications/:application_id/commands/:command_id` | Command löschen |
| GET | `/applications/:application_id/guilds/:guild_id/commands` | Guild Commands |

### Webhooks
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/channels/:channel_id/webhooks` | Webhooks |
| POST | `/channels/:channel_id/webhooks` | Webhook erstellen |
| POST | `/webhooks/:webhook_id/:token` | Webhook Nachricht |
| GET | `/webhooks/:webhook_id` | Webhook Details |

### Voice
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `/guilds/:guild_id/voice` | Voice Status |
| PATCH | `/channels/:channel_id/users/:user_id` | Voice Move |

## Beispiele

### Nachricht senden
```bash
curl -X POST "https://discord.com/api/v10/channels/12345/messages" \
  -H "Authorization: Bot YOUR_BOT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Hallo von Discord API!",
    "tts": false
  }'
```

### Server erstellen
```bash
curl -X POST "https://discord.com/api/v10/guilds" \
  -H "Authorization: Bot YOUR_BOT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Mein Server",
    "region": "eu-central",
    "icon": "base64-icon-data"
  }'
```

### Python Example
```python
import requests
import json

DISCORD_API = "https://discord.com/api/v10"
BOT_TOKEN = "your-bot-token"

headers = {
    "Authorization": f"Bot {BOT_TOKEN}",
    "Content-Type": "application/json"
}

# Nachricht senden
channel_id = "12345"
data = {
    "content": "Hallo, dies ist eine Test-Nachricht!",
    "tts": False
}
response = requests.post(
    f"{DISCORD_API}/channels/{channel_id}/messages",
    json=data,
    headers=headers
)
print(response.json())

# Server Mitglieder listen
guild_id = "67890"
response = requests.get(
    f"{DISCORD_API}/guilds/{guild_id}/members",
    headers=headers
)
print(response.json())

# User Profile
user_id = "11111"
response = requests.get(
    f"{DISCORD_API}/users/{user_id}",
    headers=headers
)
print(response.json())
```

### Node.js Example
```javascript
const axios = require('axios');

const DISCORD_API = 'https://discord.com/api/v10';
const BOT_TOKEN = 'your-bot-token';

const headers = {
    'Authorization': `Bot ${BOT_TOKEN}`,
    'Content-Type': 'application/json'
};

// Nachricht senden
const channel_id = '12345';
const data = {
    content: 'Hallo von Node.js!',
    tts: false
};

axios.post(
    `${DISCORD_API}/channels/${channel_id}/messages`,
    data,
    { headers }
)
    .then(response => console.log(response.data))
    .catch(error => console.error(error));

// Server erstellen
const guildData = {
    name: 'Mein Server',
    region: 'eu-central'
};

axios.post(
    `${DISCORD_API}/guilds`,
    guildData,
    { headers }
)
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
```

### Webhook senden
```bash
curl -X POST "https://discord.com/api/v10/webhooks/WEBHOOK_ID/WEBHOOK_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Hallo von Webhook!",
    "username": "Webhook Bot",
    "avatar_url": "https://example.com/avatar.png"
  }'
```

## Rate Limits
- Standard: 50 Anfragen pro Sekunde pro Bot
- Globale Rate Limit: 120 Anfragen pro Sekunde
- Retry-After Header bei Limit:
  - `X-RateLimit-Limit`: Max. Anfragen
  - `X-RateLimit-Remaining`: Verbleibende Anfragen
  - `X-RateLimit-Reset`: Reset Zeit (Unix Timestamp)
  - `Retry-After`: Wartezeit in ms

## Webhooks
Discord unterstützt Webhooks:
- **Guild Events**: Über Gateway Webhooks
- **Channel Webhooks**: Per-Channel Webhooks
- **Interaction Webhooks**: Für Slash Commands

Konfiguration:
1. Erstelle Webhook über API oder UI
2. Verwende Webhook URL für Nachrichten
3. Webhook URL: `https://discord.com/api/webhooks/{id}/{token}`

## SDKs und Client-Bibliotheken
- **JavaScript/TypeScript**: `discord.js` (offiziell empfohlen)
- **Python**: `discord.py` (offiziell empfohlen)
- **Java**: `JDA` (Java Discord API)
- **Go**: `discordgo`
- **C#**: `Discord.NET`
- **Rust**: `serenity`

Installieren:
```bash
# npm
npm install discord.js

# pip
pip install discord.py

# Maven
<dependency>
    <groupId>net.dv8tion</groupId>
    <artifactId>JDA</artifactId>
    <version>5.0.0</version>
</dependency>
```

## Siehe auch
- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
