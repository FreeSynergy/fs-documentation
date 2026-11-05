# DAViCal – Menu (web interface 1.1.13)

## Getting in

DAViCal has no app-like navigation; the web interface is a browser/editor system that has grown since 2006 (AWL framework). The start page `index.php` shows the principal overview after login ("Log On Please"); from there go to people → their calendar/address book collections.

## Main menu (every page)

| Menu item | Target | Sub-items |
|-----------|--------|-----------|
| **Home** | `index.php` | **Logout** |
| **User Functions** | principal browser (`admin.php?action=browse&t=principal&type=1`) | **View My Details** (own principal record) · **List Users** · **List Resources** · **List Groups** · **List Rooms** |
| **Administration** (admins only) | — | **Setup** (`setup.php`) · **Upgrade Database** (`upgrade.php`) · **Tools** (`tools.php`: import calendars, LDAP synchronisation) · **List External Calendars** (BIND subscriptions) · **iSchedule Configuration** (`iSchedule.php`) |
| **Help** | `help.php` (help for the current screen) | **DAViCal Homepage** · **DAViCal Wiki** · **Request Feature** · **Report Bug** (GitLab issues) |

Additionally in the **User Functions** menu for admins: **Inactive Principals**, **Create Principal** (new user, resource or group).

## Principal browser

Columns: ID (link to editing), Name, Display Name, EMail, "Is Member of", "Has Members" (groups only). Filter by type (user/resource/group/room) and active status.

## Principal editor

Fields include: principal ID (read-only/new), Preferred Language (locale selection), Full Name, e-mail (unique; identifier for invitations/FreeBusy), type, **Administrator** switch ("full rights to the whole DAViCal System"), passwords depending on the auth driver.

## Collection editor

- View/edit: display name, type (calendar/address book), publicly readable
- **ICS/vCard upload**: the file replaces the collection or is appended (`Append`)
- External bind URLs are shown (subscribed calendar)
- **Permission matrix** per principal with DAViCal privileges: Read, Write Metadata, Write Data, Override a Lock, Read/Write Access Controls, Create Events/Collections (bind), Delete Events/Collections (unbind), Read Free/Busy Information, "All privileges"/"Write" aggregate rights, plus seven scheduling privileges each (Deliver/Send Invitation/Reply, Query/Send Free-Busy)

## Notes

- No separate menu for events: calendar management happens in the DAV clients
- Admin access can be restricted by domain/port/role (`restrict_admin_domain`, `restrict_admin_port`, `restrict_admin_roles`)
- German is available as a UI language (po-/translation share in the project, `supported_locales`)
