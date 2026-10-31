# Planka - Menüpunkte

## Übersicht

Planka navigiert über eine linke Seitenleiste mit Projekten und Boards, einen Board-Kopf mit Mitglieds-/Aktionsbereich und Karten-Dialoge als Overlay. Fast alle Kontext-Menüs sind Aufklapp-Menüs mit kleinen Symbolleisten; Admins und Projekt-Manager sehen zusätzliche Verwaltungspunkte.

## Hauptmenüpunkte

### 1. Projekt-Sidebar (links)
- **Funktion**: Projekt- und Board-Auswahl
- **Details**:
  - Projektliste mit Suchen/Schnellauswahl (bei vielen Projekten)
  - Boards je Projekt als Reiter/Unterpunkte
  - Projekt anlegen (Symbol), Projekt bearbeiten/löschen im Projekt-Kontextmenü
  - Sidebar einklappbar (Pfeil-Symbol), Breite je Version fix

### 2. Projekt-Kontextmenü
- **Funktion**: Projekte verwalten
- **Details**:
  - Projekt bearbeiten (Name, Hintergrund)
  - Projekt-Manager verwalten (wer darf verwalten)
  - Mitglieder einladen/hinzufügen
  - Projekt löschen (Archivieren existiert für Boards, nicht für Projekte - versionsabhängig)

### 3. Board-Kopf (oben im Board)
- **Funktion**: Board-Aktionen
- **Details**:
  - Mitglieder-Avatare: Board-Mitglieder verwalten
  - Benachrichtigungs-/Beobachten-Schalter je Board
  - Board-Suchen/Filter (Label-/Mitglieder-Filter, versionsabhängig)
  - Board-Menü (drei Punkte): Board bearbeiten, Hintergrund ändern,karten archivieren, Board löschen

### 4. Karten-Dialog (Overlay)
- **Funktion**: Karte im Detail öffnen (Klick auf Karte)
- **Details**:
  - Titel und Beschreibung (Markdown-Editor)
  - Seitenleiste der Karte: Zugewiesene, Labels, Fälligkeit, Checkliste, Anhänge, Beobachten, Duplizieren, Archivieren, Löschen, Karten-ID/Moves-Info
  - Kommentarfeld und Aktivitätenstrom (Bearbeitungschronik)

### 5. Karten-Kontextmenü (in der Liste)
- **Funktion**: Schnellaktionen ohne Dialog
- **Details**:
  - Bearbeiten, Duplizieren, Verschieben (Liste/Board), Zuweisen, Label setzen
  - Fälligkeit setzen, Archivieren, Löschen

### 6. Benutzermenü (unten links)
- **Funktion**: eigenes Konto und Darstellung
- **Details**:
  - Profil: Name, Avatar, E-Mail ändern
  - Passwort ändern
  - Benachrichtigungs-Einstellungen
  - Darstellung: heller/dunkler Modus (Community: Umschalten; weitere Themes: Pro)
  - Sprache (Internationalisierung), Abmelden

### 7. Administrations-Bereich
- **Funktion**: Instanzverwaltung (Admin-Rolle)
- **Details**:
  - Benutzer anlegen/bearbeiten/löschen, Administratorrolle vergeben
  - API-Schlüssel je Benutzer verwalten
  - Initiale Admin-Anlage über Umgebungsvariablen bei Erststart (versionsabhängig)

## Kontext-Menüs

### Listen-Menü (drei Punkte je Spalte)
- Liste bearbeiten (Titel), Karten hinzufügen
- Nach rechts/links verschieben
- Karten archivieren, Liste leeren, Liste löschen

### Label-Verwaltung
- Label erstellen (Farbe, Name), bearbeiten, aus Board löschen
- Label auf Karten: Klick auf Labels-Leiste im Karten-Dialog

### Anhang-Menü
- Datei per Drag & Drop oder Picker anhängen
- Anhang im Menü: Umbenennen (Titel), Betrachter/Download, Löschen

## Menüs nach Benutzerrolle

### Administrator
- Benutzer- und Instanzverwaltung (Benutzer, Rollen, API-Schlüssel)
- Alle Projekt- und Board-Menüs, Löschen/Archivieren überall
- Webhook-Verwaltung (Community; Zugang via API/Admin-Oberfläche, versionsabhängig)

### Projekt-Manager / Bearbeiter
- Projekte/Boards/Listen/Karten anlegen und bearbeiten
- Mitglieder und Labels verwalten, Anhänge, Kommentare
- Keine Instanzverwaltung, keine fremden Profile

### Einfaches Mitglied (Leser-nah)
- Karten lesen, kommentieren, beobachten
- Karten verschieben/bearbeiten nur wenn im Board Mitglied und Board nicht schreibgeschützt (feingranante Lese-/Schreibrollen erst Pro-Gastrollen, versionsabhängig)

## Hinweise

- Beschriftungen folgen der gewählten Oberflächensprache (Deutsch vorhanden)
- Pro-Funktionen (Gastrollen, Timeline-Menüpunkt) erscheinen nur mit Lizenz
- Planka blendet Verwaltungsaktionen aus, statt sie zu deaktivieren - Rollenunterschiede sind deshalb vor allem „Menü sichtbar/nicht sichtbar"
