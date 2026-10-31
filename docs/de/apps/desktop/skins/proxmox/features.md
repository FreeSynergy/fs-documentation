# Proxmox VE - Funktionen

## Übersicht

Proxmox VE besteht aus vier Ebenen: **Virtualisierung** (VMs, Container), **Infrastruktur** (Storage, Netzwerk, Firewall), **Betrieb** (Backup, Replikation, HA, Updates) und **Verwaltung** (Benutzer, Rechte, API). Die Web-UI bildet alle Ebenen ab; jede Aktion existiert parallel in der REST-API.

---

## 1. KVM-/QEMU-Virtualmaschinen

- **Erstellungsassistent**: Guest-OS-Typ, CD/ISO, Diskbus, QCOW2/RAW, Thin/Thick
- **Hardware-Reiter**: CPU-Typ/sockets/cores, RAM + Ballooning, Netzwerk (Modelle, VLAN-Tag), Disks, PCIe-Durchreichung, GPU (versionabhängig)
- **Cloud-Init** für Vorlagen: Hostname, Nutzer, SSH-Keys, Netzwerkkonfiguration
- **Snapshots** (inkl. Memory-Snapshots), **Clones** (voll/Linked), **Vorlagen** (Templates)
- **QEMU-Agent** für saubere Shutdowns und IP-Anzeige
- **Backup-Modus** pro VM: Stop, Snapshot, suspend (mit Quiesce, versionabhängig)

## 2. LXC-Container

- **Unprivilegierte Container** als Standard, privilegierte optional
- **Template-Abruf** direkt aus der UI (Debian, Ubuntu, Alpine, TurnKey …)
- **Ressourcenlimits** (CPU, RAM, Swap), Feature-Auswahl (Nesting, FUSE, keyctl)
- **Konsolen**: Browser (xterm.js) und `pct` auf der Node (versionabhängig)
- **Push/Pull-Migration** zwischen Nodes (Shared Storage nötig; sonst Replikation)

## 3. Storage

- **Typen**: Directory, LVM, LVM-thin, ZFS (+ RAID-Level), BTRFS (versionabhängig), CIFS/SMB, NFS, iSCSI, RBD (Ceph), Proxmox Backup Server
- **Storage-Pools** mit Zuweisung pro Node und Inhaltstyp (Disk-Images, ISO, Backup, Container)
- **Disk-Verwaltung** im VM-Reiter: Resize, Move (Storage-Migration), Detach, Backup-Flag
- **IO-Throttling**, Spin-down-Flags, Cache-Modi pro Disk

## 4. Netzwerk

- **Linux-Bridges** pro Node (vmbr0 …), Ports, VLANs, Bonds (LACP), MLAG (versionabhängig)
- **SDN** (Virtual Network): Zonen (Simple, VLAN, VXLAN, QinQ), IPAM, Subnetze (seit 8.x, versionabhängig)
- **IPv4/IPv6-Konfiguration**, DNS, Routen über den Netzwerk-Reiter
- **Firewall** auf drei Ebenen: Datacenter, Node, Gast (Rules, Aliases, Rate-Limits, DHCP/RA-Guard)

## 5. Cluster und Hochverfügbarkeit

- **Corosync-Cluster** mit pmxcfs (Konfiguration repliziert), Quorum-Modell, Watchdog-Automatik
- **HA-Manager**: HA-Ressourcen, Gruppen, Fencing, Status „stopped/started“
- **Live-Migration** (online) und Resize-orientierte Offline-Migration
- **Ceph-Integration**: Mon/OSD/MDS über UI anlegen, RBD-Storage, Dashboard (versionabhängig)
- **Cluster-Ressourcenübersicht** mit Suche, Tags und Filtern

## 6. Backup und Replikation

- **vzdump** in Backup-Jobs (Zeitplan, Storage, Aufbewahrung, E-Mail) oder direkt am Objekt
- **Proxmox Backup Server**: inkrementell, deduplizierend, Verschlüsselung, Restore/Verify
- **Snapshots** (VM) und **Container-Snapshots**; **Replikation** als Zeitplan mit Point-in-Time-Kopien
- **Restore** auf andere Nodes/Storage, inkl. „als neue VMID“

## 7. Betrieb und Updates

- **Repositories** (Enterprise/No-Subscription/Test), Paketupdates über Reiter *Updates*
- **Subscription-Management**, Support-Info, **Subscription-Reminder** abschaltbar
- **Metric Server** (InfluxDB/Graphite-Export) für Monitoring-Abgriff (seit 8.1, versionabhängig)
- **Benachrichtigungen** (Reiter Notifications: Matching,.targets Mail/Jabber/SMS, versionabhängig)
- **Konsolen**: Node-Shell und Terminal in der UI; `pvesh`, `qm`, `pct`, `pvecm`, `pvesm` auf der Konsole

## 8. Benutzer, Rechte und API-Zugang

- **Realms**: `pam`, `pve` (eigener Store), LDAP/LDAP2, AD, Keycloak/OIDC (versionabhängig)
- **Zwei-Faktor**: TOTP, Recovery-Keys (Version je nach Release)
- **Rollen und ACL** granular bis auf VM-Ebene; Pools als Rechte-Sammelbecken
- **API-Tokens** mit Ablauf, Node-Bindung und Rechten — Grundlage für Skripte und Terraform

## 9. Was Proxmox VE NICHT kann

- **Kein klassisches NAS**: Dateifreigaben (SMB/NFS für Clients) sind nicht die Kernaufgabe — Storage wird für VMs verwalten, nicht für Nutzer
- **Kein eingebauter Monitoring-Stack**: Metriken gehen an externe Systeme (Metric Server, Netdata-Integrationen), Alerts sind rudimentär
- **Keine Webhooks**: weder eingehend noch ausgehend dokumentiert
- **Live-Migration nur mit Shared Storage**; ohne Ceph/LVM & Co. hilft nur Replikation
- **LXC hat keine Live-Migration im klassischen Sinn** und keinen vollen Kernel-Gast
- **Kein Mandanten-Selfservice**: Rechte ja, aber kein Cloud-Portal (dafür z. B. nette externe Projekte)

## 10. Erweiterungen

- **Proxmox Backup Server** und **Proxmox VE Backup** als Produktfamilie
- **cloud-init**, **QEMU-Agent**, **qga-Skripte** für Gastautomatisierung
- **Infrastructure as Code**: Terraform-Provider (bpg/proxmox), Ansible-Sammlung `community.proxmox`
- **Community-Werkzeuge**: Proxmox Helper Scripts (Container-/VM-Templates), pve-exporter für Prometheus, Dashboard-Bibliotheken
- **Eigene Integrationen** über die REST-API (siehe [api.md](api.md)) und Hooks (versionabhängig)

---

## Vergleich mit den Nachbarsystemen

| Funktion | Proxmox VE | Unraid | TrueNAS |
|----------|------------|--------|---------|
| Kernaufgabe | Virtualisierung + Cluster | Flexible Speicher-Array + Apps | ZFS-Speicher + Freigaben |
| VMs | KVM + LXC, Cluster/HA | KVM (einzeln, versionabhängig) | KVM (einzeln, ab 24.10) |
| API | vollständige REST-API | GraphQL (neu) | JSON-RPC v2.0 |
| Dateifreigaben | für Gäste/Storage | SMB/NFS Shares | SMB/NFS/iSCSI/S3 (Kernzweck) |
| Cluster | Corosync, HA, Ceph | ❌ | HA nur Enterprise (versionabhängig) |

---

## Siehe auch

- [menu.md](menu.md) - Ressourcenbaum und Reiter im Detail
- [structure.md](structure.md) - UI-Aufbau und Konsolen
- [api.md](api.md) - REST-API, Tokens, `pvesh`
- [shortcuts.md](shortcuts.md) - Tastatursteuerung
