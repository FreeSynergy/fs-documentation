# Wiki Skin Dokumentation

## Übersicht

Dieses Verzeichnis enthält Dokumentationen zu den Menüpunkten, Funktionen, Tastatur-Shortcuts und APIs verschiedener Wiki-Software-Systeme und Entwickler-Tools.

## Enthaltene Dokumentationen

- [Wiki.js](./wikijs/index.md) - Moderne, leichtgewichtige Wiki-Software
- [XWiki](./xwiki/index.md) - Enterprise-Wiki-Plattform
- [MediaWiki](./mediawiki/index.md) - Die beliebteste Wiki-Software (Wikipedia)
- [Tango.io](./tango.io/index.md) - Wissensmanagement-Plattform
- [Notion](./notion/index.md) - All-in-one-Plattform für Zusammenarbeit
- [Confluence](./confluence/index.md) - Enterprise-Wiki von Atlassian
- [VSCodium](./vscodium/index.md) - Quelloffener Code-Editor (VS Code Fork)

## Verzeichnisstruktur

```
docs/de/wiki/skins/
├── index.md              (diese Datei)
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
- Erweiterungen/Plugins

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
- Editor/Conversation-Shortcuts
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
- Wiki-Software enthält Wiki-Editor-Strukturen

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
