# Google Kalender – Dokumentation

## Übersicht

Google Kalender (calendar.google.com) ist Googles Kalender-Dienst: Web-Oberfläche und Apps für Android, iOS, Wear OS und Apple Watch, gekoppelt mit Gmail, Meet, Tasks und (mit Premium-Abo) Gemini. Termine, Serien, Freigaben, Reservierungsseiten, Fokuszeit, Arbeitsort und Organisationskalender stammen aus einer geschlossenen SaaS-Plattform; programmatisch erschlossen über die **Calendar REST API v3** (Discovery-Revision 2026‑10‑28) mit OAuth-Scopes, Sync-Token und Push-Kanälen. Für FreeSynergy ist er der Cloud-Skin: Anbindung nur über Google-eigene API möglich, **kein dokumentiertes CalDAV**, kein Self-Hosting.

## Dateistruktur

- [description.md](description.md) – Was Google Kalender macht, Vorteile, Abgrenzung zu DAViCal/Nextcloud/Outlook/Kalendar
- [features.md](features.md) – verifizierte Funktionen (Ansichten, Termine, Freigaben, Buchung, Integrationen) + „Was Google Kalender NICHT bietet“
- [structure.md](structure.md) – Request-/Programmablauf, Datenmodell, Konfiguration, Deployment-Realität
- [menu.md](menu.md) – Navigationsstruktur der Web-Oberfläche (aus offiziellen Hilfeseiten)
- [shortcuts.md](shortcuts.md) – offizielle Tastaturkürzel der Web-App + Abgrenzung client-seitiger Tasten
- [api.md](api.md) – Calendar API v3: Basis-URL, alle Endpunkte, Auth/Scopes, Push, Limits, SDKs

## Kurzprofil

| Merkmal | Wert |
|---------|------|
| Typ | Cloud-Dienst (SaaS), Web + Android/iOS/Wear OS/Apple Watch |
| Version | Calendar REST API **v3** (Discovery-Revision 2026‑10‑28); UI = laufender Web-Dienst |
| API | REST v3 (`calendar.googleapis.com`/`googleapis.com/calendar/v3`), Tasks API, Apps Script, Add-ons |
| Auth | OAuth 2.0 (fein granulare Scopes), Service Accounts (Domain-wide Delegation), API-Key für öffentliches |
| Sync/Push | Sync-Token/Deltas, Watch-Kanäle (HTTPS-Webhooks), Batching; **kein CalDAV** |
| Datenhaltung | ausschließlich Google-Cloud; ICS-Import/-Export, Takeout |
| Kosten | kostenlos mit Google-Konto; Workspace-/Google-One-Abos für Verwaltung + Premium (Zahlungen, Gemini) |
| Self-Hosting | ❌ nicht möglich |

## Quellen

Alle Aussagen dieser Sektion stammen aus offiziellen Primärquellen (abgerufen am 02.11.2026, sofern nicht anders angegeben):

| Quelle | Fundstelle / URL | Wofür benutzt |
|--------|------------------|----------------|
| **Discovery-Dokument Calendar v3** (Revision **20261028**) | `https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest` | api.md: alle Ressourcen/Methoden/Pfade, Parameter, Schemas, Scopes, `batchPath` |
| Scopes-Seite der API-Doku | `https://developers.google.com/workspace/calendar/api/auth` (zuletzt aktualisiert 2026‑09‑03) | api.md: vollständige Scope-Tabelle inkl. Add-on-Scopes |
| API-Übersicht | `https://developers.google.com/workspace/calendar/api/guides/overview` (2026‑09‑11) | api.md: Ressourcenbegriffe |
| Push-Notification-Leitfaden | `https://developers.google.com/workspace/calendar/api/guides/push` | api.md: Watch/Stop, Header, Zustellcodes, Erneuerung |
| Usage limits | `https://developers.google.com/workspace/calendar/api/guides/quota` | api.md/features.md: Quotas 10.000/min, 600/min/Nutzer, 1 Mio./Tag, Bepreisungsplanung 2026 |
| Referenz `events.update` | `https://developers.google.com/workspace/calendar/api/v3/reference/events/update` | api.md: ETag-Hinweis, `sendUpdates`, Versionsparameter |
| Downloads (Client-Bibliotheken) | `https://developers.google.com/workspace/calendar/api/downloads` (2026‑09‑03) | api.md: SDK-Liste |
| Workspace Events API v1 (Referenz) | `https://developers.google.com/workspace/events/reference/rest/v1` (2026‑05‑14) | api.md: Pub/Sub-Alternative (Kalender-Support als unklar markiert) |
| Produktseite Google Kalender (DE) | `https://workspace.google.com/products/calendar/` | description.md/features.md: Plattformen, Tasks/Gmail/Meet, Reservierungsseiten + Stripe-Premium, Time Insights, Fokuszeit, Arbeitsort, Migration |
| Workspace-Updates-Blog (offiziell) | `https://workspaceupdates.googleblog.com/2023/09/winding-down-google-sync-and-less-secure-apps-support.html` | api.md/features.md: CalDAV/CardDAV/Google-Sync-Ende (30.09.2024, Updates bis 2025) |
| Workspace-Admin-Wissensdatenbank | `https://knowledge.workspace.google.com/admin/sync/transition-from-less-secure-apps-to-oauth` | api.md: OAuth-Pflicht ab März/Mai 2025, CalDAV nur noch mit OAuth |
| Kalender-Hilfe: Anderen Kalender abonnieren | `https://support.google.com/calendar/answer/37100?hl=en` (zusätzlich DE-Fassung abgerufen) | features.md/menu.md: Abonnement per E-Mail/URL, Berechtigungsstufen, 400-Kalender-Grenze, deutsche Menübeschriftungen („Weitere Kalender hinzufügen“, „Kalender abonnieren“, „Per URL“) |
| Kalender-Hilfe: Ansichten (DE) | `https://support.google.com/calendar/answer/6110849?hl=de` | menu.md: „Tag, Woche, 4 Tage, Monat, Jahr, Terminübersicht“, „Heute“, kleiner Kalender, Zahnrad → „Ansichtsoptionen“, „Meine Kalender“/„Weitere Kalender“ |
| Kalender-Hilfe: Terminplan erstellen (DE) | `https://support.google.com/calendar/answer/10729749?hl=de` | menu.md: „Eintragen“ → „Terminplan“, Bereichsbezeichnungen des Editors, 4-Stunden-Standardvorlauf |
| Kalender-Hilfe: Export (DE) | `https://support.google.com/calendar/answer/37111?hl=de` | menu.md/structure.md: Dreipunkt-Menü → „Einstellungen und Freigabe“, „Importieren & Exportieren“, „Öffentliche/Privatadresse im iCal-Format“ |
| Kalender-Hilfe: Zeit im Blick (DE) | `https://support.google.com/calendar/answer/10738043?hl=de` | menu.md: „Weitere Details“ (links), Anheften von Kontakten |
| Kalender-Hilfe: Tastenkombinationen | `https://support.google.com/calendar/answer/37034?hl=de&co=GENIE.Platform%3DDesktop` | shortcuts.md: komplette offizielle Kürzelliste, Aktivierung, Seitenleisten-Tasten |
| Kalender-Hilfe: Erste Schritte | `https://support.google.com/calendar/answer/37057?hl=en` | features.md: keine Desktop-App, Offline-Nutzung, Browserliste |
| Kalender-Hilfe: Ansichten | `https://support.google.com/calendar/answer/6110849?hl=en` | features.md/menu.md: Tag/Woche/4 Tage/Monat/Jahr/Zeitplan |
| Kalender-Hilfe: Zeit im Blick | `https://support.google.com/calendar/answer/10738043` | features.md: Time Insights (Workspace, Admin-Schalter) |
| Kalender-Hilfe: Fokuszeit | `https://support.google.com/calendar/answer/11190973` | features.md: Fokuszeit-Verhalten |
| Kalender-Hilfe: Reservierungsseiten | `https://support.google.com/calendar/answer/10729749` und `.../answer/11608416` | features.md: Appointment schedules, Premium-Grenzen |
| Kalender-Hilfe: Zahlungen für Terminpläne (Admin) | `https://knowledge.workspace.google.com/admin/calendar/allow-paid-appointment-schedules-in-calendar` | features.md: Stripe-Funktion (Workspace) |
| Kalender-Hilfe: Export | `https://support.google.com/calendar/answer/37111` | features.md: ICS-Export-Bedingungen |
| Workspace-Updates-Blog: „Find a time“ | Beitrag „Save time with smart scheduling in Google Calendar“ (29.09.2016) via Blog-Suche | features.md: Find-a-time-Funktion |
| Goals-Einführung (offiziell) | Workspace-Updates-Blog, Beitrag „Goals in Google Calendar“ via Blog-Suche | features.md: Goals existierten (Einführung 2019) |
| DAVx⁵ „Tested with: Google“ | `https://www.davx5.com/tested-with/google/` (Stand der Seite Juni 2023) | api.md: inoffizieller CalDAV/CardDAV-Zugriff nur mit OAuth, „nicht offiziell unterstützt“ – **Community-Quelle, klar gekennzeichnet** |

**Recherche-Hinweise:**
- Die ältere Fassung dieser Datei enthielt Fabrikationen: einen Scope `calendar.push` (existiert nicht), `users/{user}/calendarList` (real nur `users/me/…`), einen Endpunkt „API für Terminpläne“ und eine pauschale „CalDAV wird unterstützt“-Aussage. Alle Punkte wurden gegen Discovery v3 (Rev. 20261028) und die LSA-Abkündigungen korrigiert.
- Goals-Abschaltung: offizieller Hilfartikel ist entfernt; der Wegfall (Nov. 2022) ist nur durch mehrere unabhängige Berichte belegt – entsprechend als Bericht, nicht als Primärzitat gekennzeichnet.
- „Zweite Zeitzone“ und Offline-Umfang bleiben als **nicht verifiziert** markiert.
- Der alte Shortcuts-Hilfartikel (answer/71185) existiert nicht mehr; die offizielle Kurzbefehl-Seite ist heute **answer/37034** (Computer). Beide Aussagen gegen den Live-Artikel geprüft.
- Discovery-Vergleich alt/neu: `summaryVisibility` und `subscriptionType` sind aus `CalendarListEntry` verschwunden, neu `autoAcceptInvitations`/`dataOwner`/`writerWithoutPrivateAccess` und der schreibbare Scope `calendar.settings` – in structure.md/api.md so dokumentiert.
