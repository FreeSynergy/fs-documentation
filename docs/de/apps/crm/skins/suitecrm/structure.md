# SuiteCRM - Struktur & UI/UX

## Übersicht

SuiteCRM 7.x zeigt oben eine Menüleiste, darunter die Modulansicht (Liste, Detail, Formular) und links bei Bedarf ein Filterpanel. SuiteCRM 8 legt eine Angular-Anwendung als Rahmen um dieselben Ansichten: eigene Kopfzeile, Modulmenü über ein Aufklappmenü, Inhalte in einer eigenen Panel-Fläche. Die Grundlogik bleibt gleich: Liste -> Detail -> Bearbeiten.

## Fenster-Struktur

### Listenansicht (SuiteCRM 7.x)

```
+--------------------------------------------------------------------------+
| Logo | Hauptmenue (Home, Activities, Leads, Opportunities, ...) | Admin | Benutzer |
+--------------------------------------------------------------------------+
| Brotpfade: Leads > alle Leads      [Suche] [Sortierung] [Seitengroesse]   |
+------------------+-------------------------------------------------------+
| Filterpanel      |  Liste (Tabelle)                                      |
| - Feldfilter     |  [ ] Name      Firma      Stage      Bearbeiter   ...  |
| - Gespeicherte   |  [x] Meyer AG  ...      Proposal   ...               |
|   Filter         |  [ ] ...                                             |
| - Mass Actions   |                                                       |
| - Feldauswahl    |  [Ergebnisse blaettern: < 1 2 3 >]                    |
+------------------+-------------------------------------------------------+
```

### Detailansicht mit Subpanels

```
+--------------------------------------------------------------------------+
|  Datensatz-Titel (Name)          [Bearbeiten] [Duplizieren] [Loeschen]   |
+--------------------------------------------------------------------------+
|  Feldbereich (2 Spalten)                                                 |
|  Status: New          Telefon: ...        E-Mail: ...       Branche: ... |
+--------------------------------------------------------------------------+
|  Subpanel: Kontakte          | Subpanel: Notizen      | Subpanel: Verlauf |
|  [+ Eintrag hinzufuegen]     | [+ Notiz]              | (Zeitstempel)     |
+--------------------------------------------------------------------------+
```

### SuiteCRM 8 (Angular-Shell)

```
+--------------------------------------------------------------------------+
|  App-Kopf: Modulmenue / Modulsuche    |   Persoenliches Menue             |
+--------------------------------------------------------------------------+
|  Startbereich mit Karten (Module)                                        |
|  +-------------------+   +-------------------+   +-------------------+   |
|  | Leads             |   | Opportunities     |   | Cases             |   |
|  +-------------------+   +-------------------+   +-------------------+   |
|  Inhaltspanel: eingebettete Ansicht des gewählten Moduls                 |
+--------------------------------------------------------------------------+
```

## Bereiche

| Bereich | Position | Inhalt |
|---------|----------|--------|
| Hauptmenüleiste | Oben | Module als Dropdowns, Admin-Menü, Benutzer-Menü |
| Brotpfad / Titelleiste | Unter der Menüleiste | aktueller Bereich, Suche, Ansichtsoptionen |
| Filterpanel | Links | Feldfilter, gespeicherte Filter, Mass Actions, Spaltenauswahl |
| Liste | Mitte | Tabelle mit Sortier- und Auswahlkästchen, Paginierung |
| Detailbereich | Mitte | Feldpaare, Status, Beziehungen |
| Subpanels | Unterhalb der Felder | verknüpfte Datensätze anderer Module |
| Dashlets | Startseite | kleine Paneele mit Aufgaben, Aktivitäten, Diagrammen |
| Meldungen | Oben mittig | Erfolgs- und Fehlermeldungen nach Speichern |

## UI/UX

### Design-Prinzipien

- **Modul Denkweise**: jede Datenart hat dieselbe Dreierfolge Liste, Detail, Formular
- **Administratoren statt Entwickler**: Studio und Filterpanel machen Anpassung ohne Code bedienbar
- **Daten primero**: dichte Tabellen, viele Spalten, wenig Dekorations-Elemente
- **Waagerechte Menüs mit Dropdowns** statt dauerpräsenter Seitenleiste (7.x)

### Farbschema und Themes

- **Standard-Theme "SuiteP"** (7.x) mit heller Tabellenfläche und blauer Menüleiste
- **SuiteCRM 8** liefert ein eigenes, modernes Theme der Angular-Shell (Name versionsabhängig)
- **Theme pro Benutzer** in den persönlichen Einstellungen umschaltbar (sofern installiert)
- **Eigene Themes** über Theme-Verzeichnisse und CSS; kein Dark Mode ab Werk in 7.x (in 8.x versionsabhängig)

### Typografie

- **Tabellen und Formulare** in Systemschrift, 12 bis 14 Pixel
- **Feldlabels** fett, Werte normal; Pflichtfelder mit Stern
- **Diagramme** in Dashlets mit beschrifteten Achsen

### Interaktionen

- **Hover**: Zeilenhervorhebung in Listen, Symbol-Buttons erscheinen beim Überfahren
- **Klick**: Zeile öffnet Detailansicht; Bearbeiten öffnet Formular mit Speichern oder Abbrechen
- **Drag & Drop**: nur im Dashboard zum Sortieren der Dashlets, nicht in Listen
- **Animationen**: sparsam; Auf- und Zuklappen von Filterpanel und Subpanels, Fortschrittsbalken bei Imports
- **Formularvalidierung**: Client- und Serverprüfung, Fehlermeldung über dem Feld
- **Autocomplete**: Personen- und Firmente Suche in Beziehungsfeldern

### Responsive Design

- **Desktop**: volle Breite mit Filterpanel und vielen Spalten
- **Tablet**: Menüleiste bleibt, Spaltenanzahl reduziert
- **Mobil**: umschaltbares Responsive-Theme bzw. kompaktes Theme, Menüs als Ausklappmenü, Subpanels untereinander
- **SuiteCRM 8** ist von Grund auf responsiver als 7.x; ältere Ansichte können auf kleinen Bildschirmen horizontal scrollen

### Zugänglichkeit

- **Tab-Reihenfolge** folgt Formular- und Tabellenstruktur; Checkboxen und Buttons sind per Leertaste bedienbar
- **Esc** bricht Dialoge und Popups ab (versionsabhängig)
- **Screenreader**: Beschriftungen vorhanden, aber Tabellen mit vielen Spalten sind für Screenreader dicht; ARIA-Ausbau ist in 8.x besser als in 7.x
- **Kontrast und Schriftgröße** über den Browser-Zoom skalierbar
- **Tastatur-Shortcuts**: keine anwendungsspezifischen, siehe [shortcuts.md](shortcuts.md)

### Performance

- **Serverseitiges Caching** von Metadaten und Templates, Caches im Installationsverzeichnis (`cache/`)
- **Paginierung** (Standard 10 bis 30 Zeilen) und optionale Spaltenauswahl halten Listen schnell
- **Volltextsuche** kann auf grossen Datenbeständen langsam sein; Datenbank-Indizes und Wartungsjobs helfen
- **Empfehlung**: Scheduler per `cron.php` laufen lassen, Cache nach Updates leeren, ungenutzte Module deaktivieren

## Siehe auch

- [menu.md](menu.md) - Menüpunkte nach Rolle
- [features.md](features.md) - Module und Automatisierung
- [shortcuts.md](shortcuts.md) - Tastatursteuerung
- [api.md](api.md) - REST und SOAP
