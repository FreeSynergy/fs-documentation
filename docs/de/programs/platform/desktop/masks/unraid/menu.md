# Unraid - Menüpunkte

## Übersicht

Unraid hat kein Dropdown-Menü, sondern eine **horizontale Tab-Leiste** oben auf jeder Seite: Main, Shares, Users, Docker, VMs, Apps, Plugins, Tools, Settings (Reihenfolge und Bezeichnungen je nach Version leicht unterschiedlich). Zusätzlich gibt es das Icon-Menü rechts oben (Benachrichtigungen, Hilfe, Connect, Abmelden) und je Tab eigene Buttons und Dialoge.

## Hauptmenüpunkte (Tabs)

### 1. Main
- **Funktion**: Zustand von System und Array auf einen Blick
- **Details**:
  - System-Identifikation, Update-Status, Anmeldungs-/Lizenzstatus
  - Array-Ansicht: Paritätslaufwerk(e), Datendisks, Cache, Hot Spares
  - Kapazitätsbalken pro Laufwerk und global; Laufwerk-Symbole (Farben = Status)
  - Buttons: Array neu starten, PARITY-Positionen ändern, Zusatzlaufwerke zuweisen

### 2. Shares
- **Funktion**: User Shares anlegen und verwalten
- **Details**:
  - Tabelle aller Freigaben mit Belegung, Sicherheit und Anteil pro Disk
  - **Add New Share**: Assistent mit Name, Sicherheit (public/secure/private), include/exclude-Disks
  - Bearbeiten-Dialog je Share: Sicherheit, Aufteilung, Mindestbelegung, Kontingent (versionabhängig)

### 3. Users
- **Funktion**: Benutzerkonten verwalten
- **Details**:
  - Benutzerliste mit Beschreibung und E-Mail
  - Hinzufügen/Bearbeiten/Löschen, Passwort setzen, Gültigkeit (versionabhängig)
  - Bezug zu SMB/FTP-Zugängen (versionabhängig)

### 4. Docker
- **Funktion**: Container und Docker-Grundkonfiguration
- **Details**:
  - Tabelle der Container: Name, Pfad, Port, Status, WebPUI-Button, Logs, Update
  - **Add Container**: Vorlagen-Suche (App-Store-Einbindung) und Template-Formular
  - **Docker Settings**: Docker-Disk oder Directory-Mode, abschaltbare Container-Gruppe
  - Compose-Projekte in neueren Versionen (versionabhängig)

### 5. VMs
- **Funktion**: Virtuelle Maschinen verwalten (höhere Lizenz erforderlich, versionabhängig)
- **Details**:
  - VM-Liste mit Start/Stop/Pause/Force Stop, webVNC-Konsole
  - **Add VM**: Assistent (RAM, CPU, vDisk-Typ qcow2/raw, Bus, Netz, BIOS/UEFI, Start beim Boot)
  - **VM Settings**: libvirt-Disk, ISO-Speicher, Hypervisor-Details
  - VMAusnahmen und Treiber-ISO (virtio) über Dialoge

### 6. Apps
- **Funktion**: Community Applications — Store für Vorlagen und Plugins
- **Details**:
  - Suche und Kategorien für Application- und Plugin-Katalog
  - Installationsdialoge (Vorlage → Docker-Formular), Updates und Fehlermeldungen
  - Deaktivierbarer Wartungs-/App-Modus für Update-Zwangsschritte

### 7. Plugins
- **Funktion**: Installierte Plugins verwalten
- **Details**:
  - Installationshistorie mit Versionsständen, Update-Buttons, Remove
  - Plugin-Konfigurationsseiten erscheinen teils als eigener Tab oder Settings-Eintrag

### 8. Tools
- **Funktion**: Diagnose und Instandhaltung
- **Details**:
  - **System**: Systeminformationen, Log-Dateien, Diagnose-Dumps
  - **New Permissions**: ACL-/Rechte-Reparatur auf Shares
  - **Startup Procedure / System Profiler**: Bootprotokoll, Geräteübersicht (versionabhängig)
  - PHP-Info und Web Terminal (meist als Plugin)

### 9. Settings
- **Funktion**: Systemweite Grundeinstellungen
- **Details**:
  - **Management Access**: HTTP/HTTPS, Port, Zertifikat, API-Schlüssel, Entwickleroptionen (GraphQL-Sandbox)
  - **Network Settings**: IP, DNS, Workgroup/Domain, Bridge (versionabhängig)
  - **Disk Settings**: Spin-down, Schlafmodi, Festplatten-Cache-Verhalten
  - **Scheduler**: Parity Check, Mover, Eigen-Cron
  - **Identification**: Gerätename, Farbschema, Kommentar
  - **SMB/NFS**: Freigabedienste und Feinheiten (versionabhängig)
  - **Notifications**: E-Mail- und Webhook-Versand (ab 6.12, versionabhängig)
  - **Language & Theme**, Docker-/VM-Grundeinstellungen, Update-Channel

## Icon-Menü oben rechts

- **Benachrichtigungen** (Glocke): Ereignisliste aus dem Benachrichtigungsdienst
- **Hilfe/Docs**: Link zur offiziellen Dokumentation
- **Unraid Connect**: Registrierungsstatus, Fernzugriff
- **Abmelden** (sofern WebUI-Anmeldung aktiviert)

## Kontext-Aktionen in Listen

- **Laufwerk (Main)**: klicken für Details, Smart-Werte, Zuweisung als Hot Spare/Cache
- **Share**: Bearbeiten/Löschen, View (Browser-Ordneransicht)
- **Container**: Logs, WebPUI, Update-Prüfung, Terminal/Console, Remove (Behalt-Dialog für Appdata)
- **VM**: Start, Stop, Force Stop, Pause, webVNC, Bearbeiten (Hardware-Dialog), Snapshot-Aktionen (versionabhängig)

## Menüs nach Rolle

### Unangemeldet (keine WebUI-Anmeldung erzwungen)
- Volle UI sichtbar — darum Anmeldung und HTTPS in der Praxis Pflicht

### Eingeschränkter Benutzer (falls eingerichtet, versionabhängig)
- Read-only-Sichten auf Main/Shares, keine Array-/Settings-Aktionen

### Administrator (root/WebUI-Login)
- Alle Tabs, Array-Steuerung, Plugins, Settings, API-Key-Verwaltung, Connect-Verknüpfung

## Shortcuts

Die vorhandene Tastatursteuerung (Tabwechsel per Browser, Dialoge) ist in [shortcuts.md](shortcuts.md) beschrieben, inklusive der klar als nicht vorhanden markierten Tasten.
