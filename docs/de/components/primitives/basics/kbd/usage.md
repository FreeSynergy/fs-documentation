# Kbd – Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Implementierung auf Rust und
    Blinc umstellt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Einzelne Taste

```jsx
<Kbd shortcut="Esc" />
```

## Kombination in einem Tooltip

```jsx
<Tooltip content={<>Save <Kbd keys={["Ctrl", "S"]} /></>} />
```

## Tastenkürzel-Übersicht

```jsx
<Table>
  <Row action="Open search"><Kbd keys={["Ctrl", "K"]} /></Row>
  <Row action="Save"><Kbd keys={["Ctrl", "S"]} /></Row>
</Table>
```

## Gedrückt-Zustand anzeigen (Einführung)

```jsx
<Kbd shortcut="Enter" active={userPressed} />
```

## Szenarien

| Szenario | Empfehlung |
|----------|----------------|
| Tooltip mit Tastenkürzel | `keys`-Kombination rechts neben dem Text |
| Befehlspalette (`command`) | kbd je Treffer in der Ergebnisliste |
| Mac-Varianten | Beschriftung `Cmd`/`Ctrl` je nach Plattform |
| Code-Inhalte | `code`, nicht kbd |
