# Geodaten – Technische Erklärung

## Speicherperspektive

- **Tabelle `location`** für eigenständige Orte (Karten-Features): eine Zeile pro GeoJSON-`Feature`; kanonischer Payload = Feature-JSON (Beschluss 4). Spalten herausgezogen: `id` (ULID), `geometry_type`, `bbox` (Index), `created_at`, `updated_at`.
- **Adressen sind keine eigene Tabelle**, solange sie zu einer Card gehören: sie bleiben im JSON der Card in [people/](../people/index.md) (`addresses`-Map mit Komponenten). Diese Domäne definiert nur die **Komponentennamen und Validierung**.

## Schlüssel und Verknüpfungen

- Extern: `https://<instanz>/geodata/<ulid>` (Beschluss 3). Ein Termin in [events/](../events/index.md) referenziert per JSCalendar `locations`/`locationId` auf diese IRI.
- Koordinaten in Karten: `Address.coordinates` verlangt `geo:`-URI (RFC 5870, ✅), z. B. `geo:52.5200,13.4050`.

## Fluss

1. Feature anlegen/ändern: `Create`/`Update` (AS2-Envelope) mit GeoJSON-Payload.
2. Karten-Clients fragen Filter über BBox/Radius ab (API-Muster in [api.md](../api.md)); Antwort ist eine `FeatureCollection`.
3. Adress-Eingabe in jeder App erzeugt **Komponenten**, keine Freitext-Zeile; Darstellung (einzeilig, länderspezifisch) ist Render-Regel, nicht Speicher.

## Projektionen

| Ziel | Projektion |
|------|------------|
| [events/](../events/index.md) | JSCalendar `locations` (Text + Referenz) |
| [people/](../people/index.md) | `Address`-Komponenten + `geo:`-URI |
| Karten-Renderer | Kacheln (MVT) — aus Geometrien erzeugt, nicht gespeichert |
| ISO-OA-Exporte | Komponenten nach ISO-19160-Namen, falls wir sie mitführen (offen) |

## Offene technische Punkte

- Führen wir ISO-19160-**Elementnamen** zusätzlich zu den JSContact-Komponenten mit? (Entscheidung offen, Inhalt von ISO 19160 noch ungelesen — ⚠️)
- Topologie zwischen Features (Gebäude ⊂ Grundstück) ist nicht standardisiert — eigene Festlegung nötig, noch nicht begonnen.
