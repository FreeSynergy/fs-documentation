# Standardisierte Daten

Standardisierte Daten beschreiben, in welchen **Formaten**, **Modellen** und **Feldern** FreeSynergy-Programme, Komponenten und Masken Informationen austauschen.

## Warum Standardisierung?

- **Interoperabilität**: Messenger, Wiki, Kalender und Desktop-Dashboards nutzen dieselben Feldnamen
- **Wiederverwendbarkeit**: Komponenten (`table`, `list-view`, `calendar-view`) funktionieren mit jedem Modell
- **Migrationsfähigkeit**: Daten lassen sich zwischen Programmen migrieren (Export/Import)
- **Vorhersagbarkeit**: Masken (`apps/<kategorie>/masks/<programm>/api.md`) beschreiben denselben API-Stil
- **Automatisierung**: Workflows und Webhooks greifen auf stabile Pfade zu

## Datendomänen (Beschlossen 2026-11-01)

Jede Domäne hat ein Verzeichnis mit eigener `index.md`; jeder Standard darin ein Unterverzeichnis mit `description.md` + `storage.md`.

| Domäne | Verzeichnis | Kanonischer Standard | Weitere Standards |
|--------|-------------|----------------------|-------------------|
| Kontaktdaten | [contacts/](contacts/index.md) | JSContact (RFC 9553/9554) ✅ | vCard, jCard, CardDAV |
| Nachrichten | [messages/](messages/index.md) | AS2 `Note`/`Article` ✅ | JMAP, RFC 5322, MLS (⚠️) |
| Termine | [events/](events/index.md) | JSCalendar (RFC 8984) ✅ | iCalendar, CalDAV, iTIP |
| Geodaten | [geodata/](geodata/index.md) | GeoJSON (RFC 7946) ✅ | geo:-URI, ISO 19160 |
| Login / Konten | [login/](login/index.md) | OIDC ✅ (2026-11-02), OAuth 6749 ✅, WebAuthn ✅ | SCIM (⚠️), WebFinger, kanidm |
| Identität / Web of Trust | [identity/](identity/index.md) | WoT Spec v0.1.0-draft (VC, DIDComm, did:key) ✅ gesichtet | Andockpunkte: AS2 `Relationship`, `publicKey` |
| Profil | [profile/](profile/index.md) | AS2-`Actor`-Projektion auf JSContact ✅ | schema.org `Person` (⚠️) |
| Projekte | [projects/](projects/index.md) | ❌ keine offene Daten-Spec – eigene Arbeit | ISO 21502 (Prozess) ✅, MSPDI (De-facto) ✅, JSCalendar-`Task` |

Als **vorgeschlagen, noch nicht beschlossen**: `aufgaben/` (JSCalendar deckt `Task` bereits ab), `dokumente/` (Block-Struktur = größte Lücke), `dateien/`, `verschlagwortung/` (Web Annotation ✅), `kommentare/`, `benachrichtigungen/`, `organisationen/`.

Der **Envelope** (AS2 + ActivityPub, Beschlüsse in [standards.md](standards.md)) ist querschnittlich und keine eigene Domäne.

## Datenbereiche (Querschnitt)

| Datei | Inhalt |
|-------|--------|
| [standards.md](standards.md) | Welche existierenden Standards welchen Datenbereich abdecken (mit Belegen und ungeprüften Punkten) |
| [mappings.md](mappings.md) | Unsere Felder ↔ Standardfelder (zunächst Contact, Name, Überschrift) |
| [formats.md](formats.md) | Austauschformate (JSON, YAML, TOML, CSV, NDJSON, ICS, VCF, GeoJSON, …) |
| [models.md](models.md) | Standardmodelle (User, Message, Document, Event, Task, Contact, …) |
| [fields.md](fields.md) | Standardfelder, Typen, Enums, Pflichtfelder |
| [conventions.md](conventions.md) | Benennung, Dateistrukturen, Versionierung, Validierung, i18n |
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

1. **IDs sind opaque Strings** — niemals als Nummer interpretieren; intern ULID, extern absoluter IRI `https://<instanz>/<domaene>/<ulid>` (Beschluss 3)
2. **Zeiten immer mit Zeitzonen-Offset** oder explizit `allDay: true`
3. **Leere Werte sind `null`**, nicht `""` (Ausnahme: Textfelder mit Pflicht)
4. **Enums sind lowercase und Singular** (`active`, nicht `Active`)
5. **Neue Felder sind additiv** — bestehende Felder werden nicht umbenannt
6. **Jede Ressource trägt `id`, `createdAt`, `updatedAt`**
7. **Audience-Regel:** `to`/`cc`/`bto`/`bcc` steuern, wo Kopien landen — sie ersetzen keine Ressourcens-Autorisierung (Beschluss 2)

## Verzeichnisstruktur

```
docs/de/data/
├── index.md            (diese Datei)
├── standards.md        Standards-Register + Beschlüsse 2026-11-01
├── mappings.md         unsere Felder ↔ Standardfelder
├── formats.md          Austauschformate
├── models.md          Standardmodelle
├── fields.md           Standardfelder und Typen
├── conventions.md     Benennungs- und Versionierungsregeln
├── api.md              einheitliches API-Muster
├── contacts/           ├── index.md └── jscontact/{description,storage}.md
├── messages/           ┐
├── events/             │ jede Domäne:
├── geodata/            │ index.md + description.md
├── login/              │ + technical.md + standards.md
├── identity/           │ + examples.md
├── profile/            │
└── projects/           ┘
```

## Siehe auch

- [Komponenten](../components/) — Attribute und Datentypen der UI-Elemente
- [Gesten](../interactions/gestures/) — Interaktionsdaten (Schwellwerte, Callbacks)
- [Animationen](../interactions/animations/) — Animationsattribute und -dauern
- [Programs](../programs/) — Programme mit eigener `api.md` pro Maske
- [Desktop-Masken](../programs/platform/desktop/frontends/) — Beispiel für API-Dokumentation nach Muster
