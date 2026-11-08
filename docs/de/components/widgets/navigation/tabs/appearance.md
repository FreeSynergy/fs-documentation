# Tabs - Erscheinungsbild

## Grundaufbau

Tabs (Reiter) dienen dazu, zwischen Ansichten zu wechseln. Sie können waagerecht oder senkrecht
angeordnet werden.

## Varianten
### Waagerecht (Standard)
```
┌─────────────────────────────────────────────────────┐
│ Reiter 1 │ Reiter 2 │ Reiter 3 │ Reiter 4          │
├─────────────────────────────────────────────────────┤
│                                                     │
│   Inhalt des aktiven Reiters                        │
│                                                     │
└─────────────────────────────────────────────────────┘
```
### Senkrecht (seitlich)
```
┌────────┬──────────────────────────────────────────┐
│ Reiter 1│                                          │
│ Reiter 2│   Inhalt des aktiven Reiters            │
│ Reiter 3│                                          │
│ Reiter 4│                                          │
└────────┴──────────────────────────────────────────┘
```

| Variante | Beschreibung | CSS |
| --------- | ------------- | ----- |
| **Default** | Standard-Reiter | `border-radius: 4px 4px 0 0` |
| **Pill** | Pillenform | `border-radius: 999px` |
| **Card** | In Karte integriert | `border-radius: 8px` |

## Größen

| Größe | Höhe | Verwendung |
| ------- | ------ | ------------ |
| Klein | 32px | Reiter in Textzeilen |
| Mittel | 48px | Standard-Reiter |
| Groß | 64px | hervorgehobene Reiter |

## Farben und Zustände

| Zustand | Farbe | Beschreibung |
| -------- | ------- | -------------- |
| **Aktiv** | Primärfarbe | aktiver Reiter |
| **Inaktiv** | Grau | inaktiver Reiter |
| **Hover** | heller | Hover-Zustand |
| **Deaktiviert** | ausgegraut | deaktivierte Reiter |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
| -------- | -------------- |
| `color` | die Farbe ändert sich |
| `border-bottom` | eine Unterstreichung erscheint |
| `scale` | leichte Vergrößerung |
| `shadow` | ein Schatten erscheint |

## Responsives Verhalten

| Breakpoint | Verhalten |
| ------------ | ----------- |
| Desktop (>768px) | alle Reiter sichtbar |
| Tablet (480–768px) | scrollbare Reiter |
| Mobil (<480px) | Drawer oder Akkordeon |

## Aktivitätsanzeige

```
┌─────────────────────────────────────────────────────┐
│ Reiter 1 │ Reiter 2 │ Reiter 3 │ Reiter 4          │
│ ━━━━━━━━                                            │
└─────────────────────────────────────────────────────┘
```

## Schließbare Reiter

```
┌─────────────────────────────────────────────────────┐
│ Reiter 1 ✕ │ Reiter 2 ✕ │ Reiter 3                 │
├─────────────────────────────────────────────────────┤
│                                                     │
└─────────────────────────────────────────────────────┘
```
