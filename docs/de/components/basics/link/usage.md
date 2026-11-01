# Link (Verweis) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Verweis auf ein Objekt

```jsx
<Link href="/crm/kontakt/4711">Kontakt Meier, Anna</Link>
```

## Externer Verweis

```jsx
<Link href="https://projekte.example.org/t/205" external={true} icon="external">
  Aufgabe 205
</Link>
```

## Download

```jsx
<Link href="/api/dateien/anhang.pdf" download="anhang.pdf">Anhang herunterladen</Link>
```

## Sprungmarke im Artikel

```jsx
<Link href="#kapitel-3" variant="muted">zu Kapitel 3</Link>
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Zwischen Objekten springen | `standard` |
| In Fließtext | `unterstrichen` |
| Webbrowse extern | `external` plus Icon |
| Aktion ohne Adresswechsel | [button](../../actions/button/), kein Link |
