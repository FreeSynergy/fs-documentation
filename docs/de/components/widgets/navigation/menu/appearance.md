# Menu - Erscheinungsbild

## Grundlayout

Ein Menü ist eine klickbare Menüleiste, oft oben platziert.

## Varianten

### Horizontal (Standard)

```
┌─────────────────────────────────────────┐
│ Start │ Über uns │ Leistungen │ Kontakt │
└─────────────────────────────────────────┘
```

### Vertikal (Seitenleiste)

```
┌─────────┐
│ Start   │
│ Über uns│
│ Leistung│
│ Kontakt │
└─────────┘
```

## Größen

| Größe | Höhe | Schriftgröße | Verwendung |
| ------- | ------ | ------------- | ------------ |
| Small | 32px | 12px | im Text |
| Medium | 48px | 14px | Standard |
| Large | 64px | 16px | hervorgehoben |

## Farben und Zustände

| Zustand | Farbe | Beschreibung |
| -------- | ------- | -------------- |
| **Aktiv** | Primärfarbe | aktiver Menüeintrag |
| **Inaktiv** | Grau | inaktive Menüeinträge |
| **Hover** | heller | Zustand beim Überfahren |
| **Deaktiviert** | ausgegraut | deaktivierte Menüeinträge |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
| -------- | -------------- |
| `color` | die Farbe wechselt |
| `background` | der Hintergrund wechselt |
| `border-bottom` | eine Unterstreichung erscheint |
| `shadow` | ein Schatten erscheint |

## Responsiv

| Haltepunkt | Verhalten |
| ------------ | ----------- |
| Desktop (>768px) | das ganze Menü ist sichtbar |
| Mobil (<480px) | Hamburger-Menü |

## Aufklappmenü

```
┌─────────────────────────────────────────┐
│ Start │ Über uns ▼ │ Leistungen ▼ │ Kontakt │
├─────────────────────────────────────────┤
│   Untermenü                             │
│   Untermenü 2                           │
└─────────────────────────────────────────┘
```
