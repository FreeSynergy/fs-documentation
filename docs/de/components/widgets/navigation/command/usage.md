# Command - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung zu Rust und Blinc wechselt,
    werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Die Palette wird einmal pro Programmfenster erzeugt und ist über das Tastenkürzel global erreichbar.
Sie erhält die Befehle der gerade aktiven Ansicht.

## Beispiele

### Palette im Programmfenster

```jsx
<Command commands={commands} hotkey="ctrl+k" onSelect={run} />
```

### Befehle aus einer Werkzeugleiste öffnen

```jsx
<Command commands={viewCommands} open={paletteOpen} onClose={close} />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Desktop-Client | `hotkey = "ctrl+k"`, Palette zentriert |
| Mobil | `inline` in der Seitenleiste, kein Tastenkürzel |
| Befehl nicht gefunden | Hinweis mit Vorschlägen statt einer leeren Liste |
