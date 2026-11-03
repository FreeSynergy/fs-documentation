# Heimdall - Menüpunkte

## Übersicht

Heimdall arbeitet mit einer Startseite aus Panels und einer abgetrennten Verwaltungsansicht (Einstellungen). Was sichtbar ist, hängt davon ab, ob angemeldet ist, welche Rolle das Konto hat und ob mehrere Nutzer aktiviert sind.

## Hauptmenüpunkte

### 1. Dashboard (Startseite)
- **Funktion**: zentrale Ansicht aller Panels mit App-Kacheln, Statistik und Suchfeld
- **Details**:
  - Panels untereinander, innerhalb der Panels die Kacheln
  - Inhalt entsteht aus den gespeicherten Apps und Panels des Kontos
  - Klick auf eine Kachel öffnet die Ziel-URL im eingestellten Zielrahmen

### 2. Apps verwalten
- **Funktion**: Kacheln anlegen, ändern und entfernen
- **Details**:
  - **App hinzufügen**: Titel, URL, Icon, Farbe, „in neuem Tab öffnen“
  - **Icon wählen**: Upload, Icon-Liste oder automatische Übernahme des Favicon
  - **Enhanced App wählen**: Dienst auswählen, danach Ziel-URL und Schlüssel eintragen
  - **Bearbeiten/Löschen** bestehender Apps, meist über ein Bearbeitungs-Symbol an der Kachel

### 3. Layout bearbeiten (Panels)
- **Funktion**: Panels verschieben, umbrechen, ausblenden, löschen
- **Details**:
  - eigener Bearbeitungsmodus über die Einstellungen
  - Panels per Drag & Drop anordnen, Kacheln innerhalb des Panels sortieren
  - ausgeblendete Panels wieder einblenden
  - Änderungen werden pro Konto gespeichert

### 4. Suchpanel
- **Funktion**: Suchbegriff an eine Suchmaschine übergeben
- **Details**:
  - Suchfeld auf der Startseite
  - Anbieter einstellbar (Standard: Google, weitere Anbieter zur Auswahl)
  - kein interner Suchindex über alle Apps

### 5. Einstellungen (Zahnrad)
- **Funktion**: Konto und Anwendung konfigurieren
- **Details**:
  - **Konto**: E-Mail-Adresse, Passwort ändern
  - **Benutzer** (neuere Versionen): Nutzer anlegen, Rolle setzen, löschen
  - **Layout**: Panels zurücksetzen, Ansicht neu anordnen
  - **Anpassung**: eigene Stylesheets, Logo/Titel (versionsabhängig)
  - **Support/Hinweise**: Meldungen des Projekts ein- oder ausblenden
  - **Update-Informationen**: Hinweis auf verfügbare neue Versionen

### 6. Statistik-Bereiche
- **Funktion**: CPU, Arbeitsspeicher, Festplatte und Netzwerk des Servers anzeigen
- **Details**:
  - Werte stammen vom Heimdall-Rechner
  - Anzeige als Zahl mit kleinem Diagramm
  - Bereich lässt sich ausblenden, wenn keine Statistiken gewünscht sind

### 7. Konto-Menü (oben rechts)
- **Funktion**: Konto wechseln oder abmelden
- **Details**:
  - Angemeldetes Konto, Abmelden
  - Bei deaktivierter Anmeldung entfällt dieser Punkt vollständig

## Kontext-Menüs an Panels und Kacheln

### App-Kachel (normaler Modus)
- **Linksklick**: Ziel öffnen
- **Symbolleiste beim Überfahren** (je nach Version):
  - Bearbeiten (Titel, URL, Icon, Farbe)
  - Löschen
  - In neuem Tab öffnen (alternativ über die App-Einstellung)

### App-Kachel (Layout-Bearbeitung)
- **Ziehen**: Kachel innerhalb des Panels verschieben, Einrasten am Raster
- **Panel wechseln**: Kachel in ein anderes Panel ziehen
- **Bearbeiten**: Dialog mit allen Feldern der App
- **Enhanced-App-Dialog**: Dienst, Ziel-URL, API-Key oder Benutzername/Passwort

### Panel-Werkzeuge
- **Funktion**: Bereich als Ganzes bearbeiten
- **Details**:
  - Verschieben (Griffzone am Panel-Rand)
  - Umbrechen in zwei Bereiche oder zusammenführen
  - Ausblenden und Wiederherstellen
  - Löschen (mit Sicherheitsabfrage)

### Icon-Auswahl-Dialog
- **Funktion**: Bildquelle für eine Kachel festlegen
- **Details**:
  - Datei hochladen (PNG/SVG/JPG)
  - Vorhandene Icons durchsuchen
  - Automatische Icon-Erkennung über die Ziel-URL
  - Übernehmen und Abbrechen

## Menüs nach Rolle

### Administrator
- Alle Menüpunkte inklusive Benutzerverwaltung
- Apps anlegen und löschen, Enhanced Apps einrichten und Schlüssel pflegen
- Layout bearbeiten, Panels zurücksetzen
- Systemeinstellungen und Update-Hinweise

### Angemeldeter Nutzer (Standardkonto)
- Dashboard mit eigenen Layout
- Apps je nach Version nur ansehen oder selbst bearbeiten
- Suchfeld und Statistik-Bereiche
- Konto: Passwort und eigenes Layout

### Öffentlich / ohne Anmeldung
- Nur das freigegebene Dashboard (falls für öffentliche Nutzung eingerichtet)
- Keine Einstellungs- und Verwaltungspunkte
- Apps sind nur lesbar; Reihenfolge entspricht dem gespeicherten Layout

### Betrieb ohne Login
- Wenn die Anmeldung abgeschaltet ist, erscheint die Verwaltung direkt für jeden, der die Seite erreicht
- **Sicherheitshinweis**: dann muss der Zugriff über Reverse Proxy, Netzwerk oder VPN geschützt werden

## Shortcuts

Heimdall bietet keine anwendungseigenen Shortcuts; die nutzbaren Tasten und Gesten stehen in [shortcuts.md](shortcuts.md).
