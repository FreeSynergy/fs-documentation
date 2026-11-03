# Command (Befehlspalette) - Usage

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Application

Die Palette wird einmal pro Programmfenster angelegt und ist global über das Kürzel
erreichbar. Sie erhält die Befehle der aktuell aktiven Ansicht.

## Examples

### Palette im Programmfenster

```jsx
<Command commands={commands} hotkey="ctrl+k" onSelect={run} />
```

### Befehle aus einer Werkzeugleiste heraus öffnen

```jsx
<Command commands={viewCommands} open={paletteOpen} onClose={close} />
```

## Scenarios

| Szenario | Empfehlung |
| ---------- | ------------ |
| Desktop-Client | `hotkey = "ctrl+k"`, Palette zentriert |
| Mobile | `inline` in der Seitenleiste, kein Kürzel |
| Befehl nicht gefunden | Hinweis mit Vorschlägen statt leerer Liste |
