# Link – Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Implementierung auf Rust und
    Blinc umstellt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Verweis auf ein Objekt

```jsx
<Link href="/crm/contact/4711">Contact Meier, Anna</Link>
```

## Externer Verweis

```jsx
<Link href="https://projects.example.org/t/205" external={true} icon="external">
  Task 205
</Link>
```

## Download

```jsx
<Link href="/api/files/attachment.pdf" download="attachment.pdf">Download attachment</Link>
```

## Sprungmarke in einem Artikel

```jsx
<Link href="#chapter-3" variant="muted">to chapter 3</Link>
```

## Szenarien

| Szenario | Empfehlung |
|----------|----------------|
| Springen zwischen Objekten | `standard` |
| Im Fließtext | `unterstrichen` |
| Extern im Webbrowser | `external` plus ein Icon |
| Aktion ohne Adressänderung | [button](../../actions/button/), kein Link |
