# Alert Dialog (Bestätigungsdialog) - Usage

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Application

Der Dialog erscheint aus einer Aktion heraus und hält sie zurück, bis entschieden ist.
Er wird einmal pro Programmfenster verwaltet, nicht pro Button.

## Examples

### Zerstörerische Aktion absichern

```jsx
<AlertDialog title="Seite verwerfen?" message="Änderungen gehen verloren."
             destructive={true} confirmLabel="Verwerfen" onConfirm={discard} />
```

### Bestätigung mit Tipp-Text

```jsx
<AlertDialog title="Wissensbereich löschen?" confirmWord="wiki-demo"
             confirmLabel="Endgültig löschen" onConfirm={remove} />
```

## Scenarios

| Szenario | Empfehlung |
| ---------- | ------------ |
| Aktion ist rückgängig machbar | kein Dialog, Toast mit Rückgängig |
| Objekt mit vielen Bezügen löschen | `destructive` + `confirmWord` |
| Formular mit Änderungen verlassen | Dialog mit drei Aktionen (Speichern, Verwerfen, Abbrechen) |
