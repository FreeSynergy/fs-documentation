# Standardisierte Daten

Standardisierte Daten beschreiben, in welchen **Formaten**, **Modellen** und **Feldern** FreeSynergy-Programme, Komponenten und Skins Informationen austauschen.

## Warum Standardisierung?

- **Interoperabilität**: Messenger, Wiki, Kalender und Desktop-Dashboards nutzen dieselben Feldnamen
- **Wiederverwendbarkeit**: Komponenten (`table`, `list-view`, `calendar-view`) funktionieren mit jedem Modell
- **Migrationsfähigkeit**: Daten lassen sich zwischen Programmen migrieren (Export/Import)
- **Vorhersagbarkeit**: Skins (`apps/<kategorie>/skins/<programm>/api.md`) beschreiben denselben API-Stil
- **Automatisierung**: Workflows und Webhooks greifen auf stabile Pfade zu

## Datenbereiche

| Datei | Inhalt |
|-------|--------|
| [formate.md](formate.md) | Austauschformate (JSON, YAML, TOML, CSV, NDJSON, ICS, VCF, GeoJSON, …) |
| [modelle.md](modelle.md) | Standardmodelle (User, Message, Document, Event, Task, Contact, …) |
| [felder.md](felder.md) | Standardfelder, Typen, Enums, Pflichtfelder |
| [konventionen.md](konventionen.md) | Benennung, Dateistrukturen, Versionierung, Validierung, i18n |
| [api.md](api.md) | Einheitliches CRUD-Muster, Pagination, Filter, Fehlerformat, Webhooks |

## Standardmodelle (Überblick)

| Modell | Kurzbeschreibung | Kategorie-Bezug |
|--------|------------------|-----------------|
| **User** | Konto mit Profil, Rollen, Status | alle |
| **Team** | Organisation, Gruppe, Workspace | alle |
| **Message** | Chat-, Kommentar- oder Mail-Nachricht | messenger |
| **Document** | Seite, Beitrag, Artikel mit Blöcken | wiki |
| **Block** | Inhaltselement in einem Document | components |
| **Event** | Termin mit Start, Ende, Teilnehmern | kalender |
| **Task** | Aufgabe mit Fälligkeit und Status | projektmanagement |
| **Contact** | Person mit Kontaktdaten und Organisation | kontakt, crm |
| **Location** | Ort mit Adresse und GeoJSON-Koordinate | maps |
| **File** | Datei mit Speicherort, Typ, Größe | alle |
| **Tag** | Schlagwort zur Kategorisierung | alle |
| **Comment** | An eine Ressource gehängter Kommentar | alle |
| **Notification** | Benachrichtigung an einen User | alle |
| **Revision** | Version einer Ressource | wiki, components |
| **Integration** | Webhook, API-Key, Connector | workflows |

## Datentypen

| Typ | Schreibweise | Beispiel |
|-----|--------------|----------|
| `string` | Text in `"..."` | `"Anna Weber"` |
| `number` | Ganzzahl oder Dezimalzahl | `42`, `19.99` |
| `boolean` | `true` / `false` | `true` |
| `datetime` | ISO 8601 | `"2026-10-31T06:00:00+01:00"` |
| `date` | `YYYY-MM-DD` | `"2026-10-31"` |
| `duration` | ISO 8601 Duration | `"PT30M"` |
| `enum` | feste Werteliste | `"active"` |
| `array[]` | Liste | `["tag-a", "tag-b"]` |
| `object` | verschachteltes Objekt | `{ "city": "Berlin" }` |
| `reference` | ID auf ein anderes Modell | `"user_01H…" \| User` |
| `markdown` | Markdown-Text | `"**Wichtig**"` |
| `null` | explizit leer | `null` |

## Grundregeln

1. **IDs sind opaque Strings** — niemals als Nummer interpretieren
2. **Zeiten immer mit Zeitzonen-Offset** oder explizit `allDay: true`
3. **Leere Werte sind `null`**, nicht `""` (Ausnahme: Textfelder mit Pflicht)
4. **Enums sind lowercase und Singular** (`active`, nicht `Active`)
5. **Neue Felder sind additiv** — bestehende Felder werden nicht umbenannt
6. **Jede Ressource trägt `id`, `createdAt`, `updatedAt`**

## Verzeichnisstruktur

```
docs/de/data/
├── index.md            (diese Datei)
├── formate.md          Austauschformate
├── modelle.md          Standardmodelle
├── felder.md           Standardfelder und Typen
├── konventionen.md     Benennungs- und Versionierungsregeln
└── api.md              einheitliches API-Muster
```

## Siehe auch

- [Komponenten](../components/) — Attribute und Datentypen der UI-Elemente
- [Gesten](../gestures/) — Interaktionsdaten (Schwellwerte, Callbacks)
- [Animationen](../animations/) — Animationsattribute und -dauern
- [Apps](../apps/) — Programme mit eigener `api.md` pro Skin
- [Desktop-Skins](../apps/desktop/skins/) — Beispiel für API-Dokumentation nach Muster
