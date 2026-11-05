# Google Calendar – verified features (as of 2026-11-02)

Basis: official help pages (support.google.com/calendar), the official product piece workspace.google.com/products/calendar, the Calendar REST API v3 discovery document (revision 20261028) and the official Google Workspace updates blog.

## Calendars & views

- Several calendars per account: your own default calendar plus any number of secondary calendars (product page, "Get started" help)
- Views: **Day, Week, 4 days, Month, Year, Schedule** (help "View your day, week, or month")
- Colour marking of calendars and events; light/dark/system design (product page)
- Web interface, apps for **Android, iOS, Wear OS, Apple Watch** — automatic synchronisation (product page); **no desktop app**, instead a browser (Chrome, Firefox, Safari, Edge) (help "Get started"); offline use is documented (help page "Use Google Calendar offline", detailed scope not checked)
- Free-text search (API: `q` over title, description, location, attendees among others)

## Events

- Create/edit including **all-day events, multilingual describable events, recurring events** (recurrence patterns, API field `recurrence`), reminders (pop-up/e-mail, API `EventReminder`)
- Guest handling: invitations with response status, organiser/role split; guest restrictions via `guestsCanInviteOthers`, `guestsCanModify`, `guestsCanSeeOtherGuests` (API fields `visibility`, `privateCopy`)
- **File attachments on events** (Drive links/URLs; API `supportsAttachments`, `EventAttachment`; product page)
- **Meet conferences** automatically/by click (`conferenceData`, `hangoutLink`)
- **Focus time**: an event that mutes chat notifications and auto-declines meetings (help 11190973; API `focusTimeProperties`)
- **Out of Office** and **work location/hours** as event properties for teams (API `outOfOfficeProperties`, `workingLocationProperties`; product page)
- Birthday events as their own event type (API `birthdayProperties`)
- "Quick add" via free text (API `events.quickAdd` with a `text` parameter)
- Moving an event between calendars (API `events.move`)

## Collaboration & sharing

- Sharing calendars with permission levels: **see only availability / see all details / edit events / share and manage** (help "Subscribe to someone else's calendar")
- Subscribing to other people's calendars by e-mail search or **URL (ICS subscription of public calendars)**; over **400 subscribed calendars** → performance problems (help 37100)
- "**Find a time**": suggestions of free times/rooms for groups, web + Android + iOS (Workspace updates blog 2016)
- Organisational calendars and **rooms/resources** in Google Workspace (product page FAQ; administration is a Workspace admin feature)
- Reminders/notifications per calendar and per event (e-mail, app push; API channels for third parties)

## Booking & organisation

- **Booking pages / appointment schedules**: your own booking page with availability windows, without extra apps; **free for private Google accounts** (product page FAQ; help 10729749/11608416)
- Premium (certain Google One/Workspace subscriptions): **several booking pages, Stripe payments, e-mail reminders, availability checking across several calendars** (product page; Workspace admin switch "Appointment schedules with payments")
- **Tasks integration**: tasks with date/time appear in the calendar (separate Google Tasks service) (product page)
- Automatic events from **Gmail** (flights, hotels, restaurants) (product page)
- "**Your time at a glance**" (Time Insights): analysis of meeting behaviour, Workspace accounts, can be switched off administratively (help 10738043)
- **Gemini AI** (premium subscriptions): "Plan for me" in Gmail, "Add to calendar" from e-mails (product page)
- **Migration tools** including from Microsoft Exchange/Outlook and IBM Notes (product page FAQ)

## Import, export, interfaces

- **ICS export** of calendars (web only, requires "make changes and manage sharing" rights) (help 37111); **ICS import** into Google Calendar (basic function of the import/export help; on the API side `events.import`)
- **Calendar REST API v3** (all calendar/event operations, sync token, batching, push channels) and **Tasks API**; Apps Script service `CalendarApp`; Workspace add-ons (see [api.md](api.md))

## What Google Calendar does NOT offer

- **No self-hosting**: neither server software nor a local variant; data resides exclusively in Google data centres
- **No desktop program** (browser + mobile apps only) — stated expressly in the official help
- **No official CalDAV/CardDAV** and no more Exchange ActiveSync: Google Sync was discontinued in 2024, CalDAV/CardDAV with password ("less secure apps") deactivated from 2024/2025; the official documentation names only the REST API. Third-party endpoints work unofficially over OAuth ("not officially supported by either Google or DAVx⁵")
- **No open standard protocol** for sync (own sync-token/webhook channels instead of RFC 4791 REPORT/sync as with DAViCal)
- **The "Goals" feature was discontinued** (phased out from November 2022) — still found in older literature
- Tasks are a **separate, lean service**, not an equivalent event type with attendees/series in the calendar record
- Booking pages are **not manageable via API** — in the current discovery v3 (rev. 20261028) there is neither a dedicated resource nor an `appointment` `eventType`; a pure UI feature
- Workspace administration features (rooms/resources, policies, Time Insights for the org) are **not available for private accounts**
- Quotas & thresholds (10,000/min/project, 600/min/user, 1M/day with pricing planned from "later 2026") — no unlimited automation
- No end-to-end encrypted calendar; "secret address" sharing does not replace real encryption

## Not verified

- The settings feature "Second time zone" in the web interface was documented for a long time, the old help article has moved; evidence from a current primary source was not available at editing time → not listed as verified
- Detailed scope of offline use (which operations are possible offline)
- Whether the Workspace Events API can now subscribe to calendar resources
