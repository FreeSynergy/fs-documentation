# DAViCal – Beschreibung

## Was das Programm macht

DAViCal ist ein CalDAV-/CardDAV-Server in PHP, der Kalender- und Kontaktdaten in **PostgreSQL** speichert und sie über das offene DAV-Protokoll (RFC 4791/6352) für Standard-Clients bereitstellt. Er ist in erster Linie Backend, bringt aber zusätzlich eine schlichte Web-Oberfläche (Web-Calender zum Ansehen/Bearbeiten), eine Web-Administration und einen eingebauten Zeitzone-, FreeBusy- und Feed-Dienst mit. Termine, Aufgaben (VTODO), Journale (VJOURNAL) und Kontakte liegen als ICS-/vCard-Objekte mit Änderungshistorie (Sync-Token) in der Datenbank.

## Vorteile

- **Datenbank-zentriert**: PostgreSQL als Speicher – relationale Integrität, SQL-Zugriff für Auswertungen, sauberer Migration-/Backup-Pfad
- **Feingranulare Rechte**: echte RFC-3744-ACLs, Principal-Proxy (Kalendervertretung), Gruppen, öffentlich lesbare Sammlungen und Ticket-URLs für Zugänge ohne Login
- **Kalender-Abo & Einbindung**: `BIND` bindet fremde Kalender als abonnierte Sammlung ein
- **Scheduling inklusive**: Inbox/Outbox (RFC 6638), automatisches Inviten, plus signiertes iSchedule (Domain Keys) – das bieten nur wenige Open-Source-Server
- **Reif und gepflegt**: Entwicklung seit 2006/2007, Release 1.1.13 (Mai 2026), in Debian/Arch/Gentoo paketiert
- **Echt quelloffen**: GPL v2 (einzelne Teile v3), keine Cloud-Abhängigkeit

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Baïkal** | Nutzt eine gewartete Gabelung des DAViCal-Cores, zielt auf SQLite/einzigen Admin und bringt **kein** eigenes Web-Frontend; DAViCal selbst ist der vollständige Server inkl. Web-Calender, ACLs und Scheduling |
| **Radicale** | Python, kalenderweise ICS-Dateien auf dem Dateisystem; einfacher, aber ohne SQL-Auswertung und ohne die DAViCal-eigenen Erweiterungen (Tickets, BIND, Proxy) |
| **Nextcloud (CalDAV-App)** | Suite mit Dateien/Web-UI; DAViCal ist der schlanke reine DAV-Dienst für Infrastruktur, die Kalenderdaten als standardisierte Modelle braucht |
| **Xandio Enterprise Server** | Java, Kommerzticket, Outlook/Windows-Integration; DAViCal ist leichter und community-getragen |

## Technische Details

- **Sprache/Frameworks**: PHP 8.x (Setup prüft PHP-Version; PHP-8.2-kompatibel seit 1.1.13), Aufbau auf der AWL-Bibliothek (Andrew's Web Library)
- **Datenbank**: PostgreSQL (8.2+), Schema inkl. Principal-, Collection-, Resource- und Change-History-Tabellen (`dba/davical.sql`, `update-davical-database`)
- **Frontend**: Server-gerendertes PHP-UI für Web-Calender (`index.php`) und Administration (`admin.php`)
- **Authentifizierung**: HTTP Basic; Treiber für lokale DB, LDAP (SASL, Gruppen-Sync), PAM, Kerberos/GSSAPI, externe Session
- **Hosting**: Apache/nginx + PHP-FPM, Standard-Apache-Konfig mit Alias `/davical` im Projekt; TLS über Reverse Proxy
- **Lizenz**: GPL v2 oder später (einzelne Komponenten v3)

## Für wen geeignet

- Selbstversorger, Vereine, Familien und kleine bis mittlere Teams, die Kalender/Kontakte mit echten Teilrechten betreiben
- Umgebungen mit PostgreSQL-Infrastruktur, die Kalenderdaten per SQL auswerten wollen
- FreeSynergy-Szenarien, in denen standardisierte ICS-/vCard-Modelle mit Scheduling und Kalender-Abos gebraucht werden
