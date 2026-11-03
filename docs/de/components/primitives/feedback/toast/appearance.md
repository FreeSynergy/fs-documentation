# Toast - Aussehen

## Grundlayout
Ein Toast ist eine Pop-up-Benachrichtigung, die meist oben rechts erscheint.

```
┌─────────────────────────────────────────┐
│ [✕]  📢 Titel                           │
│      Beschreibungstext...               │
└─────────────────────────────────────────┘
```

## Varianten

| Variant | Farbe | Beschreibung |
|---------|-------|--------------|
| **Info** | Blau | Informationsmeldung |
| **Success** | Grün | Erfolgsmeldung |
| **Warning** | Orange/Gelb | Warnmeldung |
| **Error** | Rot | Fehlermeldung |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 250px | Kurze Nachrichten |
| Medium | 350px | Standard |
| Large | 450px | Lange Nachrichten |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Info** | Blau | Informationsmeldung |
| **Success** | Grün | Erfolgsmeldung |
| **Warning** | Orange | Warnmeldung |
| **Error** | Rot | Fehlermeldung |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `shadow` | Schatten stärker |
| `transform` | Leichte Hebung |

## Reaktiv

Toasts stehen in einem Stapel an einer Bildecke; neue Meldungen rutschen mit `stagger` darunter.
Überfahren pausiert den Auto-Dismiss-Zähler (`paused`), Wegwischen (`swipe`) entfernt die
Meldung mit `fade-out`. Auf schmaler Fläche nimmt der Toast die ganze Breite ein und sitzt
unten, damit er erreichbar bleibt.

```css
.toast-stack { position: fixed; top: 16px; right: 16px; display: flex;
               flex-direction: column; gap: 8px; z-index: 40; }
.toast           { animation: slide-in 200ms; }
.toast--leaving  { animation: fade-out 150ms forwards; }

@media (max-width: 600px) {
  .toast-stack { left: 0; right: 0; top: auto; bottom: 0; }
  .toast { width: 100%; }
}
```

## Positionierung

| Position | Beschreibung |
|----------|--------------|
| **Top Right** | Oben rechts (Standard) |
| **Bottom Right** | Unten rechts |
| **Top Left** | Oben links |
| **Bottom Left** | Unten links |
| **Center** | In der Mitte |

## Auto-Dismiss

```
┌─────────────────────────────────────────┐
│ [✕]  📢 Titel                           │
│      Beschreibungstext...               │
│      ━━━━━━━━━━━━━━━━━━━━━              │
└─────────────────────────────────────────┘
```
