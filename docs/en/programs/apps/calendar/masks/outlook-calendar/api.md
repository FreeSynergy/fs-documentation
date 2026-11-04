# Outlook calendar – API (Microsoft Graph v1.0, as of 2026-11-02)

## Version state and development

- **Product active:** the Outlook calendar (Outlook on the web / new Outlook for Windows / Outlook for Mac / Outlook for iOS & Android) with the **Exchange Online** backend is under active development; the calendar API is called **Microsoft Graph** (`v1.0` stable, `beta` preview).
- **Successor replacing EWS:** Exchange Web Services have received no feature updates since 2018; in Exchange Online **the shutdown began in October 2026** ("starts to be disabled globally for all organizations"), **in April 2027 EWS is fully disabled**. On-premises **Exchange Server** is not affected by the shutdown. (Official deprecation page, location below.)
- **Graph basics:** a REST API based on **OAuth 2.0** (authentication), **OData 4.0** and **JSON**; on the application side narrowly scoped permissions are possible.

| API level | Base URL | Status (as of 2026-11-02) |
|-----------|----------|---------------------------|
| Microsoft Graph v1.0 | `https://graph.microsoft.com/v1.0/` | official, stable, actively developed |
| Microsoft Graph beta | `https://graph.microsoft.com/beta/` | preview, no production promise |
| EWS (Exchange Online) | `https://outlook.office365.com/EWS/Exchange.asmx` | shutdown under way: from Oct 2026 off tenant by tenant, fully off Apr 2027 |
| EWS (Exchange Server on-prem) | `{server}/EWS/Exchange.asmx` | still present, its own documentation, not documented here |
| Webhooks | Graph change notifications | present (see below) — the counterpart to "no webhooks" at Nextcloud Calendar |

## Calendar resources and endpoints (Graph v1.0)

All the methods/properties below are verified on the official `calendar` and `event` resource pages (graph-rest-1.0).

### Calendars (`calendar` resource, namespace `microsoft.graph`)

- A container for events; it belongs to a user or is the default calendar of a Microsoft 365 group.
- **Methods:** `List calendars`, `Create calendar`, `Get calendar`, `Update calendar`, `Delete calendar`, `Permanently delete`, **`Get delta`** (incremental change detection), **`List calendar view`** (a time-window query that returns occurrences, exceptions and single events of a series — `GET /me/calendarview?startDateTime=…&endDateTime=…` or per calendar), `List events`, `Create event`, **`Get free/busy schedule`** (`getSchedule` for users, distribution lists, resources), **`Find meeting times`** (`findMeetingTimes`: meeting suggestions from participant availability), extended properties (single-/multi-value).
- **Properties (fully evidenced):** `canEdit`, `canShare`, `canViewPrivateItems`, `changeKey` (version/concurrency protection), `color` (11 enum values `auto…maxColor`) + `hexColor`, `isDefaultCalendar`, `isRemovable`, `isSharedWithMe` (calendar shared through the Outlook client), `isTallyingResponses` (response tracking only in the primary calendar), `name`, `owner` (emailAddress), `allowedOnlineMeetingProviders` / `defaultOnlineMeetingProvider` (`teamsForBusiness` among others).
- **Sharing as part of the model:** the **`calendarPermissions`** association (resource `calendarPermission`) lists the rights of the users the calendar is shared with — so sharing can also be read/managed through the API (starting/ending a share happens in the Outlook client, revoking also via `calendarPermission`).
- **Group calendar limits (officially documented):** calendar groups (`calendarGroups`) only for user calendars; Outlook automatically accepts meeting requests for groups; accept/decline and reminders only for user calendars.

### Events (`event` resource)

- **Methods:** list/create/get/update/delete, `Permanently delete` (in a purge-shared folder), **`Get delta`**, **`Forward`**, **`Cancel`** (cancellation to all participants), **`Accept` / `TentativelyAccept` / `Decline`**, **`DismissReminder` / `SnoozeReminder`**, **`List event instances`** (the single occurrences of a series), **attachments** (`List attachments`, `Add attachment`), open extensions, extended properties.
- **Properties (verified excerpt):** `subject`, `start`/`end` (`DateTimeTimeZone`), `isAllDay`, `isOnlineMeeting` + `onlineMeeting` (join info, read-only), `attendees` (max. **500** participants/recipients per event including eventMessage), `organizer`, `isOrganizer`, `isDraft`, `isCancelled`, `cancelledOccurrences` (orphaned instances of a series), `seriesMasterId` (the series master), `iCalUId` (a cross-calendar UID, different per occurrence), `recurrence` (type `PatternedRecurrence`; recurrence pattern), `type` (`singleInstance`/`occurrence`/`exception`/`seriesMaster`), `transactionId` (client-side idempotency marker against duplicate POSTs while creating), `reminderMinutesBeforeStart`/`isReminderOn`, `location` + `locations`, `body` (HTML/text), `categories`, `importance`, `hideAttendees`, `allowNewTimeProposals` (participants may propose a new time), `responseStatus`, `responseRequested`, `showAs` (`free`/`tentative`/`busy`/`oof`/`workingElsewhere`/`unknown`), `sensitivity` (`normal`/`personal`/`private`/`confidential`), `changeKey`, `webLink`.
- **Online meeting detail:** `onlineMeetingProvider` (`unknown`/`teamsForBusiness`/`skypeForBusiness`/`skypeForConsumer`) is **no longer changeable** once set; `onlineMeetingUrl` is marked as a **deprecation candidate** — the join link comes through `onlineMeeting.joinUrl`.
- **ID behaviour:** by default `id` changes when moving between containers; with the header `Prefer: IdType="ImmutableId"` IDs stay stable — important for links in foreign systems.
- **Deep links (documented, from the `webLink` description):** current form `https://outlook.office365.com/calendar/item/{event-id}` (organisation account) or `https://outlook.live.com/calendar/item/{event-id}` (Microsoft account); the old `…/owa/?itemid=…&path=/calendar/item` form only opens older web versions; the link does **not work in an iFrame** and otherwise prompts for a login.

### Attendance control and availability

- RSVP via `accept`/`tentativelyAccept`/`decline` (user calendars only), organiser actions `cancel`/`forward`.
- Free/busy: `getSchedule` (batch for several users/resources), `findMeetingTimes` (slot suggestions including location), the `showAs` field per event.

## Authentication and permissions

- **OAuth 2.0** over the Microsoft identity platform (work/school account via Entra ID; private account via Microsoft account); an app registration is required, no password is handed to the app.
- **Calendars scopes (verified against the permissions reference, retrieved 2026-11-02):**

| Scope | Category | Purpose (abridged) |
|-------|----------|--------------------|
| `Calendars.Read` | app + delegated | read events in all calendars / user calendars |
| `Calendars.ReadBasic` | delegated | read events **without** `body`/attachments/extensions |
| `Calendars.ReadBasic.All` | app | basic details across all mailboxes |
| `Calendars.ReadWrite` | app + delegated | create/read/change/delete events |
| `Calendars.Read.Shared` / `Calendars.ReadWrite.Shared` | delegated | included: **delegate and shared calendars** |
| `Calendars.Read.All` / `Calendars.ReadWrite.All` | app | exclusively for the **work hours & locations** of all users |

- **Private accounts:** the delegated scopes `Calendars.Read`, `Calendars.ReadBasic`, `Calendars.ReadWrite` (and `.Read.Shared`) are, according to the permissions page, explicitly **consentable with personal Microsoft accounts** — Graph is officially intended for outlook.com private accounts.
- **Application-wide scopes** (app category) require admin consent; administrators can restrict the app's access to particular mailboxes with an **application access policy** (documented for several scopes).
- The fine-grained single-calendar app authentication ("single calendar permission") is a legacy EWS concept and is moving to Graph equivalents (parity roadmap on the EWS page).

## Push / webhooks

Graph offers **real change notifications via webhook subscription** (resource e.g. `/me/events`), verified on the official "Receive change notifications through webhooks" page:

- A publicly reachable **HTTPS endpoint** is required; a subscription with `changeType` (created/updated/deleted) on the resource URL.
- **Delivery:** a 2xx response within **3 s** = delivered; otherwise a retry with exponential backoff **for up to 4 h**; recommended: validation + queue + `202 Accepted`.
- **Endpoint health:** more than 10 % of responses over 3 s within 10 min ⇒ the endpoint counts as "slow" (delivery delayed by 10 min); more than 15 % over 10 s ⇒ "drop" (dropped for 10 min; lost notifications cannot be recovered).
- **Lifecycle:** the endpoint's access token expires after about 1 h; subscriptions must be renewed (renewal/lifecycle notifications), otherwise delivery ends.
- Alternative target infrastructure for large volumes: **Event Hubs / Event Grid** instead of an HTTP endpoint.
- The notification itself contains only the changed resource ID — fetch the details afterwards with a `GET` (a delta query as the pull alternative).

## Limits

- **Throttling:** HTTP **429** with a **`Retry-After`** header; the throttling depends on tenant- and app-wide volume, write load is throttled sooner than read access; the Graph SDKs handle `Retry-After` automatically. For bulk extraction Microsoft recommends **Microsoft Graph Data Connect** over the REST API.
- The Exchange-specific figures (requests per rolling window) live on a separate "service-specific limits" page that was **unreachable** on the research day (404) — the concrete numbers are therefore **not verified** here.
- A hard functional limit: **500 participants** per event/recipient list (event resource).

## SDKs and clients

- **Microsoft Graph SDKs** for .NET, Java, JavaScript/TypeScript, PowerShell and Go (the SDK family is official; retry handlers confirmed in the SDKs; the language list comes from the SDK overview, not re-checked in detail).
- Reference explorer: Graph Explorer (learn.microsoft.com/graph/api/overview).
- Since Exchange Online is the standard groupware here: calendar integration is in practice always Graph; classic CalDAV clients (Thunderbird, DAVx⁵) find **no** CalDAV access at Outlook.com/Exchange Online (see features.md).

## Distinctions / warnings

- **EWS scripts break:** any integration on EWS (including third-party connectors) is dead from the tenant-wise shutdown (Oct 2026–Apr 2027); migration to Graph is mandatory. Microsoft provides EWS usage reports, an EWS code analyser and a migration roadmap; some EWS capabilities (public-folder CRUD, the discovery mailbox) **never** come to Graph.
- The former "Office 365 REST API" (`office365.com/api/v1.0`) has been replaced by Graph (the Learn concept page points exclusively to Graph).
- Graph endpoints are version-bound (`v1.0` vs `beta`); only `v1.0` carries a production promise.
- Private account (outlook.com): the Calendars delegated scopes are documented for personal Microsoft accounts (see the auth table); the availability of individual convenience endpoints (e.g. `findMeetingTimes`) for consumers is nevertheless not separately stated — **not verified**.

## Sources (locations, retrieved 2026-11-02)

- EWS shutdown (official): `https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/deprecation-of-ews-exchange-online` – timeline 2018/2023/2026/2027, Midnight Blizzard context, the parity-gaps table, tools.
- `calendar` resource: `https://learn.microsoft.com/en-us/graph/api/resources/calendar?view=graph-rest-1.0` (last updated **2026-10-15**, read in full) – methods (incl. calendarView, delta, getSchedule, findMeetingTimes), properties incl. `calendarPermissions`, group calendar limits.
- `event` resource: `https://learn.microsoft.com/en-us/graph/api/resources/event?view=graph-rest-1.0` (last updated 2025-05-15, read in full) – methods (incl. accept/decline/instances/attachments/delta), properties (iCalUId, seriesMasterId, cancelledOccurrences, changeKey, allowNewTimeProposals, recurrence, type, transactionId, sensitivity …), the 500-participant limit, `IdType="ImmutableId"`, webLink URL formats.
- Webhooks: `https://learn.microsoft.com/en-us/graph/change-notifications-delivery-webhooks?view=graph-rest-1.0` – the 3 s window, 4 h retries, slow/drop thresholds, lifecycle, Event Hubs/Event Grid.
- Throttling: `https://learn.microsoft.com/en-us/graph/throttling` – 429/Retry-After, Graph Data Connect, SDK handlers.
- Graph Outlook API concept: `https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/office-365-rest-apis-for-mail-calendars-and-contacts` (last updated 2021-10-11) – OAuth 2.0, OData 4.0, JSON, the replacement of the old REST API.
- Graph permissions: `https://learn.microsoft.com/en-us/graph/permissions-reference` (Calendars section, fetched by offset 2026-11-02) – scopes, personal-account consent, application access policy.
- Unreachable on the research day: the Graph "service-specific limits" page (several candidate URLs 404) — the figures were deliberately not taken over.
