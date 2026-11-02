# Google Kalender – Beschreibung

## Was das Programm macht

Google Kalender (calendar.google.com) ist der Kalender-Dienst von Google: eine Web-Oberfläche plus Apps für Android, iOS, Wear OS und Apple Watch, in der Termine, wiederkehrende Serien, Aufgaben und Mehrpersonentermine über mehrere Kalender hinweg verwaltet werden. Dazu kommen geteilte Kalender mit Berechtigungsstufen, Freigabe-/Abonnementfunktionen, öffentliche Kalender, Reservierungsseiten (Terminpläne, „Appointment schedules“) und organisatorische Kalender inklusive Raum-/Ressourcenkalendern in Google Workspace. Der Dienst läuft ausschließlich in der Google-Cloud; Self-Hosting ist nicht möglich.

Programmierbar ist er über die **Calendar REST API v3** (JSON/HTTPS), Aufgaben zusätzlich über die separate **Tasks API**; Änderungen lassen sich per Push-Kanälen (Webhooks) empfangen. Termine, Aufgaben und Arbeitsort werden mit Gmail (automatische Reise-/Reservierungstermine), Meet (Konferenzlinks), Tasks (Termine mit Datum erscheinen im Kalender) und – mit passendem Abo – Gemini (Terminvorschläge „Plane für mich“, „Zum Kalender hinzufügen“ aus E-Mails) verknüpft.

## Vorteile

- **Kein Betriebsaufwand**: nichts zu installieren, updaten oder zu sichern; Konten, Geräte-Sync und Verfügbarkeit übernimmt Google
- **Kostenlose Basis**: volle Kalenderfunktionen mit privatem Google-Konto; Workspace-Abos ergänzen Verwaltung, Ressourcen und Premium-Buchungsfunktionen
- **Plattformbreite**: Web, Android, iOS, Wear OS, Apple Watch – automatisch synchronisiert
- **Terminfindung & Zusammenarbeit**: Freigaben mit vier Berechtigungsstufen („nur Belegung“, „Details sehen“, „Termine ändern“, „teilen verwalten“), „Einen Termin finden“-Ansicht, Einladungen mit Antwort-Status, Gruppenkalender
- **Reservierungsseiten ohne Zusatz-Apps**: Kunden/Klienten buchen direkt; Premium (bestimmte Google-One-/Workspace-Abos) mit mehreren Seiten, Stripe-Zahlungen, E-Mail-Erinnerungen
- **Zeit-Werkzeuge**: Fokuszeit (Benachrichtigungen stumm, Besprechungen automatisch ablehnen), „Ihre Zeit im Blick“-Analyse, Arbeitsort/-zeiten für Teams, Dateien an Terminen
- **Großes Integrations-Ökosystem**: Calendar API v3 mit offiziellen Client-Bibliotheken, Push-Kanälen und Add-ons; Migrationstools u. a. aus Microsoft Exchange/Outlook und IBM Notes

## Abgrenzung zu vergleichbaren Produkten

| System | Unterschied |
|--------|-------------|
| **DAViCal** (in dieser Serie dokumentiert) | DAViCal ist der schlanke, selbst gehostete CalDAV-/CardDAV-Backend-Server (PHP/PostgreSQL, RFC 4791) – Datenhoheit, echte ACLs, Scheduling nach Standard, aber eigenes Betreiben. Google Kalender ist das gegenteilige Modell: fertiger SaaS-Komplettclient + proprietäre REST-API, **kein dokumentiertes CalDAV-Angebot** (Passwort-CalDAV wurde 2024/2025 abgeschaltet) |
| **Nextcloud Calendar** (in dieser Serie dokumentiert) | Selbst-gehostete Gruppenware-Oberfläche auf CalDAV-Basis mit voller Datenkontrolle; Google Kalender liefert vergleichbaren Komfort, aber ohne eigene Infrastruktur |
| **Outlook-Kalender** (in dieser Serie dokumentiert) | Microsofts Pendant in Microsoft 365 mit Exchange/Graph-API und Teams-Integration; Google Pendant zu Googles Stack (Gmail/Meet/Tasks) |
| **Merkuro** (in dieser Serie dokumentiert) / Planner (vorgesehen) | Native Desktop-Clients (KDE), die mit Servern wie DAViCal arbeiten; Google Kalender ist selbst Server *und* Client, aber ohne Offline-Desktop-Client |

Kern der Abgrenzung: Google Kalender ist **SaaS aus einer Hand** – sehr hoher Komfort, aber Daten liegen bei Google, der Zugriff läuft über Google-Konten/OAuth, und Standard-Protokolle (CalDAV) sind nicht offiziell vorgesehen. Wer Kalenderdaten souverän betreiben will, fährt mit DAViCal oder Nextcloud besser.

## Technische Details

- **Architektur**: geschlossener Google-Dienst; Clients (Web/Android/iOS) und Drittanbieter reden die Calendar REST API v3 (`https://www.googleapis.com/calendar/v3`, Discovery-Revision 2026‑10‑28), Aufgaben die Tasks API
- **Auth**: OAuth 2.0 mit fein gestuften Scopes (`calendar`, `calendar.events`, `calendar.acls`, …), Service Accounts mit Domain-wide Delegation für Workspace, API-Key nur für öffentliche Kalender
- **Synchronisation**: Sync-Token (deltas), Push-Benachrichtigungskanäle (HTTPS-Webhooks, ohne Inhalt – danach selbst nachziehen), Batch-Endpunkt
- **Datenaustausch**: ICS-Import/-Export, Kalender-URLs (öffentlich/geheim), Takeout; Einbettung von Kalendern
- **Grenzen**: Quota-Modell seit 1. Mai 2026 (10.000 Anfragen/min/Projekt, 600/min/Nutzer, Tagesgrenze 1 Mio. mit geplanter Bepreisung „später in 2026“); >400 abonnierte Kalender pro Konto bremsen laut Hilfe
- **KI**: Gemini-Funktionen nur mit Google-One-/Workspace-Premium-Abos

## Für wen geeignet

- **Private Nutzer**, die Google Mail/Konten ohnehin nutzen und sofort einen synchronisierten Kalender ohne Verwaltung wollen
- **Organisationen/Teams auf Google Workspace**: Kalenderfreigaben, Raum-/Ressourcenkalender, Verwaltungsrichtlinien, Migration aus Exchange/Notes
- **FreeSynergy-Szenario**: als „Skin“ sinnvoll, wenn Termine externer Nutzer über die Calendar API (Push + Sync-Token) eingebunden oder nach Google hinaus gespiegelt werden sollen
- **Ungeeignet** bei Anforderungen an Datenhoheit/Self-Hosting, CalDAV-Client-Zugang (nur inoffiziell) oder Abhängigkeit von einem einzelnen Anbieter vermeiden wollenden Setups – dort DAViCal (Server) bzw. ein CalDAV-Client
