# TrueNAS - Menüpunkte

## Übersicht

TrueNAS (SCALE, aktuelle Versionen) navigiert über eine **linke Sidebar** mit klar benannten Bereichen, eine **globale Suchleiste** oben und ein **Benutzer-/Systemsymbolmenü** rechts oben. Die Punkt-Reihenfolge ändert sich über die Major-Releases (23.10 → 24.04 → 24.10 → 25.x); die Grundgruppe bleibt gleich. CORE (FreeBSD) zeigt dieselben Speicherpunkte ohne Apps-/VM-Zweige.

## Navigationspunkte (Sidebar)

### 1. Dashboard
- **Funktion**: Startseite mit Statuskarten
- **Details**: Pool-Auslastung, laufende Dienste, Apps, Alarme, Verknüpfungen; Karten aus-/einblendbar

### 2. Datasets
- **Funktion**: Dataset-Baum aller Pools
- **Details**:
  - **Create Dataset/Zvol**: Assistent (Name, Casesensitive, Compression, Quota, ACL-Preset)
  - Kontextaktionen je Dataset: Edit, Delete, Snapshots, Clone, Encryption, Quotas, Applications
  - Spalten für Nutzung, Free, Kind (Dataset/Zvol)

### 3. Pools
- **Funktion**: Pool-Verwaltung
- **Details**: Import/Export, Add, Manage (VDEVs), Scrub Tasks, Upgrade, ZFS-Statusmeldungen
- **Disks** (gleicher Bereich oder eigener Punkt, versionabhängig): SMART, Wipe, Sed, Overprovisioning

### 4. Shares
- **Funktion**: Freigabe-Übersicht mit Protokoll-Abschnitten
- **Details**: SMB (Time Machine, Samba-Extras), NFS, iSCSI (Targets/Extents), S3-Buckets, WebShare, FTP (versionabhängig); Attachments-Ansicht

### 5. Apps (SCALE)
- **Funktion**: App-Katalog und installierte Container
- **Details**:
  - **Discover**: Katalog nach Kategorie/Train, Detailseite mit Config-Formular
  - **Installed**: Status, Update, Rollback, WebUI-Link, Logs, Console
  - **Settings**: App-Pool, "Docker-Ansicht", Registry-Zugänge, Custom-Compose

### 6. Virtualization / VMs (ab 24.10)
- **Funktion**: KVM-VMs verwalten
- **Details**: Create VM (RAM, CPU, root-Device auf Dataset/Zvol, Bridge), VNC-Konsole, Cloud-Init, ISO-Auswahl

### 7. Network
- **Funktion**: Netzwerkkonfiguration
- **Details**: Interfaces (DHCP/Static), VLAN, Link Aggregation, Static Routes, DNS; Checkin-Dialog mit Countdown gegen Selbstsperre

### 8. Services
- **Funktion**: Dienste-Tabelle mit Status/Enable
- **Details**: SMB, NFS, iSCSI, SSH, SNMP, WS-DD, FTP; je Dienst Edit-Dialog (versionabhängig: WS-DD, S3)

### 9. Data Protection
- **Funktion**: Sicherungs- und Replikationsbereiche
- **Details**:
  - Periodic Snapshot Tasks, Replication Tasks, Cloud Sync Tasks, Rsync Tasks
  - TrueCloud Backup Tasks (versionabhängig), Resilver/Scrub-Einstellungen
  - Snapshot-Browser für manuelle Snapshots/Rollback

### 10. Credentials
- **Funktion**: Zugangs- und Schlüsselmaterial
- **Details**: Certificates (CSR, ACME-DNS-Authenticator), SSH Key Pairs, SSH Connections, privileged SSH login, Backup-Credentials (Cloud-Anbieter), API-Keys (auch über Benutzermenü)

### 11. Local Users / Local Groups
- **Funktion**: Konten und Gruppen
- **Details**: User anlegen (Home, Shell, SMB/FTP), 2FA-Rücksetzung, AD/LDAP-Status (Directory Service)

### 12. Reports / Logs
- **Funktion**: Diagramme und Protokolle (Punkt-Namen versionabhängig)
- **Details**: Reporting-Dashboards (Netdata-Basis), Alert-Listen, General/Audit Logs, Exporter-Konfiguration

### 13. System
- **Funktion**: Systemeinstellungen
- **Details**:
  - **General**: Zeitzone/Land, UI-Adresse/Port/Zertifikat, Sprach-/UI-Optionen
  - **NTP**, **Mail**, **Alert Settings/Alert Services**
  - **Advanced**: Syslog, Init/Shutdown Scripts, SSH-Feinheiten (versionabhängig)
  - **Boot**: Boot Environments aktivieren/klonen (SCALE)
  - **Update**, **Support/Tickets** (Community/Enterprise, versionabhängig)
  - **Failover/HA** nur Enterprise (versionabhängig)

## Symbolmenü oben rechts

- **Jobs-Symbol**: laufende/abgeschlossene Middleware-Jobs mit Fortschritt
- **Glocke**: Alarme und Alert-Historie
- **Benutzersymbol**: Abmelden, 2FA, **API Keys** (anlegen/verwalten), Sitzungen

## Kontext-Menüs und Dialoge

- **Dataset-Zeile**: Drei-Punkte-Menü mit Snapshots, Clone, Delete, Details, Applications
- **App-Karte**: WebUI öffnen, Update, Rollback, redeploy, delete (mit Data-Optionen)
- **Pool-Karte**: Manage, Export, Resize, Statusmeldungen
- **Job-Eintrag**: Logs öffnen, abbrechen (sofern Stoppbar)
- **Suchleiste oben**: findet Menüpunkte, Datasets, Freigaben, Apps (Globale Suche)

## Menüs nach Rolle

### Admin (Standard bei Erststart)
- Alle Sidebar-Punkte, System/Advanced, API-Key-Verwaltung, Update

### Nicht-privilegierter Benutzer (Rollen/Privileges, versionabhängig)
- Sichtbare Bereiche je nach Rights-Set; keine Dienste-/System-Editierung

### AD/LDAP-Gruppe mit Rechten
- Anmeldung mit Verzeichniskonto, Menüumfang über zugewiesene Rollen

### Konsolen-/API-Zugang
- Das Konsolenmenü am Server bietet Wartungspunkte (Netz, Shell, Import) unabhängig von UI-Rollen

## Shortcuts

Tastatursteuerung (Formulare, Suche, Konsolenmenü) ist in [shortcuts.md](shortcuts.md) beschrieben, inklusive der als nicht vorhanden markierten Kombinationen.
