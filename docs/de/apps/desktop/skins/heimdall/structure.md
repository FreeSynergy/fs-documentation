# Heimdall - Struktur & UI/UX

## Übersicht

Die Heimdall-Oberfläche ist eine vertikal gestapelte Seite: oben schmale Kopfzeile, darunter die Panels untereinander. In den Panels liegen quadratische Kacheln in einer Reihe oder mehreren Reihen. Bearbeitungs- und Einstellungsdialoge erscheinen als Überlagerung.

## Fenster-Struktur

### Startseite

```
┌──────────────────────────────────────────────────────────────────────┐
│  Kopfzeile: Titel/Logo                     Konto-Menü | Einstellungen │
├──────────────────────────────────────────────────────────────────────┤
│  Suchbereich: Suchfeld | Suchmaschine                                 │
├──────────────────────────────────────────────────────────────────────┤
│  App-Panel                                                             │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐              │
│  │ Icon   │ │ Icon   │ │ Icon   │ │ Icon   │ │ Icon   │              │
│  │ Titel  │ │ Titel  │ │ Titel  │ │ Titel  │ │ Titel  │              │
│  │ Wert   │ │ Wert   │ │        │ │        │ │        │  (Enhanced)  │
│  └────────┘ └────────┘ └────────┘ └────────┘ └────────┘              │
├──────────────────────────────────────────────────────────────────────┤
│  Statistik-Bereich: CPU │ RAM │ Disk │ Netz  (Zahlen + Mini-Diagramm) │
├──────────────────────────────────────────────────────────────────────┤
│  Hinweis-/Supportbereich (optional) · Fußzeile                        │
└──────────────────────────────────────────────────────────────────────┘
```

### Layout-Bearbeitung

```
┌──────────────────────────────────────────────────────────────────────┐
│  Modus-Hinweis: Layout bearbeiten | Speichern | Verwerfen             │
├───────────────────────────┬──────────────────────────────────────────┤
│  Panel A (Griffzone)      │  Panel B                                 │
│  [⋮] verschieben umbrechen│  [⋮] ausblenden löschen                  │
│  ┌────┐┌────┐             │  ┌────┐┌────┐                           │
│  │Kachel││Kachel│  ziehen  │  │Kachel││Kachel│                       │
│  └────┘└────┘             │  └────┘└────┘                           │
└───────────────────────────┴──────────────────────────────────────────┘
```

### Einstellungs-Dialog

```
┌────────────────────────────────────────────┐
│  App bearbeiten                    [✕]     │
├────────────────────────────────────────────┤
│  Titel · URL · Icon · Farbe                │
│  Enhanced App · Ziel-URL · API-Key         │
│  [ ] in neuem Tab öffnen                   │
├────────────────────────────────────────────┤
│            [Abbrechen]  [Speichern]        │
└────────────────────────────────────────────┘
```

## Bereiche

| Bereich | Position | Inhalt |
|---------|----------|--------|
| Kopfzeile | Oben | Titel/Logo, Konto-Menü, Einstellungen |
| Suchbereich | Oben, unter Kopfzeile | Suchfeld, Anbieterauswahl |
| App-Panels | Mitte | Kacheln mit Icon, Titel, optional Live-Werten |
| Statistik-Bereich | Mitte/Unten | CPU, RAM, Festplatte, Netzwerk |
| Hinweisbereich | Unten | Projektmeldungen, Versionshinweise |
| Fußzeile | Unten | Versionsstand, Projekthinweis |
| Dialoge | Overlay | App-Bearbeitung, Icon-Auswahl, Kontoeinstellungen |

## UI/UX

### Design-Prinzipien

- **Kachel zuerst**: große Icons, kurze Titel, wenig Rahmen
- **Keine Verschachtelung**: keine eingebetteten Frames, jede Kachel ist ein Link
- **Vertikale Reihenfolge statt Raster**: Panels stapeln, statt frei zu positionieren
- **Wenige Bedienelemente**: Verwaltung erscheint überwiegend beim Überfahren oder in den Einstellungen

### Farbschema und Themes

- **Standard** ist ein dunkles Grundschema mit hellen Kacheln
- **Kachelfarben** frei wählbar, dadurch farbliche Gruppierung möglich
- **Eigenes CSS**: eigene Stylesheets einbinden; ein Theme-Katalog fehlt
- **Kontrast** bleibt durch kräftige Flächen und weiße Beschriftung gut lesbar

### Interaktionen

- **Hover**: Kacheln hellen auf, Bearbeitungssymbole erscheinen
- **Drag & Drop**: Kacheln innerhalb und zwischen Panels ziehen, Panels umsortieren
- **Klick**: öffnet die Ziel-URL; bei Enhanced Apps zusätzlich Wert-Details in der Kachel
- **Formulare**: Dialoge mit konventionellen Feldern und Speichern/Abbrechen
- **Animationen**: sparsam, im Wesentlichen Übergänge beim Sortieren und Ein-/Ausblenden

### Responsive Design

- **Desktop**: mehrere Kacheln pro Reihe, Panels nebeneinander nach dem Umbrechen
- **Tablet**: weniger Kacheln pro Reihe, Statistikfelder stapeln
- **Mobil**: einspaltige Ansicht, große Kacheln, Bedienelemente als Touch-Ziele
- **Layout pro Konto**: mobile Darstellung folgt dem gespeicherten Layout, eigene Mobil-Ansicht gibt es nicht

### Zugänglichkeit

- **Tastatur**: Links, Formulare und Dialoge per `Tab` erreichbar, `Esc` schließt Dialoge
- **Screenreader**: semantische Listen für Panels, Alt-Texte für Icon-Bilder
- **Zoom**: Seiten-Zoom ohne abgeschnittene Kacheln
- **Einschränkung**: Drag & Drop ist nicht alternativ per Tastatur bedienbar; Umordnung erfordert Maus oder Touch

### Performance

- **Serverseitig**: PHP rendert die Seite, Statistikwerte und Enhanced Apps werden bei Bedarf abgefragt
- **Verzögerung**: nicht erreichbare Dienste verlängern den Seitenaufbau, da die Abfragen serverseitig laufen
- **Caching**: Browser-Caching für statische Dateien; Application-Cache über Laravel-Mechanismen
- **Empfehlung**: Anzahl der Enhanced Apps begrenzen, Datenbank-Volume auf schneller Platte, PHP-Auszeitzeiten bei vielen Abfragen erhöhen

## Siehe auch

- [menu.md](menu.md) - Menüpunkte nach Rolle
- [features.md](features.md) - Apps, Enhanced Apps, Panels
- [shortcuts.md](shortcuts.md) - Tastatursteuerung
- [api.md](api.md) - Routen und Schlüsselverwaltung
