# Floating Action Button (FAB) – Aussehen

## Grundlayout

Ein Floating Action Button (FAB) ist ein runder Hauptaktions-Button.

## Varianten

### Standard-FAB (groß)

```
                    ┌─────────┐
                    │   +     │
                    └─────────┘
```

### Mini-FAB (klein)

```
                    ┌──────┐
                    │  +   │
                    └──────┘
```

### Erweiterter FAB (mit Text)

```
                    ┌──────────────┐
                    │   +  New     │
                    └──────────────┘
```

## Größen

| Größe | Durchmesser | Verwendung |
|-------|-------------|------------|
| Standard | 56px | Hauptaktion |
| Mini | 40px | Nebenaktion |
| Erweitert | auto | Aktion mit Text |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **primary** | Primärfarbe | Standard |
| **secondary** | Sekundärfarbe | Nebenaktion |
| **disabled** | grau | deaktiviert |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Vergrößerung (1,1-fach) |
| `shadow` | Schatten wird stärker |
| `ripple` | Welleneffekt beim Klicken |

## Responsiv

Der FAB bleibt am Bildschirm verankert (`position: fixed`), damit die Hauptaktion beim Scrollen
erreichbar bleibt. Beim Scrollen nach unten verschwindet er aus dem Bild (`scroll-hidden`),
beim Scrollen nach oben kommt er mit `pop-in` zurück; auf schmalen Flächen wird er zum Mini-FAB.

```css
.fab {
  position: fixed;
  right: 16px;
  bottom: 16px;
  width: 56px;
  height: 56px;
  box-shadow: 0 3px 5px rgba(0,0,0,0.2);
  transition: transform 150ms, box-shadow 150ms;
}
.fab:hover  { transform: scale(1.1); box-shadow: 0 6px 10px rgba(0,0,0,0.25); }
.fab:active { transform: scale(0.96); }

@media (max-width: 600px) {
  .fab { width: 40px; height: 40px; }   /* mini FAB on a narrow surface */
}
.fab--scroll-hidden { transform: translateY(80px); opacity: 0; }
```

## Position

| Position | Beschreibung |
|----------|--------------|
| **unten rechts** | Standard |
| **unten links** | unten links (RTL-Sprachen) |
| **Mitte** | in der Mitte (selten) |
| **fixed** | am Bildschirm fixiert |

## Badge (mit Anzahl/Status)

```
                    ┌─────────┐
                    │   +     │
                    │  (3)    │
                    └─────────┘
```
