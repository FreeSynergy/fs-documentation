# Datenformate

Formate legen fest, **wie** Daten gespeichert und zwischen Programmen ausgetauscht werden. Die Modelle in [models.md](models.md) sind formatunabhängig.

## Übersicht

| Format | Typ | Verwendung | Kurzbeispiel |
|--------|------|-------|---------------|
| **JSON** | strukturiert | API-Antworten, Config, Export | `{"id":"doc_1","title":"Wiki"}` |
| **NDJSON** | zeilenbasiert | Streams, Bulk-Export, Logs | `{"id":"msg_1"}\n{"id":"msg_2"}` |
| **YAML** | strukturiert + Kommentare | Konfigurationsdateien (Homer, Homepage) | `services:\n  - name: Wiki` |
| **TOML** | strukturiert + Kommentare | Projekt- und Tool-Konfiguration | `[app]\nname = "Homarr"` |
| **CSV/TSV** | tabellarisch | Import/Export von Listen | `id,title\n1,Wiki` |
| **XML** | strukturiert | Altsysteme, RSS/Atom | `<item><title>Wiki</title></item>` |
| **MessagePack** | binär | interner kompakter Transfer | `{"id":"doc_1"}` (binär) |
| **Parquet** | binär, spaltenorientiert | Analytik, große Exporte | Dateiexport aus `chart` |
| **Markdown + Frontmatter** | Text + Metadaten | Wiki-Inhalte, Dokumentation | `---\ntitle: Wiki\n---` |
| **iCalendar (ICS)** | Kalenderstandard | Termine, Serien | `BEGIN:VEVENT` |
| **vCard (VCF)** | Kontaktdatenstandard | Kontakte | `BEGIN:VCARD` |
| **GeoJSON** | Geodaten | Karten, Orte | `{"type":"Point","coordinates":[13.4,52.5]}` |
| **JSON Schema** | Metadaten | Validierung von Modellen | `{"type":"object","required":["id"]}` |

## JSON

Standardformat für die gesamte API-Kommunikation.

```json
{
  "id": "doc_01HZX9",
  "title": "FreeSynergy-Überblick",
  "status": "active",
  "createdAt": "2026-10-01T09:00:00+02:00",
  "tags": ["docs", "wiki"],
  "author": { "id": "user_01HZXA", "displayName": "Anna Weber" }
}
```

Regeln:

- UTF-8, ohne BOM
- Schlüssel in `camelCase`
- keine doppelten Schlüssel, keine Kommentare
- Zahlen ohne führende Nullen, kein `NaN`/`Infinity`

## NDJSON (JSON Lines)

Ein JSON-Dokument pro Zeile — für Streams und Bulk-Import.

```json
{"id":"msg_01","channelId":"chan_01","body":"Hallo"}
{"id":"msg_02","channelId":"chan_01","body":"Wie geht es dir?"}
```

## YAML

Für Konfigurationsdateien (z. B. Homer `config.yml`, Homepage `services.yaml`).

```yaml
# Dashboard-Konfiguration
services:
  - name: Wiki
    url: https://wiki.example.org
    icon: mediawiki.svg
  - name: Kalender
    url: https://cal.example.org
    widget:
      type: calendar
      url: https://cal.example.org/dav
```

## TOML

```toml
[app]
name = "Homarr"
port = 7575

[auth]
provider = "oidc"
```

## CSV / TSV

Erste Zeile = Kopfzeile, Trennzeichen `,` (CSV) oder `\t` (TSV).

```csv
id,displayName,email,status
user_01,Anna Weber,anna@example.org,active
user_02,"Weber, Anna",anna2@example.org,invited
```

Regeln:

- Trennzeichen und Zeilenumbrüche in Werten mit `"` einschließen
- Kopfzeile ist Pflicht, Spaltennamen in `camelCase`
- Zeichensatz UTF-8 (BOM nur für Excel-Kompatibilität)

## Markdown + Frontmatter

Standard für Dokumente und für diese Dokumentation.

```markdown
---
title: Standardisierte Daten
lang: de
tags: [data, standard]
updatedAt: 2026-10-31
---

# Standardisierte Daten
```

## iCalendar (ICS)

```ics
BEGIN:VEVENT
UID:evt_01HZXB@example.org
DTSTART:20261105T100000Z
DTEND:20261105T110000Z
SUMMARY:Team-Sync
RRULE:FREQ=WEEKLY;BYDAY=WE
END:VEVENT
```

## vCard (VCF)

```vcf
BEGIN:VCARD
VERSION:3.0
N:Weber;Anna;;;
FN:Anna Weber
EMAIL;TYPE=WORK:anna@example.org
END:VCARD
```

## GeoJSON

```json
{
  "type": "Feature",
  "geometry": { "type": "Point", "coordinates": [13.404954, 52.520008] },
  "properties": { "id": "loc_01", "name": "Hauptbahnhof Berlin" }
}
```

## JSON Schema (Validierung)

```json
{
  "$id": "https://freesynergy.github.io/schema/task.json",
  "type": "object",
  "required": ["id", "title", "status", "createdAt", "updatedAt"],
  "properties": {
    "id": { "type": "string" },
    "title": { "type": "string", "maxLength": 200 },
    "status": { "enum": ["open", "in_progress", "done", "archived"] },
    "dueAt": { "type": ["string", "null"], "format": "date-time" }
  }
}
```

## Welches Format wofür?

| Ziel | Format | Grund |
|------|--------|-------|
| API-Austausch | JSON | überall verbreitet, typisiert und prüfbar |
| Config mit Kommentaren | YAML oder TOML | lesbar, Kommentare erlaubt |
| statische Dashboards | YAML | keine Datenbank nötig (Homer, Homepage) |
| Bulk-Export / -Import | NDJSON | zeilenweise, streambar |
| Tabellen-Import (Fremdsysteme) | CSV/TSV | breit unterstützt |
| Kalenderaustausch | ICS | Standard, CalDAV-kompatibel |
| Kontaktaustausch | VCF | Standard, CardDAV-kompatibel |
| Karten/Orte | GeoJSON | direkt in `map-view` nutzbar |
| Analytik-Export | Parquet | spaltenorientiert, kompakt |
| Inhalte/Dokumente | Markdown + Frontmatter | diffbar, versionierbar |

## Kodierung und Escaping

- **Zeichensatz**: immer UTF-8, ohne BOM (Ausnahme: CSV für Excel)
- **Zeilenumbruch**: `\n` in Dateien, `\r\n` nur in ICS/vCard gemäß Standard
- **Escaping**: HTML wird nicht in `markdown`-Feldern gespeichert, sondern beim Rendern erzeugt
- **Datum/Uhrzeit**: ISO 8601 mit Offset, Zeit ohne Lokalisierung
- **Zahlen**: Punkt als Dezimaltrennzeichen, Tausendertrennzeichen nur in der Anzeige

## Siehe auch

- [Standardmodelle](models.md)
- [Standardfelder](fields.md)
- [Konventionen](conventions.md)
- [Daten-API](api.md)
