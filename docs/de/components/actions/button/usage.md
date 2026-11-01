# Button (Schaltfläche) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Standardschaltfläche

```jsx
<Button label="Speichern" variant="primary" onClick={save} />
```

## Variantenduo in einem Dialog

```jsx
<Dialog title="Seite schließen?">
  <Button label="Abbrechen" variant="secondary" onClick={close} />
  <Button label="Verwerfen" variant="danger" onClick={discard} />
</Dialog>
```

## Icon-Button mit Beschriftung für Screenreader

```jsx
<Button icon="settings" iconOnly={true} aria-label="Einstellungen öffnen" />
```

## Ladezustand beim Speichern

```jsx
<Button label="Senden" variant="primary" loading={sending} onClick={send} />
```

## Formular absenden

```jsx
<Form onSubmit={save}>
  <Button label="Speichern" type="submit" variant="primary" />
</Form>
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Dokument speichern | ein `primary`, Rest `secondary` |
| Zerstörerische Aktion | `danger` + Bestätigungsdialog |
| Werkzeugleiste mit vielen Aktionen | [button-group](../button-group/) statt Einzelbuttons |
| Zurück-Navigation | `link`, kein Button |
