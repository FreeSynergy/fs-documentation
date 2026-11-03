# Proxmox VE - Menüpunkte

## Übersicht

Proxmox VE arbeitet mit einem **Ressourcenbaum links** und **Reitern im Hauptbereich rechts**. Der Baum folgt der Reihenfolge Datacenter → Nodes → VMs/Container → Unterobjekte. Welche Zweige und Reiter sichtbar sind, hängt von Rechten (Rollen/ACL) ab — Leseberechtigte sehen Menüs ohne Aktionsbuttons.

## Datacenter-Ebene

### 1. Datacenter → Summary
- **Funktion**: Gesamtübersicht über Nodes, VMs, Container, Ressourcen
- **Details**: Suchfeld, Tags, Filter, Spalten (Status, IP, Uptime … versionabhängig)

### 2. Datacenter → Cluster / Corosync
- **Funktion**: Clusterzusammensetzung und Quorum
- **Details**: Nodes, Vote-Devices (versionabhängig), Cluster-Status

### 3. Datacenter → Permissions
- **Funktion**: Rechteverwaltung
- **Details**:
  - **Users**: anlegen/sperren, Realm, Passwort, 2FA
  - **Realms/Domains**: pam, pve, ldap, ldap2, ad, keycloak (versionabhängig)
  - **API Tokens**: Token je Benutzer, Rechten, Ablauf, Node-Bindung
  - **ACL/Rollen**: Rechte auf Pools, Nodes, VMs verteilen

### 4. Datacenter → Storage
- **Funktion**: Storage-Pools anlegen und den Nodes zuweisen
- **Details**: Typ (Directory, LVM-thin, ZFS, CIFS, iSCSI, RBD, PBS …), Inhaltstypen, Zuordnung

### 5. Datacenter → Backup / Replication
- **Funktion**: Backup-Jobs (vzdump/PBS) und Replikations-Jobs
- **Details**: Zeitpläne, Storage, Aufbewahrung, E-Mail; Replikation mit Retention und Snapshots

### 6. Datacenter → HA (Resources, Groups, Status)
- **Funktion**: Hochverfügbarkeits-Management
- **Details**: Ressourcen hinzufügen, Gruppen, Fencing-Modus, Statusanzeige

### 7. Datacenter → Ceph
- **Funktion**: Ceph-Cluster-Verwaltung (versionabhängig, nur bei Ceph-Nutzung)
- **Details**: Mon, OSD, Pools, RBD, Dashboard-Links

### 8. Datacenter → Metric Server / Firewall / Subscription
- **Funktion**: Metrik-Export (InfluxDB/Graphite), Firewall-Defaults, Abo-Status (versionabhängig)
- **Details**: Reiter je Themenpunkt wie bei Nodes/Gästen

## Node-Ebene (Beispiel `pve1`)

### 9. Node → Summary / Console / System
- **Funktion**: Node-Status, Shell, Grundsätzliches
- **Details**: Last, Uptime; **Shell** (xterm.js) = echte Linux-Shell im Browser; System: Abonnement, Support, Zertifikate, Einstellungen

### 10. Node → Network
- **Funktion**: Bridges, Bonds, VLAN, SDN, DNS
- **Details**: Reiter Network (vmbr-, bond-Objekte), DNS, SDN (Zonen, IPAM, versionabhängig)

### 11. Node → Storage / Disks
- **Funktion**: Lokale Storage und Blockgeräte (versionabhängig)
- **Details**: ZFS-/LVM-Pools anlegen, Festplatten-SMART, iSCSI-Discovery

### 12. Node → Backup / Replication / Snapshots
- **Funktion**: node-lokale Jobs und Point-in-Time-Replikate
- **Details**: wie Datacenter-Jobs, aber gefiltert auf die Node

### 13. Node → Software / Updates / Services
- **Funktion**: Repositories, Paketupdates, Systemdienste (seit 8.2, versionabhängig)
- **Details**: Reiter Repositories (Enterprise/No-Sub/Test), Updates (Package-Liste), Services (Neustart)

### 14. Node → Firewall / Terminals
- **Funktion**: Node-Firewall, Konsole, KVM-Konsole des Hosts
- **Details**: Regeln, Aliases, Options; **Terminal** und **Shell** getrennt

## VM-/Container-Ebene

### 15. VM → Summary / Console / Monitor
- **Funktion**: Status, Browser-Konsole, Echtzeitdiagramme
- **Details**: Console (noVNC/xterm.js), Tastatur-Sonderaktionen über Konsolen-Menü; Monitor: CPU/RAM/Netz-Diagramme

### 16. VM → Hardware
- **Funktion**: Geräte der VM bearbeiten
- **Details**: Add (Disk, CD/DVD, Network, USB, Serial, Cloud-Init-Drive), Edit/Detach, CPU/RAM hier nur bei älteren Versionen (sonst Options)

### 17. VM → Options
- **Funktion**: Verhalten und Metadaten
- **Details**: Geräte-Autostart, Boot-Reihenfolge, Agent, Tags, Beschreibung, Migration-Verhalten, Resync

### 18. VM → Backup / Snapshots / Clone / Templates
- **Funktion**: Sicherungszweige am Objekt
- **Details**: Backup now, Restore; Snapshot take/revert; Clone (voll/Linked); Convert to Template

### 19. VM → Cloud Init / DNS / Firewall / Unmount ISO
- **Funktion**: Gastvorbereitung und Sicherheit
- **Details**: user/SSH-Keys/Netz in Cloud-Init, DNS-Suffix, Gast-Firewall, CD-ROM-Auswurf

## Kontext-Menüs und Dialoge

- **Rechtsklick im Baum**: Kopieren (ID), je nach Objekt weitere Aktionen (versionabhängig)
- **Obere Buttonleiste**: Start, Stop (Notaus), Reboot, Shutdown, Reset, Suspend/Resume, Migrate, Console (Dropdown: noVNC/xterm.js/SPICE)
- **Task-Panel**: laufende Aktionen als Liste, Doppelklick = Details
- **Suchleiste oben**: findet VMs/Container/Nodes über Name, ID, Tags, IP

## Menüs nach Rolle

### Administrator
- Volle Datacenter-Baumstruktur, alle Reiter und Buttons

### Lese-/Monitoring-Rolle
- Baum sichtbar, Reiter sichtbar, keine Start/Stop-/Edit-Buttons

### VM-Operator (delegierte Rechte)
- zugewiesene VMs vollständig, andere VMs ausgeblendet oder nur Summary

### Konsolen-Nutzer (VNCProxy)
- nur Console-Zugriff auf zugewiesene Gäste

## Shortcuts

Tastatursteuerung inklusive Konsolen-Tasten ist in [shortcuts.md](shortcuts.md) beschrieben; als nicht vorhanden markierte Kombinationen stehen dort ebenfalls.
