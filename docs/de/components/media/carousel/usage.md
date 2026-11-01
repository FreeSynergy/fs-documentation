# Carousel (Karussell) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Eine Slideshow ist eine Bilder- oder Inhaltsschleife.

- Bildergalerien
- Produktpräsentationen
- Werbung
- Karussells

## Beispiele

### Bildergalerien

```jsx
<Carousel images={eintraege} autoplay={false} interval={5000} />
```

### Produktpräsentationen

```jsx
<Carousel images={eintraege} autoplay={false} loop={true} />
```

### Werbung

```jsx
<Carousel images={eintraege} autoplay={false} loop={true} />
```
