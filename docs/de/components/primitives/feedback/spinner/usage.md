# Spinner - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung auf Rust und Blinc
    wechselt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Ladezustand in einem Bereich

```jsx
<Panel busy={loading}>
  {loading ? <Spinner text="Ansicht wird geladen…" /> : content}
</Panel>
```

## Ein kompakter Aktivitätshinweis in einer Leiste

```jsx
<Toolbar>
  <Spinner size="small" track={false} aria-label="Synchronisierung läuft" />
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
| Speichern, Antwort < 2 s | `loading` am [Button](../../actions/button/) |
| Laden einer Ansicht | `mit-text`, zentriert im Bereich |
| Synchronisation im Hintergrund | `small` in der Statusleiste |
| Dauer bekannt oder große Datenmenge | [progress](../progress/) statt Spinner |
