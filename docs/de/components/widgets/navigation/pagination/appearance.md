# Pagination - Erscheinungsbild

## Grundlayout

Pagination ist eine Navigation für große Listen, die die Daten auf Seiten verteilt.

## Varianten

### Nummeriert

```
┌─────────────────────────────────────────┐
│ [◀] 1 2 3 4 5 [▶]                       │
└─────────────────────────────────────────┘
```

### Vor/Zurück

```
┌─────────────────────────────────────────┐
│ [◀ Zurück] [Weiter ▶]                   │
└─────────────────────────────────────────┘
```

### Mehr laden

```
┌─────────────────────────────────────────┐
│ [Mehr laden]                            │
└─────────────────────────────────────────┘
```

### Endloses Scrollen

```
┌─────────────────────────────────────────┐
│ (lädt beim Scrollen automatisch nach)   │
└─────────────────────────────────────────┘
```

## Größen

| Größe | Schriftgröße | Verwendung |
| ------- | ------------- | ------------ |
| Small | 12px | im Text |
| Medium | 14px | Standard |
| Large | 16px | hervorgehoben |

## Farben und Zustände

| Zustand | Farbe | Beschreibung |
| -------- | ------- | -------------- |
| **Aktiv** | Primärfarbe | aktuelle Seite |
| **Inaktiv** | Grau | inaktive Seiten |
| **Hover** | heller | Zustand beim Überfahren |
| **Deaktiviert** | Grau | deaktivierte Schaltflächen |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
| -------- | -------------- |
| `background` | die Seitenzahl erhält eine gefüllte Fläche |
| `ring` | Fokusring bei Tastaturnavigation |
| `underline` | Unterstreichung beim aktiven Eintrag |
| `none` | deaktivierte Pfeile ohne Rückmeldung |

## Responsiv

| Haltepunkt | Verhalten |
| ------------ | ----------- |
| Desktop (>768px) | die volle Pagination ist sichtbar |
| Tablet (480-768px) | kompakt |
| Mobil (<480px) | Vor/Zurück oder Mehr laden |

## Funktionen

- **Total Items**: Gesamtzahl der Einträge
- **Current Page**: aktuelle Seite
- **Items per Page**: Einträge pro Seite
- **Jump to Page**: direkt zu einer Seite springen
- **Page Size Selector**: Anzahl der Einträge pro Seite ändern
