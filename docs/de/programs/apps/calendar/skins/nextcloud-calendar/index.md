# Nextcloud Calendar

Die Kalender-App des Nextcloud-Servers: eine Weboberfläche (Vue 3 + FullCalendar) über dem CalDAV-Backend (sabre/dav) des Nextcloud-Servers. Termine, Serien, Aufgaben (VTODO), Geburtstage und WebCal-Abos liegen als Standard-ICS-Objekte unter `remote.php/dav/`; dazu kommen Terminbuchung per Link, öffentliche/gebettete Kalenderansichten und Meeting-Vorschläge (Terminumfragen). Getrennt von der eigentlichen Datenhaltung: die App selbst ist nur Frontend plus kleine JSON-OCS-Endpunkte.

- **Kategorie:** calendar (Groupware-Weboberfläche)
- **Lizenz:** AGPL-3.0-or-later
- **Aktuell dokumentierte Version:** App **6.6.4** (Release 2026‑10‑26), benötigt Nextcloud Server 32–35 und PHP 8.1–8.5
- **Entwicklungsstatus:** aktiv (tägliche Commits, Release-Serie 6.6.x, Pflege durch das Nextcloud-Groupware-Team)

## Dateistruktur dieser Sektion

| Datei | Inhalt |
|-------|--------|
| [description.md](description.md) | Was das Programm macht, Vorteile, Abgrenzung (u. a. zu Davical und Google Kalender), technische Details, Für-wen-geeignet |
| [features.md](features.md) | Verifizierte Funktionsliste + „Was Nextcloud Calendar NICHT bietet“ |
| [api.md](api.md) | CalDAV-Backend, App-Routen, JSON/OCS-Endpunkte (Booking, Appointment-Configs, Proposals), Auth, Rate-Limits, SDKs |
| [menu.md](menu.md) | Navigations-/Menüstruktur aus Quelltext (AppNavigation, Editor, Einstellungen) |
| [shortcuts.md](shortcuts.md) | Tastenkürzel der Weboberfläche (verifiziert) + Direct-URL-Workflows |
| [structure.md](structure.md) | Request-/Modulstruktur, Datenmodell (DB-Tabellen, ICS), Konfiguration, Deployment |

## Quellen

Alle Aussagen dieser Sektion stammen vom Release-Quelltext und offiziellen Seiten; Prüfdatum 2026‑11‑02, Versionsstand überall **v6.6.4**, sofern nicht anders angegeben.

1. **Quelltext-Tarball des Release-Tags v6.6.4** (SHA des Tags `98f79f3bf69b2b3238f4a277ef7c57d4e374fddc`): `https://github.com/nextcloud/calendar/archive/refs/tags/v6.6.4.tar.gz` – lokal gelesen. Auswertungen: `appinfo/info.xml`, `appinfo/routes.php`, `lib/` (Controller, Listener, Migrations, Service), `src/` (Views, Stores, Komponenten), `package.json`, `CHANGELOG.md`, `README.md`.
2. **Tag-/Release-Liste via GitHub-API**: `https://api.github.com/repos/nextcloud/calendar/tags` – neuster stabile Tag `v6.6.4` (Gegenprüfung 2026‑11‑02: Tag‑SHA `98f79f3…` bestätigt; Hauptzweig bereits `6.7.0‑dev.1`); Release-Datum 2026‑10‑26 aus `CHANGELOG.md` des Tarballs; Repo-Aktivität `pushed_at` 2026‑11‑02 via GitHub-API.
3. **Projekt-Repo (Aktivitätsprüfung)**: `https://github.com/nextcloud/calendar` – aktiv gepflegt, AGPL, Repo nur Frontend; Backend-Fehler gehören zum Nextcloud-Server (README, Abschnitt Support).
4. **Offizielle Benutzer-/Admin-Dokumentation** (in `appinfo/info.xml` als `<documentation>` referenziert): `https://docs.nextcloud.com/server/latest/user_manual/en/groupware/calendar.html` und `https://docs.nextcloud.com/server/latest/admin_manual/groupware/calendar.html`.
5. **App Store-Eintrag**: `https://apps.nextcloud.com/apps/calendar` (Installation, Release-Tarballs unter `https://github.com/nextcloud-releases/calendar/releases`, laut README).
6. **Vom Client genutzte Herstellerbibliotheken** (Versionsstände aus `package.json` v6.6.4): `@nextcloud/cdav-library` ^2.7.0, `@nextcloud/calendar-js` ^8.1.6, `@nextcloud/calendar-availability-vue` ^3.0.0, `@fullcalendar/*` 6.1.21, Vue ^3.5.41, Pinia ^4.0.3.

Wiederholungs-Rezept: Tarball gemäß Quelle 1 holen, `appinfo/routes.php` + `lib/Controller/` (API), `src/components/AppNavigation` + `src/fullcalendar` (Menü/Shortcuts), `lib/Db` + `lib/Migration` (Datenmodell) mit dieser Dokumentation abgleichen; bei Abweichungen Versionsstand in allen Dateien aktualisieren.
