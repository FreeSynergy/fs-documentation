# Desktop-Applikationen

## Übersicht

Dieser Bereich enthält die Dokumentation für verschiedene Desktop-Applikationen und Software.

## Frontend-Dokumentation

Programme ohne eigenes Frontend-Verzeichnis werden nach dem Wiki-Schema dokumentiert (sieben Dateien pro Programm: `index`, `menu`, `features`, `description`, `structure`, `shortcuts`, `api`):

→ [Desktop-Frontends](frontends/index.md)

Dokumentiert: **homarr**, **heimdall**, **homer**, **dashy**, **homepage**, **gethomepage**, **launchboard**, **synology-dsm**, **unraid**, **proxmox**, **truenas**, **opnsense**

## Frontends

<!-- gen:frontends (Spiegel von docs/en; ADR 0011) — edits inside are overwritten -->
Analysierte Programme (12), nach Funktionen, nichts kopiert (ADR 0012/0013):

- [dashy](frontends/dashy/index.md) — Dashy ist ein anpassbares Self-Hosted-Dashboard für das eigene Netzwerk: App-Kacheln, Statusanzeigen, Widgets, Themes und Suche werden über `conf.yml` (oder JSON) beschrieben und lassen sich option…
- [gethomepage](frontends/gethomepage/index.md) — `gethomepage` bezeichnet die API-Bibliotheksschicht des Projekts `gethomepage/homepage`: die Service-Clients, Proxy-Handler, Konfigurationsleser und Hilfsfunktionen, die aus den YAML-Angaben der `s…
- [heimdall](frontends/heimdall/index.md) — Heimdall ist ein Application-Dashboard auf Laravel-Basis: App-Kacheln, optionale Statistik-Kacheln und Panels bilden eine persönliche Startseite für selbst gehostete Dienste.
- [homarr](frontends/homarr/index.md) — Homarr ist ein Self-Hosted Dashboard für Homelabs: Dienste, Container und Verknüpfungen werden in frei konfigurierbaren Boards (Widget-Rastern) gesammelt, live überwacht und per Klick geöffnet.
- [homepage](frontends/homepage/index.md) — Homepage (Projekt `gethomepage/homepage`) ist ein statisches Dashboard für Homelabs: Dienste, Links und Live-Widgets werden aus YAML-Dateien unter `config/` gerendert.
- [homer](frontends/homer/index.md) — Homer ist ein statisches Dashboard für selbst gehostete Dienste: Eine YAML-Datei beschreibt Gruppen und Kacheln, eine kleine Single-Page-Anwendung rendert daraus die Startseite.
- [launchboard](frontends/launchboard/index.md) — LaunchBoard ist ein kommerzielles, proprietäres Homelab-Dashboard: Boards werden per Drag & Drop ohne Konfigurationsdateien gebaut, Widgets liefern Live-Daten zu Containern, Medien- und Netzwerkdie…
- [opnsense](frontends/opnsense/index.md) — OPNsense ist eine Firewall- und Router-Distribution (FreeBSD-basiert, Deciso) mit vollständiger Web-UI: Interfaces, Firewall-Regeln (pf), NAT, VPN, Dienste und Plugins werden über Menüs konfigurier…
- [proxmox](frontends/proxmox/index.md) — Proxmox VE ist eine quelloffene Virtualisierungsplattform auf Debian-Basis: KVM-/QEMU-Virtualmaschinen und LXC-Container werden über eine gemeinsame Web-UI (Port 8006, HTTPS) betrieben — optional a…
- [synology-dsm](frontends/synology-dsm/index.md) — Synology DiskStation Manager (DSM) ist das proprietäre Betriebssystem der Synology-NAS mit einem vollständigen Desktop-Portal im Browser: Hauptmenü, Fenster-Verwaltung, App-Leiste, Desktop-Widgets,…
- [truenas](frontends/truenas/index.md) — TrueNAS (iXsystems, ehemals FreeNAS) ist die Open-Source-Speicherplattform mit durchgängiger ZFS-Verwaltung: Pools, Datasets, Snapshots, Replikation und Freigaben (SMB, NFS, iSCSI, S3) werden über …
- [unraid](frontends/unraid/index.md) — Unraid ist ein proprietäres Server-Betriebssystem für NAS-, Medien- und Spielserver: Ein Array mischt unterschiedlich große Festplatten, ein dediziertes Paritätslaufwerk schützt die Daten, und Dock…

Übersicht: [frontends](frontends/index.md)
<!-- /gen:frontends -->

## Dashboard- und Startseiten-Systeme

- **homarr** - Homelab-Dashboard mit Widgets und Docker-Integration
- **heimdall** - persönliches Dashboard mit Server-Statistiken
- **homer** - statisches Dashboard aus YAML-Konfiguration
- **dashy** - ausbaufähiges Dashboard mit Authentifizierung und Widgets
- **homepage** - Service-Dashboard mit Live-Widgets
- **gethomepage** - Service-Client-Bibliothek für die Widgets von homepage
- **launchboard** - kommerzielles No-Code-Dashboard
- **synology-dsm** - NAS-Portal mit eigener REST-API

## System-Oberflächen (NAS, Virtualisierung, Netzwerk)

Auch diese Programme haben eine desktopartige Oberfläche und sind als Maske dokumentiert:

- **unraid** - NAS-OS mit Array, Docker, VMs und GraphQL-API
- **proxmox** - Virtualisierungsplattform mit REST-API `/api2/json`
- **truenas** - ZFS-NAS mit Apps, VMs und JSON-RPC-API v2.0
- **opnsense** - Firewall und Router mit MVC-REST-API

## Verfügbare Systeme

- **libreoffice** - Office Suite
- **firefox** - Web-Browser
- **chrome** - Google Chrome
- **thunderbird** - E-Mail-Client
- **krita** - Digitale Malerei
- **gimp** - Bildbearbeitung
- **inkscape** - Vektorgrafik-Editor
- **blender** - 3D Creation Suite
- **obs-studio** - Video Recording und Streaming
- **audacity** - Audio-Editor
- **shotcut** - Video-Editor
- **kdenlive** - Video-Editor
- **vlc** - Media Player
- **mpv** - Media Player
- **telegram-desktop** - Desktop Messenger
- **element-desktop** - Desktop Messaging
- **discord** - Desktop App
- **slack** - Desktop App
- **zoom** - Video-Konferenz
- **skype** - Kommunikationsplattform

## Was ist eine Desktop-Applikation?

Eine Desktop-Applikation ist eine Software, die direkt auf dem Betriebssystem eines Computers ausgeführt wird. Desktop-Applikationen bieten:

- Lokale Ausführung ohne Web-Verbindung
- Zugriff auf lokale Ressourcen
- Systemintegration
- Native Performance
- Offline-Nutzung

## Anwendungsbereiche

- **Produktivität**: Office, Textverarbeitung, Tabellenkalkulation
- **Kreativität**: Grafikdesign, Video-Editing, Audio-Editing
- **Kommunikation**: E-Mail, Chat, Video-Konferenz
- **Entwicklung**: Entwicklungswerkzeuge und IDEs
- **Multimedia**: Media Player, Bildbetrachter

## Vorteile von Desktop-Applikationen

- **Performance**: Native Performance ohne Web-Begrenzungen
- **Offline-Nutzung**: Funktioniert ohne Internet-Verbindung
- **Systemintegration**: Tiefe Integration in das Betriebssystem
- **Sicherheit**: Bessere Kontrolle über Daten
- **Anpassung**: Umfangreiche Anpassungsmöglichkeiten

## Auswahlkriterien

Bei der Wahl einer Desktop-Applikation sollten folgende Kriterien berücksichtigt werden:

- **Funktionen**: Welche Features sind erforderlich?
- **Kompatibilität**: Unterstützt das Betriebssystem?
- **Open Source**: Ist das System Open Source?
- **Benutzerfreundlichkeit**: Wie einfach ist die Bedienung?
- **Integration**: Integration mit anderen Tools
- **Sicherheit**: Datenschutz und Sicherheit

## Verwandte Kategorien

- [Messenger](../../apps/messenger/) - Kommunikation und Chat
- [Wiki](../../apps/wiki/) - Wissensmanagement und Dokumentation
- [Projektmanagement](../../apps/projectmanagement/) - Project Management

## Schnellstart

1. **Applikation auswählen**: Basierend auf den Anforderungen eine Applikation wählen
2. **Installation**: Applikation herunterladen und installieren
3. **Konfiguration**: Applikation anpassen und konfigurieren
4. **Erste Schritte**: Erste Schritte mit der Applikation
5. **Integration**: Integration in bestehende Workflows

## Mehr Informationen

Weitere Informationen finden Sie in der Dokumentation der einzelnen Desktop-Applikationen.
