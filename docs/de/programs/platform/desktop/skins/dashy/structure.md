# Dashy - Struktur & UI/UX

## Übersicht

Dashy zeigt eine Kopfzeile, darunter die Suchleiste, dann die Sektionen mit Kacheln und optionalen Widgets, am Ende eine Fußzeile. Bearbeitungs- und Einstellungsflächen legen sich als Seitenteil oder Dialog über die Ansicht. Drei Ansichtsformen (Startseite, Minimal, Arbeitsbereich) ändern dieselbe Struktur in Dichte und Umfang.

## Fenster-Struktur

### Standardansicht

```
┌──────────────────────────────────────────────────────────────────────┐
│  Kopfzeile: Titel/Untertitel   Seiten-Menü | Launchpad | Zahnrad | Konto │
├──────────────────────────────────────────────────────────────────────┤
│                [ Suchleiste ]         (Tippen filtert sofort)         │
├──────────────────────────────────────────────────────────────────────┤
│  Sektion: Medien                          Sektion: Netzwerk           │
│  ┌─────────⊙──┐ ┌─────────⊙──┐          ┌─────────⊙──┐              │
│  │ Icon Titel │ │ Icon Titel │          │ Icon Titel │   ⊙ = Status  │
│  │ Beschreibung│ │ Beschreibung│         │ Beschreibung│              │
│  └────────────┘ └────────────┘          └────────────┘              │
│  ┌────────────┐ ┌────────────┐          ┌────────────┐              │
│  │ Widget Uhr │ │ Widget RSS │          │            │              │
│  └────────────┘ └────────────┘          └────────────┘              │
├──────────────────────────────────────────────────────────────────────┤
│  Fußzeile                                                            │
└──────────────────────────────────────────────────────────────────────┘
```

### Bearbeitungsmodus

```
┌──────────────────────────────────────────────────────────────────────┐
│  Modus-Hinweis: Bearbeiten aktiv        Speichern | Verwerfen | ✕     │
├──────────────────────────────────────────────────────────────────────┤
│  ┌─[⋮]──────────────[✎][🗑]─┐      ┌──────────────────────────────┐  │
│  │ Kachel (ziehen zum        │      │ Sektion (Griffzone)          │  │
│  │ Verschieben im Raster)    │      │ Kachel hinzufügen            │  │
│  └───────────────────────────┘      └──────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────┘
```

### Kachel-Dialog

```
┌──────────────────────────────────────────┐
│  Kachel bearbeiten              [✕]      │
├──────────────────────────────────────────┤
│  Titel · URL · Beschreibung · Symbol     │
│  Öffnungsart · Farben · Tags · Hotkey    │
│  Statusprüfung · Anzeigeoptionen         │
├──────────────────────────────────────────┤
│           [Abbrechen]  [Speichern]       │
└──────────────────────────────────────────┘
```

## Bereiche

| Bereich | Position | Inhalt |
|---------|----------|--------|
| Kopfzeile | Oben | Titel, Logo, Seiten-Menü, Launchpad, Einstellungen, Konto |
| Suchleiste | Unter der Kopfzeile | Filterfeld, Websuche, Kurzkommandos |
| Sektionen | Mitte | Überschrift, Kachelraster, Widgets |
| Kachel | In Sektionen | Symbol, Titel, Beschreibung, Statuspunkt |
| Statuspunkt | Rechts oben an der Kachel | erreichbar / nicht erreichbar / prüft / Fehler |
| Widget-Fläche | In Sektionen oder als Spalte | Uhr, Wetter, RSS, eigene Widgets |
| Fußzeile | Unten | Hinweis, Quellenangabe |
| Einstellungspanel | Overlay/Seitenteil | interaktiver Editor, Theme, Import/Export |
| Login | Eigene Ansicht | Anmeldung bei konfigurierter Authentifizierung |

## UI/UX

### Design-Prinzipien

- **Sofort handeln**: Tippen startet die Suche, ohne Umweg über ein Feld
- **Information am Objekt**: Statuspunkt und Beschreibung gehören zur Kachel
- **Wenig Chrome, viele Optionen**: Standardansicht schlicht, Details über Menüs und Konfiguration
- **Eine Quelle**: Was die Datei beschreibt, ist die Oberfläche — kein verborgener Zustand

### Farbschema und Themes

- **Eingebaute Schemata** in großer Auswahl, hell und dunkel, plus Theme-Editor
- **CSS-Variablen** für eigene Farben, Hintergründe und Schriftarten
- **Je Sektion und Kachel** eigene Farben und Dichte möglich
- **Automatischer Wechsel** zwischen hellem und dunklem Schema nach Systemeinstellung konfigurierbar

### Interaktionen

- **Hover**: Kacheln heben sich, Beschreibung wird betont
- **Rechtsklick**: Kontextmenü mit allen Öffnungsarten
- **Drag & Drop**: nur im Bearbeitungsmodus, Kacheln und Sektionen im Raster
- **Tastatur**: Tippen, `Tab`, Pfeiltasten, `Enter`, `Alt+Enter`, `Ctrl+Enter`, `Esc`
- **Animationen**: sanfte Übergänge beim Filtern und Umschalten der Ansicht; Statuspunkte wechseln die Farbe
- **Ladezustände**: Statuspunkte zeigen „prüft“, Widgets zeigen Platzhalter

### Responsive Design

- **Desktop**: mehrspaltige Sektionen, viele Kacheln pro Reihe
- **Tablet**: weniger Spalten, Widgets stapeln
- **Mobil**: einspaltig, große Touch-Ziele, Kopfzeile reduziert
- **Konfigurierbare Spaltenanzahl** pro Sektion; Raster bricht automatisch um

### Zugänglichkeit

- **Tastaturbedienung**: Suche, Navigation und Starten komplett ohne Maus möglich
- **Fokusanzeige**: fokussierte Kacheln sind sichtbar markiert
- **Screenreader**: Sektionen als Überschriften, Kacheln als Links mit Titel und Beschreibung
- **Farbunabhängigkeit**: Status zusätzlich über Form und Text erkennbar (Theme-abhängig)
- **Zoom**: Seiten-Zoom ohne Abschneiden

### Performance

- **Statisch im Kern**: Die Anwendung besteht aus statischen Dateien, die Auslieferung ist schnell
- **Serverkosten**: Statusprüfungen und API-Aufrufe laufen über den Node-Server und skalieren mit der Anzahl der Kacheln
- **Config-Größe**: Die Datei ist größenbegrenzt; sehr große Sammlungen gehören auf Unterseiten verteilt
- **Empfehlung**: Prüfintervalle moderat setzen, nicht benötigte Widgets entfernen, Unterseiten für lange Listen nutzen

## Siehe auch

- [menu.md](menu.md) - Kopfzeile, Panels, Kontextmenüs
- [features.md](features.md) - Kacheln, Status, Widgets, Themes
- [api.md](api.md) - REST-API und Authentifizierung
- [shortcuts.md](shortcuts.md) - Tastatursteuerung
