# Konventionen

Konventionen halten Dokumentation und Daten über alle Kategorien hinweg konsistent.

## Benennung

| Kontext | Stil | Beispiel |
|---------|------|----------|
| Felder und Attribute | `camelCase` | `createdAt`, `displayName` |
| JSON-Schlüssel in Configs | `kebab-case` oder `camelCase` (pro Datei einheitlich) | `tap-threshold` / `tapThreshold` |
| Verzeichnis- und Dateinamen | `kebab-case` | `long-press/`, `fade-in/` |
| Kategorien | Kleinbuchstaben, der übliche Name | `projectmanagement`, `whiteboards` |
| Programm-Verzeichnisse | offizieller Projektname, Kleinbuchstaben | `homarr`, `mediawiki`, `xwiki` |
| Konstanten und Umgebungsvariablen | `SCREAMING_SNAKE_CASE` | `FS_API_TOKEN` |
| Enums | Kleinbuchstaben, Singular, `_` für Leerzeichen | `in_progress` |
| Events | `<resource>.<action>`, Kleinbuchstaben | `document.published` |

## Dateikonventionen

### Programme (Frontends)

Jedes Programm in `apps/<category>/frontends/<program>/` bekommt **sieben** Dateien:

| Datei | Inhalt |
|-------|--------|
| `index.md` | Übersicht + Links zu den anderen sechs Dateien |
| `description.md` | was das Programm tut, Vorteile, Abgrenzung, technische Details |
| `features.md` | Funktionen, Widgets/Plugins, was es NICHT tut |
| `menus.md` | Menüpunkte, Kontextmenüs, Rollenmenüs |
| `layout.md` | Fensteraufbau (ASCII), UI/UX, Barrierefreiheit, Performance |
| `shortcuts.md` | alle Tastenkürzel (immer separat!) |
| `api.md` | API-Typ, Auth, Endpoints, Beispiele, Rate Limits, SDKs |

### Komponenten

`components/<band>/<group>/<element>/` mit `description.md`, `appearance.md`, `attributes.md` und `usage.md`. Bands = Ebenen: `primitives`, `widgets`, `workbenches`.

### Gesten

`gestures/<category>/<gesture>/` mit `description.md`, `attributes.md`, `appearance.md`
(Kategorien: `tap`, `swipe`, `transform`, `special`, `device`, `combined`).

### Animationen

`animations/<animation>/` mit `description.md`, `attributes.md`, `appearance.md`.

### Daten

Querschnittsdateien direkt in `data/`: `index.md`, `standards.md`, `mappings.md`, `formats.md`, `models.md`, `fields.md`, `conventions.md`, `api.md`.

Darunter gilt die Regel: **Datendomäne → Standard → Dateien**:

```
data/<domain>/index.md                       Übersicht + Tabelle der Standards der Domäne
data/<domain>/<standard>/description.md      allgemeine Beschreibung (was, Umfang, Grenzen)
data/<domain>/<standard>/storage.md          wie Daten darin gespeichert werden (DB, Dateien, Patches)
data/<domain>/<standard>/examples.md         optional, wenn nötig
data/<domain>/<standard>/mapping.md          optional, unsere Felder ↔ Standardfelder
```

- Domänen-Verzeichnisse: Kleinbuchstaben, ASCII (`contacts`, `identity`, `geodata`)
- Standard-Verzeichnisse: offizieller Kurzname, Kleinbuchstaben (`jscontact`, `jscalendar`, `vcard`)
- jeder Eintrag endet, wie überall, mit `## Siehe auch`

## Links

- Querverweise innerhalb eines Programms: relativ (`[api.md](api.md)`)
- Verweise über Bereiche hinweg: relativ mit `../` (aus `data/`: `[Gesten](../interactions/gestures/)`)
- Kategorie-Index immer als Verzeichnislink (aus `data/`: `[Messenger](../programs/apps/messenger/)`)
- jede Datei endet mit einem Abschnitt `## Siehe auch`
- keine Links auf Dateien, die nicht existieren, Ausnahme: Querverweise innerhalb der eigenen Sprachversion (Regel 6 der Sprachkonvention)

## Sprachkonvention

1. Deutsch (`docs/de/`) ist die Leitversion und wird zuerst geschrieben
2. Englisch (`docs/en/`) spiegelt die Verzeichnisstruktur (Französisch pausiert)
3. Verzeichnis- und Dateinamen sind sprachunabhängig (gleiches Schema in `de/` und `en/`)
4. Produkt- und Projektnamen bleiben unübersetzt
5. technische Begriffe aus UI und API bleiben englisch (`Modal`, `Toast`, `Endpoint`)
6. **nie sprachübergreifend verlinken:** in `en/` (und späteren Sprachen) zeigt jeder Querverweis auf die eigene Sprachversion (`en → en`), nie auf `de/`, auch wenn die Zieldatei dort noch fehlt; die Übersetzung folgt. Der Sprachwechsel läuft nur über den Sprachumschalter in `index.md`

## Versionierung und Kompatibilität

| Regel | Beschreibung |
|-------|--------------|
| SemVer | `MAJOR.MINOR.PATCH` für Schemas und API-Versionen |
| additive Änderungen | neue Felder sind `MINOR`, keine Breaking Changes |
| Breaking Change | Entfernen/Umbenennen eines Feldes oder Ändern seines Typs ist `MAJOR` |
| API-Version im Pfad | `/api/v1/…`; alte Versionen für mindestens 12 Monate |
| Deprecation | Feld bleibt mit `deprecated: true` markiert, mindestens 2 Minor-Releases lang |
| Changelog | Änderungen an Modellen in `data/` dokumentieren |

## JSON-Schema-Muster

Standard-Schema-Aufbau für jedes Modell:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://freesynergy.github.io/schema/contact.json",
  "title": "Contact",
  "type": "object",
  "additionalProperties": true,
  "required": ["id", "firstName", "lastName", "createdAt", "updatedAt"],
  "properties": {
    "id": { "type": "string", "pattern": "^con_[0-9A-HJKMNP-TV-Z]{26}$" },
    "firstName": { "type": "string", "maxLength": 100 },
    "lastName": { "type": "string", "maxLength": 100 },
    "emails": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["value"],
        "properties": {
          "type": { "enum": ["work", "home", "other"] },
          "value": { "type": "string", "format": "email" }
        }
      }
    }
  }
}
```

Beispieldokument dazu:

```json
{
  "id": "con_01HZXH7Q3T8V2B4C6D9E0F1A2K",
  "firstName": "Anna",
  "lastName": "Weber",
  "emails": [{ "type": "work", "value": "anna@example.org" }],
  "createdAt": "2026-10-01T09:00:00+02:00",
  "updatedAt": "2026-10-12T14:05:00+02:00"
}
```

## Validierungsregeln

| Regel | Beschreibung |
|-------|--------------|
| Pflichtfelder | `required` im Schema; ein fehlendes Pflichtfeld = `400 validation_error` |
| null-Werte | optionale Felder dürfen `null` sein, Pflichtfelder nicht |
| Enums | nur dokumentierte Werte; unbekannte Werte = `422` |
| Längen | `maxLength` dokumentieren und in der UI sichtbar machen |
| Referenzen | müssen existieren oder `null` sein; tote Referenzen werden bereinigt |
| Duplikate | `slug`, `email`, `username` sind innerhalb des Bereichs eindeutig |
| Zeitzonen | `timezone` muss eine IANA-Kennung sein |
| Dateien | `mimeType` und `size` sind Pflicht, `checksum` empfohlen |
| Pagination | Listen werden nie unbegrenzt ausgeliefert; Default `limit=25`, Maximum `100` |

## Internationalisierung

| Punkt | Konvention |
|-------|------------|
| Sprachcodes | ISO 639-1: `de`, `en`, `fr` |
| Regionalcodes | nur wo nötig: `de-DE`, `fr-CH` |
| Übersetzungsdateien | `locales/<code>.json` mit `camelCase`-Schlüsseln |
| Fallback | fehlender Schlüssel → `de`, den Schlüssel nie in der UI zeigen |
| Datum/Uhrzeit in der UI | nach `locale` formatieren, Daten immer ISO 8601 |
| Zahlen | Daten immer mit Punkt; Anzeige nach `locale` |

```json
{
  "task.status.open": "Offen",
  "task.status.in_progress": "In Arbeit",
  "task.status.done": "Erledigt"
}
```

## Barrierefreiheit in Daten

| Feld | Pflicht für | Beschreibung |
|------|-------------|--------------|
| `ariaLabel` | alle interaktiven Elemente | Text für Screenreader |
| `role` | alle interaktiven Elemente | ARIA-Rolle |
| `altText` | `image`, `avatar`, `icon` | alternativer Text |
| `respectReducedMotion` | alle Animationen | Animationen reduzieren |
| `alternativeAction` | Gesten | Tastatur-/Button-Entsprechung |
| `keyboardShortcut` | alle Aktionen | in `shortcuts.md` dokumentieren |

## Qualitätssicherung

- jede neue Programmdokumentation enthält alle sieben Dateien (keine leeren Platzhalter)
- Kurzdateien (`index.md`) verlinken auf alle anderen
- `shortcuts.md` und `api.md` werden nie in andere Dateien eingebettet
- fehlende Funktionen werden ausdrücklich benannt („Was X NICHT tut“)
- erfundene Tastenkürzel oder Endpoints sind ein Fehler; besser „nicht vorhanden“ schreiben
- **Standard-Verantwortung:** jedes Feld in `fields.md` nennt einen Beleg in [standards.md](standards.md) (Standard plus Nummer) oder ist ausdrücklich als **eigene Entscheidung** markiert. Ein Feld ohne Beleg und ohne Markierung ist ein Fehler
- **keine erfundenen Standardnummern:** eine RFC- oder Spezifikationsnummer wird nur genannt, wenn sie nachgeschlagen wurde. Ungeprüfte Aussagen werden mit ⚠️ markiert

## Siehe auch

- [Datenformate](formats.md)
- [Datenmodelle](models.md)
- [Standardfelder](fields.md)
- [Daten-API](api.md)
- [Komponenten](../components/)
