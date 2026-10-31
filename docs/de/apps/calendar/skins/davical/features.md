# Baïkal/Davical - Funktionen

## Hauptfunktionen

### Kalender (CalDAV, RFC 4791)
- Beliebig viele Kalender pro Benutzer
- Ereignisse inkl. Wiederholungen (RRULE), Erinnerungen (VALARM), Kategorien
- Schreib-/Leserechte je Kalender; Freigaben zwischen Benutzern
- Öffentliche Lese-Links (Subscription) für Abos

### Kontakte (CardDAV, RFC 6352)
- Adressbücher pro Benutzer, vCard 3.0/4.0
- Gruppen (VGROUP) und Verteilerlisten
- Freigaben zwischen Benutzern

### Administration
- Web-UI: Benutzer, Kalender, Adressbücher, Freigaben, Instanzeinstellungen
- Optional offene Registrierung (Baïkal-Modus)
- CLI: `baikal.php` / Davical-Tools zum Anlegen von Principals

### Betrieb
- PHP 8+, Datenbanken MySQL/MariaDB oder SQLite
- Unter StApache/nginx/Apache hinter TLS betreibbar; Docker-Images vorhanden

## Was Baïkal/Davical NICHT kann

- **Kein Kalender-Frontend für Endnutzer** — es gibt keine Web-Tagesansicht; dafür Clients (Kalendar, Thunderbird, Nextcloud Calendar) verwenden
- **Keine Aufgaben über Fälligkeits-Warnungen** (VTODO/Todo wird gespeichert, aber nicht überwacht)
- **Keine Terminfindung/Meetings-API** (kein Google-Calendar-artiges Scheduling)
- **Keine Ende-zu-Ende-Verschlüsselung** der Kalenderdaten
- **Keine iMIP/iTIP-Einladungen** auf Protokollebene — Einladungen sind rein serverinterne ATTENDEE-Felder; E-Mail-Versand übernimmt kein Baïkal
- **Keine LDAP-Anbindung** in Standard-Baïkal (Benutzerpflege nur über UI/CLI)
- **Keine Push-Benachrichtigungen** (CalDAV-Sync/Push: ❌)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Clients | jeder CalDAV-/CardDAV-Client (Thunderbird, Kalendar, Apple, mobile) |
| Reverse-Proxy-TLS | nginx/Apache; Standard-Port 443 |
| Single Sign-On | nur Basic-Auth; OIDC-Lösung vorgelagert (z.B. authelia) |
| Backup | DB-Dump (mysqldump/SQLite-Datei) + `Settings/`-Verzeichnis |
| Nextcloud-Sync | Baïkal und Nextcloud können dieselben Kalender nicht teilen — beide wären eigene DAV-Server (Migration über ICS-Export) |
