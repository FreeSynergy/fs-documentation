# Telegram - API Dokumentation

## Übersicht
Telegram bietet eine vollständige REST API für den Zugriff auf alle Chat-Funktionen. Die API ermöglicht das Senden und Empfangen von Nachrichten, Verwalten von Chats, Bots und Medien.

## Authentifizierung
Telegram nutzt Bot Token und API Keys:

- **Bot Token**: Für Bots (ohne OAuth2)
- **User Auth**: Für User-Bots (Telegram Passport)

### Header
```
Content-Type: application/json
```

### URL Format
```
https://api.telegram.org/bot<TOKEN>/<METHOD>
```

## Endpunkte

### Messages (Nachrichten)
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `getUpdates` | Empfangene Updates |
| POST | `sendMessage` | Nachricht senden |
| POST | `forwardMessage` | Nachricht weiterleiten |
| POST | `copyMessage` | Nachricht kopieren |
| POST | `editMessageText` | Nachricht bearbeiten |
| POST | `deleteMessage` | Nachricht löschen |

### Chats
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `getChat` | Chat Details |
| GET | `getChatAdministrators` | Admins |
| GET | `getChatMembersCount` | Mitgliederanzahl |
| POST | `kickChatMember` | Member kicken |
| POST | `unbanChatMember` | Member entblocken |
| POST | `restrictChatMember` | Member einschränken |
| POST | `setChatTitle` | Titel ändern |
| POST | `setChatDescription` | Beschreibung |
| POST | `setChatPhoto` | Foto ändern |
| POST | `deleteChatPhoto` | Foto löschen |

### Bots
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `getMe` | Bot Details |
| POST | `setWebhook` | Webhook setzen |
| POST | `deleteWebhook` | Webhook löschen |
| GET | `getWebhookInfo` | Webhook Info |
| POST | `answerInlineQuery` | Inline Query |
| POST | `setMyCommands` | Commands |
| GET | `getMyCommands` | Commands abrufen |

### Medien
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| POST | `sendPhoto` | Foto senden |
| POST | `sendAudio` | Audio senden |
| POST | `sendDocument` | Dokument senden |
| POST | `sendVideo` | Video senden |
| POST | `sendVoice` | Sprachnachricht |
| POST | `sendMediaGroup` | Medien-Gruppe |
| GET | `getFile` | Datei abrufen |

### Users
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `getChatMember` | Member Info |
| GET | `getChatMemberCount` | Mitgliederanzahl |

### Inline Mode
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| GET | `answerInlineQuery` | Inline Query |
| POST | `sendInvoice` | Rechnung |

### Payments
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| POST | `sendInvoice` | Rechnung |
| POST | `answerShippingQuery` | Versand |
| POST | `answerPreCheckoutQuery` | Vorbereitung |

### Stickers
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| POST | `sendSticker` | Sticker |
| GET | `getStickerSet` | Sticker Set |
| POST | `createNewStickerSet` | Neues Set |
| POST | `addStickerToSet` | Sticker hinzufügen |

### Games
| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| POST | `sendGame` | Spiel |
| POST | `setGameScore` | Score |
| POST | `getGameHighScores` | High Scores |

## Beispiele

### Nachricht senden
```bash
curl -X POST "https://api.telegram.org/bot<TOKEN>/sendMessage" \
  -H "Content-Type: application/json" \
  -d '{
    "chat_id": 12345,
    "text": "Hallo von Telegram API!",
    "parse_mode": "Markdown"
  }'
```

### Nachricht mit Keyboard
```bash
curl -X POST "https://api.telegram.org/bot<TOKEN>/sendMessage" \
  -H "Content-Type: application/json" \
  -d '{
    "chat_id": 12345,
    "text": "Wähle eine Option:",
    "reply_markup": {
      "keyboard": [
        [{"text": "Option 1"}, {"text": "Option 2"}],
        [{"text": "Option 3"}]
      ],
      "one_time_keyboard": true
    }
  }'
```

### Python Example
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

# Nachricht senden
result = send_message(12345, "Hallo, dies ist eine Test-Nachricht!")
print(result)

# Updates abrufen
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

# Datei herunterladen
def get_file(file_id):
    url = f"{TELEGRAM_API}{BOT_TOKEN}/getFile"
    params = {"file_id": file_id}
    response = requests.get(url, params=params)
    return response.json()

file_info = get_file("FILE_ID")
print(file_info)
```

### Node.js Example
```javascript
const axios = require('axios');

const BOT_TOKEN = 'your-bot-token';

// Nachricht senden
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

sendMessage(12345, 'Hallo von Node.js!')
    .then(console.log)
    .catch(console.error);

// Updates abrufen
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

### Webhook einrichten
```bash
curl -X POST "https://api.telegram.org/bot<TOKEN>/setWebhook" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://mein-server.com/webhook"
  }'
```

## Rate Limits
- Standard: 30 Nachrichten pro Sekunde pro Bot
- Nachrichten an Gruppen: 20 pro Minute
- Antwort-Header:
  - `Retry-After`: Wartezeit bei Rate Limit

## Webhooks
Telegram unterstützt Webhooks:
- `message`: Neue Nachricht
- `edited_message`: Nachricht bearbeitet
- `channel_post`: Kanal-Post
- `callback_query`: Button Klick
- `inline_query`: Inline Query
- `chosen_inline_result`: Ergebnis Auswahl

Konfiguration:
```bash
POST /setWebhook
```

## SDKs und Client-Bibliotheken
- **JavaScript**: `telegraf` (offiziell empfohlen), `node-telegram-bot-api`
- **Python**: `python-telegram-bot` (offiziell), `pyTelegramBotAPI`
- **Java**: `TelegramBots`
- **Go**: `telegram-bot-api`
- **PHP**: `TelegramBot`

Installieren:
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

## Siehe auch
- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
