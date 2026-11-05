# Nextcloud Calendar – Beschreibung

*(Quellbasis: nextcloud/calendar v6.6.4, 2026‑10‑26 – Details und Fundstellen in [index.md](../index.md#quellen))*

## Was das Programm macht

Nextcloud Calendar ist die **Kalender-Web-App des Nextcloud-Servers**: eine Weboberfläche zum Anlegen, Bearbeiten, Teilen und Einsehen von Terminen und Serien, deren Daten komplett in einem **CalDAV-Backend (sabre/dav) des Nextcloud-Servers** liegen. Die App selbst ist nur der Client – Kalender, Objekte und Freigaben sind normale CalDAV-Ressourcen, auf die parallel auch Desktop- und Handy-Clients (Thunderbird, DAVx⁵, Apple Kalender …) zugreifen.

Funktionen der Weboberfläche (v6.6.4): Tag-/Woche-/Monats-/Liste-/Jahresansichten (FullCalendar), Schnellerstellung, Vollbild-Editor mit Teilnehmern, Erinnerungen, Anlagen, Wiederholungen, Zeitzonen, Suche, Wochentag-Ansicht mit Ressourcen-Timeline, Geburtstagskalender (aus Contacts), WebCal-Abos, Aufgaben/Deck-Karten mit Fälligkeitsdatum, öffentliche Kalender- und Embed-Ansichten, **Terminbuchung per Link** (Appointment-Config mit Slot-Berechnung) und **Meeting-Vorschläge** (Doodle-artige Terminumfragen mit Abstimmungslink, seit der 6.x-Serie).

## Vorteile

- **Selbst gehostet, offene Standards:** alles RFC 5545/4791-konform über `remote.php/dav`; kein proprietäres Datenformat, beliebige CalDAV-Clients möglich.
- **Tiefe Integration in die Nextcloud-Suite:** Contacts (Teilnehmer-Autocomplete, Geburtstagskalender), Talk (Konferenzraum mit einem Klick, Verfügbarkeit im Contacts-Menü), Tasks/Deck (Fälligkeiten im Kalender), Circles/Gruppen (Gruppenkalender), Dashboard-Widget, Links-Vorschau (ReferenceProvider), Profil-Link zu Terminbuchungen.
- **Browser-Buchungsseite ohne Gegenkonto:** fremde Personen buchen Slots über einen Link; optional Bestätigungs-E-Mail-Schritt.
- **Kein Lock-in:** Daten bleiben auf dem eigenen Server; die App ist AGPL-Quelltext und lässt sich austauschen, solange der CalDAV-Server bleibt.
- **Aktive Entwicklung:** regelmäßige Releases (6.6.4 Okt 2026), gepflegte Abhängigkeiten, Support über help.nextcloud.com.

## Abgrenzung zu vergleichbaren Produkten

| Produkt | Art | Unterschied zu Nextcloud Calendar |
|---------|-----|-----------------------------------|
| **Davical** (in dieser Doku beschrieben) | reiner CalDAV/CardDAV-Server (PostgreSQL) | Davical ist nur das Backend ohne eigene Weboberfläche; Nextcloud Calendar umgekehrt nur das Frontend ohne eigenes Backend. Kombinationen aus beliebiger CalDAV-Server-App + Kalender-UI sind bei Nextcloud nicht vorgesehen – die App setzt den Nextcloud-Server mit seinem `dav`-App-Backend voraus. |
| **Google Kalender** (in dieser Doku beschrieben) | SaaS mit proprietärer REST-API | Google: Cloud-Dienst mit Push-Webhooks, ML-Funktionen, riesigem Ökosystem, aber Datenhoheit beim Anbieter. Nextcloud Calendar: volle Datenhoheit, keine Push-Webhooks, dafür CalDAV als neutraler Standard und Integration in selbst gehostete Groupware. |
| **Nextcloud „ appointments“-App** | externe Buchungs-App | Die Kalender-App bringt eigene Buchungsseiten bereits mit; die ältere separierte appointments-App ist eine Alternative für Spezialfälle. |
| Desktop-/Mobile-Kalender (KOrganizer, Thunderbird, Apple Kalender) | native Einzelplatz-Clients | Greifen oft auf dieselbe Nextcloud-Datenbank zu; die Web-App punktet mit Freigaben, öffentlichen Seiten, Buchung und Meeting-Umfragen ohne installierbaren Client. |

## Technische Details

- **Frontend:** Vue 3 + Pinia + vue-router, FullCalendar 6.1.21 (DayGrid/TimeGrid/List/MultiMonth + Resource-Timeline), eigene Bibliotheken `@nextcloud/cdav-library` (CalDAV-Client), `ical.js`/`@nextcloud/calendar-js` (ICS-Modellierung), Bau mit rspack; PHP-Teil nach Nextcloud AppFramework (Controller/Service/Db).
- **Backend-Zugriff:** ausschließlich CalDAV unter `{base}/remote.php/dav/` (siehe [api.md](api.md)); eigene Datenbanktabellen nur für Buchungs-Konfigurationen, Buchungen und Meeting-Vorschläge (`calendar_proposal_*`).
- **Server-Haken:** Dashboard-Widget, Referenz-Provider, Profil-aktion, Notifier (Notifications-App), Background-Job `CleanUpOutdatedBookingsJob`, Notify-Push-Listener für Live-Sync der Tabs, User-Migrator.
- **Laufzeit:** App v6.6.4 erfordert Nextcloud 32–35 und PHP 8.1–8.5 (Angaben aus `appinfo/info.xml`).
- **Kalender-Arten im UI:** persönliche, Gruppen-/Circles-Kalender (über serverseitige “Calendar”-Kollaboration), Geburtstagskalender, WebCal-Abos, öffentliche Freigaben (read/write, Link mit Token).

## Für wen geeignet

- **Geeignet:** Organisationen und Privaten, die Groupware selbst hosten (Nextcloud-Instanz vorhanden oder geplant), Wert auf Datenhoheit und Standard-Clients legen, Terminbuchung für Kundinnen/Termine und interne Terminumfragen ohne Zusatzdienste brauchen.
- **Weniger geeignet:** Nutzer ohne eigenen Server (dann lieber Google/Outlook), reine CalDAV-Setups ohne Nextcloud (dann Davical + beliebiger Client), und alle, die Push-Webhooks/Workflow-Automation der Kalender-API erwarten – die liefert diese Konstellation nicht.
