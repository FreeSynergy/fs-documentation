# Pipedrive - Struktur & UI/UX

## Übersicht

Pipedrive zeigt links die Navigationsleiste, oben die Filter- und Aktionsschaltflächen und in der Mitte die aktive Ansicht: Pipeline-Board, Liste oder Zeitplan. Ein angeklickter Deal öffnet einen Detailbereich als Overlay über der Liste. Konfigurationsdialoge erscheinen als zentrierte Panels mit Formular.

## Fenster-Struktur

### Pipeline-Board (Deals)

```
+---------------------------------------------------------------------------+
| Logo | Navigation links aussen | Filterleiste | [Add] | Avatar | Setup    |
+---------------------------------------------------------------------------+
| Filter: Pipeline | Stage | Bearbeiter | Betrag | Abschlusszeitraum         |
+---------------------------------------------------------------------------+
|  Stage A        |  Stage B        |  Stage C        |  Won    |  Lost     |
|  +------------+ |  +------------+ |  +------------+ |         |           |
|  | Deal 1     | |  | Deal 4     | |  | Deal 7     | |         |           |
|  | Betrag     | |  | Betrag     | |  | Betrag     | |         |           |
|  | Abschluss  | |  | Abschluss  | |  | Abschluss  | |         |           |
|  +------------+ |  +------------+ |  +------------+ |         |           |
|  Summe: ...     |  Summe: ...     |  Summe: ...     |         |           |
+---------------------------------------------------------------------------+
```

### Deal-Detailbereich (Overlay)

```
+---------------------------------------------------------------------------+
|  Deal-Titel                     [Bearbeiten] [Duplizieren] [Loeschen] x  |
+------------------------+--------------------------------------------------+
|  Felder:               |  Reiter: Uebersicht | Aktivitaeten | Dateien     |
|  Betrag, Stage, Datum  |  Produkte | Team & Zugriff                       |
|  Bearbeiter, Quelle    |                                                    |
|  Eigene Felder         |  Aktivitaeten-Protokoll (E-Mails, Anrufe, Tasks)  |
|                        |  [+ Aktivitaet hinzufuegen]                      |
+------------------------+--------------------------------------------------+
```

### Company-Setup (Admin)

```
+---------------------------------------------------------------------------+
|  Setup-Kopf (Zuruick)                        [Speichern]                  |
+------------------+--------------------------------------------------------+
|  Setup-Navigation|  Einstellungsformular                                  |
|  - Pipelines     |  Feld fuer Feld, Hilfetext rechts                     |
|  - Custom Fields |  Tabelle bei Feld- und Nutzerverwaltung                |
|  - Nutzer        |                                                        |
+------------------+--------------------------------------------------------+
```

## Bereiche

| Bereich | Position | Inhalt |
|---------|----------|--------|
| Navigationsleiste | Links | Home, Aktivitäten, Deals, Mailbox, Produkte, Marketing, Berichte, More |
| Kopfzeile | Oben rechts | Aktionsschaltfläche "Add", Suchfeld, Avatar-Menü, Setup-Symbol |
| Filterleiste | Unter der Kopfzeile | Pipeline, Stage, Bearbeiter, Betrag, Zeitraum, gespeicherte Filter |
| Board-Fläche | Mitte | Stage-Spalten mit Deal-Kacheln, Spaltensummen |
| Listenansicht | Mitte | Tabelle mit Spalten, Sortierung, Seitenzahlen |
| Detailbereich | Overlay rechts bzw. zentriert | Felder, Reiter, Aktivitätenprotokoll, Beziehungen |
| Meldungen | Oben rechts | Erfolg, Fehler, Synchronisationsstatus |

## UI/UX

### Design-Prinzipien

- **Pipeline als Hauptmetapher**: alles zeigt auf Stage, Betrag und Abschlussdatum
- **Weniger Felder, mehr Kontext**: Standard-Feldmenge bewusst klein, Erweiterungen über eigene Felder
- **Handlung direkt am Objekt**: Aktivitäten und E-Mails hängen sichtbar am Deal
- **Kurze Wege**: Anlegen über eine Aktionsschaltfläche aus jeder Ansicht

### Farbschema und Themes

- **Hell, einheitlich** über alle Ansichten; kein auswählbares Dark Mode in der Oberfläche (versionsabhängig)
- **Stage-Farben** und Statusfarben für Won/Lost sind vorgegeben
- **Akzentfarbe** in Buttons und Links, Statusgrün für erledigte Aktivitäten
- **Symbole** je Aktivitätstyp und Modul

### Typografie

- **Kachelschriften** mit Titel, Betrag und Datum in klarer Hierarchie
- **Tabellen** kompakt, Zahlen rechtsbündig, Beträge mit Währungsformat
- **Formulare** mit Beschriftung über dem Feld und Hilfetexten

### Interaktionen

- **Drag & Drop**: Deal-Kachel zwischen Stage-Spalten ziehen, Spaltenreihenfolge im Setup ändern
- **Hover**: Kachel zeigt Aktionen (Bearbeiten, Duplizieren, Bearbeiter wechseln)
- **Animationen**: kurzes Einblenden des Detailbereichs, Verschiebe-Übergang der Kachel, Skeleton-Platzhalter beim Laden
- **Inline-Bearbeitung**: Beträge und Auswahlfelder direkt in der Liste änderbar (versionsabhängig)
- **Autocomplete**: Kontakt-, Firmen- und Deal-Suche in Beziehungsfeldern
- **Bestätigungsdialog** beim Verschieben nach "Lost" mit Grundauswahl

### Responsive Design

- **Desktop**: volles Board mit allen Spalten, horizontales Scrollen bei vielen Stages
- **Tablet**: Navigationsleiste reduziert, Board mit weniger Spalten
- **Mobil**: Kartenartige Listen statt Board, Detailbereich in Vollbild; für tägliche Arbeit sind die nativen Apps die empfohlene Variante
- **Setup-Bereiche** sind auf kleinen Bildschirmen als gestapelte Formulare nutzbar

### Zugänglichkeit

- **Tab-Reihenfolge** folgt Navigation, Filterleiste, Kacheln, Detailbereich
- **`Esc`** schließt den Detailbereich und Dialoge
- **Pfeiltasten** in Auswahllisten und Autocomplete-Vorschlägen
- **Fokusanzeige** ist sichtbar; Kontrast in Standardansichten hoch
- **Screenreader**: Bereiche sind beschriftet, Board-Kacheln bleiben aber dicht; alternative Listenansicht ist einfacher
- **Zoom**: Browser-Zoom ohne abgeschnittene Bedienelemente

### Performance

- **Single Page Application**: Modulwechsel ohne vollständigen Seitenneuaufbau
- **Nachladen in Abschnitten**: lange Deal-Listen werden in Häppchen geladen
- **Caching**: Kontakte und Organisationen lokal im Client, E-Mail-Sync im Hintergrund
- **Empfehlung**: Filter setzen statt sehr viele Kacheln auf einmal zu laden; eigene Felder sparsam einsetzen

## Siehe auch

- [menu.md](menu.md) - Menüpunkte nach Rolle
- [features.md](features.md) - Module und Automatisierung
- [shortcuts.md](shortcuts.md) - Tastatursteuerung
- [api.md](api.md) - REST-API und Webhooks
