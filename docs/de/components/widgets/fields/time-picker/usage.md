# Time Picker - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung zu Rust und Blinc wechselt,
    werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Die Auswahl erscheint beim Antippen des Uhrzeitfelds. Beginn und Ende eines Termins
werden gemeinsam betrachtet, damit das Ende nie vor dem Beginn liegt.

## Beispiele

### Beginn eines Termins

```jsx
<TimePicker label="Start" value={start} step={15} onChange={setStart} />
```

### Belegte Uhrzeiten ausblenden

```jsx
<TimePicker blocked={roomBookings} min="08:00" max="18:00" />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Termin anlegen | `step = 15`, Ende automatisch mitziehen |
| Zeiterfassung | `step = 6`, `freeInput = true` |
| Raumbuchung | `blocked` aus dem Kalender des Raums |
