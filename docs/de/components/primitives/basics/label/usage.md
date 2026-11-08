# Label – Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Implementierung auf Rust und
    Blinc umstellt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Ein Feld beschriften

```jsx
<Label for="username">Username</Label>
<TextInput id="username" />
```

## Pflichtfeld

```jsx
<Label for="email" required={true}>Email</Label>
```

## Zugriffstaste

```jsx
<Label for="save" shortcut="S">Save</Label>
```

## Versteckte Beschriftung für Screenreader

```jsx
<SearchInput>
  <Label hidden={true}>Enter a search term</Label>
</SearchInput>
```

## Szenarien

| Szenario | Empfehlung |
|----------|----------------|
| Formularfeld | Label zusammen mit [field](../../fields/field/) |
| Button nur mit Icon | `aria-label` am Button, kein Label-Element |
| Feldgruppe | eine sichtbare Gruppenüberschrift, keine einzelnen Labels |
| Platzhalter als Ersatz | nicht erlaubt |
