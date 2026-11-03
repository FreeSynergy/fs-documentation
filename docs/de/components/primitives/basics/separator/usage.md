# Separator (Trennlinie) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Menügruppen trennen

```jsx
<Menu>
  <MenuItem label="Umbenennen" />
  <Separator />
  <MenuItem label="Archivieren" />
  <MenuItem label="Löschen" variant="danger" />
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
<Separator label="oder" />
<Button label="Neues Dokument" variant="primary" />
```

## Dekorative Linie unter einer Überschrift

```jsx
<Separator variant="dekorativ" />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Menü mit verschiedenen Aktionsarten | `horizontal`, Rolle `separator` |
| Zwei Seiten einer Detailansicht | `vertical` |
| Formularabschnitte | `horizontal` mit `spacing` 16 |
| Reine Optik ohne Struktur | `dekorativ` plus `aria-hidden` |
