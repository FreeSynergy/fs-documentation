# Kbd (Tastenkennung) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Einzelne Taste

```jsx
<Kbd shortcut="Esc" />
```

## Kombination im Tooltip

```jsx
<Tooltip content={<>Speichern <Kbd keys={["Strg", "S"]} /></>} />
```

## Shortcut-Übersicht

```jsx
<Table>
  <Row action="Suche öffnen"><Kbd keys={["Strg", "K"]} /></Row>
  <Row action="Speichern"><Kbd keys={["Strg", "S"]} /></Row>
</Table>
```

## Gedrückten Zustand zeigen (Onboarding)

```jsx
<Kbd shortcut="Enter" active={userPressed} />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Tooltip mit Kürzel | `keys`-Kombination rechts im Text |
| Befehlspalette (`command`) | Kbd pro Kandidat in der Ergebnisliste |
| Mac-Varianten | `Cmd`/`Strg` je nach Plattform beschriften |
| Codiierter Inhalt | `code`, kein Kbd |
