# Time Picker (Zeitauswahl) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Die Auswahl erscheint beim Antippen des Zeitfeldes. Beginn und Ende eines Termins werden
gemeinsam betrachtet, damit das Ende nie vor dem Begin liegt.

## Beispiele

### Terminbeginn

```jsx
<TimePicker label="Beginn" value={start} step={15} onChange={setStart} />
```

### Belegte Zeiten ausblenden

```jsx
<TimePicker blocked={roomBookings} min="08:00" max="18:00" />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Termin anlegen | `step = 15`, Ende automatisch nachziehen |
| Zeiterfassung | `step = 6`, `freeInput = true` |
| Raumbuchung | `blocked` aus dem Kalender des Raums |
