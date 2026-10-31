# Outlook Kalender - Menüpunkte

## Übersicht

Outlook Kalender hat kein klassisches Dateimenü, sondern eine schmale App-Startleiste, eine Befehlsleiste über dem Kalenderblatt, eine Kalenderliste links und Einstellungsdialoge über das Zahnrad. Welche Punkte sichtbar sind, hängt vom Client (Outlook im Web, neues Outlook für Windows, Outlook Classic, Outlook für Mac, Outlook Mobile), von der Lizenz und von den Freigabestufen des Kalenders ab.

## Hauptmenüpunkte

### 1. App-Startleiste (linker Rand)
- **Funktion**: Wechsel zwischen den Outlook-Modulen
- **Details**:
  - **Post** (E-Mail), **Kalender**, **Personen** (Kontakte), **To Do** (Aufgaben)
  - **Weitere Apps**: Teams, Bookings, Forms und andere M365-Anwendungen
  - In kompakten Fenstern und mobil zur unteren Symbolleiste reduziert

### 2. Kalenderliste (links)
- **Funktion**: Kalendernavigation und Überlagerung mehrerer Kalender
- **Details**:
  - **Meine Kalender**: Standardkalender, Nebenkalender, Kalendergruppen, Geburtstagskalender
  - **Hinzufügen**: Neuer Kalender, Neue Kalendergruppe, Aus dem Adressbuch (freigegebener Kalender), Empfohlene Kalender, Feiertage, Abonnement (Feed), Importieren (ICS-Datei)
  - **Freigegebene Kalender**: von anderen Personen geteilte Kalender
  - Farbpunkte und Kategorien pro Kalender, Häkchen schaltet die Anzeige im Kalenderblatt
  - Beschriftung: Bearbeiten, Teilen, Berechtigungen, Aus Liste entfernen, Löschen

### 3. Befehlsleiste (über dem Kalenderblatt)
- **Funktion**: wichtigste Kalenderaktionen
- **Details** (Bezeichnung variiert je nach Client):
  - **Neues Ereignis / Neuer Termin**: Termin anlegen (Eintrag ohne Teilnehmer)
  - **Ansicht**: Tag, Arbeitswoche, Woche, Monat, Terminübersicht (Agenda), Jahr
  - **Heute**: zum aktuellen Datum springen
  - **Filter**: nach Kategorien, Besprechungstyp oder Teilnahmen filtern
  - **Suchen**: Volltextsuche über Termine und Besprechungsanfragen
  - **Kalender drucken**: Drucklayout (Tag, Woche, Monat, Termindetail)
  - **Kalender teilen / Freigabe**: Person und Berechtigungsstufe festlegen

### 4. Ereignis- bzw. Terminformular
- **Funktion**: Termin anlegen oder bearbeiten
- **Details**:
  - Titel, Ort, Beginn/Ende, Ganztägig, Zeitzone
  - **Teilnehmer**: erforderlich, optional, Ressourcen (Raum, Equipment)
  - **Planungsassistent**: freie Zeiten der Teilnehmer und Räume in einer Wochenansicht
  - **Onlinebesprechung**: Teams-Besprechung hinzufügen
  - **Kategorie/Farbe**, **Erinnerung**, **Anzeigen als** (Free/Busy, Abwesend, Out of Office)
  - **Wiederholung** (täglich, wöchentlich, monatlich, jährlich, benutzerdefiniert)
  - **Anlagen**, **Richtlinien/Terminsache**, **Antwortstatus-Verfolgung**

### 5. Teilen-Dialog (Freigabe)
- **Funktion**: Kalender für Personen im Mandant freigeben
- **Details**:
  - Berechtigungsstufen: Verfügbarkeit (nur Free/Busy), Titel und Ort, Details anzeigen (Reviewer), bearbeiten (Author/Editor), Vollzugriff (Owner)
  - Freigabe an Verteilergruppen und an Ressourcenpostfächer
  - Öffentliche Verlinkung eines Kalenders ist in aktuellen Versionen nicht mehr vorgesehen (ältere „Im Web veröffentlichen"-Funktion wurde eingestellt; Stand: nicht dokumentiert)

### 6. Benutzermenü (rechts oben)
- **Funktion**: Konto und Darstellung
- **Details**:
  - Kontoinformationen, Abmelden, Wechsel des Kontos
  - Farbschema: hell, dunkel, systemspezifisch
  - Anzeigeeinstellungen, Sprache/Region

### 7. Einstellungen (Zahnrad)
- **Funktion**: persönliche Kalenderkonfiguration
- **Details**:
  - **Allgemein**: Sprache, Region, Datums-/Zeitformat, Wochenanfang, erste Kalenderwoche
  - **Kalender**: Standardansicht, Arbeitszeiten, Erinnerungen, Standarddauer, Anzeige von Geburtstagen und Feiertagen, Besprechungseinstellungen
  - **Kalender-Synchronisierung**: Abgleich mit Google Kalender (lizenzabhängig, Microsoft-365-Mandant)
  - **Barrierefreiheit**: Tastatur-Shortcuts, Bildschirmlerner-Optionen
  - **Post/Anhänge**: Verhalten bei Besprechungsanlagen

### 8. Administration (Exchange Admin Center, Microsoft 365 Admin Center, Entra ID)
- **Funktion**: mandantweite Kalender-Verwaltung, nur für Administratoren
- **Details**:
  - **Ressourcenpostfächer**: Besprechungsräume und Equipment anlegen, Autoverteilung, Buchungsrichtlinien
  - **Freigaben und Delegation**: Postfachberechtigungen, Organisationsbeziehungen (Free/Busy zwischen Mandanten)
  - **Geräte- und Aufbewahrungsrichtlinien**, Compliance-Suche, Audit-Protokolle
  - **App-Registrierierungen**: Microsoft-Graph-Berechtigungen (`Calendars.ReadWrite`) für Integrationen

## Kontext-Menüs

### Rechtsklick auf einen Termin
- **Öffnen** bzw. **Bearbeiten**
- Serie bearbeiten: **Nur diesen Termin** / **Alle Termine in der Serie** / **Diese und folgende**
- **Verschieben in** anderen Kalender, **Duplizieren**
- **Löschen** (Termin oder Besprechungsanfrage absagen)
- **Kopieren** (Terminlink in die Zwischenablage)
- **Kategorie** zuweisen, **Erinnerung** ändern
- **Als E-Mail weiterleiten**

### Rechtsklick auf eine freie Zeit im Kalenderblatt
- **Neues Ereignis** zur angeklickten Zeit
- **Ganztägiger Termin**
- **Alle Termine ausblenden** (nur Ansicht)

### Rechtsklick in der Kalenderliste
- **Farbe/Kategorie** ändern
- **Teilen** und **Berechtigungen**
- **Als Standardkalender festlegen**
- **Aus der Liste entfernen** (Subscription, fremder Kalender)
- **Umbenennen**, **Löschen**

### Besprechungsanfragen in der Postansicht
- **Annehmen**, **Vorläufig annehmen**, **Ablehnen**, **Verschieben**, **Terminvorschlag senden**
- **Details anzeigen** und direkt im Kalender öffnen

## Menüs nach Rolle

### Mandants-Administrator (Exchange Admin / Global Admin)
- Ressourcenpostfächer, Buchungsrichtlinien, Organisationsbeziehungen
- Postfachdelegation und Freigaben mandantweit verwalten
- Graph-App-Berechtigungen, Audit-Log, Aufbewahrungs- und Compliance-Regeln

### Kalenderbesitzer (Owner)
- Eigener Kalender, Nebenkalender und Kalendergruppen anlegen
- Freigabestufen setzen, Termine mit Teilnehmern einladen
- Standardkalender, Farben, Erinnerungen, Import/Export

### Delegierter Bearbeiter (Editor / Author)
- Termine in fremden Kalendern anlegen und ändern (Rechte beachten)
- Keine Änderung an Freigaben, keine weitere Delegation

### Leser (Reviewer / Availability only)
- Termine einsehen bzw. nur Belegungszeiten sehen
- Kein Anlegen, kein Ändern, keine Anlage eigener Termine

### Teilnehmer (Kunde / extern)
- Besprechungsanfrage annehmen, vorläufig zusagen, ablehnen, Terminvorschlag senden
- Eigene Antwort nur im eigenen Kalender wirksam

### App-Identität (Integration)
- Liest und schreibt Termine über Microsoft Graph mit `Calendars.Read` bzw. `Calendars.ReadWrite`
- Sieht nur Kalender, für die die Berechtigung erteilt bzw adminseitig genehmigt wurde

## Einstellungs-Dialoge (Struktur)

| Dialog | Bereiche | Typische Felder |
|--------|----------|-----------------|
| Ereignisformular | Inhalt, Zeit, Teilnehmer, Suchoptionen | Titel, Ort, Beginn/Ende, Kategorie, Erinnerung |
| Planungsassistent | Woche, Teilnehmer, Ressourcen | Free/Busy-Zeilen, Konfliktanzeige |
| Teilen | Person, Berechtigungsstufe, Hinweis | Freigabestufe, E-Mail-Benachrichtigung |
| Kalenderliste | Kalender, Gruppen, Abonnements | Name, Farbe, Quelle |
| Einstellungen | Allgemein, Kalender, Sync, Barrierefreiheit | Wochenanfang, Arbeitszeit, Google-Sync |
| Ressourcenpostfach (Admin) | Allgemein, Buchung, Eigenschaften | Kapazität, Autoverteilung, Annahmerichtlinie |

## Shortcuts

Die dokumentierten Tasten (und die klar als nicht vorhanden markierten) stehen in [shortcuts.md](shortcuts.md).
