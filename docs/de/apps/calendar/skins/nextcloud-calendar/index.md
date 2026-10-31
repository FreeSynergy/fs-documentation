# Nextcloud Calendar Dokumentation

## Übersicht

Nextcloud Calendar ist die Kalender-App der quelloffenen Groupware Nextcloud: ein Web-Kalender im Browser für Termine, Meetings und wiederkehrende Ereignisse. Die Daten liegen auf dem eigenen Server und werden über CalDAV mit allen üblichen Kalendernclients synchronisiert (Apple Kalender, Thunderbird, GNOME Evolution, DAVx⁵). Teamfunktionen runden den Umfang ab: automatische Gruppenkalender für jede Nextcloud-Gruppe, Freigaben mit Lese-, Bearbeitungs- und Verfügbarkeitsrechten, öffentliche Links, Verfügbarkeitsumfragen („Zeiten finden"), Talk-Terminumfragen sowie Raum- und Ressourcenbuchung. Die App läuft in jeder Nextcloud-Instanz - self-hosted oder bei einem Hosting-Anbieter.

## Dateistruktur

- [menu.md](menu.md) - Kopfzeile, Seitenleiste, Werkzeugleiste, Freigabe-Dialoge und Menüs nach Rolle
- [features.md](features.md) - Funktionen, ehrliche Grenzen („Was Nextcloud Calendar NICHT kann") und Integrationen
- [description.md](description.md) - Beschreibung, Vorteile und Abgrenzung zu Google Calendar, SOGo und Radicale
- [structure.md](structure.md) - Seiten- und Dialogaufbau, UI/UX, Drag & Drop, Responsive Design
- [shortcuts.md](shortcuts.md) - Tastatursteuerung (inkl. ausdrücklich als nicht dokumentiert markierter Tasten)
- [api.md](api.md) - CalDAV-Endpunkte, interne App-Endpunkte, Authentifizierung, Beispiele

## Hinweis

Die App erscheint mit jedem Nextcloud-Major-Release in einer neuen Version (aktuell 5.x-Reihe); Details wie Dialogaufbauten können je nach Serverversion leicht abweichen. Diese Dokumentation beschreibt den aktuellen Stand und markiert Unsicheres als „(nicht dokumentiert)".
