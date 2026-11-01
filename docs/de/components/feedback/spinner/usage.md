# Spinner (Ladeanzeige) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Ladezustand in einem Bereich

```jsx
<Panel busy={loading}>
  {loading ? <Spinner text="Ansicht wird geladen…" /> : content}
</Panel>
```

## Kompakter Aktivitätshinweis in einer Leiste

```jsx
<Toolbar>
  <Spinner size="small" track={false} aria-label="Synchronisation läuft" />
</Toolbar>
```

## In einem Feld (während der Prüfung)

```jsx
<TextInput
  value={login}
  trailing={<Spinner size="small" inline={true} />}
/>
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Speichern, Antwort < 2 s | `loading` am [button](../../actions/button/) |
| Laden einer Ansicht | `mit-text` mittig im Bereich |
| Synchronisation im Hintergrund | `small` in der Statuszeile |
| Dauer bekannt / große Datenmenge | [progress](../progress/) statt Spinner |
