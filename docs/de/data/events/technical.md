# Termine – Technische Erklärung

## Speicherperspektive

- **Eine Tabelle `calobj`** für beide JSCalendar-Typen (`Event`, `Task`): kanonischer Payload = JSCalendar-JSON (Beschluss 4). Herausgezogene Spalten: `id` (ULID), `uid` (JSCalendar-`uid`), `type` (`event`/`task`), `start_min`/`end_min` (Index über Zeitraum; bei Tasks `due_min`), `calendar_id` (welcher Kalender), `sequence`, `updated_at`, `sync_token`.
- **Serien:** das Master-Objekt mit `recurrenceRules` wird **nicht** aufgelöst gespeichert; die Auflösung in Einzelfälle passiert zur Abfragezeit (iCalendar-Halbraum-Regeln beachten). Änderungen an einem Einzelfall werden als `recurrenceOverrides`-Eintrag am Master abgelegt (RFC 8984, ✅).

## Schlüssel und Verknüpfungen

- Extern: `https://<instanz>/events/<ulid>` (Beschluss 3).
- `participants[].email` folgt RFC 5322 §3.4.1 (✅) und ist die **Verknüpfung zu [contacts/](../contacts/index.md)**: beim Rendern wird die Card gesucht, aber die Participant-Felder bleiben die terminverbindliche Kopie (sonst ändert sich die Einladung, wenn jemand umzieht).
- `participants[].locationId` ↔ ` Participant.kind = "location"` verweist auf [geodata/](../geodata/index.md).
- `relatedTo` verbindet Task ↔ Event (Aufgabe „Protokoll schreiben“ hängt an Termin).

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

- **Zeitzone-Darstellung:** `timeZone`/`timeZones` vorhanden (✅); welche IANA-Version wir ausliefern, ist Betriebs-, nicht Datenentscheidung.
- Revision `draft-ietf-calext-jscalendarbis` (✅ gefunden, Inhalt ungelesen) beobachten: wird RFC 8984 obsolet machen.
