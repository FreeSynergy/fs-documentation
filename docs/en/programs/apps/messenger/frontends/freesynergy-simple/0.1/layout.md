# FreeSynergy Simple 0.1 — Layout

## Reading screen (start screen)
```
┌──────────────────────────────────────┐
│ ⚙ settings                  ☰ list   │  top bar: two icons only
│                                      │
│  sender · time · 🔒 encryption state │
│  subject (mail) / room (chat)        │
│                                      │
│  message text, full screen           │
│  attachments inline                  │
│                                      │
└──────────────────────────────────────┘
```

## Compose / reply screen
```
┌──────────────────────────────────────┐
│ 👤+ add recipients     recipients …  │
│                                      │
│  text (simple editor)                │
│                                      │
│  ↑ send · ↓ cancel · ← draft · → attach (hints, fade out after use)
└──────────────────────────────────────┘
```

## List screen
Plain list of conversations (newest first, unread marked). Top right: ✎ new message (replaces the
list icon). Tap an entry → reading screen.

## Recipient picker
```
┌──────────────────────────────────────┐
│ 🔍 type a name, number, address …    │
│  ─ filtered contact list ─           │
│  Anna Berg       Matrix · Mail       │
│  …                                   │
└──────────────────────────────────────┘
```
No match → "new contact" form opens (see [features](features.md)).

## Settings
One short page: accounts, notifications, theme (light/dark), text size. Nothing else.
