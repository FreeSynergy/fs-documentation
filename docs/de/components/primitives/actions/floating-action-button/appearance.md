# Floating Action Button (FAB) - Aussehen

## Grundlayout

Ein Floating Action Button (FAB) ist ein runder Hauptaktion-Button.

## Varianten

### Standard FAB (Groß)

```
                    ┌─────────┐
                    │   +     │
                    └─────────┘
```

### Mini FAB (Klein)

```
                    ┌──────┐
                    │  +   │
                    └──────┘
```

### Extended FAB (Mit Text)

```
                    ┌──────────────┐
                    │   +  Neu     │
                    └──────────────┘
```

## Größen

| Größe | Durchmesser | Verwendung |
|-------|-------------|------------|
| Standard | 56px | Hauptaktion |
| Mini | 40px | Sekundäre Aktion |
| Extended | Auto | Aktion mit Text |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Primary** | Primärfarbe | Standard |
| **Secondary** | Sekundärfarbe | Sekundär |
| **Disabled** | Grau | Deaktiviert |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Vergrößerung (1.1x) |
| `shadow` | Schatten stärker |
| `ripple` | Welleneffekt bei Klick |

## Reaktiv

Der FAB bleibt am Bildschirm verankert (`position: fixed`), damit die Hauptaktion auch beim
Scrollen erreichbar bleibt. Abwärts scrollen schiebt ihn aus dem Bild (`scroll-hidden`),
aufwärts scrollen holt ihn mit `pop-in` zurück; auf schmalen Flächen wird er zum Mini FAB.

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
  .fab { width: 40px; height: 40px; }   /* Mini FAB auf schmaler Fläche */
}
.fab--scroll-hidden { transform: translateY(80px); opacity: 0; }
```

## Positionierung

| Position | Beschreibung |
|----------|--------------|
| **Bottom Right** | Standard (rechts unten) |
| **Bottom Left** | Links unten (RTL-Sprachen) |
| **Center** | In der Mitte (selten) |
| **Fixed** | Fixiert am Bildschirm |

## Badge (Mit Anzahl/Status)

```
                    ┌─────────┐
                    │   +     │
                    │  (3)    │
                    └─────────┘
```
