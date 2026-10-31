# Desktop-Skin-Dokumentation

## Übersicht

Dieses Verzeichnis enthält die Dokumentation zu Desktop- und Dashboard-Programmen nach demselben Schema wie die Wiki-Skins: Menüpunkte, Funktionen, Beschreibung, Struktur/UI-UX, Tastatur-Shortcuts und API.

Alle hier dokumentierten Programme sind **keine** FreeSynergy-Eigenentwicklungen, sondern fremde Programme, deren Oberfläche und Schnittstellen als Skin nachgebildet bzw. angebunden werden.

## Enthaltene Dokumentationen

- [Homarr](./homarr/index.md) - Modernes Homelab-Dashboard (Next.js, Widgets, Docker-Integration)
- [Heimdall](./heimdall/index.md) - schlankes persönliches Dashboard mit Server-Statistiken
- [Homer](./homer/index.md) - statisches Dashboard, rein YAML-konfiguriert
- [Dashy](./dashy/index.md) - sehr mächtiges Dashboard mit Widgets und Authentifizierung
- [Homepage](./homepage/index.md) - statisches Dashboard mit Service-Widgets (gethomepage)
- [gethomepage (Library)](./gethomepage/index.md) - Service-Client-Bibliothek hinter Homepage
- [LaunchBoard](./launchboard/index.md) - kommerzielles Homelab-Dashboard ohne Code
- [Synology DSM](./synology-dsm/index.md) - NAS-Desktop-Portal mit `SYNO.*`-REST-API
- [Unraid](./unraid/index.md) - proprietäres NAS-OS mit Array, Docker, VMs und GraphQL-API
- [Proxmox VE](./proxmox/index.md) - Virtualisierungsplattform mit REST-API `/api2/json`
- [TrueNAS](./truenas/index.md) - ZFS-NAS mit Apps/VMs und JSON-RPC-API v2.0
- [OPNsense](./opnsense/index.md) - Firewall/Router mit MVC-REST-API und API-Key-Auth

## Verzeichnisstruktur

```
docs/de/apps/desktop/skins/
├── index.md              (diese Datei)
├── homarr/
│   ├── index.md
│   ├── menu.md
│   ├── features.md
│   ├── description.md
│   ├── structure.md
│   ├── shortcuts.md
│   └── api.md
├── heimdall/   (gleiche sieben Dateien)
├── homer/      (gleiche sieben Dateien)
├── dashy/      (gleiche sieben Dateien)
├── homepage/   (gleiche sieben Dateien)
├── gethomepage/(gleiche sieben Dateien)
├── launchboard/(gleiche sieben Dateien)
├── synology-dsm/(gleiche sieben Dateien)
├── unraid/     (gleiche sieben Dateien)
├── proxmox/    (gleiche sieben Dateien)
├── truenas/    (gleiche sieben Dateien)
└── opnsense/   (gleiche sieben Dateien)
```

## Inhalt jeder Dokumentation

Jedes Programmverzeichnis enthält **sieben** Dateien:

### index.md
- Übersicht des Programms
- Links auf die sechs Detail-Dateien

### menu.md
- Alle Hauptmenüpunkte
- Kontext-Menüs (Rechtsklick, Widget-Bearbeitung)
- Menüs abhängig von Benutzerrolle

### features.md
- Hauptfunktionen und Widgets
- Was das Programm kann
- Was das Programm NICHT kann
- Erweiterungen, Plugins, Integrationen

### description.md
- Was das Programm macht
- Vorteile
- Abgrenzung zu anderen Systemen
- Technische Details (Backend, Datenbank, Frontend, Authentifizierung, Hosting)
- Für wen das Programm geeignet ist

### structure.md
- Fenster-Struktur (ASCII-Diagramm)
- UI/UX-Design, Themes, Farbschema
- Interaktionen (Drag & Drop, Animationen)
- Responsive Design, Accessibility, Performance

### shortcuts.md
- Alle Tastatur-Shortcuts
- Allgemeine Shortcuts, Navigation, Bearbeitung, Suche
- Mac-Varianten (Cmd)
- Nicht vorhandene Shortcuts sind als solche gekennzeichnet

### api.md
- API-Art (REST, TRPC, JSON/YAML-Config, `SYNO.*`)
- Authentifizierung (API-Key, OAuth2/OIDC, Session)
- Endpunkte mit Methoden, Pfaden und Beschreibungen
- Request/Response-Beispiele
- Rate Limits, Webhooks
- SDKs und Client-Bibliotheken

## Kategorien-System

Dieses Schema gilt für **alle** Kategorien:

| Kategorie | Skin-Status |
|-----------|-------------|
| Wiki | abgeschlossen (7 Programme) |
| Messenger | teilweise (7 Programme dokumentiert) |
| Desktop | abgeschlossen (12 Programme) |
| Components | eigenes Schema (`description`/`appearance`/`attributes`) |
| Whiteboards, Helpdesk, Projektmanagement, Kontakt, Kalender, CRM, Demokratie, Maps, ERP, Workflows, Marketing | Skin-Dokumentation vorgesehen |

## Nachziehen (Kandidaten je Kategorie)

Die folgenden Programme sind für die Skin-Dokumentation vorgesehen und werden nach demselben Schema ergänzt:

| Kategorie | Kandidaten |
|-----------|------------|
| Desktop | **dokumentiert:** homarr, heimdall, homer, dashy, homepage, gethomepage, launchboard, synology-dsm, unraid, proxmox, truenas, opnsense — **vorgesehen:** pfsense, chrome, windows-11, macos-finder, gnome-shell, kde-plasma, windows-start, raycast, alfred, launchy, fluent-search, ulauncher, powerlauncher, wox, flow-launcher, keeweb, obsidian, logseq |
| Whiteboards | excalidraw, miro, mural, jamboard, tldraw, drawio, openboard, figjam |
| Helpdesk | zammad, osticket, glpi, request-tracker, zendesk, freshdesk, helpscout |
| Projektmanagement | trello, jira, asana, redmine, taiga, openproject, planka, wekan, clickup, mon |
| Kontakt / CRM | nextcloud-contacts, civicrm, suitecrm, espocrm, monica, pipedrive, hubspot |
| Kalender | nextcloud-calendar, davical, rndc, Thunderbird-events, google-calendar, outlook-calendar |
| Maps | openstreetmap, leaflet, maplibre, qgis, maputnik, geojson-io |
| ERP | erpnext, odoo, dolibarr, axelor, tryton, ofbiz |
| Workflows | n8n, node-red, kestra, airflow, make, zapier, activepieces |
| Demokratie | decidim, consul, liquider, pol.is, society |

## Hinweise

- Alle Dokumentationen sind auf Deutsch verfasst
- Die Inhalte sind für Anwender und Administratoren geeignet
- **Tastatur-Shortcuts sind immer in der separaten Datei `shortcuts.md`**
- **API-Dokumentation ist immer in der separaten Datei `api.md`**
- Statische Programme ohne Backend (Homer, Homepage) haben keine API im klassischen Sinn — dort wird die Konfigurationsdatei dokumentiert

## Verwandte Bereiche

- [Desktop-Kategorie](../) - Überblick über Desktop-Applikationen
- [Wiki-Skins](../../wiki/skins/) - Referenzschema dieser Dokumentation
- [Messenger-Skins](../../messenger/skins/) - gleiche Dateistruktur
- [Standardisierte Daten](../../../data/) - Felder und Modelle für alle Skin-APIs
