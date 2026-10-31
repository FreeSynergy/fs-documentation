# Nextcloud Calendar - Beschreibung

## Übersicht

Nextcloud Calendar ist die Kalender-Anwendung der quelloffenen Collaborations-Plattform Nextcloud. Sie ist kein Einzelprogramm, sondern eine App innerhalb einer Nextcloud-Instanz: Der Server hält die Kalenderdaten, die Weboberfläche zeigt sie, und CalDAV verbindet alle Geräte. Lizenz: AGPL, komplett open source.

## Was Nextcloud Calendar macht

Nutzer legen Kalender an und tragen Termine ein - als Web-Oberfläche im Browser. Die Daten liegen in der Nextcloud-Datenbank und werden über ein eingebautes CalDAV-Backend (sabre/dav) allen Clients bereitgestellt. Termine lassen sich mit anderen Nextcloud-Nutzern, Gruppen und externen E-Mail-Adressen teilen; Einladungen laufen als ICS/iTIP über den Mail-Versand des Servers. Teamkalender entstehen automatisch für jede Benutzergruppe. Für die Terminfindung gibt es Verfügbarkeitsumfragen („Zeiten finden") und die Talk-Terminbuchung; Konferenzräume werden über die Ressourcen-App gebucht. Abos holen fremde Kalender (ICS/WebCal/CalDAV) auf den Server.

## Vorteile

- **Datenhoheit**: alles auf dem eigenen Server, DSGVO-tauglich, kein Werbedienst
- **Echter CalDAV-Server**: Apple Kalender, Thunderbird, Evolution, DAVx⁵ und Standard-Bibliotheken funktionieren ohne Zusatzsoftware
- **Groupware-Baukasten**: Kontakte (Geburtstage), Mail (ICS-Einladungen), Talk (Videos, Terminumfragen), Dateien (Anhänge), Aufgaben nahtlos verbunden
- **Keine Installationskosten pro Nutzer**: eine Instanz, ein Login für alles (Single Sign-On)
- **Teamkalender und Freigabestufen** inklusive Verfügbarkeits-only-Ansicht als Privatsphäre-Stufe
- **Öffentliche Links und Abos** für Feiertags-, Site- oder Vereinskalender
- **Aktive Entwicklung**: regelmäßige Releases zusammen mit dem Nextcloud-Major

## Abgrenzung zu anderen Systemen

### Nextcloud Calendar vs. Google Calendar
- **Google Calendar** ist ein öffentlicher Cloud-Dienst mit Komfortfunktionen (automatische Termine aus Mails, „Scheduling-Links", KI-Vorschläge); **Nextcloud Calendar** ist self-hosted ohne diese Komfortfunktionen, dafür mit voller Datenkontrolle
- **Google** bindet Geräte über sein eigenes Konto ein, **Nextcloud** über den offenen CalDAV-Standard
- **Google** ist (in der Basisversion) kostenlos, **Nextcloud** kostet Server-Betrieb und Pflege

### Nextcloud Calendar vs. SOGo
- **SOGo** ist eine klassische Groupware mit eigenem Web-Client und zusätzlich MAPI/ActiveSync - Outlook und Outlook Mobile binden nativ an; **Nextcloud Calendar** bietet „nur" CalDAV/CardDAV
- **SOGo** ist Kalender/Mail/Adressbuch in einem Paket, **Nextcloud** will die komplette Plattform (Dateien, Chat, Büro) sein
- **Nextcloud** hat die modernere Oberfläche und mehr Ökosystem, **SOGo** die stärkere Exchange-Kompatibilität

### Nextcloud Calendar vs. Radicale
- **Radicale** ist ein purer CalDAV-/CardDAV-Server ohne eigene Kalender-Oberfläche; **Nextcloud Calendar** bringt die komplette Web-UI, Freigaben, Umfragen und Teamkalender mit
- **Radicale** ist minimalistisch und in Minuten aufgesetzt, **Nextcloud** ist eine volle Plattform mit PHP-Datenbank und Wartungsaufwand
- Wer nur Sync braucht, fährt mit Radicale leichter; wer UI und Kollaboration braucht, braucht Nextcloud

## Technische Details

- **Backend**: PHP (Nextcloud Server, aktuell 8.x-Anforderungen), Kalender-App als Server-App; DAV-Schicht auf sabre/dav (sabre/vobject für ICS-Auswertung)
- **Datenbank**: MySQL/MariaDB oder PostgreSQL (Standard), SQLite für Kleinstinstanzen, Oracle in Enterprise-Umgebungen; Kalenderdaten in den Tabellen `calendars`/`calendarobjects` des CalDAV-Backends
- **Frontend**: Vue.js-App im Browser; die Zeit-Raster basieren auf FullCalendar, ICS-Parsing u. a. mit ical.js und der offiziellen Bibliothek `@nextcloud/calendar-js` (Regelwerk für Wiederholungen)
- **Authentifizierung**: Nextcloud-Konto mit Session im Browser; für CalDAV-Clients **App-Passwörter** (besonders mit Zwei-Faktor-Authentifizierung); optional SAML/OIDC/Keycloak als Identitätsanbieter; CalDAV-Standard ist HTTP Basic Auth
- **Kalender-Protokoll**: CalDAV (RFC 4791) inkl. Sync-Report (RFC 5995) und Free-Busy-Query; Einladungen nach iTIP, E-Mail-Versand über den Server
- **Hosting**: self-hosted (bare metal, Docker/Compose, offizielle Helm-Charts für Kubernetes, Snap) oder bei Managed-Anbietern (Hetzner, Netcup u. v. m.) bzw. Nextcloud GmbH (Hub); die Kalender-App ist in aktuellen Nextcloud-Versionen standardmäßig aktiviert

## Für wen ist Nextcloud Calendar geeignet?

- **Unternehmen, Behörden und Vereine mit Datenschutzauflagen**, die Kalender nicht an US-Clouds geben wollen
- **Bestehende Nextcloud-Nutzer**: Kalender + Talk + Mail + Dateien aus einem Login
- **Teams mit internen Räumen und Gruppenkalendern**, die Terminumfragen ohne Zusatzdienste brauchen
- **Weniger geeignet** für Exchange-/Outlook-zentrierte Firmen (kein MAPI/ActiveSync) und für Nutzer, die „es einfach nur bei Google anmelden" möchten - der Server-Betrieb will gepflegt sein
