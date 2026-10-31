# LaunchBoard - Menüpunkte

## Übersicht

LaunchBoard arbeitet mit einer schmalen Kopfzeile, einem seitlichen Editor-Werkzeug und Einstellungsdialogen für Board, Instanz und Konto. Welche Punkte sichtbar sind, hängt von der Rolle ab: **Administrator**, **Editor** und **Betrachter** sehen unterschiedliche Menüs.

## Hauptmenüpunkte (Kopfzeile)

### 1. Board-Auswahl (links)
- **Funktion**: zwischen den Boards wechseln, die der Nutzer sehen darf
- **Details**:
  - Dropdown mit allen freigegebenen Boards, Suche nach Board-Namen
  - Startboard je Endgerät (Desktop/Mobil) einstellbar
  - Administratoren und Editoren: „Neues Board anlegen“ im selben Menü

### 2. Bearbeiten (rechts)
- **Funktion**: Board-Inhalte ändern: Widgets hinzufügen, verschieben, skalieren, löschen
- **Details**:
  - Für Administratoren und Editoren sichtbar, Betrachter sehen den Punkt nicht
  - Im Bearbeitungsmodus öffnet sich die Widget-Bibliothek als Seitenpanel
  - Änderungen werden sofort gespeichert (kein separates „Speichern“ nötig)

### 3. Suchleiste (Mitte)
- **Funktion**: Apps, Links und Boards finden
- **Details**:
  - Autocomplete mit Treffern aus Board-Inhalten
  - Websuche über eine einstellbare Standard-Suchmaschine
  - Kurze Eingabemuster (Präfix je Suchmaschine) möglich

### 4. Board-Einstellungen
- **Funktion**: Darstellung und Freigaben des aktuellen Boards
- **Details**:
  - Reiter **Layout**: Spalten, Abstände, Standardgrößen, zurücksetzen
  - Reiter **Aussehen**: Hintergrundbild, Farbton, Deckkraft, Blur, Icon-Stil
  - Reiter **Freigabe**: öffentlich, nur eigene, Personen/Gruppen

### 5. Konto-Menü (Icon rechts oben)
- **Funktion**: persönliches Profil und Abmeldung
- **Details**:
  - Profil, Anzeigename, Sprache, Zeitzone
  - Farbschema: hell, dunkel, Systemeinstellung
  - Standard-Suchmaschine, Startboard
  - Zwei-Faktor-Einstellungen (sofern vom Anbieter freigeschaltet)
  - Abmelden

### 6. Instanz-Verwaltung (nur Administratoren)
- **Funktion**: die gesamte Instanz einrichten
- **Details**:
  - **Nutzer**: anlegen, einladen, Rolle setzen, deaktivieren, Profilbild
  - **Gruppen**: Boards Gruppen zuweisen, Freigaben bündeln
  - **Integrationen**: Dienste anlegen, Schlüssel pflegen, Verbindung testen, Root-Zertifikate
  - **Auth**: OIDC-Anbieter konfigurieren (Issuer, Client-ID, Secret, Scopes), Header-Auth, Sitzungszeit
  - **Lizenz**: Subscription-Status, Instanz-ID, Updates
  - **Design-Editor**: globale Themes und Icon-Sets
  - **System**: Protokoll/Ereignisliste, Backups anstoßen, Wiederherstellen

### 7. Hilfe und Support
- **Funktion**: Dokumentation, Versionsstand, Support-Ticket
- **Details**:
  - Versions- und Build-Nummer (wichtig für Supportanfragen)
  - Statusseite des Cloud-Dienstes (nur Cloud-Variante)

## Kontext-Menüs

### Klick auf ein Widget (Ansichtsmodus)
- App-Kachel öffnet die Ziel-URL im eingestellten Rahmen
- Integrations-Widgets bieten eigene Aktionen, zum Beispiel:
  - Container: anhalten, starten, neu starten, Protokoll ansehen
  - Requests: genehmigen oder ablehnen
  - Downloads: pausieren, fortsetzen
- Nicht unterstützte Kacheln haben keine Aktion

### Rechtsklick auf ein Widget
- **Einstellungen** der Kachel (nur mit Bearbeitungsrecht)
- **Duplizieren** der Kachel
- **Entfernen** aus dem Board
- **In neuem Tab öffnen**

### Schwebende Werkzeugleiste (Bearbeitungsmodus)
- **Bearbeiten**: Einstellungsdialog der Kachel öffnen
- **Entfernen**: Kachel aus dem Board nehmen
- **Duplizieren**: Kachel mit identischen Einstellungen anlegen
- **Ziehen**: Greifpunkt oben links zum Verschieben, Ecke unten rechts zum Skalieren
- **Ausrichten**: Hilfslinien und „am Raster ausrichten“

### Widget-Einstellungsdialog
- **Funktion**: Inhalt, Datenquelle und Aussehen einer Kachel festlegen
- **Details**:
  - Bereiche: **Allgemein** (Titel, Icon, Farbe), **Datenquelle** (Integration, Endpunkt, Felder), **Anzeige** (Einträge, Intervall, Sortierung), **Aktionen** (Ziel, Klickverhalten)
  - Fußzeile: Abbrechen, Testen (bei Datenquellen), Speichern, Entfernen

### Integrations-Dialog
- **Funktion**: Dienst anlegen oder ändern
- **Details**: Typ-Auswahl, interne und externe URL, Zugangsdaten, Test-Knopf mit Fehlerbeschreibung, Zertifikatsoptionen

## Menüs nach Benutzerrolle

### Administrator
- Volle Boardsicht und alle Bearbeiten-Funktionen
- Nutzer, Gruppen, Integrationen, Auth-/OIDC-Einstellungen, Design-Editor
- Lizenz- und Systembereich, Protokoll, Backups
- Eigene Root-Zertifikate verwalten

### Editor
- Eigene Boards anlegen und alle freigegebenen Boards bearbeiten
- Integrationen auswählen, aber keine Instanzeinstellungen öffnen
- Persönliche Einstellungen, Farbschema, Startboard

### Betrachter
- Nur freigegebene Boards in Leseansicht
- Keine Bearbeiten-Schaltfläche, kein Rechtsklick-Werkzeug (höchstens „In neuem Tab öffnen“)
- Eigene Darstellung und Abmeldung

### Eingeladener Nutzer (noch ohne Konto)
- Einladungslink mit Ablaufdatum
- Registrierung bzw. OIDC-Anmeldung, danach Rolle gemäß Einladung

## Shortcuts

Die verfügbaren Tasten für Editor und Navigation stehen in [shortcuts.md](shortcuts.md); verbreitet erwartete Kombinationen sind dort als nicht vorhanden gekennzeichnet.
