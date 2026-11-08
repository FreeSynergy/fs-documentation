# Desktop-Anwendungen

## Überblick

Dieser Bereich enthält Dokumentation zu verschiedenen Desktop-Anwendungen und Programmen.

## Frontend-Dokumentation

Programme ohne eigenes Masken-Verzeichnis werden nach dem Wiki-Schema dokumentiert (sieben Dateien je Programm: `index`, `menu`, `features`, `description`, `structure`, `shortcuts`, `api`):

→ [Desktop-Frontends](frontends/index.md)

Dokumentiert: **homarr**, **heimdall**, **homer**, **dashy**, **homepage**, **gethomepage**, **launchboard**, **synology-dsm**, **unraid**, **proxmox**, **truenas**, **opnsense**

## Dashboard- und Startseiten-Systeme

- **homarr** - Homelab-Dashboard mit Widgets und Docker-Integration
- **heimdall** - Persönliches Dashboard mit Serverstatistiken
- **homer** - Statisches Dashboard, aus einer YAML-Konfiguration erstellt
- **dashy** - Erweiterbares Dashboard mit Authentifizierung und Widgets
- **homepage** - Dienst-Dashboard mit Live-Widgets
- **gethomepage** - Client-Bibliothek für die Dienste der Widgets von homepage
- **launchboard** - Kommerzielles Dashboard ohne Code
- **synology-dsm** - NAS-Portal mit eigener REST-API

## Systemoberflächen (NAS, Virtualisierung, Netzwerk)

Diese Programme haben ebenfalls eine desktopartige Oberfläche und sind als Frontend dokumentiert:

- **unraid** - NAS-Betriebssystem mit Array, Docker, VMs und GraphQL-API
- **proxmox** - Virtualisierungsplattform mit REST-API `/api2/json`
- **truenas** - ZFS-NAS mit Apps, VMs und JSON-RPC-API v2.0
- **opnsense** - Firewall und Router mit MVC-REST-API

## Verfügbare Systeme

- **libreoffice** - Office-Suite
- **firefox** - Webbrowser
- **chrome** - Google Chrome
- **thunderbird** - E-Mail-Programm
- **krita** - Digitale Malerei
- **gimp** - Bildbearbeitung
- **inkscape** - Editor für Vektorgrafiken
- **blender** - 3D-Werkzeugpaket
- **obs-studio** - Videoaufnahme und Streaming
- **audacity** - Audioeditor
- **shotcut** - Videoeditor
- **kdenlive** - Videoeditor
- **vlc** - Medienplayer
- **mpv** - Medienplayer
- **telegram-desktop** - Desktop-Messenger
- **element-desktop** - Desktop-Messaging
- **discord** - Desktop-App
- **slack** - Desktop-App
- **zoom** - Videokonferenzen
- **skype** - Kommunikationsplattform

## Was ist eine Desktop-Anwendung?

Eine Desktop-Anwendung ist Software, die direkt auf dem Betriebssystem eines Computers läuft. Desktop-Anwendungen bieten:

- Ausführung ohne Webverbindung
- Zugriff auf lokale Ressourcen
- Integration ins System
- Native Leistung
- Nutzung ohne Internet

## Anwendungsbereiche

- **Produktivität**: Büro, Textverarbeitung, Tabellenkalkulation
- **Kreativität**: Grafikdesign, Videobearbeitung, Audiobearbeitung
- **Kommunikation**: E-Mail, Chat, Videokonferenzen
- **Entwicklung**: Entwicklungswerkzeuge und IDEs
- **Multimedia**: Medienplayer, Bildbetrachter

## Vorteile von Desktop-Anwendungen

- **Leistung**: Native Leistung ohne Einschränkungen des Webs
- **Offline-Nutzung**: Funktioniert ohne Internetverbindung
- **Systemintegration**: Tiefe Integration ins Betriebssystem
- **Sicherheit**: Mehr Kontrolle über deine Daten
- **Anpassung**: Viele Möglichkeiten zur Anpassung

## Auswahlkriterien

Bei der Wahl einer Desktop-Anwendung solltest du folgende Kriterien berücksichtigen:

- **Funktionen**: Welche Funktionen werden gebraucht?
- **Kompatibilität**: Unterstützt sie dein Betriebssystem?
- **Open Source**: Ist das System Open Source?
- **Bedienbarkeit**: Wie benutzerfreundlich ist es?
- **Integration**: Integration mit anderen Werkzeugen
- **Sicherheit**: Datenschutz und Sicherheit

## Verwandte Kategorien

- [Messenger](../../apps/messenger/) - Kommunikation und Chat
- [Wiki](../../apps/wiki/) - Wissensmanagement und Dokumentation
- [Projektmanagement](../../suites/projectmanagement/) - Projektmanagement

## Schnellstart

1. **Anwendung auswählen**: Wähle eine Anwendung anhand der Anforderungen
2. **Installation**: Anwendung herunterladen und installieren
3. **Konfiguration**: Anwendung anpassen und einrichten
4. **Erste Schritte**: Die ersten Schritte mit der Anwendung
5. **Integration**: Einbindung in bestehende Arbeitsabläufe

## Weitere Informationen

Weitere Informationen findest du in der Dokumentation der einzelnen Desktop-Anwendungen.

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
Analysierte Programme (12), nach Funktion, nichts kopiert (ADR 0012/0013):

- [Dashy](frontends/dashy/index.md) — Dashy ist ein anpassbares, selbst gehostetes Dashboard für dein eigenes Netzwerk: App-Kacheln, Statusanzeigen, Widgets, Themes und Suche werden über `conf.yml` (oder JSON) beschrieben und können optional in einer …
- [gethomepage (Bibliothek)](frontends/gethomepage/index.md) — `gethomepage` bezeichnet die **API-Bibliotheksschicht** des Projekts `gethomepage/homepage`: die Dienst-Clients, Proxy-Handler, Konfigurationsleser und Hilfsfunktionen, die die YAML-Einträge in …
- [Heimdall](frontends/heimdall/index.md) — Heimdall ist ein Anwendungs-Dashboard auf Basis von Laravel: App-Kacheln, optionale Statistik-Kacheln und Panels bilden eine persönliche Startseite für selbst gehostete Dienste.
- [Homarr](frontends/homarr/index.md) — Homarr ist ein selbst gehostetes Dashboard für Homelabs: Dienste, Container und Links werden auf frei konfigurierbaren Boards (Widget-Rastern) gesammelt, live überwacht und mit einem Klick geöffnet.
- [Homepage](frontends/homepage/index.md) — Homepage (Projekt `gethomepage/homepage`) ist ein statisches Dashboard für Homelabs: Dienste, Links und Live-Widgets werden aus YAML-Dateien unter `config/` erzeugt.
- [Homer](frontends/homer/index.md) — Homer ist ein statisches Dashboard für selbst gehostete Dienste: Eine YAML-Datei beschreibt Gruppen und Kacheln, und eine kleine Single-Page-Anwendung erzeugt daraus die Startseite.
- [LaunchBoard](frontends/launchboard/index.md) — LaunchBoard ist ein **kommerzielles, proprietäres Homelab-Dashboard**: Boards werden per Drag and Drop ohne Konfigurationsdateien gebaut, Widgets liefern Live-Daten für Container, Medien- und Netzwerkdienste, …
- [OPNsense](frontends/opnsense/index.md) — OPNsense ist eine Firewall- und Router-Distribution (auf FreeBSD basiert, von Deciso) mit einer vollständigen Web-Oberfläche: Schnittstellen, Firewall-Regeln (pf), NAT, VPN, Dienste und Plugins werden über Menüs eingerichtet, mit Änderungen …
- [Proxmox VE](frontends/proxmox/index.md) — Proxmox VE ist eine quelloffene Virtualisierungsplattform auf Debian-Basis: KVM/QEMU-virtuelle Maschinen und LXC-Container werden über eine gemeinsame Web-Oberfläche (Port 8006, HTTPS) betrieben – optional als Cluster …
- [Synology DSM](frontends/synology-dsm/index.md) — Synology DiskStation Manager (DSM) ist das proprietäre Betriebssystem der Synology-NAS-Geräte, mit einem vollständigen **Desktop-Portal im Browser**: Hauptmenü, Fensterverwaltung, App-Leiste, Desktop-Widgets …
- [TrueNAS](frontends/truenas/index.md) — TrueNAS (iXsystems, früher FreeNAS) ist die quelloffene Speicherplattform mit durchgängiger ZFS-Verwaltung: Pools, Datasets, Snapshots, Replikation und Freigaben (SMB, NFS, iSCSI, S3) werden über eine …
- [Unraid](frontends/unraid/index.md) — Unraid ist ein proprietäres Serverbetriebssystem für NAS, Medien- und Spieleserver: Ein Array mischt Festplatten unterschiedlicher Größe, eine eigene Paritätsplatte schützt die Daten, und Docker-Container und …

Übersicht: [frontends](frontends/index.md)
<!-- /gen:frontends -->
