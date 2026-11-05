# Messenger Documentation

## Overview

This directory documents the menu items, features, keyboard shortcuts and APIs of various messenger and email applications.

## Included Documentation

- [Outlook](outlook/index.md) - Microsoft email client
- [Kontact](kontact/index.md) - KDE PIM application
- [Thunderbird](thunderbird/index.md) - Mozilla email client
- [Element](element/index.md) - Matrix messenger
- [Discord](discord/index.md) - Gaming/community messenger
- [Mastodon](mastodon/index.md) - Microblogging network
- [Telegram](telegram/index.md) - Cloud messenger

## Directory Structure

```
docs/en/programs/apps/messenger/frontends/
├── index.md              (this file)
├── outlook/
│   ├── index.md
│   ├── menu.md
│   ├── features.md
│   ├── description.md
│   ├── structure.md
│   ├── shortcuts.md
│   └── api.md
├── kontact/
│   ├── index.md
│   ├── menu.md
│   ├── features.md
│   ├── description.md
│   ├── structure.md
│   ├── shortcuts.md
│   └── api.md
├── thunderbird/
│   ├── index.md
│   ├── menu.md
│   ├── features.md
│   ├── description.md
│   ├── structure.md
│   ├── shortcuts.md
│   └── api.md
├── element/
│   ├── index.md
│   ├── menu.md
│   ├── features.md
│   ├── description.md
│   ├── structure.md
│   ├── shortcuts.md
│   └── api.md
├── discord/
│   ├── index.md
│   ├── menu.md
│   ├── features.md
│   ├── description.md
│   ├── structure.md
│   ├── shortcuts.md
│   └── api.md
├── mastodon/
│   ├── index.md
│   ├── menu.md
│   ├── features.md
│   ├── description.md
│   ├── structure.md
│   ├── shortcuts.md
│   └── api.md
└── telegram/
    ├── index.md
    ├── menu.md
    ├── features.md
    ├── description.md
    ├── structure.md
    ├── shortcuts.md
    └── api.md
```

## Content of Each Documentation

Every project directory holds **six** files:

### menu.md
- All main menu items
- Context menus
- Menus that depend on user rights

### features.md
- Main features
- What the program can do
- What the program CANNOT do
- Add-ons/extensions (where present)

### description.md
- What the program does
- Advantages
- Differentiation from other systems
- Technical details
- Who the program is suitable for

### structure.md
- Window structure
- UI/UX design
- Editor structure (where present)
- Responsive design
- Accessibility

### shortcuts.md
- All keyboard shortcuts
- General shortcuts
- Chat/conversation shortcuts
- Navigation shortcuts
- Editing shortcuts
- Mac shortcuts (where they differ)

### api.md
- API type (REST, GraphQL, WebSocket, etc.)
- Authentication (OAuth2, API keys, etc.)
- Endpoints with methods, paths and descriptions
- Request/response examples
- Rate limits
- Webhooks (where present)
- SDKs and client libraries

## Notes

- All documentation is written in English
- The content suits both users and administrators
- **Keyboard shortcuts are documented in the separate file `shortcuts.md`**
- **API documentation is in the separate file `api.md`**
- Email clients include email editor structures
- Messengers include chat and community structures

## Category System

**Please note:** this system applies to ALL categories in this project:
- Wiki (complete, 7 programs)
- Messenger (complete, 7 programs)
- Desktop (complete, 12 programs)
- Whiteboards (complete, 6 programs)
- Helpdesk (complete, 8 programs)
- Project management (complete, 8 programs)
- Contact (complete, 4 programs)
- Calendar (complete, 6 programs)
- CRM (complete, 6 programs)
- Democracy (complete, 6 programs)
- Maps (complete, 7 programs)
- ERP (complete, 6 programs)
- Workflows (complete, 6 programs)
- Marketing (complete, 6 programs)
- Marketplaces (complete, 6 programs)
- Photo galleries (complete, 8 programs)
- Streaming (complete, 10 programs)

**Every application in every category always gets 7 files:**
1. index.md (overview and links)
2. menu.md
3. features.md
4. description.md
5. structure.md
6. shortcuts.md (always separate!)
7. api.md (REST, GraphQL, etc.)
