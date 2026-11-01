# Label (Beschriftung) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Feld beschriften

```jsx
<Label for="username">Benutzername</Label>
<TextInput id="username" />
```

## Pflichtfeld

```jsx
<Label for="email" required={true}>E-Mail</Label>
```

## Zugrifftaste

```jsx
<Label for="save" shortcut="S">Speichern</Label>
```

## Verstecktes Label für Screenreader

```jsx
<SearchInput>
  <Label hidden={true}>Suchbegriff eingeben</Label>
</SearchInput>
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Formularfeld | Label zusammen mit [field](../../fields/field/) |
| Icon-only-Button | `aria-label` am Button, kein Label-Element |
| Gruppe von Feldern | sichtbare Gruppenüberschrift, kein Einzellabel |
| Platzhalter als Ersatz | nicht zulässig |
