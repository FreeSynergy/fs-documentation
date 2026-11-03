# OBS Studio - Struktur und UI/UX

## Hauptfenster (Standard-Layout)

```
┌──────────────────────────────────────────────────────────────────────┐
│ Datei  Ansicht  Bearbeiten  Einstellungen  Hilfe                     │
├──────────────┬────────────────────────────────┬──────────────────────┤
│ Szenen       │        Vorschau (Ausgang)      │ Quellen              │
│ ▸ Ordner     │   ┌──────────────────────┐     │ ▸ Bildschirm         │
│   ▸ Intro    │   │   rote Umrandung =   │     │ ▸ Kamera             │
│ ▸ Talk       │   │   aktive Szene       │     │ ▸ Browserquelle      │
│--------------│   └──────────────────────┘     │----------------------│
│ Übergang     │  FPS | CPU | Verluste (Status) │ Audio-Mischer        │
├──────────────┴────────────────────────────────┴──────────────────────┤
│ Steuerungen: Start Streaming | Start Aufnahme | Studio-Modus | Rekorde│
└──────────────────────────────────────────────────────────────────────┘
```

- Rote Umrandung = aktiver Ausgang, grüne Umrandung = Studio-Vorschau
- Alle Bereiche sind Docks und frei anordbar (Ansicht-Menü)

## UI/UX

- Standard-Dark-Theme, Oberflächen-Skalierung für 4K konfigurierbar
- Statusleiste unten rechts: FPS, verlorene Frames, CPU-Auslastung, Bandbreite
- Kontextmenüs statt Buttons für die meisten Quellenaktionen

## Interaktionen

- **Drag & Drop**: Dateien in die Szenenliste (neue Szene) oder in die Quellenliste (neue Quelle)
- **Randpunkte ziehen** in der Vorschau zum Transformieren, `Alt`+Ziehen für Zuschneiden
- **Schnellwechsel** per Hotkey oder Szenen-Klick
- **Studio-Modus**: Vorschau vorbereiten, dann „Übergang ausführen“

## Responsive Design

| Plattform | Verhalten |
|-----------|-----------|
| Desktop (Win/macOS/Linux) | volles Dock-Layout, mehrmoniturfähig |
| 4K/Hidpi | UI-Skalierung 100–300 % |
| Mobil | ❌ kein offizieller Client (Fernbedienung über obs-websocket-Apps) |

## Accessibility

- Tastatursteuerung über Hotkeys und Menüfoki; Screenreader nur eingeschränkt (Qt-Docks) (⚠)
- Vorschau ohne Farbcodierung als Zustand: Statusleiste liefert Textwerte
- Hotkeys vollständig konfigurierbar, Belegungskonflikt-Warnung integriert

## Performance

- Encoding-Auslastung in der Statusleiste sichtbar, Verlustzähler für Streams
- Empfehlung: getrennte Aufnahme-/Streaming-Encoder, NVENC/QSV für Lastverteilung
