# Redmine - Menüpunkte

## Übersicht

Redmine navigiert klassisch: eine Kopfzeile mit Hauptreitern und Suchfeld, darunter Breadcrumb-Leiste und Projekt-Reiter, rechts optional eine Randspalte. Menüs sind stark rollenabhängig; Admins sehen zusätzlich den Reiter „Administration".

## Hauptmenüpunkte

### 1. Meine Startseite (My page)
- **Funktion**: persönliche Startseite
- **Details**: Block-Layout (administrativ, Projekte, Dokumente, News, Aktivitäten); Blockauswahl unter „Optionen"; neuere Versionen mit „Meine Aktivitäten"

### 2. Projekte
- **Funktion**: Liste aller Projekte (mit Suche)
- **Details**: Spalten Name, Beschreibung, Status; Häkchen für Unterprojekte und „Öffentlich"; neues Projekt (Admin-Recht)

### 3. Administration (nur Admins)
- **Funktion**: Instanz-Verwaltung
- **Details**:
  - Benutzer, Gruppen
  - Projekte, Rollen und Rechte
  - Issue-Tracker, Issue-Status, Workflows, Issue-Felder (benutzerdefinierte Felder)
  - Aufzählungen (Prioritäten, Aktivitäten, Zeiterfassungs-Aktivitäten)
  - Boards (Foren), Berichte
  - E-Mail-Benachrichtigungen, Authentifizierung (Passwort/LDAP), Sitzungen (neuere Versionen)
  - Plugins, Infos

### 4. Benutzer-Menü (oben rechts)
- **Funktion**: eigenes Konto
- **Details**: Mein Konto, Freundschaften/Aktivitäten, Einstellungen (Benachrichtigungen, Benachrichtigungs-Feed), Abmelden

### 5. Hilfe-Link
- **Funktion**: Kontexthilfe
- **Details**: zeigt standardmäßig rotes Hilfe-/Versionszeichen; Ziel konfigurierbar (text/URL)

### 6. Suchfeld (Kopfzeile, rechts)
- **Funktion**: globale Suche
- **Details**: Suchbegriff, Optional „Titel durchsuchen", Filter je Dokumenttyp nach Trefferanzeige

### 7. Breadcrumb-Leiste (Projekt)
- **Funktion**: zum Projektanfang
- **Details**: Projektname als Link auf Projektübersicht

### 8. Projekt-Reiter
- **Funktion**: Module des offenen Projekts
- **Details** (Namen/Reihenfolge je Version):
  - Übersicht
  - Aktivitäten
  - Roadmap
  - Issues
  - Zeiterfassung
  - News
  - Dokumente
  - Dateien
  - Wiki
  - Kalender
  - Boards
  - Einstellungen (Projekt-Admin)

## Kontext-Menüs

### Issue-Seite
- Links: Bearbeiten, Notiz hinzufügen, Chronik, beobachten, Löschen (rechteabhängig)
- Oben: Status-Änderung über Bearbeiten, „Nach Issue springen", Vorgänger/Nachfolger
- „Bearbeiten" öffnet Inline-Formular mit Statusfeld und Notizfeld

### Issue-Listen
- Spaltenköpfe: Sortieren, Gruppieren (über Listenoptionen), Spaltenauswahl
- Oben: Filterleiste mit „+ Filter hinzufügen", Abfrage speichern/öffentlichen, CSV-Export, Atom-Feed

### Wiki
- Reiter „Seite bearbeiten", „Historie", „Anhängen"; „Änderungen vergleichen" im Versionsvergleich

### Zeiterfassung
- „Log time" je Issue; Auswertung über „Berichte" im Zeiterfassungs-Modul

## Menüs nach Benutzerrolle

### Administrator
- Alle Projekt-Reiter plus Administration (s. o.)
- Projekt-Einstellungen, Mitglieder-Verwaltung, Modul-Auswahl

### Bearbeiter (z. B. Entwickler/Reporter)
- Issues: anlegen, bearbeiten, Status je Workflow wechseln, Notizen, Zeit buchen
- Wiki, Boards, Dateien je nach Projektmodul-Rechten
- „Meine Startseite", globale Suche, eigene Abfragen speichern (Recht „Issue-Abfragen verwalten")

### Leser / anonyme Benutzer
- Nur Lesezugriff auf freigeschaltete öffentliche Projekte
- Keine „Bearbeiten"- und „Neues Issue"-Buttons
- Anonyme Nutzung nur wenn in Authentifizierung erlaubt

## Hinweise

- Reiter und Beschriftungen folgen der Installationssprache (Deutsch vollständig übersetzt)
- Plugins blenden zusätzliche Reiter und Menüpunkte ein (z. B. Kanban, Gantt)
- Projektmodule aus-/einschalten entfernt die zugehörigen Reiter für alle Rollen
