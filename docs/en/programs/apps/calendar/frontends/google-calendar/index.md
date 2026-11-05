# Google Calendar

> Category: [calendar](../../index.md)

## What it is

Google Calendar (calendar.google.com) is Google's calendar service: a web interface plus apps for Android, iOS, Wear OS and Apple Watch, coupled with Gmail, Meet, Tasks and (with a premium subscription) Gemini. Events, series, shares, booking pages, focus time, work location and organisational calendars all come from a closed SaaS platform; accessed programmatically through the **Calendar REST API v3** (discovery revision 2026-10-28) with OAuth scopes, sync tokens and push channels. For FreeSynergy it is the cloud frontend: connection is only possible via Google's own API, there is **no documented CalDAV**, and no self-hosting.

## Notable ideas

_To do: what does this program do that others don't? Why is it documented here (ADR 0013)?_

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Required files present |
|---------|------------------------|
| [latest](latest/description.md) | 6/7 |

### latest

| File | Contents |
|------|----------|
| [description.md](latest/description.md) | Detailed description, differentiation, who it suits |
| [features.md](latest/features.md) | What the program can do — and what not |
| [layout.md](latest/layout.md) | Window structure, regions, panels |
| [menus.md](latest/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](latest/shortcuts.md) | Keyboard shortcuts |
| [api.md](latest/api.md) | APIs and protocols, authentication, rate limits |

⚠️ Missing required files: `themes/index.md`
<!-- /gen:versions -->

## Short profile

| Attribute | Value |
|-----------|-------|
| Type | Cloud service (SaaS), web + Android/iOS/Wear OS/Apple Watch |
| Version | Calendar REST API **v3** (discovery revision 2026-10-28); UI = continuously running web service |
| API | REST v3 (`calendar.googleapis.com`/`googleapis.com/calendar/v3`), Tasks API, Apps Script, add-ons |
| Auth | OAuth 2.0 (finely granular scopes), service accounts (domain-wide delegation), API key for public data |
| Sync/push | Sync token/deltas, watch channels (HTTPS webhooks), batching; **no CalDAV** |
| Data storage | Google Cloud only; ICS import/export, Takeout |
| Cost | free with a Google account; Workspace/Google One subscriptions for administration + premium (payments, Gemini) |
| Self-hosting | ❌ not possible |

## Sources

All statements in this section come from official primary sources (retrieved 2026-11-02 unless stated otherwise):

| Source | Location / URL | Used for |
|--------|----------------|----------|
| **Discovery document Calendar v3** (revision **20261028**) | `https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest` | api.md: all resources/methods/paths, parameters, schemas, scopes, `batchPath` |
| Scopes page of the API docs | `https://developers.google.com/workspace/calendar/api/auth` (last updated 2026-09-03) | api.md: complete scope table incl. add-on scopes |
| API overview | `https://developers.google.com/workspace/calendar/api/guides/overview` (2026-09-11) | api.md: resource terminology |
| Push notification guide | `https://developers.google.com/workspace/calendar/api/guides/push` | api.md: watch/stop, headers, delivery codes, renewal |
| Usage limits | `https://developers.google.com/workspace/calendar/api/guides/quota` | api.md/features.md: quotas 10,000/min, 600/min/user, 1M/day, pricing planned for 2026 |
| Reference `events.update` | `https://developers.google.com/workspace/calendar/api/v3/reference/events/update` | api.md: ETag note, `sendUpdates`, version parameters |
| Downloads (client libraries) | `https://developers.google.com/workspace/calendar/api/downloads` (2026-09-03) | api.md: SDK list |
| Workspace Events API v1 (reference) | `https://developers.google.com/workspace/events/reference/rest/v1` (2026-05-14) | api.md: Pub/Sub alternative (calendar support marked as unclear) |
| Google Calendar product page (DE) | `https://workspace.google.com/products/calendar/` | description.md/features.md: platforms, Tasks/Gmail/Meet, booking pages + Stripe premium, Time Insights, focus time, work location, migration |
| Workspace updates blog (official) | `https://workspaceupdates.googleblog.com/2023/09/winding-down-google-sync-and-less-secure-apps-support.html` | api.md/features.md: end of CalDAV/CardDAV/Google Sync (2024-09-30, updates until 2025) |
| Workspace admin knowledge base | `https://knowledge.workspace.google.com/admin/sync/transition-from-less-secure-apps-to-oauth` | api.md: OAuth mandatory from March/May 2025, CalDAV only with OAuth anymore |
| Calendar help: subscribe to another calendar | `https://support.google.com/calendar/answer/37100?hl=en` (DE version retrieved additionally) | features.md/menu.md: subscription by e-mail/URL, permission levels, 400-calendar limit, German menu labels („Weitere Kalender hinzufügen", „Kalender abonnieren", „Per URL") |
| Calendar help: views (DE) | `https://support.google.com/calendar/answer/6110849?hl=de` | menu.md: „Tag, Woche, 4 Tage, Monat, Jahr, Terminübersicht", „Heute", mini calendar, gear → „Ansichtsoptionen", „Meine Kalender"/„Weitere Kalender" |
| Calendar help: create an appointment schedule (DE) | `https://support.google.com/calendar/answer/10729749?hl=de` | menu.md: „Eintragen" → „Terminplan", area labels of the editor, 4-hour default lead time |
| Calendar help: export (DE) | `https://support.google.com/calendar/answer/37111?hl=de` | menu.md/structure.md: three-dot menu → „Einstellungen und Freigabe", „Importieren & Exportieren", „Öffentliche/Privatadresse im iCal-Format" |
| Calendar help: time insights (DE) | `https://support.google.com/calendar/answer/10738043?hl=de` | menu.md: „Weitere Details" (left), pinning contacts |
| Calendar help: keyboard shortcuts | `https://support.google.com/calendar/answer/37034?hl=de&co=GENIE.Platform%3DDesktop` | shortcuts.md: complete official shortcut list, activation, sidebar keys |
| Calendar help: get started | `https://support.google.com/calendar/answer/37057?hl=en` | features.md: no desktop app, offline use, browser list |
| Calendar help: views | `https://support.google.com/calendar/answer/6110849?hl=en` | features.md/menu.md: day/week/4 days/month/year/schedule |
| Calendar help: time insights | `https://support.google.com/calendar/answer/10738043` | features.md: Time Insights (Workspace, admin switch) |
| Calendar help: focus time | `https://support.google.com/calendar/answer/11190973` | features.md: focus-time behaviour |
| Calendar help: booking pages | `https://support.google.com/calendar/answer/10729749` and `.../answer/11608416` | features.md: appointment schedules, premium limits |
| Calendar help: payments for appointment schedules (admin) | `https://knowledge.workspace.google.com/admin/calendar/allow-paid-appointment-schedules-in-calendar` | features.md: Stripe feature (Workspace) |
| Calendar help: export | `https://support.google.com/calendar/answer/37111` | features.md: ICS export conditions |
| Workspace updates blog: "Find a time" | post "Save time with smart scheduling in Google Calendar" (2016-09-29) via blog search | features.md: find-a-time feature |
| Goals introduction (official) | Workspace updates blog, post "Goals in Google Calendar" via blog search | features.md: Goals existed (introduced 2019) |
| DAVx⁵ "Tested with: Google" | `https://www.davx5.com/tested-with/google/` (page state June 2023) | api.md: unofficial CalDAV/CardDAV access only with OAuth, "not officially supported" – **community source, clearly marked** |

**Research notes:**
- The older version of this file contained fabrications: a scope `calendar.push` (does not exist), `users/{user}/calendarList` (in reality only `users/me/…`), an "appointment schedule API" endpoint, and a blanket "CalDAV is supported" claim. All of these were corrected against discovery v3 (rev. 20261028) and the LSA deprecations.
- Goals shutdown: the official help article has been removed; the removal (Nov. 2022) is only evidenced by several independent reports — accordingly marked as a report, not as a primary citation.
- "Second time zone" and the offline scope remain marked as **not verified**.
- The old shortcuts help article (answer/71185) no longer exists; the official shortcuts page today is **answer/37034** (computer). Both statements checked against the live article.
- Discovery comparison old/new: `summaryVisibility` and `subscriptionType` have disappeared from `CalendarListEntry`, new are `autoAcceptInvitations`/`dataOwner`/`writerWithoutPrivateAccess` and the writable scope `calendar.settings` — documented as such in structure.md/api.md.
