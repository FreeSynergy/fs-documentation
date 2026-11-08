# Carousel - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden die Beispiele in `usage.md` in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Eine Diashow ist eine Schleife aus Bildern oder Inhalten.

- Bildergalerien
- Produktpräsentationen
- Werbung
- Karussells

## Beispiele

### Bildergalerien

```jsx
<Carousel images={entries} autoplay={false} interval={5000} />
```

### Produktpräsentationen

```jsx
<Carousel images={entries} autoplay={false} loop={true} />
```

### Werbung

```jsx
<Carousel images={entries} autoplay={false} loop={true} />
```
