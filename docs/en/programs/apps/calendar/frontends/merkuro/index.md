# Merkuro Calendar

> **Rename:** the KDE calendar program launched in 2021 as **Kalendar** has been called **Merkuro since KDE Gear 23.08 (August 2023)**; repos, binaries and the AppStream ID follow the new name (`pim/merkuro`, `merkuro-calendar`, `org.kde.merkuro.calendar`). This section documents the current state of the successor.

Merkuro Calendar is the **modern calendar client of the KDE desktop environment** (Qt 6/QML/Kirigami, convergent on desktop and Plasma Mobile). Events, tasks (VTodo) and journals are not stored by the app itself but managed through the KDE PIM service **Akonadi**, which synchronises local and online calendars (Nextcloud, Google, Outlook, CalDAV … via `kdepim-runtime`). Since 2025/26 Merkuro is a small suite: calendar, contacts, mail and launcher.

- **Category:** calendar (native groupware client)
- **Licence:** GPL-3.0-or-later
- **Currently documented version:** **26.08.2** (KDE Release Service, tag 2026-10-08); project activity still high (last activity entry 2026-11-02)
- **Development status:** active; maintainers Carl Schwan and Clau Cambra (KDE PIM)

## File structure of this section

| File | Contents |
|------|----------|
| [description.md](latest/description.md) | What the program does, benefits, differentiation (incl. from Nextcloud Calendar, Davical, KOrganizer), technical details, who it suits |
| [features.md](latest/features.md) | Verified feature list + "What Merkuro does NOT offer" |
| [api.md](latest/api.md) | D-Bus interface `org.kde.calendar.Calendar`, CLI/ICS import, Akonadi as the data layer, configuration, version state |
| [menus.md](latest/menus.md) | Menu structure (File/Edit/View/Settings, mobile toolbar) taken from the QML source |
| [shortcuts.md](latest/shortcuts.md) | Verified keyboard shortcuts of the QML interface |
| [layout.md](latest/layout.md) | Module/directory structure, request flow (Akonadi models), configuration, deployment |

## Sources

State of all statements: source tarball and official pages, verification date 2026-11-02, version **26.08.2**, unless stated otherwise.

1. **Official release archive (primary source):** `https://download.kde.org/stable/release-service/26.08.2/src/merkuro-26.08.2.tar.xz` – read locally: `CMakeLists.txt` (version 26.08.2, Qt ≥ 6.9, KF ≥ 6.25), `README.md`, `src/calendar/*` (incl. `main.cpp`, `calendarapplication.{h,cpp}`, `calendarconfig.kcfg`, `org.kde.calendar.Calendar.xml`, desktop/metainfo files, QML under `src/calendar/qml/`), `src/components/*`, `src/{launcher,contacts,mail}`.
2. **GitLab Invent API** (project and tag list): `https://invent.kde.org/api/v4/projects/pim%2Fmerkuro` and `…/repository/tags` – newest tag `v26.08.2` (2026-10-08), last commit on the tag commit 2026-10-06; the project `pim/kalendar` answers as a redirect to `pim/merkuro` (project ID 7106, `last_activity_at` 2026-11-02) – this evidences the rename directly at the repo.
3. **Official product pages:** `https://apps.kde.org/merkuro.calendar/` (Merkuro Calendar) and `https://apps.kde.org/en-gb/merkuro/`; README quote "Merkuro was formerly known as Kalendar."
4. **GitHub mirror:** `https://github.com/KDE/merkuro` (active); the mirror `https://github.com/KDE/kalendar` stops at `v23.04.3` — useful as a lower bound for the rename.
5. **How the rename became known (secondary sources, for dating):** KDE Gear 23.08 announcements ("Kalendar Becomes Merkuro", August 2023; linuxiac.com, phoronix.com).

Reproduction recipe: fetch the tarball according to source 1; compare the version number in `CMakeLists.txt`, the D-Bus interface in `src/calendar/org.kde.calendar.Calendar.xml`, the settings in `src/calendar/calendarconfig.kcfg`, and the shortcuts in `src/calendar/calendarapplication.cpp`/`src/components/abstractmerkuroapplication.cpp` against this documentation.
