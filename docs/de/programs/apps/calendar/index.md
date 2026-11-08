# Kalender-Systeme

## Kurz gesagt

Calendar behält deine Termine, auch die wiederkehrenden, in der richtigen Zeitzone. Es zeigt sie nach Monat, Woche, Tag oder als Agenda, und deine Aufgaben erscheinen daneben. Es beantwortet die Frage: Wo musst du sein, und wann?

**Befehl:** `fs-calendar`, ein Befehl je Programm mit Unterbefehlen ([ADR 0063](../../../decisions/0063-ein-programm-ein-befehl.md); Programme werden umgestellt, wenn sie ohnehin angefasst werden, nicht jedes ist es schon).

## Was hier anders ist

- Termine folgen dem offenen Standard JSCalendar (RFC 8984), und dieses Programm verantwortet ihn.
- Termine werden als iCalendar und als JSCalendar-JSON importiert und exportiert; der ursprüngliche Dateitext bleibt für jeden Termin erhalten.
- Ein Termin behält seine Uhrzeit über die Sommerzeit hinweg. Enthält eine Datei eine Zeitzone, die das Programm nicht lesen kann, lehnt es diesen Termin ab, statt ihn zur falschen Zeit zu speichern.
- Aufgaben werden nicht kopiert. Der Kalender fragt das Programm Tasks danach.
- Als vertraulich markierte Termine fehlen in Exporten, außer du gibst sie ausdrücklich frei.

## Wo es heute steht

Neueste Version: `v0.7.0`. Du kannst Termine anlegen, bearbeiten, löschen und auflisten, finden, was in einem Zeitraum passiert, und wiederkehrende Termine nutzen, bei denen einzelne Vorkommen geändert, entfernt oder hinzugefügt werden. Einladungen können verschickt, angenommen, vorläufig angenommen und abgelehnt werden. Die Agenda mischt Termine und Aufgaben. Ein kleiner Server und ein erstes, vorläufiges Fenster (Monat, Woche, Tag, Agenda, Import und Export) existieren.

Noch nicht da: Bearbeiten von Wiederholungsregeln oder einzelnen Vorkommen, Antworten auf Einladungen, Erinnerungen und mehrere Kalender im Fenster; CalDAV, Einladungen per E-Mail und Frei/Belegt-Berechnung. Der Kalender-Server ist noch nicht mit einem Aufgaben-Server verbunden. Große Dateien zu importieren ist langsam (etwa 45 Sekunden für 4.000 Termine). Einige späte Korrekturen am Kern wurden getestet, aber noch nicht von einem zweiten Prüfer begutachtet. Die Oberfläche ist ein Entwurf ohne Anbindung.

## Geplante Facetten

Facetten sind Teile eines Programms, die wie eigene Apps aussehen ([ADR 0061](../../../decisions/0061-facetten.md)). Jede bekommt einen eigenen Befehl, einen Link auf `fs-calendar` ([ADR 0063](../../../decisions/0063-ein-programm-ein-befehl.md)).

Vorgeschlagen, nicht gebaut:

- Calendar: deine Termine und Verabredungen.
- Buchung: Dinge und Orte reservieren, zusammen mit `fs-resources`.

## Übersicht

Dieser Bereich enthält Dokumentation für verschiedene Kalender- und Zeitmanagement-Systeme.

## Verfügbare Systeme

- **google-calendar** - Googles Kalender-Service
- **outlook-calendar** - Microsoft Kalender
- **ical** - iCalendar-Format-Unterstützung
- **davical** - CalDAV-Server
- **nextcloud-calendar** - Kalender-App für Nextcloud
- **kolab** - Groupware mit Kalender
- **caldav** - Protokoll für den Kalenderzugriff
- **sabredav** - CalDAV- und CardDAV-Server
- **memacs** - Kalenderdaten-Extraktion
- **planner** - Aufgaben- und Kalenderverwaltung
- **taskwarrior** - Aufgabenverwaltung mit Kalender
- **org-mode** - Organisationsmodus von Emacs
- **todoist** - Aufgabenverwaltung mit Kalender
- **toodledo** - Aufgaben- und Zeitmanagement
- **clockwork** - Kalendersynchronisation

## Was ist ein Kalender-System?

Ein Kalender-System ist eine Software zur Organisation von Terminen, Besprechungen und Aufgaben. Kalender-Systeme umfassen:

- Termine und Ereignisse verwalten
- Wiederkehrende Termine (Wiederholungen)
- Kalenderfreigabe und Zusammenarbeit
- Terminerinnerungen und Benachrichtigungen
- Kalenderabonnements
- Integration mit E-Mail und anderen Werkzeugen

## Anwendungsbereiche

- **Persönliches Zeitmanagement**: Termine und Aufgaben planen
- **Team-Kalender**: Teamtermine und Terminabstimmung
- **Geschäftskalender**: Firmentermine und Veranstaltungen
- **Bildung**: Schul- und Hochschulkalender
- **Veranstaltungen**: Veranstaltungsmanagement und Kalender

## Vorteile von Kalender-Systemen

- **Überblick**: Alle Termine an einem Ort
- **Zeitersparnis**: Automatisierung und Erinnerungen
- **Zusammenarbeit**: Kalender freigeben und gemeinsam nutzen
- **Integration**: Verbindung mit anderen Werkzeugen
- **Synchronisation**: Synchronisation über Geräte hinweg
- **Mobiler Zugriff**: Termine überall abrufen

## Auswahlkriterien

Bei der Wahl eines Kalender-Systems solltest du folgende Kriterien berücksichtigen:

- **Funktionen**: Welche Funktionen sind nötig?
- **Integration**: Wie gut passt das System in die bestehende Infrastruktur?
- **Synchronisation**: Synchronisation über Geräte hinweg
- **Bedienbarkeit**: Wie benutzerfreundlich ist es?
- **Sicherheit**: Datenschutz und Sicherheit
- **Open Source**: Ist das System Open Source?

## Verwandte Kategorien

- [Projektmanagement](../../suites/projectmanagement/) - Projektmanagement
- [Helpdesk](../helpdesk/) - Support- und Ticketsysteme
- [Kontakte/CRM](../people/) - Kontaktverwaltung

## Schnellstart

1. **Kalender-System auswählen**: Wähle ein System anhand der Anforderungen
2. **Installation/Konto**: System installieren oder Konto anlegen
3. **Konfiguration**: System anpassen und einrichten
4. **Termine importieren**: Bestehende Termine importieren
5. **Integration**: Integration mit anderen Werkzeugen

## Weitere Informationen

Weitere Informationen findest du in der Dokumentation der einzelnen Kalender-Systeme.

## Frontends

<!-- gen:frontends (Spiegel von docs/en; ADR 0011) — edits inside are overwritten -->
Analysierte Programme (6), nach Funktion, nichts kopiert (ADR 0012/0013):

- [DAViCal](frontends/davical/index.md) — DAViCal ist ein CalDAV-/CardDAV-Server in PHP auf PostgreSQL – ein schlanker, protokolltreuer selbst gehosteter Kalender-/Kontaktspeicher mit Web-Verwaltung.
- [Google Calendar](frontends/google-calendar/index.md) — Google Calendar (calendar.google.com) ist Googles Kalenderdienst: eine Weboberfläche plus Apps für Android, iOS, Wear OS und Apple Watch, gekoppelt mit Gmail, Meet, Tasks und (mit einem Premium-Abo…
- [Merkuro Calendar](frontends/merkuro/index.md) — Merkuro Calendar ist der **moderne Kalender-Client der KDE-Desktopumgebung** (Qt 6/QML/Kirigami, konvergent auf Desktop und Plasma Mobile).
- [Nextcloud Calendar](frontends/nextcloud-calendar/index.md) — Die Kalender-App des Nextcloud-Servers: eine Weboberfläche (Vue 3 + FullCalendar) über dem CalDAV-Backend (sabre/dav) des Nextcloud-Servers.
- [Outlook calendar](frontends/outlook-calendar/index.md) — Die Kalenderkomponente der Microsoft-Outlook-Linie: Web-App (outlook.com / Outlook im Web), das neue und das klassische Outlook für Windows, Outlook für Mac und iOS/Android — Daten im Postfach …
- [GNOME Planner](frontends/planner/index.md) — Planner ist der Projektplaner auf GNOME (App-ID `app.drey.Planner`): Aufgaben mit Start und Ende, Arbeit, Kosten und Abhängigkeiten (FS/SS/FF/SF mit Verzögerung), Ressourcen mit eigenen Arbeitskalendern, kritisch…

Übersicht: [frontends](frontends/index.md)
<!-- /gen:frontends -->
