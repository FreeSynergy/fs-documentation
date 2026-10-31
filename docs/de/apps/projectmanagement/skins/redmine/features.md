# Redmine - Funktionen

## Übersicht

Redmine hält den Kern klein und deckt trotzdem den kompletten Projektalltag ab: Issues, Zeiterfassung, Wiki, Foren, Dateiablage, Roadmap und Berichte. Fast alles lässt sich je Projekt aktivieren, je Rolle berechtigen und per Plugin erweitern.

## Funktionsbereiche

### 1. Issues und Tracker

- **Tracker**: eigene Issue-Arten (Fehler, Unterstützung, Aufgabe ...) mit eigenen Feldern, Status und Workflows
- **Attribute**: Status, Priorität, Kategorie, Meilenstein (Version), Zugewiesene, Erwartetes Ende, geschätzte Zeit
- **Beziehungen**: steht in Beziehung zu, dupliziert / wird dupliziert von, blockiert / wird blockiert von, liegt vor / folgt auf
- **Journaux**: vollständige Historie je Issue inkl. Feldänderungen und Notizen
- **Beobachten, Kopieren, Teilen**: Issues abonnieren, klonen, per privatem Link freigeben
- **Benutzerdefinierte Felder**: Text, Liste, Auswahl, Boolean, Datum, Benutzer, Projekt - je Tracker und Rollensichtbarkeit

### 2. Zeiterfassung

- **Buchungen** je Issue mit Aktivität, Stunden und Kommentar; auch ohne Issue je Projekt möglich
- **Später buchen / Zeiten kopieren** und Sammeleinträge je Tag
- **Berichte**: Zeitauswertung nach Benutzer, Aktivität, Issue, Projekt; kumulierte Ansicht
- **Verbleibende Zeit** aus Schätzung minus Buchung je Issue

### 3. Projekte und Rollen

- **Projekte mit Unterprojekten**: rollen und Rechte gelten projektweise, Mitgliedschaften je Mitglied und Projekt
- **Module pro Projekt** an-/abschaltbar: Issues, Zeiterfassung, Wiki, Boards (Forum), Dokumente, Dateien, News, Kalender, Roadmap 
- **Workflow-Konfiguration**: erlaubte Statusübergänge, Feldrechte und Buttons je Rolle und Tracker
- **Enumerationen**: Status, Prioritäten, Aktivitäten, Zeiterfassungsaktivitäten zentral pflegbar

### 4. Dokumentation und Kommunikation

- **Wiki** je Projekt mit Textile/Markdown (Markdown seit Redmine 2.x, Standard Textile), History, Sperrungen
- **Boards (Foren)** mit Themen, Antworten, Admin-Funktionen
- **News** je Projekt mit Kommentaren, auf der My page gesammelt
- **Dateien und Anhänge**: Dokument-Ordner, Anhänge an Issues/Wiki, unbegrenzte Dateitypen (konfigurierbar)

### 5. Roadmap, Kalender und Gantt

- **Roadmap**: offene Meilensteine mit fälligen Issues, Fortschrittsbalken
- **Kalender**: Termine/erwartetes Ende je Issue als Monatsansicht, iCal-Abonnement
- **Gantt**: statischer Gantt-Chart der Issue-Termine (Core, ohne Drag & Drop; interaktiv per Plugin)

### 6. Abfragen und Berichte

- **Filterbare Issue-Listen** projektintern oder projektübergreifend, Gruppierung, Spaltenauswahl
- **Öffentliche Abfragen** für alle oder Gruppen freigeben
- **Export**: CSV und Atom-Feed im Kern; PDF über Browser-Druck oder Plugins
- **Berichte-Modul** (Administration): Issues, Zeiterfassung nach Benutzer/Projekt/Monaten

### 7. Versionsverwaltung

- **Repository-Browser** für Git, Subversion und Mercurial (CVS entfallen; versionsabhängig)
- **Commit-Referenzen**: `Issues #123`, `Refs #999` verknüpfen Commits automatisch mit Issues
- **Changeset-Notizen** im Issue-Journal

### 8. Benachrichtigungen

- **E-Mail-Benachrichtigungen** bei Änderungen beobachteter oder zugewiesener Issues
- **Meine Benachrichtigungen** (Redmine 4.2+): in-App-Benachrichtigungen mit Glocke
- **RSS/Atom** für Issues, Aktivitäten, Kalender

## Module und Integrationen

- **Repositorien**: Git/SVN integriert, Webhooks via Plugin
- **Kalender**: ICS-Feed je Projekt/Benutzer mit Token-URL
- **WebDAV**: nicht im Core (Plugin), Dateien-Plugin `redmine_webdav` verbreitet
- **Auth-Anbindung**: LDAP im Core; SAML/OAuth/CAS über Plugins

## Konfiguration

- **Administration**: Benutzer, Gruppen, Projekte, Rollen, Tracker, Status, Workflows, benutzerdefinierte Felder, Boards, E-Mail-Benachrichtigungen, Authentifizierung, Sitzungen
- **Projekt-Einstellungen**: Module, Tracker-Freigaben, Wiki-Einstellungen, Board-Zuordnung
- **Instanz**: `config/configuration.yml` (E-Mail, Repositorien, Uploads), Umgebungsvariablen, `settings.yml`-Einstellungen über die UI

## Was Redmine NICHT kann

- **Keine agilen Boards im Kern**: kein Kanban/Scrum ohne Plugins (z. B. easyGantt/redmineup Boards - Drittanbieter, teils kostenpflichtig)
- **Kein Echtzeit-Editing und keine WebSockets**: Seiten werden klassisch neu geladen
- **Keine nativen Apps**: nur Browser-Oberfläche (responsiv)
- **Keine Webhooks im Kern**: eingehend/ausgehend nur als Plugin
- **Kein Zwei-Faktor-Auth im Kern** (Plugin; versionsabhängig, ob inzwischen geliefert)
- **Kein modernes Theme/Dark-Mode serienmäßig**: dunkle Darstellung nur über CSS-Themes
- **Kein Undo** für gespeicherte Änderungen (nur Journal-Rückschau)

## Erweiterungen und Plugins

- **Plugin-Architektur**: eigene Rails-Plugins mit Migrationen, Routen, Berechtigungen; großer Katalog auf redmine.org/projects/redmine/wiki/plugins
- **Verbreitete Plugins**: easyGantt/Interaktive Gantt-Plugins, Kanban-Plugins, `redmine_webhook`, `redmine_recaptcha`, Themes (RedmineUP, Curious Mind u. a.)
- **Themes**: CSS-basiert, einfach austauschbar (`public/themes/`)
- **Skripte**: REST-API für Automatisierung; `rake`-Kommandos für Wartung (siehe [shortcuts.md](shortcuts.md))
