# Calendar — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Calendar` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Cal.com](cal-com/index.md) | [latest](cal-com/latest/description.md) | Cal.com is a scheduling product: the owner defines event types and availability, and others book a slot on a public page. |
| [DAViCal](davical/index.md) | [latest](davical/latest/description.md) | DAViCal is a CalDAV/CardDAV server written in PHP on PostgreSQL — a lean, protocol-faithful self-hosted calendar/contact store with web administration. |
| [Fantastical](fantastical/index.md) | [latest](fantastical/latest/description.md) | Fantastical is a commercial calendar and task app from Flexibits for Apple platforms and Windows. |
| [Google Calendar](google-calendar/index.md) | [latest](google-calendar/latest/description.md) | Google Calendar (calendar.google.com) is Google's calendar service: a web interface plus apps for Android, iOS, Wear OS and Apple Watch, coupled with Gmail, Meet, Tasks and (with a premium subscrip… |
| [Merkuro Calendar](merkuro/index.md) | [latest](merkuro/latest/description.md) | Merkuro Calendar is the **modern calendar client of the KDE desktop environment** (Qt 6/QML/Kirigami, convergent on desktop and Plasma Mobile). |
| [Motion](motion/index.md) | [latest](motion/latest/description.md) | Motion (usemotion.com) is a commercial planner with calendar, tasks and projects. |
| [Nextcloud Calendar](nextcloud-calendar/index.md) | [latest](nextcloud-calendar/latest/description.md) | The calendar app of the Nextcloud server: a web interface (Vue 3 + FullCalendar) above the CalDAV backend (sabre/dav) of the Nextcloud server. |
| [Notion Calendar](notion-calendar/index.md) | [latest](notion-calendar/latest/description.md) | Notion Calendar (formerly Cron) is a calendar client by Notion for desktop and web. |
| [Outlook calendar](outlook-calendar/index.md) | [latest](outlook-calendar/latest/description.md) | The calendar component of the Microsoft Outlook line: web app (outlook.com / Outlook on the web), the new and the classic Outlook for Windows, Outlook for Mac and iOS/Android — data in the mailbox … |
| [GNOME Planner](planner/index.md) | [latest](planner/latest/description.md) | Planner is the project planner on GNOME (app ID `app.drey.Planner`): tasks with start/finish, work, costs and dependencies (FS/SS/FF/SF with lag), resources with their own working calendars, critic… |
| [Reclaim](reclaim/index.md) | [latest](reclaim/latest/description.md) | Reclaim (Reclaim.ai) is a web service that works on top of a Google or Outlook calendar and places tasks, habits and meetings into free time. |

## File set per program (ADR 0012)

```
programs/apps/calendar/frontends/<program>/
├── index.md        what it is, notable ideas, documented versions, sources
├── changelog.md    changes between documented versions (≥ 2 versions)
└── <version>/
    ├── description.md    required · Detailed description, differentiation, who it suits
    ├── features.md       required · What the program can do — and what not
    ├── layout.md         required · Window structure, regions, panels
    ├── menus.md          required · Menu structure, context menus, menus by role
    ├── shortcuts.md      required · Keyboard shortcuts
    ├── api.md            required · APIs and protocols, authentication, rate limits
    ├── themes/index.md   required · Themes: colours, typography, spacing — what can be rebuilt
    ├── interaction.md    if needed · Hover, focus, drag, gestures (finger, mouse, pen)
    ├── states.md         if needed · UI states and transitions
    ├── events.md         if needed · Events to the outside (webhooks, push, streams)
    ├── limits.md         if needed · Known limitations
    ├── i18n.md           if needed · Localisation, writing direction
    └── dependencies.md   if needed · Which of our components a frontend in this style needs
```

Protocols (Matrix, IMAP, CalDAV, …) are not frontends; they are described under [data](../../../../data/standards.md).
