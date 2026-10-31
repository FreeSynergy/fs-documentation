# Nextcloud Calendar - Menüpunkte

## Übersicht

Nextcloud Calendar hat keine klassische Menüleiste. Bedient wird über die Nextcloud-Kopfzeile (App-Wechsel, Benutzermenü), eine linke Kalender-Seitenleiste mit Plus-Menü, eine Werkzeugleiste für die Zeitansichten sowie Dialoge für Ereignis, Freigabe und Einstellungen. Welche Punkte sichtbar sind, hängt von der Rolle ab (Administrator, angemeldeter Nutzer, Empfänger eines öffentlichen Links, extern eingeladene Person).

## Hauptmenüpunkte (Kopfzeile und Werkzeugleiste)

### 1. App-Starter (Symbol oben links)
- **Funktion**: Wechsel zwischen den Nextcloud-Apps (Dateien, Kalender, Kontakte, Talk, Mail, Aufgaben u. a.)
- **Details**:
  - Raster-Symbol öffnet die App-Liste, angepinnte Apps stehen in der Kopfzeile
  - Nextcloud-Suche (Kopfzeile) findet auch Termine, sofern „Suche auf dem Server" aktiviert ist

### 2. Plus-Menü „Neu" (Seitenleiste)
- **Funktion**: Objekte anlegen
- **Details**:
  - **Neues Ereignis**: Termin mit Titel, Datum, Ort, Teilnehmern
  - **Neuer Kalender**: eigener Kalender mit Farbe
  - **Neue Kalendergruppe**: mehrere Kalender gemeinsam sortieren
  - **Neue Verfügbarkeit / Umfrage („Zeiten finden")**: Slot-Umfrage für Terminfindung
  - **Abwesenheit** anlegen (neuere Versionen, (nicht dokumentiert, ob immer sichtbar))

### 3. Ansichts-Umschalter (Werkzeugleiste)
- **Funktion**: Zeitdarstellung wählen
- **Details**:
  - Tag, Woche, Arbeitswoche, Monat, Agenda (Terminliste)
  - Zurück / Heute / Weiter und Datumseingabe zum Springen
  - Standardansicht in den persönlichen Einstellungen festlegbar

### 4. „Einstellungen und Filter" (rechts in der Werkzeugleiste)
- **Funktion**: Anzeige und Suche steuern
- **Details**:
  - Suche im Kalender (clientseitig oder „Suche auf dem Server")
  - Geburtstagskalender und Feiertagskalender ein-/ausblenden
  - Ereignisse nach Typ filtern, Seitenleiste ein-/ausklappen
  - „Kalenderliste initial einklappen"

### 5. Kalender-Seitenleiste (links)
- **Funktion**: Kalender sichtbar schalten, verwalten, teilen
- **Details**:
  - Checkbox pro Kalender blendet ein/aus, Farbpunkt setzt die Farbe
  - Symbolsymbole am Eintrag: **Teilen** (Personen/Symbole), **Bearbeiten** (Kalendereinstellungen), **Mehr** (Herunterladen als ICS, Löschen)
  - Gruppenkalender (Teamkalender je Nextcloud-Gruppe) mit eigenem Symbol, Abos mit Globus-Symbol und Aktualisieren-Knopf
  - Geburtstags- und Feiertagskalender erscheinen automatisch (ausblendbar)

### 6. Benutzermenü (oben rechts)
- **Funktion**: Konto, Darstellung, Abmeldung
- **Details**:
  - **Einstellungen** → Abschnitt „Kalender": Wochenanfang, Zeitzone, Standardansicht
  - Darstellung (hell/dunkel/System) und Sprache gelten instanzweit
  - Für Administratoren zusätzlich: Verwaltungsmenü (Nutzer, Apps, Server)

## Kontext- und Klick-Menüs

### Klick auf einen freien Slot (Tages-/Wochenansicht)
- Öffnet den Ereignis-Editor mit vorausgefüllter Uhrzeit
- Aufziehen über mehrere Slots erstellt den Termin direkt in dieser Zeitspanne (Drag & Drop)

### Klick auf ein Ereignis
- Öffnet den Ereignis-Editor: Details, Teilnehmer (mit Zu-/Absage-Status), Erinnerungen, Anhänge, Kommentare, Talk-Link
- Für Eingeladene erscheint **Antworten** (Annehmen / Vorläufig / Ablehnen)

### Rechtsklick
- Nextcloud Calendar bietet **kein dokumentiertes Rechtsklick-Menü** in der Rasteransicht
- Aktionen (Teilen, Umbenennen, Löschen, Export) liegen an den Kalender-Einträgen der Seitenleiste bzw. im Dialog

## Wichtige Dialoge

### Ereignis-Editor
- Titel, Zeitbereich, ganztägig, Zeitzone, Wiederholung (RRULE), Erinnerungen (Popup/E-Mail)
- Kalender-Auswahl, Privat-/Geschäftsstatus (Termin/busy), Ort, Notiz
- Teilnehmer: Nextcloud-Nutzer, Gruppen, Kreise (Circles), E-Mail-Adressen; Raum-/Ressourcenbuchung
- Reiter für Anhänge und Kommentare, Talk-Besprechung verknüpfen

### Freigabe-Dialog (Teilen)
- Empfänger: Benutzer, Gruppen, Kreise
- Berechtigungsstufen: **nur Verfügbarkeiten**, **kann anzeigen**, **kann bearbeiten**
- Öffentlicher Link: Kalender als Abo-Link, optional Passwort (je nach Serverkonfiguration)

### Kalendereinstellungen
- Name, Farbe, Beschreibung, Zeitzone des Kalenders, Herunterladen (ICS), Löschen

## Menüs nach Rolle

### Administrator
- Keine eigenen Kalender-Menüs: Kalender ist pro Nutzer dieselbe Oberfläche
- Rechnerweite Aufgaben in der Nextcloud-Verwaltung: Apps aktivieren/aktualisieren, Nutzerverwaltung, DAV- und Gruppenkalender-Einstellungen (config.php), Speicher- und Berechtigungs-App
- Einsicht in **fremde Kalender ist bewusst nicht vorgesehen** (Datenschutz)

### Angemeldeter Nutzer
- Volle Funktionen: eigene Kalender, Veranstaltungen, Umfragen, Freigaben, Abos
- Gruppenkalender der eigenen Gruppen automatisch sichtbar (nur mit Bearbeitungsrecht änderbar)

### Empfänger öffentlicher Links / Gast
- Öffentlich geteilter Kalender im Browser ohne eigene Anmeldung (schreibgeschützt)
- Keine Seitenleisten-Verwaltung, keine Freigaben

### Extern eingeladene Person (ohne Konto)
- Erhält E-Mail mit ICS-Einladung; Annehmen/Ablehnen über den Mail-Client oder Nextcloud-Link

## Shortcuts

Die vorhandene Tastatursteuerung (Dialoge, Formulare, Browser-Tasten) ist in [shortcuts.md](shortcuts.md) beschrieben - inklusive der klar als nicht dokumentiert markierten Tasten.
