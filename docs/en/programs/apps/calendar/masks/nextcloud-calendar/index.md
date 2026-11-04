# Nextcloud Calendar

The calendar app of the Nextcloud server: a web interface (Vue 3 + FullCalendar) above the CalDAV backend (sabre/dav) of the Nextcloud server. Events, series, tasks (VTODO), birthdays and WebCal subscriptions live as standard ICS objects under `remote.php/dav/`; on top come appointment booking by link, public/embedded calendar views and meeting proposals (polls). Kept separate from the actual data storage: the app itself is only a frontend plus a few small JSON-OCS endpoints.

- **Category:** calendar (groupware web interface)
- **Licence:** AGPL-3.0-or-later
- **Currently documented version:** app **6.6.4** (released 2026-10-26), requires Nextcloud Server 32–35 and PHP 8.1–8.5
- **Development status:** active (daily commits, release series 6.6.x, maintained by the Nextcloud groupware team)

## File structure of this section

| File | Contents |
|------|----------|
| [description.md](description.md) | What the program does, benefits, differentiation (incl. from Davical and Google Calendar), technical details, who it suits |
| [features.md](features.md) | Verified feature list + "What Nextcloud Calendar does NOT offer" |
| [api.md](api.md) | CalDAV backend, app routes, JSON/OCS endpoints (booking, appointment configs, proposals), auth, rate limits, SDKs |
| [menu.md](menu.md) | navigation/menu structure from the source (AppNavigation, editor, settings) |
| [shortcuts.md](shortcuts.md) | keyboard shortcuts of the web interface (verified) + direct-URL workflows |
| [structure.md](structure.md) | request/module structure, data model (DB tables, ICS), configuration, deployment |

## Sources

All statements in this section come from the release source code and official pages; verification date 2026-11-02, version **v6.6.4** everywhere unless stated otherwise.

1. **Source tarball of release tag v6.6.4** (tag SHA `98f79f3bf69b2b3238f4a277ef7c57d4e374fddc`): `https://github.com/nextcloud/calendar/archive/refs/tags/v6.6.4.tar.gz` – read locally. Analyses: `appinfo/info.xml`, `appinfo/routes.php`, `lib/` (controllers, listeners, migrations, services), `src/` (views, stores, components), `package.json`, `CHANGELOG.md`, `README.md`.
2. **Tag/release list via the GitHub API**: `https://api.github.com/repos/nextcloud/calendar/tags` – newest stable tag `v6.6.4` (cross-checked 2026-11-02: tag SHA `98f79f3…` confirmed; main branch already `6.7.0-dev.1`); release date 2026-10-26 from `CHANGELOG.md` of the tarball; repo activity `pushed_at` 2026-11-02 via the GitHub API.
3. **Project repo (activity check)**: `https://github.com/nextcloud/calendar` – actively maintained, AGPL, repo is frontend only; backend bugs belong to the Nextcloud server (README, Support section).
4. **Official user/admin documentation** (referenced in `appinfo/info.xml` as `<documentation>`): `https://docs.nextcloud.com/server/latest/user_manual/en/groupware/calendar.html` and `https://docs.nextcloud.com/server/latest/admin_manual/groupware/calendar.html`.
5. **App Store entry**: `https://apps.nextcloud.com/apps/calendar` (installation, release tarballs under `https://github.com/nextcloud-releases/calendar/releases`, according to the README).
6. **Vendor libraries used by the client** (version states from `package.json` v6.6.4): `@nextcloud/cdav-library` ^2.7.0, `@nextcloud/calendar-js` ^8.1.6, `@nextcloud/calendar-availability-vue` ^3.0.0, `@fullcalendar/*` 6.1.21, Vue ^3.5.41, Pinia ^4.0.3.

Reproduction recipe: fetch the tarball according to source 1, compare `appinfo/routes.php` + `lib/Controller/` (API), `src/components/AppNavigation` + `src/fullcalendar` (menu/shortcuts), `lib/Db` + `lib/Migration` (data model) against this documentation; if anything differs, update the version state in all files.
