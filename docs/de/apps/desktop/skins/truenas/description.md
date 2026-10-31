# TrueNAS - Beschreibung

## Übersicht

TrueNAS ist die weltweit meistgenutzte Open-Source-Speicherplattform (Community Edition kostenlos, Enterprise-Appliances mit Support). Kern ist die **ZFS-Verwaltung in einer Weboberfläche**: Pools, Datasets, Snapshots, Replikation und Berechtigungen. **TrueNAS CORE** läuft auf FreeBSD und ist auf Speicher ausgelegt; **TrueNAS SCALE** (aktuell, Versionen nach Jahreszahl wie 24.10, 25.04) läuft auf Linux und bringt Docker-Apps und KVM-Virtualisierung mit.

## Was TrueNAS macht

Die Middleware (`middlewared`) verbindet Weboberfläche, CLI und API mit dem System: Pools werden per Assistent angelegt, Datasets als Baum mit Properties (Kompression, Quota, ACL, Verschlüsselung) verwaltet. Freigaben (SMB, NFS, iSCSI, FTP, S3/Bucket, WebShare je nach Version) liegen auf Datasets; Periodic Snapshots, Replication Tasks und Cloud Sync bilden den Datenschutz. Die App-Kataloge installieren Docker-Container, ab 24.10 zusätzlich virtuelle Maschinen. Rechte kommen über lokale Nutzer/Gruppen, ACLs sowie Active Directory/LDAP; API-Keys und 2FA gehören zur Anmeldeebene.

## Vorteile

- **ZFS first-class**: Snapshots, Replikation, Integritäts-Checks, Verschlüsselung aus einer Hand
- **Klare Datenhierarchie**: Pools → Datasets → Freigaben, nachvollziehbar und skriptbar
- **Open Source**: Community Edition vollständig, Updates kostenlos (Enterprise optional)
- **Datenschutz-Bausteine eingebaut**: Snapshot-Tasks, Replication, Cloud Sync, Scrub, Alarme
- **API + CLI mit voller Abdeckung**: JSON-RPC v2.0, `midclaw call`, offizielles Python-Client-Paket
- **Apps und VMs** (SCALE): Plattform für den gesamten Homelab-/Kleinserver-Stack

## Abgrenzung zu anderen Systemen

### TrueNAS vs. Unraid
- **TrueNAS** setzt ZFS mit festen RAID-Topologien (RAIDZ etc.); **Unraid** mixt Einzelplatten mit Paritäts-Schutz und ist flexibler beim Ausbau
- **TrueNAS** ist open source mit vollständiger API; **Unraid** proprietär mit GraphQL-Ergänzung (versionabhängig)
- **Unraid** wirkt beim App-Store (CA) gewachsener; **TrueNAS** punktet bei Snapshots, Replikation und ACL-Tiefe

### TrueNAS vs. Proxmox VE
- **TrueNAS** ist Speicher-Appliance mit VM/Container-Beiwerk; **Proxmox VE** ist Hypervisor mit Storage-Anbindung
- **Proxmox** kann cluster, HA, Live-Migration; **TrueNAS** ist auf einen Storage-Host fokussiert (HA nur Enterprise-Lösungen)
- Häufiges Kombinationsmuster: Proxmox-VMs mit TrueNAS-iSCSI/NFS als Storage

### TrueNAS vs. Synology DSM
- **DSM** ist proprietäre Appliance-Software mit eigenem Paket-Ökosystem und `SYNO.*`-API; **TrueNAS** ist offen mit JSON-RPC-API
- **DSM** glänzt bei Multimedia-/Mobile-Apps, **TrueNAS** bei ZFS-Data-Protection und Enterprise-Storage
- Beide bieten Web-Desktop-artige Oberflächen; TrueNAS bleibt Speicher-zentriert, DSM breiter aufgestellt

## Technische Details

- **Backend**: Middleware-Prozess `middlewared` (Python); CORE auf FreeBSD, SCALE auf Debian-Linux; ZFS im Kernel
- **Database**: Konfiguration der Middleware in einer SQLite-Datei im System-Pool; keine externe DB nötig
- **Frontend**: Angular-SPA mit NG-ZORRO-Komponenten, Live-Status über WebSocket
- **Authentication**: lokale Nutzer (Passwort/2FA), Active Directory, LDAP; API-Keys (benutzerspezifisch), Rollen/Privileges (versionabhängig)
- **Hosting**: Bare-Metal oder VM; Web-UI Port 80/443 (HTTP→HTTPS-Umleitung), SSH/Console-Menü; Updates über UI/Konsolenmenü

## Für wen ist TrueNAS geeignet?

- **Speicher-first-Umgebungen**: Datensicherung, Medienarchive, Virtualisierungs-Storage (NFS/iSCSI)
- **Administratoren mit Datenschutz-Anspruch**: Snapshot-Pläne, Replikation, Scrub-Intervalle
- **SCALE-Nutzer**, die Apps und ein paar VMs auf dem NAS mitlaufen lassen wollen
- **Weniger geeignet** für große VM-Cluster (Proxmox) oder für Mischplatten-Bastler ohne ZFS-Plan (Unraid)
