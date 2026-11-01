# Konventionen

Konventionen halten Dokumentation und Daten über alle Kategorien hinweg konsistent.

## Benennung

| Kontext | Stil | Beispiel |
|---------|------|----------|
| Felder und Attribute | `camelCase` | `createdAt`, `displayName` |
| JSON-Schlüssel in Configs | `kebab-case` oder `camelCase` (pro Datei einheitlich) | `tap-threshold` / `tapThreshold` |
| Verzeichnis- und Dateinamen | `kebab-case` | `long-press/`, `fade-in/` |
| Kategorien | lowercase, deutscher Name wenn üblich | `projektmanagement`, `whiteboards` |
| Programmverzeichnisse | offizieller Projektname, lowercase | `homarr`, `mediawiki`, `xwiki` |
| Konstanten und Umgebungsvariablen | `SCREAMING_SNAKE_CASE` | `FS_API_TOKEN` |
| Enums | lowercase, Singular, `_` bei Leerzeichen | `in_progress` |
| Events | `<resource>.<aktion>` lowercase | `document.published` |

## Datei-Konventionen

### Programme (Skins)

Jedes Programm in `apps/<kategorie>/skins/<programm>/` bekommt **sieben** Dateien:

| Datei | Inhalt |
|-------|--------|
| `index.md` | Übersicht + Links auf die sechs anderen Dateien |
| `description.md` | Was das Programm macht, Vorteile, Abgrenzung, Technische Details |
| `features.md` | Funktionen, Widgets/Plugins, Was es NICHT kann |
| `menu.md` | Menüpunkte, Kontextmenüs, Rollen-Menüs |
| `structure.md` | Fenster-Struktur (ASCII), UI/UX, Accessibility, Performance |
| `shortcuts.md` | Alle Tastatur-Shortcuts (immer separat!) |
| `api.md` | API-Art, Auth, Endpunkte, Beispiele, Rate Limits, SDKs |

### Komponenten

`components/<gruppe>/<element>/` mit `description.md`, `appearance.md`, `attributes.md` und bei Bedarf `usage.md`, `examples.md`.

### Gesten

`gestures/<geste>/` mit `description.md`, `attributes.md`, `appearance.md`.

### Animationen

`animations/<animation>/` mit `description.md`, `attributes.md`, `appearance.md`.

### Daten

Querschnitts-Dateien direkt in `data/`: `index.md`, `standards.md`, `mappings.md`, `formate.md`, `modelle.md`, `felder.md`, `konventionen.md`, `api.md`.

Darunter gilt: **Datendomäne → Standard → Dateien**:

```
data/<domaene>/index.md                      Übersicht + Tabelle der Standards der Domäne
data/<domaene>/<standard>/beschreibung.md    allgemeine Beschreibung (was, Umfang, Grenzen)
data/<domaene>/<standard>/speicherung.md     wie Daten darin gespeichert werden (DB, Dateien, Patches)
data/<domaene>/<standard>/beispiele.md       optional, bei Bedarf
data/<domaene>/<standard>/mapping.md         optional, unsere Felder ↔ Standardfelder
```

- Domänenverzeichnisse: lowercase, ASCII (`kontakt`, `identitaet`, `geodaten`)
- Standardverzeichnisse: offizieller Kurzname, lowercase (`jscontact`, `jscalendar`, `vcard`)
- Jeder Eintrag endet wie überall mit `## Siehe auch`

## Links

- Querverweise innerhalb eines Programms: relativ (`[api.md](api.md)`)
- Verweise über Bereiche hinweg: relativ mit `../` (von `data/` aus: `[Gesten](../gestures/)`)
- Kategorien-Index immer als Verzeichnislink (von `data/` aus: `[Messenger](../apps/messenger/)`)
- Jede Datei endet mit einem `## Siehe auch`-Abschnitt
- Keine Links auf Dateien, die nicht existieren

## Sprachkonvention

1. Deutsch (`docs/de/`) ist die Leitversion und wird zuerst geschrieben
2. Englisch (`docs/en/`) spiegelt die Verzeichnisstruktur (Französisch pausiert)
3. Verzeichnis- und Dateinamen sind sprachunabhängig (gleiches Schema in `de/` und `en/`)
4. Produkt- und Projektnamen bleiben unübersetzt
5. Fachbegriffe aus UI und API bleiben englisch (`Modal`, `Toast`, `Endpoint`)

## Versionierung und Kompatibilität

| Regel | Beschreibung |
|-------|--------------|
| SemVer | `MAJOR.MINOR.PATCH` für Schemas und API-Versionen |
| Additive Änderungen | neue Felder sind `MINOR`, keine Breaking Changes |
| Breaking Change | Feld entfernen/umbenennen oder Typ ändern ist `MAJOR` |
| API-Version im Pfad | `/api/v1/…`; alte Versionen mindestens 12 Monate |
| Deprecation | Feld bleibt mit `deprecated: true` markiert, mindestens 2 Minor-Releases |
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

Beispiel-Dokument dazu:

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
| Pflichtfelder | `required` im Schema; fehlendes Pflichtfeld = `400 validation_error` |
| Null-Werte | optionale Felder dürfen `null` sein, Pflichtfelder nicht |
| Enums | nur dokumentierte Werte; unbekannte Werte = `422` |
| Längen | `maxLength` dokumentieren und im UI sichtbar machen |
| Referenzen | müssen existieren oder `null` sein; tote Referenzen werden bereinigt |
| Duplikate | `slug`, `email`, `username` sind eindeutig im Geltungsbereich |
| Zeitzonen | `timezone` muss ein IANA-Identifier sein |
| Dateien | `mimeType` und `size` sind Pflicht, `checksum` empfohlen |
| Paginierung | Listen werden niemals unbegrenzt geliefert; Default `limit=25`, Maximum `100` |

## Internationalisierung

| Punkt | Konvention |
|-------|------------|
| Sprachcodes | ISO 639-1: `de`, `en`, `fr` |
| Regionale Codes | nur wo nötig: `de-DE`, `fr-CH` |
| Übersetzungsdateien | `locales/<code>.json` mit `camelCase`-Keys |
| Fallback | fehlender Key → `de`, niemals Key-Anzeige im UI |
| Datum/Zeit in UI | nach `locale` formatieren, Daten immer ISO 8601 |
| Zahlen | Daten immer mit Punkt; Anzeige nach `locale` |

```json
{
  "task.status.open": "Offen",
  "task.status.in_progress": "In Bearbeitung",
  "task.status.done": "Erledigt"
}
```

## Barrierefreiheit in Daten

| Feld | Pflicht für | Beschreibung |
|------|-------------|--------------|
| `ariaLabel` | alle interaktiven Elemente | Screenreader-Text |
| `role` | alle interaktiven Elemente | ARIA-Rolle |
| `altText` | `image`, `avatar`, `icon` | Alternativtext |
| `respectReducedMotion` | alle Animationen | Animationen reduzieren |
| `alternativeAction` | Gesten | Tastatur-/Button-Äquivalent |
| `keyboardShortcut` | alle Aktionen | in `shortcuts.md` dokumentieren |

## Qualitätssicherung

- Jede neue Programm-Doku enthält alle sieben Dateien (keine leeren Platzhalter)
- Kurzform-Dateien (`index.md`) verlinken auf alle übrigen
- `shortcuts.md` und `api.md` sind nie in anderen Dateien enthalten
- Fehlende Funktionen werden ausdrücklich benannt („Was X NICHT kann“)
- Erfundene Shortcuts oder Endpoints sind ein Fehler — lieber „nicht vorhanden“
- **Standard-Pate:** Jedes Feld in `felder.md` nennt in [standards.md](standards.md) einen Beleg (Standard samt Nummer) oder ist ausdrücklich als **eigene Festlegung** markiert. Ein Feld ohne Beleg und ohne Markierung ist ein Fehler
- **Keine erfundenen Standard-Nummern:** Eine RFC- oder Spec-Nummer wird nur genannt, wenn sie nachgesehen wurde. ungeprüfte Angaben werden mit ⚠️ gekennzeichnet

## Siehe auch

- [Datenformate](formate.md)
- [Datenmodelle](modelle.md)
- [Standardfelder](felder.md)
- [Daten-API](api.md)
- [Komponenten](../components/)
