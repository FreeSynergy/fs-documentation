# Baïkal/Davical - Menüpunkte

## Übersicht

Baïkal/Davical hat zwei Oberflächen: den **DAV-Endpunkt** (protokollgetrieben, kein Menü) und die **Web-Administration** unter `/admin/`. Die Menüpunkte beziehen sich auf die Administration.

## Admin-Web-UI (Hauptmenü)

| Menüpunkt | Beschreibung |
|-----------|--------------|
| Users | Benutzer anlegen/löschen, Passwort, Admin-Recht, Suspend |
| Calendars | Kalender je Benutzer: Name, Beschreibung, Farbe, Schreibrecht (read-write/read) |
| Subscriptions | abonnierte Kalender (Share-Links, Lesezugriff) verwalten |
| Address Books | CardDAV-Adressbücher je Benutzer anlegen/freigeben |
| User-specific shares | Kalender-/Adressbuch-Freigaben zwischen Benutzern |
| Settings | Instanzname, Registrierung offen/geschlossen, Kalenderlimits, Timeout |
| Baïkal UI / Davical-Modus | UI-Umschalter: Baïkal verteilt ein eigenes Frontend über Davical; „classic Davical" zeigt die alte Admin-Maske |

## Kontext-Menüs / Aktionen

- **User bearbeiten** - Anzeigename, Admin-Schalter, Passwort-Reset
- **Kalender löschen** - löscht Kalender und alle Ereignisse (unwiderruflich)
- **Share-Link erzeugen** - öffentlicher Lese-Link für einen Kalender
- **Principal sperren** - Benutzer deaktivieren, ohne Daten zu löschen

## Rollen

| Rolle | Sichtbare Menüs |
|-------|-----------------|
| Admin | alle Menüs, auch Settings |
| Normaler Benutzer | keine Admin-UI — Zugriff nur über CalDAV-/CardDAV-Clients |

## DAV-Endpunkte (für Clients, kein Menü)

- `/.well-known/caldav` und `/.well-known/carddav` - Discovery
- `/dav.php` bzw. `/` (Rewrite) - CalDAV-/CardDAV-Wurzel
