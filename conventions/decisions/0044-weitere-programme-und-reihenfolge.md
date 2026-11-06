# 0044 – Weitere Programme: Files, Kanban, Surveys, Gallery, Whiteboard, Streaming

Status: **Vorschlag** (2026-11-06), Entscheidungen des Nutzers stehen aus · ergänzt ADR 0017, 0018, 0037

## Kontext (Nutzer)
Nach den Groupware-Programmen sollen folgen: `fs-gallery`, allgemeine Dateien (evtl. mit RustFS),
`fs-whiteboard`, `fs-surveys`, `fs-kanban` samt Components; Streaming, wenn es nicht zu schwierig ist.
„Absolut wichtig“ sind Whiteboard, Surveys und Kanban. Die Doku muss immer zeigen, was wir tun und
wohin wir gehen (Transparenz).

## Vom Nutzer entschieden
- Die Programme kommen, auch `fs-kanban` und `fs-surveys` als eigene Programme.

## Vorschlag (offen)
1. **`fs-files`** kommt als Grundlage: Metadaten in `fs-store`, Bytes hinter der Schnittstelle `BlobStore`.
2. **RustFS** ist ein empfohlenes Server-Backend über S3, nicht die Maschine von `fs-files`: Es ist ein eigener
   Server, und jedes Programm muss allein laufen (ADR 0017). Dieselbe Rolle wie Stalwart in ADR 0018.
3. **Reihenfolge:** Files → Kanban → Surveys → Gallery → Whiteboard → Streaming. Kanban und Surveys können parallel
   zu Files laufen.
4. **Kanban:** Eine Karte ist ein JSCalendar-`Task`; `Task` zieht aus `fs-calendar-core` in eine gemeinsame Crate.
5. **Surveys:** zunächst drei Stufen (namentlich, anonym offen, anonym mit Token); die Grenze des Token-Modells
   wird offen gesagt. Verbindliche Wahlen gehören in die Demokratie-Suite.
6. **Whiteboard:** Abgleich je Objekt hinter einer Schnittstelle; CRDT nur, falls nötig.
7. **Streaming:** Stufe 1 (weiterleiten ohne Dekodieren) ist machbar. Stufe 2 (Enkodieren) verlangt eine Ausnahme von
   „100 % Rust“ oder nur AV1; Entscheidung, wenn Stufe 2 ansteht.

## Folgen
- Öffentlich: `docs/en/programs/apps/roadmap.md`, je Programm `design.md` und `requirements.md`,
  `docs/en/components/planned.md`.
- `files` und `surveys` haben noch keine analysierten Frontends; ihre Requirements sind vorläufig.
- Entscheidet der Nutzer, wird dieses ADR angepasst und die Seiten werden nachgezogen.
