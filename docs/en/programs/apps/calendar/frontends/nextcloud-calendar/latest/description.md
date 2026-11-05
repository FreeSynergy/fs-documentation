# Nextcloud Calendar – Description

*(Source basis: nextcloud/calendar v6.6.4, 2026-10-26 – details and locations in [index.md](../index.md#sources))*

## What the program does

Nextcloud Calendar is the **calendar web app of the Nextcloud server**: a web interface for creating, editing, sharing and viewing events and series whose data lives entirely in a **CalDAV backend (sabre/dav) of the Nextcloud server**. The app itself is only the client — calendars, objects and shares are ordinary CalDAV resources that desktop and mobile clients (Thunderbird, DAVx⁵, Apple Calendar …) access in parallel.

Features of the web interface (v6.6.4): day/week/month/list/year views (FullCalendar), quick creation, full-screen editor with attendees, reminders, attachments, recurrences, time zones, search, weekday view with resource timeline, birthday calendar (from Contacts), WebCal subscriptions, tasks/Deck cards with due dates, public calendar and embed views, **appointment booking by link** (appointment config with slot calculation) and **meeting proposals** (Doodle-style polls with a voting link, since the 6.x series).

## Benefits

- **Self-hosted, open standards:** everything RFC 5545/4791 compliant over `remote.php/dav`; no proprietary data format, any CalDAV client works.
- **Deep integration into the Nextcloud suite:** Contacts (attendee autocomplete, birthday calendar), Talk (conference room with one click, availability in the Contacts menu), Tasks/Deck (due dates in the calendar), Circles/groups (group calendars), dashboard widget, link preview (ReferenceProvider), profile link to appointment bookings.
- **Browser booking page without a counterpart account:** outside people book slots through a link; an optional confirmation e-mail step.
- **No lock-in:** the data stays on your own server; the app is AGPL source code and can be replaced as long as the CalDAV server remains.
- **Active development:** regular releases (6.6.4 Oct 2026), maintained dependencies, support via help.nextcloud.com.

## How it differs from comparable products

| Product | Type | Difference from Nextcloud Calendar |
|---------|------|-----------------------------------|
| **Davical** (described in this documentation) | pure CalDAV/CardDAV server (PostgreSQL) | Davical is only the backend with no web interface of its own; Nextcloud Calendar is conversely only the frontend with no backend of its own. Combinations of an arbitrary CalDAV server app + calendar UI are not provided in Nextcloud — the app presupposes the Nextcloud server with its `dav` app backend. |
| **Google Calendar** (described in this documentation) | SaaS with a proprietary REST API | Google: a cloud service with push webhooks, ML features, a huge ecosystem, but the provider holds the data. Nextcloud Calendar: full data sovereignty, no push webhooks, but CalDAV as a neutral standard and integration into self-hosted groupware. |
| **Nextcloud "appointments" app** | external booking app | The calendar app already ships its own booking pages; the older separate appointments app is an alternative for special cases. |
| Desktop/mobile calendars (KOrganizer, Thunderbird, Apple Calendar) | native single-seat clients | Often access the same Nextcloud database; the web app scores with sharing, public pages, booking and meeting polls without an installable client. |

## Technical details

- **Frontend:** Vue 3 + Pinia + vue-router, FullCalendar 6.1.21 (DayGrid/TimeGrid/List/MultiMonth + resource timeline), the project's own libraries `@nextcloud/cdav-library` (CalDAV client), `ical.js`/`@nextcloud/calendar-js` (ICS modelling), built with rspack; the PHP part follows the Nextcloud AppFramework (Controller/Service/Db).
- **Backend access:** exclusively CalDAV under `{base}/remote.php/dav/` (see [api.md](api.md)); own database tables only for booking configurations, bookings and meeting proposals (`calendar_proposal_*`).
- **Server hooks:** dashboard widget, reference provider, profile action, notifier (Notifications app), background job `CleanUpOutdatedBookingsJob`, Notify-Push listener for live sync of the tabs, user migrator.
- **Runtime:** app v6.6.4 requires Nextcloud 32–35 and PHP 8.1–8.5 (from `appinfo/info.xml`).
- **Calendar kinds in the UI:** personal, group/Circles calendars (through server-side "Calendar" collaboration), birthday calendars, WebCal subscriptions, public shares (read/write, link with token).

## Who it suits

- **Suitable:** organisations and individuals hosting groupware themselves (a Nextcloud instance exists or is planned), who value data sovereignty and standard clients, and who need appointment booking for customers/appointments and internal polls without extra services.
- **Less suitable:** users without their own server (use Google/Outlook then), pure CalDAV setups without Nextcloud (use Davical + any client then), and anyone expecting push webhooks/workflow automation from the calendar API — this constellation does not deliver that.
