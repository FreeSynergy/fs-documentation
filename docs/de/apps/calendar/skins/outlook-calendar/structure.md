# Outlook Kalender - Struktur & UI/UX

## Übersicht

Outlook Kalender ist nach demselben Grundmuster aufgebaut wie die übrigen Microsoft-365-Oberflächen: links die Modulleiste und die Kalenderliste, oben die Befehlsleiste, in der Mitte das Kalenderblatt, rechts bzw. als Ebene darüber Detailformulare. Web, neues Outlook für Windows und Outlook für Mac sind identisch aufgebaut; Outlook Classic nutzt die klassische Windows-Fensterstruktur mit Registerblättern.

## Fenster-Struktur

### Hauptbereich (Outlook im Web / neues Outlook)

```
┌──────────────────────────────────────────────────────────────────────┐
│  App-Startleiste | Suche                                 Konto  Zahn│
├────┬──────────────┬──────────────────────────────────────────────────┤
│    │ Kalenderliste│  Befehlsleiste: Neues Ereignis | Ansicht | Heute │
│ P  │ ○ Meine Kal.│  Filter | Drucken | Teilen                        │
│ o  │ ─────────    ├──────────────────────────────────────────────────┤
│ s  │ ■ Privat     │  Datumsleiste  ◀  Oktober 2026  ▶   [Heute]     │
│ t  │ ■ Arbeit     │ ┌────┬────┬────┬────┬────┬────┬────┐            │
│    │ ■ Projekt A  │ 08 │09  │10  │11  │12  │13  │14  │            │
│ T  │ ─────────    │    │▓▓  │    │▓▓▓ │    │    │    │            │
│ o   │ Freigegeben │    │▓▓  │    │▓▓▓ │    │    │    │            │
│    │ ■ Vertretung│    │    │    │    │    │    │    │            │
│    │ ─────────    │    │    │    │    │    │    │    │            │
│ +  │ Feiertage    │    └────┴────┴────┴────┴────┴────┘            │
│    │ [Hinzufügen] │  Terminübersicht / Agenda unten oder rechts      │
└────┴──────────────┴──────────────────────────────────────────────────┘
```

### Bereiche

| Bereich | Position | Inhalt |
|---------|----------|--------|
| Modulleiste | links (mobil unten) | Post, Kalender, Personen, To Do, Weitere Apps |
| Kalenderliste | links | Eigene Kalender, Gruppen, Freigaben, Feiertage, Hinzufügen |
| Befehlsleiste | oben | Neues Ereignis, Ansicht, Heute, Filter, Drucken, Teilen |
| Kalenderblatt | Mitte | Raster nach Zeit (Tag/Woche/Monat), Terminblöcke |
| Detailformular | Overlay/Rechts | Termin- oder Ereignisfeld, Planungsassistent als Reiter |
| Such- und Kontobereich | oben rechts | Volltextsuche, Konto, Einstellungen |

### Detailformular (Termin)

```
┌──────────────────────────────────────────────────────────────┐
│  Betreff                                    [Senden] [?] [X] │
├──────────────────────────────────────────────────────────────┤
│  Titel · Ort · Beginn · Ende · Ganztägig · Zeitzone          │
│  Kategorie (Farbe) · Erinnerung · Anzeigen als               │
│  Teilnehmer: erforderlich / optional / Ressourcen            │
│  Onlinebesprechung (Teams) · Wiederholung · Anlagen          │
├──────────────────────────────────────────────────────────────┤
│  Reiter:  Formularelemente  |  Planungsassistent             │
└──────────────────────────────────────────────────────────────┘
```

### Planungsassistent

```
┌────────────────────────────────────────────────────────────────┐
│  Woche: 12.10. ─ 16.10.   [Auto-Vorschlag]  [Konflikt: 2]      │
├──────────┬─────────────────────────────────────────────────────┤
│ Anna     │ ░░░░│      │████│        │        │        │        │
│ Ben      │     │░░░░░░│████│        │████████│        │        │
│ Raum 3.4 │     │      │████│        │  frei  │        │        │
└──────────┴─────────────────────────────────────────────────────┘
```

### Layout-Varianten

1. **Standard**: Modulleiste + Kalenderliste + Kalenderblatt
2. **Kompakt**: Kalenderliste als Einblendung, Kalenderblatt breit
3. **Mobile**: untere Modulleiste, Kalenderliste als Drawer, Wochen-/Tagesansicht
4. **Outlook Classic**: Menüband (Register „Kalender"), Ordnerliste links, drei Ansichtspläne (Spalte, Karte, Vorschau)

## UI/UX

### Design-Prinzipien

- **Fluent Design**: Flächen, Kanten, dezente Schatten, Akzentfarbe aus dem Theme
- **Dichte Information**: viele Termine gleichzeitig sichtbar, ohne Dialogflut
- **Direktpfad statt Menüsuche**: wichtigste Aktionen in der Befehlsleiste
- **Konsistenz**: gleiche Bedienung in Web, neuem Outlook und Mac

### Farb- und Typografie-System

- **Hell/Dunkel/System** als Farbschema, hoher Kontrast als Windows-Modus
- **Kategoriefarben** pro Kalender und pro Termin, frei benennbar
- **Arbeitszeit** und Feiertage als hinterlegte Flächen im Raster
- Klare Hierarchie: Datumsleiste größer als Uhrzeitachse, Terminblocktitel fett

### Interaktionen

- **Drag & Drop im Kalenderblatt**: Termin verschieben (Minutenrastrierung, meist 15-/30-Minuten-Schritte)
- **Ziehen an der Unterkante**: Dauer ändern
- **Ziehen über die Zeitachse**: neuen Termin durch Aufziehen anlegen
- **Strg/Cmd + Ziehen**: Termin kopieren
- **Ziehen zwischen Kalendern**: Termin in anderen Kalender verschieben
- **Rechtsklick**: Kontextmenü mit Bearbeiten, Duplizieren, Verschieben, Link kopieren
- **Multi-Select** mit `Shift`/`Strg` für Serienaktionen (Löschen, Kategorie)
- **Animationen**: Overlay-Flyouts gleiten ein, Terminblöcke blenden beim Umzug kurz aus/ein, Sparrow/Skelett beim Laden; Reduktion der Bewegung über die Systemeinstellung „Bewegung reduzieren"
- **Auto-Speichern** bei Feldänderungen im Overlay-Formular; vollständiges Formular explizit mit **Senden**

### Responsive Design

- **Desktop**: volle Kalenderliste, Monats-/Wochenansicht, Planungsassistent
- **Schmales Browserfenster**: Kalenderliste klappt zur Einblendung, Befehlsleiste bündelt seltene Aktionen in „…"
- **Tablet**: Touch-Ziehen, größere Trefferflächen, Tages-/Wochenansicht bevorzugt
- **Telefon / Outlook Mobile**: untere Navigationsleiste, Agenda-Liste, Termin als Vollbildformular
- **Schrift skalierbar**: Browser-Zoom ohne Funktionsverlust, Layout bricht in Spalten um

### Barrierefreiheit

- **Tastatur**: Tab-Reihenfolge durch Raster, Liste und Formular; `Esc` schließt Overlays
- **Screenreader**: ARIA-Bezeichnungen für Terminblöcke, Datum und Antwortstatus
- **Fokusindikator** sichtbar, Fokus fängt in Dialogen
- **Kontrast**: Dark Theme und Windows-High-Contrast
- **Alt-Texte/Beschriftungen** für Symbole in der Befehlsleiste
- **Reduzierte Bewegung** folgt der Betriebssystemvorgabe
- **Diktat und Vergrößerung** über die Betriebssystem-Werkzeuge

## Performance

- **Lazy Loading**: Kalenderblätter laden den sichtbaren Zeitraum, Blättern lädt nach
- **Caching**: Desktop-Clients halten Kalender lokal (OST/Cache), Web-Client nutzt Sitzungs-Cache
- **Paginierung** bei Suchergebnissen und Calenderviews (auch über `@odata.nextLink` in der API)
- **Debounce** in Suche und Teilnehmerauswahl
- **Free/Busy-Cache** im Planungsassistenten, damit viele Teilnehmer schnell darstellbar bleiben

## Siehe auch

- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md)
