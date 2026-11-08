# Drawer - Erscheinungsbild

## Grundlayout
Ein Drawer ist ein seitliches Overlay-Fenster (einklappbar).

```
┌─────────────────────────────────────────┐
│  ┌───────────────────────────────────┐  │
│  │ [✕] Menü                          │  │
│  ├───────────────────────────────────┤  │
│  │                                   │  │
│  │   Inhalt                          │  │
│  │   ...                             │  │
│  │                                   │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Position | Beschreibung |
|---------------|----------|--------------|
| **Left Drawer** | links | links |
| **Right Drawer** | rechts | rechts |
| **Bottom Drawer** | unten | unten |
| **Full Drawer** | vollständig | Vollbild |

## Größen

| Größe | Breite/Höhe | Verwendung |
| ------- | ------------- | ------------ |
| Small | 200px | wenige Einträge |
| Medium | 300px | Standard |
| Large | 400px | viele Einträge |
| Full | 100% | volle Breite/Höhe |

## Farben und Zustände

| Zustand | Farbe | Beschreibung |
| -------- | ------- | -------------- |
| **Hintergrund** | hell | Hintergrund |
| **Kopfbereich** | hell | Titelleiste |
| **Overlay** | dunkel | Hintergrund abdunkeln |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
| -------- | -------------- |
| `shadow` | stärkerer Schatten |
| `border` | der Rahmen leuchtet auf |

## Responsiv

Der Drawer gleitet vom Rand herein (`slide-in`) und legt sich mit einem Schatten über den Inhalt;
auf einer breiten Fläche kann er dauerhaft offen bleiben und teilt dann den Platz wie
[split-view](../../containers/split-view/). Auf einer schmalen Fläche wird der linke Drawer zu einem
Overlay mit Abdunkelung, der untere Drawer füllt höchstens 80 % der Höhe.

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
  .drawer--bottom { max-height: 80vh; }                        /* unterer Drawer */
}
```

## Overlay

```
┌─────────────────────────────────────────┐
│  ┌───────────────────────────────────┐  │
│  │ [✕] Menü                          │  │
│  │                                   │  │
│  │   Inhalt                          │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```
