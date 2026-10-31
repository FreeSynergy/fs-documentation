# OpenProject - Menüpunkte

## Übersicht

Die Navigation von OpenProject besteht aus der Projektauswahl oben links, der Modul-Leiste (linkes Menü bzw. „Hauptmenü"-Schaltfläche) und dem Benutzermenü oben rechts. Welche Module erscheinen, hängt vom Projekt und von den Rechten ab; Modulnamen sind versionsabhängig.

## Hauptmenüpunkte

### 1. Projektauswahl (oben links)
- **Funktion**: Projekt wechseln oder globale Sicht („Alle Projekte") wählen
- **Details**:
  - Suchfeld über alle Projekte
  - Zuletzt besuchte Projekte
  - Globale Module, wenn kein Projekt ausgewählt ist

### 2. Übersicht (Modul)
- **Funktion**: Projekt-Startseite
- **Details**: Projektdaten, Kennzahlen, aktive Meilensteine, Project-Card, benutzerdefiniertes Dashboard-Layout je Version

### 3. Aktivitäten
- **Funktion**: Chronik aller Änderungen im Projekt
- **Details**: Filter nach Typ (Arbeitspaket, Wiki, Datei), Datum, Benutzer; Abonnement per E-Mail

### 4. Meilensteine
- **Funktion**: Liste aller Meilensteine des Projekts
- **Details**: nach Status gruppiert, Link zu Terminen und Roadmap

### 5. Roadmap
- **Funktion**: Zeitleiste der Versionen und Meilensteine
- **Details**: Datumsgrenzen der Versionen, Fortschrittsanzeige

### 6. Arbeitspakete
- **Funktion**: Tabelle aller Aufgaben und Anforderungen
- **Details**:
  - Filterleiste und Spaltenauswahl
  - Gespeicherte Abfragen (links)
  - Gruppenansicht, Timeline-Ansicht (versionsabhängig)

### 7. Boards (agile Boards)
- **Funktion**: Scrum-/Kanban-Boards und task Boards
- **Details**:
  - Board auswählen, Board-Einstellungen öffnen
  - Backlog-Ansicht mit Sprints und Epics
  - Reports (Burndown, Zyklusanalyse)

### 8. Gantt
- **Funktion**: Terminplanung als Balkendiagramm
- **Details**: Drag & Drop für Termine, Abhängigkeiten, Baselines (Enterprise, versionsabhängig)

### 9. Termine / Meetings
- **Funktion**: Terminkalender und Meeting-Protokolle
- **Details**: Meeting anlegen, Protokollpunkte, Aufgaben ableiten

### 10. Wiki, Dateien, Nachrichten, Forum
- **Funktion**: Projektdokumentation und Kommunikation
- **Details**: Wiki mit Navigation; Dateien als Upload-Bereich; Forum mit Themensträngen

### 11. Zeit- und Kostenberichte / Budget
- **Funktion**: Zeiterfassung, Kosten, Budgets
- **Details**: Berichte nach Benutzer/Aktivität; Budgetmaske (editionsabhängig)

### 12. Benutzermenü (oben rechts)
- **Funktion**: Konto, Benachrichtigungen, Abmeldung
- **Details**:
  - Glocke: Benachrichtigungen und Lesezeichen
  - Avatar: Meine Kontoeinstellungen, Sprache, Farbschema, Abmelden
  - Hilfe-Menü (?-Symbol): Versionshinweise, Kurzanleitung, Tastatur (Browser)

## Kontext-Menüs

### Arbeitspaket-Kontextmenü
- In Tabelle: Rechtsklick bzw. Symbol für Öffnen, Bearbeiten, Kopieren, Löschen, Teilen
- Detail-Split: Übergänge des Workflows als Buttons, Watch togglen, Anhängnisse anhängen
- Zeilen-Selektion: Mehrfachauswahl für Massenbearbeitung (Status, Zuweisung)

### Query-/Spaltenkopf-Menü
- Spalten ein-/ausblenden, sortieren, gruppiern
- Abfrage speichern, als Standard setzen, teilen (Link)

### Board-Kontextmenü
- Karte: Öffnen, Verschieben, Zuweisen, Label ändern
- Spalte: Karten hinzufügen, Spalte bearbeiten (Status-Zuordnung)
- Board-Einstellungen: Karten, Sprints, Filter, Epics

## Menüs nach Benutzerrolle

### Administrator (Instanz-Admin)
- Alle Projekt-Menüs plus **Administration**:
  - Benutzer, Gruppen, Projekte anlegen/löschen
  - Rollen und Rechte, Typen, Status, Workflows
  - Benutzerdefinierte Felder, Aufzählungen (Prioritäten, Aktivitäten)
  - System-/Login-Einstellungen, Webhooks, API-Dokumentation
  - Plugins/Integrationen, Nachrichten (Ankündigungen)

### Bearbeiter (Mitglied mit Rechten)
- Arbeitspakete anlegen/bearbeiten, kommentieren, Zeit buchen
- Boards nutzen, Karten verschieben, Wiki bearbeiten
- Eigene Abfragen speichern; keine Projekt- oder Systemeinstellungen

### Leser (Nur-Lese-Recht)
- Module ansehen: Arbeitspakete, Gantt, Meilensteine, Wiki, Aktivitäten
- Keine Bearbeiten-Buttons, keine Board-Aktionen
- Abhängig vom Projekt: anonyme Sicht nur für freigegebene Projekte

## Hinweise

- Modulnamen und -reihenfolge sind admin-konfigurierbar und je Version unterschiedlich
- Blenden Projekte einzelne Module aus, verschwinden sie aus der Navigationsleiste
- Die globale Navigation ohne Projektauswahl zeigt nur kontextneutrale Module
