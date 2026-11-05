# Merkuro – Description

*(Source basis: Merkuro 26.08.2, Release Service Oct 2026 – locations in [index.md](../index.md#sources))*

## Name history

**Kalendar** (started 2021, in KDE Gear since 22.12) was **renamed to Merkuro with the release of KDE Gear 23.08 (August 2023)** because the application had grown beyond calendar/tasks into a groupware suite. Today four programs exist: `merkuro-calendar`, `merkuro-contact`, `merkuro-mail` and `merkurolauncher`. This section documents the successor of Kalendar: **Merkuro Calendar** (`org.kde.merkuro.calendar`).

## What the program does

Merkuro Calendar is the **modern calendar app of the KDE desktop environment**: events, recurring incidents and tasks (VTodos) in month, week, work-week, 3-day, day, schedule and task views. The data is not held by the app itself but by the KDE PIM service **Akonadi**, which synchronises local calendars and online calendars (**Nextcloud, Google Calendar, Outlook, CalDAV and many more** (via resources from `kdepim-runtime`)). That makes Merkuro the native desktop/mobile counterpart to web calendars.

The UI is **convergent** (Kirigami/QML, Qt 6): on the desktop with a collapsible sidebar (`MainDrawer`) and a menu bar (can be switched off), on mobile devices (Plasma Mobile) with swipe gestures and a bottom toolbar.

## Benefits

- **Seamless in KDE/Plasma:** Akonadi accounts, KDE frameworks (widgets, notifications, I18n), combinable with the suite's contacts/mail twin; single-instance over D-Bus.
- **Works offline:** local Akonadi calendars without a network; online calendars are mirrored in the background.
- **Convergent:** the same app on desktop and phone — a unique selling point in this documentation series for something like Nextcloud Calendar, which is a web calendar.
- **Public holidays by region, tasks with sorting (due date/alphabet/priority), reminders, ICS import by double-click, undo/redo, free view configuration** (swipeable grids, week numbers, occupancy/FreeBusy settings) — all configurable via `kalendarrc`.
- **Current and actively maintained:** monthly releases (26.08.2 Oct 2026), maintainers from the KDE PIM team.

## How it differs from comparable products

| Product (in this documentation) | Difference |
|--------------------------------|------------|
| **Nextcloud Calendar** | A web interface on a Nextcloud server; Merkuro is a native client that, among other things, works *with* Nextcloud servers (via CalDAV) but needs neither a server nor a browser. |
| **Davical** | A pure CalDAV server (backend); Merkuro is a client. The combination Davical + Merkuro (CalDAV resource) is possible. |
| **Google Calendar** | A SaaS service; Merkuro is a client for it (via the Google resource in kdepim-runtime), but open source and self-determined with Akonadi as the data layer. |
| **KOrganizer** (no section of its own) | The classic, feature-broad KDE calendar (integrated in Kontact, widgets toolkit); Merkuro is the deliberately slimmer QML-based successor build that also works on mobile. |

## Technical details

- **Stack:** C++/Qt 6 (≥ 6.9), QML UI with Kirigami, KDE Frameworks ≥ 6.25; KDE PIM libraries 6.8.2 (`Akonadi`, `AkonadiCalendar`, `AkonadiContact`, `KCalCore` …) plus KDE widgets such as `KF6::Holidays` (public-holiday calendar), `KF6::Contacts`, `KF6::DBusAddons`.
- **Model layer:** Qt models on top of Akonadi (`IncidenceWrapper`, `RemindersModel`, `HourlyIncidenceModel`, collection models); the views are pure QML delegates.
- **D-Bus identity:** `KDBusService::Unique` (desktop name `org.kde.merkuro.calendar`), object `/Calendar`, interface `org.kde.calendar.Calendar` with `showIncidenceByUid` (details in [api.md](api.md)).
- **File types:** `text/calendar` (`.ics`) as the MIME type, import via positional arguments.
- **Configuration:** KConfig `kalendarrc` (groups General/Views/TaskView/Editor), accounts in Akonadi.
- **Licence:** GPL-3; repo `invent.kde.org/pim/merkuro`, AppStream `org.kde.merkuro.calendar` (addon to `org.kde.merkuro`).

## Who it suits

- **Suitable:** KDE/Plasma users who want to manage calendar + tasks natively (also on Plasma Mobile); a mix of local and online calendars (Nextcloud/Google/CalDAV) without a web UI; anyone who values Akonadi-based reuse (contacts, mail suite).
- **Less suitable:** non-KDE environments (Akonadi is a heavyweight dependency), pure server/headless scenarios (use Davical/Nextcloud there), teams needing shared booking/partial administration in a browser (the domain of web calendars), and anyone expecting API hooks — the app offers none (see api.md).
