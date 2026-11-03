# Organic Maps - Struktur und UI/UX

## App-Layout

```
┌──────────────────────────────────┐
│        (Vollbildkarte, 3D)       │
│              ⬤⬤ Favoriten        │
│  Schicht◧  Kompass⌖              │
├──────────────────────────────────┤
│ [🔍 Suche oder Adresse …]        │
│ Kategorien-Grid (wenn nichts     │
│ ausgewählt)                      │
│ Reiter: Karte | Gespeichert | Navigation │
└──────────────────────────────────┘
POI-Details als Sheet von unten (wischbar)
```

## UI/UX

- Apple-ähnliche Klarheit: ein Sheet, ein Suchfeld, Icons mit Labels
- Kategorien in bunten Kacheln (offline-POI-Klassifikation)

## Interaktionen

- Blättern/Zoomen/Zwei-Finger-Drehen; Sheet-Hochziehen für POI-Details
- „Route“ = Zwei-Tasten-Workflow (Start/Ziel via Karte/Suche)

## Responsive Design

- Handy + Tablet; Desktop-Vorschau (Projektfortschritt beachten)

## Accessibility

- VoiceOver/TalkBack-Grundlagen; Sprachführung in Navigation

## Performance

- Regionen-Downloads gestaffelt; Suchergebnisse offline <1 s
