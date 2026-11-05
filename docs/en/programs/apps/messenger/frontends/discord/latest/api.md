# Discord - API documentation

## Overview
Discord offers a REST API via the Discord API for access to servers, channels, messages, users and bots. The API allows full integration into Discord servers and bot development.

## Authentication
Discord uses OAuth2 and bot tokens:

- **Bot token**: for bots (without OAuth2)
- **OAuth2 access token**: for user apps
- **Bearer token**: for application commands

### Headers
```
Authorization: Bot <bot-token>
# or
Authorization: Bearer <access-token>
Content-Type: application/json
```

## Endpoints

### Guilds (servers)
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/guilds/:guild_id` | Server details |
| GET | `/users/@me/guilds` | The user's servers |
| PATCH | `/guilds/:guild_id` | Update a server |
| DELETE | `/guilds/:guild_id` | Delete a server |
| GET | `/guilds/:guild_id/members` | Server members |
| POST | `/guilds/:guild_id/members/:user_id` | Add a member |

### Channels
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/channels/:channel_id` | Channel details |
| POST | `/guilds/:guild_id/channels` | Create a channel |
| PATCH | `/channels/:channel_id` | Update a channel |
| DELETE | `/channels/:channel_id` | Delete a channel |
| GET | `/channels/:channel_id/messages` | Messages |

### Messages
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/channels/:channel_id/messages/:message_id` | Message |
| POST | `/channels/:channel_id/messages` | Send a message |
| PATCH | `/channels/:channel_id/messages/:message_id` | Edit a message |
| DELETE | `/channels/:channel_id/messages/:message_id` | Delete a message |
| POST | `/channels/:channel_id/messages/:message_id/reactions` | Add a reaction |
| DELETE | `/channels/:channel_id/messages/:message_id/reactions/:emoji` | Remove a reaction |

### Users
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/users/:user_id` | User details |
| GET | `/users/@me` | Current user |
| PATCH | `/users/@me` | Update the user |
| GET | `/users/@me/guilds/:guild_id/member` | Server member info |

### Roles
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/guilds/:guild_id/roles` | Roles |
| POST | `/guilds/:guild_id/roles` | Create a role |
| PATCH | `/guilds/:guild_id/roles/:role_id` | Update a role |
| DELETE | `/guilds/:guild_id/roles/:role_id` | Delete a role |

### Bots (commands)
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/applications/:application_id/commands` | Global commands |
| POST | `/applications/:application_id/commands` | Create a command |
| PUT | `/applications/:application_id/commands/:command_id` | Update a command |
| DELETE | `/applications/:application_id/commands/:command_id` | Delete a command |
| GET | `/applications/:application_id/guilds/:guild_id/commands` | Guild commands |

### Webhooks
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/channels/:channel_id/webhooks` | Webhooks |
| POST | `/channels/:channel_id/webhooks` | Create a webhook |
| POST | `/webhooks/:webhook_id/:token` | Webhook message |
| GET | `/webhooks/:webhook_id` | Webhook details |

### Voice
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/guilds/:guild_id/voice` | Voice status |
| PATCH | `/channels/:channel_id/users/:user_id` | Voice move |

## Examples

### Sending a message
```bash
curl -X POST "https://discord.com/api/v10/channels/12345/messages" \
  -H "Authorization: Bot YOUR_BOT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Hello from the Discord API!",
    "tts": false
  }'
```

### Creating a server
```bash
curl -X POST "https://discord.com/api/v10/guilds" \
  -H "Authorization: Bot YOUR_BOT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My server",
    "region": "eu-central",
    "icon": "base64-icon-data"
  }'
```

### Python example
```python
import requests
import json

DISCORD_API = "https://discord.com/api/v10"
BOT_TOKEN = "your-bot-token"

headers = {
    "Authorization": f"Bot {BOT_TOKEN}",
    "Content-Type": "application/json"
}

# send a message
channel_id = "12345"
data = {
    "content": "Hello, this is a test message!",
    "tts": False
}
response = requests.post(
    f"{DISCORD_API}/channels/{channel_id}/messages",
    json=data,
    headers=headers
)
print(response.json())

# list server members
guild_id = "67890"
response = requests.get(
    f"{DISCORD_API}/guilds/{guild_id}/members",
    headers=headers
)
print(response.json())

# user profile
user_id = "11111"
response = requests.get(
    f"{DISCORD_API}/users/{user_id}",
    headers=headers
)
print(response.json())
```

### Node.js example
```javascript
const axios = require('axios');

const DISCORD_API = 'https://discord.com/api/v10';
const BOT_TOKEN = 'your-bot-token';

const headers = {
    'Authorization': `Bot ${BOT_TOKEN}`,
    'Content-Type': 'application/json'
};

// send a message
const channel_id = '12345';
const data = {
    content: 'Hello from Node.js!',
    tts: false
};

axios.post(
    `${DISCORD_API}/channels/${channel_id}/messages`,
    data,
    { headers }
)
    .then(response => console.log(response.data))
    .catch(error => console.error(error));

// create a server
const guildData = {
    name: 'My server',
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

### Sending via a webhook
```bash
curl -X POST "https://discord.com/api/v10/webhooks/WEBHOOK_ID/WEBHOOK_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Hello from a webhook!",
    "username": "Webhook Bot",
    "avatar_url": "https://example.com/avatar.png"
  }'
```

## Rate limits
- Standard: 50 requests per second per bot
- Global rate limit: 120 requests per second
- On a limit, the retry headers:
  - `X-RateLimit-Limit`: maximum requests
  - `X-RateLimit-Remaining`: requests left
  - `X-RateLimit-Reset`: reset time (Unix timestamp)
  - `Retry-After`: wait time in ms

## Webhooks
Discord supports webhooks:
- **Guild events**: via gateway webhooks
- **Channel webhooks**: per-channel webhooks
- **Interaction webhooks**: for slash commands

Configuration:
1. Create the webhook via the API or the UI
2. Use the webhook URL for messages
3. Webhook URL: `https://discord.com/api/webhooks/{id}/{token}`

## SDKs and client libraries
- **JavaScript/TypeScript**: `discord.js` (officially recommended)
- **Python**: `discord.py` (officially recommended)
- **Java**: `JDA` (Java Discord API)
- **Go**: `discordgo`
- **C#**: `Discord.NET`
- **Rust**: `serenity`

Installing:
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

## See also
- [menu.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
