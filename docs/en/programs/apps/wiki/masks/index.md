# Wiki Mask Documentation

## Overview

This directory documents the menu items, features, keyboard shortcuts and APIs of various wiki software systems and developer tools.

## Included Documentation

- [Wiki.js](wikijs/index.md) - Modern, lightweight wiki software
- [XWiki](xwiki/index.md) - Enterprise wiki platform
- [MediaWiki](mediawiki/index.md) - The most popular wiki software (Wikipedia)
- [Tango.io](tango.io/index.md) - Knowledge management platform
- [Notion](notion/index.md) - All-in-one collaboration platform
- [Confluence](confluence/index.md) - Enterprise wiki by Atlassian
- [VSCodium](vscodium/index.md) - Open-source code editor (VS Code fork)

## Directory Structure

```
docs/en/programs/apps/wiki/masks/
├── index.md              (this file)
├── wikijs/
│   ├── index.md
│   ├── menu.md
│   ├── features.md
│   ├── description.md
│   ├── structure.md
│   ├── shortcuts.md
│   └── api.md
├── xwiki/
│   ├── index.md
│   ├── menu.md
│   ├── features.md
│   ├── description.md
│   ├── structure.md
│   ├── shortcuts.md
│   └── api.md
├── mediawiki/
│   ├── index.md
│   ├── menu.md
│   ├── features.md
│   ├── description.md
│   ├── structure.md
│   ├── shortcuts.md
│   └── api.md
├── tango.io/
│   ├── index.md
│   ├── menu.md
│   ├── features.md
│   ├── description.md
│   ├── structure.md
│   ├── shortcuts.md
│   └── api.md
├── notion/
│   ├── index.md
│   ├── menu.md
│   ├── features.md
│   ├── description.md
│   ├── structure.md
│   ├── shortcuts.md
│   └── api.md
├── confluence/
│   ├── index.md
│   ├── menu.md
│   ├── features.md
│   ├── description.md
│   ├── structure.md
│   ├── shortcuts.md
│   └── api.md
└── vscodium/
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
- Extensions/plugins

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
- Editor/conversation shortcuts
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
- Wiki software includes wiki editor structures

## Category System

**Please note:** this system applies to ALL categories in this project:
- Wiki (7 programs)
- Messenger (7 programs)
- Desktop (12 programs)
- Whiteboards (6 programs)
- Helpdesk (8 programs)
- Project management (8 programs)
- Contact (4 programs)
- Calendar (6 programs)
- CRM (6 programs)
- Democracy (6 programs)
- Maps (7 programs)
- ERP (6 programs)
- Workflows (6 programs)
- Marketing (6 programs)
- Marketplaces (6 programs)
- Photo galleries (8 programs)
- Streaming (10 programs)

**Every application in every category always gets 7 files:**
1. index.md (overview and links)
2. menu.md
3. features.md
4. description.md
5. structure.md
6. shortcuts.md (always separate!)
7. api.md (REST, GraphQL, etc.)

Status of this mirror: in `en/` each of the seven programs currently has only
`index.md`; the remaining six files per program are still to be translated from
`docs/de/programs/apps/wiki/masks/` (see `todo/translator.md`).
