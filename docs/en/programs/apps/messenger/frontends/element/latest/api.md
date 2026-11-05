# Element - API documentation

## Overview
Element (the Matrix client) offers a full REST API through the Matrix specification for access to messages, rooms, users and media. The API allows full integration into the Matrix network.

## Authentication
Element uses OAuth2 and Matrix authentication:

- **Access token**: direct authentication
- **OAuth2**: for third-party apps
- **Login flow**: password, token, recaptcha, SSO

### Headers
```
Authorization: Bearer <access-token>
Content-Type: application/json
```

## Endpoints (Matrix API)

### Rooms
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/_matrix/client/v3/joined_rooms` | Joined rooms |
| GET | `/_matrix/client/v3/rooms/:room_id/state` | Room state |
| POST | `/_matrix/client/v3/rooms/:room_id/join` | Join a room |
| POST | `/_matrix/client/v3/rooms/:room_id/leave` | Leave a room |
| POST | `/_matrix/client/v3/rooms/:room_id/ban` | Ban a user |
| POST | `/_matrix/client/v3/rooms/:room_id/kick` | Kick a user |
| POST | `/_matrix/client/v3/rooms/:room_id/create` | Create a room |

### Messages
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/_matrix/client/v3/rooms/:room_id/messages` | Messages (with a filter) |
| POST | `/_matrix/client/v3/rooms/:room_id/send` | Send a message |
| PUT | `/_matrix/client/v3/rooms/:room_id/send/:msgtype/:txn_id` | Idempotent send |
| POST | `/_matrix/client/v3/rooms/:room_id/redact` | Redact a message |
| GET | `/_matrix/client/v3/rooms/:room_id/event/:event_id` | Fetch an event |

### Media
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/_matrix/media/v3/download/:server_name/:media_id` | Download media |
| POST | `/_matrix/media/v3/upload` | Upload media |
| GET | `/_matrix/media/v3/thumbnail/:server_name/:media_id` | Thumbnail |

### Users
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/_matrix/client/v3/account/whoami` | Current user |
| GET | `/_matrix/client/v3/profile/:user_id` | User profile |
| PUT | `/_matrix/client/v3/profile/:user_id/displayname` | Set the display name |
| PUT | `/_matrix/client/v3/profile/:user_id/avatar_url` | Set the avatar |

### Sync
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/_matrix/client/v3/sync` | Synchronise (long polling) |
| GET | `/_matrix/client/v3/sync?filter=:filter_id` | With a filter |

### Typing
| Method | Endpoint | Description |
|---------|----------|--------------|
| PUT | `/_matrix/client/v3/rooms/:room_id/typing/:user_id` | Typing status |

### Read receipts
| Method | Endpoint | Description |
|---------|----------|--------------|
| POST | `/_matrix/client/v3/rooms/:room_id/read_markers` | Read receipt |

### Push notifications
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `/_matrix/client/v3/pushers` | List pushers |
| POST | `/_matrix/client/v3/pushers/add` | Add a pusher |
| DELETE | `/_matrix/client/v3/pushers/:pusher_id` | Delete a pusher |

### Account data
| Method | Endpoint | Description |
|---------|----------|--------------|
| PUT | `/_matrix/client/v3/user/:user_id/account_data/:event_type` | Set account data |
| GET | `/_matrix/client/v3/user/:user_id/account_data/:event_type` | Get account data |

## Examples

### Sending a message
```bash
curl -X PUT "https://matrix.example.com/_matrix/client/v3/rooms/!roomid/send/m.room.message/m12345678901234" \
  -H "Authorization: Bearer <access-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "msgtype": "m.text",
    "body": "Hello from the Element API!"
  }'
```

### Creating a room
```bash
curl -X POST "https://matrix.example.com/_matrix/client/v3/createRoom" \
  -H "Authorization: Bearer <access-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My room",
    "topic": "Topic of this room",
    "preset": "public_chat",
    "visibility": "public"
  }'
```

### Python example
```python
import requests
import json

MATRIX_URL = "https://matrix.example.com"
ACCESS_TOKEN = "your-access-token"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# send a message
room_id = "!roomid:example.com"
txn_id = "m12345678901234"
data = {
    "msgtype": "m.text",
    "body": "Hello, this is a test message!"
}
response = requests.put(
    f"{MATRIX_URL}/_matrix/client/v3/rooms/{room_id}/send/m.room.message/{txn_id}",
    json=data,
    headers=headers
)
print(response.json())

# list rooms
response = requests.get(
    f"{MATRIX_URL}/_matrix/client/v3/joined_rooms",
    headers=headers
)
print(response.json())

# user profile
user_id = "@user:example.com"
response = requests.get(
    f"{MATRIX_URL}/_matrix/client/v3/profile/{user_id}",
    headers=headers
)
print(response.json())
```

### Node.js example
```javascript
const axios = require('axios');

const MATRIX_URL = 'https://matrix.example.com';
const ACCESS_TOKEN = 'your-access-token';

const headers = {
    'Authorization': `Bearer ${ACCESS_TOKEN}`,
    'Content-Type': 'application/json'
};

// send a message
const room_id = '!roomid:example.com';
const txn_id = 'm12345678901234';
const data = {
    msgtype: 'm.text',
    body: 'Hello from Node.js!'
};

axios.put(
    `${MATRIX_URL}/_matrix/client/v3/rooms/${room_id}/send/m.room.message/${txn_id}`,
    data,
    { headers }
)
    .then(response => console.log(response.data))
    .catch(error => console.error(error));

// room information
axios.get(
    `${MATRIX_URL}/_matrix/client/v3/rooms/${room_id}/state`,
    { headers }
)
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
```

### WebSocket sync (long polling)
```javascript
let since = null;

async function sync() {
    let url = `${MATRIX_URL}/_matrix/client/v3/sync`;
    if (since) {
        url += `?since=${since}`;
    }

    const response = await axios.get(url, { headers });

    // process updates
    console.log('Rooms:', response.data.rooms);
    console.log('Notifications:', response.data.next_batch);

    since = response.data.next_batch;

    // next sync
    setTimeout(sync, 1000);
}

sync();
```

## Rate limits
- Standard: 1000 requests per day per user
- Synapse server: configurable in `synapse.cfg`
- Response headers:
  - `Retry-After`: wait time on a limit
  - `X-Rate-Limit-Limit`: maximum requests
  - `X-Rate-Limit-Remaining`: requests left

## Webhooks
Element/Matrix supports no direct webhooks, but:
- **Push notifications**: via a push gateway
- **Bot clients**: regular sync polling
- **Federation webhooks**: for server admins

## SDKs and client libraries
- **JavaScript/TypeScript**: `matrix-js-sdk` (official)
- **Python**: `matrix-client`, `python-sdk`
- **Java**: `matrix-java-sdk`
- **Go**: `go-matrix-client`
- **C#**: `SimpleMatrixNet`
- **Rust**: `ruma`, `matrix-sdk`

Installing:
```bash
# npm
npm install matrix-js-sdk

# pip
pip install matrix-client

# Go
go get github.com/matrix-org/gomatrix
```

## See also
- [menus.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [layout.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
