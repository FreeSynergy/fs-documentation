# Nextcloud Calendar - Struktur & UI/UX

## Übersicht

Nextcloud Calendar ist eine Web-App innerhalb des Nextcloud-Browsers: feste Kopfzeile der Plattform links die Kalender-Seitenleiste, rechts davon Werkzeugleiste und Zeit-Raster. Ereignisse werden in Dialogen (Modals) bearbeitet, nicht auf eigenen Seiten.

## Seiten-Struktur

### Hauptansicht

```
┌─────────────────────────────────────────────────────────────────┐
│  Nextcloud-Kopfzeile  [App-Starter] [Suche]      [Benutzermenü]  │
├──────────────────┬──────────────────────────────────────────────┤
│  Seitenleiste    │  Werkzeugleiste                              │
│  [＋ Neu]        │  [Agenda|Tag|Woche|Arbeitswoche|Monat]       │
│                  │  [← Heute →]  [Datum]   [Einstellungen/Filter]│
│  Kalender        │ ┌──────────────────────────────────────────┐ │
│  ☑ Privat        │ │  Zeit-Raster                             │ │
│  ☑ Team XY       │ │  ┌────────────────────────────────────┐  │ │
│  ▸ Gruppenkalender│ │  │  Termine als farbige Blöcke        │  │ │
│  ☁ Abos          │ │  └────────────────────────────────────┘  │ │
│  ☼ Geburtstag    │ │  (Tag/Woche/Monat mit Stundenlinien)     │ │
│  ⚑ Feiertage     │ │                                          │ │
│                  │ └──────────────────────────────────────────┘ │
└──────────────────┴──────────────────────────────────────────────┘
```

### Ereignis-Editor (Dialog)

```
┌─────────────────────────────────────────────────────────────────┐
│  [Titel eingeben]                                   [Speichern ⌄] │
├──────────────────────────────────┬──────────────────────────────┤
│  Datum/Uhrzeit · ganztägig       │  Reiter „Details"             │
│  Wiederholung · Erinnerungen     │  Kalender & Farbe             │
│  Beschreibung                    │  Teilnehmer (+Nutzer, Raum,   │
│  Ort · Talk-Link                 │    Gruppe, E-Mail)            │
│  Anhänge · Kommentare            │  Terminstatus (busy/frei)     │
│                                  │  Verfügbarkeiten-Ansicht      │
└──────────────────────────────────┴──────────────────────────────┘
```

### Freigabe-Dialog

```
┌─────────────────────────────────────┐
│  [Empfänger suchen …]               │
│  Max  [Verfügbarkeiten ▾] [×]      │
│  Team Vertrieb  [Anzeigen ▾]  [×]  │
│  Öffentlicher Link  [ ] an  [Passwort] │
└─────────────────────────────────────┘
```

## UI/UX

### Design-Prinzipien

- **Plattform-Konsistenz**: folgt dem Nextcloud-Design (Kopfzeile, Icons, Buttons wie in Dateien/Mail)
- **Reduzierung**: Verwaltung fast vollständig über Symbole an Kalender-Einträgen statt Menüs
- **Direktheit**: Klick/Ziehen im Raster erzeugt oder verschiebt Termine ohne Zwischenschritte
- **Farbcodierung**: Kalenderfarben ziehen sich durch Raster, Seitenleiste und Dritter clients

### Farben und Typografie

- Kalenderfarben: wählbar aus einer Nextcloud-Palette (Punkt-Menü), auch Eigene
- **Hell-/Dunkelmodus** über die Darstellungs-Einstellung der Instanz (Systemfarben möglich)
- Schrift: Systemschrift der Plattform, kleine Beschriftungen, gute Lesbarkeit im Raster; keine einstellbare Schriftgröße in der App (Browser-Zoom nutzen)

### Interaktionen

- **Drag & Drop**: Termine im Raster verschieben, am Rand die Dauer ändern
- **Ziehen zum Erstellen**: im Wochen-/Tagesraster aufziehen erzeugt den Termin in dieser Zeitspanne
- **Klick auf freien Slot / auf Termin**: Editor mit vorausgefüllten Werten bzw. Details
- **Hover**: Termine und Kalender-Einträge zeigen Aktionen (Teilen, Bearbeiten, Mehr) als Symbole
- **Animationen**: sparsam - sanfte Übergänge beim Ansichtswechsel, Ein-/Ausklappen der Seitenleiste, Modal-Einblendung; keine aufwendigen Effekte (Details je Version (nicht dokumentiert))
- **Rückgängig-Meldung**: Nach dem Löschen eines Termins erscheint kurz eine „Rückgängig"-Meldung (Action im Notification-Flyout)

## Responsive Design

- **Desktop**: volle Seitenleiste neben dem Raster, alle Ansichten
- **Tablet/schmal**: Seitenleiste wird zum Überlagerungs-Fach (Hamburger/Menu-Icon), Raster passt Spalten an
- **Mobil**: kompaktere Kopfzeile, Agenda-/Tagesansichten praktisch, Editor als Vollbild-Dialog; Terminerstellung per Fingertipp
- Eigenständige native Apps für die Kalender-UI existieren nicht - mobil ist die responsive Web-Ansicht oder ein CalDAV-Client der Weg

## Zugänglichkeit

- **Tastatur**: Formularfelder, Buttons und Dialoge sind per `Tab`/`Enter`/`Esc` bedienbar (Nextcloud-Standardkomponenten); **kein vollständiges Tastatur-Modell** für Raster und Drag & Drop - Termine lieber im Editor per Datum/Zeit verschieben
- **Screenreader**: Dialoge und Seitenleisten-Elemente sind beschriftet (Nextcloud-Grundlage); Terminblöcke im Raster sind dichte Graphiken - die Agenda-Ansicht ist die zugänglichste Alternative
- **Kontrast und Zoom**: helles Standard-Theme mit gutem Kontrast, Skalierung über Browser-Zoom ohne Funktionsverlust
- **Redundante Wege**: jede Aktion (Löschen, Teilen, Export) ist auch ohne Drag & Drop über Dialoge erreichbar

## Performance

- **Bereichsnachladen**: nur der sichtbare Zeitraum wird vom Server geholt (timeobjects-Schnittstelle)
- **Serverseitige Suche** abschaltbar, damit große Postfächer die Oberfläche nicht bremsen
- **Caching**: Caching im Browser und serverseitig (Redis empfohlen); Abos werden in Hintergrundjobs aktualisiert
- **Debounce** in der Suche und beim Freigabe-Sucher

## Siehe auch

- [menu.md](menu.md) - Menüpunkte und Rollen
- [features.md](features.md) - Funktionsumfang
- [shortcuts.md](shortcuts.md) - Tastatursteuerung
