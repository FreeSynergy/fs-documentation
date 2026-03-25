# Session

[← Zurück zum Index](../INDEX.md) | [Registry](registry.md) | [Repository-Übersicht](../architektur/repositories.md)

---

## Was ist eine Session?

Eine **Session** ist der aktive Kontext eines eingeloggten Benutzers. Sie verbindet alles was gerade läuft:

- Wer ist der User (user_id, display_name)
- Seit wann ist er eingeloggt
- Welche Programme sind offen und in welchem Zustand

**Repository:** `FreeSynergy/fs-session`

---

## Das Minimize-Problem (und wie Session es löst)

**Ohne Session:**
```
User minimiert fs-store → Desktop vergisst das Fenster
User klickt auf Icon  → Desktop startet fs-store NEU
Ergebnis: zwei Instanzen offen, State verloren
```

**Mit Session:**
```
User minimiert fs-store → Session setzt State auf Minimized
User klickt auf Icon  → Desktop fragt Session: "Ist fs-store offen?"
                       → Session: "Ja, Minimized"
                       → Desktop: Fenster restore (kein Neustart)
Ergebnis: eine Instanz, State erhalten
```

---

## Modell

```rust
Session {
    id:           String,          // UUID
    user_id:      String,
    display_name: String,
    started_at:   DateTime<Utc>,
    programs:     Vec<ProgramEntry>,
}

ProgramEntry {
    program_id: String,            // z.B. "fs-store"
    state:      ProgramState,      // Open | Minimized | Focused
    opened_at:  DateTime<Utc>,
}
```

---

## API

```rust
let store = SessionStore::open("fs-session.db").await?;

// Login
let session = store.create("user-42", "Alice").await?;

// Programm öffnen
store.open_program(session.id(), "fs-store").await?;

// Minimieren
store.minimize_program(session.id(), "fs-store").await?;

// Restore (kein Neustart)
store.restore_program(session.id(), "fs-store").await?;

// Logout
store.close(session.id()).await?;
```

---

## Abgrenzung

| | Session | Inventory |
|---|---|---|
| Frage | Wer ist eingeloggt + was läuft? | Was ist installiert? |
| Lebensdauer | Login bis Logout | Persistent |
| User-abhängig | Ja | Nein |
