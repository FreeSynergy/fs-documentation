# Geodaten – Beispiele

Feldnamen ausschließlich aus den ✅ geprüften Standards (RFC 7946, RFC 5870, RFC 9553 §2.5.1).

## 1. Ort als GeoJSON-`Feature` (kanonischer Speicher)

```json
{
  "type": "Feature",
  "id": "01HTZK9F2W7P3D8S5V1BQ6XH4M",
  "geometry": {
    "type": "Point",
    "coordinates": [13.4050, 52.5200]
  },
  "properties": {
    "name": "Rathaus Berlin",
    "category": "civic"
  }
}
```

## 2. `FeatureCollection` als API-Antwort auf eine BBox-Abfrage

```json
{
  "type": "FeatureCollection",
  "features": [
    { "type": "Feature", "geometry": { "type": "Point", "coordinates": [13.4050, 52.5200] }, "properties": { "name": "Rathaus Berlin" } },
    { "type": "Feature", "geometry": { "type": "Point", "coordinates": [13.4340, 52.5170] }, "properties": { "name": "Hackescher Markt" } }
  ]
}
```

## 3. Postadresse als JSContact-`Address` (Komponenten, kein Freitext)

```json
{
  "home": {
    "components": [
      { "kind": "street", "value": "Torstraße 1" },
      { "kind": "locality", "value": "Berlin" },
      { "kind": "region", "value": "Berlin" },
      { "kind": "postcode", "value": "10115" },
      { "kind": "country", "value": "DE" }
    ],
    "coordinates": "geo:52.5278,13.3978"
  }
}
```

## 4. Adresse in einem anderen Land — gleiches Modell

```json
{
  "work": {
    "components": [
      { "kind": "street", "value": "Calle de Alcalá 12" },
      { "kind": "locality", "value": "Madrid" },
      { "kind": "region", "value": "Comunidad de Madrid" },
      { "kind": "postcode", "value": "28014" },
      { "kind": "country", "value": "ES" }
    ]
  }
}
```

## 5. Verknüpfung von zwei Domänen (Termin → Ort)

Ein Termin in [events/](../events/index.md) speichert nur die Referenz:

```json
{
  "locations": {
    "loc1": { "name": "Rathaus Berlin", "link": "https://<instanz>/geodata/01HTZK9F2W7P3D8S5V1BQ6XH4M" }
  }
}
```
