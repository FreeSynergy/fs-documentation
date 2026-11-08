# Hover Card - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung zu Rust und Blinc wechselt,
    werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Die Karte hängt an einem Verweis. Sie öffnet sich nur, wenn der Zeiger ruhig auf dem
Auslöser liegt; der Inhalt kommt aus dem bereits geladenen Datensatz oder wird danach abgerufen.

## Beispiele

### Profilvorschau bei einem Namen

```jsx
<HoverCard target={user.id} variant="profil" placement="top" />
```

### Artikelauszug in einer Liste

```jsx
<HoverCard content={{ title, excerpt, updated }} openDelay={400} />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Name in einer Chat-Nachricht | `variant = "profil"`, `openDelay = 300` |
| Verweis in einer Tabelle | `variant = "dokument"`, `size = "small"` |
| Touch-Fläche | langes Drücken, Karte als untere Leiste |
