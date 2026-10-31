# OsmAnd - Struktur und UI/UX

## App-Layout

```
┌──────────────────────────────────┐
│ ⚙️-Statuszeile · Suche…          │
│                                  │
│      (Vollbildkarte, 3D/2D)      │
│          ⬤ Meine-Orte-Layer      │
│                                  │
│  [Navigation][Planen][Meine Orte]│  ← Hauptleiste unten
│  [OSM-Wiki][nearby][configure…]  │
└──────────────────────────────────┘
Seitenleisten: links (Downloads/Einstellungen),
rechts (Ebenen/Messung/Nacht) — als Chips am Rand
```

- Navigationsmodus: obere Abbiege-Kachel + untere Infozeile (Abstand/Zeit)

## UI/UX

- Funktionsdichte hoch; Kontextmenü (Langpress auf Karte) als Drehscheibe
- Kartenprofile (Standard/Ski/Topo…) schalten Stil + Profile gemeinsam

## Interaktionen

- **Gesten**: Doppelklick Zoom, Zwei-Finger-Rotation/Kippen (3D), Langpress = Kontextmenü (Ziel/Notiz)
- Punkte ziehen für Routenplanung; Track-Folge-Modus („Route folgen“)

## Responsive Design

- Handy-UI; Tablet-Layout; keine Desktop-Version (Desktop = OsmAnd? nein)

## Accessibility

- Sprachausgabe stark (blinde Navigation möglich); UI-Kontraste teils schwach (Dark-Menüs)

## Performance

- große Regionen (>1 GB) → Speicher beachten; Kachel-Cache-Aufbau kostet Startzeit
