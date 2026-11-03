# TrueNAS - Funktionen

## Übersicht

TrueNAS dreht sich um die **Datenebene**: Pools, Datasets und Freigaben mit ZFS-Werkzeugen (Snapshots, Replikation, Scrub) sowie um den **Dienstestapel** (SMB, NFS, iSCSI, SSH …), dazu Apps und VMs auf SCALE. Alles läuft über die Middleware; Weboberfläche, CLI und API sind gleichwertige Eingänge.

---

## 1. Pools und VDEVs

- **Pool-Assistent**: VDEV-Typen (stripe, mirror, RAIDZ1/2/3), Disk-Auswahl, Format
- **Pool-Verwaltung**: importieren/exportieren, erweitern (add VDEV, replace, detach), Scrub-Jobs
- **SLOG/L2ARC/L2ARC-Cache** und Special VDEVs (versionabhängig)
- **Verschlüsselung** (dataset- oder pool-Ebene, Passphrase/Key, KMIP-Anbindung in Enterprise-Versionen)
- **Disks-Übersicht** mit SMART-Tests, Temperaturempfehlungen und SED-Verwaltung

## 2. Datasets und ZFS-Feinheiten

- **Dataset-Baum** pro Pool mit Create/Rename/Delete/Clone
- **Properties**: Kompression, Recordsize, Quota/Reservation, atime, Snapshots-Vererbung
- **ACL-Editor** (POSIX und SMB/NFSv4-Mischung), "Apply to child datasets"
- **Zvols** für iSCSI/VM-Storage inkl. empfohlenen Blockgrößen (versionabhängig)
- **Klonen, Promoten, Rollback** auf Snapshot-Basis

## 3. Snapshots und Datenschutz

- **Periodic Snapshot Tasks**: Zeitplan, Retention-Schemas, Exclude-Datasets
- **Manual Snapshots**, Holds, Clone, Rollback (UI-geführt)
- **Replication Tasks**: Push/Pull, SSH-Schlüssel-Bindung, inkrementell, Dedup-Optionen (versionabhängig), Verschlüsselungs-Replikation
- **Cloud Sync** (S3, B2, Google Drive, OneDrive …), **Rsync Tasks**, TrueCloud Backup (versionabhängig)
- **Audit-Logs** und **Scrub**-Überwachung als eigene Bereiche

## 4. Freigaben (Shares)

- **SMB**: Time Machine, Shadow Copies (Snapshot-basiert), Presets, ACL-Modi
- **NFS**: Pseudo-Pfade, Clients/Maps, NFSv3/v4-Feinheiten
- **iSCSI**: Targets, Extents (Zvol/File), CHAP-Authentifizierung
- **S3-Objektspeicher**, **WebShare** (HTTP-Zugriff auf Datasets) und FTP (jeweils versionabhängig)
- **Attachments-Ansicht**: welche Datasets/Disks von Freigaben/Apps genutzt werden

## 5. Apps und Container (SCALE)

- **App-Katalog** (offizielle Trains + Community-Trains), Custom-Compose-Erstellung (ab 24.10)
- **App-Verwaltung**: Deploy, Update, Rollback, Logs, Konsolen, certificates/anbindung
- **Docker-Einstellungen**: Pool für App-Images, "Docker-Features", GPU-Passthrough (versionabhängig)
- **Registry-Zugangsdaten** für private_images (versionabhängig)

## 6. Virtualisierung (SCALE, ab 24.10)

- **KVM-VMs** in der UI: Erstellungsdialog, Zvol-/Dataset-Disks, Bridge-Netz, VNC-Konsole
- **Cloud-Init**-Unterstützung und ISO-Verwaltung (versionabhängig)
- Kein Cluster, keine Live-Migration — Einzelhost-Virtualisierung

## 7. Nutzer, Gruppen, Verzeichnisintegration

- **Local Users/Groups** mit Home-Verzeichnis, Shell, SMB/FTP-Flags, 2FA-Status
- **Active Directory** und **LDAP** als Verzeichnisquelle, Idmap-Feinheiten (versionabhängig)
- **ACL-Editor** verknüpft Unix-Rechte, SMB-Rechte und Verzeichnisnutzer
- **API-Keys** pro Benutzer (Rollen/privilege-Rollen, versionabhängig), Sitzungsverwaltung

## 8. Dienste, Netzwerk und System

- **Services-Übersicht**: SMB, NFS, iSCSI, SSH, SNMP, WS-DD, FTP … mit Start/Enable-Toggle
- **Netzwerk**: Interfaces, VLAN, Link Aggregation, IPs, DNS, Static Routes; Netzwerk-Checkin-Dialog (Selbstsperre-Schutz)
- **System**: General (Zeit, Region, UI-HTTPS), NTP, Mail, Alert Settings/Alert Services, Certificates/ACME, Init/Shutdown Scripts, Update, Boot Environments (SCALE)
- **Reporting**: Diagramme (Netdata-Basis, versionabhängig), Exporter, Alert-Integrationen
- **High Availability / Failover** nur auf Enterprise-Hardware (versionabhängig)

## 9. Was TrueNAS NICHT kann

- **Kein VM-Cluster**: VMs (SCALE) sind Einzelhost, kein HA/Migration wie bei Proxmox VE
- **Kein gemischtes Array**: ZFS braucht geplante VDEVs; Einzelplatten-Ad-hoc-Erweiterung wie Unraid ist nicht der Weg
- **Kein klassisches Monitoring-Alerting-Ökosystem** (Prometheus/Grafana nur über Exporter-Anbindungen)
- **Keine eingehenden Webhooks**; Automatisierung ist API-pull/CLI-lastig
- **CORE ohne Docker/VMs** (Apps/VMs sind ein SCALE-Thema)
- **Keine Selbstläufer**: rechenintensive ZFS-Features (Dedup) bleiben Workloads mit viel RAM vorbehalten

## 10. Erweiterungen

- **App-Trains** (offiziell, Community, Enterprise) und Custom-Apps per Docker Compose
- **Plugins** nur noch historisch in CORE (Jail-System wurde abgelöst) — Migrationspfad zu SCALE-Apps
- **S.M.A.R.T.**, **syslog forwarding**, **SNMP/Graphite/Prometheus**-Exporte (versionabhängig)
- **Community-Werkzeuge**: py-nas (Python-WebSocket-Client), Ansible-Module `community.general.truenas_*`, Dashboard-Widgets (Homarr/Homepage)
- **Konsolenmenü + `midclaw`** für alles, was die UI nicht abbildet (versionabhängig)

---

## Vergleich mit den Nachbarsystemen

| Funktion | TrueNAS | Unraid | Proxmox VE |
|----------|---------|--------|------------|
| Dateisystem/Array | ZFS (VDEV-Plan) | Mix-Array + Parität | ZFS/LVM frei wählbar |
| Freigaben | SMB/NFS/iSCSI/S3 (Kern) | SMB/NFS (Shares) | Gast/Storage-only |
| Snapshots/Replikation | eingebaut, tief | ❌ (nur Drittwerkzeuge) | Snapshots/Replikation für VMs |
| Apps/VMs | Apps + VMs (SCALE) | Apps + VMs (Lizenz) | VMs/Container = Kernzweck |
| API | JSON-RPC v2.0 + CLI | GraphQL (neu) | REST `/api2/json` |

---

## Siehe auch

- [menu.md](menu.md) - Navigation und Dialoge nach Rolle
- [structure.md](structure.md) - UI-Aufbau, Panels, Jobs
- [api.md](api.md) - API v2.0, API-Keys, CLI
- [shortcuts.md](shortcuts.md) - Tastatursteuerung
