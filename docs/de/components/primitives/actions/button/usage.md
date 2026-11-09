# Button – Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt ist, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Standard-Button

```jsx
<Button label="Save" variant="primary" onClick={save} />
```

## Variantenpaar in einem Dialog

```jsx
<Dialog title="Close page?">
  <Button label="Cancel" variant="secondary" onClick={close} />
  <Button label="Discard" variant="danger" onClick={discard} />
</Dialog>
```

## Icon-Button mit Beschriftung für Screenreader

```jsx
<Button icon="settings" iconOnly={true} aria-label="Open settings" />
```

## Ladezustand beim Speichern

```jsx
<Button label="Send" variant="primary" loading={sending} onClick={send} />
```

## Formular absenden

```jsx
<Form onSubmit={save}>
  <Button label="Save" type="submit" variant="primary" />
</Form>
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Ein Dokument speichern | ein `primary`, der Rest `secondary` |
| Zerstörerische Aktion | `danger` + Bestätigungsdialog |
| Werkzeugleiste mit vielen Aktionen | [button-group](../button-group/) statt einzelner Buttons |
| Zurück-Navigation | `link`, kein Button |
