# Floating Action Button (FAB) - Aussehen

## Grundlayout

Ein Floating Action Button (FAB) ist ein runder Hauptaktion-Button.

## Layout-Varianten

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

## Größe-Varianten

| Größe | Durchmesser | Verwendung |
|-------|-------------|------------|
| Standard | 56px | Hauptaktion |
| Mini | 40px | Sekundäre Aktion |
| Extended | Auto | Aktion mit Text |

## Farb-Varianten

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Primary** | Primärfarbe | Standard |
| **Secondary** | Sekundärfarbe | Sekundär |
| **Disabled** | Grau | Deaktiviert |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Vergrößerung (1.1x) |
| `shadow` | Schatten stärker |
| `ripple` | Welleneffekt bei Klick |

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
