# Synology DSM - Beschreibung

## Übersicht

DSM ist kein Dashboard im Sinne einer Link-Sammlung, sondern das **Betriebssystem eines Network Attached Storage** mit graphischer Verwaltungsoberfläche im Browser. Es bringt Speicher-, Rechte-, Sicherungs-, Freigabe- und Anwendungslogik mit; das Browser-Portal ist der Arbeitsplatz, über den alles gesteuert wird.

## Was Synology DSM macht

DSM verwaltet Datenträger, Storage-Pools, Volumes und Freigegebene Ordner und stellt sie über SMB, NFS, AFP/WebDAV/FTP bereit. Das Desktop-Portal zeigt eine **Desktop-Fläche mit Fenstern**, eine App-Leiste am unteren Rand, ein **Hauptmenü** mit allen installierten Paketen, Desktop-Widgets für Systemzustand (CPU, Arbeitsspeicher, Netzwerk, Volume-Gesundheit – in aktuellen DSM-Versionen als „System Pulse"-artige Kacheln ausgebracht) sowie eine Benachrichtigungszone. Über das **Paketzentrum** werden Anwendungen installiert (Drive, Backup, Media Server, Surveillance Station, Docker-Container über Container Manager). Die **Systemsteuerung** bündelt Benutzer, Gruppen, Rechte, Dienste, Sicherheit und Aufgabenplanung. Der Schnellstart-Führer führt durch Ersteinrichtung, Freigaben und Fernzugriff (QuickConnect, Reverse Proxy, DDNS).

## Vorteile

- **Ausgereift und breit dokumentiert**: lang gepflegte Oberfläche, große Community, offizielle Handbücher
- **Paketsystem**: Speicher-, Backup-, Medien-, Virtualisierungs- und Überwachungsanwendungen mit einem Klick installiert
- **Rechte und Dienste aus einer Hand**: Benutzer, Gruppen, Freigaben, Protokolle, ACL, 2FA und IP-Sperren
- **Sicherungskonzept**: Snapshot Replication, Active Backup, Hybrid Backup, Versionskontrolle von Freigaben
- **Eigene Verwaltungs-API**: `SYNO.*`-Schnittstelle für Automatisierung, inklusive `SYNO.FileStation.*` und `SYNO.Core.*`
- **Fernzugriff inklusive**: QuickConnect, Reverse-Proxy-Assistent, VPN-Server
- **Hardware-nah**: SMART-Prüfung, Speicher-Warnungen, E-Mail-/Push-Benachrichtigungen

## Abgrenzung zu anderen Systemen

### Synology DSM vs. Homarr
- **DSM** ist ein vollständiges NAS-Betriebssystem, **Homarr** ein Dashboard, das nur anzeigt und bedient
- **DSM** mit eigener Rechteverwaltung und Paketen, **Homarr** mit Board-Freigaben und Integrationen
- **Beide** sind proprietär bzw. quelloffen unterschiedlich lizenziert: **DSM** proprietär, **Homarr** open source

### Synology DSM vs. Heimdall
- **Heimdall** sammelt Kacheln und Statistik-Overlays, **DSM** stellt die Dienste selbst bereit
- **Heimdall** läuft als PHP-Anwendung ohne Systemverwaltung, **DSM** verwaltet Datenträger, Freigaben und Dienste
- **Heimdall** kostenlos, **DSM** nur auf Synology-Hardware bzw. lizenziert verfügbar

### Synology DSM vs. Homer
- **Homer** ist eine statische YAML-Seite ohne Anmeldung und Backend, **DSM** ist ein volles System mit Konten, Protokollen und Paketen
- **Homer** zeigt Links, **DSM** zeigt und steuert Storage, Pakete und Aufgaben
- **Homer** auf jedem Webserver hostbar, **DSM** an Synology-Geräte gebunden

### Synology DSM vs. Dashy
- **Dashy** konfiguriert Dashboards (`conf.yml`) und prüft Link-Status, **DSM** bietet die überwachten Dienste selbst
- **Dashy** mit Theme-System und Eigen-Betrieb, **DSM** mit Systemsteuerung, Wartung und Support
- **Dashy** kann DSM über dessen API als Kachel einbinden – umgekehrt nicht gedacht

## Technische Details

- **Backend**: proprietäres DSM (Linux-basis), Webdienst `nginx`/eigener HTTP-Server mit `entry.cgi` als API-Eingang
- **Database**: interne Systemdatenbank für Konten, Pakete und Einstellungen; für Nutzer nicht als klassische DB zugänglich – Pakete nutzen eigene Speicher (z. B. MariaDB für Web-Anwendungen)
- **Frontend**: Browser-Portal mit Fenster-Manager, App-Leiste, Hauptmenü, Desktop-Widgets; eigene Clients für Desktop und Mobile
- **Authentication**: lokale Konten und Gruppen, LDAP/AD-Domäne, 2FA/OTP, Trusted-Devices, Sitzung mit Timeout; Ports **5000/5001** (HTTPS empfohlen), QuickConnect als Vermittlungsdienst
- **Hosting**: auf Synology-Hardware (DiskStation, RackStation); alternative Plattformen sind vom Hersteller nicht freigegeben; Zugriff über LAN, VPN oder Reverse Proxy
- **Update-Modell**: DSM-Updates über Systemsteuerung/Paketzentrum, Paket-Lebenszyklus separat verwaltet

## Für wen ist Synology DSM geeignet?

- **Heim- und Kleinbüro-Umgebungen**, die zentrale Speicherung, Freigaben und Sicherung mit wenig Wartungsaufwand wollen
- **Administratoren, die Rechte, Protokolle und Protokoll-Überwachung** brauchen und Pakete komfortabel verwalten möchten
- **Automatisierer**, die über `entry.cgi` Aufträge, Freigaben und Status aus Skripten steuern
- **Weniger geeignet** als reines Übersichts-Dashboard (dafür Homarr/Homepage/Dashy) und für Umgebungen ohne Synology-Hardware
