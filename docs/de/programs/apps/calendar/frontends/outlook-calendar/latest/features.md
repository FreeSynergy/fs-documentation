# Outlook-Kalender – Funktionen (verifiziert an Microsoft Graph v1.0 + offizieller Hilfe, 2026-11-02)

Grundlage: `event`-/`calendar`-Ressourcen von Microsoft Graph v1.0, die offizielle Tastaturkürzel-Seite (deckt neues Outlook, klassisches Outlook und Outlook on the web ab) und offizielle Hilfeartikel. Fundstellen in [index.md](../index.md#quellen). Als UI-Elemente, die nur aus der Kürzel-Liste erschlossen sind, gekennzeichnete Punkte sind Funktionsbelege, keine erfundenen Menüs.

## Termine und Serien

- Termine mit Titel, Rumpf (HTML/Text), Ort (+ mehrfache `locations`), Kategorien (`categories`), Priorität (`importance`), ganztägig (`isAllDay`), **eigene Zeitzone je Termin** (`DateTimeTimeZone`, `start`/`end`).
- **Wiederholungsserien** (`recurrence`, Typ `PatternedRecurrence`; Event-Typ-Feld `type`: singleInstance/occurrence/exception/seriesMaster) mit Einzel-Instanz-Verwaltung: Instanzen auflisten (`instances`), einzelne Occurrences löschen/ändern, `cancelledOccurrences` und `seriesMasterId` zur Serienbuchung; `iCalUId` als RFC-5545-UID.
- **Erinnerungen** pro Termin (`isReminderOn`, Minuten vor Beginn) mit Snooze/Zurückweisen als Aktionen (`snoozeReminder`, `dismissReminder`); im klassischen Outlook zusätzlich Reminder-Fenster (Kürzel `Alt+V,M`) und Erinnerungs-Sound konfigurierbar.
- **Dateianhänge** an Termine (`attachments`-Sammlung: Hinzufügen/Auflisten).
- Entwürfe für Meeting-Aktualisierungen (`isDraft` – Änderungen noch nicht an Teilnehmer versendet).
- Privatsphäre/Vertraulichkeit: `sensitivity` (`normal`/`personal`/`private`/`confidential`) und `showAs`-Status (`free`/`tentative`/`busy`/`oof`/`workingElsewhere`/`unknown`) als Free/Busy-Tarnung, `hideAttendees` (jeder Teilnehmer sieht nur sich selbst).

## Teilnehmer und Meetings

- **Einladungen** an Nutzer mit RSVP: annehmen / vorläuig / ablehnen (`accept`, `tentativelyAccept`, `decline`), Organisator kann absagen (`cancel`) und weiterleiten (`forward`).
- **Zeitvorschläge durch Teilnehmer** (`allowNewTimeProposals`) – Gegenstück zu Meeting-Umfragen anderer Produkte.
- **Free/Busy:** `getSchedule` (Belegung mehrerer Nutzer/Ressourcen/Verteiler abfragen) und **`findMeetingTimes`** (automatische Terminvorschläge aus Teilnehmer-Verfügbarkeit); im klassischen Outlook der **Assistent für die Terminplanung** (`Alt+X`).
- **Online-Besprechungen:** `isOnlineMeeting` + `onlineMeeting` (Join-Link über `onlineMeeting.joinUrl`; das alte `onlineMeetingUrl` ist Deprecation-Kandidat), Anbieter nach Wahl **nicht mehr umstellbar**; erlaubte Anbieter je Kalender über `allowedOnlineMeetingProviders` – praktisch **Teams** (`teamsForBusiness`); keine Zoom/Meet-Integration im Produkt.
- **Ressourcen:** Räume/Ausstattungen als CalDAV-lose Exchange-Ressourcen über dasselbe Postfachmodell (`getSchedule` unterstützt Ressourcentypen).
- Grenze: max. **500 Teilnehmer** pro Termin.

## Kalenderverwaltung und Freigabe

- Mehrere Kalender je Postfach, Kalenderordner/-gruppen, Farben (11 Theme-Farben + `hexColor`), Standardkalender markierbar, `changeKey` als Versionierung; Freigaben sind über die Assoziation **`calendarPermissions`** API-seitig ablesbar (`isSharedWithMe` kennzeichnet empfangene Freigaben).
- **Freigaben** mit Rechtestufen (canViewPrivateItems/canEdit/canShare als API-Abbild): Im klassischen Outlook per Kürzel belegt: „Freigegebenen Kalender hinzufügen" (`Alt+H,O,C`), „Kalender freigeben" (`Alt+H,S,C`), Ordner-Freigaberechte bearbeiten (`Alt+H,F,P`), **Kalender online veröffentlichen** (`Alt+H,P,O`).
- **Klassischer Outlook:** Kalender per E-Mail versenden (`Alt+H,E`).
- **Scheduling-Links/Buchung:** Die Produktlinie löst öffentliche Buchung über die separate App **Microsoft Bookings** – die Kalender-App selbst hat keine eigene Buchungsseite wie Nextcloud Calendar oder Google-Terminbuchung (Buchung extern, daher hier als Grenze notiert).
- **To Do/Aufgaben:** eigene To-Do-Ansicht im Client (`Ctrl+5` in der Navigationsliste des klassischen Outlook) – Aufgaben liegen bei Microsoft To Do, nicht als VTodo im Kalenderpostfach wie bei CalDAV-Servern.

## Clients und Ansichten

- **Neues Outlook / Outlook on the web:** Ansichten Tag, Arbeitswoche, Woche, Monat, 3-Tage, Listenansicht (aus der offiziellen Kürzel-Tabelle: `Strg+Alt+1` Tag, `Strg+Alt+2` Woche/Arbeitswoche, `Strg+Alt+4`/`Alt+ =` Monat, `Alt+3` 3-Tage; Listenansicht ohne Kürzel); „Heute" `Alt+Shift+Y/Home`.
- **Klassisches Outlook (Windows):** Feinere Tagesraster 1–10 Tage (`Alt+1`…`Alt+0`), Ganze Woche/Vollwoche, Monatsansicht, Datumsnavigator, „Nächste 7 Tage".
- **Sync über Geräte:** Exchange-Postfach-Sync (EAS/mobile Outlook-Apps); Outlook für iOS/Android als eigene Apps.
- **Live-Updates:** Push-artige Aktualisierung der Clients über Exchange-Protokolle; für Drittsysteme echte **Webhooks** über Graph change notifications (siehe api.md).
- **Kalender-Sharing-Modernisierung (2026):** Umstellung der Kalenderfreigabe von MAPI auf ein REST-Modell läuft tenantweise (Sekundärquellen office365itpros.com 2026-05, admin365.blog 2026-07 – als Sekundärquelle gekennzeichnet).

## Was Outlook-Kalender NICHT bietet

- **Kein CalDAV/CardDAV** in den Outlook-Clients: „Outlook für Mac unterstützt nicht die CalDAV- oder CardDAV-Internetstandards" (offizieller Hilfeartikel, Fundstelle index.md). An Outlook.com/Exchange Online gibt es für externe CalDAV-Clients keinen offiziellen Zugang; Drittanbieter-Connectoren (z. B. Outlook CalDav Synchronizer) inoffiziell.
- **Privatkonto-Zugänge entzogen:** Für kostenlose Outlook.com-Kontone wurden die Protokolle EAS/MAPI/CalDAV zum Januar 2025 abgeschaltet (technische Umstellung auf das neue Outlook; Primärquelle der Support-Seite war am Recherchetag nicht erreichbar – als Sekundärinformation aus techcommunity-Beitrag gekennzeichnet, **im Detail nicht verifiziert**).
- **Kein Self-Hosting:** Outlook.com ist reiner Dienst; ein selbst betriebenes Gegenstück wäre Exchange Server (on-prem) oder ein CalDAV-Server (davical in dieser Serie).
- **Keine eigene Terminbuchungs-Seite** (wie Google-Terminbuchung / Nextcloud Booking) – dafür separate Bookings-App.
- **Keine Meeting-Umfrage als Kalender-Feature** im Stil von Doodle: dem Outlook-Kalender fehlt ein äquivalentes „Vorschläge zur Abstimmung stellen"-Objekt (Nextcloud Calendar bietet das als Proposals, Google Kalender „Umfragen"); dem Outlook-Termin fehlt ein Abstimmungs-Modell – `allowNewTimeProposals` ist nur der Einzel-Vorschlag eines Teilnehmers. (Als Grenzziehung nach Quellenlage der Ressourcen-Seiten formuliert.)
- **Keine Drittanbieter-Konferenzanbieter** außer Teams (siehe `allowedOnlineMeetingProviders`).
- **Keine offene ICS-API für Dritte:** Termine sind Postfachobjekte (MAPI/Graph), kein ICS-Objektspeicher wie bei CalDAV-Servern; Import/Export ist Client-Funktion (ICS-Dateien importierbar), nicht Standard-Objektformat der Server-API.
- **EWS-Abhängigkeiten brechen** (Abschaltung Exchange Online Okt 2026–Apr 2027).
- **Keine Client-API für eigene Add-ins im neuen Outlook wie im klassischen:** COM-Add-ins/VBA/Macro-Kürzel (`Alt+F11`, `Alt+F8`) existieren nur im klassischen Outlook (offizielle Kürzel-Seite listet sie unter „classic Outlook").
