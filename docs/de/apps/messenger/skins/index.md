# Messenger Dokumentation

## Übersicht

Dieses Verzeichnis enthält Dokumentationen zu den Menüpunkten, Funktionen, Tastatur-Shortcuts und APIs verschiedener Messenger- und E-Mail-Anwendungen.

## Enthaltene Dokumentationen

- [Outlook](./outlook/index.md) - Microsoft E-Mail-Client
- [Kontact](./kontact/index.md) - KDE PIM-Anwendung
- [Thunderbird](./thunderbird/index.md) - Mozilla E-Mail-Client
- [Element](./element/index.md) - Matrix-Messenger
- [Discord](./discord/index.md) - Gaming/Community-Messenger
- [Mastodon](./mastodon/index.md) - Mikroblogging-Netzwerk
- [Telegram](./telegram/index.md) - Cloud-Messenger

## Verzeichnisstruktur

```
docs/de/messenger/skins/
├── index.md              (diese Datei)
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

## Inhalt jeder Dokumentation

Jedes Projektverzeichnis enthält **sechs** Dateien:

### menu.md
- Alle Hauptmenüpunkte
- Kontext-Menüs
- Benutzerrechte-abhängige Menüs

### features.md
- Hauptfunktionen
- Was das Programm kann
- Was das Programm NICHT kann
- Add-ons/Erweiterungen (wenn vorhanden)

### description.md
- Was das Programm macht
- Vorteile
- Abgrenzung zu anderen Systemen
- Technische Details
- Für wen das Programm geeignet ist

### structure.md
- Fenster-Struktur
- UI/UX Design
- Editor-Struktur (wenn vorhanden)
- Responsive Design
- Accessibility

### shortcuts.md
- Alle Tastatur-Shortcuts
- Allgemeine Shortcuts
- Chat/Conversation-Shortcuts
- Navigation-Shortcuts
- Bearbeiten-Shortcuts
- Mac Shortcuts (wenn verschieden)

### api.md
- API-Art (REST, GraphQL, WebSocket, etc.)
- Authentifizierung (OAuth2, API keys, etc.)
- Endpunkte mit Methoden, Pfaden und Beschreibungen
- Request/Response-Beispiele
- Rate Limits
- Webhooks (wenn vorhanden)
- SDKs und Client-Bibliotheken

## Hinweise

- Alle Dokumentationen sind auf Deutsch verfasst
- Die Inhalte sind für Anwender und Administratoren geeignet
- **Tastatur-Shortcuts sind in separater Datei `shortcuts.md` dokumentiert**
- **API-Dokumentation ist in separater Datei `api.md` dokumentiert**
- E-Mail-Clients enthalten E-Mail-Editor-Strukturen
- Messenger enthalten Chat- und Community-Strukturen

## Kategorien-System

**Bitte beachte:** Dieses System gilt für ALLE Kategorien in diesem Projekt:
- Wiki (abgeschlossen, 7 Programme)
- Messenger (abgeschlossen, 7 Programme)
- Desktop (abgeschlossen, 12 Programme)
- Whiteboards (abgeschlossen, 6 Programme)
- Helpdesk (abgeschlossen, 8 Programme)
- Projektmanagement (abgeschlossen, 8 Programme)
- Kontakt (abgeschlossen, 4 Programme)
- Kalender (abgeschlossen, 6 Programme)
- CRM (abgeschlossen, 6 Programme)
- Demokratie (abgeschlossen, 6 Programme)
- Maps (abgeschlossen, 7 Programme)
- ERP (abgeschlossen, 6 Programme)
- Workflows (abgeschlossen, 6 Programme)
- Marketing (abgeschlossen, 6 Programme)
- Marktplätze (abgeschlossen, 6 Programme)
- Foto-Galerien (abgeschlossen, 8 Programme)
- Streaming (abgeschlossen, 10 Programme)

**Jede Anwendung in jeder Kategorie erhält immer 7 Dateien:**
1. index.md (Übersicht und Links)
2. menu.md
3. features.md
4. description.md
5. structure.md
6. shortcuts.md (immer separat!)
7. api.md (REST, GraphQL, etc.)
