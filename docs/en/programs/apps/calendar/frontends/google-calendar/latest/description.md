# Google Calendar – Description

## What the program does

Google Calendar (calendar.google.com) is Google's calendar service: a web interface plus apps for Android, iOS, Wear OS and Apple Watch, in which events, recurring series, tasks and multi-person appointments are managed across several calendars. On top of that come shared calendars with permission levels, share/subscribe features, public calendars, booking pages (appointment schedules) and organisational calendars including room/resource calendars in Google Workspace. The service runs exclusively in the Google Cloud; self-hosting is not possible.

It can be programmed through the **Calendar REST API v3** (JSON/HTTPS), tasks additionally through the separate **Tasks API**; changes can be received via push channels (webhooks). Events, tasks and work location are linked with Gmail (automatic travel/booking events), Meet (conference links), Tasks (dated events appear in the calendar) and — with a matching subscription — Gemini (event suggestions "Plan for me", "Add to calendar" from e-mails).

## Benefits

- **No operating effort**: nothing to install, update or back up; accounts, device sync and availability are Google's job
- **Free base tier**: full calendar features with a private Google account; Workspace subscriptions add administration, resources and premium booking features
- **Across all platforms**: web, Android, iOS, Wear OS, Apple Watch — synchronised automatically
- **Appointment finding & collaboration**: sharing with four permission levels ("see only availability", "see all details", "edit events", "share and manage"), a "Find a time" view, invitations with response status, group calendars
- **Booking pages without extra apps**: customers/clients book directly; premium (certain Google One/Workspace subscriptions) with several pages, Stripe payments, e-mail reminders
- **Time tools**: focus time (mute notifications, auto-decline meetings), "Your time at a glance" analytics, work location/hours for teams, files on events
- **Large integration ecosystem**: Calendar API v3 with official client libraries, push channels and add-ons; migration tools including from Microsoft Exchange/Outlook and IBM Notes

## How it differs from comparable products

| System | Difference |
|--------|------------|
| **DAViCal** (documented in this series) | DAViCal is the lean self-hosted CalDAV/CardDAV backend server (PHP/PostgreSQL, RFC 4791) — data sovereignty, real ACLs, scheduling by standard, but you operate it yourself. Google Calendar is the opposite model: a finished SaaS full client + proprietary REST API, **no documented CalDAV offering** (password CalDAV was shut down in 2024/2025) |
| **Nextcloud Calendar** (documented in this series) | Self-hosted groupware frontend on a CalDAV basis with full data control; Google Calendar delivers comparable convenience but without your own infrastructure |
| **Outlook calendar** (documented in this series) | Microsoft's counterpart in Microsoft 365 with Exchange/Graph API and Teams integration; Google's counterpart to Google's stack (Gmail/Meet/Tasks) |
| **Merkuro** (documented in this series) / Planner (planned) | Native desktop clients (KDE) that work with servers such as DAViCal; Google Calendar is itself *both* server and client, but with no offline desktop client |

The core of the distinction: Google Calendar is **SaaS from a single source** — very high convenience, but the data sits with Google, access runs over Google accounts/OAuth, and standard protocols (CalDAV) are not officially provided. Anyone who wants to operate calendar data sovereignly is better off with DAViCal or Nextcloud.

## Technical details

- **Architecture**: closed Google service; clients (web/Android/iOS) and third parties talk to the Calendar REST API v3 (`https://www.googleapis.com/calendar/v3`, discovery revision 2026-10-28), tasks to the Tasks API
- **Auth**: OAuth 2.0 with finely graded scopes (`calendar`, `calendar.events`, `calendar.acls`, …), service accounts with domain-wide delegation for Workspace, API key only for public calendars
- **Synchronisation**: sync token (deltas), push notification channels (HTTPS webhooks, without content — you fetch afterwards yourself), batch endpoint
- **Data exchange**: ICS import/export, calendar URLs (public/secret), Takeout; embedding of calendars
- **Limits**: quota model since 1 May 2026 (10,000 requests/min/project, 600/min/user, daily limit 1M with pricing planned "later in 2026"); more than 400 subscribed calendars per account slow things down according to the help
- **AI**: Gemini features only with Google One/Workspace premium subscriptions

## Who it suits

- **Private users** who already use Google Mail/accounts and want an immediately synchronised calendar without administration
- **Organisations/teams on Google Workspace**: calendar sharing, room/resource calendars, admin policies, migration from Exchange/Notes
- **FreeSynergy scenario**: useful as a "skin" when external users' events are to be integrated via the Calendar API (push + sync token) or mirrored out to Google
- **Unsuitable** where data sovereignty/self-hosting is required, where CalDAV client access is needed (only unofficially), or where dependence on a single vendor must be avoided — use DAViCal (server) or a CalDAV client there
