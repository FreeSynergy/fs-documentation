# Alert - Aussehen

## Grundlayout
Ein Alert ist eine Status-Meldung (Info, Warning, Error, Success).

```
┌─────────────────────────────────────────┐
│ [✕]                                     │
│ 📢 Titel                                │
│ Beschreibungstext...                    │
│                                         │
│ [Aktion]                                │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **inline** | Rahmenlose Fläche im Inhalt, links ein Icon |
| **banner** | volle Breite über der Ansicht, abgesetzter Hintergrund, fixiert |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 200px | Inline |
| Medium | 400px | Standard |
| Large | 600px | Featured |
| Full | 100% | Volle Breite |

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
| `border-left` | Linie leuchtet auf |

## Reaktiv

Eine inline-Meldung fließt mit dem Inhalt mit; die banner-Variante bleibt oben stehen
(`sticky`), während der Inhalt weiterläuft. Beim Schließen schrumpft die Meldung auf ihre
Linienhöhe (`fade-out`, `collapse`), damit der restliche Inhalt nachrückt. Bei schmaler
Breite stapeln sich die Aktionen untereinander.

```css
.alert--banner { position: sticky; top: 0; z-index: 20; }
.alert-message { overflow-wrap: anywhere; }
.alert--dismissing { opacity: 0; max-height: 0; }   /* fade-out + collapse */

@media (max-width: 600px) {
  .alert-actions { flex-direction: column; }        /* Aktionen untereinander */
}
```

## Typen

| Typ | Farbe | Beschreibung |
|-----|-------|--------------|
| `info` | Blau | Informationsmeldung |
| `success` | Grün | Erfolgsmeldung |
| `warning` | Orange/Gelb | Warnmeldung |
| `error` | Rot | Fehlermeldung |

## Dismissible

```
┌─────────────────────────────────────────┐
│ [✕]                                     │
│ 📢 Titel                                │
│ Beschreibungstext...                    │
└─────────────────────────────────────────┘
```
