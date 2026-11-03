# Google Kalender – API (Calendar REST API v3, Stand: Discovery-Revision 2026‑10‑28)

## Versionsstand und Entwicklung

- **Aktuelle und einzige offiziell dokumentierte Version: Calendar REST API v3.** Das maschinenlesbare Discovery-Dokument (`https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest`) trägt die **Revision 20261028**; die Entwickler-Dokumentation wurde zuletzt im Herbst 2026 aktualisiert. Der Dienst wird aktiv weiterentwickelt (2026 u. a. neues Quota-Modell zum 1. Mai 2026, Event‑Labels, Focus‑Time-/Out‑of‑Office-/Working‑Location-Felder).
- Google Calendar ist intensiv in Nutzung (Consumer- und Workspace-Konten); ein Einstellen der API ist nicht erkennbar.
- **Self-Hosting der API ist nicht möglich** – der Dienst läuft ausschließlich in der Google-Cloud. Eine Calendar API v2 (Altbestand) ist in der aktuellen offiziellen Dokumentation nicht mehr enthalten.

| Eigenschaft | Wert |
|-------------|------|
| Basis-URL | `https://www.googleapis.com/calendar/v3/` |
| Batch-Endpunkt | `https://www.googleapis.com/batch/calendar/v3` |
| Discovery | `https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest` (Revision 20261028) |
| Format | JSON über HTTPS; `alt` (z. B. `json`), `fields` (Partial Response), `prettyPrint` als globale Parameter |
| Auth | OAuth 2.0 (`Authorization: Bearer …`), Service Accounts, API-Key nur für öffentliche Kalender |

## Authentifizierung und Scopes

- **OAuth 2.0** ist der Standardweg (Access-Token als Bearer-Header, Refresh-Token für Langzeitintegrationen). Öffentliche Apps mit sensiblen Scopes müssen Googles Verifizierungsprozess durchlaufen.
- **Service Account + Domain-wide Delegation**: Server-zu-Server-Zugriff auf Kalender einer Workspace-Domäne; Workspace-Administratoren können mit `useAdminAccess` in Kalendern der Organisation handeln.
- **API-Key** (`?key=…`): nur für lesende Zugriffe auf öffentliche Kalender ohne Nutzerkontext.
- **Kalender-IDs**: `primary` (Standardkalender des angemeldeten Nutzers), E-Mail-Adresse (Privat-/Gruppen-/Ressourcenkalender), Kalender-ID aus `calendarList.list`.

Vollständige offizielle Scope-Liste (Scopes-Seite, Stand 2026‑09; Basis `https://www.googleapis.com/auth/`):

| Scope | Berechtigung |
|-------|--------------|
| `calendar` | Alle zugänglichen Kalender einsehen, ändern, teilen, endgültig löschen |
| `calendar.readonly` | Alle zugänglichen Kalender nur einsehen/herunterladen |
| `calendar.events` | Termine in allen eigenen Kalendern ansehen und ändern |
| `calendar.events.readonly` | Termine aller Kalender nur ansehen |
| `calendar.events.owned` | Termine in Kalendern, die man besitzt, ansehen/ändern/löschen |
| `calendar.events.owned.readonly` | Termine in eigenen Kalendern nur ansehen |
| `calendar.events.public.readonly` | Termine öffentlicher Kalender nur ansehen |
| `calendar.events.freebusy` | Verfügbarkeit (Free/Busy) zugänglicher Kalender sehen |
| `calendar.freebusy` | Eigene Verfügbarkeit ansehen |
| `calendar.calendars` | Kalendereigenschaften ansehen/ändern, Sekundärkalender anlegen |
| `calendar.calendars.readonly` | Kalendereigenschaften nur ansehen |
| `calendar.calendarlist` | Eigene Kalenderliste einsehen, Kalender hinzufügen/entfernen |
| `calendar.calendarlist.readonly` | Eigene Kalenderliste nur einsehen |
| `calendar.acls` | Freigaben eigener Kalender ansehen/ändern |
| `calendar.acls.readonly` | Freigaben eigener Kalender nur ansehen |
| `calendar.app.created` | Von der App angelegte Sekundärkalender verwalten |
| `calendar.settings` | Kalendereinstellungen ansehen und ändern |
| `calendar.settings.readonly` | Kalendereinstellungen nur ansehen |
| `calendar.addons.execute` / `.addons.current.event.read` / `.addons.current.event.write` | nur für Calendar-Add-ons |

Es gibt **keinen** Scope namens `calendar.push` (Push-Kanäle werden mit den normalen Ressourcen-Scopes angelegt).

## Ressourcen und Endpunkte (exakt, Discovery v3 Rev. 20261028)

| Ressource | Methode | HTTP | Pfad |
|-----------|---------|------|------|
| `calendars` | insert | POST | `/calendars` |
| | get | GET | `/calendars/{calendarId}` |
| | update / patch | PUT / PATCH | `/calendars/{calendarId}` |
| | delete | DELETE | `/calendars/{calendarId}` |
| | clear (alle Termine löschen) | POST | `/calendars/{calendarId}/clear` |
| | transferOwnership (`newDataOwner`, `useAdminAccess`) | POST | `/calendars/{calendarId}/transferOwnership` |
| `calendarList` | list | GET | `/users/me/calendarList` |
| | insert | POST | `/users/me/calendarList` |
| | get | GET | `/users/me/calendarList/{calendarId}` |
| | update / patch | PUT / PATCH | `/users/me/calendarList/{calendarId}` |
| | delete (nur abbestellen) | DELETE | `/users/me/calendarList/{calendarId}` |
| | watch | POST | `/users/me/calendarList/watch` |
| `events` | list | GET | `/calendars/{calendarId}/events` |
| | insert | POST | `/calendars/{calendarId}/events` |
| | get | GET | `/calendars/{calendarId}/events/{eventId}` |
| | update / patch | PUT / PATCH | `/calendars/{calendarId}/events/{eventId}` |
| | delete | DELETE | `/calendars/{calendarId}/events/{eventId}` |
| | import (Termin ohne Einladungs-Mails übernehmen) | POST | `/calendars/{calendarId}/events/import` |
| | quickAdd (`text`-Parameter) | POST | `/calendars/{calendarId}/events/quickAdd` |
| | move (`destination`) | POST | `/calendars/{calendarId}/events/{eventId}/move` |
| | instances | GET | `/calendars/{calendarId}/events/{eventId}/instances` |
| | watch | POST | `/calendars/{calendarId}/events/watch` |
| `acl` | list/insert | GET/POST | `/calendars/{calendarId}/acl` |
| | get/update/patch/delete | GET/PUT/PATCH/DELETE | `/calendars/{calendarId}/acl/{ruleId}` |
| | watch | POST | `/calendars/{calendarId}/acl/watch` |
| `freebusy` | query | POST | `/freeBusy` |
| `colors` | get (Kalender-/Event-Farbpalette) | GET | `/colors` |
| `settings` | list | GET | `/users/me/settings` |
| | get | GET | `/users/me/settings/{setting}` |
| | watch | POST | `/users/me/settings/watch` |
| `channels` | stop | POST | `/channels/stop` |

Hinweise: `calendarList` und `settings` sind fest an `users/me` gebunden – fremde Kalenderlisten sind über die API nicht einsehbar. Ein `events.freeBusy`-Endpunkt existiert in v3 nicht; Free/Busy läuft ausschließlich über `POST /freeBusy`.

## Wichtige Methodenparameter

- **`events.list`**: `timeMin`/`timeMax` (RFC 3339), `singleEvents` (Serien zu Einzelterminen auffächern), `orderBy` (`startTime`), `q` (Freitext über Summary, Beschreibung, Ort, Teilnehmer u. a.), `updatedMin`, `showDeleted`, `showHiddenInvitations`, `eventTypes` (wiederholbar), `privateExtendedProperty`/`sharedExtendedProperty`, `maxResults` (Standard 250), `pageToken`, **`syncToken`** (delta-Sync über `nextSyncToken`), `timeZone`, `maxAttendees`, `iCalUID`.
- **`events.insert`/`update`/`patch`/`import`**: `sendUpdates` (`all` / `externalOnly` / `none`; `sendNotifications` veraltet), `conferenceDataVersion` (0–1, Meet-Konferenzen via `createRequest`), `supportsAttachments` (Dateianhänge), `eventLabelVersion` (0 = `colorId`, 1 = `eventLabelId`). `update` ersetzt immer das ganze Ressourcenobjekt (keine Patch-Semantik); für Teilupdates `get` + ändern + `patch`, Atomarität über ETags.
- **`events.instances`**: Seiten der wiederkehrenden Serie (`timeMin`/`timeMax`, `originalStart`, max. 250 pro Seite).
- **`freebusy.query`**: Request `FreeBusyRequest` mit `timeMin`/`timeMax`, `timeZone`, `items` (Kalender/Gruppen), `calendarExpansionMax`, `groupExpansionMax`; Antwort pro Kalender `busy`-Intervalle und optional `errors`, für Gruppen `groups`.
- **`calendars.*`**: `useAdminAccess` für Workspace-Admins.
- **Optimistische Sperre**: alle Ressourcen tragen `etag`; offizielle Referenz empfiehlt `get` + `update`/`patch` mit ETag für atomare Änderungen.

## Datenmodell (Kurzform, Details in structure.md)

Ressourcen laut Discovery: `Calendar`, `CalendarListEntry`, `Event`, `EventAttendee`, `EventReminder`, `EventDateTime`, `AclRule`, `Setting`, `Channel`, `Colors`, `FreeBusyRequest/Response`, `ConferenceData` (Meet), `EventAttachment`, `EventLabel`, `FocusTimeProperties`, `OutOfOfficeProperties`, `WorkingLocationProperties`, `BirthdayProperties`.

## Push-Benachrichtigungen (Webhooks)

- Watch-fähige Ressourcen: **Acl, CalendarList, Events, Settings** – je eigener `…/watch`-Endpunkt, ein gemeinsamer Stop-Endpunkt `POST /channels/stop` (mindestens `id` + `resourceId`).
- Channel-Anfrage: `id` (projekteindeutig, max. 64 Zeichen), `type: "web_hook"`, `address` (**HTTPS mit gültigem, nicht selbstsigniertem Zertifikat**), optional `token` (max. 256 Zeichen) und `expiration` (Unix ms).
- Antworten liefern `resourceId` (versionsunabhängig) und `resourceUri`; jede Benachrichtigung ist ein HTTPS-POST (User-Agent `APIs-Google`) mit Headern `X-Goog-Channel-ID`, `-Token`, `-Expiration`, `X-Goog-Resource-ID`, `-URI`, `-State` (`sync` | `exists` | `not_exists`), `-Message-Number`.
- **Die Nachricht enthält keinen Termininhalt** – danach die Änderung selbst über `events.list` mit `syncToken` nachziehen.
- Empfänger muss 200/201/202/204/102 antworten; bei 500/502/503/504 wiederholt Google mit exponentiellem Backoff, alle anderen Codes gelten als Fehlzustellung.
- **Keine automatische Verlängerung**: Kanäle vor Ablauf mit neuer `watch`-Anfrage und neuer `id` ersetzen.

## Limits und Quotas (offizielle Usage-Limits-Seite, Stand: Modell seit 1. Mai 2026)

| Grenze | Wert |
|--------|------|
| Anfragen pro Minute pro Cloud-Projekt | 10.000 |
| Anfragen pro Minute pro Nutzer pro Projekt | 600 |
| Tägliche Schwelle pro Projekt (danach geplante Gebühren) | 1.000.000 |
| Fehlercode bei Überschreitung | HTTP 403/429 `usageLimits` (Sliding-Window; exponentielles Backoff empfohlen) |

Zusätzlich **operative Grenzen**, die Google jederzeit anpassen kann (z. B. zu schnelle Schreibvorgänge auf einen einzelnen Kalender). Standardnutzung ist kostenlos; Überschreitungen der Tagesgrenze sollen „später in 2026“ kostenpflichtig werden (mit ≥ 90 Tagen Ankündigung). Quota-Erhöhungen sind in der Google-Cloud-Console beantragbar; Service-Account-Traffic zählt als ein Nutzer. Randnotiz aus der Hilfe: mehr als **400 abonnierte Kalender** in einem Konto verursachen Performance-Probleme.

## Batching

Mehrere Aufrufe pro HTTP-Anfrage über `POST https://www.googleapis.com/batch/calendar/v3` (Multipart, je Teilaufruf mit eigener Auth/Parametern).

## Client-Bibliotheken (offizielle Downloads-Seite)

Stabil: **Java, JavaScript, .NET, Objective-C (REST), PHP, Python (v1/v2)**. Frühes Stadium: **Dart (Beta), Go, Node.js (Alpha), Ruby (Alpha)**. Alle Bibliotheken unterstützen Bearer-OAuth und Push-Kanal-Hilfen.

## Weitere offizielle Schnittstellen

- **Google Tasks API** (`https://tasks.googleapis.com/tasks/v1/…`): Aufgaben, die im Kalender-UI neben Terminen erscheinen; eigener Dienst, nicht Teil von v3.
- **Apps Script-Dienst `CalendarApp`** und **Workspace-Add-ons für Calendar**: Skript-/Erweiterungssteuerung innerhalb des Google-Kontos (`calendar.addons.*`-Scopes).
- **Google Workspace Events API** (`https://workspaceevents.googleapis.com/v1/subscriptions`, Pub/Sub-basiert): offizieller Workspace-Pub/Sub-Mechanismus; ob Kalender-Ressourcen aktuell subscribed werden können, ist in der geprüften Referenzseite nicht belegt (**nicht verifiziert**).

## Was es auf API-Ebene NICHT gibt

- **Kein dokumentiertes CalDAV/CardDAV-Angebot.** Google hat CalDAV/CardDAV-Zugang mit Passwort (Less Secure Apps) für Workspace ab 30.09.2024 bzw. kontenübergreifend ab 2025 abgeschaltet; offizielle Entwickler-Dokumentation nennt nur die REST-API. Community-Tools (DAVx⁵) sprechen Google-Endpunkte weiterhin über OAuth an – laut DAVx⁵ „weder von Google noch von DAVx⁵ offiziell unterstützt“ – als Stütze, nicht als Garantie.
- Kein GraphQL, kein OData, keine eigene Server-/Self-Hosting-Variante, keine API für öffentliche Buchungsseiten („Terminpläne“) – im aktuellen Discovery v3 (Rev. 20261028) existiert weder eine eigene Ressource noch ein `appointment`-Wert für `eventType`; Reservierungsseiten sind reine UI-Funktion.
- Kein Zugriff auf `users/me`-fremde Kalenderlisten, keine Kalender-Such-API (Freigaben laufen über IDs/E-Mail).
