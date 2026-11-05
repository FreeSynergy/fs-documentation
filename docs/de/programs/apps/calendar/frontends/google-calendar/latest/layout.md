# Google Kalender – Struktur (Stand: 2.11.2026)

Google Calendar ist Closed Source; Interne Prozess-/Serverarchitektur sind nicht öffentlich. Diese Datei dokumentiert den **offiziell belegbaren** Aufbau: externer Request-Ablauf, öffentliche Ressourcen-/Modulstruktur der API v3, Datenmodell, Konfigurationsoberflächen und Deployment-Realität. Quellen: Discovery v3 (Revision 20261028) + offizielle Hilfeseiten (URLs in [index.md](../index.md)).

## Request-Ablauf

### Nutzung über die Oberfläche

Browser/Apps (Android, iOS, Wear OS, Apple Watch) → `https://calendar.google.com` bzw. Google-Konto-Sync der Apps → Google-Backend (intern, undokumentiert). Änderungen stehen sofort auf allen Google-Kanälen; ICS-Adressen (öffentlich/geheim je Kalender) dienen externen Clients zum Abo.

### Nutzung über die API v3 (dokumentierter Weg)

```
1. OAuth-2.0-Handshake:
   Consent-Screen (Scope-Auswahl) → Zugangs-/Refresh-Token
   (alternativ: Service Account + Domain-wide Delegation; API-Key nur für öffentliche Kalender)

2. API-Aufrufe:
   HTTPS + Authorization: Bearer → https://www.googleapis.com/calendar/v3/…
   Antworten als JSON, je Ressource mit etag (optimistische Sperre)

3. Synchronisation:
   Vollsynchronisation mit events.list (timeMin/timeMax, singleEvents)
   → nextSyncToken merken
   → nächste Änderung als Delta: events.list?syncToken=… (updatedMin, showDeleted)

4. Push statt Polling:
   POST …/events/watch {id, type:"web_hook", address:"https://…"}
   → Google sendet header-only POSTs (X-Goog-Resource-State: sync|exists|not_exists)
   → Empfänger antwortet mit 200/201/202/204/102 und zieht Delta per syncToken nach
   → Kanal läuft ab und muss mit neuer id erneuert werden; Stop via POST /channels/stop

5. Batching:
   POST https://www.googleapis.com/batch/calendar/v3 (Multipart mehrerer Aufrufe)

6. Free/Busy:
   POST /freeBusy {timeMin,timeMax,items:[{id:…}]} → busy-Intervalle je Kalender
   (Gruppen werden mit expandiert: groupExpansionMax)
```

## Modul-/Ressourcenstruktur (öffentliche API-Oberfläche)

Acht Ressourcengruppen laut Discovery v3:

| Gruppe | Zweck |
|--------|-------|
| `calendars` | Kalenderstamm (anlegen/ändern/löschen/clear/transferOwnership) |
| `calendarList` | nutzerbezogene Kalenderliste (`users/me`): Sichtbarkeit, Farben, Erinnerungen, watch |
| `events` | Termine inkl. import/quickAdd/move/instances/watch |
| `acl` | Freigaberegeln je Kalender inkl. watch |
| `freebusy` | Verfügbarkeitsabfrage (POST) |
| `colors` | Farbpaletten (Kalender/Termine) |
| `settings` | Nutzeroberfläche-Einstellungen als Key/Value (`users/me/settings`, watch) |
| `channels` | Push-Kanäle beenden (ein Stop-Endpunkt für alle watch-Ressourcen) |

39 Schemas, u. a.: `Event`, `EventAttendee`, `EventDateTime`, `EventReminder`, `EventAttachment`, `EventLabel`, `EventFocusTimeProperties`, `EventOutOfOfficeProperties`, `EventWorkingLocationProperties`, `EventBirthdayProperties`, `ConferenceData`/`EntryPoint` (Meet), `Calendar`, `CalendarListEntry`, `AclRule`, `Setting`, `Channel`, `Colors`, `FreeBusyRequest/Response`, `FreeBusyCalendar/Group`, `TimePeriod`.

## Datenmodell

- **Calendar**: `summary`, `description`, `timeZone`, `location`, `conferenceProperties` (erlaubte Konferenztypen), `autoAcceptInvitations`, `dataOwner`, `labelProperties`.
- **CalendarListEntry** (nutzerspezifische Ansicht desselben Kalenders): `primary`, `selected`, `hidden`, `colorId`/`backgroundColor`/`foregroundColor`, `defaultReminders`, `notificationSettings`, `summaryOverride`, `timeZone`, `deleted`, `accessRole`, `dataOwner`, `autoAcceptInvitations`.
  *Achtung, verifizierter Schema-Wandel:* die früheren Felder `summaryVisibility` und `subscriptionType` kommen in der Discovery-Revision 20261028 **nicht mehr vor** – ältere Dritt-Doku ist hier überholt.
- **Zugriffsrollen** (`accessRole`, `AclRule`): `freeBusyReader`, `reader`, `writerWithoutPrivateAccess` (neu: schreiben ohne private Details), `writer`, `owner`; ACL-Scopes: `user`, `group`, `domain`, `default` (public). Wichtige Unterscheidung laut API: **owner-Rolle ≠ dataOwner** (mehrere owner möglich, ein dataOwner; Wechsel via `calendars.transferOwnership`).
- **Event**:
  - Zeit: `start`/`end` als `EventDateTime` (`dateTime` mit Offset oder `date` für Ganztage), `endTimeUnspecified`, `recurrence` (RRULE-Zeilen), `originalStartTime`, `recurringEventId`, `sequence`, `created`/`updated`
  - Identität: `id`, `iCalUID`, `etag`, `htmlLink`
  - Status/Sicht: `status` (`confirmed`/`tentative`/`cancelled`), `transparency` (`opaque`/`transparent`), `visibility` (`default`/`public`/`private`), `locked`, `privateCopy`
  - Typen (`eventType`): `default`, `birthday`, `focusTime`, `fromGmail` (nicht erstellbar), `outOfOffice`, `workingLocation` – mit eigenen Property-Blöcken
  - Teilnehmer: `attendees[]` (`email`, `displayName`, `optional`, `resource`, `organizer`, `self`, `responseStatus` needsAction/declined/accepted/tentative, `additionalGuests`, `comment`), `attendeesOmitted`, Gastschalter (`guestsCanInviteOthers`, `guestsCanModify`, `guestsCanSeeOtherGuests`)
  - Sonstiges: `reminders` + `reminderOverrides`, `attachments[]` (Drive/URL), `eventLabelId` (Labels via eventLabelVersion=1), `conferenceData` (Meet-Konferenz, `createRequest`), `extendedProperties` (private/shared), `source`, `colorId`, `gadget` (Altbestand)
- **Setting**: `id`/`value` pro Nutzer (die API-Doku nennt als Beispiel die Zeitzone; die vollständige ID-Liste ist nicht veröffentlicht → **nicht verifiziert**), änderbar über die UI, lesbar/überwachbar über `users/me/settings`.
- **Channel**: `id`, `resourceId`, `resourceUri`, `address`, `expiration`, `token`, `params`.

## Konfiguration

| Ebene | Wo | Belegte Beispiele |
|-------|----|-------------------|
| Nutzer (UI) | Zahnrad → „Einstellungen“ | „Tastenkombinationen aktivieren“, „Ansichtsoptionen“ (Wochenbeginn, benutzerdefinierte Ansicht), „Importieren & Exportieren“ |
| Nutzer (API) | `settings`-Ressource | Zeitzone u. a. (vollständige Liste nicht veröffentlicht) |
| Kalender (Stamm) | `calendars` + UI „Einstellungen und Freigabe“ | Name, Zeitzone, Beschreibung, Ort, iCal-Adressen (öffentlich/geheim), Freigabeliste, Export |
| Kalender (pro Nutzer) | `calendarList` | Farbe, Auswahl/Ausgeblendet, Standarderinnerungen, Benachrichtigungen |
| Terminplan | UI „Eintragen → Terminplan“ | Termindauer, Verfügbarkeitsfenster, Puffer, Max/Tag, Gästerechte, Zielkalender |
| Workspace-Admin | Admin-Konsole | Zahlungen für Terminpläne (Stripe) ON/OFF, Time Insights deaktivierbar, Export einschränkbar; LSA/G-Sync-Schalter entfielen 2024/2025 |
| API-Nutzung | Google-Cloud-Projekt | OAuth-Zustimmungsbildschirm, Scopes, Quota-Verwaltung, API-Key |

## Deployment

- **Ausschließlich Google-SaaS**: kein Server-Image, keine Eigeninstallation, keine On-Premises-Variante; Datenhaltung in Google-Rechenzentren (genaue Region/Redundanz für Kalender publiziert Google nicht → **nicht verifiziert**).
- UI und Apps werden kontinuierlich ausgerollt (Workspace-Updates-Blog unterscheidet „Rapid Release“ und „Scheduled Release“).
- API-Stand über Discovery-Revisionen versioniert (aktuell 20261028); Breaking-Change-Schutz über ETags und Versionsparameter (`conferenceDataVersion`, `eventLabelVersion`).
- Abrechnung/Quota: Standardnutzung kostenlos; Quota-Modell für Projekte ab 1. Mai 2026, Bepreisung oberhalb der Tagesgrenze für „später in 2026“ angekündigt.

## Einordnung im FreeSynergy-Kontext

Anders als DAViCal (offener Request-Ablauf: PROPFIND/PUT/REPORT nach RFC 4791 gegen eigenen Server) ist Google Calendar nur über den REST-Fluss oben anbindbar: eigene OAuth-App, Sync-Token-Deltas und Watch-Kanäle. Ein Austausch mit CalDAV-Clients ist offiziell nicht vorgesehen; Brücken müssen die Calendar API v3 (oder ICS-Abos im Lesebetrieb) verwenden.
