# Desktop — Frontend-Dokumentation

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Desktop` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [Dashy](dashy/index.md) | [latest](dashy/latest/description.md) | Dashy ist ein anpassbares Self-Hosted-Dashboard für das eigene Netzwerk: App-Kacheln, Statusanzeigen, Widgets, Themes und Suche werden über `conf.yml` (oder JSON) beschrieben und lassen sich option… |
| [gethomepage (Bibliothek)](gethomepage/index.md) | [latest](gethomepage/latest/description.md) |  |
| [Heimdall](heimdall/index.md) | [latest](heimdall/latest/description.md) | Heimdall ist ein Application-Dashboard auf Laravel-Basis: App-Kacheln, optionale Statistik-Kacheln und Panels bilden eine persönliche Startseite für selbst gehostete Dienste. |
| [Homarr](homarr/index.md) | [latest](homarr/latest/description.md) | Homarr ist ein Self-Hosted Dashboard für Homelabs: Dienste, Container und Verknüpfungen werden in frei konfigurierbaren Boards (Widget-Rastern) gesammelt, live überwacht und per Klick geöffnet. |
| [Homepage](homepage/index.md) | [latest](homepage/latest/description.md) | Homepage (Projekt `gethomepage/homepage`) ist ein statisches Dashboard für Homelabs: Dienste, Links und Live-Widgets werden aus YAML-Dateien unter `config/` gerendert. |
| [Homer](homer/index.md) | [latest](homer/latest/description.md) | Homer ist ein statisches Dashboard für selbst gehostete Dienste: Eine YAML-Datei beschreibt Gruppen und Kacheln, eine kleine Single-Page-Anwendung rendert daraus die Startseite. |
| [LaunchBoard](launchboard/index.md) | [latest](launchboard/latest/description.md) | LaunchBoard ist ein kommerzielles, proprietäres Homelab-Dashboard: Boards werden per Drag & Drop ohne Konfigurationsdateien gebaut, Widgets liefern Live-Daten zu Containern, Medien- und Netzwerkdie… |
| [OPNsense](opnsense/index.md) | [latest](opnsense/latest/description.md) | OPNsense ist eine Firewall- und Router-Distribution (FreeBSD-basiert, Deciso) mit vollständiger Web-UI: Interfaces, Firewall-Regeln (pf), NAT, VPN, Dienste und Plugins werden über Menüs konfigurier… |
| [Proxmox VE](proxmox/index.md) | [latest](proxmox/latest/description.md) | Proxmox VE ist eine quelloffene Virtualisierungsplattform auf Debian-Basis: KVM-/QEMU-Virtualmaschinen und LXC-Container werden über eine gemeinsame Web-UI (Port 8006, HTTPS) betrieben — optional a… |
| [Synology DSM](synology-dsm/index.md) | [latest](synology-dsm/latest/description.md) | Synology DiskStation Manager (DSM) ist das proprietäre Betriebssystem der Synology-NAS mit einem vollständigen Desktop-Portal im Browser: Hauptmenü, Fenster-Verwaltung, App-Leiste, Desktop-Widgets,… |
| [TrueNAS](truenas/index.md) | [latest](truenas/latest/description.md) | TrueNAS (iXsystems, ehemals FreeNAS) ist die Open-Source-Speicherplattform mit durchgängiger ZFS-Verwaltung: Pools, Datasets, Snapshots, Replikation und Freigaben (SMB, NFS, iSCSI, S3) werden über … |
| [Unraid](unraid/index.md) | [latest](unraid/latest/description.md) | Unraid ist ein proprietäres Server-Betriebssystem für NAS-, Medien- und Spielserver: Ein Array mischt unterschiedlich große Festplatten, ein dediziertes Paritätslaufwerk schützt die Daten, und Dock… |

## Dateisatz pro Programm (ADR 0012)

```
programs/platform/desktop/frontends/<program>/
├── index.md        was es ist, bemerkenswerte Ideen, dokumentierte Versionen, Quellen
├── changelog.md    Änderungen zwischen dokumentierten Versionen (≥ 2 Versionen)
└── <version>/
    ├── description.md    Pflicht · Ausführliche Beschreibung, Abgrenzung, für wen es passt
    ├── features.md       Pflicht · Was das Programm kann — und was nicht
    ├── layout.md         Pflicht · Fensterstruktur, Bereiche, Panels
    ├── menus.md          Pflicht · Menüstruktur, Kontextmenüs, Menüs nach Rolle
    ├── shortcuts.md      Pflicht · Tastatur-Shortcuts
    ├── api.md            Pflicht · APIs und Protokolle, Authentifizierung, Rate Limits
    ├── themes/index.md   Pflicht · Themes: Farben, Typografie, Abstände — was sich nachbauen lässt
    ├── interaction.md    bei Bedarf · Hover, Fokus, Ziehen, Gesten (Finger, Maus, Stift)
    ├── states.md         bei Bedarf · UI-Zustände und Übergänge
    ├── events.md         bei Bedarf · Ereignisse nach außen (Webhooks, Push, Streams)
    ├── limits.md         bei Bedarf · Bekannte Grenzen
    ├── i18n.md           bei Bedarf · Lokalisierung, Schreibrichtung
    └── dependencies.md   bei Bedarf · Welche unserer Bausteine ein Frontend dieser Art braucht
```

Protokolle (Matrix, IMAP, CalDAV, …) sind keine Frontends; sie stehen unter [data](../../../../data/standards.md).
