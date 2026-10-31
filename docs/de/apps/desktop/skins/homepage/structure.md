# Homepage - Struktur & UI/UX

## Übersicht

Homepage rendert eine einzige Seite: Kopfzeile, Informations-Widgets, darunter die Dienstgruppen als Kachelraster, am Ende die Fußzeile. Es gibt keine Dialoge, keine Navigation zwischen Ansichten und keine Seitenleiste. Was wie ein Layout-Editor aussieht, ist in Wirklichkeit eine YAML-Angabe.

## Fenster-Struktur

### Standardseite

```
┌──────────────────────────────────────────────────────────────────────┐
│  Kopfzeile: Begrüßung · Datum/Uhrzeit · Suchleiste · Lesezeichen     │
├──────────────────────────────────────────────────────────────────────┤
│  Info-Widgets links          │        Info-Widgets rechts           │
│  ├ Wetter (openweathermap)   │  ├ Ressourcen (CPU/RAM/Platte)       │
│  ├ Suchleiste (Provider)     │  ├ Aktien (stocks)                   │
│  └ Kubernetes-Status         │  └ Glances / Search                  │
├──────────────────────────────────────────────────────────────────────┤
│  Gruppe "Medien"                                                     │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                 │
│  │ Jellyfin     │ │ Sonarr       │ │ qBittorrent  │  ← Kacheln mit  │
│  │ Icon · Name  │ │ 3 Requests   │ │ ↑ 2,4 MB/s   │    Service-     │
│  │ Widget-Zeile │ │ Widget-Zeile │ │ Widget-Zeile │    Werten       │
│  └──────────────┘ └──────────────┘ └──────────────┘                 │
│  Gruppe "Netzwerk"                                                   │
│  ┌──────────────┐ ┌──────────────┐                                  │
│  │ UniFi        │ │ Pi-hole      │                                  │
│  └──────────────┘ └──────────────┘                                  │
├──────────────────────────────────────────────────────────────────────┤
│  Fußzeile (footer)                                    Theme-Wechsel  │
└──────────────────────────────────────────────────────────────────────┘
```

### Mobile Ansicht

```
┌────────────────────────────┐
│  Kopfzeile (kompakt)       │
│  Info-Widgets (gestapelt)  │
│  Gruppe 1                  │
│  ┌────────────────────┐    │
│  │ Kachel (volle      │    │
│  │ Breite)            │    │
│  └────────────────────┘    │
│  Gruppe 2 …                │
└────────────────────────────┘
```

## Bereiche

| Bereich | Position | Inhalt | Konfiguration |
|---------|----------|--------|---------------|
| Kopfzeile | Oben | Titel, Datum, Suchleiste, Lesezeichen | `settings.yaml`, `bookmarks.yaml` |
| Info-Widgets | Oben links/rechts | Wetter, Ressourcen, Aktien, Status | `widgets.yaml` |
| Dienstgruppen | Mitte | Kacheln mit Links und Service-Widgets | `services.yaml` |
| Kachel | Im Raster | Icon, Name, Beschreibung, Widget-Zeilen | `services.yaml` |
| Fußzeile | Unten | Text, Hinweis | `settings.yaml` |
| Theme-Fläche | Gesamte Seite | Hintergrundbild, Farbton, Deckkraft | `settings.yaml`, `custom_css.css` |
| Log / Protokoll | Container-Log | YAML- und Verbindungsfehler | nicht in der UI sichtbar |

## UI/UX

### Design-Prinzipien

- **Übersicht vor Bedienung**: Seite dient dem Ablesen, nicht dem Bearbeiten
- **Dichte Information**: kleine Zahlenzeilen statt großer Diagramme
- **Ein Raster, keine Ebenen**: keine Overlays, Tabs oder Dialoge
- **Vorhersagbarkeit**: Position und Größe der Kacheln stehen in der Konfiguration, nicht im Browser

### Farbschema und Themes

- **Hell, dunkel und Systemeinstellung** über `theme` in `settings.yaml`
- **Akzentfarbe** über `color` (Tailwind-Farbnamen), Hintergrund über `background` oder `image`
- **Deckkraft/Blur** der Kacheln über `opacity` und `style`
- **Eigenes CSS** (`custom_css.css`) für Feinschliff; Klassen an Kacheln über `class`
- **Hintergrundbilder** lokal im Config-Ordner oder per URL; Skalierung und Verlauf über CSS

### Interaktionen

- **Klick auf Kachel**: öffnet `href` im eingestellten Ziel (`launch: new_tab` oder gleicher Tab)
- **Suchleiste**: Text eingeben, `Enter` öffnet die Ergebnisseite des Providers; Vorschläge erscheinen als Dropdown
- **Hover**: leichte Hervorhebung der Kachel, bei manchen Widgets zusätzliche Werte
- **Aktualisierung**: Daten werden in Intervallen nachgeladen (SWR), kein manuelles Neuladen nötig
- **Animationen**: bewusst minimal – Fade-Übergänge beim Nachladen, keine Umsortier-Animationen
- **Rechtsklick / Drag & Drop**: nicht vorhanden

### Responsive Design

- **Desktop**: mehrspaltiges Raster, Info-Widgets links und rechts
- **Tablet**: reduzierte Spaltenzahl, Info-Widgets rücken untereinander
- **Mobil**: einspaltige Stapelung, Kopfzeile kompakt, Suchleiste vollbreit
- **Layout-Angaben** in `settings.yaml` gelten je Endgerät nur begrenzt; mobil dominiert die Browserbreite

### Zugänglichkeit

- **Tastatur**: Links und Suchfeld sind mit `Tab` erreichbar, `Enter` löst aus
- **Screenreader**: Kacheln sind einfache Linkstrukturen mit Text; Widget-Zahlen werden als Text ausgegeben
- **Kontrast**: Themes mit ausreichendem Kontrast; Hintergrundbilder können den Kontrast senken – bei Bedarf `opacity` erhöhen
- **Zoom**: Browser-Zoom funktioniert ohne abgeschnittene Bereiche, weil die Seite fließend ist
- **Sprache**: Oberfläche übersetzt (`language`), Zahlenformate folgen der Sprache

### Performance

- **Statisches Rendering**: HTML kommt serverseitig fertig vom Next.js-Prozess
- **Proxy-Caching**: Antworten der Widget-Abfragen werden kurzzeitig im Prozess gecacht (`memory-cache`), identische Abfragen bündeln sich
- **Abfrageintervalle**: Widgets fragen in Minutenabständen, nicht permanent; zu kurze Intervalle belasten die Ziel-Dienste
- **Träge Dienste** bremsen nur ihre eigene Kachel: sie zeigt Lade- oder Fehlerzustand
- **Empfehlung**: nicht benötigte Service-Widgets entfernen, Docker-Erkennung auf benötigte Container begrenzen

## Siehe auch

- [menu.md](menu.md) - Bereiche und Rollen
- [features.md](features.md) - Widgets und Konfiguration
- [shortcuts.md](shortcuts.md) - Tastatursteuerung
- [api.md](api.md) - Datenquellen und Proxy-Routen
