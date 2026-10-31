# Unraid - Funktionen

## Übersicht

Unraid dreht sich um vier Bausteine: das **Array** (Speicher mit Parität), **Freigaben und Benutzer**, **Container/VMs** sowie der **Erweiterungsbaumarkt** aus Community Applications und Plugins. Fast alles wird über die Tabs der Weboberfläche gesteuert; die Einstellungen wandern als XML auf das USB-Bootmedium.

---

## 1. Storage-Array

- **Gemischte Laufwerke**: Datenlaufwerke unterschiedlicher Größe/Hersteller in einem Array
- **Dedizierte Parität**: ein oder zwei Paritätslaufwerke (versionabhängig), Schutz vor Einzel- bzw. Doppellaufwerksausfall
- **Laufwerksweiser Ausbau**: neue, größere Platten ersetzen die größten Datenlaufwerke
- **Cache-Pools**: schnelle SSD-/NVMe-Laufwerke (auch ZFS-Pools, versionabhängig) als Schreib- und App-Zwischenschicht
- **Parity Checks und Corrections** als geplante oder manuelle Läufe mit Fortschrittsanzeige
- **Start/Stop des Arrays** über die Weboberfläche, inkl. Umbaubetrieb (Array gestoppt, Platten getauscht)

## 2. Freigaben (Shares)

- **User Shares**: Ordner-Freigaben, deren Blöcke automatisch über die Array-Laufwerke verteilt werden
- **Sicherheitsstufen** pro Share: `public` (ohne Login), `secure` (optional), `private` (nur mit Login)
- **SMB- und NFS-Freigaben** für Windows-, macOS- und Linux-Clients; SMB-Optionen (VSS/Shadow Copy versionabhängig)
- **Upstream/Downstream-Verhalten**: neue Dateien wandern auf den Cache, altern blocks wandern ins Array (versionabhängig)

## 3. Benutzer und Rechte

- **Lokale Benutzer** mit Passwörtern, verwaltet im Tab *Users*
- **Samba-/Unix-Rechte** darunter, Freigaben mit public/secure/private daran gekoppelt
- **WebUI-Zugriff** unterscheidet unangemeldet, eingeschränkt und Administrator (versionabhängig)
- **Unraid Connect** als optionales Konto für Remote-UI, Updates und Ferndiagnose

## 4. Docker

- **Docker-Engine** mit eigener virtueller Disk (`docker.img`) oder Directory-Mode auf einem Pool (versionabhängig)
- **Vorlagen-Katalog** im Tab *Docker*: fertige App-Template-Formulare (Pfade, Ports, Variablen)
- **Container-Verwaltung**: Start/Stopp/Neustart, Logs, WebPUI-Buttons, Update-Prüfung
- **Compose-Projekt** für mehrere Container (neuere Versionen, versionabhängig)

## 5. Virtuelle Maschinen

- **libvirt/KVM-VMs** im Tab *VMs*: Erstellungsassistent, DISK-, CPU-, RAM-, Netzwerk- und GPU-Durchreichung
- **webVNC-Konsole** im Browser, optional RDP nach Installation
- **Lizenzpflicht**: VM-Funktionen an höhere Lizenzstufen gebunden (versionabhängig)
- **QCOW2/RAW-Images** auf Array oder Cache, Snapshots nur eingeschränkt (kein imagebasiertes Backup-Werkzeug eingebaut)

## 6. Apps und Plugins

- **Community Applications (CA)**: Suchbarer Store für Container-Vorlagen, Plugins und Templates
- **Plugin-Sammlung** (Dynamix, Drive Buttons, Unassigned Devices, Web terminal, Language/Translations u. v. m.)
- **Plugin-Updates** zentral im Tab *Plugins*, Deinstallation räumt meist mit auf
- **Eigene Templates/Plugins**: XML-basierte Vorlagen und Bash/PHP-Plugins, Community-getragen

## 7. Werkzeuge und Überwachung

- **System-Informationen und Logs** im Tab *Tools* (syslog, SMART-Werte je nach Plugin)
- **Scheduler**: Parity Check, Mover (Cache→Array), disk spin-down, Eigen-Cron (versionabhängig)
- **Benachrichtigungen**: E-Mail und **Webhooks** für Statusereignisse (ab Version 6.12, versionabhängig)
- **Dynamix-Plugins** liefern Dashboards, Themes und Statusleisten nach

## 8. Konfiguration

- **XML-Grundgerüst** auf dem USB-Stick: `/boot/config` (Shares, Identifikation, Super-Metadaten)
- **Management Access**: HTTP/HTTPS, Zertifikate, Port, optionale WebUI-Anmeldung
- **Sprache/Themes** über Plugins; Grund-UI ist primär englisch
- **Backups**: USB-Bootmedium kopieren (versteckt auch die Lizenzdatei) — defekter Stick ohne Backup bedeutet Neuinstallation mit Lizenzfall

## 9. Was Unraid NICHT kann

- **Kein Cluster, kein HA**: ein Server, ein Array — Replikation über Systeme hinweg fehlt eingebaut
- **Kein klassisches RAID**: Ausfall eines Datenlaufwerks kostet dessen Inhalte (Parität rekonstruiert weiter), kein RAID-10-Verhalten
- **Keine offizielle Kern-REST-API** über Jahre hinweg; Automatisierung lief über Dateien und Plugins, heute GraphQL (versionabhängig)
- **Keine Snapshot-/Replikationswerkzeuge** wie TrueNAS; Backups bleiben Drittanbieter-Werkzeugen oder Plugins vorbehalten
- **Keine echte Mehrmandantenfähigkeit** und keine rollenbasierten Rechte wie Proxmox VE
- **Proprietär**: Quellcode der Kernkomponenten nicht offen, Lizenzkosten ab der Testphase

## 10. Erweiterungen

- **Community Applications** als zentrale Quelle für Container und Plugins
- **Unraid Connect** für registrierte Geräte, Fernzugriff und Update-Kanäle
- **GraphQL-API und `unraid-api` CLI** in aktuellen Versionen (siehe [api.md](api.md))
- **Drittanbieter-Bibliotheken**: `pyunraid` (Python-Client für die WebUI-Endpunkte), Community-Dashboards mit Unraid-Widgets
- **Eigene Skripte** über `go`-Hook-Dateien (`/boot/config/go`, versionabhängig) und Init-Skripte auf dem Stick

---

## Vergleich mit den Nachbarsystemen

| Funktion | Unraid | TrueNAS | Proxmox VE |
|----------|--------|---------|------------|
| Lizenz | proprietär | Open Source (Enterprise-Optionen) | Open Source (Abo-Optionen) |
| Dateisystem/Array | Mix-Array + Parität, ZFS-Cache möglich | ZFS durchgängig | ZFS/LVM auf Node-Ebene |
| Docker/Apps | CA-Store, Vorlagen | Apps-Katalog (SCALE) | Container-Unterstützung (LXC/Proxmox VE 8, versionabhängig) |
| VMs | KVM, einzeln | KVM (ab 24.10), einzeln | KVM + LXC, Cluster/HA |
| API | GraphQL (neu), sonst Dateien | JSON-RPC v2.0, CLI | vollständige REST-API |

---

## Siehe auch

- [menu.md](menu.md) - Tabs, Dialoge und Rollen
- [structure.md](structure.md) - Web-UI-Aufbau
- [api.md](api.md) - GraphQL, API-Keys, Webhooks
- [shortcuts.md](shortcuts.md) - Tastatursteuerung
