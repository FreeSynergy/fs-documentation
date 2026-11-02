# Outlook-Kalender – API (Microsoft Graph v1.0, Stand: 2026-11-02)

## Versionsstand und Entwicklung

- **Produkt aktiv:** Outlook-Kalender (Outlook on the web / neues Outlook für Windows / Outlook für Mac / Outlook für iOS & Android) mit Backend **Exchange Online** wird aktiv entwickelt; die Kalender-API heißt **Microsoft Graph** (`v1.0` stabil, `beta` Vorschau).
- **Nachfolger-Ablösung EWS:** Exchange Web Services erhalten seit 2018 keine Funktionsupdates mehr; in Exchange Online wurde **Oktober 2026 mit der Abschaltung begonnen** („starts to be disabled globally for all organizations"), **April 2027 ist EWS vollständig deaktiviert**. On-Premises-**Exchange Server** sind von der Abschaltung nicht betroffen. (Offizielle Deprecation-Seite, Fundstelle unten.)
- **Graph-Grundlagen:** REST-API auf Basis von **OAuth 2.0** (Authentifizierung), **OData 4.0** und **JSON**; anwendungsseitig eng gefächerte Berechtigungen möglich.

| API-Ebene | Basis-URL | Status (Stand 2026-11-02) |
|-----------|-----------|---------------------------|
| Microsoft Graph v1.0 | `https://graph.microsoft.com/v1.0/` | offiziell, stabil, aktiv entwickelt |
| Microsoft Graph beta | `https://graph.microsoft.com/beta/` | Vorschau, nicht produktionsversprochen |
| EWS (Exchange Online) | `https://outlook.office365.com/EWS/Exchange.asmx` | Abschaltung läuft: ab Okt 2026 tenantweise Aus, Apr 2027 komplett aus |
| EWS (Exchange Server on-prem) | `{server}/EWS/Exchange.asmx` | weiterhin vorhanden, eigene Doku, hier nicht dokumentiert |
| Webhooks | Graph change notifications | vorhanden (siehe unten) – Gegenstück zu „keine Webhooks" bei Nextcloud Calendar |

## Kalender-Ressourcen und Endpunkte (Graph v1.0)

Alle folgenden Methoden/Properties sind auf den offiziellen Resource-Seiten `calendar` bzw. `event` (graph-rest-1.0) verifiziert.

### Kalender (`calendar`-Ressource, Namespace `microsoft.graph`)

- Container für Events; gehört einem Nutzer oder ist der Standardkalender einer Microsoft-365-Gruppe.
- **Methoden:** `List calendars`, `Create calendar`, `Get calendar`, `Update calendar`, `Delete calendar`, `Permanently delete`, **`Get delta`** (inkrementelle Änderungserkennung), **`List calendar view`** (Zeitfenster-Abfrage liefert Occurrences, Ausnahmen und Einzeltermine einer Serie – `GET /me/calendarview?startDateTime=…&endDateTime=…` bzw. pro Kalender), `List events`, `Create event`, **`Get free/busy schedule`** (`getSchedule` für Nutzer, Verteilerlisten, Ressourcen), **`Find meeting times`** (`findMeetingTimes`: Terminvorschläge aus Verfügbarkeit der Teilnehmer), Extended Properties (single-/multi-value).
- **Eigenschaften (vollständig belegt):** `canEdit`, `canShare`, `canViewPrivateItems`, `changeKey` (Versions-/Konkurrenzschutz), `color` (11 enum-Werte `auto…maxColor`) + `hexColor`, `isDefaultCalendar`, `isRemovable`, `isSharedWithMe` (per Outlook-Client geteilter Kalender), `isTallyingResponses` (Response-Tracking nur im Primärkalender), `name`, `owner` (emailAddress), `allowedOnlineMeetingProviders` / `defaultOnlineMeetingProvider` (`teamsForBusiness` u. a.).
- **Freigaben als Modell:** die Assoziation **`calendarPermissions`** (Ressource `calendarPermission`) führt die Rechte der Nutzer, mit denen der Kalender geteilt ist – Freigabe ist also auch über die API ablesbar/verwaltbar (Start/Ende der Freigabe erfolgt im Outlook-Client, Rücknahme auch über `calendarPermission`).
- **Gruppenkalender-Grenzen (offiziell dokumentiert):** Kalendergruppen (`calendarGroups`) nur für Nutzerkalender; Meeting-Anfragen für Gruppen akzeptiert Outlook automatisch; annehmen/ablehnen und Erinnerungen nur bei Nutzerkalendern.

### Termine (`event`-Ressource)

- **Methoden:** list/create/get/update/delete, `Permanently delete` (in Purge-Freigabeordner), **`Get delta`**, **`Forward`**, **`Cancel`** (Absage an alle Teilnehmer), **`Accept` / `TentativelyAccept` / `Decline`**, **`DismissReminder` / `SnoozeReminder`**, **`List event instances`** (Einzeltermine einer Serie), **Attachments** (`List attachments`, `Add attachment`), Open Extensions, Extended Properties.
- **Eigenschaften (verifizierter Auszug):** `subject`, `start`/`end` (`DateTimeTimeZone`), `isAllDay`, `isOnlineMeeting` + `onlineMeeting` (Join-Infos, Read-only), `attendees` (max. **500** Teilnehmer/Empfänger je Ereignis inkl. eventMessage), `organizer`, `isOrganizer`, `isDraft`, `isCancelled`, `cancelledOccurrences` (Verwaiste Instanzen einer Serie), `seriesMasterId` (Serien-Master), `iCalUId` (kalendarübergreifende UID, pro Occurrence unterschiedlich), `recurrence` (Typ `PatternedRecurrence`; Wiederholungsmuster), `type` (`singleInstance`/`occurrence`/`exception`/`seriesMaster`), `transactionId` (clientseitige Idempotenz-Kennung gegen doppelte POSTs beim Anlegen), `reminderMinutesBeforeStart`/`isReminderOn`, `location` + `locations`, `body` (HTML/Text), `categories`, `importance`, `hideAttendees`, `allowNewTimeProposals` (Teilnehmer dürfen neue Zeit vorschlagen), `responseStatus`, `responseRequested`, `showAs` (`free`/`tentative`/`busy`/`oof`/`workingElsewhere`/`unknown`), `sensitivity` (`normal`/`personal`/`private`/`confidential`), `changeKey`, `webLink`.
- **Online-Meeting-Detail:** `onlineMeetingProvider` (`unknown`/`teamsForBusiness`/`skypeForBusiness`/`skypeForConsumer`) ist nach dem Setzen **nicht mehr änderbar**; `onlineMeetingUrl` ist als **Deprecation-Kandidat** markiert – der Join-Link kommt über `onlineMeeting.joinUrl`.
- **ID-Verhalten:** `id` wechselt standardmäßig beim Verschieben zwischen Containern; mit Header `Prefer: IdType="ImmutableId"` bleiben IDs stabil – wichtig für Verknüpfungen in Fremdsystemen.
- **Deep Links (dokumentiert, aus `webLink`-Beschreibung):** aktuelle Form `https://outlook.office365.com/calendar/item/{event-id}` (Organisationskonto) bzw. `https://outlook.live.com/calendar/item/{event-id}` (Microsoft-Konto); die alte `…/owa/?itemid=…&path=/calendar/item`-Form öffnet nur ältere Web-Versionen; der Link funktioniert **nicht im iFrame** und fordert sonst zum Login auf.

### Teilnahmesteuerung und Verfügbarkeit

- RSVP über `accept`/`tentativelyAccept`/`decline` (nur Nutzerkalender), Organisator-Aktionen `cancel`/`forward`.
- Free/Busy: `getSchedule` (Batch für mehrere Nutzer/Ressourcen), `findMeetingTimes` (Slot-Vorschläge inkl. Ort), `showAs`-Feld je Termin.

## Authentifizierung und Berechtigungen

- **OAuth 2.0** über die Microsoft-Identitätsplattform (Arbeits-/Schulkonto via Entra ID; Privatkonto via Microsoft-Konto); App-Registrierung nötig, keine Passwort-Weitergabe an die App.
- **Calendars-Scopes (verifiziert an der Permissions-Referenz, Abruf 2026-11-02):**

| Scope | Kategorie | Zweck (gekürzt) |
|-------|-----------|-----------------|
| `Calendars.Read` | App + delegiert | Termine in allen Kalendern / Nutzerkalendern lesen |
| `Calendars.ReadBasic` | delegiert | Termine lesen, **ohne** `body`/Anhänge/Extensions |
| `Calendars.ReadBasic.All` | App | Basisdetails über alle Postfächer |
| `Calendars.ReadWrite` | App + delegiert | Termine anlegen/lesen/ändern/löschen |
| `Calendars.Read.Shared` / `Calendars.ReadWrite.Shared` | delegiert | einbezogen: **Delegaten- und freigegebene Kalender** |
| `Calendars.Read.All` / `Calendars.ReadWrite.All` | App | exklusiv für **Arbeitszeiten & Orte** (work hours/locations) aller Nutzer |

- **Privatkonto:** die delegierten Scopes `Calendars.Read`, `Calendars.ReadBasic`, `Calendars.ReadWrite` (und `.Read.Shared`) sind laut Permissions-Seite ausdrücklich **mit persönlichen Microsoft-Konten konsentierbar** – Graph ist für outlook.com-Privatkonten offiziell vorgesehen.
- **Applikationsweite Scopes** (App-Kategorie) verlangen Admin-Einwilligung; Administratoren können per **application access policy** den App-Zugriff auf bestimmte Postfächer eingrenzen (bei mehreren Scopes dokumentiert).
- Die feingranulare Einzelkalender-App-Authentifizierung („single calendar permission") ist ein Legacy-EWS-Konzept und wandert zu Graph-Äquivalenten (Parity-Roadmap auf der EWS-Seite).

## Push / Webhooks

Graph bietet **echte Change Notifications per Webhook-Subscription** (Ressource z. B. `/me/events`), verifiziert an der offiziellen „Receive change notifications through webhooks"-Seite:

- Öffentlich erreichbarer **HTTPS-Endpunkt** nötig; Subscription mit `changeType` (created/updated/deleted) auf die Ressourcen-URL.
- **Zustellung:** 2xx-Antwort innerhalb **3 s** = zugestellt; sonst Retry mit exponentiellem Backoff **bis 4 h**; empfohlen: Validierung + Queue + `202 Accepted`.
- **Endpunkt-Gesundheit:** >10 % Antworten >3 s in 10 min ⇒ Endpunkt gilt als „slow" (Versand um 10 min verzögert); >15 % >10 s ⇒ „drop" (10 min Verwurfe; verlorene Notifications sind nicht wiederherstellbar).
- **Lifecycle:** Access-Token des Endpunkts läuft ~1 h; Subscriptionen müssen erneuert werden (Renewal/Lifecycle-Notifications), sonst enden die Zustellungen.
- Alternative Ziel-Infrastruktur für große Volumina: **Event Hubs / Event Grid** statt HTTP-Endpunkt.
- Die eigentliche Benachrichtigung enthält nur die geänderte Ressourcen-ID – Details danach per `GET` abholen (Delta-Query als Pull-Alternative).

## Limits

- **Throttling:** HTTP **429** mit **`Retry-After`**-Header; Drosselung hängt von Tenant- und App-weitem Volumen ab, Schreiblast wird eher gedrosselt als Lesezugriff; Graph-SDKs behandeln `Retry-After` automatisch. Für Massenextraktion empfiehlt Microsoft **Microsoft Graph Data Connect** statt der REST-API.
- Die Exchange-spezifischen Zahlenwerke (requests je Rollfenster) liegen auf einer separaten „Service-specific limits"-Seite, die am Recherchetag **nicht erreichbar** war (404) – konkrete Zahlen hier daher **nicht verifiziert**.
- Harte fachliche Grenze: **500 Teilnehmer** pro Termin/Empfängerkreis (Event-Ressource).

## SDKs und Clients

- **Microsoft Graph SDKs** für .NET, Java, JavaScript/TypeScript, PowerShell und Go (SDK-Familie offiziell; Retry-Handler in den SDKs bestätigt; Sprachliste aus der SDK-Übersicht, im Detail nicht nachgeprüft).
- Referenz-Explorer: Graph Explorer (learn.microsoft.com/graph/api/overview).
- Da Exchange Online CAL-Standard-Groupware ist: Kalender-Einbindung real praktisch immer Graph; klassische CalDAV-Clients (Thunderbird, DAVx⁵) finden an Outlook.com/Exchange Online **keinen** CalDAV-Zugang (siehe features.md).

## Abgrenzung / Warnungen

- **EWS- Skripte brechen:** Jede Integration auf EWS (auch Drittanbieter-Connectoren) ist ab der tenantweisen Abschaltung (Okt 2026–Apr 2027) tot; Migration zwingend auf Graph. Microsoft stellt EWS-Usage-Reports, EWS-Code-Analyzer und eine Migrations-Roadmap bereit; einige EWS-Fähigkeiten (Public-Folder-CRUD, Discovery-Mailbox) kommen **nie** in Graph.
- Die frühere „Office 365 REST API" (`office365.com/api/v1.0`) ist durch Graph ersetzt (Learn-Konzeptseite verweist ausschließlich auf Graph).
- Graph-Endpunkte sind versionsgebunden (`v1.0` vs. `beta`); nur `v1.0` ist produktionsversprochen.
- Privatkonto (outlook.com): die Calendars-Delegations-Scopes sind für persönliche Microsoft-Konten dokumentiert (siehe Auth-Tabelle); Verfügbarkeit einzelner Komfort-Endpunkte (z. B. `findMeetingTimes`) für Consumer ist trotzdem nicht separat ausgewiesen – **nicht verifiziert**.

## Quellen (Fundstellen, abgerufen 2026-11-02)

- EWS-Abschaltung (offiziell): `https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/deprecation-of-ews-exchange-online` – Timeline 2018/2023/2026/2027, Midnight-Blizzard-Kontext, Parity-Lücken-Tabelle, Tools.
- `calendar`-Ressource: `https://learn.microsoft.com/en-us/graph/api/resources/calendar?view=graph-rest-1.0` (zuletzt aktualisiert **2026-10-15**, komplett gelesen) – Methoden (inkl. calendarView, delta, getSchedule, findMeetingTimes), Properties inkl. `calendarPermissions`, Gruppenkalender-Grenzen.
- `event`-Ressource: `https://learn.microsoft.com/en-us/graph/api/resources/event?view=graph-rest-1.0` (zuletzt aktualisiert 2025-05-15, komplett gelesen) – Methoden (inkl. accept/decline/instances/attachments/delta), Properties (iCalUId, seriesMasterId, cancelledOccurrences, changeKey, allowNewTimeProposals, recurrence, type, transactionId, sensitivity …), 500-Teilnehmer-Limit, `IdType="ImmutableId"`, webLink-URL-Formate.
- Webhooks: `https://learn.microsoft.com/en-us/graph/change-notifications-delivery-webhooks?view=graph-rest-1.0` – 3-s-Fenster, 4-h-Retries, slow/drop-Schwellen, Lifecycle, Event Hubs/Event Grid.
- Throttling: `https://learn.microsoft.com/en-us/graph/throttling` – 429/Retry-After, Graph Data Connect, SDK-Handler.
- Graph-Outlook-API-Konzept: `https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/office-365-rest-apis-for-mail-calendars-and-contacts` (zuletzt aktualisiert 2021-10-11) – OAuth 2.0, OData 4.0, JSON, Ablösung der alten REST-API.
- Graph-Berechtigungen: `https://learn.microsoft.com/en-us/graph/permissions-reference` (Calendars-Abschnitt, Offset-Abruf 2026-11-02) – Scopes, Personal-Konto-Konsent, application access policy.
- Nicht erreichbar am Recherchetag: Graph-„Service-specific limits"-Seite (mehrere Kandidat-URLs 404) – Zahlen bewusst nicht übernommen.
