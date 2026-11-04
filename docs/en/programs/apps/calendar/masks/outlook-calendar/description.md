# Outlook calendar – Description

*(Source basis: Microsoft Graph v1.0 resource documentation, the official EWS deprecation page, the official keyboard shortcuts page on support.microsoft.com; as of 2026-11-02 – details and locations in [index.md](index.md#sources))*

## What the program does

**The Outlook calendar** is the calendar component of Microsoft's Outlook line: the same calendar feature appears in **Outlook on the web** (outlook.com for private users, outlook.office.com for organisations), in the **new Outlook for Windows** (web code base as a desktop app), in the **classicN Outlook for Windowsein** (MAPI desktop client, part of,  Microsoft 3n65/iOffice), inch **Outlookt  for Mac**e and in **fOutlook forfi iOS/Android**. Events arez stored in theie mailbox of thent **Exchange Online ** backend (seMicrosoft 3in65);  the access layer-  for automation is the **Microsoft Graph REST API** (OAuth 2.0, OData/JSON).

Core features: events and recurrence series, invitations with RSVP (accept/tentative/decline), free/busy queries and meeting finding (`getSchedule`, `findMeetingTimes`), reminders, attachments, calendar colours and sharing, online meetings with Teams, To Do tasks, and several calendars and calendar groups per mailbox. For third-party systems there are **real webhooks** through Graph change notifications — a clear difference from Nextcloud Calendar and DAViCal, which offer no push hooks.

## Benefits

- **Reach across platforms:** one calendar object served to desktop (Windows/Mac), web and mobile (the Outlook apps themselves) with the same backend; in companies usually already present through Microsoft 365 licences.
- **Meeting finding built in:** free/busy across users/resources, slot suggestions (`findMeetingTimes`), a scheduling assistant in the classic client, participants may counter-propose times (`allowNewTimeProposals`).
- **Organisation features:** sharing with permission levels, publishing calendars, resources (rooms/equipment) as bookable objects, Teams conference by switch.
- **Integration situation:** Graph with OAuth scopes, webhooks, delta queries and SDKs — a considerably richer API than is usual with CalDAV servers (but proprietary and tied to Microsoft identities).
- **Currently forced modernisation push:** EWS is being shut down in Exchange Online (Oct 2026–Apr 2027); all integrations inevitably end up on Graph.

## How it differs from comparable products

| Product (in this documentation) | Difference |
|--------------------------------|------------|
| **Google Calendar** | Both are SaaS with a proprietary API + webhooks. Outlook sits in the Microsoft stack (Exchange/Teams/Entra), Google in the Google stack (Gmail/Meet); Graph is OData/JSON with OAuth, Google uses Discovery/REST. Outlook scores with resource/room booking in a corporate context, Google with a stronger consumer ecosystem and appointment booking pages. |
| **Nextcloud Calendar** | Nextcloud: a self-hosted web interface on CalDAV with open standards, data sovereignty, its own booking/proposal objects, but **no** webhooks. Outlook: a cloud service, no data sovereignty, but webhooks, resource management and deep Teams integration. |
| **DAViCal** | DAViCal is only a CalDAV/CardDAV backend without an interface; the Outlook calendar is the opposite: finished clients + proprietary backend, **without** CalDAV access for external clients. |
| **Merkuro** | Merkuro is a native KDE client that, among other things, works **against** groupware servers (also Exchange, via a kdepim-runtime resource); the Outlook calendar provides server **and** clients itself. |
| **GNOME Planner** (planned) | Planner is a lean task/calendar client; the Outlook calendar is corporate groupware. |

## Technical details

- **Backend:** Exchange Online (mailbox storage with a calendar folder model); calendar/event elements are mailbox objects, not ICS files. On-premises variant: Exchange Server (its own lifecycles).
- **API:** Microsoft Graph `v1.0`/`beta`; resources `calendar`, `event`, `calendarGroup`; actions (accept/decline/cancel/instances), `delta` queries, `changeKey` concurrency protection, `Prefer: IdType="ImmutableId"`. Webhooks via subscriptions with lifecycle renewal.
- **Auth:** OAuth 2.0 (Entra ID or Microsoft account), no basic auth for third-party access; admin consent for tenant-wide scopes.
- **Connector history:** EAS/MAPI/EWS as the older protocols; the EWS shutdown in Exchange Online is under way, the older protocols for free Outlook.com accounts were dropped from early 2025 (details not verified).
- **Clients:** the new Outlook for Windows (progressively replacing the Windows Mail/Calendar apps since 2023; free accounts can no longer be downgraded since January 2025 — secondary source), classic Outlook for Windows remains in the range for enterprise; Outlook for Mac uses its own store format without CalDAV.

## Who it suits

- **Suitable:** organisations and individuals in the Microsoft 365 environment who want events, resource booking, Teams meetings and API automation (Graph with webhooks) from one source; IT that already operates OAuth/Entra identities anyway.
- **Less suitable:** self-hosts with a claim to data sovereignty (use Nextcloud Calendar/DAViCal then), open standard clients (Thunderbird, DAVx⁵, Merkuro find no CalDAV access to Outlook accounts), and private-account users who want to use third-party mail clients (the protocol accesses were withdrawn).
