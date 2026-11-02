# Termine – Beschreibung

**Was diese Domäne ist:** Kalendereinträge, wiederkehrende Serien, Teilnehmer mit Einladungs-Status — und **Aufgaben**. Kanonisches Modell: **JSCalendar** (RFC 8984, ✅), dessen Objekttypen `Event` **und** `Task` wir beide hier verwalten (Beschluss 1).

**Was sie abdeckt:**

- `Event` mit `start`, `duration`, `status`, `freeBusyStatus`, `privacy`
- Serien über `recurrenceRules` / `recurrenceOverrides` (Regelwerk wie iCalendar-`RRULE`)
- Teilnehmer (`participants`) mit `roles`, `participationStatus`, `scheduleAgent`
- Einladungsfluss (Anfrage/Antwort/Zurückziehen) über iTIP (RFC 5546, ✅)
- `Task` mit `due`, `start`, `percentComplete`, `progress` — auch für [projects/](../projects/index.md)
- Weckrufe/Erinnerungen (`alerts`, RFC 9074, ✅), Rich-Text-Beschreibungen (RFC 9073, ✅)

**Abgrenzung zu anderen Domänen:**

| Thema | Wo es liegt | Warum |
|-------|-------------|-------|
| Board-/Listen-/Beziehungsstruktur | [projects/](../projects/index.md) | projects ergänzt nur Struktur um die Task-Objekte **dieser** Domäne |
| Personen/Organisationen der Teilnehmer | [contacts/](../contacts/index.md) | JSCalendar-`Participant` ist eine **Termin-Kopie** mit `sendTo`/`email` als Brücke |
| Orte | [geodata/](../geodata/index.md) | Termin referenziert Orte nur (`locations`) |
| Chat-Absprachen zur Einladung | [messages/](../messages/index.md) | iTIP-Antworten sind Protokollnachrichten, keine Chat-Beiträge |

**Keine separate `aufgaben/`-Domäne:** solange JSCalendar-`Task` ausreicht, leben Aufgaben hier (siehe [index.md](index.md)).
