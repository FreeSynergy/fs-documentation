# Termine – Technische Erklärung

## Speicherperspektive

- **Original + Envelope + Protokoll (ADR 0020, 0030):** die eingehende iTIP/iMIP-Nachricht, ICS, jCal oder das ActivityPub-Objekt wird **wie empfangen** aufbewahrt (mit Hash und der benutzten tzdb-Version); Envelope = AS2 **`Event`** (`name` ← JSCalendar `title`, `startTime`/`endTime`, `location`); Inhalt = **JSCalendar 2.0**-JSON.
- **Eine Tabelle `calobj`** für beide JSCalendar-Typen (`Event`, `Task`). Herausgezogene Spalten: `id` (UUIDv7), `uid` (JSCalendar-`uid`), `type` (`event`/`task`), `start_min`/`end_min` (Index über Zeitraum; bei Tasks `due_min`), `calendar_id` (welcher Kalender), `sequence`, `updated_at`, `sync_token`.
- **Serien:** das Master-Objekt mit `recurrenceRules` wird **nicht** aufgelöst gespeichert; die Auflösung in Einzelfälle passiert zur Abfragezeit (iCalendar-Halbraum-Regeln beachten). Änderungen an einem Einzelfall werden als `recurrenceOverrides`-Eintrag am Master abgelegt (✅). JSCalendar 2.0 hat ein einziges `recurrenceRule`.

## Schlüssel und Verknüpfungen

- Extern: `https://<instanz>/events/<uuid>` (Beschluss 3).
- `participants[].email` folgt RFC 5322 §3.4.1 (✅) und ist die **Verknüpfung zu [people/](../people/index.md)**: beim Rendern wird die Card gesucht, aber die Participant-Felder bleiben die terminverbindliche Kopie (sonst ändert sich die Einladung, wenn jemand umzieht).
- `participants[].locationId` ↔ ` Participant.kind = "location"` verweist auf [geodata/](../geodata/index.md).
- `relatedTo` verbindet Task ↔ Event (Aufgabe „Protokoll schreiben“ hängt an Termin).

## Protokoll-Abbildung (AS2, ✅)

| Aktion | Activity | iTIP |
|--------|----------|------|
| veröffentlichen / anlegen | `Create` | PUBLISH |
| einladen | `Invite` | REQUEST |
| antworten | `Accept` / `TentativeAccept` / `Reject` | REPLY |
| ändern | `Update` | REQUEST (sequence +1) |
| absagen | `Delete` oder Status `cancelled` | CANCEL |

## Fluss (Einladung)

1. Organizer speichert `Event` mit `participants` → `Create` im Envelope.
2. iTIP (RFC 5546, ✅): Anfragen an `sendTo` (`imip`/`other`), Antworten schreiben `participationStatus` (`needs-action` → `accepted`/`declined`/`tentative`/`delegated`).
3. Teil-Patches über die RFC-8984-Pfadform (`participants/<id>/participationStatus`, ✅) statt Ganz-Objekt-Ersetzen.
4. Sync für Clients über `sync_token` (Beleg: RFC 6578, ✅).

## Projektionen

| Ziel | Projektion |
|------|------------|
| Datei-Austausch | iCalendar (RFC 5545) / jCal (RFC 7265) — Export/Import |
| Server-Interop | CalDAV + Scheduling (RFC 6638, ✅) |
| [projects/](../projects/index.md) | Task-Objekte unverändert, Struktur-Referenzen als Extension |
| Webhooks/Webhooks-Feed | `Create`/`Update`/`Delete` (Beschluss 2) |

## Offene technische Punkte

- **Zeitzonen:** JSCalendar 2.0 erlaubt nur IANA-IDs (`timeZones` obsolet); wir liefern tzdb (2026f) aus und notieren ihre Version zu jedem Original.
- iTIP-Planungs-Eigenschaften sind in 2.0 nur *reserviert* → behalten sie im Original und als Anbieter-Eigenschaften, bis eine Planungs-Erweiterung existiert (Lücke).
