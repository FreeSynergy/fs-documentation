# Datenformate

Formate legen fest, **wie** Daten gespeichert und zwischen Programmen ausgetauscht werden. Die Modelle in [modelle.md](modelle.md) sind formatunabhängig.

## Überblick

| Format | Typ | Verwendung | Kurzbeispiel |
|--------|-----|------------|--------------|
| **JSON** | strukturiert | API-Responses, Config, Export | `{"id":"doc_1","title":"Wiki"}` |
| **NDJSON** | zeilenbasiert | Streams, Bulk-Export, Logs | `{"id":"msg_1"}\n{"id":"msg_2"}` |
| **YAML** | strukturiert + Kommentare | Config-Dateien (Homer, Homepage) | `services:\n  - name: Wiki` |
| **TOML** | strukturiert + Kommentare | Projekt- und Tool-Config | `[app]\nname = "Homarr"` |
| **CSV/TSV** | tabellarisch | Import/Export von Listen | `id,title\n1,Wiki` |
| **XML** | strukturiert | Alt-Systeme, RSS/Atom | `<item><title>Wiki</title></item>` |
| **MessagePack** | binär | interne Kompaktübertragung | `{"id":"doc_1"}` (binär) |
| **Parquet** | binär, spaltenweise | Analytics, große Exporte | Datei-Export aus `chart` |
| **Markdown + Frontmatter** | Text + Metadaten | Wiki-Inhalt, Dokumentationen | `---\ntitle: Wiki\n---` |
| **iCalendar (ICS)** | Kalenderstandard | Termine, Serien | `BEGIN:VEVENT` |
| **vCard (VCF)** | Kontaktdatenstandard | Kontakte | `BEGIN:VCARD` |
| **GeoJSON** | Geodaten | Karten, Orte | `{"type":"Point","coordinates":[13.4,52.5]}` |
| **JSON Schema** | Metadaten | Validierung von Modellen | `{"type":"object","required":["id"]}` |

## JSON

Standardformat für alle API-Kommunikation.

```json
{
  "id": "doc_01HZX9",
  "title": "FreeSynergy Übersicht",
  "status": "active",
  "createdAt": "2026-10-01T09:00:00+02:00",
  "tags": ["doku", "wiki"],
  "author": { "id": "user_01HZXA", "displayName": "Anna Weber" }
}
```

Regeln:

- UTF-8, keine BOM
- Keys in `camelCase`
- Keine Duplikate von Keys, keine Kommentare
- Zahlen ohne führende Nullen, keine `NaN`/`Infinity`

## NDJSON (JSON Lines)

Ein JSON-Dokument pro Zeile — für Streams und Bulk-Import.

```json
{"id":"msg_01","channelId":"chan_01","body":"Hallo"}
{"id":"msg_02","channelId":"chan_01","body":"Wie geht's?"}
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

Erste Zeile = Header, Trennzeichen `,` (CSV) oder `\t` (TSV).

```csv
id,displayName,email,status
user_01,Anna Weber,anna@example.org,active
user_02,"Weber, Anna",anna2@example.org,invited
```

Regeln:

- Trennzeichen und Zeilenumbrüche in Werten mit `"` quoten
- Header-Zeile Pflicht, `camelCase`-Spaltennamen
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

## Wann welches Format?

| Ziel | Format | Begründung |
|------|--------|------------|
| API-Austausch | JSON | allgegenwärtig, typisiert validierbar |
| Config mit Kommentaren | YAML oder TOML | lesbar, Kommentare erlaubt |
| Statische Dashboards | YAML | keine Datenbank nötig (Homer, Homepage) |
| Bulk-Export / Import | NDJSON | zeilenweise, streamingfähig |
| Tabellen-Import (Fremdsysteme) | CSV/TSV | breit unterstützt |
| Kalender-Exchange | ICS | Standard, CalDAV-kompatibel |
| Kontakt-Exchange | VCF | Standard, CardDAV-kompatibel |
| Karten/Orte | GeoJSON | direkt in `map-view` nutzbar |
| Analytics-Export | Parquet | spaltenweise, kompakt |
| Inhalte/Dokumente | Markdown + Frontmatter | diffbar, versionierbar |

## Kodierung und Escaping

- **Zeichensatz**: UTF-8 immer, ohne BOM (Ausnahme: CSV für Excel)
- **Zeilenumbruch**: `\n` in Dateien, `\r\n` nur in ICS/vCard nach Standard
- **Escaping**: HTML wird in `markdown`-Feldern nicht gespeichert, sondern beim Rendern erzeugt
- **Datum/Zeit**: ISO 8601 mit Offset, Uhrzeit ohne Lokalisierung
- **Zahlen**: Punkt als Dezimaltrennzeichen, Tausendertrennzeichen nur in Anzeige

## Siehe auch

- [Standardmodelle](modelle.md)
- [Standardfelder](felder.md)
- [Konventionen](konventionen.md)
- [Daten-API](api.md)
