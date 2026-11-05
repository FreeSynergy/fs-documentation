# Outlook-Kalender – Struktur (Stand: 2026-11-02)

Fundstellen in [index.md](../index.md#quellen). Markierungen: *(verifiziert)* = direkt auf der zitierten offiziellen Seite abgelesen; *(Sekundär)* = Community-/Fachblog-Quelle; *(nicht verifiziert)* = allgemein bekannt, aber in diesem Durchlauf nicht belegt.

## Bauschichten (Request-Ablauf)

1. **Clients:** neues Outlook für Windows (Web-Codebasis als Windows-App – teilt sich Menüs/Kürzel weitgehend mit Outlook on the web *(verifiziert über identische Kürzel-/Layoutartikel)*), Outlook on the web (outlook.com privat bzw. outlook.office.com Organisation), klassisches Outlook für Windows (MAPI-Vollclient, Ribbon/COM-Add-ins/VBA *(verifiziert: VBA-Kürzel nur im „Classic“-Teil der Kürzelseite)*), Outlook für Mac, Outlook für iOS/Android.
2. **Zugriffsschicht:** **Microsoft Graph v1.0/beta** (REST, OAuth 2.0, OData 4.0/JSON) als moderne API *(verifiziert)*; älter: EWS (Abschaltung Exchange Online Okt 2026→Apr 2027 *(verifiziert)*), EAS (mobil; ab 2026 nur noch EAS ≥ 16.1 *(Sekundär: petri.com/windowsforum)*), MAPI (klassischer Desktop).
3. **Backend:** Exchange Online – Termine sind **Postfachobjekte** im Kalenderordner-Modell, kein ICS-Dateispeicher wie bei CalDAV-Servern. Auf each Objekt ein **`changeKey`** für Konkurrenzschutz *(verifiziert an calendar-/event-Ressource)*.
4. **Ereignis-Pipeline für Integrationen:** Graph-**Change-Notifications** (Webhook-Subscriptions mit Lifecycle-Erneuerung) oder Delta-Queries als Pull *(verifiziert)*.

## Datenmodell (Graph-Ressourcen, verifiziert)

- **`calendar`** – Ordner über Terminen; Eigenschaften u. a. `name`, `owner`, `color`/`hexColor`, `isDefaultCalendar`, `isRemovable`, `isSharedWithMe`, `isTallyingResponses`, `canEdit`/`canShare`/`canViewPrivateItems`, `changeKey`, `allowedOnlineMeetingProviders`; gruppierbar in `calendarGroups` (nur Nutzerkalender); Freigaben als **`calendarPermissions`**-Assoziation (Ressource `calendarPermission`).
- **`event`** – `id` (mutable; `Prefer: IdType="ImmutableId"` für stabile IDs), **`iCalUId`** (UID pro Occurrence), **`seriesMasterId`** + **`cancelledOccurrences`** + `exceptionOccurrences` (Serienmodell: Master ↔ Occurrences ↔ Ausnahmen; `instances` exklusive cancellierter), `type` (`singleInstance`/`occurrence`/`exception`/`seriesMaster`), `start`/`end` als `DateTimeTimeZone`, `isAllDay`, `recurrence` (`PatternedRecurrence`), `attendees` (≤ 500), `responseStatus`/`responseRequested`, `showAs` (Free/Busy), `sensitivity`, `isOnlineMeeting`/`onlineMeeting`(+`onlineMeetingProvider`, fix nach Setzen; `onlineMeetingUrl` deprecated), `attachments` (File/Item/reference), `categories`, `isDraft`, `transactionId` (Idempotenz), `webLink` (Deep Link `…/calendar/item/{id}`, kein iFrame), `body`, `location`/`locations`, `allowNewTimeProposals`, `hideAttendees`, `importance`, `changeKey`.
- **Aktionen als Modellbestandteil:** `accept`/`tentativelyAccept`/`decline`/`cancel`/`forward`, `snoozeReminder`/`dismissReminder`, `instances`, `getSchedule`, `findMeetingTimes`, `delta`.
- **Ressourcen (Räume/Ausstattung):** über `getSchedule` als eigene Objektart ansprechbar *(verifiziert an getSchedule-Beschreibung: „users, distributions lists, or resources“)*.

## Modul-/Oberflächenstruktur der Clients

- **Neues Outlook / OWA:** horizontale Navigationsleiste (Suche, My Day, Benachrichtigungen, Hilfe, Einstellungen) → Ribbon-Reiter (Home u. a.) → linkes Navigationsfenster (New event, Datumsauswahl, Kalenderliste; ganz links Umschalter Mail/Calendar/Contacts/To Do) → Kalenderbereich mit Toolbar (Monats-Picker, Ansichten Day/Work week/Week/Month/Today, Share) *(alle Regionen verifiziert im Screenreader-Artikel)*.
- **Klassisches Outlook:** Ribbon + Folder pane (Kalenderordner, Feiertags-/Shared-Kalender) + Kalenderansicht + Statusleiste *(verifiziert)*; Calendar-Settings-Dialog, Assistent für die Terminplanung, Erinnerungsfenster *(verifiziert über Access-Key-Kürzel)*.
- **Settings-Fenster (neues Outlook):** Reiter *Calendar* mit Unterreitern; belegte Punkte: Arbeitszeiten/-tage, Abwesenheitsnotizen, Standard-Erinnerungszeit *(verifiziert)*.

## Konfiguration

- **Nutzer:** Kalenderfarben/-listen, Standarderinnerung, Arbeitszeit/-tage, Ansicht (UI; per Graph `calendar`-PATCH bzw. Postfacheinstellungen).
- **Admin (Exchange Online):** Postfach- und Ordnerberechtigungen per PowerShell/EAC, Freigabe-/Verfügbarkeitsrichtlinien zwischen Mandanten (Cross-Tenant Access Policy, Migrationsartikel auf learn.microsoft.com), Ressourcenpostfächer. *(Existenz verifiziert über learn-Artikel; Einzelparameter nicht abgelesen.)*
- **App-Registrierung (Entwickler):** OAuth-Scopes, Webhook-Endpunkt (HTTPS, 3-s-Antwort), Subscription-Renewal – Details in [api.md](api.md).

## Deployment

- **SaaS:** Microsoft 365 / Exchange Online; Outlook on the web ohne Installation; neues Outlook für Windows als vorinstallierter/pushbarer Client. **On-prem:** Exchange Server (ältere Protokolle inklusive EWS dort weiter aktiv – eigene Support-Lebenslinien *(Randnotiz, im Detail nicht verifiziert)*).
- **Client-Migration ( timelines ):** neues Outlook ersetzt schrittweise Mail-/Kalender-Apps von Windows; kostenlose Outlook.com-Konten können **seit Januar 2025 nicht mehr zum klassischen Outlook zurückwechseln** *(Sekundär: techcommunity-Beitrag)*; die Kalenderfreigabe wird 2026 tenantweise von MAPI auf ein **REST-Modell** umgestellt *(Sekundär: office365itpros.com 2026-05, admin365.blog 2026-07; Abschlussfrist März 2027 genannt)*.
- **Protokoll-Härtung 2026:** EWS-Abschaltung Exchange Online (Okt 2026 Start, Apr 2027 komplett) *(verifiziert)*; EAS-Clients < 16.1 blockiert *(Sekundär)*.

## Betriebshinweise

- Webhook-Endpunkte brauchen Betriebs-SLA (3-s-Antwort, 4-h-Retries, slow/drop-Verhalten) oder Event Hubs/Event Grid *(verifiziert)*.
- Integrationen müssen auf **immutable IDs** und `changeKey`-Konfliktbehandlung achten *(verifiziert)*.
- EWS-Restbestände frühzeitig migrieren; Microsoft bietet EWS-Usage-Reports und EWS-Code-Analyzer *(verifiziert)*.
