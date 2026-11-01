# Drawer (Seitenleiste) - Aussehen

## Grundlayout
Ein Drawer ist ein seitliches Overlay-Fenster (einklappbar).

```
┌─────────────────────────────────────────┐
│  ┌───────────────────────────────────┐  │
│  │ [✕] Menü                        │  │
│  ├───────────────────────────────────┤  │
│  │                                   │  │
│  │   Inhalt                          │  │
│  │   ...                             │  │
│  │                                   │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

## Varianten

| Variant | Position | Beschreibung |
|---------|----------|--------------|
| **Left Drawer** | Links | Links |
| **Right Drawer** | Rechts | Rechts |
| **Bottom Drawer** | Unten | Unten |
| **Full Drawer** | Voll | Vollständig |

## Größen

| Größe | Breite/Höhe | Verwendung |
|-------|-------------|------------|
| Small | 200px | Wenige Elemente |
| Medium | 300px | Standard |
| Large | 400px | Viele Elemente |
| Full | 100% | Volle Breite/Höhe |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Background** | Hell | Hintergrund |
| **Header** | Hell | Titelzeile |
| **Overlay** | Dunkel | Hintergrund abdunkeln |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `shadow` | Schatten stärker |
| `border` | Rand leuchtet auf |

## Reaktiv

Der Drawer gleitet von der Kante herein (`slide-in`) und überdeckt den Inhalt mit
Schatten; auf breiter Fläche kann er dauerhaft offen stehen und teilt den Raum dann wie
[split-view](../../containers/split-view/). Auf schmaler Fläche wird der linke Drawer zum
Overlay mit Abblenden, der Bottom Drawer füllt höchstens 80 % der Höhe.

```css
.drawer { position: fixed; top: 0; bottom: 0; left: 0; width: 300px;
          transform: translateX(-100%); transition: transform 200ms; }
.drawer--open { transform: translateX(0); }
.scrim        { background: rgba(0,0,0,.4); }

@media (min-width: 1024px) {
  .drawer--permanent { position: static; transform: none; }   /* fest, ohne Overlay */
  .scrim { display: none; }
}
@media (max-width: 600px) {
  .drawer--bottom { max-height: 80vh; }                        /* Bottom Drawer */
}
```

## Overlay

```
┌─────────────────────────────────────────┐
│  ┌───────────────────────────────────┐  │
│  │ [✕] Menü                        │  │
│  │                                   │  │
│  │   Inhalt                          │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```
