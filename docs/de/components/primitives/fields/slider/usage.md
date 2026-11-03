# Slider (Schieberegler) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein Slider ist ein Wertebereich mit Schieberegler.

- Lautstärke
- Bewertung
- Einstellungen

## Beispiele

### Lautstärke

```jsx
<Slider onChange={aktion} />
```

### Bewertung

```jsx
<Slider onChange={aktion} min={0} />
```

### Einstellungen

```jsx
<Slider onChange={aktion} max={100} />
```
