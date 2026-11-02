# Nextcloud Calendar – Funktionen (verifiziert an v6.6.4, 2026‑10‑26)

Alle Punkte sind im Quelltext des Release-Tags v6.6.4 belegt; Fundstellen in [index.md](index.md#quellen).

## Ansichten und Navigation

- Fünf Hauptansichten, hart als Routen-Requirements definiert: **Tag** (`timeGridDay`), **Woche** (`timeGridWeek`), **Monat** (`dayGridMonth`), **Jahr/Multi-Monat** (`multiMonthYear`), **Liste** (`listMonth`); Zeitfenster direkt per URL adressierbar (`/{view}/{timeRange}`).
- **Ressourcen-Timeline** (FullCalendar resource-timeline) im Raum-Verfügbarkeits-Dialog.
- Seitenleiste mit Kalenderliste (Farben, Haken, Sortierung per Drag), Öffentlichen Kalendern, Terminbuchungs-Konfigurationen, Vorschlagsliste und „Ungeplante Aufgaben“.
- **Müll-/Papierkorb-Ansicht** für gelöschte Kalender und Objekte (`CalendarList/Trashbin.vue`).
- Suche, Tages-/Wochen-/Jahres-Navigation, „Heute“-Sprung; Event-Legende in den Einstellungen.
- **Permanent-Deep-Links**: `/apps/calendar/object/{uid}` löst Termine anhand der iCal-UID auf; `/new`, `/edit/{objectId}` als direktes Anlegen/Bearbeiten per Link.

## Termine (Editor)

- Zwei Editoren: **schneller Editor** (Zeitleiste/Klick) und **Voll-Editor** (`EditSimple.vue`/`EditFull.vue`).
- Felder: Titel, Kalenderzuordnung, Farbe, Start/Ende, ganztägig, **eigene Zeitzone je Termin**, Beschreibung, Ort, **Ressourcen/Räume** (Room-Availability-Modal mit Free/Busy-Timeline).
- **Wiederholungen** (RRULE-Editor inkl. Ausnahmen/Serien-Handling), **Erinnerungen/Alarme** (mehrere, wählbare Zeiteinheiten; Browser-Benachrichtigung und E-Mail laut offizieller App-Beschreibung; Default-Reminder einstellbar).
- **Dateianhänge** aus dem Nextcloud-Files-Ordner (einstellbarer Anlagen-Ordner).
- **Teilnehmer** mit Autocomplete (Nutzer, Gruppen, Circles, E-Mail-Kontakte), **Free/Busy-Ansicht** der Teilnehmer, Verfügbarkeits-Slotvorschläge, Einladungsannahme-Buttons (annehmen/vorläufig/ablehnen) direkt im Editor.
- **Konferenzen nur über Nextcloud Talk**: Talk-Raum bei Terminbuchung anlegen/verknüpfen (`AddTalkModal.vue`); keine anderen Konferenzanbieter im Quelltext.
- Termine als **ICS herunterladen** (am Server abschaltbar via `hideEventExport`); Verschieben/Resize per **Drag & Drop** in Kalenderansichten (`fullcalendar/interaction/eventDrop.js`).
- Kommentare/Dialogfelder für Objekte: **nicht verifiziert** – in v6.6.4 kein eigener Kommentar-Endpunkt in `routes.php`.

## Kalenderverwaltung

- Anlegen/Bearbeiten (Name, Farbe, Beschreibung, Zeitzone), Löschen mit **Wiederherstellung aus dem Papierkorb**, Teilen mit Nutzern/Gruppen/Circles (`EditCalendarModal/SharingSearch.vue`).
- **Öffentliche Freigabe** per Token-Link: Lese-/Schreib-Stufen, **Veröffentlichen** (`PublishCalendar.vue`), eigene **Embed-Ansicht ohne Nextcloud-Oberfläche** (`/embed/{token}`), interner Link.
- **WebCal-Abos** (`/components/Subscription`): externe Kalender abonnieren (schreibgeschützt; Verwaltung der Abos im UI).
- **Geburtstagskalender** (aus Contacts, Umschalter in den Einstellungen) und **Aufgaben-/Deck-Kalender** (VTODO-Komponenten; Fälligkeiten aus Tasks/Deck erscheinen im Kalender).
- **Delegation** (`store/delegation.ts`): Proxy-Lese-/Schreibrechte über CalDAV-Prinzipale verwalten (Delegierende und Delegationen einsehen, widerrufen).
- **ICS-Import** über die Einstellungen (`SettingsImportSection.vue`, Import-Bildschirm mit Fortschritt).

## Terminbuchung (Appointment-Booking)

- Buchungs-Konfigurationen mit Name, Beschreibung, Ort, Sichtbarkeit (`PUBLIC`/`CONFIRMED`), Zielkalender, **Wochenverfügbarkeit** (Slots je Wochentag + Zeitzone), Slotdauer, Inkrement, Vor-/Nachlauf, Mindestabstand zum nächsten Slot, Tageslimit, Start-/Enddatum, Future-Limit.
- Öffentliche Buchungsseite pro Nutzer (`/appointments/{userId}`) und pro Konfiguration (`/appointment/{token}`), Slot-Auswahl, **Bestätigungs-E-Mail-Schritt** (optional), Cleanup veralteter Buchungen per Hintergrund-Job.
- Buchungsseite im **Nextcloud-Profil** verlinkt (Profile-Link-Action).
- Hinweis: die separate ältere App „appointments“ ist eine Alternative; die Kalender-App kann selbst buchen.

## Meeting-Vorschläge (Terminumfragen, Serie 6.x)

- Vorschlag mit Titel, Beschreibung, Ort, Dauer, **Kandidatenterminen** und Teilnehmern anlegen/bearbeiten/löschen.
- **Abstimmungslink** für Externe (`{base}/calendar/proposal/{token}`, Anonym-Abstimmung), Antworten mit Vote-Status je Teilnehmer, **Benachrichtigung des Organisators** bei Antwort (`responseNotify`).
- **Umwandeln** eines Terminvorschlags in einen echten Kalendereintrag (Optionen, optional Talk-Raum, Einladungen an Teilnehmer).

## Sonstiges

- **Dashboard-Widget** „Kommende Termine“ (früheste Objekte).
- **Referenz-Provider**: Kalenderlinks erzeugen Vorschau-Karten in Talk, Text & Co.
- **Live-Sync der Tabs** über die Notify-Push-App (`calendar_sync`-Nachricht bei Objektänderungen).
- **Verfügbarkeit im Kontakte-Menü** der Server-UI (`ContactsMenuAvailability.vue`).
- Einstellungen: Zeitzone, Wochenanfang- und Standardansicht-Optionen, Wochenend-/Kalenderwochennummern-Schalter, Terminlimit-Popover, Geburtstags-/Aufgaben-/Popover-Schalter, Anlagen-Ordner.
- Auf Deutsch und vielen weiteren Sprachen lokalisiert (Ordner `l10n`, 185 Sprachen).
- Berechtigungsmodell: keine App-eigenen Rechte – Nextcloud-Nutzerrechte + CalDAV-ACLs; öffentliche Bereiche token-basiert.

## Was Nextcloud Calendar NICHT bietet

- **Keine Webhooks/Push-API** für Drittsysteme; Integration bleibt Pull über CalDAV (`sync-collection`, `getctag`).
- **Kein Offline-Modus und keine native App** – reine Web-App (Mobilgeräte nutzen CalDAV-Clients wie DAVx⁵).
- **Keine Synchronisation mit Google/Exchange/EWS**: keine write-back-Sync zu externen Diensten; externe Kalender nur lesbar per WebCal-Abo.
- **Keine Kalender-Schreibrechte in WebCal-Abos** (Abos sind read-only).
- **Keine weiteren Konferenzanbieter** außer Nextcloud Talk (kein Zoom/Teams/Meet).
- **Keine eigene Ressourcenverwaltung**: Räume/Ausstattungen müssen serverseitig als CalDAV-Ressourcen angelegt sein; die UI bildet sie nur ab.
- **Keine Terminserien-Buchung**: Buchung konfiguriert Wochen-Slots, aber keine wiederkehrenden Einzeltermine als Serie buchbar.
- **Keine gruppenweite Raum-Buchungs-Workflow-Engine** (kein Genehmigungs-Workflow über CalDAV-ACLs hinaus).
- **Keine eigenen Chat-Bots/Task-Automation** – Automatisierung ist dem Nextcloud-Ökosystem (Workflow-Apps, OCC) überlassen.
