# Google Calendar – Menu and navigation structure (web interface, as of 2026)

Google Calendar has no menu that can be reviewed in source code (closed source). This structure is evidenced **exclusively by official German-language help pages** of the help centre and the Workspace admin knowledge base (locations given in parentheses each time; full URLs in [index.md](index.md)). The menu labels below are therefore the German originals; the English gloss in brackets is the corresponding label of the English interface.

## Header

| Element | Content / evidence |
|---------|--------------------|
| „Heute" (Today; top left) | jump to today's date; next to it arrows to nearby dates (help "View your day, week, or month") |
| Mini calendar (top left) | date selection by click (same help) |
| „Eintragen" (Create; left) | creation menu; among other things it contains **„Terminplan"** (Appointment schedule) for booking pages (help "Create an appointment schedule") |
| Search (top) | free-text search across calendars/events (mirror of the API `q` search) |
| Views (top right) | **Day, Week, 4 days, Month, Year, Schedule** (Tag, Woche, 4 Tage, Monat, Jahr, Terminübersicht) — the last one chosen becomes the default view (help "View your day, week, or month") |
| „Einstellungen" (Settings; gear, top right) | opens the settings page (see below) (same help) |
| Account/avatar (far right) | Google account switcher (multiple accounts) |

## Left sidebar

- **Mini calendar** with month navigation
- Calendar list groups (help "View your day, week, or month"):
  - **„Meine Kalender"** (My calendars) — calendars you own (clicking toggles visibility)
  - **„Weitere Kalender"** (Other calendars) — shared primary calendars of people, rooms or groups; tick to hide, unsubscribe via the menu
- **„Weitere Kalender hinzufügen"** (Add other calendars; plus next to „Weitere Kalender") with the evidenced entries:
  - **„Kalender abonnieren"** (Subscribe to calendar) — search by e-mail address (help "Subscribe to someone else's calendar")
  - **„Per URL"** (By URL) — add public calendars via link/ICS URL (same help)
  - (creating a new calendar also happens in this area; the exact menu label was not individually evidenced in the help page checked)
- **Three-dot menu per calendar** → **„Einstellungen und Freigabe"** (Settings and sharing) — the "Calendar settings" subpage includes among other things **„Kalender exportieren"** (Export calendar) and the **iCal addresses** („Öffentliche Adresse im iCal-Format" / public iCal address, „Privatadresse im iCal-Format" / private iCal address) (help "Export events from your Google Calendar")
- **„Weitere Details"** (More details; left) → the **„Ihre Zeit im Blick"** (Your time at a glance) dashboard with a time breakdown, "People you interact with", "Manage pinned people" (up to 10) (help "See how much time you spend in meetings")

## Settings page (gear → „Einstellungen" / Settings)

Categorised on the left; the following are evidenced:

- **„Ansichtsoptionen"** (View options) — start of week, custom view, reference calendar (help "View your day, week, or month"; changes are saved automatically)
- **„Importieren & Exportieren"** (Import & export) — „Exportieren" (Export; ZIP with the ICS of all calendars) and import (help "Export events from your Google Calendar")

Further categories (General, Notifications, app/add-on access) do exist in the interface but are not individually named in the primary articles retrieved → **not verified**.

## Event editor (dialog)

- Clicking on a time opens the event quick editor; at the top it can be switched to **„Fokuszeit"** (Focus time) (help "Use focus time" — day/week view only, with a fixed start/end time)
- The expanded event page with guest rights, reminders, location, attachments, conference (not every field is individually evidenced in the articles checked; API fields in [api.md](api.md))

## Appointment schedule editor (booking page)

Reached via „Eintragen" (Create) → „Terminplan" (Appointment schedule); area labels according to the help "Create an appointment schedule":

1. **„Zeitplan für Terminreservierung"** (Appointment availability; left area): title, **Termindauer** (appointment length; also „Benutzerdefiniert"/custom), **Allgemeine Verfügbarkeit** (General availability; daily windows; „Ganztags nicht verfügbar" / not available all day, „Diesem Tag eine weitere Zeitspanne hinzufügen" / add another time range to this day, „Für alle Tage übernehmen" / apply to all days)
2. **„Zeitfenster für Reservierungen"** (Booking availability): max./min. lead time (default: at least 4 hours)
3. **„Angepasste Verfügbarkeit"** (Specific times and days; single exceptions such as public holidays)
4. **„Einstellungen für reservierte Termine"** (Booking settings): **Puffer** (buffer), **Maximale Anzahl von Reservierungen pro Tag** (maximum number of bookings per day), **Berechtigungen für Gäste** (booking options for guests)
5. **„Kalender"** (Calendar): target calendar (primary/secondary)
6. Optional entry point: „Terminplan erstellen" (Create an appointment schedule) in the **„Reservierungsseiten"** area

## Google Workspace administration (Admin console)

- **Admin console → Calendar → Advanced settings → "Appointment schedules with payments"** (ON/OFF for Stripe payments in appointment schedules) (Workspace knowledge article "Allow paid appointment schedules in Calendar")
- Time Insights can be disabled organisationally (help "See how much time you spend in meetings")
- Export can be restricted administratively (help on export)

## Mobile apps (Android/iOS)

The apps have their own, slimmer navigation (day/week/month view, calendar list, "+" to create). The help articles on subscribing and on appointment schedules state expressly: **subscribing to calendars and creating appointment schedules only works in the web browser on a computer, not in the app**. A complete app menu structure was not extracted from primary sources → deliberately not documented in detail.
