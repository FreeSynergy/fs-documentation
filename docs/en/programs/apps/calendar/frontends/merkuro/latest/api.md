# Merkuro – API (Merkuro Calendar 26.08.2, as of 2026-11-02)

## Naming first (important for this section)

The KDE calendar program started under the name **Kalendar was renamed to Merkuro with KDE Gear 23.08 (August 2023)** because the app outgrew events (contacts, planned e-mail integration). Repo and releases have since run under `pim/merkuro` (Invent) and `KDE/merkuro` (GitHub); the GitHub mirror `KDE/kalendar` stops at the last Kalendar tag v23.04.3. Product development lives on in full: the newest release is **Merkuro 26.08.2** (KDE Release Service, tag 2026-10-08), last activity commit 2026-11-02. This documentation describes the successor state.

## Version state and development

| Property | Value |
|----------|-------|
| Current version | **26.08.2** (`RELEASE_SERVICE_VERSION` in `CMakeLists.txt`), Release Service 26.08 from October 2026 |
| Versioning scheme | YY.MM.x since KDE Release Service (formerly 22.12, 23.04 …) |
| Development | active (maintainers Carl Schwan, Clau Cambra; daily commits; bugs via bugs.kde.org, product "merkuro") |
| Licence | GPL-3.0-or-later (`KAboutData … KAboutLicense::GPL_V3`) |
| Platform | KDE/Qt: Qt ≥ 6.9, KDE Frameworks ≥ 6.25, KDE PIM libraries 6.8.2 (Akonadi, AkonadiCalendar, AkonadiContact, KCalCore …) |
| Programs of the suite | `merkuro-calendar`, `merkuro-contact`, `merkuro-mail`, `merkurolauncher` – this doc covers `merkuro-calendar` |

## Basic architecture with regard to the API question

Merkuro Calendar is a **pure desktop client with no network server of its own and no REST/HTTP API of its own**. Events and tasks are not held by the app but by the **Akonadi PIM service** (its own local database + synchronisation resources from `kdepim-runtime`: CalDAV, Google, Exchange/WebDAV …). Every kind of "integration" therefore runs over one of these three levels:

1. the D-Bus interface of the running app (below),
2. Akonadi as the data layer (agent API/resources),
3. CLI arguments (ICS import).

## D-Bus interface of the app (verified against 26.08.2)

- **Single-instance:** `KDBusService(KDBusService::Unique)` in `src/calendar/main.cpp`; the bus name is derived from the desktop file name (`org.kde.merkuro.calendar`). A second launch activates the running instance and hands over arguments (`activateRequested`).
- **Registered object:** `/Calendar` on the session bus (`QDBusConnection::sessionBus().registerObject(u"/Calendar", this)` in `calendarapplication.cpp`).
- **Interface `org.kde.calendar.Calendar`** (introspectable via `src/calendar/org.kde.calendar.Calendar.xml`):

| Method | Signatures | Purpose |
|--------|-----------|---------|
| `showIncidenceByUid` | `uid: s`, `occurrence: QDateTime` (marshalling `((iii)(iiii)i)`), `xdgActivationToken: s` | Opens/focuses the event with the given iCal **UID** (with an optional recurrence instance); the activation token follows the XDG activation standard for focusing while opening |

Example:

```bash
qdbus org.kde.merkuro.calendar /Calendar \
  org.kde.calendar.Calendar.showIncidenceByUid \
  "uid-1234@example" "$(date -u +%Y-%m-%dT%H:%M:%S)" ""
```

(The exact marshalling of the QDateTime argument may need adjusting depending on the qdbus version — the interface itself is source-code verified.)

## CLI / file association

- Start: `merkuro-calendar [PATH|URL …]`. Positional arguments are passed through to the **ICS importer** during operation (`Importer::importCalendarFromFile` in `main.cpp`/`importer.cpp`); on first start the same path imports through `Importer`.
- Desktop file: `Exec=merkuro-calendar %u`, `MimeType=text/calendar`, `SingleMainWindow=true`, category `Office;Calendar` — the app can be registered as the default handler for `.ics` (`xdg-mime default org.kde.merkuro.calendar.desktop text/calendar`).
- Standard KDE options via `KAboutData` (`--help`, `--version`, Qt/KF flags). No special flags of its own exist in 26.08.2.

## Data layer: Akonadi (the actual calendar API)

- Merkuro reads/writes exclusively through **Akonadi**: `Akonadi::ETMCalendar` (the app holds an `ETMCalendar::Ptr`), Akonadi agents, the D-Bus service `org.freedesktop.Akonadi.*`.
- **Console control:** `akonadictl start|stop|restart|status` (Akonadi, not Merkuro). After installing `kdepim-runtime` the official README recommends an `akonadictl restart` so that online resources (CalDAV & co.) appear.
- **Programmatic use:** the C++/Qt libraries `Akonadi`, `AkonadiCalendar`, `AkonadiContact`, `KCalCore` (the same layer Merkuro itself builds against) — a language-independent public API of the app does not exist.
- **Online calendars** (Nextcloud, Google, Outlook, CalDAV) are synchronised by resources from `kdepim-runtime`; their credentials/protocols are those resources' API, not Merkuro's.

## Configuration (file level)

- KConfig file **`kalendarrc`** (`calendarconfig.kcfg`): groups `General` (among others `showMenubar`, `enableMaps`, `enableMailIntegration`, `lastOpenedView`), `GeneralView` (holidays `showHolidaysInCalendarViews`, `holidayRegions`, tasks on/off), `MonthView`/`WeekView`/`ScheduleView` (presentation, week numbers), `TaskView` (sorting DueTime/Alphabetically/Priority).
- Accounts/collections do not live in Merkuro but in Akonadi (`~/.local/share/akonadi/`).

## Webhooks / push

- **Not present and not planned.** Updates come from Akonadi resources (client-side polling/sync of the respective online calendar); Merkuro offers no endpoints for third parties.

## Limits

- No documented rate limits on the app side; what matters practically are the limits of the connected calendar services (via kdepim-runtime resources) and the Akonadi database.

## Sources (locations, all 26.08.2)

- Official release archive: `https://download.kde.org/stable/release-service/26.08.2/src/merkuro-26.08.2.tar.xz` (retrieved 2026-11-02; read locally: `CMakeLists.txt`, `README.md`, `src/calendar/{main.cpp,calendarapplication.{h,cpp},calendarconfig.kcfg,org.kde.calendar.Calendar.xml,org.kde.merkuro.calendar.desktop,org.kde.merkuro.calendar.metainfo.xml}`, `src/{launcher,mail,contacts}/CMakeLists.txt`).
- GitLab API project/tag list `pim/merkuro` (`https://invent.kde.org/api/v4/projects/pim%2Fmerkuro/repository/tags`): newest tag `v26.08.2` (2026-10-08); project `pim/kalendar` redirects to `pim/merkuro` (project ID 7106, `last_activity_at` 2026-11-02).
- Official product pages: `https://apps.kde.org/merkuro.calendar/` ("Merkuro Calendar"; formerly "Kalendar"), README line "Merkuro was formerly known as Kalendar." in the source.
- Rename coverage for the release series: KDE Gear 23.08 announcements ("Kalendar Becoming Merkuro", Aug 2023; linuxiac/phoronix as secondary sources).
