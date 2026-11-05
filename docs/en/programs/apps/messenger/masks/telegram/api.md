# Telegram - API documentation

## Overview
Telegram offers a full REST API for access to all chat features. The API allows sending and receiving messages, and managing chats, bots and media.

## Authentication
Telegram uses bot tokens and API keys:

- **Bot token**: for bots (without OAuth2)
- **User auth**: for user bots (Telegram Passport)

### Headers
```
Content-Type: application/json
```

### URL format
```
https://api.telegram.org/bot<TOKEN>/<METHOD>
```

## Endpoints

### Messages
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `getUpdates` | Incoming updates |
| POST | `sendMessage` | Send a message |
| POST | `forwardMessage` | Forward a message |
| POST | `copyMessage` | Copy a message |
| POST | `editMessageText` | Edit a message |
| POST | `deleteMessage` | Delete a message |

### Chats
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `getChat` | Chat details |
| GET | `getChatAdministrators` | Administrators |
| GET | `getChatMembersCount` | Member count |
| POST | `kickChatMember` | Kick a member |
| POST | `unbanChatMember` | Unblock a member |
| POST | `restrictChatMember` | Restrict a member |
| POST | `setChatTitle` | Change the title |
| POST | `setChatDescription` | Description |
| POST | `setChatPhoto` | Change the photo |
| POST | `deleteChatPhoto` | Delete the photo |

### Bots
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `getMe` | Bot details |
| POST | `setWebhook` | Set a webhook |
| POST | `deleteWebhook` | Delete a webhook |
| GET | `getWebhookInfo` | Webhook info |
| POST | `answerInlineQuery` | Inline query |
| POST | `setMyCommands` | Commands |
| GET | `getMyCommands` | Fetch the commands |

### Media
| Method | Endpoint | Description |
|---------|----------|--------------|
| POST | `sendPhoto` | Send a photo |
| POST | `sendAudio` | Send audio |
| POST | `sendDocument` | Send a document |
| POST | `sendVideo` | Send a video |
| POST | `sendVoice` | Voice message |
| POST | `sendMediaGroup` | Media group |
| GET | `getFile` | Fetch a file |

### Users
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `getChatMember` | Member info |
| GET | `getChatMemberCount` | Member count |

### Inline mode
| Method | Endpoint | Description |
|---------|----------|--------------|
| GET | `answerInlineQuery` | Inline query |
| POST | `sendInvoice` | Invoice |

### Payments
| Method | Endpoint | Description |
|---------|----------|--------------|
| POST | `sendInvoice` | Invoice |
| POST | `answerShippingQuery` | Shipping |
| POST | `answerPreCheckoutQuery` | Pre-checkout |

### Stickers
| Method | Endpoint | Description |
|---------|----------|--------------|
| POST | `sendSticker` | Sticker |
| GET | `getStickerSet` | Sticker set |
| POST | `createNewStickerSet` | New set |
| POST | `addStickerToSet` | Add a sticker |

### Games
| Method | Endpoint | Description |
|---------|----------|--------------|
| POST | `sendGame` | Game |
| POST | `setGameScore` | Score |
| POST | `getGameHighScores` | High scores |

## Examples

### Sending a message
```bash
curl -X POST "https://api.telegram.org/bot<TOKEN>/sendMessage" \
  -H "Content-Type: application/json" \
  -d '{
    "chat_id": 12345,
    "text": "Hello from the Telegram API!",
    "parse_mode": "Markdown"
  }'
```

### A message with a keyboard
```bash
curl -X POST "https://api.telegram.org/bot<TOKEN>/sendMessage" \
  -H "Content-Type: application/json" \
  -d '{
    "chat_id": 12345,
    "text": "Choose an option:",
    "reply_markup": {
      "keyboard": [
        [{"text": "Option 1"}, {"text": "Option 2"}],
        [{"text": "Option 3"}]
      ],
      "one_time_keyboard": true
    }
  }'
```

### Python example
```python
import requests
import json

TELEGRAM_API = "https://api.telegram.org/bot"
BOT_TOKEN = "your-bot-token"

def send_message(chat_id, text, parse_mode="Markdown"):
    url = f"{TELEGRAM_API}{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": parse_mode
    }
    response = requests.post(url, json=data)
    return response.json()

# send a message
result = send_message(12345, "Hello, this is a test message!")
print(result)

# fetch updates
def get_updates(offset=None):
    url = f"{TELEGRAM_API}{BOT_TOKEN}/getUpdates"
    params = {}
    if offset:
        params["offset"] = offset
    response = requests.get(url, params=params)
    return response.json()

updates = get_updates()
for update in updates.get("result", []):
    print(update)

# download a file
def get_file(file_id):
    url = f"{TELEGRAM_API}{BOT_TOKEN}/getFile"
    params = {"file_id": file_id}
    response = requests.get(url, params=params)
    return response.json()

file_info = get_file("FILE_ID")
print(file_info)
```

### Node.js example
```javascript
const axios = require('axios');

const BOT_TOKEN = 'your-bot-token';

// send a message
async function sendMessage(chatId, text) {
    const response = await axios.post(
        `https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`,
        {
            chat_id: chatId,
            text: text
        }
    );
    return response.data;
}

sendMessage(12345, 'Hello from Node.js!')
    .then(console.log)
    .catch(console.error);

// fetch updates
async function getUpdates() {
    const response = await axios.get(
        `https://api.telegram.org/bot${BOT_TOKEN}/getUpdates`
    );
    return response.data;
}

getUpdates()
    .then(data => {
        data.result.forEach(update => console.log(update));
    })
    .catch(console.error);
```

### Setting up a webhook
```bash
curl -X POST "https://api.telegram.org/bot<TOKEN>/setWebhook" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://my-server.com/webhook"
  }'
```

## Rate limits
- Standard: 30 messages per second per bot
- Messages to groups: 20 per minute
- Response headers:
  - `Retry-After`: wait time on a rate limit

## Webhooks
Telegram supports webhooks:
- `message`: new message
- `edited_message`: message edited
- `channel_post`: channel post
- `callback_query`: button click
- `inline_query`: inline query
- `chosen_inline_result`: chosen result

Configuration:
```bash
POST /setWebhook
```

## SDKs and client libraries
- **JavaScript**: `telegraf` (officially recommended), `node-telegram-bot-api`
- **Python**: `python-telegram-bot` (official), `pyTelegramBotAPI`
- **Java**: `TelegramBots`
- **Go**: `telegram-bot-api`
- **PHP**: `TelegramBot`

Installing:
```bash
# npm
npm install telegraf

# pip
pip install python-telegram-bot

# Maven
<dependency>
    <groupId>org.telegram</groupId>
    <artifactId>telegrambots</artifactId>
    <version>6.9.0</version>
</dependency>
```

## See also
- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
