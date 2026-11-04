# Outlook calendar – Documentation

The calendar component of the Microsoft Outlook line: web app (outlook.com / Outlook on the web), the new and the classic Outlook for Windows, Outlook for Mac and iOS/Android — data in the mailbox of **Exchange Online**, automation through **Microsoft Graph v1.0** (REST/OAuth/OData). Its striking API feature compared with the other entries in this series: **real webhooks** (Graph change notifications) — and a protocol boundary drawn firmly: **no CalDAV**, with the EWS shutdown in Exchange Online under way (Oct 2026–Apr 2027).

- **Category:** calendar (SaaS groupware interface + proprietary API)
- **Licence:** proprietary (Microsoft service; clients partly with a Microsoft 365 subscription, web apps free for private accounts)
- **Currently documented version:** Microsoft Graph **v1.0** (stable) + beta; client state "new Outlook for Windows" / Outlook on the web, verification date **2026-11-02**
- **Development status:** very active (ring releases; EWS→Graph migration forced; calendar-sharing migration MAPI→REST in 2026)

## File structure of this section

| File | Contents |
|------|----------|
| [description.md](description.md) | What the program does, benefits, differentiation (incl. from Google Calendar, Nextcloud Calendar, Davical, Merkuro), technical details, who it suits |
| [features.md](features.md) | Verified feature list + "What the Outlook calendar does NOT offer" |
| [api.md](api.md) | Graph v1.0: calendar/event endpoints, auth/scopes, webhooks, limits, SDKs, EWS shutdown |
| [menu.md](menu.md) | navigation structure (new Outlook, classic Outlook, admin level) from official layout articles |
| [shortcuts.md](shortcuts.md) | official keyboard shortcuts (new/classic Outlook, web) + direct workflows |
| [structure.md](structure.md) | build layers, data model (changeKey/iCalUId/series), configuration, deployment |

## Sources

All statements come from the official content of the documentation pages; verification date 2026-11-02. **Outlook is closed source — so the primary sources are Microsoft's official API/help pages (not source files as for the open-source skins in this series).**

1. **EWS deprecation (official):** `https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/deprecation-of-ews-exchange-online` – timeline (2018/2023/Oct 2026/Apr 2027), Midnight Blizzard, parity gaps, tools.
2. **Graph calendar resource:** `https://learn.microsoft.com/en-us/graph/api/resources/calendar?view=graph-rest-1.0` (page last updated **2026-10-15**, read in full) – methods incl. calendarView/delta/getSchedule/findMeetingTimes, properties incl. the `calendarPermissions` association, group limits.
3. **Graph event resource:** `https://learn.microsoft.com/en-us/graph/api/resources/event?view=graph-rest-1.0` (page last updated 2025-05-15, read in full) – actions, properties (iCalUId, seriesMasterId, cancelledOccurrences, changeKey, allowNewTimeProposals, webLink, recurrence/`type`, transactionId, sensitivity, onlineMeetingProvider), 500-attendee limit, ImmutableId, documented deep-link formats `…/calendar/item/{id}`.
4. **Graph webhooks:** `https://learn.microsoft.com/en-us/graph/change-notifications-delivery-webhooks?view=graph-rest-1.0` – delivery contract (3 s, 4 h retry), slow/drop, lifecycle, Event Hubs/Event Grid.
5. **Graph throttling:** `https://learn.microsoft.com/en-us/graph/throttling` – 429/Retry-After, Graph Data Connect.
6. **Graph Outlook API concept:** `https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/office-365-rest-apis-for-mail-calendars-and-contacts` (state 2021-10-11) – OAuth2/OData/JSON.
7. **Keyboard shortcuts (official):** `https://support.microsoft.com/en-us/accessibility/outlook/keyboard-shortcuts-for-outlook` – tabs New Outlook / Classic Outlook / Web; calendar, navigation and VBA shortcuts.
8. **Layout (official):** `https://support.microsoft.com/en-us/accessibility/outlook/use-a-screen-reader-to-explore-and-navigate-outlook-calendar` – regions of the new Outlook (nav bar, ribbon, navigation window, toolbar) and of the classic Outlook (folder pane, ribbon, status bar), settings sub-levels.
9. **CalDAV boundary (official):** `https://support.microsoft.com/en-us/outlook/sync-your-icloud-calendar-with-outlook-for-mac` – "Outlook for Mac doesn't support the CalDAV or CardDAV Internet standards".
10. **Secondary sources (marked as such):** techcommunity post "Outlook for Windows: Timelines…" (free accounts from Jan 2025 no way back to classic Outlook); office365itpros.com 2026-05 + admin365.blog 2026-07 (calendar sharing MAPI→REST, deadline March 2027); petri.com/windowsforum (EAS ≥ 16.1 from 2026).
11. **Graph permissions (added, verified 2026-11-02):** `https://learn.microsoft.com/en-us/graph/permissions-reference` (Calendars section fetched by offset) – scopes `Calendars.Read/ReadBasic/ReadWrite` (app + delegated), `.Shared` (delegated, incl. delegates/shares), `.Read.All`/`.ReadWrite.All` (app only, exclusively working hours and locations); delegated Calendars scopes explicitly consentable with **personal Microsoft accounts**; application access policy for restricting mailboxes.
12. **Not verified (deliberately left open):** the Graph "service-specific limits" figures (page returned 404 on the research day); the protocol shutdown details for free Outlook.com accounts (support page unreachable); Mac shortcuts; consumer availability of individual convenience endpoints (e.g. findMeetingTimes).

Reproduction recipe: fetch pages 1–5 + 7–9 directly (learn/support.microsoft.com are reachable without login; older /office/ slugs on support.microsoft.com partly 404/403 — in that case use the /accessibility/ paths); the permissions reference is ~495k characters long — the Calendars section sits at character offset ~56000–61000; compare changes to the EWS timeline and the Graph resource pages against this documentation; check the secondary sources for newer states.
