# Homarr - Menüpunkte

## Übersicht

Homarr hat kein klassisches Anwendungs-Menü, sondern eine schlanke Kopfzeile, ein Bearbeiten-Werkzeug für Boards sowie Einstellungsdialoge für Board, Instanz und Konto. Welche Punkte sichtbar sind, hängt von der Rolle (Administrator, Mitglied, Gast) und vom Board-Status ab.

## Hauptmenüpunkte (Kopfzeile)

### 1. Board-Wechsler (links)
- **Funktion**: Zwischen den Boards wechseln, die der Nutzer sehen darf
- **Details**:
  - Dropdown mit allen freigegebenen Boards
  - Start-Board für Desktop und Mobil getrennt einstellbar
  - Administrator kann hier auch neue Boards anlegen

### 2. Suchleiste (Mitte)
- **Funktion**: Apps/Links der Boards und Websuche finden
- **Details**:
  - Autocomplete mit Treffern aus den Board-Inhalten
  - Websuche mit einstellbarer Suchmaschine
  - Kurzkommandos (Bangs) im Suchtext möglich

### 3. Bearbeiten-Modus (rechts)
- **Funktion**: Board-Inhalte ändern: Widgets hinzufügen, verschieben, größen, löschen
- **Details**:
  - Nur für Board-Berechtigte sichtbar
  - Im Bearbeitungsmodus erscheint eine Auswahl der verfügbaren Widgets
  - Änderungen werden sofort gespeichert

### 4. Board-Einstellungen
- **Funktion**: Darstellung des aktuellen Boards anpassen
- **Details**:
  - Raster: Spaltenanzahl, Abstände, Standardgrößen
  - Aussehen: Hintergrundbild, Farbton, Transparenz/Blur
  - Icon-Darstellung und Beschriftungen
  - Sichtbarkeit des Boards und Freigaben

### 5. Benutzermenü (Icon rechts oben)
- **Funktion**: Konto, Darstellung und Abmeldung
- **Details**:
  - Profil und persönliche Einstellungen
  - Farbschema: hell, dunkel, Systemeinstellung
  - Kopfzeilen-Optionen, Suchpräferenzen, erster Wochentag
  - Verhalten des Rechtsklicks auf Widgets
  - Abmelden

### 6. Instanzeinstellungen (nur Administratoren)
- **Funktion**: Die gesamte Homarr-Instanz verwalten
- **Details**:
  - **Nutzer**: anlegen, bearbeiten, löschen, Rolle setzen, Profilbild
  - **Einladungen**: erzeugen, auflisten, widerrufen
  - **Integrationen**: Dienste anlegen, Schlüssel pflegen, Verbindung testen
  - **Boards**: globale Board-Vorgaben, Standard-Raster
  - **Zertifikate**: eigene Root-Zertifikate hinterlegen, um interne HTTPS-Dienste zu erreichen

## Kontext-Menüs im Board

### Widget-Klick (normales Board)
- App-Kachel öffnet die Ziel-URL im eingestellten Zielrahmen
- Integrations-Widgets bieten eigene Aktionen, zum Beispiel:
  - Container: anhalten, starten, neu starten, Log öffnen
  - Requests: genehmigen oder ablehnen
  - Kalender: Termindetails, Termin im Kalender öffnen

### Widget-Rechtsklick
- **Funktion**: Direktzugriff auf Kachel-Aktionen
- **Details**:
  - Einstellungen der Kachel (nur mit Bearbeitungsrecht)
  - Kachel entfernen oder duplizieren
  - Link in neuem Tab öffnen
  - **Hinweis**: Das Rechtsklick-Menü ist eine persönliche Einstellung und kann abgeschaltet sein

### Schwebende Symbolleiste (Bearbeitungsmodus)
- **Funktion**: Zugriff auf Kachel-Werkzeuge beim Überfahren
- **Details**:
  - **Bearbeiten**: Widget-Einstellungsdialog öffnen
  - **Entfernen**: Kachel aus dem Board nehmen
  - **Ziehen**: linke obere Ecke zum Verschieben nutzen
  - **Ecke ziehen**: Größe ändern (Raster-Rasterung, Einrasten an Spalten)

### Widget-Einstellungsdialog
- **Funktion**: Inhalt und Aussehen einer Kachel festlegen
- **Details**:
  - Titel, Icon, Farbe, Ziel-URL
  - Zugehörige Integration auswählen
  - Anzeigeparameter (Einträge, Intervall, Sortierung)
  - Abbrechen, Speichern, Löschen

## Menüs nach Rolle

### Administrator
- Volle Board-Rechte, alle Boards sichtbar und editierbar
- Nutzer, Einladungen, Integrationen, globale Board-Einstellungen
- Eigene Root-Zertifikate verwalten
- Instanz-Informationen (Version, Serverinformationen) einsehen

### Mitglied
- Eigene Boards anlegen und bearbeiten
- Freigegebene Boards ansehen, bei Bearbeitungsrecht auch ändern
- Integrationen auswählen, aber keine Instanz-Einstellungen öffnen
- Persönliche Einstellungen und Farbschema

### Gast / nicht zugewiesener Nutzer
- Nur öffentlich freigegebene Boards
- Keine Bearbeiten-Schaltfläche, keine Integrationsverwaltung
- Eigene Darstellung (Farbschema) und Abmelden

## Einstellungs-Dialoge (Struktur)

| Dialog | Bereiche | Typische Felder |
|--------|----------|-----------------|
| Widget-Einstellungen | Inhalt, Darstellung, Integration | Titel, URL, Icon, Intervall |
| Board-Einstellungen | Raster, Aussehen, Freigaben | Spalten, Hintergrund, Sichtbarkeit |
| Integration | Typ, Verbindung, Schlüssel | URL, API-Key, Verbindungstest |
| Nutzer | Konto, Rolle, Rechte | Name, Rolle, Board-Freigaben |
| Instanz | Allgemein, Zertifikate | Registrierung, Root-Zertifikat |

## Shortcuts

Die vorhandene Tastatursteuerung (Dialoge, Drag & Drop, Fokussierung) ist in [shortcuts.md](shortcuts.md) beschrieben, inklusive der klar als nicht vorhanden markierten Tasten.
