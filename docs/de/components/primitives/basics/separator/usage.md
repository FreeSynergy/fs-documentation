# Separator – Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Implementierung auf Rust und
    Blinc umstellt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Menügruppen trennen

```jsx
<Menu>
  <MenuItem label="Rename" />
  <Separator />
  <MenuItem label="Archive" />
  <MenuItem label="Delete" variant="danger" />
</Menu>
```

## Werkzeuggruppen in einer Leiste

```jsx
<Toolbar>
  <ToolbarGroup items={formatItems} />
  <Separator orientation="vertical" />
  <ToolbarGroup items={alignItems} />
</Toolbar>
```

## Alternative mit Beschriftung

```jsx
<Separator label="or" />
<Button label="New document" variant="primary" />
```

## Dekorative Linie unter einer Überschrift

```jsx
<Separator variant="dekorativ" />
```

## Szenarien

| Szenario | Empfehlung |
|----------|----------------|
| Menü mit verschiedenen Aktionsarten | `horizontal`, Rolle `separator` |
| Zwei Seiten einer Detailansicht | `vertical` |
| Formularabschnitte | `horizontal` mit `spacing` 16 |
| Reines Aussehen ohne Struktur | `dekorativ` plus `aria-hidden` |
