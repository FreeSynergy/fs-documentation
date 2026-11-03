# Synology DSM - Funktionen

## Übersicht

DSM gliedert sich in vier Funktionsbereiche: **Speicher und Datendienste**, **Benutzer und Rechte**, **Pakete und Anwendungen** sowie **Sicherheit, Sicherung und Überwachung**. Das Desktop-Portal ist die gemeinsame Oberfläche; jede Funktion gehört zu einem Paket oder zur Systemsteuerung.

---

## 1. Speicher und Volumes

- **Storage-Pools** aus HDD/SSD mit RAID-Typen (SHR, SHR-2, RAID 0/1/5/6/10)
- **Volumes** mit Dateisystem Btrfs oder ext4, Pool-Erweiterung und Cache-Beschleunigung (SSD-Cache)
- **Speicher-Verwaltung** als zentrale Anwendung: Laufwerks-Gesundheit, SMART-Tests, Volume-Kapazität, Storage-Warnungen
- **Btrfs-Funktionen**: Datenintegritätsprüfung, Snapshot-Plansätze, Kontingente, Datenoptimierung
- **Laufwerks-Hotplug**, Hybrid-Setup aus Volume und Virtuellem Storage (Virtual Machine Manager)
- **System Pulse / Desktop-Widgets**: CPU-, RAM-, Netzwerk-, Volume- und Temperaturwerte direkt auf der Desktop-Fläche

## 2. Freigaben und Datendienste

- **Freigegebene Ordner** mit Rechtevergabe, Papierkorb, verschlüsselten Freigaben und Datenkomprimierung
- **Protokolle**: SMB/CIFS, NFS, AFP, FTP/SFTP, WebDAV, iSCSI/LUN
- **Datei-Übertragung** im Browser über **File Station**: Vorschau, Umbenennen, Kopieren/Verschieben, Komprimieren, Hoch- und Herunterladen mit Aufgabenliste
- **Team-Ordner und Dateien mit Versionskontrolle** (Synology Drive), Freigabelinks mit Ablauf und Passwort
- **Mediendurchlauf**: Medien-Indizierung, Transkodierung, Web-Zugriff (Media Server, Video Station, Audio Station)
- **Universal Search** als indexierte Suche über Freigaben und Paketinhalte

## 3. Benutzer, Gruppen und Rechte

- **Lokale Konten** mit Kennwortrichtlinien, Ablauf, Anmeldeversuchen und 2FA (TOTP)
- **Gruppen** mit primärer Gruppe, Rechteübertrag und Kontingent
- **Domänen-Anbindung**: LDAP und Windows AD, Single-Sign-On für Freigaben
- **Paketrechte**: je Anwendung darf eine Gruppe/Person nutzen oder verwalten
- **Gast-Konto** und ** application-Gruppe** für dienstkonten
- **Schutz des Admin-Kontos** (Umbenennen, Kennworthistorie, 2FA-Pflicht) und **Konto-Schutz** mit IP-Sperre nach fehlgeschlagenen Anmeldungen
- **Protokolle**: Anmeldung, Freigabezugriff, Administration, Verbindung (Verbindungsinstrument)

## 4. Pakete und Anwendungen

- **Paketzentrum**: Katalog, automatische Updates, erzwungene Updates, manuelle Installation von `.spk`-Paketen, Paketquellen Dritter
- **Wichtige Pakete**: Synology Drive Server, Snapshot Replication, Active Backup for Business, Universal Search, Media Server, Video/Audio Station, Mail Server/Plus, Chat, Directory Server, VPN Server, Web Station, Database Server, Virtual Machine Manager, Container Manager (Docker/OCI)
- **Paketverwaltung**: Start/Stopp, Autostart, Ressourcenanzeige, Deinstallation mit Datenüberrest-Kontrolle
- **Aufgabenplanung**: Zeitpläne, Bash-/PowerShell-Skripte, Ereignisgebundene Aufgaben
- **Schnellstart (QuickStart)**: geführte Ersteinrichtung und Aufgaben-Kurzanleitungen direkt im Portal

## 5. Sicherung und Wiederherstellung

- **Snapshot Replication**: zeitplangesteuerte Snapshots, Replikation auf ein zweites NAS, Verzeichnis-Replikation
- **Active Backup for Business**: Sicherung von PCs, Servern, VMs und mobilen Geräten
- **Datensicherung** (früher Hyper Backup): Sicherung von Freigaben und Konfiguration auf lokale Ziele, NFS, WebDAV, S3, Synology C2
- **Schreibgeschützte Versionen** und Verschlüsselung für Sicherungsziele
- **Systemkonfigurations-Sicherung** über die Systemsteuerung, Wiederherstellung nach Update

## 6. Netzwerk, Fernzugriff und Dienste

- **Schnittstellenverwaltung** mit Link Aggregation, VLAN, DNS, statischen Routen
- **QuickConnect**: verschalteter Zugriff ohne öffentliche Adressen, mit eigenem Port-Management
- **Reverse-Proxy-Assistent**: Weiterleitungen, Zertifikate (Let's Encrypt), HTTP/2
- **Firewall** je Profil, Geo-IP-Blocklisten, Auto-Block, DoS-Schutz
- **VPN-Server** (OpenVPN, WS, PPTP/L2TP), VPN-Client
- **DSM-Ports**: Standard **5000/5001**, weitere Ports je Paket; Umschaltung und Redirect in der Systemsteuerung

## 7. Überwachung und Benachrichtigung

- **Ressourcenmonitor**: Auslastung, Prozesse, Dienste, Netzwerk, Storage mit Verlaufsdiagrammen
- **Protokoll-Center**: Ereignisprotokolle, Windows-Log-Zusammenführung, Syslog-Empfang
- **Benachrichtigungen**: E-Mail, Synology Notification (Push), SMS (Anbieterabhängigkeit), Benachrichtigungsglocke im Portal
- **Speicherwarnungen**: SMART, defekte Blöcke, Volume-Annäherung an die Kapazitätsgrenze, RAID-Konsistenz
- **Datenschutz-/Sicherheitsprüfungen**: Sicherheits-Assistent, Sicherheitsprüfung, Sicherheits-Guard (Malware-Scan)

## 8. Was DSM NICHT kann

- **Kein freier Betriebssystem-Ausbau**: DSM läuft offiziell nur auf Synology-Hardware, Pakete sind signiert
- **Kein öffentliches Plugin-System** für das Desktop-Portal: eigene Oberflächen sind nicht vorgesehen
- **Kein frei zugängliches API-Design**: `SYNO.*` ist in Paket-Entwicklerhandbüchern dokumentiert, aber nicht als stabile, versionierte Produkt-API zugesagt
- **Kein Monitoring-Stack wie Prometheus/Grafana**: Verläufe sind lokal und begrenzt, Alerting elementar
- **Keine Mandantenfähigkeit im Dashboard-Sinn**: ein System, eine Kontenlandschaft
- **Keine beliebig tiefgreifende Automatisierung der Oberfläche**: Pakete mit eigener Logik (z. B. Drive, Surveillance) haben eigene, teils nicht dokumentierte Endpunkte
- **Kein Ersatz für ein Dashboard-Portal**: Verknüpfungen zu Dritt-Diensten sind möglich, aber ohne Widget-Editor wie bei Homarr oder Dashy

## 9. Erweiterungen und Integrationen

- **Paketentwicklung**: `.spk`-Pakete mit eigenem Web-UI und eigener API (Entwicklerhandbuch von Synology)
- **Web Station** betreibt PHP-/Node-Anwendungen, die über `entry.cgi` auf DSM-Funktionen zugreifen können
- **Container Manager** bindet Docker-/OCI-Container ein; Ports erscheinen im Portal unter Fenster/Ports
- **API-Aufrufe aus Skripten**: Bash, PowerShell, Python, Go – Details siehe [api.md](api.md)
- **Third-Party-Integrationen**: Home-Assistant- und Monitoring-Skripte nutzen regelmäßig `SYNO.Core.System.Utilization`
- **Homepage/Dashy-Anbindung**: die Homepage-Bibliothek besitzt einen eigenen DSM-Handler, siehe [../gethomepage/features.md](../gethomepage/features.md)

---

## Vergleich mit den anderen Systemen

| Funktion | Synology DSM | Homarr | Heimdall | Dashy |
|----------|--------------|--------|----------|-------|
| Zweck | NAS-Betriebssystem | Dashboard | Dashboard | Dashboard |
| Eigene Pakete/Apps | ja | nein | nein | nein |
| Konten und ACL | ja (Systemebene) | Board-Freigaben | einfach | Rollen |
| API | `entry.cgi`, `SYNO.*` | tRPC | Laravel-Endpunkte | REST (optional) |
| Updates | Hersteller | Container-Image | Composer/Image | Image |
| Kosten | Hardware + proprietär | kostenlos | kostenlos | kostenlos |

---

## Siehe auch

- [menu.md](menu.md) - Menüpunkte nach Rolle
- [structure.md](structure.md) - Desktop-Portal, Fenster und Widgets
- [api.md](api.md) - Authentifizierung, Session und Endpunkte
- [shortcuts.md](shortcuts.md) - Tastatursteuerung
