# Toast - Erscheinungsbild

## Grundlayout
Ein Toast ist eine Benachrichtigung als Pop-up. Sie erscheint meist oben rechts.

```
┌─────────────────────────────────────────┐
│ [✕]  📢 Titel                           │
│      Beschreibungstext...               │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Farbe | Beschreibung |
|----------|-------|--------------|
| **info** | blau | Informationsmeldung |
| **success** | grün | Erfolgsmeldung |
| **warning** | orange/gelb | Warnmeldung |
| **error** | rot | Fehlermeldung |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 250px | kurze Meldungen |
| medium | 350px | Standard |
| large | 450px | lange Meldungen |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **info** | blau | Informationsmeldung |
| **success** | grün | Erfolgsmeldung |
| **warning** | orange | Warnmeldung |
| **error** | rot | Fehlermeldung |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|--------------|
| `shadow` | der Schatten wird stärker |
| `transform` | leichtes Anheben |

## Responsiv

Toasts stehen als Stapel in einer Bildschirmecke. Neue Meldungen gleiten mit `stagger`
darunter hinein. Beim Hover hält der Zähler für das automatische Schließen an (`paused`).
Wischen (`swipe`) entfernt die Meldung mit `fade-out`. Auf einer schmalen Fläche nimmt
der Toast die volle Breite ein und sitzt unten, damit er erreichbar bleibt.

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

## Position

| Position | Beschreibung |
|----------|--------------|
| **oben rechts** | Standard |
| **unten rechts** | unten rechts |
| **oben links** | oben links |
| **unten links** | unten links |
| **Mitte** | in der Mitte |

## Automatisches Schließen

```
┌─────────────────────────────────────────┐
│ [✕]  📢 Titel                           │
│      Beschreibungstext...               │
│      ━━━━━━━━━━━━━━━━━━━━━              │
└─────────────────────────────────────────┘
```
