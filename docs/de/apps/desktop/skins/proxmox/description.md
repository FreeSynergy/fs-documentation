# Proxmox VE - Beschreibung

## Übersicht

Proxmox VE (PVE, Proxmox Server Solutions) ist eine freie Virtualisierungsplattform: Ein Debian-Linux-System mit eigenem Web-Desktop für KVM-/QEMU-Virtualmaschinen, LXC-Container, Storage- und Netzwerkverwaltung. Abos (Enterprise-Repository, Support) finanzieren die Entwicklung; die Software selbst ist GPL-lizenziert und vollständig nutzbar.

## Was Proxmox VE macht

Proxmox VE verwaltet auf jeder **Node** virtuelle Maschinen und Container und fasst mehrere Nodes zu einem **Cluster** zusammen (Corosync, gemeinsamer Konfigurationsspeicher pmxcfs). Die Weboberfläche zeigt links einen Ressourcenbaum (Datacenter → Nodes → VMs/CTs) und rechts Reiter je Objekt: Summary, Hardware, Options, Console, Monitor, Backup, Snapshots. Dazu kommen Storage-Anbindung (LVM-thin, ZFS, CIFS, iSCSI, Ceph), Netzwerk (Bridges, Bonds, VLAN, SDN), Firewall je VM/Node/Cluster, Backups (vzdump, Proxmox Backup Server), Replikation und HA. Eine vollständige REST-API bildet jede UI-Aktion ab.

## Vorteile

- **Zwei Virtualisierungstypen**: Vollvirtualisierung (KVM) und Container (LXC) in einer Oberfläche
- **Cluster eingebaut**: Corosync, HA-Manager, Live-Migration, Replikation ohne Zusatzprodukte
- **Vollständige REST-API**: praktisch jede UI-Aktion ist automatisierbar (Ticket oder API-Token)
- **Storage-Breite**: lokal (LVM-thin, ZFS), über Netz (CIFS, iSCSI, NFS) bis Ceph
- **Debian-Basis**: vertraute Paketverwaltung, Standard-Werkzeuge, kein eigenes Dateisystem-Dogma
- **Proxmox Backup Server**: dediziertes, deduplizierendes Backup-System aus demselben Haus
- **Kein Lock-in**: offene Formate (QCOW2, RAW), API, CLI (`pvesh`)

## Abgrenzung zu anderen Systemen

### Proxmox VE vs. Unraid
- **Proxmox** ist Virtualisierung zuerst, Storagemittel; **Unraid** ist Speicher zuerst mit VM-Anbau
- **Proxmox** clustering- und API-stark; **Unraid** Einzelserver mit GraphQL-Ergänzung (versionabhängig)
- **Unraid** mixt beliebig große Platten mit Parität; **Proxmox** setzt RAID/LVM/ZFS unter den VM-Disks voraus

### Proxmox VE vs. TrueNAS
- **TrueNAS** ist Storage-Appliance (ZFS, Shares, Apps) mit VM-Funktion obendrauf; **Proxmox** ist Hypervisor mit Storage-Anbindung
- **TrueNAS** REST/JSON-RPC-API deckt die UI ab, aber ohne Cluster-Komponenten; **Proxmox** hat Cluster-API, HA, Live-Migration
- Wer primär Dateien teilt, wählt TrueNAS; wer VM-Landschaften betreibt, Proxmox

### Proxmox VE vs. Homarr/Heimdall
- **Homarr/Heimdall** sind Dashboards ohne eigenen Betriebsdienst; **Proxmox** ist das betriebene System selbst
- Homarr/Heimdall können Proxmox nur anzeigen (via API), keine Aktionen mit Cluster-Semantik
- Typische Kombination: Proxmox betreibt die VMs, das Dashboard sammelt die Links

## Technische Details

- **Backend**: Debian Linux; Dämonen `pvedaemon` (API/Web), `pveproxy`, `pve-cluster` (pmxcfs), `pve-manager`; QEMU/KVM und LXC
- **Database**: keine SQL-Datenbank — Konfiguration in Cluster-Dateisystem **pmxcfs** (SQLite-unterfüttert, auf allen Nodes repliziert); Status/RRD in Datenbanken unter `/var/lib`
- **Frontend**: Weboberfläche als JS-App (historisch Sencha ExtJS, Teile neu), Konsolen via xterm.js/noVNC (versionabhängig)
- **Authentication**: Realms `pam` (System), `pve` (eigener Userstore), LDAP/LDAP2, AD, Keycloak/OIDC (versionabhängig); API-Tokens, 2FA (TOTP/Recovery), Rollen/ACL
- **Hosting**: Bare-Metal-Installer oder Debian-Nachrüstung; Web-UI HTTPS Port 8006; SPICE/xterm-Konsolen; Abo- oder Free-Repository

## Für wen ist Proxmox VE geeignet?

- **Homelab- und Kleinserver-Betreiber**, die viele VMs/Container sauber trennen wollen
- **Administratoren mit Cluster-Ambitionen**: HA, Live-Migration, Ceph, Backups aus einer Hand
- **Automatisierer**: REST-API, `pvesh`, Terraform/Ansible-Integrationen
- **Weniger geeignet** für reine NAS-Speicherlandschaften (TrueNAS/Unraid sind dort direkter) und für Nutzer ohne Linux-Grundwissen
