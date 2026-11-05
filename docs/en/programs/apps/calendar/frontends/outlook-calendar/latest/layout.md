# Outlook calendar – Structure (as of 2026-11-02)

Locations in [index.md](../index.md#sources). Markers: *(verified)* = read directly off the cited official page; *(secondary)* = community/ specialist-blog source; *(not verified)* = generally known but not evidenced in this pass.

## Build layers (request flow)

1. **Clients:** the new Outlook for Windows (web code base as a Windows app — largely shares menus/shortcuts with Outlook on the web *(verified through the identical shortcut/layout articles)*), Outlook on the web (outlook.com for private users or outlook.office.com for organisations), classic Outlook for Windows (full MAPI client, ribbon/COM add-ins/VBA *(verified: VBA shortcuts only in the "Classic" part of the shortcuts page)*), Outlook for Mac, Outlook for iOS/Android.
2. **Access layer:** **Microsoft Graph v1.0/beta** (REST, OAuth 2.0, OData 4.0/JSON) as the modern API *(verified)*; older: EWS (shutdown in Exchange Online Oct 2026→Apr 2027 *(verified)*), EAS (mobile; from 2026 only EAS ≥ 16.1 *(secondary: petri.com/windowsforum)*), MAPI (classic desktop).
3. **Backend:** Exchange Online — events are **mailbox objects** in the calendar-folder model, not an ICS file store as with CalDAV servers. Every object carries a **`changeKey`** for concurrency protection *(verified against the calendar/event resource)*.
4. **Event pipeline for integrations:** Graph **change notifications** (webhook subscriptions with lifecycle renewal) or delta queries as pull *(verified)*.

## Data model (Graph resources, verified)

- **`calendar`** – a folder over events; properties include `name`, `owner`, `color`/`hexColor`, `isDefaultCalendar`, `isRemovable`, `isSharedWithMe`, `isTallyingResponses`, `canEdit`/`canShare`/`canViewPrivateItems`, `changeKey`, `allowedOnlineMeetingProviders`; groupable into `calendarGroups` (user calendars only); shares as the **`calendarPermissions`** association (resource `calendarPermission`).
- **`event`** – `id` (mutable; `Prefer: IdType="ImmutableId"` for stable IDs), **`iCalUId`** (a UID per occurrence), **`seriesMasterId`** + **`cancelledOccurrences`** + `exceptionOccurrences` (the series model: master ↔ occurrences ↔ exceptions; `instances` excluding cancelled ones), `type` (`singleInstance`/`occurrence`/`exception`/`seriesMaster`), `start`/`end` as `DateTimeTimeZone`, `isAllDay`, `recurrence` (`PatternedRecurrence`), `attendees` (≤ 500), `responseStatus`/`responseRequested`, `showAs` (free/busy), `sensitivity`, `isOnlineMeeting`/`onlineMeeting` (+`onlineMeetingProvider`, fixed once set; `onlineMeetingUrl` deprecated), `attachments` (File/Item/reference), `categories`, `isDraft`, `transactionId` (idempotency), `webLink` (deep link `…/calendar/item/{id}`, not an iFrame), `body`, `location`/`locations`, `allowNewTimeProposals`, `hideAttendees`, `importance`, `changeKey`.
- **Actions as part of the model:** `accept`/`tentativelyAccept`/`decline`/`cancel`/`forward`, `snoozeReminder`/`dismissReminder`, `instances`, `getSchedule`, `findMeetingTimes`, `delta`.
- **Resources (rooms/equipment):** addressable through `getSchedule` as their own object kind *(verified against the getSchedule description: "users, distributions lists, or resources")*.

## Module/interface structure of the clients

- **New Outlook / OWA:** horizontal navigation bar (search, My Day, notifications, help, settings) → ribbon tabs (Home among others) → left navigation window (New event, date selector, calendar list; far left the switcher Mail/Calendar/Contacts/To Do) → calendar area with a toolbar (month picker, views Day/Work week/Week/Month/Today, Share) *(all regions verified in the screen-reader article)*.
- **Classic Outlook:** ribbon + folder pane (calendar folders, public-holiday/shared calendars) + calendar view + status bar *(verified)*; calendar settings dialog, scheduling assistant, reminder window *(verified via the access-key shortcuts)*.
- **Settings window (new Outlook):** tab *Calendar* with sub-tabs; evidenced items: work hours/days, out-of-office replies, default reminder time *(verified)*.

## Configuration

- **Users:** calendar colours/lists, default reminder, work hours/days, view (UI; via Graph `calendar` PATCH respectively mailbox settings).
- **Admin (Exchange Online):** mailbox and folder permissions via PowerShell/EAC, sharing/availability policies between tenants (Cross-Tenant Access Policy, migration article on learn.microsoft.com), resource mailboxes. *(Existence verified via the learn article; individual parameters not read off.)*
- **App registration (developers):** OAuth scopes, webhook endpoint (HTTPS, 3 s response), subscription renewal — details in [api.md](api.md).

## Deployment

- **SaaS:** Microsoft 365 / Exchange Online; Outlook on the web with no installation; the new Outlook for Windows as a preinstalled/pushable client. **On-prem:** Exchange Server (the older protocols including EWS remain active there — their own support lifecycles *(side note, not verified in detail)*).
- **Client migration (timelines):** the new Outlook progressively replaces the Mail/Calendar apps of Windows; free Outlook.com accounts **can no longer switch back to classic Outlook since January 2025** *(secondary: techcommunity post)*; calendar sharing is being moved from MAPI to a **REST model** tenant by tenant in 2026 *(secondary: office365itpros.com 2026-05, admin365.blog 2026-07; a completion deadline of March 2027 is named)*.
- **Protocol hardening 2026:** the EWS shutdown in Exchange Online (starting Oct 2026, complete Apr 2027) *(verified)*; EAS clients < 16.1 blocked *(secondary)*.

## Operations notes

- Webhook endpoints need an operating SLA (3 s response, 4 h retries, slow/drop behaviour) or Event Hubs/Event Grid *(verified)*.
- Integrations must pay attention to **immutable IDs** and `changeKey` conflict handling *(verified)*.
- Migrate leftover EWS usage early; Microsoft offers EWS usage reports and an EWS code analyser *(verified)*.
