# FreeSynergy Simple 0.1 — Features

| Feature | Capability (requirements) |
|---------|---------------------------|
| full-screen reading, unread first | `conversation.list`, `message.open` |
| next / previous unread | `message.open` |
| forward, delete with undo, reply | `message.forward`, `message.delete`, `message.reply` |
| new message from the list screen | `message.send` |
| plain text composer, attachments | `message.send`, `attachment.add` |
| drafts | `draft.save` |
| encryption state on every message; unencrypted marked with link to the guide | `message.encryption` (ADR 0018, 0031) |
| recipient picker with live filter | contacts program via its workbench (ADR 0037) |
| **new contact on the fly:** typed text that matches nobody opens a form with the fields needed to reach the person (phone, e-mail, Matrix, Telegram, …); the typed text pre-fills the right field (e-mail address → e-mail, `+49…` → phone, `@name:server` → Matrix) ⚠️ detection rules proposed | contacts: `Create` JSContact card |
| minimal settings: accounts, notifications, theme, text size | `account.*` |

## What it does NOT do (deliberately)
Folders, rules, search filters, multi-select, formatting, reactions, threads view — those are in the
full frontend (no. 2).
