# Google Kalender - Struktur & UI/UX

## Übersicht

Google Kalender ist eine Web-Einzelseitenanwendung mit drei Hauptzonen: schmale Kopfzeile, einklappbare Kalender-Seitenleiste links und ein Datumsraster in der Mitte. Termine werden nie in eigenen Fenstern dargestellt, sondern als Popups über dem Raster und als Vollseite beim Bearbeiten. Dazu kommen die Einstellungsseite und die Buchungsseite von Terminplänen.

## Seiten-Struktur

### Hauptansicht (Woche/Tag)

```
┌──────────────────────────────────────────────────────────────────────┐
│ ☰  Ansicht ▾   ‹  Heute  ›   27. Oktober 2026     🔍  ⚙  ❓  Konto  │  Kopfzeile
├──────────────┬───────────────────────────────────────────────────────┤
│ Erstellen +  │ Mo   Di   Mi   Do   Fr   Sa   So                      │
│              │ ┌────┬────┬────┬────┬────┬────┬────┐                  │
│ 📅 Mini-Monat│09:00 │▓▓▓│    │    │    │    │    │                  │
│              │      │Team│    │ ░░ │    │    │    │   Raster:        │
│ Meine Kalender│ 10:00│    │████│    │    │    │    │   Zeilen =       │
│  ☑ Primär    │ 11:00│    │████│    │▓▓▓│    │    │   Uhrzeiten,     │
│  ☑ Projekt A │ 12:00│    │    │    │▓▓▓│    │    │   Spalten = Tage │
│  ☐ Geburtstage│     │    │    │    │    │ ●  │    │   "Jetzt"-Linie  │
│              │ ...  │    │    │    │    │    │    │                  │
│ Andere Kalender│             │    │    │    │    │    │                 │
│  ☑ Team (geteilt)│          └────┴────┴────┴────┴────┴────┴────┘     │
│  + hinzufügen│ [Aufgaben]  [Frei/Belegt]                             │
└──────────────┴───────────────────────────────────────────────────────┘
```

### Monatsansicht

```
┌───────────────────────────────────────────────────────────┐
│  Mo  Di  Mi  Do  Fr  Sa  So                               │
│ ┌────┬────┬────┬────┬────┬────┬────┐                      │
│ │ 20 │ 21 │ 22 │ 23 │ 24 │ 25 │ 26 │  Zellen pro Tag,    │
│ │ ●  │ ██ │    │ ▓▓ │    │    │ ○  │  Einträge als       │
│ ├────┼────┼────┼────┼────┼────┼────┤  Farbchip + Titel;   │
│ │ 27 │ 28 │ 29 │ 30 │ 31 │  1 │  2 │  Überlauf → "+3     │
│ │ ███│    │ ▓▓ │ ██ │    │    │    │  weitere"            │
│ └────┴────┴────┴────┴────┴────┴────┘                      │
└───────────────────────────────────────────────────────────┘
```

### Schnell-Dialog (Klick ins Raster)

```
┌────────────────────────────────────────────┐
│ Termin hinzufügen          ⌄  ✕            │
│ Titel ____________________________         │
│ 📅 27. Okt. 2026   🕘 09:00 → 🕙 09:30     │
│ Kalender ▾ Primär        [ ] Ganztägig     │
│ [ Mehr Optionen ]        [ Fertig ]        │
└────────────────────────────────────────────┘
```

### Termin-Editor (Vollseite/Dialog)

```
┌──────────────────────────────────────────────────────────────┐
│ Termin bearbeiten                                    🗑  ✕   │
├──────────────────────────────────────────────────────────────┤
│ Titel                                                        │
│ Ort · Datum · Uhrzeit · Zeitzone             [Ganztägig]     │
│ Wiederholung ▾ (täglich/wöchentlich/monatlich/benutzerdef.)  │
│──────────────────────────────────────────────────────────────│
│ Gast hinzufügen ────────────────────────  Gäste: Ja/Nein/Viel │
│ Google-Meet hinzufügen  ·  Raum/Gerät hinzufügen             │
│ Erinnerung: Pop-up 10 Min. · Kalender · Farbe · Sichtbarkeit  │
│ Verfügbarkeit: belegt / frei                                 │
│ Beschreibung (Rich Text) · Anhänge · Arbeitsort/Fokuszeit    │
│ Gäste dürfen: einladen · ändern · löschen                    │
│                     [ Abbrechen ]  [ Speichern ]             │
└──────────────────────────────────────────────────────────────┘
```

### Termindetail-Popup (Klick auf Termin)

```
┌──────────────────────────────────────────┐
│ Team-Meeting                        ⋮  ✕ │
│ Mo, 27. Okt. · 09:00 - 09:30 (MESZ)      │
│ 📍 Raum 3 · 🎥 Meet beitreten            │
│ Gäste:  ● Anna (Ja) ● Ben (Nein) ○ Cira  │
│ [ Ja ] [ Nein ] [ Vielleicht ]           │
│ Beschreibung, Anhänge, Kalendereintrags-ID│
│ ⋮ = Duplizieren · Löschen · Verschieben   │
└──────────────────────────────────────────┘
```

### Einstellungsseite

```
┌──────────────┬────────────────────────────────────────────┐
│ Allgemein    │  Standardkalender, Wochenstart, Dichte,    │
│ Ansichten    │  Zeitzonen, Sprache, Aufgaben, …           │
│ Arbeitszeiten│                                            │
│ Benachricht. │  (linke Navigation, rechter Formular-      │
│ Intelligent  │   bereich; eigene URL pro Abschnitt)       │
│ Import/Export│                                            │
│ Wiederherst. │                                            │
│ Kalenderliste│  jeder Kalender einzeln anklickbar         │
└──────────────┴────────────────────────────────────────────┘
```

### Mobile App (Android/iOS)

```
┌──────────────────────────┐
│ ☰   27. Oktober    🔍 ⚙  │
│ ─────────────────────────│
│ 9:00 ┌──────────────┐    │
│      │ Team-Meeting │    │
│      │ Raum 3 · Meet│    │
│ 9:30 └──────────────┘    │
│10:00 ░░ frei ░░          │
│      (Zeitleiste)        │
│──────────────────────────│
│ Heute · Agenda · Kalender │  untere Navigation /
└──────────────────────────┘  Kalenderauswahl je nach Version
```

## UI/UX

### Design-Prinzipien
- **Material Design**: flache Flächen, Karten-Popups, abgerundete Ecken, deutliche Primärschaltfläche
- **Farbcodierung**: jeder Kalender hat Farbe und optional Symbol; Termine übernehmen die Kalenderfarbe
- **Dichte**: "kompakt" und "normal" für Raster und Agenda
- **Reduzierte Chrome-Elemente**: Raster dominiert, Werkzeuge erscheinen bei Hover/Fokus
- **Konsistenz mit Gmail/Meet**: gleiche Kopfzeile, gleiches Kontomenü

### Typografie und Symbole
- **Schrift**: Roboto, variable Größen (ca. 12 px Rasterbeschriftung bis 18-22 px Titel)
- **Symbole**: Google-Material-Icons für Erstellen, Suche, Einstellungen, Drei-Punkte-Menüs
- **Ziffernblatt**: Uhrzeitachse links, Tages-/Wochen-/Monatskopf mit heutiger Markierung

### Interaktionen
- **Drag & Drop**: Termin am Block greifen und auf Zielzeit ziehen; an der Unterkante ziehen verlängert; Einrasten am Rasterraster (15/30-Minuten-Schritten)
- **Hover**: freie Zeitfenster zeigen "+"-Symbol, Termine zeigen Stift- und Detailsymbol
- **Klick**: freies Fenster → Schnell-Dialog; Termin → Detail-Popup; "Mehr Optionen" → Voll-Editor
- **Animationen**: Popups skalieren/blenden ein, Termine gleiten beim Verschieben in die neue Position, "Jetzt"-Linie wandert, Toast-Meldung mit "Rückgängig" nach Änderungen
- **Ladezustände**: Skeleton-Plätze im Raster, dezente Fortschrittsanzeige oben
- **Rückgängig**: nach Verschieben, Löschen undÄndern erscheint ein Rückgängig-Hinweis

### Responsive Design
- **Desktop (breit)**: Seitenleiste dauerhaft sichtbar, Wochen-/Monatsraster mit allen Spalten
- **Tablet/schmal**: Seitenleiste wird Overlay, Wochenansicht auf wenige Tage reduziert, Mini-Monat ausgeblendet
- **Smartphone**: Kopfzeile mit Hamburger und Suche, Raster als Tages-/Zeitleiste, Termine als Karten, Bottom-Navigation; Querdrehen vergrößert das Raster
- **Desktop-Programm**: existiert nicht; Websicht und mobile Apps sind die einzigen offiziellen Clients

### Barrierefreiheit
- **Tastatur**: Tab-Reihenfolge über Kopfzeile, Seitenleiste und Termine; offizielle Kurzbefehle (siehe [shortcuts.md](shortcuts.md))
- **Screenreader**: ARIA-Beschriftungen für Rasterzellen, Termine und Dialoge; Termininformationen als zusammenhängender Text lesbar
- **Farbfehlsichtigkeit**: Symbole pro Kalender statt nur Farbe, dunkles und helles Farbschema, hohe Kontraste
- **Zoom und Textgröße**: Browser-Zoom ohne Funktionsverlust, Dichteoption reduziert Überlappungen
- **Bewegungsreduktion**: Systemweite Reduktion von Animationen wird vom Browser unterstützt; eigene Einstellung in Kalender ist nicht dokumentiert

## Performance

- **Inkrementelles Nachladen**: nur der sichtbare Zeitbereich wird abgerufen (API-Zeitfenster)
- **Sync-Tokens und ETags**: wiederholte Abfragen liefern nur Änderungen
- **Raster-Virtualisierung**: lange Zeitachsen rendern nur sichtbare Zeilen
- **Caching**: Browser-Cache und Client-seitiger Kalenderbestand; Mobil-App hält den aktuellen Zeitraum lokal

## Siehe auch

- [menu.md](menu.md)
- [features.md](features.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md)
