# Baïkal/Davical - Beschreibung

## Was das Programm macht

Baïkal verpackt den Davical-CalDAV/CardDAV-Server in eine einfach zu installierende PHP-Anwendung mit Web-Administration. Es speichert Kalender und Kontakte in einer SQL-Datenbank und stellt sie über das offene DAV-Protokoll allen Standard-Clients bereit. Es ist bewusst **nur Backend**: Der Nutzer arbeitet in seinen Kalender-/Kontakt-Apps.

## Vorteile

- **Echt quelloffen und protokolltreu**: reines RFC-4791/6352, herstellerneutral
- **Winziger Footprint**: PHP + SQLite genügen für Einzelnutzer; läuft auf einem 1-€-VPS
- **Schnelle Administration**: Benutzer und Kalender in Sekunden angelegt
- **Betriebssicher**: lange im Einsatz, bewährte Migrationen, Docker-Images (z.B. ckulka/baikal)

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Ricale/Radicale** | Radicale ist Python/Datei-basiert (Kalender als ICS-Dateien); Baïkal ist PHP/SQL — besser für viele Benutzer, dafür weniger Dateisystem-zugänglich |
| **Nextcloud (CalDAV-App)** | Nextcloud bringt Files/Contacts/Web-Kalender als Suite; Baïkal ist der pure DAV-Dienst ohne eigenes UI — schlanker, aber ohne Komfort-Extras |
| **Xandio Enterprise Server** | Java, Gruppenkalender mit detaillierten Rechten und Windows-Integration; schwerer und kommerziell |

## Technische Details

- **Backend**: PHP 8.x, Framework Slim (Baïkal-Admin), Davical-Core (Cal::DAV::Server)
- **Datenbank**: MySQL/MariaDB oder SQLite; Tabellen für Principal, Kalender, Adressbuch, Objekte, Änderungshistorie (Sync Token)
- **Frontend**: Admin-Web-UI (Server-rendered HTML + wenig JS)
- **Authentifizierung**: HTTP Basic gegen die Principal-Tabelle; optional offene Registrierung
- **Hosting**: Apache/nginx + PHP-FPM, Docker; TLS über Reverse Proxy
- **Lizenz**: quelloffen (Davical-Server unter eigener BSD-artiger Lizenz, Baïkal-Administration MIT)

## Für wen geeignet

- Selbstversorger, Familien und kleine Teams, die Kalender/Kontakte ohne Cloud-Suite betreiben
- als DAV-Backend hinter Thunderbird/Kalendar/Apple-Geräten
- FreeSynergy-Szenarien, in denen Kalenderdaten als standardisierte ICS/vCard-Modelle gebraucht werden
