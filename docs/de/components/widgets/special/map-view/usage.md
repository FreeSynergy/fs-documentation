# Map View - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und Blinc
    wechselt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Eine Kartenansicht zeigt interaktive Karten (Google Maps, Leaflet, OpenStreetMap).

- Anzeige eines Ortes
- Kartenansicht
- Geodaten

## Beispiele

### Anzeige eines Ortes

```jsx
<MapView center={settings} onChange={action} />
```

### Kartenansicht

```jsx
<MapView center={settings} mapType="roadmap" />
```

### Geodaten

```jsx
<MapView center={settings} interactive={true} />
```

## Hinweise

- Gesten: `drag`
