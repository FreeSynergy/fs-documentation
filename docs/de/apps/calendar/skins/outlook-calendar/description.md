# Outlook Kalender - Beschreibung

## Übersicht

Outlook Kalender ist der Kalender-Baustein von Microsoft 365: Termine, Besprechungen, Aufgaben und Ressourcen liegen im Exchange-Postfach und werden in Outlook im Web, Outlook für Windows und Mac, Outlook Mobile und Outlook Classic angezeigt. Der Kalender ist kein Einzelprogramm, sondern Teil einer Groupware – E-Mail, Kontakte und Besprechungsabstimmung teilen sich dieselbe Datenbasis.

## Was Outlook Kalender macht

Termine und wiederkehrende Serien werden angelegt, mit Teilnehmern und Räumen verknüpft und als Besprechungsanfragen versendet. Free/Busy-Zeiten der Kollegen erscheinen im Planungsassistenten, Freigabestufen regeln, wer einen Kalender nur liest oder bearbeitet. Alle Objekte sind über Microsoft Graph programmatisch erreichbar; für den Austausch mit anderen Kalendern dient das iCalendar-Format (ICS-Import, Terminlinks, Google-Kalender-Abgleich).

## Vorteile

- **Ein Postfach, alle Geräte**: Web, Windows, Mac, iOS, Android zeigen denselben Stand
- **E-Mail und Kalender verzahnt**: Besprechungsanfragen, Antworten, Anlagen und Aufgaben in einem Ablauf
- **Ressourcenbuchung**: Besprechungsräume und Equipment als Postfach mit Buchungsrichtlinien
- **Free/Busy und Planungsassistent** mandantenweit, auch über Organisationsbeziehungen
- **Rechte abgestuft**: von „nur Verfügbarkeit" bis „Vollzugriff", dazu Delegiertenzugriff
- **Compliance und Verwaltung**: Aufbewahrungsrichtlinien, Audit-Log, Conditional Access, MFA
- **Breite API**: Microsoft Graph mit Terminen, Kalendern, Gruppen, Freigaben, Zeitplan und Webhooks
- **Besprechungstools am Termin**: Teams-Besprechung mit einem Klick, Add-ins wie FindTime oder Zoom
- **Barrierefreiheit und Mehrsprachigkeit** auf dem Stand der Microsoft-365-Oberflächen

## Abgrenzung zu anderen Kalendersystemen

### Outlook Kalender vs. Google Kalender
- **Outlook** ist an Exchange-Postfächer und Entra-ID-Identitäten gebunden, **Google Kalender** an Google-Konten
- **Outlook** hat Ressourcenpostfächer und Delegiertenzugriff für Unternehmen, **Google Kalender** dafür unkomplizierte öffentliche ICS-Feeds
- **Outlook** punktet mit Free/Busy im Unternehmen und Microsoft-365-Verwaltung, **Google Kalender** mit einfacher Freigabe nach außen und starker Websuche
- Beide sind Cloud-Dienste ohne Self-Hosting

### Outlook Kalender vs. Nextcloud Kalender
- **Nextcloud** ist self-hosted mit **CalDAV** (`/.well-known/caldav`) und damit mit jedem offenen Client nutzbar, **Outlook** bietet kein CalDAV
- **Nextcloud** gehört datenschutzrechtlich komplett dem Betreiber, **Outlook** folgt den M365-Datenregionszusagen
- **Outlook** hat mehr Komfortfunktionen (Ressourcen, Planungsassistent, Onlinebesprechungen), **Nextcloud** dafür volle Datenhoheit und einfache App-Passung
- Nextcloud-Installation erfordert eigenen Betrieb, Outlook ist bezogene Lizenzware

### Outlook Kalender vs. DAViCal / SabreDAV (CalDAV-Server)
- **DAViCal/SabreDAV** sind reine Kalender-/Kontaktserver (PostgreSQL bzw. PHP-Bibliothek) ohne eigene Oberfläche im großen Stil, **Outlook** bringt Clients, Mobile-Vertrieb und Admin-Werkzeuge mit
- **CalDAV-Server** sind frei konfigurierbar und beliebig skalierbar, **Outlook** ist in Struktur und Rechten an die Mandantsorganisation gebunden
- Für Gruppen ohne Microsoft-365-Lizenzen sind CalDAV-Server günstiger, für M365-Landschaften ist Outlook Kalender die naheliegende Wahl

## Technische Details

- **Plattformen**: Browser (Outlook im Web), Windows (neues Outlook, Outlook Classic), macOS, iOS, Android
- **Backend**: Exchange Online (Postfachdienste von Microsoft 365); lokal alternativ Exchange Server als eigene Produktlinie inkl. Hybridbetrieb
- **Datenspeicher**: Exchange-Postfach (Kalenderordner, Termine als iCalendar-artige Objekte); die genaue Speicherengine von Exchange Online ist öffentlich nicht dokumentiert
- **Frontends**: Outlook im Web (Web-App, Fluent-Design), neues Outlook für Windows (Web-Technologie verpackt), Outlook Classic (Win32, MAPI/HTTP, OST-Cache), Outlook für Mac, Outlook Mobile (iOS/Android)
- **Schnittstellen**: Microsoft Graph REST (`/v1.0`, `/beta`), Exchange Web Services (veraltet, für Exchange Online abgelöst angekündigt), MAPI over HTTP, Exchange ActiveSync, IMAP4 (Kalenderordner), ICS-Import
- **Protokolle/Formate**: iCalendar (RFC 5545) als Austauschformat, MIME für Besprechungsanfragen
- **Authentifizierung**: OAuth 2.0 / OpenID Connect über Microsoft Entra ID, delegated und application permissions (`Calendars.Read`, `Calendars.ReadWrite`), MFA/Conditional Access, MSAL-Bibliotheken
- **Autorisierung**: RBAC im Mandant (Exchange-Rollen), Freigabestufen pro Kalender, App-Rechte mit Administratorzustimmung
- **Hosting**: ausschließlich Cloud (Microsoft 365, Datenregions-/Data-Boundary-Zusagen) bzw. Outlook.com für Privatkonten; **kein Self-Hosting**
- **Lizenz**: kostenpflichtig im Business-Umfeld (Microsoft-365-Plan), privat mit Outlook.com-Konto kostenlos nutzbar

## Für wen ist Outlook Kalender geeignet?

- **Unternehmen mit Microsoft 365**: Raumplanung, Delegation, Free/Busy und Compliance sind direkt nutzbar
- **IT-Administrationen**, die Kalender über Entra-ID und Exchange-Rollen steuern müssen
- **Entwickler**, die Termine automatisieren wollen (Graph, Power Automate, Change Notifications)
- **Privatanwender** mit Microsoft-Konto für Mail, Kalender und Aufgaben aus einer Hand
- **Weniger geeignet** für Self-Hosting-Umgebungen, offene CalDAV-Landschaften und stark regulierte Umfelder, in denen Daten die eigene Infrastruktur nicht verlassen dürfen – dort passen Nextcloud Kalender, DAViCal oder SabreDAV besser
