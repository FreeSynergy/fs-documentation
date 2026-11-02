# DAViCal – Menü (Web-Oberfläche 1.1.13)

## Einstieg

DAViCal hat keine App-artige Navigation; die Weboberfläche ist ein seit 2006 gewachsenes Browser/Editor-System (AWL-Framework). Startseite `index.php` zeigt nach Login („Log On Please") die Principal-Übersicht; von dort zu Personen → deren Kalender-/Adressbuch-Sammlungen.

## Hauptmenü (jede Seite)

| Menüpunkt | Ziel | Unterpunkte |
|-----------|------|-------------|
| **Home** | `index.php` | **Logout** |
| **User Functions** | Principal-Browser (`admin.php?action=browse&t=principal&type=1`) | **View My Details** (eigener Principal-Datensatz) · **List Users** · **List Resources** · **List Groups** · **List Rooms** |
| **Administration** (nur Admins) | — | **Setup** (`setup.php`) · **Upgrade Database** (`upgrade.php`) · **Tools** (`tools.php`: Kalender importieren, LDAP-Synchronisation) · **List External Calendars** (BIND-Abos) · **iSchedule Configuration** (`iSchedule.php`) |
| **Help** | `help.php` (Hilfe zum aktuellen Bildschirm) | **DAViCal Homepage** · **DAViCal Wiki** · **Request Feature** · **Report Bug** (GitLab-Issues) |

Zusätzlich im Menü **User Functions** für Admins: **Inactive Principals**, **Create Principal** (neuer Benutzer, Ressource oder Gruppe).

## Principal-Browser

Spalten: ID (Link zur Bearbeitung), Name, Display Name, EMail, „Is Member of", „Has Members" (nur Gruppen). Filter nach Typ (Benutzer/Ressource/Gruppe/Raum) und Aktivstatus.

## Principal-Editor

Felder u. a.: Principal-ID (nur lesbar/neu), Preferred Language (Locale-Auswahl), Full Name, E-Mail (eindeutig; Identifikator für Invitations/FreeBusy), Typ, **Administrator**-Schalter („full rights to the whole DAViCal System"), Passwörter je nach Auth-Treiber.

## Collection-Editor

- Anzeige/Bearbeitung: Displayname, Typ (Kalender/Adressbuch), öffentlich-lesbar
- **ICS/vCard-Upload**: Datei ersetzt die Sammlung oder wird angehängt (`Append`)
- Externe Bind-URLs werden angezeigt (abonnierter Kalender)
- **Rechte-Matrix** je Principal mit DAViCal-Privilegien: Read, Write Metadata, Write Data, Override a Lock, Read/Write Access Controls, Create Events/Collections (bind), Delete Events/Collections (unbind), Read Free/Busy Information, „All privileges"/„Write"-Sammelrechte sowie je sieben Scheduling-Rechte (Deliver/Send Invitation/Reply, Query/Send Free-Busy)

## Hinweise

- Kein eigenes Menü für Termine: Kalenderführung passiert in den DAV-Clients
- Admin-Zugang kann per Domain/Port/Rolle eingeschränkt werden (`restrict_admin_domain`, `restrict_admin_port`, `restrict_admin_roles`)
- Deutsch als UI-Sprache vorhanden (po-/Übersetzungsanteil im Projekt, `supported_locales`)
