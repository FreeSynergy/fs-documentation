# Synology DSM - Struktur & UI/UX

## Übersicht

DSM imitiert einen Desktop im Browser: eine schmale obere Leiste, eine App-Leiste am unteren Rand, eine Desktop-Fläche mit Widgets und frei positionierbaren Fenstern. Jede Anwendung (File Station, Systemsteuerung, Paketzentrum …) öffnet ein Fenster mit eigener Titelleiste und oft eigenen Reitern. Mehrere Fenster und mehrere Browser-Tabs können parallel arbeiten.

## Fenster-Struktur

### Desktop-Ansicht

```
┌──────────────────────────────────────────────────────────────────────┐
│ [Hauptmenü]              [     Suche      ] [Meldungen] [Konto]    │
├──────────────────────────────────────────────────────────────────────┤
│  Desktop-Fläche                                  ┌────────────────┐ │
│                                                  │ System Pulse    │ │
│   ┌───────────────────────────┐                  │ CPU 12 % · RAM │ │
│   │ File Station (Fenster)    │                  │ Volume 68 %    │ │
│   │ Titel: - + x            │                  │ Netz ↓ 3 MB/s  │ │
│   │ [Ordner][Vorschau][Aufgaben]                 ├────────────────┤ │
│   │ ┌───────┬───────────────┐ │                  │ Speicher-      │ │
│   │ │Baum   │ Dateiliste     │ │                  │ warnungen (2)  │ │
│   │ └───────┴───────────────┘ │                  └────────────────┘ │
│   └───────────────────────────┘                                    │
│                                                  ┌────────────────┐ │
│                                                  │ Uhr / Datum     │ │
│                                                  └────────────────┘ │
├──────────────────────────────────────────────────────────────────────┤
│  App-Leiste: [Datei][Systemsteuerung][Paketzentrum][Drive] (…)      │
└──────────────────────────────────────────────────────────────────────┘
```

### Hauptmenü (Overlay)

```
┌────────────────────────────────────────────┐
│  Suchfeld im Menü                          │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌──────┐ │
│  │ Dateist│ │ System │ │ Paket  │ │Drive │ │
│  │ ation  │ │ steuer.│ │ zentrum│ │      │ │
│  └────────┘ └────────┘ └────────┘ └──────┘ │
│  [Anordnung bearbeiten]  [Alle Programme]  │
└────────────────────────────────────────────┘
```

### Dialog (Bestätigung / Assistent)

```
┌──────────────────────────────────────────┐
│ Dialogtitel                      [✕]     │
├──────────────────────────────────────────┤
│  Feld · Auswahl · Schalter               │
│  Fortgeschritten ▸                       │
├──────────────────────────────────────────┤
│          [Abbrechen]  [Weiter/OK]        │
└──────────────────────────────────────────┘
```

## Bereiche

| Bereich | Position | Inhalt |
|---------|----------|--------|
| Obere Leiste | Oben | Hauptmenü, Universal Search, Benachrichtigungen, Konto-Menü |
| App-Leiste | Unten | angepinnte Anwendungen, laufende Fenster |
| Desktop-Fläche | Mitte | Hintergrund, Desktop-Widgets, Fensterschatten |
| Fenster | frei verschiebbar | Titelleiste, Reiter/Werkzeugleiste, Arbeitsbereich |
| Seitenleiste im Fenster | links | Ordnerbaum, Kategorien, Filter |
| Statusleiste im Fenster | unten | Auswahlinfo, Aufgabenfortschritt |
| Overlay-Dialoge | zentriert | Formulare, Assistenten, Bestätigungen |
| Toast / Meldung | rechts oben | Erfolg, Fehler, laufende Aufgaben |

## UI/UX

### Design-Prinzipien

- **Desktop-Metapher**: Fenster, Leisten, Andocken – Nutzer finden sich wie am Schreibtisch zurecht
- **Dichte Tabellenansichten**: Listen mit Spalten, Filtern und Massenaktionen statt Einzelkarten
- **Rechte sichtbar machen**: nicht freigeschaltete Pakete erscheinen gar nicht erst im Menü
- **Assistenten für Risiko**: kritische Schritte (Volume, Freigabelöschung) mit Rückblick-Seite und Bestätigung

### Farbschema und Themes

- **Heller und dunkler Modus** (DSM 7), wählbar im Konto-Menü bzw. nach Systemeinstellung
- **Akzentfarbe** und Symbolstil in den Desktop-Einstellungen
- **Hintergrundbilder** (vorhandene Auswahl oder eigenes Bild)
- **Kontrastreiche Statusfarben** für Warnung (gelb), Fehler (rot), Erfolg (grün)
- **Barrierefreiheitsoptionen** in den Anzeigeeinstellungen (Textgröße, Kontrast je nach DSM-Stand)

### Interaktionen

- **Fenster**: verschieben über Titelleiste, skalieren an Kanten, maximieren/wiederherstellen, Überlappung mit Fokuswechsel
- **Fensteranordnung**: andocken an Bildschirmrändern, seitlich nebeneinander, alle minimieren
- **Drag & Drop**: Dateien aus dem Finder/Explorer in File Station ziehen, Zielordner wird hervorgehoben
- **Mehrfachauswahl**: Klick mit `Strg`/`Cmd`, Bereich mit `Umschalt`, Aufklapp-Auswahl in Listen
- **Kontextmenüs**: Rechtsklick auf Dateien, Symbole, Desktop und Leistenobjekte
- **Animationen**: Fenster öffnen/schließen mit kurzer Blende, Menüs klappen auf, Fortschrittsbalken bei Aufgaben; bewusst dezent
- **Aufgaben-Center**: lang laufende Operationen (Kopieren, Löschen, Hochladen) laufen als Aufgabe mit Fortschritt und Abbrechen

### Responsive Design

- **Desktop-Browser**: voller Desktop mit Fenstern und Widgets
- **Tablet**: Fenster werden großflächig dargestellt, Leiste reduziert, Touch-Gesten für Wischen zwischen Fenstern
- **Schmaler Browser / Mobil**: Einkomponentenansicht, Menü als Overlay, Dateiliste einspaltig
- **Eigene Apps** (DS file, Drive, Surveillance) ersetzen das Portal auf kleinen Geräten durch zugeschnittene Oberflächen
- **QuickConnect-Links** leiten auf die Mobilvariante weiter

### Zugänglichkeit

- **Tastatur**: Formulare, Listen und Dialoge per `Tab`/`Enter`/`Esc` bedienbar; Massenaktionen bleiben meist mausorientiert
- **Fokusanzeige**: aktives Feld und aktive Datei sind markiert
- **Screenreader**: Beschriftungen für Symbole und Dialoge in aktuellen DSM-Versionen verbessert, aber nicht flächendeckend
- **Farbunabhängigkeit**: Status zusätzlich mit Symbol und Text
- **Sprachen**: vollständige Lokalisierung, auch Deutsch
- **Zoom**: Browser-Zoom funktioniert, Fensterlayout passt sich an

### Performance

- **Index-basierte Suche**: Universal Search arbeitet gegen einen Index, nicht gegen Live-Verzeichnisläufe
- **Aufgaben statt Blockierung**: Kopier-/Löschvorgänge laufen asynchron mit Aufgabenliste
- **Verzögertes Nachladen**: große Ordner laden Abschnitt für Abschnitt
- **Ressourcenmonitor** zeigt, welches Paket das System belastet; Pakete lassen sich gezielt stoppen
- **Empfehlung**: Indizierung einschränken, Thumbnail-Erzeugung zeitsteuern, Protokoll-Aufbewahrung begrenzen

## Siehe auch

- [menu.md](menu.md) - Menüpunkte nach Rolle
- [features.md](features.md) - Pakete und Dienste
- [shortcuts.md](shortcuts.md) - Tastatursteuerung und Systembefehle
- [api.md](api.md) - `entry.cgi` und Sitzungsbehandlung
