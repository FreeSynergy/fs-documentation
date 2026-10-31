# draw.io - Struktur & UI/UX

## Übersicht

draw.io baut den Arbeitsplatz wie ein Desktop-Programm auf: Menüleiste oben, Formbibliothek links, Formatierungs-Panel rechts, Leinwand mit Seiten Reitern in der Mitte und unten. Alle Seitenteile sind einklappbar, die Leinwand bleibt stets der größte Bereich.

## Fenster-Struktur

### Standardansicht

```
┌──────────────────────────────────────────────────────────────────────┐
│  Datei  Bearbeiten  Ansicht  Anordnen  Extras  Hilfe   [Dateiname]   │
├───────────────┬──────────────────────────────────────────┬───────────┤
│ Suchfeld      │                                          │ Format    │
│ Formbibliothek│        Leinwand (1..n Seiten)            │ Panel     │
│ - General     │   [Formen, Kanten, orangefarbene         │ - Stil    │
│ - Arrows      │    Ausrichtungs-Linien]                  │ - Anordnen│
│ - BPMN / UML  │                                          │ - Optionen│
│ - AWS / Azure │                                          │           │
├───────────────┴──────────────────────────────────────────┴───────────┤
│  [Seite 1] [Seite 2] +      Zoom-Regler        Ansicht 100 %         │
└──────────────────────────────────────────────────────────────────────┘
```

### Bereichs-Tabelle

| Bereich | Position | Inhalt |
|---------|----------|--------|
| Menüleiste | oben | Datei, Bearbeiten, Ansicht, Anordnen, Extras, Hilfe |
| Titelfeld | oben rechts | Dateiname, Speicherort, Status (gespeichert/geändert) |
| Formbibliothek | links | Formsuche, Bibliotheks-Ordner, „Weitere Formen“ |
| Leinwand | Mitte | Seiten mit Raster, Linealen (optional), Ebenen |
| Format-Panel | rechts | Stil, Anordnung, Texte, Dokumentoptionen |
| Seitenleiste unten | unten | Seiten-Reiter, neues Blatt, Zoom-Regler |
| Dialoge | Overlay | Ebenen, Outline, Versionen, Realtime-Sync, Seiten-Dialog |

### Format-Panel (Reiter)

- **Stil**: Füllfarbe, Linienstil, Schriftfamilie/-größe, Kantenausführung
- **Anordnen**: Position und Größe numerisch, Drehung, Textausrichtung, Daten
- **Optionen**: Raster, Führungslinien, Hintergrund, Auto-Save (versionsabhängig)

### Dialog-Overlay (Beispiel Ebenen)

```
┌──────────────────────────────────────┐
│  Ebenen                        [✕]   │
├──────────────────────────────────────┤
│  Name        Sichtb.  Sperren        │
│  Hintergrund   Auge   Schloss        │
│  Objekte       Auge   Schloss        │
├──────────────────────────────────────┤
│  [Ebene hinzufügen]                  │
└──────────────────────────────────────┘
```

- Weitere Overlays: Outline, Versionen, Realtime-Sync, Seiten-Dialog, Stilvorlagen
- Dialoge sind modal über der Leinwand; die Leinwand bleibt im Hintergrund aktiv

## UI/UX

### Design-Prinzipien

- **Zweckmäßigkeit**: Panels und Menüs vor Eleganz, maximale Dichte an Funktionen
- **Alles benennbar**: Stile, Formen und XML bleiben für Nutzer einsichtig
- **Kein Onboarding**: Werkzeug für Anwendende, die Diagramme bereits können
- **konsistentes Konzept**: Rechtsklick-Menüs spiegeln die Menüpunkte der Leiste

### Farbschema und Themes

- **Standard**: hellgraue Bedienflächen, weiße Seiten, dunkle Linien
- **Dunkelmodus/Theme-System**: vorhanden, Bezeichnung und Umfang versionsabhängig
- **Formpalette**: voreingestellte Pastellfarben (Blau, Grün, Gelb, Rot) mit Standard-Stilvorgaben
- **Seitenhintergrund**: je Seite wählbar (Extras > Seiten)

### Typography

- **Oberfläche**: kompakte Systemschrift für Menüs, Panels und Statuszeile
- **Zelltexte**: Standardschrift groß wählbar, HTML-artige Formatierung (fett, kursiv, Umbrüche)
- **Mathematik**: LaTeX-Rendering für Zelltexte aktivierbar (Extras-Menü, versionsabhängig)
- **Schriftgrößen** im Stil-Panel numerisch einstellbar, Skalierung über Zoom

### Interaktionen

- **Verbindungspunkte**: Ein-/Ausgänge erscheinen blau beim Überfahren einer Form
- **Führungslinien**: orange Linien zeigen Ausrichtung und gleiche Abstände
- **Auswahl**: gestrichelter Rahmen mit Quadraten an Ecken und Kanten
- **Ziehen und Andocken**: Kanten folgen Formen, Container schlucken Formen beim Hineinziehen
- **Formatübertragung**: Stil mit kopieren/einfügen auf andere Formen übertragen
- **Animationen**: praktisch keine — redraw erfolgt sofort; nur Menüs blenden weich ein

### Responsive Verhalten

- **Desktop**: voll ausgebaute Panels und Menüs
- **Tablet**: Touch-Zeichnen und -Bewegen möglich, Panel-Bedienung dichter
- **Smartphone**: Web-App nutzbar, aber für feine Diagrammarbeit gedacht; kein natives Mobile-Interface

## Zugänglichkeit

- **Tastatur**: Menüpunkte und Zell-Operationen über Shortcuts (siehe [shortcuts.md](shortcuts.md))
- **Screenreader**: eingeschränkt — Diagramme sind gezeichnete Flächen, XML nur indirekt barrierefrei
- **Zoom**: Browser-Zoom und App-Zoom kombinierbar für größere Darstellung
- **Kontrast**: Standard-Stile sind kontrastreich; Farben frei anpassbar

## Performance

- **Komprimierte Dateien**: `.drawio`-Dateien intern deflate-komprimiert (abschaltbar für lesbare XMLs)
- **Seiten-Rendering**: große Werke werden seitweise gezeichnet; „Umblatten“ hält den Ausschnitt klein
- **Formbibliotheken**: werden lazy geladen; wenige aktive Sets halten das Interface schnell
- **Realtime-Sync**: überträgt Bearbeitungsschritte der Cloud-Datei; sehr große Seiten können verzögern
- **Plugins**: eigene Erweiterungen sparsam einsetzen, sie laufen im UI-Thread mit
