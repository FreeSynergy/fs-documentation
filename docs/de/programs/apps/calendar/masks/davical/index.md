# DAViCal Dokumentation

## Übersicht

DAViCal ist ein CalDAV-/CardDAV-Server in PHP auf PostgreSQL – ein schlanker, protokolltreuer Self-Hosted-Kalender-/Kontaktspeicher mit Web-Administration. Für FreeSynergy ist er der Backend-Skin hinter Merkuro, Thunderbird, DAVx⁵ und Apple-Geräten; gepflegt und aktiv entwickelt (1.1.13, Mai 2026).

## Dateistruktur

- [description.md](description.md) - Was DAViCal macht, Vorteile, Abgrenzung zu Radicale/Nextcloud/Xandio
- [features.md](features.md) - CalDAV/CardDAV, ACLs, Proxy, Tickets, BIND-Abos, Scheduling, was es NICHT kann
- [structure.md](structure.md) - Serveraufbau: PHP/PostgreSQL, htdocs/Schema, Deployment
- [menu.md](menu.md) - Menüpunkte der Web-Administration
- [shortcuts.md](shortcuts.md) - Kurzbefehle
- [api.md](api.md) - Exakte API 1.1.13: DAV-Methoden, REPORTs, Endpunkte, Tickets, Metriken

## Quellen

Alle Aussagen dieser Sektion stammen aus dem offiziellen Quelltext des aktuellen Release:

| Quelle | Fundstelle / URL | Wofür benutzt |
|--------|------------------|----------------|
| Quelltext-Release **r1.1.13** (11.05.2026) | `https://gitlab.com/api/v4/projects/davical-project%2Fdavical/repository/archive.tar.gz?ref=r1.1.13` | alle Dateien |
| GitLab-Projekt | `https://gitlab.com/davical-project/davical` (Tags, ChangeLog) | Versionsstand, Entwicklung aktiv |
| `htdocs/caldav.php` | Front-Controller, DAV-Header, Methoden-Dispatch | api.md, structure.md |
| `inc/DAVResource.php` | `FetchSupportedMethods`, `FetchSupportedReports` | api.md |
| `inc/interactive-page.php` | Hauptmenü Home/User Functions/Administration/Help | menu.md |
| `inc/ui/principal-*.php`, `collection-edit.php` | Browser-Spalten, Editor-Felder, Rechte-Matrix | menu.md |
| `dba/davical.sql` | Datenbanktabellen | structure.md |
| `config/apache-davical.conf`, `config/example-config.php` | Apache-Deployment, Konfigurationsoptionen, `/etc/davical/…`-Suchpfad | structure.md, features.md |
| `inc/caldav-MKTICKET.php`, `caldav-BIND.php`, `well-known.php`, `iSchedule*.php` | Tickets, BIND/webcal, Well-Known, iSchedule | api.md, features.md |
| `htdocs/metrics.php`, `freebusy.php`, `tz.php`, `feed.php` | Metriken-, FreeBusy-, Zeitzone-, Feed-Endpunkte | api.md |
| `scripts/` und `dba/` | CLI-/Migrationswerkzeuge | shortcuts.md, structure.md |
| Debian-Paket | `https://packages.debian.org/davical` (1.1.13-2, Mai 2026) | Paketierung, Nutzung |
| DAViCal-Wiki | `https://wiki.davical.org/` (Release Notes) | Versionshistorie |
| AWL-Bibliothek | `https://gitlab.com/davical-project/awl` | Framework-Herkunft |

Hinweis zur Recherche: Die XML-RPC-API, die in älterer Dritt-Dokumentation behauptet wird, ist in keinem Release-Tags ab 0.9.9.8 enthalten (per Quelltext-Suche geprüft, ebenso im AWL-Repositorium).
