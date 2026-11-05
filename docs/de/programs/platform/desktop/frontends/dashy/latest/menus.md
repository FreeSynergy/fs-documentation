# Dashy - Menüpunkte

## Übersicht

Dashy wird überwiegend über die Konfigurationsdatei gesteuert; die Oberfläche bietet zusätzlich eine Kopfzeile mit Navigation, ein Einstellungspanel für die interaktive Bearbeitung und Kontextmenüs an Kacheln. Welche Punkte sichtbar sind, hängt von der Mindestrolle und davon ab, ob Schreibzugriff erlaubt ist.

## Hauptmenüpunkte (Kopfzeile)

### 1. Titel und Logo
- **Funktion**: Kennzeichnung der Startseite, oft mit Untertitel
- **Details**: aus `pageInfo.title` und `pageInfo.description`; Logo optional; Klick führt auf die Startseite zurück

### 2. Seiten-Menü
- **Funktion**: zwischen Unterseiten wechseln, wenn `pages` definiert sind
- **Details**:
  - Dropdown oder Leiste mit Name und Symbol je Seite
  - jede Seite nutzt eine eigene Konfigurationsdatei
  - nicht sichtbar bei einer einzelnen Seite

### 3. Suchleiste
- **Funktion**: Kacheln filtern, Websuche starten, URLs direkt öffnen
- **Details**:
  - Fokus ist nicht nötig: Tippen startet die Suche sofort
  - `Enter` öffnet den ersten Treffer oder startet die Websuche
  - Kurzkommandos (`searchBangs`) sind möglich
  - Leeren mit `Esc`

### 4. Launchpad
- **Funktion**: alle Kacheln aller Seiten in einer Rasteransicht öffnen
- **Details**:
  - praktisch, wenn viele Seiten existieren

### 5. Ansicht wechseln
- **Funktion**: zwischen Startansicht, Minimalansicht und Arbeitsbereich wechseln
- **Details**:
  - Minimal: ohne Beiwerk, nur Kacheln und Suche
  - Arbeitsbereich: eine Sektion großflächig

### 6. Bearbeiten (Schaltfläche „Bearbeiten“)
- **Funktion**: Bearbeitungsmodus für Kacheln und Sektionen starten
- **Details**:
  - nur mit ausreichender Rolle sichtbar
  - im Modus erscheinen Bearbeitungs- und Löschungssymbole an den Objekten
  - Speichern schreibt in die Konfigurationsdatei
  - abschaltbar, wenn die Datei nicht aus der Oberfläche verändert werden darf

### 7. Einstellungspanel (Zahnrad)
- **Funktion**: Konfiguration interaktiv ändern
- **Details** (Bezeichner je Version unterschiedlich):
  - **Allgemein und Layout**: Titel, Beschreibung, Sprache, Spaltenanzahl, Dichte, Kopf-/Fußzeile
  - **Theme**: Schema wählen, Farben anpassen, eigenes CSS
  - **Suche und Statusanzeigen**: Suchmaschine, Kurzkommandos, Websuche, Prüfintervall und erwartete Antworten
  - **Interaktiver Editor**: Sektionen, Kacheln und Seiten verwalten
  - **Import/Export**: Datei herunterladen, hochladen, Sicherungen ansehen
  - **Authentifizierung**: Hinweise zu Nutzern und Rollen (Bearbeiten der Schlüssel bleibt der Datei/Umgebung vorbehalten)

### 8. Nutzer-Menü
- **Funktion**: Anmelden, Abmelden, Zwei-Faktor-Einstieg
- **Details**:
  - erscheint nur bei konfigurierter Authentifizierung
  - Login-Seite bei fehlender Sitzung
  - Abmelden beendet die Sitzung

## Kontextmenüs an Kacheln und Sektionen

### Rechtsklick auf eine Kachel
- **Funktion**: alle Öffnungsarten und Objektaktionen auf einen Schlag
- **Details**:
  - In neuem Tab öffnen
  - Im gleichen Tab öffnen
  - Im Modal öffnen
  - Im Arbeitsbereich öffnen
  - URL in die Zwischenablage kopieren
  - **Bearbeiten** und **Löschen** (nur im Bearbeitungsmodus)

### Schwebende Werkzeuge (Bearbeitungsmodus)
- **Funktion**: Objekt bearbeiten, verschieben, duplizieren, entfernen
- **Details**:
  - Bearbeiten öffnet den Kachel-Dialog (Titel, URL, Symbol, Farbe, Öffnungsart, Tags)
  - Ziehen an der Griffzone verschiebt die Kachel im Raster
  - Sektionen lassen sich als Ganzes umsortieren
  - Änderungen werden beim Speichern in die Datei geschrieben

### Kachel-Dialog
- **Funktion**: alle Felder einer Kachel pflegen
- **Details**:
  - `title`, `url`, `description`, `icon`, `target`, `tags`, `keywords`
  - Anzeigeoptionen: Name ausblenden, kompakt, Farbe, Rahmen
  - Statusprüfung: Prüf-URL und erwartete Antwort, Hotkey-Ziffer für Schnellstart

### Sektions-Dialog
- **Funktion**: Gruppe konfigurieren
- **Details**:
  - Name, Reihenfolge, Spaltenanzahl
  - Widgets der Sektion hinzufügen und einstellen
  - Kacheln hinzufügen oder entfernen, Sektion löschen (mit Sicherheitsabfrage)

## Menüs nach Rolle

### Administrator
- Volle Schreibrechte: Editor, Import/Export, Theme-Editor, Seiten anlegen
- Nutzer und Schlüssel verwalten (in der Datei bzw. über Umgebungsvariablen)
- Statusprüfungen und Intervalle global einstellen
- API-Schreibzugriff (Bearer-Token oder Admin-Sitzung)

### Angemeldeter Nutzer
- Startseite, Suche, Launchpad, Ansichten, Rechtsklick-Menüs
- Bearbeiten nur, wenn die Mindestrolle es erlaubt
- Eigene Vorlieben (z. B. aktives Theme) bleiben lokal im Browser

### Anonym (ohne Anmeldung)
- Bei konfigurierter Authentifizierung: nur die Login-Seite
- Ohne Authentifizierung: vollständige Ansicht, aber ohne Bearbeiten, wenn der Editor gesperrt ist

### Gesperrter Editiermodus
- Alle Änderungen laufen dann über Datei, Deployment oder API

## Shortcuts

Die vollständige Tastatursteuerung (Tippen sucht, `Tab`, Pfeiltasten, `Enter`, `Alt+Enter`, `Ctrl+Enter`, `Esc`, Hotkeys `0`–`9`) steht in [shortcuts.md](shortcuts.md).
