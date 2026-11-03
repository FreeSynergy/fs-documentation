# Map View - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A map view shows interactive maps (Google Maps, Leaflet, OpenStreetMap).

- Showing a location
- Map view
- Geo data

## Examples

### Showing a location

```jsx
<MapView center={settings} onChange={action} />
```

### Map view

```jsx
<MapView center={settings} mapType="roadmap" />
```

### Geo data

```jsx
<MapView center={settings} interactive={true} />
```

## Notes

- Gestures: `drag`
