# DAViCal – Kurzbefehle (Stand 1.1.13)

## Web-Oberfläche

DAViCal bringt **eigene Tastaturkurzbefehle nicht mit** – die Weboberfläche (Principal-/Collection-Browser und -Editoren) ist klassisches server-gerendertes HTML ohne Tastenbelegungen (`accesskey`/`keydown` sind im Code nicht vorhanden). Browser-eigene Bedienung (Tab/Enter, Browser-Shortcuts) gilt unverändert.

## Direct-URLs als „Abkürzungen"

Häufige Seiten lassen sich über feste URLs direkt ansteuern (Basis `/davical`):

| URL | Ziel |
|-----|------|
| `/davical/index.php` | Principal-Übersicht / Login |
| `/davical/admin.php?action=browse&t=principal&type=1` | Benutzerliste |
| `/davical/admin.php?action=browse&t=principal&type=3` | Gruppenliste |
| `/davical/admin.php?action=edit&t=principal` | Neuen Principal anlegen |
| `/davical/admin.php?action=browse&t=external` | Externe Kalender-Abos (BIND) |
| `/davical/tools.php` | Import-/LDAP-Sync-Werkzeuge |
| `/davical/upgrade.php` | Datenbank-Migration |

## Wartungs-Einzeiler (CLI)

```sh
dba/update-davical-database          # Schema aktualisieren
scripts/tz-update.php                # Zeitzonen nachziehen
scripts/sync-remote-caldav.php       # Counter-Abgleich mit Gegenstelle
scripts/load_calendar.php datei.ics  # Kalender einspielen
```

## Kurzbefehle in den Calendern (Client-Seite)

Die eigentlichen Kalender-Kurzbefehle stellt der Client, nicht DAViCal:

- **Thunderbird (KALENDAR-Tab)**: `D` Tag, `W` Woche, `M` Monat, `N`/`P` vor/zurück, `T` heute, `Ctrl+N` neuer Termin
- **Kalendar**: `Strg+N` neuer Termin, Blättern mit `←`/`→` in der Monatsansicht
- **Apple Kalender**: `Cmd+N` Neuer Termin, `Cmd+1..6` Ansichten
- **Evolution**: `Strg+2` Kalender, `Strg+N` neuer Termin

Alle Befehle gehören zum jeweiligen Client und wirken auf DAViCal nur als normale CalDAV-Operationen (`PUT`/`REPORT`).
