# Alert Dialog - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung zu Rust und Blinc wechselt,
    werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Der Dialog erscheint aus einer Aktion heraus und hält sie zurück, bis eine Entscheidung fällt.
Er wird einmal pro Programmfenster verwaltet, nicht einmal pro Button.

## Beispiele

### Absicherung einer zerstörerischen Aktion

```jsx
<AlertDialog title="Seite verwerfen?" message="Änderungen gehen verloren."
             destructive={true} confirmLabel="Verwerfen" onConfirm={discard} />
```

### Bestätigung mit einem getippten Wort

```jsx
<AlertDialog title="Wissensbereich löschen?" confirmWord="wiki-demo"
             confirmLabel="Endgültig löschen" onConfirm={remove} />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Aktion kann rückgängig gemacht werden | kein Dialog, Toast mit Rückgängig |
| Löschen eines Objekts mit vielen Verweisen | `destructive` + `confirmWord` |
| Verlassen eines Formulars mit Änderungen | Dialog mit drei Aktionen (Speichern, Verwerfen, Abbrechen) |
