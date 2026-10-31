# OpenProject - Funktionen

## Übersicht

OpenProject bündelt Aufgabenverwaltung, Terminplanung, agile Methoden, Dokumentation und Abrechnung in einer Webanwendung. Welche Module sichtbar sind, hängt von der Edition (Community/Enterprise) und den Projekteinstellungen ab.

## Funktionsbereiche

### 1. Arbeitspakete (Work Packages)

- **Typen**: Anforderungen, Aufgaben, Meilensteine, Risiken, Fehler (anpassbare Typen)
- **Attribute**: Status, Priorität, Zugewiesene, Version, Termine, Dauer, Fortschritt; zusätzliche Felder über benutzerdefinierte Felder
- **Relationen und Abhängigkeiten**: abhängige/ablösende, teilende, verwandte Arbeitspakete
- **Detail-Ansicht**: rechter Split-Screen mit Beschreibung, Aktivitäten, Kommentaren, Anhängnissen, Watchern
- **Inline-Bearbeitung**: Felder direkt in der Tabelle ändern (versionsabhängig)
- **Kopieren, Verschieben, Teilen**: Arbeitspakete zwischen Projekten kopieren, per Link teilen

### 2. Tabellen, Abfragen und Filter

- **Modul "Arbeitspakete"**: filterbare, sortierbare Tabelle mit konfigurierbaren Spalten
- **Abfragen speichern**: private und öffentliche Abfragen mit Filtern, Sortierung, Gruppierung
- **Filterkriterien**: Projekt, Typ, Status, Zugewiesene, Version, Datum, Freitext u. v. m.
- **Export**: CSV-Export der Tabellenansicht (weitere Formate versionsabhängig)

### 3. Terminplanung und Meilensteine

- **Gantt-Diagramm**: Balken per Drag & Drop verschieben, Abhängigkeiten ziehen
- **Roadmap**: Meilensteine und Versionen je Projekt als Zeitleiste
- **Baseline-Vergleich**: Plan-Ist-Vergleich von Terminen (Enterprise; versionsabhängig)
- **Portfolios und Projektberichte**: zusammengefasste Auswertungen (Enterprise; versionsabhängig)

### 4. Agile Boards und Backlogs

- **Board-Typen**: Scrum (Sprint-Backlog), Kanban, task Boards, Mischformen (Verfügbarkeit versionsabhängig)
- **Sprints**: Backlog-Spalte, Sprint-Zuweisung, aktive Sprints mit Burndown
- **Epics**: Epics als Klammer über mehreren Projekten im Backlog
- **Spalten und WIP-Limits**: über die Board-Einstellungen konfigurieren
- **Board-Reports**: Burndown und Zyklusanalyse

### 5. Zeit und Kosten

- **Zeitberichte**: Buchungen je Arbeitspaket, Datum und Aktivität
- **Kostenberichte**: verursachte und geplante Kosten je Projekt und Benutzer
- **Budgets**: Budgets und Kostensätze je Projekt (versions-/editionsabhängig)
- **Auslastung**: Ist-/Plan-Vergleich in den Berichten

### 6. Zusammenarbeit und Dokumentation

- **Wiki**: Seiten mit verschachtelter Navigation und Historie
- **Foren**: Diskussionsforen je Projekt
- **Meetings**: Terminkalender, Protokolle, Aufgaben direkt aus Meetings
- **Aktivitäten und Nachrichten**: Projekt-Aktivitätsstrom, Watch-Abonnements
- **Dateien**: Uploads und Anhänge an Arbeitspaketen

## Module und Integrationen

- **Module je Projekt aktivierbar**: Aktivitäten, Arbeitspakete, Board, Gantt, Meilensteine, Termine, Wiki, Dateien, Nachrichten, Meetings, Budget und Zeit/Kosten (Namen versionsabhängig)
- **Kalender-Abonnement**: iCal-Feed für "Meine Arbeiten" und Projektaktivitäten
- **E-Mail-Eingang**: Arbeitspakete per E-Mail anlegen und aktualisieren (IMAP-Konfiguration)
- **Datei-Integrationen**: Verknüpfung mit Nextcloud/OneDrive (versions-/editionsabhängig)
- **Webhooks**: Ereignisse an externe Systeme (siehe [api.md](api.md))

## Konfiguration

- **Administration**: Typen, Status, Workflows, benutzerdefinierte Felder, Projekte, Benutzer, Rollen und Rechte
- **Systemeinstellungen**: Farbschema, Anmeldepflicht, Passwörter, E-Mail, Zeitzone, Sprache
- **Projektrollen**: granulare Berechtigungen je Rolle (Module sehen, bearbeiten, verwalten)
- **Instanz-Konfiguration**: Umgebungsvariablen (Datenbank, Secret, Instanz-URL) bei Docker-/Paketinstallation

## Was OpenProject NICHT kann

- **Keine dokumentierte Shortcut-Liste**: es gibt keine zentral gepflegten Anwendungshortcuts (siehe [shortcuts.md](shortcuts.md))
- **Kein voll offlinefähiger nativer Client**: die Oberfläche ist responsiv, aber ein Offline-Modus fehlt
- **Kein Echtzeit-Co-Editing im Wiki**: Seiten werden nacheinander bearbeitet, mit Kollisionswarnung
- **Kein App-Marketplace**: Erweiterbarkeit läuft über API, Webhooks und Kernmodule; ein Plugin-System wie bei Redmine existiert nicht
- **Nicht alles ist kostenlos**: Baselines, Portfolios und manche SSO-/Datei-Integrationen sind Enterprise-Funktionen (versionsabhängig)
- **Keine andere Datenbank als PostgreSQL**

## Erweiterungen und Plugins

- **Kein Plugin-System**: OpenProject setzt statt Plugins auf API, Webhooks und ausgebaute Kernmodule
- **REST-API v3**: Skripte, Dashboard-Anbindungen und BI-Auswertungen über die dokumentierte Schnittstelle
- **Webhook-Empfänger**: CI/CD-Ketten und Chat-Bots reagieren auf Arbeitspaket-Ereignisse
- **Optische Anpassung**: eigenes Farbschema/CSS; tiefgreifende UI-Extensions sind nicht vorgesehen
- **BIM/IFC-Sichten** für Bauplanung als Zusatzmodul (versions-/editionsabhängig)
