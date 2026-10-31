# Synology DSM - Menüpunkte

## Übersicht

DSM arbeitet wie ein Desktop: eine **obere Leiste** mit Hauptmenü, Suche und Konto, eine **App-Leiste** am unteren Rand, **Fenster** für jede Anwendung und **Desktop-Widgets** für den Systemzustand. Welche Punkte sichtbar sind, hängt von Rolle und Paketrechten ab – Administratoren sehen Systemsteuerung und Paketzentrum, Standardbenutzer nur die Pakete, für die sie freigeschaltet sind.

## Hauptmenüpunkte

### 1. Hauptmenü (Symbol oben links)
- **Funktion**: zentrale Auflistung aller installierten Pakete und Systemfunktionen
- **Details**:
  - Raster aus Symbolen, Suchfeld im Menü, Kategorien
  - „Anpinnen" überträgt ein Programm in die App-Leiste
  - **Alle Programme / Bearbeiten**: Reihenfolge ändern, Einträge ablegen
  - Sichtbarkeit folgt den Paket-Rechten der Gruppe bzw. des Kontos

### 2. App-Leiste (unten)
- **Funktion**: Startpunkte und offene Fenster
- **Details**:
  - Angepinnte Anwendungen mit Rechtsklick-Menü (öffnen, abheften, Fensterliste)
  - Laufende Fenster zeigen Indikator und Titelvorschau
  - Leiste kann ausgeblendet und automatisch versteckt werden

### 3. Desktop-Widgets / System Pulse
- **Funktion**: Live-Systemzustand auf der Desktop-Fläche
- **Details**:
  - Kacheln für CPU-, Arbeitsspeicher- und Netzwerkauslastung
  - Volume- und Storage-Gesundheit, Laufwerksstatus, Temperatur
  - Benachrichtigungs- und Aufgabenkachel, Uhr/Datum (Umfang je DSM-Version)

### 4. Suche oben (Universal Search)
- **Funktion**: indexierte Suche über Freigaben, Pakete und Einstellungen
- **Details**:
  - Ergebnisse nach Typ gruppiert (Dateien, Ordner, Pakete, Systemsteuerungsoptionen)
  - Filter nach Freigegebenem Ordner, Typ, Datum
  - Direktaktionen: öffnen, herunterladen, Pfad kopieren

### 5. Benachrichtigungen (Glocke oben rechts)
- **Funktion**: System-, Speicher- und Paketereignisse
- **Details**:
  - Ungelesene Meldungen, Kategorien, Zeitleiste
  - Einstellungen für E-Mail-/Push-Benachrichtigung

### 6. Konto-Menü (Avatar oben rechts)
- **Funktion**: persönliches Profil und Abmeldung
- **Details**:
  - **Abmelden**, **Fenster schließen**
  - **Persönliche Informationen**: Kennwort ändern, 2FA einrichten, E-Mail, Sprache, Themenwahl
  - **Desktop-Einstellungen**: Hintergrund, Symbolgröße, Widget-Sichtbarkeit

### 7. Systemsteuerung (nur mit Recht)
- **Funktion**: zentrale Verwaltung des Systems
- **Details**:
  - **Benutzer und Gruppen**: Konten, Gruppen, Paketrechte, Kontingente, Domäne/LDAP
  - **Freigegebener Ordner**: anlegen, Rechte, Verschlüsselung, Papierkorb
  - **Dateidienste**: SMB, NFS, AFP, FTP, WebDAV, rsync
  - **Aufgabenplanung**: Zeitpläne, Skripte, ereignisgesteuerte Aufgaben

### 8. Paketzentrum
- **Funktion**: Pakete installieren, aktualisieren, starten, entfernen
- **Details**:
  - **Empfohlen / Kategorien / Suchen**, Paketdetails und Versionshinweise
  - **Installiert**: Updates, Autostart, Ressourcen, Deinstallation
  - **Manuelle Installation** einer `.spk`-Datei
  - **Einstellungen**: automatische Updates, zusätzliche Paketquellen, Testkanal

### 9. Speicher-Verwaltung
- **Funktion**: Storage-Pools, Volumes, Laufwerke, Cache
- **Details**:
  - Konsolenansicht mit Warnungen, Pool- und Volume-Listen, Laufwerksdetails
  - SMART-Tests, Storage-Analyse, Laufwerks-Signalton
  - Volume erweitern, Storage-Pool hinzufügen, Cache einrichten
  - **Volume-/Snapshot-Informationen** je Btrfs-Volume

### 10. Schnellstart (QuickStart)
- **Funktion**: geführte Einrichtung und Aufgaben-Anleitungen
- **Details**:
  - Themenblöcke „Ersteinrichtung“, „Fernzugriff“, „Sicherung“, „Medien“
  - Verlinkung auf Assistenten (Freigabe anlegen, QuickConnect aktivieren, Zertifikat beziehen)

## Kontext-Menüs

### Desktop-Rechtsklick
- **Widgets hinzufügen/entfernen**, Desktop-Aktualisierung
- **Alle Fenster schließen / minimieren**

### Fenster-Titelleiste
- **Minimieren**, **Wiederherstellen/Maximieren**, **Schließen**
- **Vollbild** bei bestimmten Paketen

### File Station
- **Rechtsklick auf Datei/Ordner**: öffnen, herunterladen, herunterladen als ZIP, kopieren, verschieben, umbenennen, löschen, freigeben, Eigenschaften, komprimieren, entpacken
- **Rechtsklick auf freien Bereich**: neuer Ordner, Hochladen, Aufgaben, Ansicht
- **Freigabelink** mit Ablaufdatum, Passwort und Berechtigung

## Menüs nach Benutzerrolle

### Administrator (Gruppe `administrators`)
- Systemsteuerung, Paketzentrum, Speicher-Verwaltung, Protokoll-Center, Ressourcenmonitor
- Benutzer und Gruppen, Paketrechte, Firewall, Dienste, Update-Einstellungen
- Alle Freigegebenen Ordner, Systemeinstellungen, Konfigurations-Wiederherstellung

### Standardbenutzer
- Nur Pakete mit zugewiesenem Recht (z. B. Drive, File Station, Media Server)
- **Keine** Systemsteuerung, kein Paketzentrum, keine Speicher-Verwaltung
- Eigene Kontoeinstellungen: Kennwort, 2FA, Sprache, Desktop-Hintergrund
- Zugriff auf Freigaben gemäß ACL

### Benutzer mit eingeschränkten Rechten
- File Station nur auf erlaubte Freigaben, ohne Umbenennen/Löschen (je ACL)
- Keine Admin-Werkzeuge, keine Systemprotokolle
- Paket-Weboberflächen erscheinen nur, wenn die Gruppe dort freigeschaltet ist

### Gast / Anwendungskonto
- Gast: eingeschränkter Web-Zugriff, keine Verwaltung, keine persönlichen Einstellungen
- Anwendungskonto (Gruppe `applications`): API-/Skriptzugang, meist ohne Desktop-Portal-Rechte, aber mit API-Berechtigung

## Shortcuts

Tastatursteuerung im Portal ist begrenzt; die vollständige Liste inklusive als fehlend markierter Kombinationen steht in [shortcuts.md](shortcuts.md).
