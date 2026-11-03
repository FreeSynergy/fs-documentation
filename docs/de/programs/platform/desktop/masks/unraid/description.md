# Unraid - Beschreibung

## Übersicht

Unraid (Unraid OS, Lime Technology) ist ein proprietäres, vom USB-Stick bootendes Server-Betriebssystem, das Netzwerkspeicher, Container und virtuelle Maschinen in einer Weboberfläche vereint. Die Oberfläche arbeitet mit festen Tabs (Main, Shares, Docker, VMs, Apps, Plugins, Tools, Settings) statt mit einem Desktop-Portal.

## Was Unraid macht

Unraid verwaltet ein **Array aus beliebig gemischten Festplatten**: Jedes Datenlaufwerk behält seine eigene Größe, ein (bei mehreren Paritätslaufwerken mehrere) Paritätslaufwerk(e) sichern gegen Ausfälle. Kapazität lässt sich laufwerkweise erweitern. Darüber hinaus verwaltet die Weboberfläche **SMB/NFS-Freigaben** (User Shares), **Benutzer**, **Docker-Container** (mit Vorlagen-Katalog), **virtuelle Maschinen** (libvirt/KVM) und einen **Plugin-Store** (Community Applications). Die Konfiguration liegt als XML auf dem USB-Bootmedium; seit jüngeren Versionen ergänzt eine GraphQL-API mit API-Keys die Automatisierung.

## Vorteile

- **Flexibles Array**: beliebige Plattengrößen mischbar, kapazitätsgenaue Erweiterung, eigene Parität
- **Alles in einer UI**: Speicher, Freigaben, Docker, VMs, Plugins in einem System
- **Community Applications**: großer, kuratierter Katalog fertiger Container-Vorlagen
- **Einfacher Einstieg**: Web-UI führt durch Array, Freigaben und Apps ohne Config-Dateien
- **Unraid Connect**: Remote-Zugriff, Updates und Support-Diagnose über das Unraid-Konto
- **API-Keys und GraphQL**: moderne Automatisierungsgrundlage in aktuellen Versionen

## Abgrenzung zu anderen Systemen

### Unraid vs. TrueNAS
- **Unraid** ist proprietär (Lizenzmodell versionabhängig), **TrueNAS** ist Open Source
- **Unraid** nutzt ein mdadm-artiges Array mit mixbarer Kapazität, **TrueNAS** setzt durchgängig auf ZFS
- **TrueNAS** hat die tiefere Datenverwaltung (Datasets, Replikation, ACL), **Unraid** die lockerere App-/Medien-Küche

### Unraid vs. Proxmox VE
- **Proxmox VE** ist eine ausgewachsene Virtualisierungsplattform mit Cluster, Ceph und HA; **Unraid** ist ein Einzelserver-System mit Speicher-Schwerpunkt
- **Proxmox** hat eine vollständige REST-API, **Unraid** historisch gar keine und inzwischen GraphQL (versionabhängig)
- **Unraid** richtet sich an Medien- und Homelab-Nutzer, **Proxmox** an Betreiber von VM-Landschaften

### Unraid vs. Homarr/Heimdall
- **Homarr/Heimdall** sind Dashboards: Sie zeigen nur Kacheln und Statuswerte anderer Dienste
- **Unraid** ist das System selbst; ein Dashboard kann Unraid allenfalls per API einbinden
- Alle drei zusammen sind üblich: Unraid betreibt, das Dashboard verlinkt und überwacht

## Technische Details

- **Backend**: Slackware-Linux-Basis; Weboberfläche als PHP-Anwendung (webGui/Dynamix), Docker-Engine und libvirt/QEMU für VMs
- **Database**: keine klassische Datenbank — Konfiguration als XML-Dateien auf dem USB-Bootmedium (`/boot/config`), Array-Metadaten auf den Laufwerken
- **Frontend**: serverseitig gerenderte HTML-Seiten mit Formularen und Tabellen, jQuery-basierte Details (versionabhängig)
- **Authentication**: lokale WebUI-Anmeldung, Unix-/Samba-Benutzer, Unraid-Connect-Konto für Remote-Funktionen, API-Keys mit Rollen (`admin`, `connect`, `guest`)
- **Hosting**: Bare-Metal-x86-64, bootend vom USB-Stick; Web-UI auf 80/443, SSH optional; Lizenz an die Hardware-Merge gebunden (versionabhängig)

## Für wen ist Unraid geeignet?

- **Medien- und Homelab-Nutzer**, die viele verschiedene (Rest-)Platten mit Parität nutzen wollen
- **Selbstversorger mit App-Stapeln**, die Docker-Anwendungen schnell aus Vorlagen installieren möchten
- **Einzelserver-Betreiber ohne Cluster-Anspruch** — für HA-Verbünde und reine Storage-Appliances sind TrueNAS oder Proxmox VE die bessere Wahl
