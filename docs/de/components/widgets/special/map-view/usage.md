# Map View (Kartenansicht) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Map View zeigt interaktive Karten an (Google Maps, Leaflet, OpenStreetMap).

- Standort-Anzeige
- Kartenansicht
- Geo-Daten

## Beispiele

### Standort-Anzeige

```jsx
<MapView center={einstellungen} onChange={aktion} />
```

### Kartenansicht

```jsx
<MapView center={einstellungen} mapType="roadmap" />
```

### Geo-Daten

```jsx
<MapView center={einstellungen} interactive={true} />
```

## Hinweise

- Gesten: `drag`
