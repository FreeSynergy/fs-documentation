# Homer - Struktur & UI/UX

## Übersicht

Homer rendert eine einzige, vertikal aufgebaute Seite. Oben ein schmaler Kopfbereich, darunter ein Raster aus Spalten; in jeder Spalte stehen Gruppenüberschriften mit Kacheln. Änderungen an der Struktur entstehen ausschließlich in der Konfigurationsdatei.

## Fenster-Struktur

### Standardansicht

```
┌──────────────────────────────────────────────────────────────────────┐
│  Logo  Titel · Untertitel                     [Icon-Link] [Icon-Link] │
├──────────────────────────────────────────────────────────────────────┤
│                 [ Suchfeld ]                                         │
├──────────────────┬──────────────────┬────────────────────────────────┤
│  Gruppe: Medien  │  Gruppe: Netz    │  Gruppe: Werkzeuge             │
│  ┌────┐ ┌────┐   │  ┌────┐ ┌────┐   │  ┌────┐ ┌────┐                │
│  │Icon│ │Icon│   │  │Icon│ │Icon│   │  │Icon│ │Icon│                │
│  │Name│ │Name│   │  │Name│ │Name│   │  │Name│ │Name│                │
│  └────┘ └────┘   │  └────┘ └────┘   │  └────┘ └────┘                │
│  ┌────┐ ┌────┐   │  ┌────┐          │                               │
│  │Icon│ │Icon│   │  │Icon│          │  (Reihenfolge folgt der Datei)│
│  └────┘ └────┘   │  └────┘          │                               │
├──────────────────┴──────────────────┴────────────────────────────────┤
│  Fußzeile                                                            │
└──────────────────────────────────────────────────────────────────────┘
```

### Gefilterte Ansicht (Suchtext aktiv)

```
┌──────────────────────────────────────────────────────────────────────┐
│  Kopfzeile                                     [Icon-Links]          │
├──────────────────────────────────────────────────────────────────────┤
│                 [ down ]   ← Suchtext                                │
├──────────────────────────────────────────────────────────────────────┤
│  Gruppe: Netz                                                        │
│  ┌────────┐ ┌────────┐                                              │
│  │Down…   │ │Down…   │   ← nur passende Kacheln bleiben sichtbar    │
│  └────────┘ └────────┘                                              │
└──────────────────────────────────────────────────────────────────────┘
```

### Mobile Ansicht

```
┌────────────────────────┐
│ Logo Titel             │
│ [Suchfeld]             │
│ Gruppe: Medien         │
│ ┌──────┐ ┌──────┐      │
│ │Kachel│ │Kachel│      │
│ └──────┘ └──────┘      │
│ Gruppe: Netz           │
│ ┌──────┐               │
│ │Kachel│               │
│ └──────┘               │
└────────────────────────┘
```

## Bereiche

| Bereich | Position | Inhalt |
|---------|----------|--------|
| Kopfzeile | Oben | Logo, Titel, Untertitel, Icon-Links rechts |
| Suchfeld | Unter der Kopfzeile | Filterfeld, wenn `search` aktiv ist |
| Spalten | Mitte | `columns` Spalten mit Gruppen |
| Gruppen | In Spalten | Überschrift, optionales Logo/Symbol, Kacheln |
| Kachel | In Gruppen | Icon, Name, optional Tag |
| Fußzeile | Unten | Freitext |
| Meldung | Overlay/Zeile | Lade-, Fehler- oder Offline-Hinweis |

## UI/UX

### Design-Prinzipien

- **Lesbarkeit vor Dichte**: große Symbole, kurzer Name, viel Weißraum
- **Struktur aus der Datei**: keine Bedienelemente, die Struktur verändern könnten
- **Ein Bildschirm, kein Menü**: alles ist sichtbar, Suche ersetzt Navigation
- **Vorhersagbarkeit**: Positionen ändern sich nur bei Fenstergröße oder Dateiänderung

### Farbschema und Themes

- **Hell und Dunkel** über den `theme`-Eintrag, automatischer Wechsel nach Systemeinstellung möglich
- **Eigenes Stylesheet** (`stylesheet`) für Farben, Schrift, Abstände
- **CSS-Variablen** überschreiben, ohne mitgelieferte Dateien zu bearbeiten
- **Kachelfarben** sind nicht pro Kachel konfigurierbar; Akzente kommen aus dem Theme oder eigenen CSS-Regeln

### Interaktionen

- **Klick**: öffnet den Link im eingestellten Zielrahmen
- **Hover**: leichte Hervorhebung, Tooltip beim Icon-Link
- **Tippen im Suchfeld**: filtert sofort, ohne Neuladen
- **Rechtsklick**: zeigt das Browser-Menü, kein eigenes Kontextmenü
- **Kein Drag & Drop**: Verschieben und Vergrößern von Kacheln ist nicht möglich
- **Keine Animationen**: Übergänge beschränken sich auf Hover-Effekte

### Responsive Design

- **Desktop**: mehrere Spalten, Kacheln nebeneinander
- **Tablet**: Spaltenanzahl reduziert sich, Gruppen stapeln
- **Mobil**: einspaltige Ansicht, große Touch-Ziele
- **Spaltensteuerung**: über `columns` vorgeben; ein eigenes Mobil-Layout wie bei Homarr existiert nicht
- **Breite Fenster**: Kacheln skalieren mit, der Inhalt bleibt zentriert

### Zugänglichkeit

- **Tastatur**: Kacheln sind echte Links und per `Tab` erreichbar, `Enter` öffnet
- **Screenreader**: Überschriften strukturieren Gruppen, `aria`-Merkmale für das Suchfeld (je nach Version)
- **Suchfeld**: beschriftet; Filterung ändert den DOM, was Hilfstechnologien mitteilen
- **Zoom**: Browser-Zoom ohne Abschneiden; auf kleinen Screens bleiben Kacheln lesbar
- **Einschränkung**: Farbakzente tragen keine Information, daher bleibt die Seite farbunabhängig bedienbar

### Performance

- **Kein Server**: die Seite besteht aus statischen Dateien, Antwortzeiten entstehen durch Webserver und CDN
- **Konfiguration wird geladen**: die YAML-Datei ist ein zusätzlicher Request und wird ohne Auth ausgeliefert
- **Sehr geringe Datenmenge**: keine Charts, keine Dauerschleifen, keine Polling-Intervalle
- **Empfehlung**: Config und Icons cachen (Cache-Header), große Icon-Ordner schlank halten, optional HTTP/2 oder CDN

## Siehe auch

- [menu.md](menu.md) - Bedienelemente und Betriebsrollen
- [features.md](features.md) - Kacheln, Suche, Themes
- [api.md](api.md) - `config.yml` im Detail
- [shortcuts.md](shortcuts.md) - Tastatur und Browser-Tasten
