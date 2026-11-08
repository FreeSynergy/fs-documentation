# Alert – Erscheinungsbild

## Grundlayout
Ein Alert ist eine Statusmeldung (Info, Warnung, Fehler, Erfolg).

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

| Variante | Erscheinungsbild |
|---------|------------|
| **inline** | rahmenloser Bereich innerhalb des Inhalts, links ein Icon |
| **banner** | volle Breite über der Ansicht, abgesetzter Hintergrund, fixiert |

## Größen

| Größe | Breite | Verwendung |
|------|-------|-----|
| small | 200px | im Textfluss |
| medium | 400px | Standard |
| large | 600px | hervorgehoben |
| full | 100% | volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|--------|-------------|
| **info** | blau | Informationsmeldung |
| **success** | grün | Erfolgsmeldung |
| **warning** | orange | Warnung |
| **error** | rot | Fehlermeldung |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|-------------|
| `shadow` | der Schatten wird stärker |
| `border-left` | die Linie links leuchtet auf |

## Responsiv

Eine Inline-Meldung fließt mit dem Inhalt mit; die Banner-Variante bleibt oben
(`sticky`), während der Inhalt weiterscrollt. Beim Schließen schrumpft die Meldung auf
ihre Zeilenhöhe (`fade-out`, `collapse`), damit der restliche Inhalt nachrückt. Bei schmalen
Breiten stehen die Aktionen untereinander.

```css
.alert--banner { position: sticky; top: 0; z-index: 20; }
.alert-message { overflow-wrap: anywhere; }
.alert--dismissing { opacity: 0; max-height: 0; }   /* fade-out + collapse */

@media (max-width: 600px) {
  .alert-actions { flex-direction: column; }        /* actions stacked */
}
```

## Typen

| Typ | Farbe | Beschreibung |
|------|--------|-------------|
| `info` | blau | Informationsmeldung |
| `success` | grün | Erfolgsmeldung |
| `warning` | orange/gelb | Warnung |
| `error` | rot | Fehlermeldung |

## Schließbar

```
┌─────────────────────────────────────────┐
│ [✕]                                     │
│ 📢 Titel                                │
│ Beschreibungstext...                    │
└─────────────────────────────────────────┘
```
